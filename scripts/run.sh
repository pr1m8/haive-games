#!/bin/bash
# Clean game runner for haive

# Check if game name is provided
if [[ -z $1 ]]; then
	echo "Usage: ./run.sh <game_name>"
	echo "Available games: fox_and_geese, hold_em"
	exit 1
fi

# Disable all the noisy output
export HAIVE_NO_RICH=1
export HAIVE_LOG_QUIET=1

# Set USER_AGENT to avoid warning
export USER_AGENT="haive-games/1.0"

# Run the game
exec python -m haive.games."$1".example "$@"
