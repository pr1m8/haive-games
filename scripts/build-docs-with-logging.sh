#!/bin/bash

# Build documentation with full logging
echo "Building Sphinx documentation with logging..."

# Create logs directory if it doesn't exist
mkdir -p docs/logs

# Clean previous build
rm -rf docs/build

# Build with full logging
cd docs || exit
sphinx-build -b html source build/html --keep-going 2>&1 | tee logs/sphinx-build-$(date +%Y%m%d-%H%M%S).log

# Count errors
echo ""
echo "=== Build Summary ==="
echo "Total warnings/errors:"
grep -c "WARNING\|ERROR" logs/sphinx-build-*.log | tail -1

echo ""
echo "Unexpected indentation errors:"
grep -c "Unexpected indentation" logs/sphinx-build-*.log | tail -1

echo ""
echo "Latest log file:"
ls -t logs/sphinx-build-*.log | head -1
