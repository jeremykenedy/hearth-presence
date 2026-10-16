# Verification

## Device matrix

| Device | Type | OS/API | Resolution | Result |
|---|---|---|---|---|
| Google TV emulator aql-googletv34 | Emulator | Android 14/API 34 | 1920x1080 | Real 1080 wood/gas playback, material modes, settings provider and remote Menu/Back tested |
| AFTDEC012E | Physical Fire TV | Fire OS/API 30 | 1920x1080 capture | Wood preview, wide frame and frameless slow playback captured; final modern gas and idle activation pending |
| Android TV | Other physical models | Untested | Untested | Volunteer needed |
| Google TV | Physical | Untested | Untested | Volunteer needed |

If you have an untested TV, please test and report your model, OS/API, resolution,
remote navigation, dream activation, sustained playback, exit and sleep/wake
results through this repository's issue tracker. Emulator results do not establish
vendor idle startup, sustained thermal behavior or native 4K composition.

## Host checks

- Signed APK builds with SDK36, minSdk23 and targetSdk36.
- SettingsValues host Java tests enforce 100% line and branch coverage.
- Installer tests enforce 100% Python line and branch coverage.
- Style uses Google Java Format through Spotless.
- Manifest/source privacy checks and media/XML/SVG validation run locally and in CI.
- App has no permission requests or application runtime dependencies.

## Screenshot provenance

Images in art/screenshots are unretouched ADB captures from the running app on
Google TV API 34, 1920x1080, October 15 2026. Each filename describes its mode.
The in-app preview is a resized version of the verified default screenshot.
Wood footage is CC BY 3.0 and traditional gas footage is CC BY-SA 4.0; see NOTICE and MEDIA.md.

## Native evidence

A 34.9 second native screen recording contains 1784 compositor frames at 1920x1080,
covering the entire 29.25 second wood loop without a blank transition in inspected
samples. This is not an independent flame-rate benchmark; source footage is 30 fps.
The scene uses actual decoded footage, not a still fire with camera motion.
After sustained emulator playback, dumpsys meminfo reported 24,514 KB total PSS.
This is one emulator sample, not a hardware memory or power guarantee.
D-pad/Select changed the surround from Brick to White and the provider confirmed
persistence. Invalid provider values were rejected. Menu and Back exited preview.

## Scope

No reboot, platform update blocking, sleep timer modification or physical TV
changes are performed by the standalone installer. Platform-specific settings
safeguards belong to Fire TV Toolkit. Drift reduces stationary edges but does
not guarantee prevention of image retention or burn-in. Native4K, long-term
thermal behavior and all vendor versions require separate device evidence.

## Physical Fire TV evidence

Wood playback was inspected on AFTDEC012E/API 30. Original physical captures
include a wide brick frame and frameless wood at 0.75x. A first frameless capture
was black, so playback was relaunched and the slow mode was captured again with
visible moving fire. This is a retest result, not a claim that the first attempt
passed. A 39.4 second recording contains 869 captured frames, approximately
22 captured frames per second. Screen recording timestamps do not establish
the uncaptured renderer frame rate. SurfaceFlinger returned no usable timing
samples. One physical meminfo sample reported 152,058 KB total PSS.

The original Aquarium screensaver choice and enabled state were preserved.
Final modern linear gas playback, actual DreamService activation, settings
persistence, sleep/wake and sustained thermal checks remain release gates.

## Development candidate

The repository contains development source while the modern linear gas asset
is being replaced with an original simulated burner. The existing linear clip
is a rejected interim crop and must not be presented as the finished modern
fireplace. No public APK release has been published from this candidate.

The current API34 build exposes Modern linear gas in the remote Fire type list.
D-pad Down/Select selected it; the provider returned `fuel=linear` before and
after force-stop. Wood was restored afterward. A native DreamService preview
was bound through IDreamManager.testDream, rendered visible wood for the
settling interval and exited on Back. The original Aquarium Live selection
and enabled=1 remained intact. `art/screenshots/dream-wood.png` records that run.
