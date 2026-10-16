# Host integration contract

| Field | Value |
|---|---|
| Toolkit ID | `hearth-presence` |
| Repository | `jeremykenedy/hearth-presence` |
| Application package | `com.jeremykenedy.hearthpresence` |
| Dream component | `com.jeremykenedy.hearthpresence/.HearthDreamService` |
| Fully qualified service | `com.jeremykenedy.hearthpresence.HearthDreamService` |
| Settings activity | `com.jeremykenedy.hearthpresence/.SettingsActivity` |
| Preview activity | `com.jeremykenedy.hearthpresence/.PreviewActivity` |
| Minimum API | 23 |
| APK asset | `hearth-presence.apk` |
| Checksum asset | `hearth-presence.apk.sha256` |
| Settings schema | `content://com.jeremykenedy.hearthpresence.settings/schema` |
| Current settings | `content://com.jeremykenedy.hearthpresence.settings/settings` |
| Preview source | `art/screenshots/brick-wood.png` |
| Embedded preview | `res/drawable-nodpi/screensaver_preview.jpg` |

The first release remains pending final modern gas validation. Integrators must
use the published release tag, final signed APK byte count and SHA-256 sidecar;
do not pin a development build hash. Source alone does not establish release
availability. The standalone installer preserves package identity and the
production signing certificate for subsequent updates.

Fire TV UI discovers the exported, protected DreamService through the package
manager and opens the settings activity declared in Dream metadata. A bundled
thumbnail must use the host's existing normalized-component SHA-256 filename
helper. Preserve the screenshot's wood footage attribution in NOTICE and
sources metadata. Native discovery, remote settings launch, dream selection,
Back/Menu/Home, restoration and actual fire output must be verified on the host.

The settings provider accepts only documented `key` and `value` pairs. Its
schema includes defaults, choices and whether random is accepted. Modern gas
flame height changes only the flame region above its fixed burner bed. It does
not resize flames independently in recorded wood or traditional gas footage.
See [configuration](CONFIGURATION.md) and [device verification](VERIFICATION.md).
