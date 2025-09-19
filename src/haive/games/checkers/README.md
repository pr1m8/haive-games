# Checkers Game Module

A comprehensive implementation of the classic strategy game Checkers (also known as Draughts) with advanced AI analysis, strategic decision-making, and multi-level gameplay using the Haive framework.

## Table of Contents

1. [Overview](#overview)
2. [Game Rules and Mechanics](#game-rules-and-mechanics)
3. [Strategic Foundations](#strategic-foundations)
4. [Installation](#installation)
5. [Quick Start](#quick-start)
6. [API Reference](#api-reference)
7. [Strategic Analysis](#strategic-analysis)
8. [Examples](#examples)
9. [Performance Considerations](#performance-considerations)
10. [Testing](#testing)
11. [Advanced Usage](#advanced-usage)
12. [Contributing](#contributing)
13. [Version History](#version-history)

## Overview

Checkers (also known as Draughts) is a strategic board game for two players involving diagonal moves of uniform game pieces and mandatory captures by jumping over opponent pieces. The game demonstrates fundamental concepts of tactical planning, positional advantage, and endgame technique.

### Key Features

- **Complete Rule Implementation**: Standard 8x8 American Checkers with mandatory jumps and king promotion
- **Advanced AI Analysis**: LLM-powered strategic reasoning with position evaluation
- **Rich Terminal UI**: Beautiful visualization with colors, animations, and move highlighting
- **Strategic Decision Support**: Move analysis, position evaluation, and tactical suggestions
- **Performance Optimized**: Efficient game state management and move generation
- **Educational Tools**: Comprehensive explanations of strategy and tactics
- **Tournament Ready**: Full game state management and replay capabilities

### Strategic Significance

Checkers demonstrates key strategic concepts:

- **Tactical Combinations**: Multi-move sequences leading to material gain
- **Positional Play**: Control of key squares and piece development
- **Endgame Technique**: King vs. men advantages and opposition principles
- **Sacrifice Patterns**: Trading material for positional or tactical advantage

## Game Rules and Mechanics

### Standard American Checkers Rules

The implementation follows standard American Checkers rules on an 8x8 board:

#### Board Setup

- **Board Size**: 8x8 alternating dark and light squares
- **Piece Placement**: Each player starts with 12 pieces on dark squares
- **Initial Position**: Three rows of pieces on each side of the board

#### Basic Movement

- **Direction**: Pieces move diagonally forward only (until crowned)
- **Single Move**: One square diagonally to an adjacent empty square
- **Turn-Based**: Players alternate turns, with one player controlling dark pieces

#### Capturing Rules

- **Mandatory Jumps**: Players must capture if possible
- **Jump Mechanics**: Leap over opponent's piece to empty square behind it
- **Multiple Jumps**: Continue jumping if additional captures are available
- **Capture Priority**: Must take the jump that captures the most pieces

#### King Promotion

- **Promotion Condition**: Piece reaches the opposite end of the board
- **King Abilities**: Can move diagonally forward or backward
- **King Captures**: Can jump in any diagonal direction
- **Crown Symbol**: Visually distinguished from regular pieces

#### Win Conditions

- **No Pieces**: Opponent has no pieces remaining
- **No Moves**: Opponent cannot make any legal moves
- **Stalemate**: Game declared draw after extended play without progress

### Advanced Rules

#### Huffing Rule (Optional)

- **Failure to Jump**: If player fails to make mandatory jump
- **Penalty**: Opposing player may remove the piece that should have jumped
- **Implementation**: Configurable in game settings

#### Draw Conditions

- **Repetition**: Same position repeated three times
- **50-Move Rule**: 50 moves without capture or piece promotion
- **Insufficient Material**: Impossible to achieve checkmate

## Strategic Foundations

### Opening Principles

1. **Center Control**: Occupy central squares (d4, e4, d5, e5) early
2. **Piece Development**: Activate pieces toward the center
3. **Avoid Weaknesses**: Don't create isolated or backward pieces
4. **Maintain Formation**: Keep pieces supporting each other

### Middlegame Strategy

1. **Tactical Awareness**: Look for jumping opportunities
2. **Positional Play**: Control key squares and diagonals
3. **Piece Coordination**: Work pieces together for combinations
4. **King Creation**: Advance pieces toward promotion

### Endgame Technique

1. **King Activity**: Use king mobility advantage
2. **Opposition**: Control key squares to restrict opponent
3. **Zugzwang**: Force opponent into disadvantageous moves
4. **Tempo**: Use move timing to gain advantages

### Tactical Patterns

#### The Fork

- **Definition**: Attack two pieces simultaneously
- **Execution**: Position piece to threaten multiple targets
- **Counter**: Avoid placing pieces on same diagonal

#### The Pin

- **Definition**: Immobilize piece protecting another
- **Execution**: Attack through protected piece
- **Counter**: Remove defending piece safely

#### The Skewer

- **Definition**: Force valuable piece to move, exposing lesser piece
- **Execution**: Attack high-value piece in line with lower-value piece
- **Counter**: Block the attack or move both pieces

#### The Sacrifice

- **Definition**: Give up material for positional or tactical advantage
- **Execution**: Calculate compensation accurately
- **Counter**: Accept sacrifice only if beneficial

## Installation

This module is part of the `haive-games` package. Install it using:

```bash
pip install haive-games
```

### Requirements

- Python 3.8+
- haive-core package
- LangChain integration
- Rich library for terminal UI
- Pydantic for data validation

### Optional Dependencies

```bash
# For enhanced visualization
pip install rich

# For game analysis
pip install numpy

# For tournament play
pip install pandas
```

## Quick Start

### Basic Game Setup

```python
from haive.games.checkers import CheckersAgent, CheckersAgentConfig

# Create a basic checkers game
config = CheckersAgentConfig()
agent = CheckersAgent(config)

# Run the game with visualization
result = agent.run_game(visualize=True)
print(f"Winner: {result.get('winner')}")
```

### Custom Player Configuration

```python
from haive.core.engine.aug_llm import AugLLMConfig

# Configure with different LLM settings
config = CheckersAgentConfig(
    aug_llm_configs={
        "player1": AugLLMConfig(
            model="gpt-4",
            temperature=0.3,  # Conservative play
            system_message="You are a defensive checkers player"
        ),
        "player2": AugLLMConfig(
            model="gpt-4",
            temperature=0.9,  # Aggressive play
            system_message="You are an aggressive checkers player"
        )
    },
    max_turns=300,
    show_analysis=True
)

agent = CheckersAgent(config)
result = agent.run_game(visualize=True)
```

### Position Analysis

```python
from haive.games.checkers import CheckersStateManager

# Analyze a specific position
manager = CheckersStateManager()
state = manager.initialize_game()

# Make some moves
state = manager.make_move(state, "player1", "22-18")
state = manager.make_move(state, "player2", "9-14")

# Get position analysis
analysis = manager.analyze_position(state, "player1")
print(f"Material: {analysis.material_advantage}")
print(f"Position: {analysis.positional_evaluation}")
print(f"Best move: {analysis.best_move}")
```

## API Reference

### CheckersAgent

```python
class CheckersAgent(GameAgent[CheckersAgentConfig]):
    """Main checkers game agent with LLM-powered gameplay."""

    def run_game(self, visualize: bool = True) -> Dict[str, Any]:
        """Run a complete checkers game.

        Args:
            visualize: Whether to show game visualization

        Returns:
            Dict containing game results and statistics
        """

    def analyze_position(self, state: CheckersState, player: str) -> CheckersAnalysis:
        """Analyze a checkers position.

        Args:
            state: Current game state
            player: Player to analyze for

        Returns:
            Comprehensive position analysis
        """

    def make_move(self, state: CheckersState, player: str, move: str) -> CheckersState:
        """Make a move in the game.

        Args:
            state: Current game state
            player: Player making the move
            move: Move in algebraic notation

        Returns:
            Updated game state
        """

    def get_valid_moves(self, state: CheckersState, player: str) -> List[str]:
        """Get all valid moves for a player.

        Args:
            state: Current game state
            player: Player to get moves for

        Returns:
            List of valid moves in algebraic notation
        """

    def save_game(self, filename: str) -> None:
        """Save current game to file.

        Args:
            filename: File path to save game
        """

    def load_game(self, filename: str) -> None:
        """Load game from file.

        Args:
            filename: File path to load game from
        """
```

### CheckersStateManager

```python
class CheckersStateManager:
    """Manages checkers game state and rules."""

    def initialize_game(self) -> CheckersState:
        """Initialize a new game state.

        Returns:
            New game state with standard starting position
        """

    def get_valid_moves(self, state: CheckersState, player: str) -> List[str]:
        """Get all valid moves for a player.

        Args:
            state: Current game state
            player: Player to get moves for

        Returns:
            List of valid moves in algebraic notation
        """

    def make_move(self, state: CheckersState, player: str, move: str) -> CheckersState:
        """Make a move and return new state.

        Args:
            state: Current game state
            player: Player making the move
            move: Move in algebraic notation

        Returns:
            Updated game state
        """

    def is_game_over(self, state: CheckersState) -> bool:
        """Check if the game is over.

        Args:
            state: Current game state

        Returns:
            True if game is over, False otherwise
        """

    def get_winner(self, state: CheckersState) -> Optional[str]:
        """Determine the game winner.

        Args:
            state: Current game state

        Returns:
            Winner player name or None if game is ongoing
        """

    def analyze_position(self, state: CheckersState, player: str) -> CheckersAnalysis:
        """Analyze a position for strategic insights.

        Args:
            state: Current game state
            player: Player to analyze for

        Returns:
            Detailed position analysis
        """

    def validate_move(self, state: CheckersState, player: str, move: str) -> bool:
        """Validate if a move is legal.

        Args:
            state: Current game state
            player: Player making the move
            move: Move in algebraic notation

        Returns:
            True if move is valid, False otherwise
        """
```

### CheckersUI

```python
class CheckersUI:
    """Rich terminal interface for checkers."""

    def display_board(self, state: CheckersState) -> None:
        """Display the current board state.

        Args:
            state: Current game state to display
        """

    def display_move(self, move: CheckersMove, player: str) -> None:
        """Display a move with animation.

        Args:
            move: Move to display
            player: Player making the move
        """

    def display_analysis(self, analysis: CheckersAnalysis) -> None:
        """Display position analysis.

        Args:
            analysis: Analysis results to display
        """

    def display_game_result(self, result: Dict[str, Any]) -> None:
        """Display final game results.

        Args:
            result: Game result dictionary
        """

    def get_user_input(self, prompt: str) -> str:
        """Get input from user.

        Args:
            prompt: Prompt message to display

        Returns:
            User input string
        """
```

### Data Models

```python
class CheckersMove(BaseModel):
    """Represents a checkers move with validation."""
    from_position: str
    to_position: str
    player: str
    is_jump: bool = False
    captured_position: Optional[str] = None
    is_king_move: bool = False
    reasoning: Optional[str] = None

class CheckersAnalysis(BaseModel):
    """Comprehensive checkers position analysis."""
    material_advantage: str
    positional_evaluation: str
    best_move: str
    strategic_notes: str
    tactical_opportunities: List[str]
    threats: List[str]

class CheckersState(BaseModel):
    """Complete checkers game state."""
    board: List[List[str]]
    current_player: str
    move_history: List[CheckersMove]
    game_over: bool
    winner: Optional[str]
    kings: Dict[str, List[str]]
```

## Strategic Analysis

### Position Evaluation Framework

#### Material Evaluation

- **Piece Values**: Men = 1 point, Kings = 3 points
- **Material Balance**: Track piece count and type advantages
- **Exchange Evaluation**: Assess trade benefits

#### Positional Factors

- **Center Control**: Value of controlling central squares
- **Piece Activity**: Mobility and attacking potential
- **King Safety**: Protection of promoted pieces
- **Pawn Structure**: Formation and advancement patterns

#### Strategic Principles

1. **Opening Strategy**
   - Develop pieces toward center
   - Avoid early weaknesses
   - Maintain piece coordination

2. **Middlegame Tactics**
   - Look for tactical combinations
   - Control key squares and diagonals
   - Create threats and forcing moves

3. **Endgame Technique**
   - Activate kings effectively
   - Use opposition principles
   - Calculate winning sequences

### Advanced Tactical Patterns

#### Multi-Jump Combinations

- **Setup**: Create forcing sequences
- **Calculation**: Accurate move calculation
- **Execution**: Precise move timing

#### Positional Sacrifices

- **Material for Initiative**: Trade pieces for attack
- **Piece for Position**: Sacrifice for better placement
- **Time for Space**: Use tempo effectively

#### King Endgames

- **King vs. Men**: Winning techniques
- **King Opposition**: Control key squares
- **Breakthrough**: Create passed pieces

## Examples

### Example 1: Basic Game

```python
from haive.games.checkers import CheckersAgent, CheckersAgentConfig
from haive.core.engine.aug_llm import AugLLMConfig

# Create LLM configurations for players
llm_config = AugLLMConfig(
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

### Example 2: Advanced Configuration

```python
# Configure with different player personalities
config = CheckersAgentConfig(
    aug_llm_configs={
        "player1": AugLLMConfig(
            model="gpt-4",
            temperature=0.3,  # Conservative player
            system_message="You are a defensive checkers player who prioritizes piece safety."
        ),
        "player2": AugLLMConfig(
            model="gpt-4",
            temperature=0.9,  # Aggressive player
            system_message="You are an aggressive checkers player who seeks quick victories."
        ),
        "analyzer": AugLLMConfig(
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

### Example 3: Tournament Play

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

### Example 4: Custom Analysis

```python
from haive.games.checkers.state_manager import CheckersStateManager

# Analyze a specific position
state_manager = CheckersStateManager()
state = state_manager.initialize_game()

# Make some moves
state = state_manager.make_move(state, "player1", "22-18")
state = state_manager.make_move(state, "player2", "9-14")

# Analyze position
analysis = agent.analyze_position(state, "player1")
print(f"Position evaluation: {analysis.positional_evaluation}")
print(f"Best move: {analysis.best_move}")
print(f"Strategic notes: {analysis.strategic_notes}")
```

### Example 5: Educational Mode

```python
# Configure for educational analysis
config = CheckersAgentConfig(
    show_analysis=True,
    analysis_depth=3,
    educational_mode=True,
    move_timeout=60  # Allow time for analysis
)

agent = CheckersAgent(config)

# Run with detailed explanations
result = agent.run_game(visualize=True, explain_moves=True)
```

### Example 6: Performance Testing

```python
import time

# Test game performance
config = CheckersAgentConfig(
    show_analysis=False,
    ui_enabled=False,
    move_timeout=5  # Quick moves
)

start_time = time.time()
games_played = 0

for _ in range(100):
    agent = CheckersAgent(config)
    result = agent.run_game(visualize=False)
    games_played += 1

    if games_played % 10 == 0:
        elapsed = time.time() - start_time
        print(f"Played {games_played} games in {elapsed:.2f} seconds")

print(f"Average game time: {elapsed/games_played:.2f} seconds")
```

### Example 7: Move Validation

```python
from haive.games.checkers import CheckersStateManager

# Test move validation
manager = CheckersStateManager()
state = manager.initialize_game()

# Test various moves
test_moves = ["22-18", "9-14", "25-22", "invalid-move"]

for move in test_moves:
    is_valid = manager.validate_move(state, "player1", move)
    print(f"Move {move}: {'Valid' if is_valid else 'Invalid'}")
```

### Example 8: Game State Serialization

```python
import json
from haive.games.checkers import CheckersAgent, CheckersAgentConfig

# Create and play partial game
config = CheckersAgentConfig(max_turns=10)
agent = CheckersAgent(config)

# Play a few moves
for _ in range(5):
    state = agent.get_current_state()
    if not state.game_over:
        agent.make_next_move()

# Save game state
state_dict = agent.get_current_state().model_dump()
with open('checkers_game.json', 'w') as f:
    json.dump(state_dict, f, indent=2)

print("Game state saved to checkers_game.json")
```

## Performance Considerations

### Recommended Settings

```python
# For fast games
config = CheckersAgentConfig(
    max_turns=100,
    show_analysis=False,
    ui_enabled=False,
    move_timeout=10,
    analysis_depth=1
)

# For detailed analysis
config = CheckersAgentConfig(
    max_turns=300,
    show_analysis=True,
    analysis_depth=3,
    move_timeout=60,
    educational_mode=True
)

# For tournament play
config = CheckersAgentConfig(
    max_turns=150,
    show_analysis=False,
    ui_enabled=False,
    move_timeout=15,
    save_game_history=True
)
```

### Performance Metrics

- **Average Game Time**: 5-15 minutes depending on settings
- **Move Generation**: ~1-3 seconds per move
- **Analysis Time**: 2-10 seconds per position
- **Memory Usage**: ~5-20MB per game session

### Optimization Tips

1. **Reduce Analysis Depth**: Lower `analysis_depth` for faster play
2. **Disable UI**: Set `ui_enabled=False` for headless operation
3. **Shorter Timeouts**: Reduce `move_timeout` for quick games
4. **Batch Processing**: Run multiple games in sequence
5. **Caching**: Enable position caching for repeated analysis

### Memory Usage

- **State Size**: ~2KB per game state
- **Move History**: ~15KB for 200-turn game
- **Analysis Data**: ~8KB per position analysis
- **UI Components**: ~5KB for visualization
- **Total Session**: ~30KB per complete game

## Testing

Run the checkers tests:

```bash
# Run all checkers tests
poetry run pytest packages/haive-games/tests/test_checkers/ -v

# Test specific functionality
poetry run pytest packages/haive-games/tests/test_checkers/test_agent.py -v
poetry run pytest packages/haive-games/tests/test_checkers/test_state_manager.py -v
poetry run pytest packages/haive-games/tests/test_checkers/test_models.py -v

# Test with coverage
poetry run pytest packages/haive-games/tests/test_checkers/ --cov=haive.games.checkers

# Run integration tests
poetry run pytest packages/haive-games/tests/test_checkers/test_integration.py -v
```

### Test Categories

- **Unit Tests**: Individual component testing
- **Integration Tests**: Full game workflow testing
- **Performance Tests**: Speed and memory usage testing
- **Rule Tests**: Game rule validation testing
- **UI Tests**: Visualization and interaction testing

### Test Coverage

- **Agent Tests**: Game flow and decision-making
- **State Manager Tests**: Rule enforcement and validation
- **Model Tests**: Data structure validation
- **UI Tests**: Display and interaction components
- **Performance Tests**: Speed and efficiency metrics

## Advanced Usage

### Custom Move Validation

```python
from haive.games.checkers.state_manager import CheckersStateManager

class CustomStateManager(CheckersStateManager):
    def validate_move(self, state, player, move):
        # Add custom validation logic
        base_valid = super().validate_move(state, player, move)
        if not base_valid:
            return False

        # Add custom rules
        return self.custom_rule_check(state, player, move)

    def custom_rule_check(self, state, player, move):
        # Implement custom rules
        return True
```

### Game State Persistence

```python
import json

# Save game state
state_dict = state.model_dump()
with open('game_state.json', 'w') as f:
    json.dump(state_dict, f)

# Load game state
with open('game_state.json', 'r') as f:
    state_dict = json.load(f)
state = CheckersState.model_validate(state_dict)
```

### Custom AI Strategies

```python
# Implement custom strategy engine
class CustomStrategy:
    def __init__(self, style="aggressive"):
        self.style = style

    def evaluate_position(self, state, player):
        # Custom position evaluation
        return self.calculate_advantage(state, player)

    def suggest_move(self, state, player, valid_moves):
        # Custom move selection
        return self.select_best_move(state, player, valid_moves)
```

## Configuration Options

### CheckersAgentConfig

```python
class CheckersAgentConfig:
    aug_llm_configs: Dict[str, AugLLMConfig]  # Player and analyzer engines
    max_turns: int = 200                      # Maximum game turns
    show_analysis: bool = True                # Display position analysis
    analysis_depth: int = 2                   # Analysis depth levels
    ui_enabled: bool = True                   # Enable rich UI
    move_timeout: int = 30                    # Seconds per move
    retry_attempts: int = 3                   # Invalid move retries
    log_level: str = "INFO"                   # Logging verbosity
    educational_mode: bool = False            # Enable educational explanations
    save_game_history: bool = True            # Save game for replay
    enable_hints: bool = False                # Show move hints
    difficulty_level: str = "normal"          # AI difficulty setting
```

### Engine Configurations

- **player1/player2**: Main game engines for move generation
- **analyzer**: Position analysis and evaluation engine
- **validator**: Move validation and rule checking (optional)
- **hint_engine**: Move suggestion system (optional)

### Difficulty Levels

- **beginner**: Lower temperature, basic analysis
- **normal**: Balanced play with moderate analysis
- **advanced**: Higher analysis depth, strategic play
- **expert**: Maximum analysis depth, complex strategies

## Troubleshooting

### Common Issues

1. **Invalid Move Errors**

   ```python
   # Enable move validation debugging
   config.log_level = "DEBUG"
   config.retry_attempts = 5
   ```

2. **Game Timeout**

   ```python
   # Increase move timeout
   config.move_timeout = 60
   config.max_turns = 300
   ```

3. **UI Display Issues**

   ```python
   # Disable rich UI if needed
   config.ui_enabled = False
   ```

4. **Memory Issues**

   ```python
   # Optimize memory usage
   config.save_game_history = False
   config.analysis_depth = 1
   ```

5. **Performance Issues**
   ```python
   # Speed up gameplay
   config.show_analysis = False
   config.move_timeout = 10
   ```

### Performance Tuning

- Reduce `analysis_depth` for faster moves
- Disable `show_analysis` for speed
- Use lower `temperature` for more consistent play
- Set `max_turns` to prevent infinite games
- Enable `ui_enabled=False` for headless operation
- Adjust `move_timeout` based on hardware capabilities

### Debug Mode

```python
# Enable comprehensive debugging
config = CheckersAgentConfig(
    log_level="DEBUG",
    show_analysis=True,
    ui_enabled=True,
    move_timeout=120,
    retry_attempts=5
)
```

## Contributing

Contributions to the Checkers module are welcome! Please follow these guidelines:

### Development Setup

```bash
# Clone the repository
git clone https://github.com/pr1m8/haive
cd haive

# Install dependencies
poetry install

# Run tests
poetry run pytest packages/haive-games/tests/test_checkers/ -v
```

### Code Style

- Follow PEP 8 guidelines
- Use type hints for all functions
- Add comprehensive docstrings
- Include unit tests for new features
- Follow existing patterns and conventions

### Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Implement changes with tests
4. Update documentation
5. Submit pull request with clear description

## Version History

### v2.0.0 (Current)

- Enhanced AI analysis with strategic reasoning
- Improved UI with rich terminal visualization
- Added educational mode and move explanations
- Performance optimizations and memory management
- Comprehensive test coverage

### v1.5.0

- Added tournament play capabilities
- Improved move validation and error handling
- Enhanced position analysis
- Better configuration options

### v1.0.0

- Initial release with basic checkers gameplay
- LLM-powered players
- Standard rule implementation
- Basic UI visualization

## License

This module is part of the Haive framework and is licensed under the same terms as the parent project.

## See Also

- [Chess](../chess/): Advanced chess implementation with similar architecture
- [Tic-Tac-Toe](../tic_tac_toe/): Simpler game for understanding basics
- [Nim](../nim/): Mathematical game with optimal strategy
- [Connect4](../connect4/): Strategic connection game
- [Base Framework](../base/): Core game framework components
- [Game Theory Documentation](../../../docs/game_theory.md): Strategic concepts
- [LLM Configuration Guide](../../../docs/llm_configuration.md): Engine setup
