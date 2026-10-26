# Verification

## Unreleased 1.1 wood height

The code 3 development candidate has SHA-256
`6ae9a6f0779e80efb56d3fe09020adf8b47bf9615d6c50452dd352e8202cc77f`.
It was installed in place with the production signer on the Android TV API 34
emulator. All eleven prior Hearth provider values survived and were restored
after the test. The native height selector was enabled for wood; selecting Small
and reading the provider confirmed persistence. This was a tap-assisted emulator
selection, not a physical remote-input claim.

Small, medium and large wood Preview captures and an eight-second large-height
movie were saved at 1920x1080. Back returned to settings. The first code 2 attempt
also resized some changing wall illumination; it was rejected. Code 3 gates the
resized emission to bright flame channels, preserving the fixed brickwork and
log silhouette. Independent review of that corrected eight-second movie passed
for proceeding to the physical gate. This does not establish final performance.

All fourteen surrounding launcher portable keys, eleven system values, available
surrounding-provider snapshots, external backup/import bytes, storage app-op
mode and stopped guard state matched the fresh on-disk baseline after cleanup.
The existing emulator remained running at Home. No physical TV, timer, reboot,
audio, account or selected-Dream changes were part of this test.

The development background asset was regenerated from the bundled source and
matched the tested APK byte-for-byte. Settings tests and actual Java style checks
passed. The final code 4 adds the derivative notice and release version metadata.
Its SHA-256 is `581782d2752866e6dcc6ffcaba1cbaf9273a009f0225d5ccd041936df034a909`
and its size is 69,920,808 bytes. The production certificate is unchanged.
Compared with the native-tested code 3 APK, only `AndroidManifest.xml` and
`assets/NOTICE` differ: DEX, media, backdrop, shader and all remaining resources
are byte-identical. Signed build, Java/style checks, installer coverage, privacy
and artifact checks pass. The exact code 4 physical gate below failed its
presentation-rate requirement, so this candidate must not be released.
See [current candidate captures](SCREENSHOTS.md).

### Code 4 physical performance failure

On October 26, the exact code 4 APK was installed in place on the physical
AFTDEC012E/API 30 device. All eleven stored Hearth values survived. Native D-pad
selection exercised small, medium and large wood heights with Preview and Back;
an eight-second large-height recording was saved for review. A normal, non-test
Hearth Dream was actually bound and detached with Back.

The worst tested preset was frameless wood, large flames, lively playback,
bright lighting, lively ash, gentle motion and crackle off. Three short
SurfaceFlinger latency windows from the actual Preview content SurfaceView
measured 11.14449, 11.15453 and 11.14385 presents per second. Three windows from
the actual Dream content SurfaceView measured 11.12751, 11.14427 and 11.14432.
Sampling occurred without screen recording after 25 seconds of Preview
settling and 40 seconds of Dream settling. These are presentation measurements,
not source-video frame counts or a continuous thermal benchmark. The bundled
wood source itself is 1920x1080 at 30 fps.

This result fails the minimum 24 presents-per-second release gate. It does not
identify whether the new height compositing, existing ash rendering or their
combination dominates the cost. A controlled medium/large and ash-off/lively
comparison remains necessary before choosing an optimization. No other preset
inherits a performance result from this test.

Cleanup restored the eleven Hearth values, fifty-one current launcher portable
values, fifteen observed system values, surrounding available providers,
external backup/import bytes and storage app-op modes. Other package identities
were unchanged. The legitimate Hearth upgrade was retained. A final full
window-manager dump verified Main focus, Awake state and no bound Dream; the
original Aerial selection was restored. No reboot, power toggle, sleep command,
audio or CEC changes were used. These physical results hold the release rather
than extending the earlier 1.0 performance claim to the new renderer.

The eight existing banner files are unchanged from the earlier public GitHub
browser matrix recorded on October 16. That matrix checked desktop/mobile,
light/dark and motion/reduced-motion selections and observed changed animation
phases; it did not record a full continuous loop or change account-wide theme
preferences. The updated wood gallery passed a public Chrome check at source
`f8c411e` on October 26: all twenty-two 1920x1080 images loaded at desktop 1280px
and phone 320px, both galleries were visually inspected, and all three columns
fit without horizontal page overflow. The README's three new previews and
features table also passed both widths. Temporary viewport changes were reset
and the owned review tab was closed; no account appearance setting changed.

## Final 1.0.0 artifact

The production-signed APK is `hearth-presence.apk`, version 1.0.0/code 1, 69,011,424 bytes, SHA-256 `96067a79be86a0f29f034ee4bcc647e9da7195978b690a7d982f28a17b78278f`. Its production signing certificate SHA-256 is `91128471b54e0c2cc28cb0400ebb5bd8e2b7f2509ba0b6d5ed0507f59752d5cf`. CI review APKs use ephemeral signers and must not replace this update-compatible production artifact.

## Device matrix

| Device | Type | OS/API | Observed output | Result |
| --- | --- | --- | --- | --- |
| Google TV emulator, shared 5580 | Emulator | Android 14/API 34 | 1920x1080 | Recorded wood/gas and modern linear playback, material/frame/height/color controls, provider, remote credits and bound test-Dream with Back checked |
| Amazon AFTDEC012E | Physical Fire TV | Android API 30; Fire OS build not refreshed | 1920x1080 capture | Final signed APK update, remote Settings to Preview and Back, modern linear playback, frameless blue slow/small actual test-Dream and Back checked |
| Other physical Android TV and Google TV models | Physical | Untested | Untested | Not established by these checks |

## Final physical Fire TV run

On October 16, 2026, the exact final production APK was installed in place on AFTDEC012E. The ten existing stored preferences survived the update. The newly supported `flame_size` resolved to its `medium` default. Subsequent checks restored all eleven post-update values exactly.

The remote operated Settings, Open fireplace, Preview and Back to Settings. The modern linear scene ran in a slate surround with large flames, bright lighting, lively ash and crackle enabled. The actual native recording lasts 19.741 seconds. A SurfaceFlinger latency sample contains 126 valid presents across 3.7167 seconds, approximately 33.63 buffer presents per second. This short presentation sample is not decoded-video FPS, a sustained renderer benchmark, an acoustic test or a thermal guarantee. The modern source video is 1920x540 at 30 fps.

A separate run used frameless blue grading, small flames and slow playback through the actual HearthDreamService. Dream-manager output identified the service, `mCurrentDreamIsTest=true` and `mBound=true`; Back cleared the bound dream. This explicit test exercises the real service rather than only launching an activity. It does not establish automatic idle startup across vendor configurations.

The selected Aquarium Dream, screensaver enabled state, sleep timeout, screen-off timeout and auto-wake setting were unchanged. All eleven app preferences matched the post-update baseline after restoration, and the device returned to its original asleep state. No physical TV commands were issued by the documentation worker; these results come from the coordinated device run.

The unretouched physical captures are [`fire-tv-modern-linear.png`](../art/screenshots/fire-tv-modern-linear.png) and [`fire-tv-frameless-blue-dream.png`](../art/screenshots/fire-tv-frameless-blue-dream.png). Their exact timestamps, artifact hash, routes and dimensions are in [`physical-provenance.json`](../art/screenshots/physical-provenance.json). Independent native QuickTime review played the final physical recording from start to end and replayed the middle through the end. Flames changed continuously within the correct slate frame and reflected lighting, with no empty or missing fire observed. The separate frameless blue actual-Dream capture was also inspected.

## Emulator controls and moving evidence

The current modern scene uses isolated recorded wood flame emission over an original steel burner and glass bed. It replaces the rejected traditional-gas crop and is a composite depiction rather than a photographed gas burner or fluid simulation. Its 19-second source loop ran on Google TV API 34 at 1920x1080. Small, medium and large flame heights retain the same frame and burner bed. Frameless slow playback, a wide white frame, blue and violet grading and matching reflections were checked on the native surface.

The corrected scene capture build SHA-256 was `fcc20d8628d562a07ea9a50365e9a08704c28689cecf115a5544e0782589d174`. The final production APK retains the same renderer and scene media, embeds the refreshed native preview and adds the offline credits dialog. On that exact final APK, D-pad navigation opened credits, scrolled from source attribution into the full Apache application license, and Back closed the dialog. Packaged NOTICE and LICENSE match the root files byte-for-byte. Existing preferences and the selected Reel Atrium Dream remained unchanged.

A 22.544-second modern native recording contains 764 captured compositor frames across a loop boundary. Earlier wood evidence spans the complete 29.25-second source loop. Recording counts support moving review and are not independent renderer frame-rate measurements. The separate source loops contain genuine changing recorded fire; the animation does not consist of a still fire with camera motion.

## Host verification

The production APK builds with SDK 36, minSdk 23 and targetSdk 36. SettingsValues host tests enforce 100% line and branch coverage, and installer tests separately enforce 100% Python line and branch coverage. Spotless checks actual Java source. Privacy, media hashes, XML/SVG and secret checks run locally and in CI. The app requests no permissions, uses no network client and adds no application runtime dependencies. Framework, decoder, graphics and lifecycle code remain outside host coverage and require native checks.

## Limits

Automatic idle activation, long-duration decoder/GPU behavior, temperature, power and vendor-specific sleep/wake paths have not been comprehensively measured for this release. Native output evidence is 1920x1080; a 4K panel does not establish native 4K composition. Protective drift reduces stationary edges but does not guarantee prevention of image retention or burn-in. The standalone installer changes no selected dream, timers, sleep behavior or update settings. Physical preservation checks do not establish support for every vendor model or OS version.
