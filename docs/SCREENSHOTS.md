# Native screenshots

## Wood height development candidate

These current captures come from version 1.1.0/code 3 on the Android TV API 34
emulator at 1920x1080. They are PreviewActivity captures, not physical-TV or
DreamService proof. The fixed logs and frame retain their coordinates while the
recorded flame emission changes height. Final physical testing is pending.
Exact artifact hashes are in [capture provenance](../art/screenshots/wood-height-provenance.json).

<table><tr><th>Small</th><th>Medium</th><th>Large</th></tr><tr><td><img src="../art/screenshots/wood-height-small-api34.png" alt="Small wood flame emission above unchanged logs"></td><td><img src="../art/screenshots/wood-height-medium-api34.png" alt="Original medium wood footage with unchanged logs"></td><td><img src="../art/screenshots/wood-height-large-api34.png" alt="Large wood flame emission above unchanged logs"></td></tr><tr><td><img src="../art/screenshots/wood-height-settings-api34.png" alt="Native settings with wood flame height enabled"></td><td></td><td></td></tr></table>

## Released 1.0.0 modes

The following captures document the earlier released build. The modern linear,
surround, frame, grading, ash and sound behavior is unchanged by the wood-height
work; these images are retained as historical evidence rather than new tests.

Captured from the running native application. The first two images show the exact final production APK on a physical AFTDEC012E Fire TV; the third shows its unchanged modern scene through the actual DreamService on API 34. Remaining captures show the verified emulator controls and materials. Footage attribution is in [NOTICE](../NOTICE).

<table><tr><td><img src="../art/screenshots/fire-tv-modern-linear.png" alt="Final modern linear fireplace on physical AFTDEC012E Fire TV"></td><td><img src="../art/screenshots/fire-tv-frameless-blue-dream.png" alt="Final frameless blue small flames through the bound DreamService on physical Fire TV"></td><td><img src="../art/screenshots/dream-modern-linear.png" alt="Modern linear scene through actual DreamService on API 34 emulator"></td></tr><tr><td><img src="../art/screenshots/brick-wood.png" alt="Recorded wood fire in a brick surround"></td><td><img src="../art/screenshots/modern-linear-medium.png" alt="Modern wide burner with recorded flame emission and a slate surround"></td><td><img src="../art/screenshots/settings-modern-linear.png" alt="Remote settings with modern linear flame height enabled"></td></tr><tr><td><img src="../art/screenshots/white-wood.png" alt="Wood fire with a light plaster surround"></td><td><img src="../art/screenshots/classic-wood.png" alt="Classic timber fireplace with molding and columns"></td><td><img src="../art/screenshots/marble-wood.png" alt="Wood fire in a veined marble surround"></td></tr><tr><td><img src="../art/screenshots/modern-linear-small.png" alt="Small modern flames above the unchanged burner bed"></td><td><img src="../art/screenshots/modern-linear-large.png" alt="Large modern flames above the unchanged burner bed"></td><td><img src="../art/screenshots/modern-linear-frameless-slow.png" alt="Modern fire filling the display without a surround"></td></tr><tr><td><img src="../art/screenshots/modern-linear-white-wide-blue.png" alt="Blue flame grading retaining bright cores and translucent edges"></td><td><img src="../art/screenshots/modern-linear-white-violet.png" alt="Violet flame grading with matching surround reflections"></td><td><img src="../art/screenshots/settings-effects.png" alt="Burn speed, color, ash, sound and drift controls"></td></tr><tr><td><img src="../art/screenshots/credits.png" alt="Bundled source credits opened with the TV remote"></td><td><img src="../art/screenshots/credits-scrolled.png" alt="Full offline application license scrolled with the remote"></td><td><img src="../art/screenshots/frameless-wood.png" alt="Recorded wood fire filling the screen without a surround"></td></tr></table>
