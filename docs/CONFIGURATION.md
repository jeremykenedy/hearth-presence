# Configuration

Open Hearth Presence from the TV launcher. Use the remote to focus a list,
press Select, choose with Up/Down and confirm. Back returns to the previous screen.
Settings persist locally. Restart the preview or dream to apply changes.

| Setting | Default | Choices |
|---|---|---|
| Surround | Brick | Brick, white plaster, classic timber, slate, marble, frameless, random |
| Fire type | Wood | Real wood fire, traditional gas footage, modern linear burner composite, random |
| Linear gas flame height | Medium | Small (0.65x), medium (1x), large (1.3x), random; enabled for modern linear gas |
| Frame width | Standard | Thin, standard, wide, random |
| Burn speed | Natural | Slow (0.75x), natural (1x), lively (1.25x), random |
| Flame color | Natural | Natural, amber, blue, violet, random |
| Room lighting | Warm | Night, warm, bright, random |
| Drifting ash | Subtle | Off, subtle, lively, random |
| Crackle sound | Off | Off, quiet, lively, random |
| Protective camera drift | Gentle | Gentle, off |
| Randomize each start | False | False, true |

Frame width changes the material band around the fire and the metal reveal
thickness. Thin shows a larger firebox; wide gives the surround more space.
The video retains its aspect ratio. Frameless removes the entire surround and
fills the screen with moving fire; frame width does not apply in that mode.
Burn speed uses Android PlaybackParams. Crackle playback follows the same speed
with pitch fixed at 1.0, avoiding a higher or lower tone. It does not simulate fuel
flow or independently resize individual flames in recorded wood or traditional gas footage.
The modern linear gas flame-height control changes only the region above the
fixed burner line. Its stone/glass bed and frame keep their original dimensions.
It is flame presentation scaling, not a physical gas-valve simulation.
Blue and violet are artistic grading of actual footage, not physically simulated combustion.
Ash is a separate sparse animated layer. Crackle is original synthesized audio,
independent of recorded flame events. Gas footage includes a real safety mesh.
The modern linear scene uses isolated recorded flame emission over an original
steel burner and glass bed, encoded 1920x540 and shown in a matching 32:9 opening.
Its recorded flame source is wood combustion; no photographed logs or mesh
appear in the composite. Combine it with Slate for a modern fireplace.
Traditional gas retains the taller recorded firebox and visible safety mesh.
Color options remap the recorded channels while preserving bright cores and
soft edges. They do not change the fuel or simulate combustion.
Drift shifts the complete fireplace slowly. This reduces stationary edges but
cannot guarantee protection from burn-in; keep TV brightness appropriate.

## Host settings contract

Read `content://com.jeremykenedy.hearthpresence.settings/schema` for the
version-one table (`key`, `title`, `type`, `default`, `choices`, `randomAllowed`).
Read `/settings` for current `key`/`value` rows. Update `/settings` with string
`key` and `value` columns. Invalid keys and choices are rejected. The exported
provider intentionally allows installed host apps to edit visual settings;
it exposes no identity, files or system controls.

```sh
adb -s SERIAL shell content query --uri content://com.jeremykenedy.hearthpresence.settings/schema
adb -s SERIAL shell content update --uri content://com.jeremykenedy.hearthpresence.settings/settings --bind key:s:surround --bind value:s:slate
```
