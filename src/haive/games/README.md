# Haive Games

## Overview

The Haive Games module provides a comprehensive framework for creating and running AI agent-based games. It includes implementations of classic games like Chess, Poker, and Monopoly, as well as novel AI-specific games like debate and social deduction games. The framework enables researchers and developers to evaluate AI capabilities, test multi-agent interactions, and explore emergent behaviors in competitive and cooperative environments.

## Key Features

- **Game Framework**: Reusable components for building new games with minimal boilerplate
- **Multi-Agent Support**: Infrastructure for games with 2+ players and complex interaction patterns
- **State Management**: Robust game state tracking, validation, and progression
- **Agent Integration**: Seamless integration with LLM-based agents for decision making
- **Visualization**: Tools for rendering game states and agent interactions
- **Evaluation**: Benchmarking and metrics for comparing agent performance
- **Configurability**: Flexible configuration for customizing game parameters

## Installation

This module is part of the `haive-games` package. Install it with:

```bash
pip install haive-games
```

Or install via Poetry:

```bash
poetry add haive-games
```

## Quick Start

### Playing a Simple Game

```python
from haive.games.tic_tac_toe import TicTacToeAgent, TicTacToeConfig
from haive.core.engine.aug_llm import AugLLMConfig

# Configure the game
config = TicTacToeConfig(
    player_names=["Player 1", "Player 2"],
    llm_config=AugLLMConfig(
        system_message="You are playing Tic Tac Toe. Make strategic moves to win.",
        temperature=0.2
    )
)

# Create and run the game
agent = TicTacToeAgent(config)
result = agent.run()

# View the results
print(f"Winner: {result.winner}")
print(f"Game history: {result.moves}")
```

### Creating a Custom Game

```python
from haive.games.framework import GameAgent, GameConfig, GameState, GameStateManager
from pydantic import Field
from typing import List

# Define game-specific models
class MyGameState(GameState):
    score: int = Field(default=0)
    rounds: int = Field(default=0)

class MyGameConfig(GameConfig):
    max_rounds: int = Field(default=10)
    difficulty: str = Field(default="medium")

# Create state manager for game logic
class MyGameStateManager(GameStateManager):
    def initialize_state(self) -> MyGameState:
        return MyGameState()

    def is_game_over(self, state: MyGameState) -> bool:
        return state.rounds >= self.config.max_rounds

    def process_move(self, state: MyGameState, move: dict) -> MyGameState:
        # Game-specific move processing
        state.rounds += 1
        return state

# Create the game agent
class MyGameAgent(GameAgent):
    def __init__(self, config: MyGameConfig):
        super().__init__(config)
        self.state_manager = MyGameStateManager(config)

    def run(self):
        state = self.state_manager.initialize_state()

        while not self.state_manager.is_game_over(state):
            # Game turn logic
            move = self.get_agent_move(state)
            state = self.state_manager.process_move(state, move)

        return state
```

## Game Catalog

The package includes implementations for the following games:

### Classic Games

- **Chess**: Complete chess implementation with LLM-based reasoning
- **Poker**: Texas Hold'em with betting, hand evaluation, and bluffing
- **Monopoly**: Property management and economic strategy
- **Tic-Tac-Toe**: Simple grid-based game for quick testing
- **Go**: Ancient strategy board game
- **Nim**: Mathematical strategy game
- **Battleship**: Grid-based search game
- **Mancala**: Stone collection strategy game
- **Connect4**: Vertical grid connection game
- **Mastermind**: Code-breaking logic game
- **Reversi/Othello**: Disk flipping territory game

### Novel AI Games

- **Among Us**: Social deduction game with deception and reasoning
- **Debate**: Structured argumentation with judges and rebuttals
- **Mafia/Werewolf**: Social deduction with hidden roles
- **Clue/Cluedo**: Mystery solving with evidence collection

### Single Player Games

- **Wordle**: Word guessing game
- **2048**: Tile sliding puzzle
- **Word Search**: Grid-based word finding

## Framework Architecture

The games framework is organized into several key components:

### Base Classes

- **GameAgent**: Core agent class that manages the game flow
- **GameState**: Data model for the current game state
- **GameStateManager**: Handles state transitions and game logic
- **GameConfig**: Configuration for the game parameters

### Key Modules

- **framework**: Core framework components shared across games
- **base**: Legacy framework for backward compatibility
- **base_v2**: New version of the framework with enhanced features
- **multi_player**: Extensions for games with multiple players
- **single_player**: Simplified framework for single-player games

## Best Practices

### Game Development

1. **Extend Base Classes**: Always extend the framework's base classes rather than starting from scratch
2. **State Immutability**: Treat game states as immutable; create new states for changes
3. **Clear Validation**: Implement thorough move validation to prevent illegal moves
4. **Agent Interfaces**: Design clear, structured interfaces for agent decisions
5. **Progressive Disclosure**: Provide agents only with information they should have access to

### Agent Configuration

1. **Adjust Temperature**: Use lower temperatures (0.1-0.3) for logic/rule-based decisions
2. **Structured Output**: Use structured outputs for moves to ensure valid formatting
3. **Context Management**: Provide relevant game context without overwhelming the agent
4. **Few-Shot Examples**: Include examples of valid moves for better performance

## Advanced Usage

### Game Evaluation and Benchmarking

```python
from haive.games.benchmark import benchmark_agents
from haive.games.chess import ChessAgent, ChessConfig

# Configure different agent variants
configurations = [
    ChessConfig(name="Aggressive", strategy_bias="aggressive", temperature=0.7),
    ChessConfig(name="Defensive", strategy_bias="defensive", temperature=0.3),
    ChessConfig(name="Balanced", strategy_bias="balanced", temperature=0.5),
]

# Run a tournament with multiple games
results = benchmark_agents(
    agent_class=ChessAgent,
    configurations=configurations,
    num_games=50,
    parallel=True
)

# Analyze results
print(results.win_rates)
print(results.average_game_length)
print(results.strategy_analysis)
```

### Custom Visualization

```python
from haive.games.utils.visualization import GameVisualizer
from haive.games.chess import ChessState

class ChessVisualizer(GameVisualizer):
    def render_board(self, state: ChessState) -> str:
        # Create ASCII or Unicode representation of the chess board
        # ...
        return board_representation

    def render_history(self, states: list[ChessState]) -> str:
        # Generate a move-by-move replay
        # ...
        return history_representation

# Use the visualizer
visualizer = ChessVisualizer()
rendered_board = visualizer.render_board(current_state)
print(rendered_board)
```

### Adding Observer Agents

```python
from haive.games.poker import PokerAgent, PokerConfig
from haive.games.utils.observers import GameObserver

class PokerCommentator(GameObserver):
    def observe(self, state, previous_state=None):
        # Generate commentary on the current game state
        if previous_state and state.current_phase != previous_state.current_phase:
            print(f"Moving to {state.current_phase} phase!")

        if state.last_action:
            print(f"Player {state.last_action.player_id} {state.last_action.type} "
                  f"with {state.last_action.amount if hasattr(state.last_action, 'amount') else ''}")

# Add observer to game
config = PokerConfig(player_names=["Alice", "Bob", "Charlie", "Dave"])
game = PokerAgent(config)
game.add_observer(PokerCommentator())
result = game.run()
```

## Performance Considerations

### Agent Response Time

- **Temperature Settings**: Lower temperatures (0.1-0.3) speed up decision-making
- **Context Pruning**: Only include recent moves and relevant state
- **Structured Output**: Use JSON mode for faster, more reliable parsing
- **Parallel Processing**: Run multiple agent decisions concurrently when possible

### Memory Management

- **State History**: Limit stored history to prevent memory bloat
- **Move Validation**: Cache validation results for repeated checks
- **Board Representations**: Use efficient data structures (bitboards for chess)
- **Agent Pooling**: Reuse agent instances across games

## Testing Games

### Unit Testing Game Logic

```python
import pytest
from haive.games.chess import ChessStateManager, ChessState

class TestChessLogic:
    def test_valid_move_detection(self):
        manager = ChessStateManager()
        state = manager.initialize_state()

        # Test pawn move
        move = {"from": "e2", "to": "e4", "piece": "pawn"}
        assert manager.is_valid_move(state, move)

        # Test invalid move
        invalid_move = {"from": "e2", "to": "e5", "piece": "pawn"}
        assert not manager.is_valid_move(state, invalid_move)

    def test_checkmate_detection(self):
        manager = ChessStateManager()
        # Set up checkmate position
        state = ChessState(board=setup_checkmate_position())
        assert manager.is_checkmate(state)
```

### Integration Testing

```python
from haive.games.poker import PokerAgent
from haive.games.utils.test_helpers import create_test_config, MockEngine

async def test_full_poker_game():
    # Create test configuration with mock engines
    config = create_test_config(
        PokerConfig,
        player_engines=[
            MockEngine(decisions=["call", "raise:20", "fold"]),
            MockEngine(decisions=["raise:10", "call", "check"]),
        ]
    )

    agent = PokerAgent(config)
    result = await agent.arun()

    assert result.winner in ["Player1", "Player2"]
    assert len(result.hands_played) > 0
```

## Troubleshooting

### Common Issues

#### Agent Makes Invalid Moves

**Problem**: Agent repeatedly attempts invalid moves.

**Solutions**:

```python
# 1. Add move validation examples to prompt
config = ChessConfig(
    system_message="""You are playing chess.
    Valid moves are in format: {"from": "e2", "to": "e4"}
    Only move your own pieces (white/black)."""
)

# 2. Use structured output
config = ChessConfig(
    output_format="json",
    output_schema=ChessMoveSchema
)

# 3. Add retry logic
config = ChessConfig(
    max_invalid_moves=3,
    invalid_move_penalty=True
)
```

#### Game State Corruption

**Problem**: Game state becomes inconsistent.

**Solutions**:

```python
# 1. Enable state validation
config = GameConfig(
    validate_state_transitions=True,
    state_validation_level="strict"
)

# 2. Use immutable states
class MyGameState(GameState):
    class Config:
        frozen = True  # Make immutable

# 3. Add state recovery
manager = GameStateManager(
    enable_checkpoints=True,
    checkpoint_frequency=10
)
```

#### Performance Degradation

**Problem**: Games slow down over time.

**Solutions**:

```python
# 1. Limit context window
config = GameConfig(
    max_history_length=20,
    context_compression=True
)

# 2. Use caching
from functools import lru_cache

@lru_cache(maxsize=1000)
def evaluate_position(board_hash):
    # Expensive evaluation
    pass

# 3. Profile and optimize
import cProfile

with cProfile.Profile() as pr:
    game.run()
pr.print_stats(sort='cumulative')
```

## Examples

For comprehensive examples demonstrating various games and patterns, see the [example.py](example.py) file which includes:

- Quick game setup and execution
- Tournament organization
- Custom game creation
- Agent evaluation
- Visualization examples
- Advanced configuration patterns

## Contributing

### Adding a New Game

1. Create a new directory under `games/`
2. Implement required classes:
   - `{Game}State` - Game state model
   - `{Game}StateManager` - Game logic
   - `{Game}Config` - Configuration
   - `{Game}Agent` - Main agent class
3. Add tests under `tests/test_{game}/`
4. Create README.md with game rules and usage
5. Add example.py demonstrating gameplay

### Code Style

- Follow the project's coding standards
- Use type hints for all public APIs
- Include docstrings with examples
- Add unit tests for game logic
- Ensure moves are deterministic and reproducible

## API Reference

### Core Classes

| Class              | Description                    |
| ------------------ | ------------------------------ |
| `GameAgent`        | Base class for all game agents |
| `GameState`        | Base state model for games     |
| `GameStateManager` | Handles game logic and rules   |
| `GameConfig`       | Configuration for games        |
| `GameVisualizer`   | Base class for visualization   |
| `GameObserver`     | Interface for game observers   |

### Key Methods

| Method                      | Description          |
| --------------------------- | -------------------- |
| `agent.run()`               | Run a complete game  |
| `agent.arun()`              | Async version of run |
| `manager.is_game_over()`    | Check if game ended  |
| `manager.get_valid_moves()` | Get legal moves      |
| `manager.process_move()`    | Apply move to state  |
| `state.to_dict()`           | Serialize state      |

For detailed API documentation, see the [API Reference](../../../../docs/source/api/haive/games/index.rst).

## Related Modules

- [haive-core](../../../haive-core/README.md) - Core framework components
- [haive-agents](../../../haive-agents/README.md) - Agent implementations
- [haive-tools](../../../haive-tools/README.md) - Tools for gameplay
- [Game Framework](framework/README.md) - Framework documentation
- [Multi-Player Framework](multi_player/README.md) - Multi-player patterns
