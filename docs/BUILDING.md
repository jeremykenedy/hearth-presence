# Building and checks

Install JDK 17 or newer, Android SDK platform 36 and build-tools 36.0.0, Python 3,
and the usual macOS command-line tools. Set ANDROID_HOME if the SDK is elsewhere.

```sh
./build.sh
./scripts/test-coverage.sh
./scripts/test-python-coverage.sh
python3 scripts/check-privacy.py
```

The build uses only the Android framework, without Gradle Android plugins or
application dependencies. A unique key is created under ~/.android on first
build and reused. Preserve hearth-presence.jks and hearth-presence.pass outside
the repository. HEARTH_KEYSTORE and HEARTH_KEYPASS override those paths.
Production builds produce build/hearth-presence.apk and its SHA-256 file.
Never share signing material. CI builds use ephemeral signing files and the
resulting APKs are review artifacts, not update-compatible production releases.

Host Java tests cover accepted and rejected provider choices, defaults and
random selection. JaCoCo enforces 100% line and branch coverage of SettingsValues,
the owned pure logic boundary. Android service, settings widgets, provider,
media decoder and GL adapter require device validation and are not included
in host coverage. The shader is visually verified on Android, not covered by
host tests. Installer coverage independently enforces 100% lines and branches.

CI also runs a pinned Gitleaks secret scan. GitHub secret scanning and push
protection are enabled on the public repository. Paid rating services and
external token-dependent scanners are not configured or advertised.
