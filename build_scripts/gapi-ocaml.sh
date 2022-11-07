#!/usr/bin/env bash
set -exuo pipefail

#Build gapi-ocaml .src.rpm
pushd /build/gdfs/gapi-ocaml
rpmdev-bumpspec -n "$GAPI_OCAML_VER" -c "Update gapi-ocaml to $GAPI_OCAML_VER" gapi-ocaml.spec
spectool -g gapi-ocaml.spec
rpmbuild -bs gapi-ocaml.spec --define "_sourcedir ." --define "_srcrpmdir ."
popd