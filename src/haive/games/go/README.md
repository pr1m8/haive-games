# Go

Advanced Go (Weiqi/Baduk) game implementation with LLM-powered AI players and SGF support.

## Overview

The Go module provides a comprehensive implementation of the ancient strategy game Go, featuring AI players that understand complex territorial concepts, strategic patterns, and traditional Go principles. Built on the Haive framework with SGF (Smart Game Format) support for professional game analysis.

**Key Features:**

- **Complete Go Rules**: Full implementation including ko rule, territory scoring, and game ending
- **Multiple Board Sizes**: Support for 9x9, 13x13, and 19x19 boards
- **AI Players**: LLM-based agents that understand Go strategy, joseki patterns, and territorial concepts
- **SGF Integration**: Import/export games in standard SGF format using the sente library
- **Position Analysis**: Deep evaluation of board positions, territory estimation, and move suggestions
- **Professional Features**: Handicap stones, komi, and tournament-style timing
- **Rich Visualization**: Beautiful terminal display with coordinate systems and move history

**Go Concepts Implemented:**

- **Territory Control**: Area scoring with dead stone removal
- **Capture Mechanics**: Stone capture and liberties calculation
- **Ko Rule**: Prevention of immediate board repetition
- **Life and Death**: Basic tsumego (life and death) analysis
- **Strategic Patterns**: Opening principles, middle game fighting, endgame technique

## Architecture

The Go implementation follows traditional game engine architecture with AI enhancements:

```
GoAgent
├── Configuration (GoAgentConfig)
├── Game Engine (sente library integration)
├── State Management (GoGameStateManager)
├── LLM Players (black_player, white_player, analyzer)
├── SGF Support (game import/export)
└── Workflow (LangGraph-based game flow)
```

### Core Components

- **GoAgent**: Main game controller with LangGraph workflow
- **GoGameState**: Complete board state with move history and scoring
- **GoGameStateManager**: Rule enforcement, move validation, and territory calculation
- **sente Integration**: Professional Go engine for rules and SGF support
- **GoAnalysis**: Position evaluation with territorial and strategic analysis
- **GoMoveModel**: Structured move representation with coordinates and reasoning

## Installation

This module is part of the `haive-games` package with additional Go dependencies:

```bash
# Install haive-games
pip install haive-games

# Additional dependencies for Go
pip install sente  # For SGF support and Go rules
```

## Usage Examples

### Basic 19x19 Game

```python
from haive.games.go import GoAgent, GoAgentConfig
from haive.core.models.llm.configs import LLMConfig

# Configure LLM for Go players
llm_config = LLMConfig(
    model="gpt-4",
    temperature=0.7,
    max_tokens=1500
)

# Create Go agent for standard 19x19 game
config = GoAgentConfig(
    aug_llm_configs={
        "black_player": llm_config,
        "white_player": llm_config,
        "analyzer": llm_config
    },
    board_size=19,
    include_analysis=True,
    komi=6.5,
    max_moves=400
)

agent = GoAgent(config)
result = agent.run_game()

print(f"Game result: {result.get('winner')}")
print(f"Final score: {result.get('score')}")
print(f"Total moves: {result.get('move_count')}")
```

### Quick 9x9 Game

```python
# Faster game on smaller board
config = GoAgentConfig(
    aug_llm_configs=llm_configs,
    board_size=9,
    include_analysis=False,
    komi=5.5,
    max_moves=100
)

agent = GoAgent(config)
result = agent.run_game(visualize=True)
```

### Professional Game Analysis

```python
# Load and analyze professional game
from haive.games.go.state_manager import GoGameStateManager

# Load SGF file
state_manager = GoGameStateManager()
state = state_manager.load_sgf("professional_game.sgf")

# Analyze key positions
for move_number in [50, 100, 150, 200]:
    position_state = state_manager.get_position_at_move(state, move_number)
    analysis = agent.analyze_position(position_state)

    print(f"Move {move_number} Analysis:")
    print(f"Territory: Black {analysis.black_territory}, White {analysis.white_territory}")
    print(f"Best move: {analysis.best_move}")
    print(f"Strategic assessment: {analysis.notes}")
```

### Handicap Game

```python
# Configure handicap game for skill difference
config = GoAgentConfig(
    aug_llm_configs={
        "black_player": LLMConfig(
            model="gpt-3.5-turbo",  # Weaker player gets handicap
            temperature=0.8
        ),
        "white_player": LLMConfig(
            model="gpt-4",  # Stronger player
            temperature=0.6
        )
    },
    board_size=19,
    handicap_stones=4,  # 4 stone handicap
    komi=0.5,  # Reduced komi for handicap
    include_analysis=True
)

agent = GoAgent(config)
result = agent.run_game()
```

### Tournament with Different Playing Styles

```python
# Configure different AI personalities
styles = {
    "territorial": LLMConfig(
        model="gpt-4",
        temperature=0.4,
        system_prompt="You play territorial Go, focusing on secure territory and solid play."
    ),
    "fighting": LLMConfig(
        model="gpt-4",
        temperature=0.8,
        system_prompt="You play fighting Go, seeking complex battles and tactical opportunities."
    ),
    "influence": LLMConfig(
        model="gpt-4",
        temperature=0.6,
        system_prompt="You play influence-oriented Go, building large-scale strategic frameworks."
    )
}

# Tournament between styles
for black_style, white_style in [("territorial", "fighting"), ("fighting", "influence")]:
    config = GoAgentConfig(
        aug_llm_configs={
            "black_player": styles[black_style],
            "white_player": styles[white_style]
        },
        board_size=19
    )

    agent = GoAgent(config)
    result = agent.run_game()
    print(f"{black_style} vs {white_style}: {result.get('winner')} wins")
```

## Go Strategy & AI Understanding

### Opening Principles

1. **Corner-Side-Center**: Secure corners first, then sides, finally center
2. **Joseki Knowledge**: Standard corner patterns for balanced play
3. **Direction of Play**: Choose correct side for development
4. **Influence vs Territory**: Balance between immediate territory and future potential

### Middle Game Concepts

- **Life and Death**: Ensuring group survival through eye formation
- **Attack and Defense**: Pressuring weak groups while securing your own
- **Fighting**: Complex tactical battles in local areas
- **Shape**: Efficient stone placement for strength and mobility

### Endgame Technique

- **Yose**: Endgame moves that determine final territory
- **Ko Fights**: Strategic use of ko threats and timing
- **Counting**: Accurate territory estimation for optimal play
- **Sente vs Gote**: Initiative management in the endgame

## Configuration Options

### GoAgentConfig

```python
class GoAgentConfig:
    aug_llm_configs: Dict[str, LLMConfig]  # Player engines
    board_size: int = 19                   # 9, 13, or 19
    include_analysis: bool = True          # Position analysis
    komi: float = 6.5                      # Compensation for white
    handicap_stones: int = 0               # Black handicap stones
    max_moves: int = 400                   # Maximum game length
    sgf_output: bool = True                # Save games as SGF
    analysis_depth: int = 3                # Analysis detail level
    time_control: Optional[int] = None     # Seconds per move
    scoring_method: str = "area"           # "area" or "territory"
```

### Engine Configurations

- **black_player**: Black stone player engine
- **white_player**: White stone player engine
- **analyzer**: Position analysis and evaluation engine
- **joseki_engine**: Opening pattern recognition (optional)

## API Reference

### GoAgent

```python
class GoAgent(Agent[GoAgentConfig]):
    """Main Go game agent."""

    def run_game(self) -> Dict[str, Any]:
        """Run a complete Go game."""

    def analyze_position(self, state: GoGameState) -> GoAnalysis:
        """Analyze a Go position."""

    def make_move(self, state: GoGameState, player: str, move: str) -> GoGameState:
        """Make a move in the game."""

    def export_sgf(self, state: GoGameState) -> str:
        """Export game as SGF format."""
```

### GoGameStateManager

```python
class GoGameStateManager:
    """Manages Go game state and rules."""

    def initialize(self, board_size: int = 19) -> GoGameState:
        """Initialize new game state."""

    def get_legal_moves(self, state: GoGameState, player: str) -> List[str]:
        """Get all legal moves for player."""

    def calculate_score(self, state: GoGameState) -> Dict[str, float]:
        """Calculate final game score."""

    def load_sgf(self, sgf_path: str) -> GoGameState:
        """Load game from SGF file."""

    def save_sgf(self, state: GoGameState, path: str) -> None:
        """Save game to SGF file."""
```

### GoAnalysis

```python
class GoAnalysis:
    """Go position analysis results."""

    territory_estimate: Dict[str, int]     # Territory count by player
    best_moves: List[str]                  # Top move candidates
    strategic_assessment: str              # Position evaluation
    tactical_threats: List[str]            # Immediate threats
    joseki_suggestions: List[str]          # Pattern recommendations
    life_death_status: Dict[str, str]      # Group safety analysis
```

## Board Representation

### Coordinate System

```
19x19 Board Coordinates:
   A B C D E F G H J K L M N O P Q R S T
19 . . . . . . . . . . . . . . . . . . . 19
18 . . . . . . . . . . . . . . . . . . . 18
17 . . . . . . . . . . . . . . . . . . . 17
...
 2 . . . . . . . . . . . . . . . . . . .  2
 1 . . . . . . . . . . . . . . . . . . .  1
   A B C D E F G H J K L M N O P Q R S T

Note: I is skipped in traditional Go notation
```

### Move Notation

- **Standard**: "D4", "Q16", "K10" (column + row)
- **Pass**: "pass" or "PASS"
- **Resign**: "resign" or "RESIGN"

## Performance & Optimization

### Recommended Settings

```python
# Fast games (9x9)
config = GoAgentConfig(
    board_size=9,
    include_analysis=False,
    max_moves=100,
    komi=5.5
)

# Standard games (19x19)
config = GoAgentConfig(
    board_size=19,
    include_analysis=True,
    analysis_depth=2,
    max_moves=400,
    komi=6.5
)

# Professional analysis
config = GoAgentConfig(
    board_size=19,
    include_analysis=True,
    analysis_depth=4,
    sgf_output=True,
    time_control=300  # 5 minutes per move
)
```

### Memory Usage

- **9x9 Game**: ~5KB per game state
- **19x19 Game**: ~20KB per game state
- **SGF Files**: ~50KB for 300-move game
- **Analysis Data**: ~15KB per position analysis

## Testing

Run Go-specific tests:

```bash
# Run all Go tests
poetry run pytest packages/haive-games/tests/test_go/ -v

# Test SGF functionality
poetry run pytest packages/haive-games/tests/test_go/test_sgf.py -v

# Test game rules
poetry run pytest packages/haive-games/tests/test_go/test_rules.py -v
```

## Troubleshooting

### Common Issues

1. **Invalid Move Errors**

   ```python
   # Enable detailed move validation
   config.log_level = "DEBUG"
   ```

2. **SGF Import Errors**

   ```python
   # Check SGF file format
   state_manager.validate_sgf("game.sgf")
   ```

3. **Scoring Discrepancies**

   ```python
   # Use manual territory marking
   config.scoring_method = "territory"
   ```

4. **Performance Issues**
   ```python
   # Reduce analysis depth
   config.analysis_depth = 1
   config.include_analysis = False
   ```

## Advanced Features

### Custom Joseki Database

```python
# Load custom opening patterns
from haive.games.go.joseki import JosekiDatabase

joseki_db = JosekiDatabase()
joseki_db.load_patterns("custom_joseki.json")

config.joseki_database = joseki_db
```

### Time Control Integration

```python
# Tournament time controls
config = GoAgentConfig(
    time_control=1800,  # 30 minutes main time
    byo_yomi=30,        # 30 seconds per move
    byo_yomi_periods=5  # 5 overtime periods
)
```

## See Also

- [Chess](../chess/): Another complex strategy game implementation
- [Checkers](../checkers/): Simpler board game for comparison
- [SGF Specification](https://www.red-bean.com/sgf/): Standard Game Format documentation
- [Go Rules](https://www.usgo.org/aga-concise-rules-go): Official game rules
- [Sente Library](https://github.com/atw1020/sente): Python Go library used for rules
- [Professional Go Resources](https://online-go.com/): Online Go community and games
