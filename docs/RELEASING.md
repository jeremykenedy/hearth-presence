# Releasing

Run all local checks and required CI for the exact intended commit. Verify native
playback, settings, dream lifecycle, remote exit, screenshots and privacy first.
Keep device-specific gaps explicit in VERIFICATION.md. Preserve the signing key.

Fetch origin, verify main is the remote default branch, and require the checked-out
commit to match origin/main. Build the production APK on that commit, check the
package, version, dream metadata and signer, then create the matching SemVer tag.
Publish only from that verified remote primary tip. Never move an existing tag.

Attach build/hearth-presence.apk and build/hearth-presence.apk.sha256, with notes
covering upgrade, breaking changes, major changes, minor fixes and device evidence.
Download the published files and verify the checksum. Integrate the exact package,
dream component, asset name, hash and reviewed preview into Toolkit and Fire TV UI.
Update About, homepage and topics. Never publish CI review builds as production.
