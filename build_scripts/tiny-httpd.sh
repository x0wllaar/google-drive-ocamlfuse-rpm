#!/usr/bin/env bash
set -exuo pipefail

#Build ocamlfuse .src.rpm
pushd /build/gdfs/tiny-httpd-ocaml
spectool -g tiny-httpd-ocaml.spec
rpmbuild -bs tiny-httpd-ocaml.spec --define "_sourcedir ." --define "_srcrpmdir ."
popd
