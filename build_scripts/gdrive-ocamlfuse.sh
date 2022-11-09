#!/usr/bin/env bash
set -exuo pipefail

#Build gapi-ocamlfuse .src.rpm
pushd ./google-drive-ocamlfuse
rpmdev-bumpspec -n "$GOOGLE_DRIVE_OCAMLFUSE_VER" -c "Update google-drive-ocamlfuse to $GOOGLE_DRIVE_OCAMLFUSE_VER" google-drive-ocamlfuse.spec
spectool -g google-drive-ocamlfuse.spec
rpmbuild -bs google-drive-ocamlfuse.spec --define "_sourcedir ." --define "_srcrpmdir ."
popd