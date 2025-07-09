# Monopoly

A comprehensive implementation of the Monopoly board game with intelligent AI agents powered by Large Language Models (LLMs).

## Overview

The Monopoly game implementation provides sophisticated AI agents that can play the classic board game with strategic decision-making, property management, and adaptive gameplay. The system includes both game orchestration agents and individual player agents that use LLM reasoning to make intelligent decisions.

## Key Features

- **Strategic AI Players**: LLM-powered agents that analyze game state and make strategic decisions
- **Complete Game Implementation**: Full Monopoly board with properties, utilities, railroads, and special spaces
- **Property Management**: Intelligent buying, selling, mortgaging, and building decisions
- **Trade Negotiations**: Support for property trading between players (configurable)
- **Jail Mechanics**: Smart decisions for getting out of jail
- **Event System**: Chance and Community Chest cards with proper game effects
- **Game Orchestration**: Automated game flow with turn management and win conditions

## Quick Start

### Basic Game Setup

```python
from haive.games.monopoly import MonopolyGameAgent, MonopolyGameAgentConfig
from haive.games.monopoly import MonopolyPlayerAgent, MonopolyPlayerAgentConfig

# Create player agent for decision-making
player_config = MonopolyPlayerAgentConfig(
    name="player_agent",
    engine=your_llm_engine,
    temperature=0.7
)
player_agent = MonopolyPlayerAgent(player_config)

# Create game orchestration agent
game_config = MonopolyGameAgentConfig(
    name="monopoly_game",
    player_names=["Alice", "Bob", "Charlie"],
    max_turns=1000,
    enable_trading=True,
    player_agent=player_agent
)

game_agent = MonopolyGameAgent(game_config)

# Run the game
result = await game_agent.arun("Start a new Monopoly game")
```

### Simple Demo

```python
from haive.games.monopoly import MonopolyState
from haive.games.monopoly.utils import create_board, create_players, roll_dice, move_player

# Initialize game state
state = MonopolyState()
state.board = create_board()
state.players = create_players(["Alice", "Bob"])
state.current_player = 0

# Simulate a turn
dice_roll = roll_dice()
print(f"Player {state.players[0].name} rolled {dice_roll.total}")

# Move player and handle game events
state = move_player(state, 0, dice_roll.total)
```

## Core Components

### Game Agents

#### MonopolyGameAgent

The main orchestration agent that manages the overall game flow:

```python
from haive.games.monopoly import MonopolyGameAgent, MonopolyGameAgentConfig

config = MonopolyGameAgentConfig(
    name="monopoly_game",
    player_names=["Alice", "Bob", "Charlie", "Diana"],
    max_turns=1000,
    enable_trading=True
)

game_agent = MonopolyGameAgent(config)
```

#### MonopolyPlayerAgent

Individual player decision-making agent:

```python
from haive.games.monopoly import MonopolyPlayerAgent, MonopolyPlayerAgentConfig

config = MonopolyPlayerAgentConfig(
    name="strategic_player",
    engine=your_llm_engine,
    temperature=0.7
)

player_agent = MonopolyPlayerAgent(config)
```

### Game State

The `MonopolyState` class maintains complete game state:

```python
from haive.games.monopoly import MonopolyState

# Create new game state
state = MonopolyState()

# Access game components
print(f"Current player: {state.current_player}")
print(f"Players: {[p.name for p in state.players]}")
print(f"Properties: {len(state.board)}")
print(f"Game events: {len(state.events)}")
```

### Decision Types

The system supports various decision types:

```python
from haive.games.monopoly.models import (
    PropertyDecision,
    BuildingDecision,
    JailDecision,
    TradeResponse,
    PlayerActionType
)

# Property purchase decision
property_decision = PropertyDecision(
    action=PlayerActionType.BUY_PROPERTY,
    reasoning="This property completes a color group"
)

# Building decision
building_decision = BuildingDecision(
    action=PlayerActionType.BUILD_HOUSE,
    properties=["Boardwalk", "Park Place"],
    reasoning="Monopoly on high-rent properties"
)
```

## Game Flow

### Turn Structure

1. **Dice Roll**: Player rolls dice and moves
2. **Landing Effects**: Handle space effects (property, tax, cards, etc.)
3. **Decision Making**: AI agent evaluates options and makes decisions
4. **Action Execution**: Execute chosen actions (buy, build, trade, etc.)
5. **Turn End**: Check win conditions and advance to next player

### Strategic Decision Making

The AI agents consider multiple factors:

- **Property Value**: Purchase price vs. potential rent income
- **Color Group Completion**: Prioritize monopolies for building
- **Cash Flow Management**: Balance property investments with liquidity
- **Opponent Analysis**: Consider other players' positions and strategies
- **Risk Assessment**: Evaluate jail time, bankruptcy risks, and opportunity costs

## Advanced Usage

### Custom Player Strategies

You can customize player behavior by adjusting agent configurations:

```python
# Aggressive property buyer
aggressive_config = MonopolyPlayerAgentConfig(
    name="aggressive_player",
    engine=your_llm_engine,
    temperature=0.3,  # More consistent decisions
    # Add custom prompts for aggressive play
)

# Conservative player
conservative_config = MonopolyPlayerAgentConfig(
    name="conservative_player",
    engine=your_llm_engine,
    temperature=0.8,  # More varied decisions
    # Add custom prompts for conservative play
)
```

### Game Variants

Configure different game modes:

```python
# Quick game
quick_config = MonopolyGameAgentConfig(
    name="quick_monopoly",
    player_names=["Alice", "Bob"],
    max_turns=500,
    enable_trading=False
)

# Tournament mode
tournament_config = MonopolyGameAgentConfig(
    name="tournament_monopoly",
    player_names=["Player1", "Player2", "Player3", "Player4"],
    max_turns=2000,
    enable_trading=True
)
```

### Event Handling

Monitor game events and statistics:

```python
from haive.games.monopoly.models import GameEvent

# Access game events
for event in state.events:
    print(f"{event.turn}: {event.player} - {event.action}")
    if event.details:
        print(f"  Details: {event.details}")
```

## Testing

Run the test suite to verify functionality:

```bash
# Run all Monopoly tests
poetry run pytest packages/haive-games/tests/test_monopoly.py -v

# Run specific test
poetry run pytest packages/haive-games/tests/test_monopoly.py::test_init -v
```

## Examples

### Complete Game Example

```python
import asyncio
from haive.games.monopoly import (
    MonopolyGameAgent,
    MonopolyGameAgentConfig,
    MonopolyPlayerAgent,
    MonopolyPlayerAgentConfig
)

async def run_monopoly_game():
    """Run a complete Monopoly game with AI players."""

    # Create player agent
    player_config = MonopolyPlayerAgentConfig(
        name="ai_player",
        engine=your_llm_engine
    )
    player_agent = MonopolyPlayerAgent(player_config)

    # Create game agent
    game_config = MonopolyGameAgentConfig(
        name="monopoly_game",
        player_names=["Alice", "Bob", "Charlie"],
        player_agent=player_agent,
        enable_trading=True
    )
    game_agent = MonopolyGameAgent(game_config)

    # Run the game
    result = await game_agent.arun("Start new game")

    # Access final state
    final_state = game_agent.get_state()
    winner = final_state.winner
    print(f"Game completed! Winner: {winner}")

    return result

# Run the game
asyncio.run(run_monopoly_game())
```

### Property Analysis Example

```python
from haive.games.monopoly.utils import calculate_rent, get_property_at_position

# Analyze property at position
property_obj = get_property_at_position(state.board, 1)  # Mediterranean Avenue
if property_obj:
    rent = calculate_rent(property_obj, dice_roll=7)
    print(f"{property_obj.name}: ${rent} rent")

    # Check if property is part of a monopoly
    if property_obj.owner:
        owner_properties = [p for p in state.board if p.owner == property_obj.owner]
        color_group = [p for p in owner_properties if p.color == property_obj.color]
        print(f"Owner has {len(color_group)} properties in {property_obj.color} group")
```

## Key Classes

- **MonopolyGameAgent**: Main game orchestration agent
- **MonopolyPlayerAgent**: Individual player decision-making agent
- **MonopolyState**: Complete game state management
- **Player**: Individual player data and status
- **Property**: Property details and ownership
- **GameEvent**: Game event tracking and history

## Error Handling

The system includes robust error handling:

```python
try:
    result = await game_agent.arun("Invalid command")
except ValueError as e:
    print(f"Invalid game command: {e}")
except TimeoutError:
    print("Game timed out")
except Exception as e:
    print(f"Unexpected error: {e}")
```

This implementation provides a complete, intelligent Monopoly game experience with sophisticated AI players that can adapt and strategize throughout the game.
