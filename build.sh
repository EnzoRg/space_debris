#!/bin/bash

set -e

IMAGE_NAME="space-debris-2026"
TAG="dev"

echo "Building ${IMAGE_NAME}:${TAG}..."

docker build -f Dockerfile -t ${IMAGE_NAME}:${TAG} .

echo "Build completed."