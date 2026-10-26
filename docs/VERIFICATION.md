# Verification

## Final 1.1.0/code 7 physical gate

The exact production-signed APK is 121,223,466 bytes, SHA-256
`9541eb4fe2f4d7d69ac1f85b38144f5b5926274291ebec796d8150d27e07b781`.
Its certificate is `91128471b54e0c2cc28cb0400ebb5bd8e2b7f2509ba0b6d5ed0507f59752d5cf`.
On October 26 it updated code 6 in place on AFTDEC012E/API 30 and retained all
eleven stored settings. Actual remote D-pad input selected Small, Medium and
Large wood heights; Preview and Back worked for each. Thin/wide white frames,
frameless wood and Small/Natural versus Large/Blue/Slow linear presets were
captured on the exact build. Home and reorder-to-front resumed the same Preview
ActivityRecord; Back returned to Settings.

Frameless Large wood with lively playback, bright lighting and lively ash
measured 57.6915 to 58.1241 compositor presents per second across three clean
Preview windows. The actual content SurfaceView provided 125 to 126 timestamps
per rolling window; within-buffer maximum intervals were 33.15 to 33.42 ms.
An eight-second moving recording was made separately, not during timing.

With the existing 300000 ms idle timer unchanged, the selected Hearth service
became bound after 302.365 seconds with `mCurrentDreamIsTest=false`. It remained
bound for approximately 85 seconds, then detached with Back. Three rolling
windows near each of 20, 40 and 70 seconds measured 47.9996 to 57.6751 compositor
presents per second. These separated windows are not continuous run timing,
decoded-video FPS or a thermal test. The wood source contains 30 fps; lively
playback is 1.25x. Current native stills are in the [gallery](SCREENSHOTS.md).

Strict cleanup matched all eleven Hearth settings, 51 live launcher portable
values, 19 observed OS values, 28 readable surrounding provider interfaces,
other installed APK hashes, external backup/import bytes and existence, app-op
modes in both observed scopes, and guard/VPN/accessibility health. Unsupported
provider responses were retained privately and do not establish value retention
for those interfaces. Original Aerial selection was restored explicitly. Main
was focused and Awake, and Hearth was stopped after final provider reads.
No timer, permission, app-op, audio, CEC, account, reboot or sleep changes were used.

The unchanged source period had already received independent normal-speed
moving review through the 34.685-second API 34 capture. This does not represent
owner-wide visual acceptance, frame-exact seam verification, audible crackle
quality or long-duration thermal validation. Genuinely filmed modern linear gas
remains unfinished; the shipped linear scene is the credited existing composite.

## Earlier 1.1 development and rejected candidates

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

A subsequent controlled comparison used the unchanged code 4 APK and the same
frameless wood preset. Medium with ash off measured 51.322 to 51.369 presents per
second; large with ash off measured 21.800 to 21.804; medium with lively ash
measured 19.224 to 19.275. Each range comprises three short content-SurfaceView
windows. The fourth combination was skipped to retain the cleanup reserve; the
earlier separate large/lively result is not relabeled as part of this matrix.
Both the height branch and the existing full-screen ash loop independently
failed the release threshold. The first comparison attempt stopped before any
measurements because Settings lost foreground. Activity logs recorded a delayed
launcher Home start after the harness Home key; that attempt does not establish
a provider defect. Fresh state was restored after both attempts.

The replacement candidate pre-renders only the two discrete height variants at
1080p/30 fps and draws the twelve ash particles as additive GL points. A chroma
mask excludes red brick illumination from the resized flame emission. Native
visual, shader, lifecycle and physical presentation gates remain pending for
that replacement; the code 4 results cannot validate it.

The corrected replacement is version 1.1.0/code 6, SHA-256
`e4e87c718204f4afc27423ae1bcba4b7ef821302a67985c2e8815e67f1ca458e`,
115,087,658 bytes, with the unchanged production certificate. Code 5 was not
device-tested: full-resolution source-frame inspection caught displaced red
brick illumination, so its media mask was corrected before the next candidate.
Small, medium and large clips each fully decode to 878 frames at 1920x1080/30.
The original medium file is unchanged. The new source stills are development
media checks, not final native captures.

On the Android TV API 34 emulator, exact code 6 retained all eleven existing
Hearth values. Native D-pad selection and provider readback checked small,
medium and large heights, with Preview and Back to Settings for each. An
eight-second native recording checked lively ash with large wood flames. The
updated gallery uses this exact APK. Independent moving review and physical
presentation results remain pending.

The existing Preview activity also resumed after Home, verified by the same
ActivityRecord before and after returning, and Back returned to its original
Settings activity. An earlier harness launched a second Preview rather than
resuming the first; its failed Back assertion is retained as a harness failure,
not a runtime regression or a passing route. No app change was needed for that
correction. Cleanup verified Hearth's eleven values, fourteen launcher portable
values, fifteen observed system values, exact external backup/import bytes,
storage app-op modes and the stopped guard. Surrounding observed package hashes
and available provider values matched. The emulator remained alive at Google
Home, with the legitimate Hearth upgrade retained and force-stopped.

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

### Code 6 physical performance foundation and visual hold

The exact code 6 APK was subsequently tested on AFTDEC012E/API 30. Native
D-pad selection exercised all three wood heights with Preview and Back. The
frameless large/lively/bright/lively-ash preset measured 54.349 to 58.139 presents
per second across three short Preview windows. One initial Preview window had
a 133.531 ms interval; its cause was not isolated. Later Preview maxima were
33.37 and 34.02 ms.

A normal, non-test Dream remained bound for 300.004 seconds. Three windows at
each of approximately 40, 150 and 280 seconds measured 57.230 to 57.696 presents
per second. Each sampled window covered about 2.15 to 2.18 seconds, without
screen recording. These are compositor presentations, not decoded video FPS
or continuous full-run timing. The wood source contains 30 frames per second.
Within those Dream windows the largest intervals were 33.35 to 34.12 ms.

Strict cleanup verified the fresh Hearth, launcher and available surrounding
provider values, observed system keys, external backup/import bytes and app-op
modes. The original Aerial selection was explicitly restored, Main was focused
and Awake, and the working guard state was retained. The legitimate upgrade
was retained. No audio, CEC, account, reboot or sleep changes were used.

This establishes a performance foundation, not final visual acceptance. Moving
review identified a bright rectangular bezel edge and overly isolated pale
flame cores. The next private code 7 candidate replaces that bezel edge with a
smooth shadow and pre-renders softer orange flame emission while protecting
the fixed sidewalls. Matched source frames and a complete 29.267-second source
movie were reviewed, plus a ten-second last-to-first content boundary proof.
Natural detached bright flame flecks remain. These source checks do not replace
fresh Android visual, lifecycle and presentation checks of the final candidate.
Historical code 6 screenshots remain tied to that candidate; the current gallery
uses code 7 captures of the new polish.

The frozen code 7 candidate has SHA-256
`9541eb4fe2f4d7d69ac1f85b38144f5b5926274291ebec796d8150d27e07b781`
and is 121,223,466 bytes. Its production signing certificate is unchanged.
Compared with code 6, only the version manifest, bezel shader and two adapted
wood videos differ. DEX, settings, point-ash shaders, source medium video,
traditional gas, modern linear, background, materials and audio are identical.
Both new clips fully decode to 878 frames at 1920x1080/30. Large is byte-identical
to the complete source proof reviewed in QuickTime. Local build, Java/style,
installer, privacy, media integrity and artifact checks passed. The exact code 7 emulator gate is recorded below; its later final physical
gate is summarized at the start of this document.

### Exact code 7 emulator gate

The exact frozen code 7 APK was installed in place on the API 34 emulator and
retained all eleven Hearth values. Actual D-pad selection exercised Small,
Medium and Large with provider readback, Preview and Back. Current native
captures show each size and the softened bezel. A 34.685-second frameless,
large-height, lively-ash recording was saved; its length spans a source loop,
and was independently played at normal speed through its end. Samples near
0.24, 13.69, 29.00 and 34.68 seconds showed moving fire and ash, stable log and
wall coordinates, and no obvious bright rectangular bezel ring or gross chroma
halo. This was sampled moving review across the 29.267-second source period,
not frame-by-frame seam verification or owner acceptance. No DreamService or
physical code 7 presentation claim is made from this Preview gate.

Home and reorder-to-front resumed the same Preview ActivityRecord, and Back
returned to the original Settings activity. Strict cleanup matched Hearth's
eleven values, fourteen live UI values, fifteen observed system values,
available surrounding providers, twenty-nine other package hashes, external
backup/import bytes and existence, and both app-op scopes. Accessibility health,
stopped guard, unlimited/zero-latency network and Google Home were verified.
Hearth 7 and the retained Skycast 3 were force-stopped; the AVD remained alive.

The AVD had been absent at preflight. Starting its existing userdata loaded a
Quick Boot snapshot, so this is not a cold-boot claim. Before app mutation,
read-only package, OS, weather, network, guard, accessibility, app-op and file
comparisons matched the previous coordinated run. A fresh live UI export then
matched that run's fourteen values as well. All new baselines were persisted
on disk before the gate, and the temporary export app-op was immediately
restored. The current source screenshots were inspected before inclusion.

## Final 1.0.0 artifact

The production-signed APK is `hearth-presence.apk`, version 1.0.0/code 1, 69,011,424 bytes, SHA-256 `96067a79be86a0f29f034ee4bcc647e9da7195978b690a7d982f28a17b78278f`. Its production signing certificate SHA-256 is `91128471b54e0c2cc28cb0400ebb5bd8e2b7f2509ba0b6d5ed0507f59752d5cf`. CI review APKs use ephemeral signers and must not replace this update-compatible production artifact.

## Device matrix

| Device | Type | Version | OS/API | Observed output | Result |
| --- | --- | --- | --- | --- | --- |
| Google TV emulator, shared 5580 | Emulator | 1.1.0/code 7 | Android 14/API 34 | 1920x1080 | Remote wood heights, Large/lively-ash moving recording, Preview/Back and same-instance resume checked; independent 34.685-second movie review |
| Amazon AFTDEC012E | Physical Fire TV | 1.1.0/code 7 | API 30 | 1920x1080 | In-place preservation, remote heights/frame contrasts/linear presets, natural non-test Dream after 302.365 seconds and about 85 seconds bound; separated compositor windows and strict cleanup |
| Google TV emulator, shared 5580 | Emulator | 1.0.0/code 1 | Android 14/API 34 | 1920x1080 | Recorded wood/gas and modern linear playback, material/frame/height/color controls, provider, remote credits and bound test-Dream with Back checked |
| Amazon AFTDEC012E | Physical Fire TV | 1.0.0/code 1 | API 30 | 1920x1080 capture | Remote Settings to Preview and Back, modern linear playback, frameless blue slow/small test-Dream and Back checked |
| Other physical Android TV and Google TV models | Physical | Untested | Untested | Untested | Not established by these checks |

If you can test an unlisted model, report its model, OS/API, resolution, Preview,
remote controls and normal idle-Dream results through the
[issue tracker](https://github.com/jeremykenedy/hearth-presence/issues).

## Released 1.0.0 physical Fire TV run

On October 16, 2026, the exact final production APK was installed in place on AFTDEC012E. The ten existing stored preferences survived the update. The newly supported `flame_size` resolved to its `medium` default. Subsequent checks restored all eleven post-update values exactly.

The remote operated Settings, Open fireplace, Preview and Back to Settings. The modern linear scene ran in a slate surround with large flames, bright lighting, lively ash and crackle enabled. The actual native recording lasts 19.741 seconds. A SurfaceFlinger latency sample contains 126 valid presents across 3.7167 seconds, approximately 33.63 buffer presents per second. This short presentation sample is not decoded-video FPS, a sustained renderer benchmark, an acoustic test or a thermal guarantee. The modern source video is 1920x540 at 30 fps.

A separate run used frameless blue grading, small flames and slow playback through the actual HearthDreamService. Dream-manager output identified the service, `mCurrentDreamIsTest=true` and `mBound=true`; Back cleared the bound dream. This explicit test exercises the real service rather than only launching an activity. It does not establish automatic idle startup across vendor configurations.

The selected Aquarium Dream, screensaver enabled state, sleep timeout, screen-off timeout and auto-wake setting were unchanged. All eleven app preferences matched the post-update baseline after restoration, and the device returned to its original asleep state. No physical TV commands were issued by the documentation worker; these results come from the coordinated device run.

The unretouched physical captures are [`fire-tv-modern-linear.png`](../art/screenshots/fire-tv-modern-linear.png) and [`fire-tv-frameless-blue-dream.png`](../art/screenshots/fire-tv-frameless-blue-dream.png). Their exact timestamps, artifact hash, routes and dimensions are in [`physical-provenance.json`](../art/screenshots/physical-provenance.json). Independent native QuickTime review played the final physical recording from start to end and replayed the middle through the end. Flames changed continuously within the correct slate frame and reflected lighting, with no empty or missing fire observed. The separate frameless blue actual-Dream capture was also inspected.

## Released 1.0.0 emulator controls and moving evidence

The current modern scene uses isolated recorded wood flame emission over an original steel burner and glass bed. It replaces the rejected traditional-gas crop and is a composite depiction rather than a photographed gas burner or fluid simulation. Its 19-second source loop ran on Google TV API 34 at 1920x1080. Small, medium and large flame heights retain the same frame and burner bed. Frameless slow playback, a wide white frame, blue and violet grading and matching reflections were checked on the native surface.

The corrected scene capture build SHA-256 was `fcc20d8628d562a07ea9a50365e9a08704c28689cecf115a5544e0782589d174`. The final production APK retains the same renderer and scene media, embeds the refreshed native preview and adds the offline credits dialog. On that exact final APK, D-pad navigation opened credits, scrolled from source attribution into the full Apache application license, and Back closed the dialog. Packaged NOTICE and LICENSE match the root files byte-for-byte. Existing preferences and the selected Reel Atrium Dream remained unchanged.

A 22.544-second modern native recording contains 764 captured compositor frames across a loop boundary. Earlier wood evidence spans the complete 29.25-second source loop. Recording counts support moving review and are not independent renderer frame-rate measurements. The separate source loops contain genuine changing recorded fire; the animation does not consist of a still fire with camera motion.

## Host verification

The production APK builds with SDK 36, minSdk 23 and targetSdk 36. SettingsValues host tests enforce 100% line and branch coverage, and installer tests separately enforce 100% Python line and branch coverage. Spotless checks actual Java source. Privacy, media hashes, XML/SVG and secret checks run locally and in CI. The app requests no permissions, uses no network client and adds no application runtime dependencies. Framework, decoder, graphics and lifecycle code remain outside host coverage and require native checks.

## Limits

Automatic idle activation, long-duration decoder/GPU behavior, temperature, power and vendor-specific sleep/wake paths have not been comprehensively measured for this release. Native output evidence is 1920x1080; a 4K panel does not establish native 4K composition. Protective drift reduces stationary edges but does not guarantee prevention of image retention or burn-in. The standalone installer changes no selected dream, timers, sleep behavior or update settings. Physical preservation checks do not establish support for every vendor model or OS version.
