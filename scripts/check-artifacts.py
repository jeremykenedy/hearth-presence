#!/usr/bin/env python3
"""Check media notices, XML and required app metadata before building."""
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET
root = Path(__file__).resolve().parent.parent
for path in list((root / 'res').rglob('*.xml')) + list((root / 'art').glob('*.svg')):
    ET.parse(path)
manifest = ET.parse(root / 'AndroidManifest.xml').getroot()
ns = '{http://schemas.android.com/apk/res/android}'
service = manifest.find('application/service')
assert manifest.attrib['package'] == 'com.jeremykenedy.hearthpresence'
assert service.attrib[ns + 'permission'] == 'android.permission.BIND_DREAM_SERVICE'
assert service.attrib[ns + 'name'] == '.HearthDreamService'
assert not manifest.findall('uses-permission')
assert 'CC BY-SA 4.0' in (root / 'NOTICE').read_text()
for asset in ('wood.mp4', 'gas.mp4', 'linear.mp4', 'crackle.m4a'):
    assert (root / 'res/raw' / asset).stat().st_size > 10000
for item in json.loads((root / 'media/manifest.json').read_text()):
    path = root / item['file']
    assert path.stat().st_size == item['bytes'], path
    assert hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256'], path
print('App metadata, media notices, XML and SVG checks passed.')
