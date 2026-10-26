# Architecture

Wood flame height uses a licensed temporal-minimum backdrop with an encoded log
silhouette. Medium samples the original video directly. For small and large,
only bright moving emission above that silhouette is sampled at a different
height; the logs, lower fire and wall texture keep their coordinates. The two
height variants are baked into separate 1920x1080, 30 fps clips during development
so the runtime does not repeat flame extraction for every display pixel. This is
image compositing, not an independent combustion simulation.

A native Android DreamService owns an OpenGL ES 2 surface. MediaPlayer decodes
bundled H.264 wood or gas footage into an external OES texture. The fragment
shader places that moving fire inside a layered metal reveal and a material
surround spanning the screen. Photographed brick courses, joints, plaster grain,
marble veins and timber grain are shaded with warm fluctuating spill light.
A tiny optional drift moves the entire fireplace. Twelve optional ash particles
are drawn as small additive GL points, clipped to the firebox, rather than a
full-screen fragment loop. No image slideshow is used.

Dream stop and preview pause release video, sound and SurfaceTexture on the
GL thread before pausing the surface. Starting creates fresh decoder and GL
resources. There are no background services, wake locks or runtime dependencies.

The default wood source and encoded video are genuine 1920x1080. The gas
source is 3840x2160. Standard gas crops to 3840x1780 and encodes 1920x890 at 30 fps (H.264 High Level 4.0);
The modern linear scene composites isolated recorded flame emission over an original
rendered burner bed at 1920x540 for a 32:9 opening. Its source footage is wood
combustion; it does not contain photographed gas hardware or a cropped log pile.
PlaybackParams controls burn speed and preserves audio pitch. Frameless covers
the display using aspect-preserving center cropping when needed. Neither asset nor
emulator establishes native 4K output. The wood adaptation is CC BY 3.0 and the
gas adaptation is CC BY-SA 4.0; application code is Apache-2.0. See NOTICE.

The app requests no permissions, includes no networking library and performs
no runtime downloads, analytics, crash reporting or tracking. The installer
alone contacts GitHub when explicitly run by the user.

Material textures are photographed Poly Haven assets under CC0-1.0: red_brick,
white_plaster_02, wood_floor, slate_floor and marble_01. Original 1K diffuse
and OpenGL normal maps are bundled unchanged. Exact source URLs and SHA-256
are in assets/materials/provenance.json. License: https://polyhaven.com/license
