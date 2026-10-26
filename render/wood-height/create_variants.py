"""Bake discrete wood flame heights without changing the fixed logs or surround.

Uses the credited original 1080p30 video and temporal backdrop produced by
create_background.py. Runtime playback needs no flame-extraction shader.
"""
from pathlib import Path
import subprocess

import cv2
import numpy as np
from PIL import Image

cv2.setNumThreads(1)
root = Path(__file__).resolve().parents[2]
width, height = 1920, 1080
background = np.asarray(Image.open(root / "assets/wood-background.png"))
background = cv2.resize(background, (width, height), interpolation=cv2.INTER_LINEAR)
background_rgb = background[:, :, :3].astype(np.float32) / 255
background_linear = background_rgb ** 2.2
anchors = background[:, :, 3].astype(np.float32) / 255 * height
xx, yy = np.meshgrid(np.arange(width, dtype=np.float32), np.arange(height, dtype=np.float32))
variants = {}
for name, scale in [("small", .65), ("large", 1.3)]:
    sample_y = anchors + (yy - anchors) / scale
    sampled_background = cv2.remap(background_rgb, xx, sample_y, cv2.INTER_LINEAR,
                                  borderMode=cv2.BORDER_REPLICATE)
    variants[name] = (sample_y, sampled_background ** 2.2)
fade = np.clip((anchors - yy) / (height * .033333), 0, 1)[:, :, None]
reader = subprocess.Popen([
    "ffmpeg", "-v", "error", "-threads", "1", "-i", str(root / "res/raw/wood.mp4"),
    "-threads", "1", "-f", "rawvideo", "-pix_fmt", "rgb24", "pipe:1",
], stdout=subprocess.PIPE)
writers = {}
for name in variants:
    writers[name] = subprocess.Popen([
        "ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
        "-s", f"{width}x{height}", "-r", "30", "-i", "pipe:0", "-an",
        "-c:v", "libx264", "-threads", "2", "-preset", "medium", "-crf", "16",
        "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.1",
        "-movflags", "+faststart", str(root / f"res/raw/wood_{name}.mp4"),
    ], stdin=subprocess.PIPE)
frames = 0
try:
    while True:
        data = reader.stdout.read(width * height * 3)
        if not data:
            break
        if len(data) != width * height * 3:
            raise RuntimeError("Incomplete source frame")
        original = np.frombuffer(data, np.uint8).reshape(height, width, 3).astype(np.float32) / 255
        for name, (sample_y, sampled_background) in variants.items():
            recorded = cv2.remap(original, xx, sample_y, cv2.INTER_LINEAR,
                                 borderMode=cv2.BORDER_CONSTANT)
            emission = np.maximum(recorded ** 2.2 - sampled_background, 0)
            gate = np.clip((recorded[:, :, 1] - .08) / .16, 0, 1)
            gate = gate * gate * (3 - 2 * gate)
            # Exclude red brick reflections while retaining gold flame emission.
            ratio = recorded[:, :, 1] / np.maximum(recorded[:, :, 0], .01)
            chroma = np.clip((ratio - .28) / .22, 0, 1)
            gate *= chroma * chroma * (3 - 2 * chroma)
            emission *= gate[:, :, None]
            adjusted = np.clip(background_linear + emission, 0, 1) ** (1 / 2.2)
            result = original * (1 - fade) + adjusted * fade
            writers[name].stdin.write(np.rint(np.clip(result, 0, 1) * 255).astype(np.uint8).tobytes())
        frames += 1
        if frames % 60 == 0:
            print(f"Encoded {frames} source frames", flush=True)
finally:
    reader.stdout.close()
    reader_code = reader.wait()
    codes = []
    for writer in writers.values():
        writer.stdin.close()
        codes.append(writer.wait())
    if reader_code or any(codes):
        raise RuntimeError("Could not encode the wood height variants")
if not frames:
    raise RuntimeError("The wood source is empty")
print(f"Completed {frames} frames at 1920x1080/30 for each height", flush=True)
