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
| Preview source | `art/screenshots/physical7-wood-large.png` |
| Embedded preview | `res/drawable-nodpi/screensaver_preview.jpg` |

The release contract is `v1.1.0`. Use this exact physically tested production artifact, not an ephemeral CI review build:

| Release field | Value |
| --- | --- |
| Version / Android code | `1.1.0` / `7` |
| APK bytes | `121223466` |
| APK SHA-256 | `9541eb4fe2f4d7d69ac1f85b38144f5b5926274291ebec796d8150d27e07b781` |
| Signing certificate SHA-256 | `91128471b54e0c2cc28cb0400ebb5bd8e2b7f2509ba0b6d5ed0507f59752d5cf` |
| Intended tag | `v1.1.0`, verified remote primary tip at publication |

Source alone does not establish release availability. The standalone installer preserves package identity and the
production signing certificate for subsequent updates.

Fire TV UI discovers the exported, protected DreamService through the package
manager and opens the settings activity declared in Dream metadata. A bundled
thumbnail must use the host's existing normalized-component SHA-256 filename
helper. Preserve the screenshot's wood footage attribution in NOTICE and
sources metadata. Native discovery, remote settings launch, dream selection,
Back/Menu/Home, restoration and actual fire output must be verified on the host.

The settings provider accepts only documented `key` and `value` pairs. Its
schema includes defaults, choices and whether random is accepted. Modern gas
flame height changes only the flame region above its fixed burner bed. Version
1.1 also applies the same stored `flame_size` choices to recorded wood emission,
keeping the logs fixed. Traditional gas height remains unsupported. The provider
retains the same eleven keys and choices; no preference migration is required.
See [configuration](CONFIGURATION.md) and [device verification](VERIFICATION.md).
