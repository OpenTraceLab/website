#!/bin/bash

# Deploy script for OpenTraceLab website
# Deploys main content with versioning and hardware docs without versioning

set -e

VERSION=${1:-"latest"}
PUSH=${2:-"--push"}

echo "Deploying OpenTraceLab website..."
echo "Version: $VERSION"

# Deploy versioned content (without hardware)
echo "Building and deploying versioned content..."
mike deploy --config-file mkdocs-versioned.yml $VERSION $PUSH

# Build hardware docs separately (unversioned)
echo "Building hardware documentation..."
mkdocs build --config-file mkdocs-hardware.yml --site-dir site-hardware

# Copy hardware docs to gh-pages branch at /hardware path
echo "Deploying hardware documentation..."
git checkout gh-pages
mkdir -p hardware
cp -r site-hardware/* hardware/
git add hardware/
git commit -m "Update hardware documentation" || echo "No changes to hardware docs"
git checkout main

echo "Deployment complete!"
echo "Main docs: versioned at /$VERSION"
echo "Hardware docs: unversioned at /hardware"
