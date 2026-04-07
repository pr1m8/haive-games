# haive-games

[![PyPI version](https://img.shields.io/pypi/v/haive-games.svg)](https://pypi.org/project/haive-games/)
[![Python Versions](https://img.shields.io/pypi/pyversions/haive-games.svg)](https://pypi.org/project/haive-games/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/pr1m8/haive-games/actions/workflows/ci.yml/badge.svg)](https://github.com/pr1m8/haive-games/actions/workflows/ci.yml)
[![Docs](https://github.com/pr1m8/haive-games/actions/workflows/docs.yml/badge.svg)](https://pr1m8.github.io/haive-games/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/haive-games.svg)](https://pypi.org/project/haive-games/)

**LLM-powered game agents** for chess, Go, poker, social deduction, and 20+ other games.

A curated suite of game environments where LLM agents play against each other (or themselves). Each game has a state manager, role-based player agents, and a unified workflow.

## Installation

```bash
pip install haive-games

# For Chess support:
pip install haive-games[games-chess]

# For Go support:
pip install haive-games[go]
```

## Features

### 🎮 23 Working Games

**Two-player board games:**
- ♟️ Chess, Go, Checkers, Connect4, Reversi, Tic Tac Toe
- 🎲 Mancala, Nim, Fox and Geese, Battleship, Mastermind

**Multi-player social/strategy:**
- 🕵️ Among Us, Mafia, Clue, Debate
- 🃏 Poker, Hold'em, Dominoes
- 🌍 Risk

**Single-player puzzles:**
- 🟢 Flow Free, Wordle, Rubiks, 2048, Towers of Hanoi

### 🏗️ Framework
- **GameAgent** — base class for all game agents
- **GameStateManager[T]** — generic state transitions (initialize, apply_move, get_legal_moves, check_game_status)
- **MultiPlayerGameAgent** — role-based multi-player coordination

## Quick Start

```python
from haive.games.chess.agent import ChessAgent
from haive.games.chess.config import ChessConfig
from haive.core.engine.aug_llm import AugLLMConfig

config = ChessConfig(
    aug_llm_configs={
        "white": AugLLMConfig(temperature=0.3),
        "black": AugLLMConfig(temperature=0.3),
    }
)

agent = ChessAgent(config)
result = agent.run_game()
```

## Run a Demo

```bash
# Two-player games
poetry run python demos/games/14_chess.py
poetry run python demos/games/31_tic_tac_toe.py
poetry run python demos/games/33_checkers.py

# Multi-player social
poetry run python demos/games/28_among_us.py
poetry run python demos/games/41_mafia.py

# Single-player puzzles
poetry run python demos/games/45_flow_free.py
```

## Documentation

📖 **Full documentation:** https://pr1m8.github.io/haive-games/

## Related Packages

| Package | Description |
|---------|-------------|
| [haive-core](https://pypi.org/project/haive-core/) | Foundation: engines, graphs |
| [haive-agents](https://pypi.org/project/haive-agents/) | Production agents |

## License

MIT © [pr1m8](https://github.com/pr1m8)
