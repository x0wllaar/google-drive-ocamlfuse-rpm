#!/usr/bin/env bash
set -exuo pipefail

#Build ocamlfuse .src.rpm
pushd /build/gdfs/ocamlfuse
rpmdev-bumpspec -n "$OCAML_FUSE_VER" -c "Update ocamlfuse to $OCAML_FUSE_VER" ocamlfuse.spec
spectool -g ocamlfuse.spec
rpmbuild -bs ocamlfuse.spec --define "_sourcedir ." --define "_srcrpmdir ."
popd
