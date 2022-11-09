#!/usr/bin/env bash
set -exuo pipefail

echo "Copying build files to container"
mkdir -p /tmp/rpmbuilder
cp -Rv /buildfiles/* /tmp/rpmbuilder

echo "Starting build"
pushd /tmp/rpmbuilder
./build_scripts/build_all.sh
popd