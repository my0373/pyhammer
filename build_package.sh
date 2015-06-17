#!/usr/bin/bash

# Clean up any stale build directories
rm MANIFEST
rm -rf build
rm -rf dist

# Create the source package
python setup sdist