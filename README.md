# Haive Games

Comprehensive collection of AI-powered game implementations for the Haive framework.

## Overview

Haive Games is a sophisticated package that provides 22 different game implementations, each featuring AI agents powered by large language models (LLMs). These games serve as both entertainment and educational tools, demonstrating advanced AI capabilities in structured, rule-based environments.

**Key Features:**

- **22 Complete Games**: From classic board games to modern social deduction games
- **LLM-Powered AI**: Agents that use strategic reasoning and natural language understanding
- **Rich Visualizations**: Beautiful terminal interfaces with colors, animations, and game state displays
- **Configurable Difficulty**: Adjustable AI behavior and game parameters
- **Tournament Support**: Multi-game competitions and performance analysis
- **Educational Value**: Game theory concepts and AI strategy demonstrations

## Game Categories

### 🏆 **Classic Board Games**

- **[Chess](src/haive/games/chess/)**: Complete chess with FEN notation, strategic analysis, and multiple AI personalities
- **[Checkers](src/haive/games/checkers/)**: American checkers with mandatory jumps, king promotion, and rich UI
- **[Go](src/haive/games/go/)**: Ancient strategy game with territory control and capture mechanics
- **[Reversi](src/haive/games/reversi/)**: Othello-style game with flipping mechanics
- **[Clue](src/haive/games/clue/)**: Mystery deduction game with logical reasoning and hypothesis tracking

### 🎯 **Strategy Games**

- **[Tic-Tac-Toe](src/haive/games/tic_tac_toe/)**: Classic 3x3 game with strategic analysis and position evaluation
- **[Connect 4](src/haive/games/connect4/)**: Gravity-based connection game with win detection
- **[Battleship](src/haive/games/battleship/)**: Naval combat with hidden ship placement and strategic targeting
- **[Risk](src/haive/games/risk/)**: World domination through territorial control and dice combat
- **[Mancala](src/haive/games/mancala/)**: Ancient seed-sowing game with capture mechanics

### 🃏 **Card Games**

- **[Poker](src/haive/games/poker/)**: Texas Hold'em with betting, bluffing, and hand evaluation
- **[Texas Hold'em](src/haive/games/hold_em/)**: Advanced poker implementation with tournament support
- **[Blackjack](src/haive/games/cards/blackjack/)**: Classic card game with card counting strategies

### 🎭 **Social Deduction Games**

- **[Among Us](src/haive/games/among_us/)**: Find the impostor with task completion and voting mechanics
- **[Mafia](src/haive/games/mafia/)**: Day/night phases with role-based gameplay
- **[Werewolf](src/haive/games/mafia/)**: Classic social deduction with special roles

### 🧩 **Puzzle & Logic Games**

- **[Mastermind](src/haive/games/mastermind/)**: Code-breaking game with logical deduction
- **[Nim](src/haive/games/nim/)**: Mathematical strategy game with pile manipulation
- **[Fox and Geese](src/haive/games/fox_and_geese/)**: Asymmetric strategy game

### 🏢 **Economic Games**

- **[Monopoly](src/haive/games/monopoly/)**: Property trading and development with economic strategy

### 🎨 **Other Games**

- **[Dominoes](src/haive/games/dominoes/)**: Tile-matching game with multiple variants
- **[Debate](src/haive/games/debate/)**: Structured argumentation with scoring and judging

## Installation

```bash
# Install from PyPI
pip install haive-games

# Or install from source
cd haive/packages/haive-games
pip install -e .
```

## Quick Start

```python
from haive.games.chess import ChessAgent, ChessConfig
from haive.games.checkers import CheckersAgent, CheckersAgentConfig
from haive.core.models.llm.configs import LLMConfig

# Configure LLM for game agents
llm_config = LLMConfig(
    model="gpt-4",
    temperature=0.7,
    max_tokens=1000
)

# Play chess
chess_config = ChessConfig(
    aug_llm_configs={
        "white_player": llm_config,
        "black_player": llm_config
    }
)
chess_agent = ChessAgent(chess_config)
chess_result = chess_agent.run_game(visualize=True)

# Play checkers
checkers_config = CheckersAgentConfig(
    aug_llm_configs={
        "player1": llm_config,
        "player2": llm_config
    }
)
checkers_agent = CheckersAgent(checkers_config)
checkers_result = checkers_agent.run_game(visualize=True)

print(f"Chess winner: {chess_result.get('winner')}")
print(f"Checkers winner: {checkers_result.get('winner')}")
```

## Architecture

All games follow a consistent architectural pattern:

```
Game Agent (e.g., ChessAgent)
├── Configuration (ChessConfig)
├── State Management (ChessState, StateManager)
├── LLM Engines (player engines, analyzer engines)
├── Game Logic (rule enforcement, move validation)
├── UI Components (rich terminal visualization)
└── Workflow (LangGraph-based game flow)
```

### Core Components

1. **Game Agent**: Main controller using LangGraph workflow
2. **State Management**: Game state tracking and history
3. **LLM Engines**: AI players with different personalities
4. **UI Components**: Rich terminal interfaces
5. **Configuration**: Customizable game parameters

## Advanced Features

### Tournament System

```python
from haive.games.tournament import Tournament

# Create tournament with multiple games
tournament = Tournament([
    (ChessAgent, chess_config),
    (CheckersAgent, checkers_config),
    (ClueAgent, clue_config)
])

# Run tournament
results = tournament.run(rounds=10)
print(f"Tournament winner: {results.winner}")
```

### AI Personality Configuration

```python
# Aggressive player
aggressive_config = LLMConfig(
    model="gpt-4",
    temperature=0.9,
    system_prompt="You are an aggressive player who takes calculated risks."
)

# Defensive player
defensive_config = LLMConfig(
    model="gpt-4",
    temperature=0.3,
    system_prompt="You are a defensive player who prioritizes safety."
)

# Strategic analyzer
analyzer_config = LLMConfig(
    model="gpt-4",
    temperature=0.1,
    system_prompt="You are a strategic analyzer who evaluates positions objectively."
)
```

### Performance Monitoring

```python
# Enable detailed logging and analysis
config = ChessConfig(
    aug_llm_configs=llm_configs,
    enable_analysis=True,
    log_level="DEBUG",
    collect_metrics=True
)

agent = ChessAgent(config)
result = agent.run_game()

# Access performance metrics
metrics = result.get('metrics', {})
print(f"Average move time: {metrics.get('avg_move_time')}")
print(f"Total analysis calls: {metrics.get('analysis_calls')}")
```

## Documentation

Each game includes comprehensive documentation:

- **README.md**: Complete game overview and usage examples
- **API Reference**: Detailed class and method documentation
- **Strategy Guides**: Game theory concepts and AI tactics
- **Configuration Options**: All available settings and parameters

## Game Statistics

- **Total Games**: 22 complete implementations
- **2-Player Games**: 15 games
- **Multi-Player Games**: 7 games
- **Card Games**: 3 games
- **Board Games**: 8 games
- **Strategy Games**: 5 games
- **Social Deduction**: 3 games

## Requirements

- Python 3.8+
- Haive Core Framework
- LangChain for LLM integration
- Rich for terminal UI
- Pydantic for data validation

## Development

```bash
# Install development dependencies
poetry install --extras dev

# Run tests
poetry run pytest packages/haive-games/tests/ -v

# Run specific game tests
poetry run pytest packages/haive-games/tests/test_chess/ -v

# Lint code
poetry run ruff check packages/haive-games/src/

# Format code
poetry run black packages/haive-games/src/
```

## Contributing

We welcome contributions! See our [Contributing Guide](../../CONTRIBUTING.md) for details.

### Adding New Games

1. Create game directory: `src/haive/games/your_game/`
2. Implement required components:
   - `agent.py`: Main game agent
   - `config.py`: Configuration class
   - `state.py`: Game state management
   - `models.py`: Data models
   - `README.md`: Documentation
3. Add tests in `tests/test_your_game/`
4. Update this README

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Support

For questions and support:

- 📧 Email: support@haive.ai
- 🐛 Issues: [GitHub Issues](https://github.com/pr1m8/haive/issues)
- 📚 Documentation: [Full Documentation](https://docs.haive.ai)

## Citation

If you use Haive Games in your research, please cite:

```bibtex
@software{haive_games,
  title={Haive Games: AI-Powered Game Implementations},
  author={Haive Team},
  year={2024},
  url={https://github.com/pr1m8/haive}
}
```
