# Battleship

Classic naval strategy game with LLM-powered AI agents and advanced targeting strategies.

## Overview

The Battleship module provides a complete implementation of the classic naval combat game, featuring AI agents that use sophisticated targeting strategies, pattern recognition, and tactical reasoning. Built on the Haive framework, it supports configurable fleet compositions and multiple difficulty levels.

**Key Features:**

- **Classic Battleship Rules**: Standard 10x10 grid with traditional ship placement and targeting
- **AI-Powered Players**: LLM-based agents with strategic thinking and pattern recognition
- **Advanced Targeting**: Hunt-and-destroy algorithms with probability-based targeting
- **Flexible Fleet Configuration**: Customizable ship types, sizes, and quantities
- **Strategic Analysis**: Board evaluation, probability mapping, and move suggestions
- **Game Visualization**: Rich terminal display with board states and move history
- **Multi-Provider Support**: Works with Azure, OpenAI, and Anthropic LLM providers

**Naval Strategy Elements:**

- **Ship Placement**: Strategic positioning with clustering and spacing considerations
- **Targeting Patterns**: Systematic search patterns and adaptive strategies
- **Probability Analysis**: Statistical targeting based on remaining ship configurations
- **Hunt Mode**: Focused attacks after scoring hits
- **Pattern Recognition**: Learning from opponent behavior and shot patterns

## Architecture

The battleship implementation follows two-player game architecture:

```
BattleshipAgent
├── Configuration (BattleshipAgentConfig)
├── State Management (BattleshipStateManager)
├── Player Boards (ship placement and targeting grids)
├── LLM Engines (placement, targeting, analysis)
├── Strategy System (hunt/target modes)
└── Workflow (LangGraph-based game flow)
```

### Core Components

- **BattleshipAgent**: Main game controller managing flow and player interactions
- **BattleshipState**: Complete game state with boards, ships, and move history
- **BattleshipStateManager**: Rule enforcement, hit detection, and victory conditions
- **PlayerBoard**: Individual player's grid with ship placement and targeting data
- **Ship**: Individual vessel with size, position, orientation, and damage status
- **Strategy Engines**: LLM-powered placement and targeting decision makers
- **Analysis System**: Board evaluation and probability calculation

## Installation

This module is part of the `haive-games` package. Install it using:

```bash
pip install haive-games
```

## Usage Examples

### Basic Battleship Game

```python
from haive.games.battleship import BattleshipAgent, BattleshipAgentConfig
from haive.core.models.llm.configs import LLMConfig

# Configure LLM for battleship players
llm_config = LLMConfig(
    model="gpt-4",
    temperature=0.7,
    max_tokens=1000
)

# Create battleship agent
config = BattleshipAgentConfig(
    aug_llm_configs={
        "player1_placement": llm_config,
        "player1_targeting": llm_config,
        "player2_placement": llm_config,
        "player2_targeting": llm_config,
        "analyzer": llm_config
    },
    board_size=10,
    enable_analysis=True,
    show_boards=True
)

agent = BattleshipAgent(config)
result = agent.run_game()

print(f"Winner: {result.get('winner')}")
print(f"Total moves: {result.get('total_moves')}")
print(f"Game duration: {result.get('duration')} seconds")
```

### Custom Fleet Configuration

```python
# Configure custom fleet composition
custom_fleet = {
    "carrier": {"size": 5, "count": 1},      # Aircraft carrier
    "battleship": {"size": 4, "count": 1},  # Battleship
    "cruiser": {"size": 3, "count": 1},     # Cruiser
    "submarine": {"size": 3, "count": 1},   # Submarine
    "destroyer": {"size": 2, "count": 2}    # Two destroyers
}

config = BattleshipAgentConfig(
    aug_llm_configs=llm_configs,
    board_size=10,
    fleet_configuration=custom_fleet,
    enable_analysis=True
)

agent = BattleshipAgent(config)
result = agent.run_game()
```

### Different AI Personalities

```python
# Configure different player strategies
strategies = {
    "aggressive": LLMConfig(
        model="gpt-4",
        temperature=0.8,
        system_prompt="You are an aggressive naval commander who takes calculated risks and hunts enemy ships relentlessly."
    ),
    "defensive": LLMConfig(
        model="gpt-4",
        temperature=0.4,
        system_prompt="You are a defensive naval commander who uses systematic patterns and conservative strategies."
    ),
    "analytical": LLMConfig(
        model="gpt-4",
        temperature=0.5,
        system_prompt="You are an analytical naval commander who uses probability and statistical analysis for optimal play."
    )
}

config = BattleshipAgentConfig(
    aug_llm_configs={
        "player1_placement": strategies["aggressive"],
        "player1_targeting": strategies["aggressive"],
        "player2_placement": strategies["defensive"],
        "player2_targeting": strategies["defensive"],
        "analyzer": strategies["analytical"]
    }
)

agent = BattleshipAgent(config)
result = agent.run_game()
```

### Tournament with Statistics

```python
# Run multiple games for statistical analysis
tournament_stats = {
    "player1_wins": 0,
    "player2_wins": 0,
    "total_moves": [],
    "game_durations": []
}

for game_num in range(10):
    print(f"\nGame {game_num + 1}/10")
    agent = BattleshipAgent(config)
    result = agent.run_game(visualize=False)

    winner = result.get('winner')
    if winner == 'player1':
        tournament_stats['player1_wins'] += 1
    else:
        tournament_stats['player2_wins'] += 1

    tournament_stats['total_moves'].append(result.get('total_moves', 0))
    tournament_stats['game_durations'].append(result.get('duration', 0))

# Calculate statistics
avg_moves = sum(tournament_stats['total_moves']) / len(tournament_stats['total_moves'])
avg_duration = sum(tournament_stats['game_durations']) / len(tournament_stats['game_durations'])

print(f"\nTournament Results:")
print(f"Player 1 wins: {tournament_stats['player1_wins']}")
print(f"Player 2 wins: {tournament_stats['player2_wins']}")
print(f"Average game length: {avg_moves:.1f} moves")
print(f"Average duration: {avg_duration:.1f} seconds")
```

### Advanced Analysis Mode

```python
# Enable detailed analysis and probability mapping
config = BattleshipAgentConfig(
    aug_llm_configs=llm_configs,
    enable_analysis=True,
    probability_mapping=True,
    show_target_probabilities=True,
    analysis_depth=3,
    log_detailed_moves=True
)

agent = BattleshipAgent(config)
result = agent.run_game()

# Access detailed analytics
analysis = result.get('game_analysis', {})
print(f"Ship placement efficiency: {analysis.get('placement_score')}")
print(f"Targeting accuracy: {analysis.get('accuracy_percentage')}%")
print(f"Average shots per ship: {analysis.get('shots_per_ship')}")
```

### Custom Board Size

```python
# Play on different board sizes
for board_size in [8, 10, 12]:
    # Adjust fleet for board size
    if board_size == 8:
        fleet = {"destroyer": {"size": 2, "count": 2}, "cruiser": {"size": 3, "count": 1}}
    elif board_size == 12:
        fleet = {"carrier": {"size": 6, "count": 1}, "battleship": {"size": 5, "count": 1},
                "cruiser": {"size": 4, "count": 1}, "destroyer": {"size": 3, "count": 2}}
    else:
        fleet = None  # Use default

    config = BattleshipAgentConfig(
        aug_llm_configs=llm_configs,
        board_size=board_size,
        fleet_configuration=fleet
    )

    agent = BattleshipAgent(config)
    result = agent.run_game()
    print(f"Board {board_size}x{board_size}: Winner {result.get('winner')} in {result.get('total_moves')} moves")
```

## Naval Strategy & AI Tactics

### Ship Placement Strategies

1. **Clustering**: Group ships together to confuse targeting
2. **Spacing**: Spread ships to minimize damage from systematic search
3. **Edge Placement**: Use board edges to limit attack angles
4. **Diagonal Patterns**: Place ships diagonally to disrupt grid searches
5. **Decoy Positioning**: Use smaller ships to protect larger vessels

### Targeting Strategies

1. **Random Hunt**: Initial random targeting to find ships
2. **Grid Pattern**: Systematic coverage with optimal spacing
3. **Probability Targeting**: Target highest-probability squares
4. **Hunt and Destroy**: Focus on areas around hits
5. **Pattern Recognition**: Learn from opponent placement tendencies

### Advanced Tactics

- **Adaptive Targeting**: Adjust strategy based on hit/miss patterns
- **Endgame Optimization**: Efficient cleanup of remaining ships
- **Statistical Analysis**: Use game history for better placement
- **Bluffing Patterns**: Vary strategies to avoid predictability

## Configuration Options

### BattleshipAgentConfig

```python
class BattleshipAgentConfig:
    aug_llm_configs: Dict[str, LLMConfig]  # Player engines
    board_size: int = 10                   # Grid dimensions
    fleet_configuration: Dict = None       # Custom ship setup
    enable_analysis: bool = True           # Board analysis
    show_boards: bool = True               # Visual display
    probability_mapping: bool = False      # Show target probabilities
    analysis_depth: int = 2                # Analysis detail level
    max_moves_per_player: int = 100        # Game length limit
    enable_hints: bool = False             # Strategic hints
    log_detailed_moves: bool = False       # Detailed move logging
    allow_adjacent_ships: bool = False     # Ship touching rules
    diagonal_adjacency: bool = False       # Diagonal ship placement
```

### Fleet Configurations

**Standard Fleet:**

```python
standard_fleet = {
    "carrier": {"size": 5, "count": 1},
    "battleship": {"size": 4, "count": 1},
    "cruiser": {"size": 3, "count": 1},
    "submarine": {"size": 3, "count": 1},
    "destroyer": {"size": 2, "count": 1}
}
```

**Mini Fleet (faster games):**

```python
mini_fleet = {
    "cruiser": {"size": 3, "count": 1},
    "destroyer": {"size": 2, "count": 2}
}
```

### Engine Configurations

- **placement_engine**: Ship positioning strategy
- **targeting_engine**: Attack decision making
- **analysis_engine**: Board evaluation and probability calculation
- **strategy_engine**: High-level tactical planning (optional)

## API Reference

### BattleshipAgent

```python
class BattleshipAgent(Agent[BattleshipAgentConfig]):
    """Main battleship game agent."""

    def run_game(self, visualize: bool = True) -> Dict[str, Any]:
        """Run a complete battleship game."""

    def place_ships(self, player: str, board: PlayerBoard) -> PlayerBoard:
        """Handle ship placement for a player."""

    def make_move(self, state: BattleshipState, player: str) -> BattleshipState:
        """Process a player's targeting move."""

    def analyze_board(self, state: BattleshipState, player: str) -> Analysis:
        """Analyze current board state for strategic insights."""
```

### BattleshipStateManager

```python
class BattleshipStateManager:
    """Manages battleship game state and rules."""

    def initialize(self, board_size: int, fleet: Dict) -> BattleshipState:
        """Initialize new game state."""

    def process_shot(self, state: BattleshipState, player: str, target: Coordinates) -> MoveOutcome:
        """Process a targeting shot and return result."""

    def check_victory(self, state: BattleshipState) -> Optional[str]:
        """Check if game is won and return winner."""

    def get_valid_targets(self, board: PlayerBoard) -> List[Coordinates]:
        """Get all valid targeting coordinates."""

    def calculate_hit_probability(self, board: PlayerBoard, target: Coordinates) -> float:
        """Calculate probability of hit at target location."""
```

### Ship and Board Models

```python
class Ship:
    """Individual battleship."""
    name: str
    size: int
    position: List[Coordinates]
    orientation: str  # "horizontal" or "vertical"
    hits: List[bool]
    is_sunk: bool

class PlayerBoard:
    """Player's game board."""
    grid_size: int
    ships: List[Ship]
    shots_taken: List[Coordinates]
    hits: List[Coordinates]
    misses: List[Coordinates]
    enemy_ships_sunk: int

class MoveOutcome:
    """Result of a targeting move."""
    target: Coordinates
    result: str  # "hit", "miss", "sunk"
    ship_sunk: Optional[str] = None
    remaining_ships: int
```

## Game Mechanics

### Ship Placement Rules

1. **Grid Bounds**: Ships must fit entirely within board
2. **Orientation**: Ships placed horizontally or vertically only
3. **Adjacency**: Ships cannot touch (configurable)
4. **Validation**: Automatic checking for legal placements

### Targeting Rules

1. **One Shot Per Turn**: Players alternate single shots
2. **No Repeats**: Cannot target same square twice
3. **Hit Feedback**: Immediate notification of hit/miss/sunk
4. **Victory Condition**: Game ends when all enemy ships are sunk

### Board Coordinates

```
10x10 Standard Board:
   A B C D E F G H I J
10 . . . . . . . . . . 10
 9 . . . . . . . . . .  9
 8 . . . . . . . . . .  8
 7 . . . . . . . . . .  7
 6 . . . . . . . . . .  6
 5 . . . . . . . . . .  5
 4 . . . . . . . . . .  4
 3 . . . . . . . . . .  3
 2 . . . . . . . . . .  2
 1 . . . . . . . . . .  1
   A B C D E F G H I J
```

## Performance & Optimization

### Recommended Settings

```python
# Fast games
config = BattleshipAgentConfig(
    board_size=8,
    fleet_configuration=mini_fleet,
    enable_analysis=False,
    show_boards=False
)

# Standard games
config = BattleshipAgentConfig(
    board_size=10,
    enable_analysis=True,
    probability_mapping=True,
    analysis_depth=2
)

# Tournament mode
config = BattleshipAgentConfig(
    board_size=10,
    enable_analysis=False,
    log_detailed_moves=True,
    max_moves_per_player=50
)
```

### Memory Usage

- **Game State**: ~5KB per game state
- **Board Analysis**: ~10KB per analysis
- **Move History**: ~2KB for 100-move game
- **Probability Maps**: ~3KB per board

## Testing

Run battleship-specific tests:

```bash
# Run all battleship tests
poetry run pytest packages/haive-games/tests/test_battleship/ -v

# Test specific functionality
poetry run pytest packages/haive-games/tests/test_battleship/test_placement.py -v
poetry run pytest packages/haive-games/tests/test_battleship/test_targeting.py -v
```

## Troubleshooting

### Common Issues

1. **Invalid Ship Placement**

   ```python
   # Enable placement debugging
   config.log_detailed_moves = True
   config.enable_hints = True
   ```

2. **Targeting Errors**

   ```python
   # Check coordinate validation
   valid_targets = state_manager.get_valid_targets(board)
   ```

3. **Game Too Long**

   ```python
   # Set move limits
   config.max_moves_per_player = 50
   ```

4. **Performance Issues**
   ```python
   # Disable heavy features
   config.enable_analysis = False
   config.probability_mapping = False
   ```

### Strategy Optimization

- Use higher `temperature` for creative placement
- Lower `temperature` for systematic targeting
- Enable `probability_mapping` for better accuracy
- Adjust `analysis_depth` based on performance needs

## Advanced Features

### Custom Targeting Algorithms

```python
# Implement custom targeting strategy
class CustomTargetingEngine:
    def generate_target(self, board_state: PlayerBoard) -> Coordinates:
        # Your custom targeting logic here
        return best_target

config.custom_targeting_engine = CustomTargetingEngine()
```

### Real-time Visualization

```python
# Enable live board updates
config.real_time_display = True
config.animation_speed = 0.5  # seconds between moves
config.show_probability_heatmap = True
```

## See Also

- [Chess](../chess/): Another classic strategy game with similar depth
- [Checkers](../checkers/): Board game with tactical elements
- [Connect4](../connect4/): Grid-based strategy game
- [Tic-Tac-Toe](../tic_tac_toe/): Simpler grid game for comparison
- [Naval Strategy Resources](https://en.wikipedia.org/wiki/Naval_strategy): Historical naval tactics
- [Game Theory](https://en.wikipedia.org/wiki/Game_theory): Mathematical strategy concepts
