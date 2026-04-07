# CLAUDE.md — Haive Games Package

**Version**: 2.0
**Last Updated**: 2026-04-06
**Branch**: `final-refactor`

## Purpose

Haive Games provides LLM-powered game agents for turn-based board games, card games, social deduction games, and single-player puzzles. Each game has a state manager, player agents, and a unified workflow pattern (initialize → move → analyze → check_status).

## Package Structure

```
haive-games/
├── src/haive/games/
│   ├── framework/              # Base classes for all games
│   │   ├── base/               # GameAgent, GameState, GameStateManager
│   │   ├── core/               # Board, piece, move, rule, player abstractions
│   │   └── multi_player/       # MultiPlayerGameAgent + coordination
│   │
│   ├── # Two-player board games
│   ├── chess/, go/, checkers/, connect4/, reversi/, tic_tac_toe/
│   ├── mancala/, nim/, fox_and_geese/, battleship/, mastermind/
│   │
│   ├── # Multi-player social/strategy
│   ├── among_us/, mafia/, clue/, debate/, risk/
│   ├── poker/, hold_em/, dominoes/
│   │
│   ├── # Single-player puzzles
│   └── single_player/
│       ├── wordle/, flow_free/, rubiks/
│       ├── twenty_fourty_eight/, towers_of_hanoi/
│       └── (stubs: crossword, logic_grid, mine_sweeper, sudoku, word_search)
│
├── tests/                      # Per-game test dirs
├── examples/                   # Standalone usage examples
└── project_docs/               # Package-level docs

# Demos live in the main repo:
/demos/games/{14..45}_*.py     # 23 working game demos
```

## Framework Architecture

```python
# Base pattern (legacy import — works as-is, don't change)
from haive.core.engine.agent.agent import Agent

# Game agent extends Agent
class ChessAgent(GameAgent):
    config: ChessConfig

    def __init__(self, config):
        super().__init__(config)
        self.state_manager = ChessStateManager()

# State manager handles game logic
class ChessStateManager(GameStateManager[ChessState]):
    def initialize_state(self) -> ChessState: ...
    def apply_move(self, state, move) -> ChessState: ...
    def get_legal_moves(self, state) -> list[Move]: ...
    def check_game_status(self, state) -> GameStatus: ...
```

**Key classes:**
- `framework/base/agent.py` → `GameAgent` — base for all game agents
- `framework/base/state_manager.py` → `GameStateManager[T]` — generic state transitions
- `framework/base/state.py` → `GameState` — pydantic state model
- `framework/multi_player/agent.py` → `MultiPlayerGameAgent` — role-based multi-player coordination
- `framework/multi_player/state.py` → `MultiPlayerGameState` — includes `roles` dict

## Quick Start

```python
# Run a game via demo
poetry run python demos/games/31_tic_tac_toe.py
poetry run python demos/games/14_chess.py
poetry run python demos/games/28_among_us.py

# Programmatic usage
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

## Game Status (23 Working Demos)

### Two-Player Board Games (11)
| Game | Demo | State Mgr | Notes |
|------|------|-----------|-------|
| Chess | 14_chess.py | ✅ | `python-chess` dep |
| Go | 15_go.py | ✅ | `sgfmill` dep |
| Tic Tac Toe | 31_tic_tac_toe.py | ✅ | |
| Connect4 | 32_connect4.py | ✅ | |
| Checkers | 33_checkers.py | ✅ | |
| Nim | 34_nim.py | ✅ | |
| Battleship | 35_battleship.py | ✅ | |
| Reversi | 36_reversi.py | ✅ | |
| Mancala | 37_mancala.py | ✅ | |
| Mastermind | 38_mastermind.py | ✅ | |
| Fox and Geese | 40_fox_and_geese.py | ✅ | |

### Multi-Player Social/Strategy (8)
| Game | Demo | State Mgr | Notes |
|------|------|-----------|-------|
| Among Us | 28_among_us.py | ✅ | Uses `roles` field in state |
| Mafia | 41_mafia.py | ✅ | |
| Debate | 42_debate.py | ✅ | Original, working |
| Clue | 43_clue.py | ✅ | |
| Hold'em | 44_holdem.py | ✅ | |
| Dominoes | 39_dominoes.py | ✅ | |
| Poker | (no demo) | ✅ | |
| Risk | (no demo) | ✅ | |

### Single-Player (1 demo, many games)
| Game | Demo | Notes |
|------|------|-------|
| Flow Free | 45_flow_free.py | ✅ |
| Wordle, Rubiks, 2048, Towers of Hanoi | (no demos) | Full implementations |

### Category Demos
- `25_board_games.py`, `26_card_games.py`, `27_single_player.py`
- `29_strategy_games.py`, `30_social_deduction.py`

## Critical Rules

1. **Legacy import is fine**: Games use `from haive.core.engine.agent.agent import Agent` — **do NOT change to new pattern**. They work as-is.
2. **NO MOCKS**: Test with real LLMs (Azure OpenAI, OpenAI)
3. **Poetry run everything**: `poetry run python demos/games/...`
4. **State manager pattern**: All games follow `GameStateManager[T]` — initialize, apply_move, get_legal_moves, check_game_status
5. **Role-based configs**: Multi-player games use `aug_llm_configs: dict[role, AugLLMConfig]` for per-player LLM settings
6. **Among Us roles fix**: `MultiPlayerGameState` has a `roles` field — Among Us state manager must populate it

## Cleanup Applied (2026-04-06)

- ✅ Deleted `base_v2/` — all files were 0-byte stubs
- ✅ Deleted `single_player/config.py` — empty file
- ⚠️ `debate_v2/` — has 2 agent variants but no state_manager.py (incomplete)
- ⚠️ `monopoly/` — has 3+ agent files and multiple UI/config variants, no state_manager (incomplete)

## Known Issues

### Duplicate/Experimental Code
- `monopoly/` — 3 agent files (agent.py, game_agent.py, main_agent.py, player_agent.py), 3 config variants, 3 engine variants, incomplete
- `debate_v2/` — experimental rewrite with judges.py, incomplete
- Multiple UI files in some games (ui.py + ui_fixed.py or rich_ui.py) — pick canonical version if cleaning up

### Stub Games
`single_player/crossword_puzzle/`, `logic_grid/`, `mine_sweeper/`, `sudoku/`, `word_search/` — base.py exists but minimal. Either implement or leave as-is.

## Dependencies

```toml
# pyproject.toml
[tool.poetry.dependencies]
python = ">=3.12,<3.13"
haive-agents = {path = "../haive-agents", develop = true}
pydantic = "^2.0"
langchain = "*"
langgraph = "*"
sgfmill = "^1.1.1"  # for Go

[tool.poetry.group.games-chess.dependencies]
chess = "^1.11.2"
```

## Testing

```bash
# Run all tests
poetry run pytest tests/ -v

# Run specific game tests
poetry run pytest tests/games/chess/ -v

# Integration tests
poetry run pytest tests/test_all_games_end_to_end.py -v
```

## Development Workflow

```bash
# On final-refactor branch
cd packages/haive-games
git status && git diff

# Work on a game
# Edit src/haive/games/{game}/*.py
poetry run python demos/games/{demo}.py  # verify

# Commit
git add src/haive/games/{game}/
git commit -m "feat(games): <change>"
git push origin final-refactor

# Update main repo submodule ref
cd ../..
git add packages/haive-games
git commit -m "chore: update haive-games submodule"
git push origin final-refactor
```

## Writing a New Game

1. Create `src/haive/games/{name}/` with:
   - `state.py` — pydantic state model
   - `state_manager.py` — implements `GameStateManager[StateT]`
   - `config.py` — extends `GameConfig` with `aug_llm_configs`
   - `agent.py` — extends `GameAgent` or `MultiPlayerGameAgent`
   - `prompts.py` — system messages per role
   - `__init__.py` — exports

2. Add demo: `demos/games/{NN}_{name}.py`
3. Add test: `tests/games/{name}/test_{name}.py` (NO MOCKS)

## Related Docs

- Main CLAUDE.md: `@/home/will/Projects/haive/CLAUDE.md`
- Agent design: `@/home/will/Projects/haive/project_docs/guides/agent/AGENT_DESIGN_PATTERNS.md`
- Multi-agent state: `@/home/will/Projects/haive/project_docs/guides/agent/MULTIAGENT_STATE_DESIGN.md`

---

**Keep this lean. Don't touch working games — they use legacy imports but work.**
