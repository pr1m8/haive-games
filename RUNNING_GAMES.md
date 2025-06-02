# Running Haive Games

This directory contains example implementations of games using the Haive framework.

## Quick Start

We provide convenient shell scripts to run games with different verbosity levels:

### Clean Run (Recommended)

For the cleanest output, use the `run.sh` script:

```bash
./run.sh fox_and_geese
./run.sh hold_em
```

This will:

- Suppress all debug output from the framework
- Show only game-relevant information
- Hide rich console panels and debug messages

### Debug Run

For debugging and development, use the `run-debug.sh` script:

```bash
./run-debug.sh fox_and_geese
./run-debug.sh hold_em
```

This will:

- Show all debug output
- Display rich console panels with configuration details
- Track print statements with source information
- Enable verbose logging

### Manual Run

You can also run games manually with custom settings:

```bash
# Clean run
HAIVE_NO_RICH=1 HAIVE_LOG_QUIET=1 python -m haive.games.fox_and_geese.example

# Debug run
HAIVE_DEBUG_CONFIG=1 HAIVE_DEV=1 python -m haive.games.fox_and_geese.example
```

## Environment Variables

You can control the logging output with these environment variables:

- `HAIVE_NO_RICH` - Disable rich console output (panels, trees, etc.)
- `HAIVE_LOG_QUIET` - Suppress most logging output
- `HAIVE_DEBUG_CONFIG` - Show debug output from configuration modules
- `HAIVE_DEV` or `DEBUG` - Enable developer mode with print tracking
- `HAIVE_TRACK_PRINTS` - Track print() statements with source info
- `HAIVE_LOG_LEVEL` - Set logging level (DEBUG, INFO, WARNING, ERROR)
- `USER_AGENT` - Set to avoid langchain warning

## Available Games

1. **Fox and Geese** - A strategy board game

   - Run: `./run.sh fox_and_geese`
   - Location: `haive.games.fox_and_geese.example`

2. **Texas Hold'em** - Poker game implementation
   - Run: `./run.sh hold_em`
   - Location: `haive.games.hold_em.test`

## Tips

1. Use `./run.sh` for normal gameplay
2. Use `./run-debug.sh` when developing or debugging
3. Set `USER_AGENT` to avoid langchain warnings
4. The games will create visualization files in `graph_visualizations/`
