#!/usr/bin/env bash
set -exuo pipefail

IMAGE_NAME="rpm-builder"

rm -rf ./rpms
mkdir ./rpms

podman build -f ./Dockerfile -t "$IMAGE_NAME"

podman run -it --rm -v "$(pwd)"/rpms:/rpms:rw -v "$(pwd)":/buildfiles:ro "$IMAGE_NAME" || true