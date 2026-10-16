<p align="center">
  <a href="https://github.com/jeremykenedy/hearth-presence#gh-light-mode-only"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="art/banner-mobile-still-light.b4bd1b3cf35b.svg"><source media="(prefers-reduced-motion: reduce)" srcset="art/banner-still-light.d753accda9a8.svg"><source media="(max-width: 600px)" srcset="art/banner-mobile-light.68b32868733b.svg"><img src="art/banner-light.d14414c248de.svg#gh-light-mode-only" alt="Hearth Presence" width="800"></picture></a>
  <a href="https://github.com/jeremykenedy/hearth-presence#gh-dark-mode-only"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="art/banner-mobile-still-dark.3a6e12260e87.svg"><source media="(prefers-reduced-motion: reduce)" srcset="art/banner-still-dark.9ccdf3eddea3.svg"><source media="(max-width: 600px)" srcset="art/banner-mobile-dark.c3438e388145.svg"><img src="art/banner-dark.953f0afb64a3.svg#gh-dark-mode-only" alt="Hearth Presence" width="800"></picture></a>
</p>
<p align="center">A real burning fireplace with material surrounds, flame grading and gentle protective drift.</p>
<p align="center">
  <a href="https://github.com/jeremykenedy/hearth-presence/releases"><img alt="Downloads" src="https://img.shields.io/github/downloads/jeremykenedy/hearth-presence/total"></a>
  <a href="https://github.com/jeremykenedy/hearth-presence/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/jeremykenedy/hearth-presence"></a>
  <a href="https://github.com/jeremykenedy/hearth-presence/actions/workflows/tests.yml"><img alt="Tests" src="https://github.com/jeremykenedy/hearth-presence/actions/workflows/tests.yml/badge.svg"></a>
  <a href="LICENSE"><img alt="Apache-2.0" src="https://img.shields.io/badge/License-Apache--2.0-blue"></a>
</p>
<p align="center">
  <a href="https://github.com/jeremykenedy"><img alt="Follow" src="https://img.shields.io/github/followers/jeremykenedy?label=Follow"></a>
  <a href="https://github.com/jeremykenedy/hearth-presence/stargazers"><img alt="Star repository" src="https://img.shields.io/github/stars/jeremykenedy/hearth-presence"></a>
  <a href="https://github.com/sponsors/jeremykenedy"><img alt="Sponsor" src="https://img.shields.io/badge/Sponsor-GitHub-pink"></a>
</p>

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Features](#features)
- [Configuration](#configuration)
- [Fire TV Toolkit](#fire-tv-toolkit)
- [Privacy](#privacy)
- [Testing](#testing)
- [Documentation](#documentation)
- [Screenshots](#screenshots)
- [License](#license)

The source is available while the first release completes native verification.
The modern linear gas clip is being replaced with an original burner render;
its interim crop is not an accepted modern fireplace. See the
[verification record](docs/VERIFICATION.md) for completed checks and release gates.

## Requirements

Android API 23 or newer, OpenGL ES 2 and H.264 decoding. A TV remote is recommended.
See the [device verification matrix](docs/VERIFICATION.md) for actual results.
A successful build alone does not establish Fire TV or Google TV compatibility.

## Installation

Download the signed APK and its checksum from [Releases](https://github.com/jeremykenedy/hearth-presence/releases).
The guided installer downloads and verifies the latest release automatically:

```sh
python3 install.py --serial SERIAL
```

An existing installation updates in place. The installer changes no system timers
or selected screensaver. See [installation and removal](docs/INSTALLATION.md).

## Quick Start

Open **Hearth Presence** from the TV launcher, choose your surround and fire,
then select **Open fireplace** to preview. Back exits. Select Hearth Presence
in the platform screensaver settings or through Fire TV Toolkit for idle use.

## Features

- Genuine moving wood, gas and wide linear gas fire, bundled for offline playback.
- Brick, white plaster, classic timber, modern slate and marble surrounds, plus full-bleed Frameless.
- Grain, joints, layered metal reveals and warm flickering light on the surround.
- Natural, amber, blue and violet flame grading.
- Thin/standard/wide frames, adjustable burn speed, room lighting, optional drifting ash and crackle sound.
- Slow camera drift and random choices for supported settings.
- Native DreamService with a remote-friendly settings screen and host settings provider.

Show some love by starring this repository on GitHub.

## Configuration

The default is a wood fire in brick with a standard frame, natural flame color and warm
lighting. Ash is subtle, sound is off and protective drift is on.
[Configuration](docs/CONFIGURATION.md) lists every choice and the host contract.
Frame width changes the material band and metal reveal. Frameless removes both.
Burn speed offers 0.75x, 1x and 1.25x playback with pitch preserved. Linear gas
uses its own matching 32:9 source crop. Color grades the recorded flame.
Ash is a separate visual effect; crackle is synthesized, not recorded flame audio.
The gas footage includes a real safety mesh. These are video-based fires,
so controls do not independently simulate fuel, combustion or individual flames.

## Fire TV Toolkit

[Fire TV Toolkit](https://github.com/jeremykenedy/fire-tv-toolkit) provides a guided
TV setup and screensaver installer:

```sh
git clone https://github.com/jeremykenedy/fire-tv-toolkit.git
cd fire-tv-toolkit
node setup.js
firetv-screensavers --install=hearth-presence
screensaver --set=hearth-presence
firetv-screensavers --install=hearth-presence
firetv-screensavers --uninstall=hearth-presence --force
```

Toolkit also manages supported launcher choices, sleep/screensaver timers and
supported settings safeguards. App-specific visual preferences live in this app.
Fire TV UI discovers installed dreams; its settings and installation capabilities
are documented by that project. It does not provide an arbitrary GitHub installer.

## Privacy

No ads, no analytics, no tracking and no app network access. Both fire clips and
sound are bundled. The manifest requests no permissions and there are no runtime
application dependencies. The user-run installer contacts GitHub for release files.
See [architecture](docs/ARCHITECTURE.md) for the verification boundary.

## Testing

```sh
./build.sh
./scripts/test-coverage.sh
./scripts/test-python-coverage.sh
python3 scripts/check-privacy.py
python3 scripts/check-artifacts.py
```

Java settings logic and the installer each enforce 100% line and branch coverage.
Framework and rendering code require native validation; they are explicitly outside
the host coverage boundary. See [building](docs/BUILDING.md) and [verification](docs/VERIFICATION.md).

## Documentation

- [Building and coverage boundary](docs/BUILDING.md)
- [Installation, update and removal](docs/INSTALLATION.md)
- [Configuration and settings contract](docs/CONFIGURATION.md)
- [Host integration contract](docs/INTEGRATION.md)
- [Architecture and privacy](docs/ARCHITECTURE.md)
- [Media provenance and licenses](docs/MEDIA.md)
- [Device verification](docs/VERIFICATION.md)
- [Release notes](CHANGELOG.md)
- [Release procedure](docs/RELEASING.md)
- [1.0.0 release details](docs/releases/v1.0.0.md)

## Screenshots

Captured from the running native application. Footage attribution is in [NOTICE](NOTICE).

<table><tr><td><img src="art/screenshots/brick-wood.png" alt="Real wood fire in a brick surround"></td><td><img src="art/screenshots/slate-gas.png" alt="Gas fire in a modern slate surround"></td><td><img src="art/screenshots/settings.png" alt="Remote-friendly fireplace settings"></td></tr><tr><td><img src="art/screenshots/white-wood.png" alt="Wood fire with a light plaster surround"></td><td><img src="art/screenshots/classic-wood.png" alt="Classic timber fireplace with molding and columns"></td><td><img src="art/screenshots/marble-wood.png" alt="Wood fire in a veined marble surround"></td></tr></table>

## License

This application is open-sourced software licensed under the [Apache License 2.0](LICENSE).
The wood footage is [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).
The gas footage and composites containing it are
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). See [NOTICE](NOTICE)
and [media provenance](docs/MEDIA.md) for author credits and modifications.
