"""Build the licensed wood backdrop and fixed log silhouette for flame resizing.

Uses the same development dependencies as render/linear-gas/requirements.txt.
This does not change the source video or run in the Android application.
"""

from pathlib import Path
import subprocess
import numpy as np
from PIL import Image

root = Path(__file__).resolve().parents[2]
width, height = 1920, 1080
decoder = subprocess.Popen(
    [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-threads", "1",
        "-i", str(root / "res/raw/wood.mp4"), "-vf", "fps=4", "-threads", "1",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "pipe:1",
    ],
    stdout=subprocess.PIPE,
)
minimum = None
try:
    while True:
        data = decoder.stdout.read(width * height * 3)
        if not data:
            break
        if len(data) != width * height * 3:
            raise RuntimeError("Incomplete source frame")
        frame = np.frombuffer(data, dtype=np.uint8).reshape(height, width, 3)
        minimum = frame.copy() if minimum is None else np.minimum(minimum, frame)
finally:
    decoder.stdout.close()
    if decoder.wait() != 0:
        raise RuntimeError("Could not decode the bundled wood video")
if minimum is None:
    raise RuntimeError("The bundled wood video contains no frames")

width, height = 960, 540
background = np.asarray(
    Image.fromarray(minimum).resize((width, height), Image.Resampling.LANCZOS)
)
# The alpha channel stores each column's log-top height, not transparency.
anchor = np.interp(
    np.arange(width),
    [0, 150, 250, 340, 435, 490, 600, 740, 850, 959],
    [510, 490, 450, 405, 360, 404, 420, 440, 485, 515],
)
alpha = np.tile(np.rint(anchor / height * 255).astype(np.uint8), (height, 1))
output = root / "assets/wood-background.png"
Image.fromarray(np.dstack([background, alpha]), "RGBA").save(output)
print(output)
