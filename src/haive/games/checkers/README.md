# Checkers

Comprehensive checkers game implementation with LLM-powered AI players and rich visualization.

## Overview

The Checkers module provides a complete implementation of the classic checkers (draughts) game with advanced AI capabilities. Built on the Haive framework, it features LLM-powered players that use strategic reasoning, position analysis, and sophisticated move generation.

**Key Features:**

- **Complete Checkers Rules**: Standard 8x8 board with mandatory jumps and king promotion
- **AI-Powered Players**: LLM-based agents with strategic thinking and position analysis
- **Rich Visualization**: Beautiful terminal UI with colors, animations, and game state display
- **Move Validation**: Comprehensive rule enforcement with error handling
- **Game Analysis**: Position evaluation and strategic move suggestions
- **Configurable Settings**: Customizable game parameters and player configurations

**Game Rules Implemented:**

- Standard checkers movement (diagonal only)
- Mandatory jump captures
- Multiple jump sequences
- King promotion at board edges
- Win conditions (no pieces or no valid moves)
- Draw detection for prolonged games

## Architecture

The checkers implementation follows Haive's agent-based architecture:

```
CheckersAgent
├── Configuration (CheckersAgentConfig)
├── State Management (CheckersStateManager)
├── UI Visualization (CheckersUI)
├── LLM Engines (player1, player2, analyzer)
└── Game Flow (LangGraph workflow)
```

### Core Components

- **CheckersAgent**: Main game controller using LangGraph workflow
- **CheckersState**: Game state representation with board and player data
- **CheckersStateManager**: Game logic, rule enforcement, and move validation
- **CheckersUI**: Rich terminal interface with board visualization
- **CheckersMove**: Structured move representation with validation
- **CheckersAnalysis**: Position evaluation and strategic analysis

## Installation

This module is part of the `haive-games` package. Install it using:

```bash
pip install haive-games
```

## Usage Examples

### Basic Game

```python
from haive.games.checkers import CheckersAgent, CheckersAgentConfig
from haive.core.models.llm.configs import LLMConfig

# Create LLM configurations for players
llm_config = LLMConfig(
    model="gpt-4",
    temperature=0.7,
    max_tokens=1000
)

# Configure checkers agent
config = CheckersAgentConfig(
    aug_llm_configs={
        "player1": llm_config,
        "player2": llm_config,
        "analyzer": llm_config
    },
    max_turns=200,
    show_analysis=True
)

# Create and run game
agent = CheckersAgent(config)
result = agent.run_game(visualize=True)

print(f"Game winner: {result.get('winner')}")
print(f"Total turns: {result.get('turn_count')}")
```

### Advanced Configuration

```python
# Configure with different player personalities
config = CheckersAgentConfig(
    aug_llm_configs={
        "player1": LLMConfig(
            model="gpt-4",
            temperature=0.3,  # Conservative player
            system_prompt="You are a defensive checkers player who prioritizes piece safety."
        ),
        "player2": LLMConfig(
            model="gpt-4",
            temperature=0.9,  # Aggressive player
            system_prompt="You are an aggressive checkers player who seeks quick victories."
        ),
        "analyzer": LLMConfig(
            model="gpt-4",
            temperature=0.1   # Analytical
        )
    },
    max_turns=300,
    show_analysis=True,
    analysis_depth=3
)

agent = CheckersAgent(config)
result = agent.run_game(visualize=True)
```

### Tournament Play

```python
# Run multiple games for tournament
wins = {"player1": 0, "player2": 0, "draws": 0}

for game_num in range(10):
    print(f"\nGame {game_num + 1}/10")
    agent = CheckersAgent(config)
    result = agent.run_game(visualize=False)

    winner = result.get('winner')
    if winner:
        wins[winner] += 1
    else:
        wins["draws"] += 1

    print(f"Winner: {winner or 'Draw'}")

print(f"\nTournament Results:")
print(f"Player 1: {wins['player1']} wins")
print(f"Player 2: {wins['player2']} wins")
print(f"Draws: {wins['draws']}")
```

### Custom Analysis

```python
from haive.games.checkers.state_manager import CheckersStateManager

# Analyze a specific position
state_manager = CheckersStateManager()
state = state_manager.initialize()

# Make some moves
state = state_manager.make_move(state, "player1", "5-4")
state = state_manager.make_move(state, "player2", "12-11")

# Analyze position
analysis = agent.analyze_position(state, "player1")
print(f"Position evaluation: {analysis.evaluation}")
print(f"Best move: {analysis.best_move}")
print(f"Strategic notes: {analysis.notes}")
```

## Game Strategy

### Basic Principles

1. **Center Control**: Occupy central squares for maximum mobility
2. **Piece Safety**: Avoid leaving pieces vulnerable to capture
3. **Tempo**: Force opponent moves while maintaining initiative
4. **King Creation**: Promote pieces to kings for enhanced mobility
5. **Endgame Technique**: Use king advantages effectively

### Advanced Tactics

- **Forced Moves**: Use mandatory jumps to control opponent options
- **Piece Sacrifice**: Trade pieces advantageously for position
- **King vs. Men**: Leverage king mobility in endgames
- **Opposition**: Control key squares to limit opponent movement

## Configuration Options

### CheckersAgentConfig

```python
class CheckersAgentConfig:
    aug_llm_configs: Dict[str, LLMConfig]  # Player and analyzer engines
    max_turns: int = 200                   # Maximum game turns
    show_analysis: bool = True             # Display position analysis
    analysis_depth: int = 2                # Analysis depth levels
    ui_enabled: bool = True                # Enable rich UI
    move_timeout: int = 30                 # Seconds per move
    retry_attempts: int = 3                # Invalid move retries
    log_level: str = "INFO"                # Logging verbosity
```

### Engine Configurations

- **player1/player2**: Main game engines for move generation
- **analyzer**: Position analysis and evaluation engine
- **validator**: Move validation and rule checking (optional)

## API Reference

### CheckersAgent

```python
class CheckersAgent(GameAgent[CheckersAgentConfig]):
    """Main checkers game agent."""

    def run_game(self, visualize: bool = True) -> Dict[str, Any]:
        """Run a complete checkers game."""

    def analyze_position(self, state: CheckersState, player: str) -> CheckersAnalysis:
        """Analyze a checkers position."""

    def make_move(self, state: CheckersState, player: str, move: str) -> CheckersState:
        """Make a move in the game."""
```

### CheckersStateManager

```python
class CheckersStateManager:
    """Manages checkers game state and rules."""

    def initialize(self) -> CheckersState:
        """Initialize a new game state."""

    def get_valid_moves(self, state: CheckersState, player: str) -> List[str]:
        """Get all valid moves for a player."""

    def is_game_over(self, state: CheckersState) -> bool:
        """Check if the game is over."""

    def get_winner(self, state: CheckersState) -> Optional[str]:
        """Determine the game winner."""
```

### CheckersUI

```python
class CheckersUI:
    """Rich terminal interface for checkers."""

    def display_board(self, state: CheckersState) -> None:
        """Display the current board state."""

    def display_move(self, move: CheckersMove, player: str) -> None:
        """Display a move with animation."""

    def display_analysis(self, analysis: CheckersAnalysis) -> None:
        """Display position analysis."""
```

## Performance & Optimization

### Recommended Settings

```python
# For fast games
config = CheckersAgentConfig(
    max_turns=100,
    show_analysis=False,
    ui_enabled=False,
    move_timeout=10
)

# For detailed analysis
config = CheckersAgentConfig(
    max_turns=300,
    show_analysis=True,
    analysis_depth=3,
    move_timeout=60
)
```

### Memory Usage

- **State Size**: ~1KB per game state
- **Move History**: ~10KB for 200-turn game
- **Analysis Data**: ~5KB per position analysis

## Testing

Run the checkers tests:

```bash
# Run all checkers tests
poetry run pytest packages/haive-games/tests/test_checkers/ -v

# Test specific functionality
poetry run pytest packages/haive-games/tests/test_checkers/test_agent.py -v
```

## Troubleshooting

### Common Issues

1. **Invalid Move Errors**

   ```python
   # Enable move validation debugging
   config.log_level = "DEBUG"
   ```

2. **Game Timeout**

   ```python
   # Increase move timeout
   config.move_timeout = 60
   ```

3. **UI Display Issues**
   ```python
   # Disable rich UI if needed
   config.ui_enabled = False
   ```

### Performance Tuning

- Reduce `analysis_depth` for faster moves
- Disable `show_analysis` for speed
- Use lower `temperature` for more consistent play
- Set `max_turns` to prevent infinite games

## See Also

- [Chess](../chess/): Advanced chess implementation with similar architecture
- [Tic-Tac-Toe](../tic_tac_toe/): Simpler game for understanding basics
- [Base Framework](../base/): Core game framework components
- [Game Theory Documentation](../../../docs/game_theory.md): Strategic concepts
- [LLM Configuration Guide](../../../docs/llm_configuration.md): Engine setup
