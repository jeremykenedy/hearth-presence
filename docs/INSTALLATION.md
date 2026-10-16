# Installation

Enable ADB on your TV and connect it. Use an explicit serial from `adb devices`.

```sh
python3 install.py --serial SERIAL
python3 install.py --serial SERIAL --apk build/hearth-presence.apk
```

The installer explains the action, asks for confirmation, downloads the APK
and sibling SHA-256 asset from the fixed GitHub repository, validates trusted
HTTPS redirects and verifies the bytes before installing. Local --apk is an
explicit trust override for your own build. --yes supports scripted installation.
An existing installation updates in place with the same signing key.

Open Hearth Presence to configure or preview. Select its DreamService in your
platform's screensaver picker or with Fire TV Toolkit. The standalone installer
changes no system timers, selected screensaver, update settings or sleep behavior.

```sh
python3 install.py --serial SERIAL --uninstall
```

Removal deletes the app and its local preferences. Noninteractive removal also
requires --yes --force. Select a different screensaver before uninstalling.
Toolkit provides its own guided selection and reversible platform safeguards.
