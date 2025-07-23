#!/bin/bash

# Set up PYTHONPATH to include all package src directories
export PYTHONPATH="/home/will/Projects/haive/backend/haive/packages/haive-core/src:/home/will/Projects/haive/backend/haive/packages/haive-agents/src:/home/will/Projects/haive/backend/haive/packages/haive-tools/src:/home/will/Projects/haive/backend/haive/packages/haive-games/src:/home/will/Projects/haive/backend/haive/packages/haive-dataflow/src:/home/will/Projects/haive/backend/haive/packages/haive-prebuilt/src"

# Get the directory of this script
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change to the script directory
cd "${DIR}" || exit

# Run the example with the specified arguments
python enhanced_example.py "$@"
