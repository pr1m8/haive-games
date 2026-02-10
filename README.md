# haive-games
> **LLM-powered games for agent evaluation, learning, and fun.**  
> A curated suite of game environments + AI agents built on the Haive framework.

[![Python](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#license)
[![Haive](https://img.shields.io/badge/powered%20by-haive-7c3aed.svg)](https://tinyurl.com/haive-games)
[![Rich](https://img.shields.io/badge/ui-rich-10b981.svg)](https://github.com/Textualize/rich)
[![LangGraph](https://img.shields.io/badge/workflows-langgraph-f97316.svg)](https://github.com/langchain-ai/langgraph)

---

## 🚧 Status: Under Active Development

**haive-games is currently being migrated to the latest Haive framework APIs.**  
Expect breaking changes while the package converges on the unified Haive runtime + agent protocol standards.

- ✅ Core games and agents are usable today  
- 🔄 APIs, configs, and imports may change during migration  
- 🧪 Test coverage is expanding (no-mocks, real integration focus)

---

## 🎯 Overview

**Haive Games** is a comprehensive collection of **LLM-powered game agents** and **game environments** designed for:

- **Agent evaluation** in structured, rule-based settings  
- **Strategy + reasoning demonstrations** (planning, deduction, imperfect information)  
- **Multi-agent coordination experiments** (teams, tournaments, meta-controllers)  
- **Developer examples** of Haive patterns (state machines, tool use, graph workflows)

**Highlights**

- ✅ **22+ complete games** with consistent APIs  
- 🤖 **LLM-powered players** with configurable personalities and difficulty  
- 🎛️ **Rich terminal UI** with state visualization  
- 🏟️ **Tournament mode** for benchmarking and comparisons  
- 📊 **Metrics + telemetry hooks** (timing, turns, decisions)

**Project link:** https://tinyurl.com/haive-games

---

## 📦 Installation

### From PyPI

```bash
pip install haive-games
```

### With Poetry

```bash
poetry add haive-games
```

### From source (monorepo)

```bash
cd haive/packages/haive-games
pip install -e .
```

---

## 🚀 Quick Start

Below is a minimal example showing how to run two games with LLM-driven agents.

```python
from haive.games.chess import ChessAgent, ChessConfig
from haive.games.checkers import CheckersAgent, CheckersAgentConfig
from haive.core.models.llm.configs import LLMConfig

# 1) Configure LLMs for players
llm_config = LLMConfig(
    model="gpt-4",
    temperature=0.7,
    max_tokens=1000,
)

# 2) Chess
chess_config = ChessConfig(
    aug_llm_configs={
        "white_player": llm_config,
        "black_player": llm_config,
    }
)

chess_agent = ChessAgent(chess_config)
chess_result = chess_agent.run_game(visualize=True)

# 3) Checkers
checkers_config = CheckersAgentConfig(
    aug_llm_configs={
        "player1": llm_config,
        "player2": llm_config,
    }
)

checkers_agent = CheckersAgent(checkers_config)
checkers_result = checkers_agent.run_game(visualize=True)

print(f"Chess winner: {chess_result.get('winner')}")
print(f"Checkers winner: {checkers_result.get('winner')}")
```

---

## 🗂️ Game Catalog

haive-games includes a wide variety of games across multiple difficulty levels and reasoning types.

### 🏆 Classic Board Games

- **Chess** — FEN support, strategic analysis, configurable personalities  
- **Checkers** — mandatory jumps, king promotion, rich UI  
- **Go** — territory control and capture mechanics  
- **Reversi (Othello)** — flipping mechanics + positional play  
- **Clue** — mystery deduction and hypothesis tracking

### 🎯 Strategy Games

- **Tic-Tac-Toe** — position evaluation + forced wins  
- **Connect 4** — gravity-based tactics and win detection  
- **Battleship** — hidden placement, targeting, information gathering  
- **Risk** — territorial control + dice combat  
- **Mancala** — sowing/capture mechanics

### 🃏 Card Games

- **Poker** — Texas Hold’em + bluffing + hand evaluation  
- **Texas Hold’em (advanced)** — tournaments + deeper betting model  
- **Blackjack** — probabilistic play + strategy variants

### 🎭 Social Deduction

- **Among Us** — tasks, deception, voting mechanics  
- **Mafia / Werewolf** — role-based day/night play

### 🧩 Puzzle & Logic

- **Mastermind** — code-breaking via deduction  
- **Nim** — mathematical optimal play  
- **Fox and Geese** — asymmetric strategy

### 🏢 Economic

- **Monopoly** — trading + development + risk management

### 🎨 Other

- **Dominoes** — tile-matching variants  
- **Debate** — structured argumentation + scoring/judging

---

## 🧠 How the Games Are Built

Each game follows a consistent architecture designed for reuse and extensibility:

```
Game Agent (e.g., ChessAgent)
├── Configuration (GameConfig)
├── State Management (GameState, reducers, history)
├── Player Engines (LLM configs / providers)
├── Rules + Validation (legal actions, win conditions)
├── UI Layer (Rich rendering, progress, panels)
└── Workflow (graph-based game loop / stages)
```

### Core Components

1. **Agent Controller**  
   Orchestrates the game loop and delegates decisions to players.

2. **State System**  
   Tracks turns, legal moves, history, and derived information.

3. **Player Engines**  
   Configurable LLM-backed players (temperature, prompts, tool access).

4. **UI/Visualization**  
   Rich terminal UI for live play and debugging.

---

## 🏟️ Tournament Mode

Run multiple games repeatedly to compare agents, prompts, or models.

```python
from haive.games.tournament import Tournament

tournament = Tournament([
    (ChessAgent, chess_config),
    (CheckersAgent, checkers_config),
    # (ClueAgent, clue_config),
])

results = tournament.run(rounds=10)

print(f"Tournament winner: {results.winner}")
print(f"Leaderboard:\n{results.leaderboard}")
```

---

## 🎭 AI Personalities & Difficulty

Tune player behavior by adjusting LLM configuration:

```python
from haive.core.models.llm.configs import LLMConfig

aggressive = LLMConfig(
    model="gpt-4",
    temperature=0.9,
    system_prompt="Play aggressively. Take calculated risks and pressure opponents."
)

defensive = LLMConfig(
    model="gpt-4",
    temperature=0.3,
    system_prompt="Play defensively. Avoid losing positions and prioritize safety."
)

analyzer = LLMConfig(
    model="gpt-4",
    temperature=0.1,
    system_prompt="Be objective. Evaluate positions carefully and explain key ideas."
)
```

---

## 📊 Metrics & Monitoring

Many games can collect timing and decision metadata:

```python
config = ChessConfig(
    aug_llm_configs=llm_configs,
    enable_analysis=True,
    log_level="DEBUG",
    collect_metrics=True,
)

agent = ChessAgent(config)
result = agent.run_game()

metrics = result.get("metrics", {})
print("avg_move_time:", metrics.get("avg_move_time"))
print("analysis_calls:", metrics.get("analysis_calls"))
```

---

## 🧪 Testing

haive-games follows a **production-style testing approach**, favoring real components whenever possible.

```bash
# Run all tests
poetry run pytest packages/haive-games/tests/ -v

# Run a specific game test suite
poetry run pytest packages/haive-games/tests/test_chess/ -v
```

Lint / format:

```bash
poetry run ruff check packages/haive-games/src/
poetry run black packages/haive-games/src/
```

---

## 📁 Package Structure

```
haive-games/
├── src/haive/games/           # Game implementations
│   ├── chess/
│   ├── checkers/
│   ├── go/
│   ├── among_us/
│   ├── mafia/
│   └── ...
├── examples/                  # Demo scripts and usage patterns
├── tests/                     # Game + integration tests
└── project_docs/              # Guides, architecture notes, and references
```

---

## 🧩 Adding a New Game

1. Create a game directory:
   `src/haive/games/your_game/`

2. Implement the required components:
   - `agent.py` — main controller
   - `config.py` — configuration models
   - `state.py` — state + reducers + transitions
   - `models.py` — structured models used by state/actions
   - `README.md` — game docs + examples

3. Add tests:
   `tests/test_your_game/`

4. Register it in the package index (if applicable)

---

## 🗺️ Roadmap

- 🎛️ Unified agent config for all games
- 🧠 Better evaluation harness + standardized metrics output
- 🏟️ Multi-league tournaments (ELO / TrueSkill)
- 🖥️ Optional web UI for select games
- 🔌 Tight integration with Haive MCP + tool ecosystems

---

## 🤝 Contributing

Contributions are welcome:

1. Fork the repository  
2. Create a feature branch  
3. Add tests for changes  
4. Ensure formatting + lint passes  
5. Open a PR

---

## 📄 License

MIT License — see `LICENSE`.

---

## 🔗 Support

- Issues: open a GitHub issue on the Haive monorepo (or relevant package repo)
- Docs: see the Haive documentation hub
