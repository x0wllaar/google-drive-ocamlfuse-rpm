#!/usr/bin/env bash
set -exuo pipefail

rm -rf ./rpms
mkdir ./rpms

podman build -f ./Dockerfile
IMAGE_NAME="$(podman build -q -f ./Dockerfile)"

podman run -it --rm --mount type=bind,source="$(pwd)"/rpms,target=/rpms "$IMAGE_NAME" ./build_scripts/build_all.sh || true
podman image rm "$IMAGE_NAME"