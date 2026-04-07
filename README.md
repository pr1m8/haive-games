# haive-games

[![PyPI version](https://img.shields.io/pypi/v/haive-games.svg)](https://pypi.org/project/haive-games/)
[![Python Versions](https://img.shields.io/pypi/pyversions/haive-games.svg)](https://pypi.org/project/haive-games/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/pr1m8/haive-games/actions/workflows/ci.yml/badge.svg)](https://github.com/pr1m8/haive-games/actions/workflows/ci.yml)
[![Docs](https://github.com/pr1m8/haive-games/actions/workflows/docs.yml/badge.svg)](https://pr1m8.github.io/haive-games/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/haive-games.svg)](https://pypi.org/project/haive-games/)

**LLM-powered game agents** for chess, Go, poker, social deduction, and 20+ other games.

A curated suite of game environments where LLM agents play against each other (or themselves). Each game is a complete implementation: state manager, role-based player agents, prompt templates, and end-to-end workflows. Use it for **agent evaluation**, **reinforcement learning research**, **multi-agent benchmarks**, or just **fun**.

---

## Why haive-games?

LLM agents need environments to be evaluated in. Traditional benchmarks (MMLU, HumanEval) test knowledge and code, but not strategic reasoning, social deduction, or long-horizon planning. Games are an ideal test bed:

- **Strategic depth** — Chess, Go, Risk test long-term planning
- **Social reasoning** — Mafia, Among Us, Clue test deception, trust, and inference
- **Hidden information** — Poker, Battleship test reasoning under uncertainty
- **Cooperation** — Debate, Hold'em test negotiation and coordination
- **Bounded scope** — Each game has clear rules, a defined state space, and measurable outcomes

`haive-games` provides 23 working game environments with the framework already built. You configure the LLMs, run a game, and get a complete trace.

---

## Framework Architecture

Every game follows the same pattern. Three core abstractions:

### GameStateManager[T]

Generic state transition manager. Each game implements four methods:

```python
class ChessStateManager(GameStateManager[ChessState]):
    def initialize_state(self) -> ChessState:
        """Create starting state."""
        return ChessState(board=chess.Board())

    def apply_move(self, state: ChessState, move: Move) -> ChessState:
        """Apply a move and return new state."""
        new_board = state.board.copy()
        new_board.push(move.to_chess_move())
        return state.copy(update={"board": new_board})

    def get_legal_moves(self, state: ChessState) -> list[Move]:
        """Return all legal moves for current player."""
        return [Move.from_chess_move(m) for m in state.board.legal_moves]

    def check_game_status(self, state: ChessState) -> GameStatus:
        """Check if game is over and who won."""
        if state.board.is_checkmate():
            return GameStatus(over=True, winner="white" if state.board.turn == chess.BLACK else "black")
        return GameStatus(over=False)
```

### GameAgent

Base class for game agents. Implements the standard workflow:

```
initialize → loop:
    current_player.move(state) → apply_move → analyze → check_status → break_if_over
```

### MultiPlayerGameAgent

Extension for multi-player games with role-based player configs. Each role gets its own `AugLLMConfig` (so you can have GPT-4 play white and Claude play black, for example).

---

## Game Catalog (23 Working Demos)

### 🏁 Two-Player Board Games

**Chess** — Full chess with `python-chess`. White vs Black, legal move generation, checkmate detection.
```bash
poetry run python demos/games/14_chess.py
```

**Go** — 9x9 or 19x19 board with `sgfmill`. Territory scoring, ko rule, capture detection.
```bash
poetry run python demos/games/15_go.py
```

**Other:** Tic Tac Toe, Connect4, Checkers, Reversi (Othello), Mancala, Nim, Fox and Geese, Battleship, Mastermind.

### 🕵️ Multi-Player Social Deduction

**Among Us** — Players have roles (crewmate, impostor). Tasks, voting, sabotage, discussion. Tests deception and inference.

**Mafia** — Classic werewolf-style game. Day/night cycles, voting, role abilities.

**Clue** — Murder mystery deduction. Players make accusations and eliminate possibilities.

**Debate** — Structured argumentation. Tests persuasion and counter-argument generation.

### 🃏 Multi-Player Card/Strategy

**Hold'em** — Texas Hold'em poker. Betting rounds, hand evaluation, bluffing.

**Poker** — General poker variants.

**Dominoes** — Tile-based game with chains.

**Risk** — Strategy game with territory control and battles.

### 🟢 Single-Player Puzzles

**Flow Free** — Connect colored dots without crossing paths.

**Wordle** — Word guessing with feedback.

**Rubiks Cube** — Cube solving (uses real cube state).

**2048** — Sliding tile puzzle.

**Towers of Hanoi** — Classic disk-moving puzzle.

---

## Quick Start

### Run a Demo

```bash
# Install
pip install haive-games

# For Chess support:
pip install haive-games[games-chess]

# For Go support:
pip install haive-games[go]

# Run any demo from the parent repo
poetry run python demos/games/14_chess.py
poetry run python demos/games/28_among_us.py
poetry run python demos/games/41_mafia.py
```

### Programmatic Usage

```python
from haive.games.chess.agent import ChessAgent
from haive.games.chess.config import ChessConfig
from haive.core.engine.aug_llm import AugLLMConfig

# Configure both players
config = ChessConfig(
    aug_llm_configs={
        "white": AugLLMConfig(
            temperature=0.3,
            system_message="You are a chess grandmaster playing white.",
            model="gpt-4o",
        ),
        "black": AugLLMConfig(
            temperature=0.3,
            system_message="You are a chess grandmaster playing black.",
            model="claude-opus-4-6",
        ),
    }
)

# Run a game
agent = ChessAgent(config)
result = agent.run_game()

# Inspect the result
print(f"Winner: {result.winner}")
print(f"Moves: {len(result.move_history)}")
print(f"Final board:\n{result.final_state.board}")
```

### Multi-Player Game with Roles

```python
from haive.games.among_us.agent import AmongUsAgent
from haive.games.among_us.config import AmongUsConfig

config = AmongUsConfig(
    n_players=8,
    n_impostors=2,
    aug_llm_configs={
        "crewmate": AugLLMConfig(temperature=0.5),
        "impostor": AugLLMConfig(temperature=0.7),  # More creative
    }
)

agent = AmongUsAgent(config)
result = agent.run_game()
```

---

## Use Cases

### Agent Evaluation

Compare different LLMs head-to-head:

```python
gpt4 = AugLLMConfig(model="gpt-4o")
claude = AugLLMConfig(model="claude-opus-4-6")

config = ChessConfig(aug_llm_configs={"white": gpt4, "black": claude})
results = [ChessAgent(config).run_game() for _ in range(10)]
gpt4_wins = sum(1 for r in results if r.winner == "white")
print(f"GPT-4 won {gpt4_wins}/10 games as white")
```

### Strategic Reasoning Benchmarks

Use Chess, Go, or Risk to test long-horizon planning capabilities. The state manager provides ground-truth legal moves and outcomes.

### Social Deduction Research

Among Us, Mafia, and Clue are ideal for testing theory of mind, deception, and Bayesian reasoning under uncertainty.

### Creative Writing Evaluation

Use Debate to evaluate persuasion. Use Social Media Conversation to test personality consistency.

---

## Writing a New Game

The framework makes it straightforward:

1. **State** — `state.py` with a Pydantic model
2. **State Manager** — `state_manager.py` implementing `GameStateManager[T]`
3. **Config** — `config.py` extending `GameConfig` with `aug_llm_configs`
4. **Agent** — `agent.py` extending `GameAgent` or `MultiPlayerGameAgent`
5. **Prompts** — `prompts.py` with role-specific system messages
6. **Demo** — `demos/games/{NN}_{name}.py`

See `src/haive/games/tic_tac_toe/` for a minimal example or `src/haive/games/chess/` for a complex one.

---

## Installation

```bash
pip install haive-games

# With chess support
pip install haive-games[games-chess]

# With Go support
pip install haive-games[go]
```

---

## Documentation

📖 **Full documentation:** https://pr1m8.github.io/haive-games/

---

## Related Packages

| Package | Description |
|---------|-------------|
| [haive-core](https://pypi.org/project/haive-core/) | Foundation: engines, graphs |
| [haive-agents](https://pypi.org/project/haive-agents/) | Production agents (used by game agents) |

---

## License

MIT © [pr1m8](https://github.com/pr1m8)
