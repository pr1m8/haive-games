# Connect4 Game Module

**A comprehensive, strategic Connect4 implementation with AI analysis, beautiful UI, and advanced game theory algorithms.**

The Connect4 module provides a sophisticated implementation of the classic Connect4 game within the Haive framework, featuring LLM-based strategic reasoning, comprehensive position analysis, and an interactive Rich-based terminal UI. This module demonstrates advanced game AI capabilities with vertical drop mechanics, pattern recognition, and deep strategic planning.

## 🎯 Features

### Core Game Engine

- **Complete Connect4 Rules**: Full 7x6 grid implementation with gravity-based piece drops
- **Strategic AI Analysis**: Deep position evaluation including threat detection and pattern recognition
- **LLM-Based Decision Making**: Advanced reasoning using language models for strategic play
- **Advanced Algorithms**: Position evaluation, center control analysis, and winning pattern detection
- **Rich Terminal UI**: Beautiful, animated interface with real-time game state display and drop animations

### Advanced Analysis

- **Winning Move Detection**: Immediate four-in-a-row opportunity identification
- **Blocking Move Analysis**: Critical defensive move computation for all directions
- **Threat Assessment**: Multi-directional threat detection (horizontal, vertical, diagonal)
- **Center Control Evaluation**: Strategic importance of center column positioning
- **Pattern Recognition**: Complex winning pattern analysis and formation detection

### Developer Features

- **Type-Safe Models**: Comprehensive Pydantic data structures with validation
- **Async Support**: Full asynchronous operation for scalability
- **Configuration System**: Flexible game setup and AI personality adjustment
- **Comprehensive Testing**: Unit tests for all game mechanics and edge cases
- **Documentation**: Detailed API documentation with strategic insights

## 🚀 Quick Start

### Basic Game

```python
from haive.games.connect4 import Connect4Agent, Connect4AgentConfig

# Create and run a simple game
config = Connect4AgentConfig(enable_analysis=True)
agent = Connect4Agent(config)
final_state = agent.run_game()
print(f"Game result: {final_state.get('game_status', 'unknown')}")
```

### Rich UI Game

```python
from haive.games.connect4 import Connect4Agent, Connect4AgentConfig, Connect4UI
from haive.games.connect4.state_manager import Connect4StateManager

# Create enhanced configuration
config = Connect4AgentConfig(
    name="ai_showcase",
    enable_analysis=True,
    max_moves=42,
    should_visualize_graph=True
)

# Initialize agent and UI
agent = Connect4Agent(config)
ui = Connect4UI()

# Initialize game state and run
state = Connect4StateManager.initialize()
ui.display_state(state)

# Run game with beautiful interface
for step in agent.app.stream(state.model_dump(), debug=False, stream_mode="values"):
    ui.display_state(step)
    if step.get("game_status") != "ongoing":
        ui.show_game_over(step.get("winner"))
        break
```

## 🏗️ Architecture

### Component Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Connect4 Module                         │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │
│  │   Models    │  │    Agent    │  │   Config    │       │
│  │             │  │             │  │             │       │
│  │ Connect4-   │  │ Connect4-   │  │ Connect4-   │       │
│  │ Move        │  │ Agent       │  │ AgentConfig │       │
│  │             │  │             │  │             │       │
│  │ Connect4-   │  │ Strategic   │  │ Engine      │       │
│  │ Analysis    │  │ Reasoning   │  │ Selection   │       │
│  └─────────────┘  └─────────────┘  └─────────────┘       │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │
│  │    State    │  │   Engine    │  │     UI      │       │
│  │             │  │             │  │             │       │
│  │ Connect4-   │  │ Move        │  │ Rich        │       │
│  │ State       │  │ Generation  │  │ Terminal    │       │
│  │             │  │             │  │ Interface   │       │
│  │ State       │  │ Position    │  │             │       │
│  │ Manager     │  │ Analysis    │  │ Animated    │       │
│  └─────────────┘  └─────────────┘  └─────────────┘       │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **Game Initialization**: Configuration → Agent → State Manager
2. **Move Generation**: Current State → Analysis Engine → Strategic Move
3. **Move Validation**: Proposed Move → State Manager → Gravity & Collision Check
4. **State Update**: Valid Move → State Manager → New State with Piece Drop
5. **UI Display**: Game State → Rich UI → Terminal Visualization with Animation

## 📊 Game Rules & Mechanics

### Basic Rules

Connect4 is played on a 7×6 grid with these fundamental rules:

1. **Players**: Two players alternate turns (Red and Yellow)
2. **First Move**: Red traditionally plays first
3. **Drop Mechanism**: Pieces fall to the lowest available position in chosen column
4. **Objective**: Get four pieces in a row (horizontal, vertical, or diagonal)
5. **Win Conditions**: Complete any line of four pieces
6. **Draw Condition**: Board fills (42 pieces) without any player achieving four in a row

### Grid Layout

```
Column:  0   1   2   3   4   5   6
Row 0:   ·   ·   ·   ·   ·   ·   ·
Row 1:   ·   ·   ·   ·   ·   ·   ·
Row 2:   ·   ·   ·   ·   ·   ·   ·
Row 3:   ·   ·   ·   ·   ·   ·   ·
Row 4:   ·   ·   ·   ·   ·   ·   ·
Row 5:   ·   ·   ·   ·   ·   ·   ·
```

### Strategic Positions

- **Center Columns (3)**: Highest strategic value - maximum connectivity
- **Inner Columns (2,4)**: High value - good connectivity options
- **Outer Columns (1,5)**: Medium value - moderate connectivity
- **Edge Columns (0,6)**: Lower value - limited connectivity

### Win Conditions

The game checks for wins in 4 directions:

- **Horizontal**: 4 consecutive pieces in same row
- **Vertical**: 4 consecutive pieces in same column
- **Diagonal (/)**: 4 consecutive pieces in ascending diagonal
- **Diagonal (\)**: 4 consecutive pieces in descending diagonal

## 🎮 Configuration Options

### Basic Configuration

```python
from haive.games.connect4 import Connect4AgentConfig

config = Connect4AgentConfig(
    name="custom_game",           # Game identifier
    enable_analysis=True,         # Enable strategic analysis
    max_moves=42,                # Maximum moves (full board)
    should_visualize_graph=True,  # Show workflow visualization
)
```

### Advanced Configuration

```python
# Tournament-style configuration
config = Connect4AgentConfig(
    name="tournament_game",
    enable_analysis=True,
    max_moves=42,
    should_visualize_graph=False,  # Disable for performance
)

# Quick game configuration
config = Connect4AgentConfig(
    name="quick_game",
    enable_analysis=False,  # Faster gameplay
    max_moves=20,          # Shorter game
    should_visualize_graph=False,
)
```

## 🎨 UI Features

### Rich Terminal Interface

The Connect4UI class provides comprehensive visualization:

```python
from haive.games.connect4 import Connect4UI
from haive.games.connect4.state_manager import Connect4StateManager

ui = Connect4UI()
state = Connect4StateManager.initialize()

# Display game state
ui.display_state(state)

# Show AI thinking
ui.show_thinking("red")

# Display move with animation
from haive.games.connect4.models import Connect4Move
move = Connect4Move(column=3, explanation="Control center")
ui.show_move(move, "red")

# Show game over screen
ui.show_game_over("red")
```

### UI Customization

```python
# Custom color schemes
ui = Connect4UI()
ui.colors["red"]["piece"] = "bright_red"
ui.colors["yellow"]["piece"] = "bright_yellow"
ui.colors["board"] = "blue"
ui.colors["highlight"] = "green"
```

## 🧠 Strategic Analysis

### Position Analysis

The module provides comprehensive position analysis:

```python
from haive.games.connect4.models import Connect4Analysis

# Example analysis structure
analysis = Connect4Analysis(
    position_score=0.5,           # Overall position evaluation (-1.0 to 1.0)
    center_control=7,             # Center column control rating (0-10)
    threats={
        "winning_moves": [3, 4],  # Columns with immediate wins
        "blocking_moves": [2, 5]  # Columns requiring defensive play
    },
    suggested_columns=[3, 2, 4], # Recommended move order
    winning_chances=65            # Estimated win probability (0-100)
)
```

### Threat Detection

The AI analyzes multiple threat types:

1. **Immediate Threats**: Four-in-a-row completions
2. **Blocking Threats**: Opponent's winning opportunities
3. **Setup Threats**: Moves that create multiple threat vectors
4. **Trap Threats**: Forcing sequences that guarantee wins

### Strategic Principles

- **Center Control**: Prioritize center columns for maximum flexibility
- **Vertical Stacking**: Build vertical threats while maintaining horizontal options
- **Diagonal Awareness**: Monitor diagonal patterns early in the game
- **Trap Creation**: Set up situations where opponent must choose between two threats

## 📈 Performance Considerations

### Computational Complexity

- **Move Generation**: O(7) - Check each column for validity
- **Win Detection**: O(1) - Check 4 directions from last move
- **Position Evaluation**: O(42) - Evaluate all board positions
- **Threat Analysis**: O(42 × 4) - Check all positions in 4 directions

### Memory Usage

- **Game State**: ~2KB per state (7×6 grid + metadata)
- **Move History**: ~50 bytes per move
- **Analysis Data**: ~500 bytes per analysis

### Optimization Tips

```python
# For production use, disable expensive features
config = Connect4AgentConfig(
    enable_analysis=False,  # Disable for faster gameplay
    should_visualize_graph=False,  # Reduce memory usage
    max_moves=42  # Set appropriate limits
)

# Use batch processing for multiple games
async def run_multiple_games(num_games: int):
    results = []
    for i in range(num_games):
        agent = Connect4Agent(config)
        result = await agent.arun_game()
        results.append(result)
    return results
```

## 🔧 Advanced Usage

### Custom Move Validation

```python
from haive.games.connect4.state_manager import Connect4StateManager
from haive.games.connect4.models import Connect4Move

# Custom move validation
def validate_strategic_move(state: Connect4State, move: Connect4Move) -> bool:
    """Validate move with custom strategic rules."""
    # Check if move is legal
    if not Connect4StateManager.is_valid_move(state, move):
        return False

    # Custom rule: avoid edge columns early game
    if len(state.move_history) < 4 and move.column in [0, 6]:
        return False

    return True
```

### Position Evaluation

```python
def evaluate_position(state: Connect4State, player: str) -> float:
    """Evaluate position strength for given player."""
    score = 0.0

    # Center control bonus
    center_pieces = sum(1 for row in state.board
                       if row[3] == player)
    score += center_pieces * 0.3

    # Threat detection
    threats = detect_threats(state, player)
    score += len(threats) * 0.2

    # Connectivity analysis
    connections = analyze_connections(state, player)
    score += connections * 0.1

    return score
```

### Batch Game Analysis

```python
async def analyze_strategies(num_games: int = 100):
    """Analyze different strategies across multiple games."""
    strategies = ['center_first', 'edge_first', 'random']
    results = {}

    for strategy in strategies:
        config = Connect4AgentConfig(name=f"strategy_{strategy}")
        wins = 0

        for _ in range(num_games):
            agent = Connect4Agent(config)
            result = await agent.arun_game()
            if result.get('winner') == 'red':
                wins += 1

        results[strategy] = wins / num_games

    return results
```

## 🎯 Game Theory Insights

### Perfect Play Analysis

Connect4 is a solved game with perfect information:

1. **First Player Advantage**: Red (first player) has a theoretical win with perfect play
2. **Critical Columns**: Center columns (3,4) are most important for control
3. **Trap Patterns**: Certain patterns force wins regardless of opponent response
4. **Defensive Priority**: Blocking opponent threats takes precedence over creating own

### Strategic Depth

- **Opening Theory**: Center control is crucial in first 6 moves
- **Mid-game Tactics**: Focus on creating multiple threats simultaneously
- **End-game Technique**: Force opponent into zugzwang (must make bad move)

### Common Patterns

```python
# Classic trap pattern
trap_sequence = [
    Connect4Move(column=3, explanation="Control center"),
    Connect4Move(column=2, explanation="Create diagonal threat"),
    Connect4Move(column=4, explanation="Mirror diagonal"),
    Connect4Move(column=1, explanation="Force trap completion")
]
```

## 🧪 Testing & Validation

### Unit Tests

```python
import pytest
from haive.games.connect4 import Connect4State, Connect4Move
from haive.games.connect4.state_manager import Connect4StateManager

def test_valid_move():
    """Test valid move application."""
    state = Connect4StateManager.initialize()
    move = Connect4Move(column=3)
    new_state = Connect4StateManager.apply_move(state, move)
    assert new_state.board[5][3] == "red"

def test_column_full():
    """Test column full detection."""
    state = Connect4StateManager.initialize()
    # Fill column 0
    for _ in range(6):
        move = Connect4Move(column=0)
        state = Connect4StateManager.apply_move(state, move)

    # Next move should be invalid
    assert not Connect4StateManager.is_valid_move(state, Connect4Move(column=0))

def test_win_detection():
    """Test win condition detection."""
    state = Connect4StateManager.initialize()

    # Create horizontal win
    for col in range(4):
        move = Connect4Move(column=col)
        state = Connect4StateManager.apply_move(state, move)
        if col < 3:  # Alternate players
            state.turn = "yellow"
            dummy_move = Connect4Move(column=6)
            state = Connect4StateManager.apply_move(state, dummy_move)
            state.turn = "red"

    assert state.game_status == "red_win"
```

### Integration Tests

```python
def test_full_game_flow():
    """Test complete game from start to finish."""
    agent = Connect4Agent(Connect4AgentConfig(enable_analysis=True))
    final_state = agent.run_game()

    # Verify game completed
    assert final_state.get("game_status") in ["red_win", "yellow_win", "draw"]

    # Verify move history
    moves = final_state.get("move_history", [])
    assert len(moves) >= 7  # Minimum moves for a win
    assert all(0 <= move.column <= 6 for move in moves)
```

## 📚 API Reference

### Core Classes

#### Connect4Agent

```python
class Connect4Agent:
    """Main Connect4 game agent with LLM integration."""

    def __init__(self, config: Connect4AgentConfig):
        """Initialize agent with configuration."""

    def run_game(self) -> dict:
        """Run complete game and return final state."""

    async def arun_game(self) -> dict:
        """Async version of run_game."""
```

#### Connect4State

```python
class Connect4State:
    """Complete game state representation."""

    board: List[List[str | None]]  # 6x7 grid
    turn: Literal["red", "yellow"]  # Current player
    game_status: Literal["ongoing", "red_win", "yellow_win", "draw"]
    move_history: List[Connect4Move]
    winner: Optional[str]

    @property
    def board_string(self) -> str:
        """Get formatted board representation."""

    def is_column_full(self, column: int) -> bool:
        """Check if column is full."""

    def get_next_row(self, column: int) -> int:
        """Get next available row in column."""
```

#### Connect4Move

```python
class Connect4Move:
    """Represents a Connect4 move with validation."""

    column: int  # Column number (0-6)
    explanation: Optional[str]  # Move reasoning

    def __str__(self) -> str:
        """Human-readable move description."""
```

#### Connect4Analysis

```python
class Connect4Analysis:
    """Strategic position analysis."""

    position_score: float  # -1.0 to 1.0
    center_control: int  # 0-10 rating
    threats: Dict[str, List[int]]  # Threat detection
    suggested_columns: List[int]  # Move recommendations
    winning_chances: int  # 0-100 percentage
```

### Utility Functions

#### Connect4StateManager

```python
class Connect4StateManager:
    """Manages game state transitions."""

    @staticmethod
    def initialize() -> Connect4State:
        """Create initial game state."""

    @staticmethod
    def apply_move(state: Connect4State, move: Connect4Move) -> Connect4State:
        """Apply move to state."""

    @staticmethod
    def is_valid_move(state: Connect4State, move: Connect4Move) -> bool:
        """Check if move is valid."""

    @staticmethod
    def check_win(state: Connect4State) -> bool:
        """Check for win condition."""
```

### Configuration

#### Connect4AgentConfig

```python
class Connect4AgentConfig:
    """Configuration for Connect4 agent."""

    name: str = "connect4_agent"
    enable_analysis: bool = True
    max_moves: int = 42
    should_visualize_graph: bool = False
```

## 🔍 Debugging & Troubleshooting

### Common Issues

#### Move Validation Errors

```python
# Issue: Invalid column number
move = Connect4Move(column=7)  # Invalid: columns are 0-6
# Solution: Validate column range
if 0 <= column <= 6:
    move = Connect4Move(column=column)
```

#### Column Full Errors

```python
# Issue: Attempting to play in full column
# Solution: Check column availability
if not state.is_column_full(column):
    move = Connect4Move(column=column)
```

#### Performance Issues

```python
# Issue: Slow analysis
# Solution: Disable analysis for faster gameplay
config = Connect4AgentConfig(enable_analysis=False)
```

### Debug Mode

```python
# Enable detailed logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Run with debug output
agent = Connect4Agent(config)
final_state = agent.run_game()  # Will show detailed logs
```

## 📊 Statistics & Analytics

### Game Statistics

```python
def calculate_game_stats(final_state: dict) -> dict:
    """Calculate comprehensive game statistics."""
    moves = final_state.get("move_history", [])

    stats = {
        "total_moves": len(moves),
        "game_duration": len(moves),  # In turns
        "winner": final_state.get("winner"),
        "final_status": final_state.get("game_status"),
        "column_usage": {i: 0 for i in range(7)},
        "center_control": 0,
        "edge_plays": 0
    }

    # Analyze move patterns
    for move in moves:
        stats["column_usage"][move.column] += 1
        if move.column == 3:  # Center column
            stats["center_control"] += 1
        elif move.column in [0, 6]:  # Edge columns
            stats["edge_plays"] += 1

    return stats
```

### Performance Metrics

```python
def benchmark_performance(num_games: int = 10):
    """Benchmark game performance."""
    import time

    start_time = time.time()
    results = []

    for i in range(num_games):
        agent = Connect4Agent(Connect4AgentConfig(enable_analysis=False))
        game_start = time.time()
        result = agent.run_game()
        game_time = time.time() - game_start

        results.append({
            "game_id": i,
            "duration": game_time,
            "moves": len(result.get("move_history", [])),
            "winner": result.get("winner")
        })

    total_time = time.time() - start_time
    avg_game_time = total_time / num_games

    return {
        "total_time": total_time,
        "avg_game_time": avg_game_time,
        "games_per_second": num_games / total_time,
        "results": results
    }
```

## 🚀 Future Enhancements

### Planned Features

1. **Multi-level AI**: Different difficulty levels with varying analysis depth
2. **Tournament Mode**: Automated tournament with bracket management
3. **Position Database**: Opening book and endgame tablebase
4. **Machine Learning**: Neural network position evaluation
5. **Multiplayer Support**: Network play capabilities

### Extension Points

```python
# Custom evaluation function
def custom_position_evaluator(state: Connect4State) -> float:
    """Custom position evaluation algorithm."""
    # Implement your own evaluation logic
    pass

# Custom UI theme
def custom_ui_theme():
    """Custom UI color scheme and styling."""
    return {
        "red": {"piece": "red", "highlight": "bright_red"},
        "yellow": {"piece": "yellow", "highlight": "bright_yellow"},
        "board": "blue",
        "background": "black"
    }
```

## 📝 Contributing

### Development Setup

```bash
# Clone repository
git clone <repository-url>
cd haive/packages/haive-games

# Install dependencies
poetry install

# Run tests
poetry run pytest src/haive/games/connect4/tests/

# Run examples
poetry run python -m haive.games.connect4.example
```

### Code Style

- Follow PEP 8 guidelines
- Use type hints for all functions
- Add comprehensive docstrings
- Include unit tests for new features

### Documentation

- Update README.md for new features
- Add examples for new functionality
- Include performance considerations
- Document breaking changes

---

_This Connect4 module demonstrates the power of combining traditional game AI with modern language models, creating an engaging and educational gaming experience while maintaining high performance and code quality._
