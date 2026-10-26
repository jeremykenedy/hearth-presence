# Media provenance

The two original videos were visually inspected across their full duration.
Neither contains a watermark, logo or text. Both show real moving fire.
The original wood video is preserved in media/source/wood-fire.webm.
The 156 MB original gas source is not committed; its source page links the original.

| Asset | Author | Source | License | Changes |
|---|---|---|---|---|
| wood.mp4 | free video library | [Commons source](https://commons.wikimedia.org/wiki/File:Fantastic-fireplace-fire-chimney-hearth-_background_-_texture_-_motion_graphics_-_free_video_library.webm) | CC BY 3.0 | Original 1920x1080, slight desaturation, H.264, blend loop boundary |
| gas.mp4 | FASTILY | [Commons source](https://commons.wikimedia.org/wiki/File:Fireplace_1_2021-02-14.webm) | CC BY-SA 4.0 | Original 3840x2160, crop 3840x1780 at 0,380, encode 1920x890 at 30 fps, denoise, H.264 High Level 4.0 |
| linear.mp4 | free video library and Jeremy Kenedy | Same wood source; original rendered burner bed | CC BY 3.0 footage; Apache-2.0 original bed | Isolated recorded flame emission, four independent source offsets, additive compositing, 19-second loop with one-second boundary blend, 1920x540 at 30 fps, H.264 High Level 4.0 |
| crackle.m4a | Original | scripts/generate-crackle.py | Apache-2.0 | Synthesis, AAC encoding |

The wood source was verified through its Commons source license record,
which preserves CC BY 3.0 and the original author's attribution. It is not
licensed under the application's Apache license. The gas adaptation and
composites containing it remain CC BY-SA 4.0. Screenshots retain these credits.

- Wood license: https://creativecommons.org/licenses/by/3.0/
- Gas license: https://creativecommons.org/licenses/by-sa/4.0/

Material textures are photographed Poly Haven assets under CC0-1.0: red_brick,
white_plaster_02, wood_floor, slate_floor and marble_01. Original 1K diffuse and
OpenGL normal maps are bundled unchanged. Exact source URLs and SHA-256 hashes
are in assets/materials/provenance.json. License: https://polyhaven.com/license

No Pexels or Pixabay media is bundled.

## Wood flame-height backdrop

`assets/wood-background.png` derives from the same credited CC BY 3.0 wood video.
The RGB channels contain a temporal-minimum backdrop sampled at four frames per
second. Alpha stores the hand-traced log silhouette for each image column; it is
data rather than transparency. The shader keeps this backdrop and the lower
recorded fire fixed, resampling only bright moving emission above the silhouette.
Medium height bypasses the composite and shows the original frame unchanged.

Rebuild this derivative with the existing development rendering dependencies:

```sh
build/render-venv/bin/python render/wood-height/create_background.py
```

The script uses FFmpeg, NumPy and Pillow during development. Android gains no
runtime dependency or download. The derivative retains the wood source's CC BY
3.0 license. New gas-source experiments remain outside the application: no
clipped, mesh-filtered or ceramic-log-ghost composite replaces the released
modern linear asset.

## Modern linear scene

The wide burner scene combines actual moving flame emission with an original
black-steel tray and small glass bed. The recorded combustion source is the
credited wood video. No photographed logs, safety mesh or traditional gas
hardware appear in this scene. The resulting flame footage retains CC BY 3.0
attribution; the original burner bed and renderer source are Apache-2.0.

The render pipeline removes the static room estimate in linear light and
retains recorded flame color. Four independently timed source bands use broad
overlap and feathering. A one-second blend joins the end to the opening, making
a 19-second loop from 20 seconds of motion. This is compositing, not a claim of
new footage captured from a real gas appliance.

The checked-in burner plate is `render/linear-gas/burner-bed.png`. Its Blender
4.5 LTS scene recipe is `render/linear-gas/create_scene.py`; it renders only the
bed and does not perform a fluid simulation. Rebuild the moving composite with:

```sh
python3 -m venv build/render-venv
build/render-venv/bin/pip install -r render/linear-gas/requirements.txt
build/render-venv/bin/python render/linear-gas/composite.py
```

FFmpeg must be on PATH. These are development rendering tools, not Android
runtime dependencies. Output remains under `build/linear-composite.mp4` until
moving review and native checks pass. Asset hashes in `media/manifest.json`
identify the exact clips bundled in the application.
