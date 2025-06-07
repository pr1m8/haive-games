#!/bin/bash
# Debug game runner for haive - shows all output

# Check if game name is provided
if [ -z "$1" ]; then
    echo "Usage: ./run-debug.sh <game_name>"
    echo "Available games: fox_and_geese, hold_em"
    exit 1
fi

# Enable all debug output
export HAIVE_DEBUG_CONFIG=1
export HAIVE_TRACK_PRINTS=1
export HAIVE_DEV=1
export HAIVE_LOG_LEVEL=DEBUG

# Set USER_AGENT to avoid warning
export USER_AGENT="haive-games/1.0"

# Run the game
exec python -m haive.games.$1.example "$@" 