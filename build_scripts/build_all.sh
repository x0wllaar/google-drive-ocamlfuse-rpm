#!/usr/bin/env bash
set -exuo pipefail

#Set environment vars
source ./build_scripts/versions_config.sh

#Build tiny_httpd
./build_scripts/tiny-httpd.sh

#Build ocamlfuse .src.rpm
./build_scripts/ocamlfuse.sh

#Build gapi-ocaml .src.rpm
./build_scripts/gapi-ocaml.sh

#Build google-drive-ocamlfuse .src.rpm
./build_scripts/gdrive-ocamlfuse.sh

#Copy src rpms into a folder
mkdir -p ./src_rpms/
cp ./tiny-httpd-ocaml/*.src.rpm ./src_rpms/
cp ./gapi-ocaml/*.src.rpm ./src_rpms/
cp ./google-drive-ocamlfuse/*.src.rpm ./src_rpms/
cp ./ocamlfuse/*.src.rpm ./src_rpms/

#Build src rpms into normal rpms
./build_scripts/srcrpm-build.sh

#Copy built RPMs to the host
cp -v /root/rpmbuild/RPMS/$(arch)/*.rpm /rpms