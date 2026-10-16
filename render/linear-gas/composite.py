"""Composite licensed moving flame emission over the original modern burner.

Render-only dependencies: numpy, opencv-python-headless, Pillow and FFmpeg.
The Android app has none of these dependencies. Output stays in build/ until
its moving and native quality checks pass.
"""

from pathlib import Path
import argparse
import hashlib
import subprocess
import cv2
import numpy as np
from PIL import Image

cv2.setNumThreads(1)
root = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument("--seconds", type=float, default=20)
parser.add_argument("--output", default="linear-composite")
args = parser.parse_args()
if args.seconds < 2:
    parser.error("--seconds must be at least 2")
fps = 30
count = round(args.seconds * fps)
blend = min(30, count // 4)
out = root / "build" / args.output
out.mkdir(parents=True, exist_ok=True)
background = (
    np.asarray(
        Image.open(root / "render/linear-gas/burner-bed.png").convert("RGB"),
        dtype=np.float32,
    )
    / 255
)
background = background**2.2
source = root / "res/raw/wood.mp4"

source_hash = hashlib.sha256(source.read_bytes()).hexdigest()[:12]
cache = root / "build" / f"wood-background-{source_hash}.npy"
if not cache.exists():
    decoder = subprocess.Popen(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-threads",
            "1",
            "-i",
            str(source),
            "-vf",
            "fps=4",
            "-threads",
            "1",
            "-f",
            "rawvideo",
            "-pix_fmt",
            "rgb24",
            "pipe:1",
        ],
        stdout=subprocess.PIPE,
    )
    minimum = None
    while True:
        data = decoder.stdout.read(1920 * 1080 * 3)
        if len(data) != 1920 * 1080 * 3:
            break
        frame = np.frombuffer(data, dtype=np.uint8).reshape(1080, 1920, 3)
        minimum = frame.copy() if minimum is None else np.minimum(minimum, frame)
    decoder.stdout.close()
    if decoder.wait() != 0 or minimum is None:
        raise RuntimeError("Cannot decode wood source")
    np.save(cache, minimum.astype(np.float32) / 255)
baseline = np.load(cache)[140:820, 400:1500]
baseline = cv2.resize(baseline, (520, 320), interpolation=cv2.INTER_AREA)
static = cv2.GaussianBlur((baseline**2.2)[:, :, 1], (0, 0), 2)
processes = []
for start in [2.1, 7.7, 14.3, 22.6]:
    command = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-threads",
        "1",
        "-stream_loop",
        "-1",
        "-ss",
        str(start),
        "-i",
        str(source),
        "-t",
        str(args.seconds),
        "-vf",
        "crop=1100:680:400:140,fps=30,scale=520:320",
        "-threads",
        "1",
        "-f",
        "rawvideo",
        "-pix_fmt",
        "rgb24",
        "pipe:1",
    ]
    processes.append(subprocess.Popen(command, stdout=subprocess.PIPE))
encoder = subprocess.Popen(
    [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-f",
        "rawvideo",
        "-pix_fmt",
        "rgb24",
        "-s",
        "1920x540",
        "-r",
        "30",
        "-i",
        "pipe:0",
        "-an",
        "-c:v",
        "libx264",
        "-threads",
        "1",
        "-preset",
        "fast",
        "-profile:v",
        "high",
        "-level",
        "4.0",
        "-crf",
        "17",
        "-pix_fmt",
        "yuv420p",
        "-movflags",
        "+faststart",
        "-y",
        str(out.with_suffix(".mp4")),
    ],
    stdin=subprocess.PIPE,
)
fade = np.ones((320, 520), np.float32)
fade[:14] *= np.linspace(0, 1, 14)[:, None]
fade[-6:] *= np.linspace(1, 0, 6)[:, None]
fade[:, :38] *= np.linspace(0, 1, 38)[None, :]
fade[:, -38:] *= np.linspace(1, 0, 38)[None, :]
try:
    for number in range(count):
        canvas = background.copy()
        for p, left in zip(processes, [0, 467, 934, 1400]):
            data = p.stdout.read(520 * 320 * 3)
            if len(data) != 520 * 320 * 3:
                raise RuntimeError(f"Source ended at {number}")
            clean = (
                np.frombuffer(data, dtype=np.uint8)
                .reshape(320, 520, 3)
                .astype(np.float32)
                / 255
            )
            radiance = clean**2.2
            value = radiance[:, :, 1]
            opacity = np.maximum(value - static * 1.4, 0) / (value + 0.00001)
            emission = radiance * opacity[:, :, None]
            emission *= np.clip((clean[:, :, 1] - 0.08) / 0.52, 0, 1)[:, :, None] ** 2
            emission *= fade[:, :, None]
            canvas[126:446, left : left + 520] += emission * 0.95
        if number < blend:
            np.save(out / f"opening-{number:04}.npy", canvas)
        else:
            if number >= count - blend:
                weight = (number - (count - blend) + 1) / blend
                opening = np.load(out / f"opening-{number-(count-blend):04}.npy")
                canvas = canvas * (1 - weight) + opening * weight
            image = (np.clip(canvas, 0, 1) ** (1 / 2.2) * 255).astype(np.uint8)
            encoder.stdin.write(image.tobytes())
        if number in [0, 30, count // 2, count - 1]:
            Image.fromarray(
                (np.clip(canvas, 0, 1) ** (1 / 2.2) * 255).astype(np.uint8)
            ).save(out / f"proof-{number:04}.png")
        if number % 60 == 0:
            print("FRAME", number, flush=True)
finally:
    try:
        encoder.stdin.close()
    finally:
        encoder_result = encoder.wait()
        for p in processes:
            p.stdout.close()
            p.terminate()
            p.wait()
if encoder_result != 0:
    raise RuntimeError("Cannot encode linear scene")
print(out.with_suffix(".mp4"), flush=True)
