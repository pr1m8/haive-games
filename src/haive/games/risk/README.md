# Risk

A complete implementation of the classic board game Risk with sophisticated AI agents that use Large Language Models for strategic decision-making.

## Overview

The Risk game module provides a full implementation of the classic world domination strategy game, featuring intelligent AI agents that can analyze territorial positions, plan attacks, manage reinforcements, and execute complex strategic maneuvers. The system supports customizable game rules, multiple player counts, and advanced strategic analysis.

## Key Features

- **Complete Risk Implementation**: Full classic Risk rules with territories, continents, armies, and cards
- **Strategic AI Agents**: LLM-powered agents with sophisticated strategic reasoning
- **Flexible Game Configuration**: Customizable rules, player counts, and game variants
- **Territory Management**: Complete world map with adjacency relationships and continent bonuses
- **Combat System**: Dice-based combat with proper attack/defense mechanics
- **Card Trading**: Risk card collection and trading for reinforcement armies
- **Phase Management**: Proper game phase progression (reinforce, attack, fortify)
- **Strategic Analysis**: Deep position analysis and move recommendations

## Quick Start

### Basic Game Setup

```python
from haive.games.risk import RiskStateManager, RiskAgent, RiskConfig

# Initialize a 3-player game
players = ["Napoleon", "Caesar", "Alexander"]
config = RiskConfig.classic()
manager = RiskStateManager.initialize(players, config)

# Create AI agents for each player
agents = {
    name: RiskAgent(name=name, state=manager.state, strategy="balanced")
    for name in players
}

# Game loop
while not manager.state.is_game_over():
    current_player = manager.state.current_player
    agent = agents[current_player]

    # Get strategic move from agent
    move = agent.get_move()

    # Apply move to game state
    manager.apply_move(move)
    print(f"Turn {manager.state.turn_number}: {current_player} - {move}")

# Determine winner
winner = manager.state.get_winner()
print(f"Game over! {winner} has conquered the world!")
```

### Simple Territory Analysis

```python
from haive.games.risk import RiskState, Territory

# Create game state
state = RiskState()

# Access territory information
for territory in state.territories:
    print(f"{territory.name} ({territory.continent}): {territory.armies} armies")
    if territory.owner:
        print(f"  Controlled by: {territory.owner}")
    print(f"  Adjacent to: {', '.join(territory.adjacent)}")
```

## Core Components

### Game State Management

#### RiskState

Complete game state representation:

```python
from haive.games.risk import RiskState

# Create new game state
state = RiskState()

# Access game information
print(f"Current player: {state.current_player}")
print(f"Game phase: {state.current_phase}")
print(f"Turn number: {state.turn_number}")
print(f"Territories: {len(state.territories)}")
print(f"Players: {[p.name for p in state.players]}")
```

#### RiskStateManager

Manages state transitions and rule enforcement:

```python
from haive.games.risk import RiskStateManager, RiskConfig

# Initialize game
players = ["Player1", "Player2", "Player3"]
config = RiskConfig.classic()
manager = RiskStateManager.initialize(players, config)

# Apply moves
from haive.games.risk.models import RiskMove, MoveType

# Reinforce territory
reinforce_move = RiskMove(
    move_type=MoveType.REINFORCE,
    player=manager.state.current_player,
    territory="Alaska",
    armies=3
)
manager.apply_move(reinforce_move)
```

### Strategic AI Agent

#### RiskAgent

LLM-powered strategic agent:

```python
from haive.games.risk import RiskAgent

# Create agent with specific strategy
agent = RiskAgent(
    name="General Patton",
    state=game_state,
    strategy="aggressive"  # or "defensive", "balanced"
)

# Get strategic analysis
analysis = agent.analyze_position()
print(f"Territories controlled: {analysis.controlled_territories}")
print(f"Strategic recommendation: {analysis.recommendation}")
print(f"Threat level: {analysis.threat_level}")

# Get next move
move = agent.get_move()
print(f"Agent decides: {move}")
```

### Game Models

#### Territory

Represents a territory on the Risk board:

```python
from haive.games.risk.models import Territory

# Create territory
territory = Territory(
    name="Alaska",
    continent="North America",
    owner="Player1",
    armies=5,
    adjacent=["Northwest Territory", "Alberta", "Kamchatka"]
)

# Check territory properties
print(f"Strategic value: {territory.strategic_value}")
print(f"Border territory: {territory.is_border}")
print(f"Can attack: {territory.can_attack}")
```

#### Card System

Risk card collection and trading:

```python
from haive.games.risk.models import Card, CardType

# Create cards
cards = [
    Card(card_type=CardType.INFANTRY, territory_name="Alaska"),
    Card(card_type=CardType.CAVALRY, territory_name="Brazil"),
    Card(card_type=CardType.ARTILLERY, territory_name="Egypt"),
    Card(card_type=CardType.WILD)
]

# Check card combinations
def can_trade_cards(cards):
    """Check if cards can be traded for armies."""
    if len(cards) < 3:
        return False

    # Check for matching set or one of each type
    types = [card.card_type for card in cards]
    return len(set(types)) == 1 or len(set(types)) == 3
```

## Game Configuration

### RiskConfig

Customize game rules and parameters:

```python
from haive.games.risk import RiskConfig

# Classic Risk rules
classic_config = RiskConfig.classic()

# Custom configuration
custom_config = RiskConfig(
    player_count=4,
    use_mission_cards=True,
    allow_card_trade_anytime=True,
    escalating_card_values=True,
    fortify_from_multiple_territories=True,
    max_attack_dice=3,
    max_defense_dice=2
)

# Quick game variant
quick_config = RiskConfig(
    player_count=2,
    balanced_initial_placement=True,
    escalating_card_values=False,
    allow_card_trade_anytime=True
)
```

### Game Variants

#### Classic Risk

Standard world domination game:

```python
classic_config = RiskConfig.classic()
manager = RiskStateManager.initialize(players, classic_config)
```

#### Mission-Based Risk

Alternative win conditions with mission cards:

```python
mission_config = RiskConfig(
    player_count=4,
    use_mission_cards=True,
    balanced_initial_placement=True
)
manager = RiskStateManager.initialize(players, mission_config)
```

## Combat System

### Attack Mechanics

```python
from haive.games.risk.models import RiskMove, MoveType

# Launch attack
attack_move = RiskMove(
    move_type=MoveType.ATTACK,
    player="Player1",
    territory="Alaska",      # Attacking from
    target="Kamchatka",      # Attacking to
    armies=3                 # Attacking armies
)

# The state manager handles dice rolling and combat resolution
result = manager.apply_move(attack_move)
```

### Defense Strategy

```python
# Agent automatically handles defense decisions
agent = RiskAgent(name="Defender", state=state, strategy="defensive")

# Defensive agents prioritize:
# - Fortifying border territories
# - Maintaining strong defensive positions
# - Protecting continent bonuses
```

## Strategic Analysis

### Position Evaluation

```python
from haive.games.risk.models import RiskAnalysis

# Get detailed position analysis
analysis = agent.analyze_position()

print(f"Player: {analysis.player}")
print(f"Controlled territories: {analysis.controlled_territories}")
print(f"Total armies: {analysis.total_armies}")
print(f"Continent bonuses: {analysis.continent_bonuses}")
print(f"Strategic strength: {analysis.strategic_strength}")
print(f"Threat assessment: {analysis.threat_level}")
print(f"Recommended action: {analysis.recommendation}")
```

### Continental Strategy

```python
# Check continent control
def analyze_continent_control(state, continent_name):
    """Analyze control of a specific continent."""
    continent_territories = [
        t for t in state.territories
        if t.continent == continent_name
    ]

    players = {}
    for territory in continent_territories:
        if territory.owner:
            players[territory.owner] = players.get(territory.owner, 0) + 1

    total_territories = len(continent_territories)
    return {
        "total_territories": total_territories,
        "control_breakdown": players,
        "bonus_value": state.get_continent_bonus(continent_name)
    }

# Example usage
na_analysis = analyze_continent_control(state, "North America")
print(f"North America: {na_analysis}")
```

## Advanced Features

### Multi-Phase Strategy

```python
from haive.games.risk.models import PhaseType

# Agents adapt strategy based on game phase
def get_phase_strategy(agent, phase):
    """Get strategy based on current game phase."""
    if phase == PhaseType.REINFORCE:
        return agent.plan_reinforcement()
    elif phase == PhaseType.ATTACK:
        return agent.plan_attacks()
    elif phase == PhaseType.FORTIFY:
        return agent.plan_fortification()
```

### Dynamic Difficulty

```python
# Adjust agent difficulty
beginner_agent = RiskAgent(
    name="Beginner",
    state=state,
    strategy="balanced",
    # Could add difficulty parameter in future
)

expert_agent = RiskAgent(
    name="Expert",
    state=state,
    strategy="aggressive",
    # Advanced strategic reasoning
)
```

## Game Flow

### Turn Structure

1. **Reinforcement Phase**: Place armies based on territories and continent bonuses
2. **Attack Phase**: Launch attacks against adjacent enemy territories
3. **Fortification Phase**: Move armies between connected territories
4. **Card Management**: Trade cards for additional armies

### Victory Conditions

```python
# Check for game end conditions
def check_victory(state):
    """Check if game has ended."""
    if state.use_mission_cards:
        # Check mission completion
        return state.check_mission_victory()
    else:
        # Check world domination
        return state.check_domination_victory()
```

## Testing

Run the test suite to verify functionality:

```bash
# Run all Risk tests
poetry run pytest packages/haive-games/tests/games/risk/ -v

# Run specific test categories
poetry run pytest packages/haive-games/tests/games/risk/test_risk_models.py -v
poetry run pytest packages/haive-games/tests/games/risk/test_risk_state.py -v
```

## Examples

### Tournament Play

```python
import asyncio
from haive.games.risk import RiskStateManager, RiskAgent, RiskConfig

async def run_risk_tournament():
    """Run a Risk tournament with multiple AI agents."""

    # Tournament configuration
    tournament_config = RiskConfig(
        player_count=4,
        use_mission_cards=False,
        escalating_card_values=True,
        balanced_initial_placement=True
    )

    # Create players with different strategies
    players = ["Aggressive", "Defensive", "Balanced", "Adaptive"]
    strategies = ["aggressive", "defensive", "balanced", "balanced"]

    # Initialize game
    manager = RiskStateManager.initialize(players, tournament_config)

    # Create agents
    agents = {
        name: RiskAgent(name=name, state=manager.state, strategy=strategy)
        for name, strategy in zip(players, strategies)
    }

    # Run tournament
    turn_count = 0
    while not manager.state.is_game_over() and turn_count < 1000:
        current_player = manager.state.current_player
        agent = agents[current_player]

        # Get strategic move
        move = agent.get_move()

        # Apply move
        manager.apply_move(move)

        turn_count += 1
        if turn_count % 10 == 0:
            print(f"Turn {turn_count}: Game in progress...")

    # Determine winner
    winner = manager.state.get_winner()
    print(f"Tournament complete! Winner: {winner}")

    # Game statistics
    print(f"Total turns: {turn_count}")
    print(f"Final territories per player:")
    for player in manager.state.players:
        territories = [t for t in manager.state.territories if t.owner == player.name]
        print(f"  {player.name}: {len(territories)} territories")

    return winner

# Run tournament
winner = asyncio.run(run_risk_tournament())
```

### Custom Map Support

```python
# Define custom territory adjacencies
custom_map = {
    "Territory1": ["Territory2", "Territory3"],
    "Territory2": ["Territory1", "Territory4"],
    "Territory3": ["Territory1", "Territory4"],
    "Territory4": ["Territory2", "Territory3"]
}

# Create custom configuration
custom_config = RiskConfig(
    player_count=3,
    custom_territories=custom_map,
    balanced_initial_placement=True
)

# Initialize game with custom map
manager = RiskStateManager.initialize(players, custom_config)
```

## Key Classes

- **RiskStateManager**: Game state management and rule enforcement
- **RiskAgent**: Strategic AI agent with LLM decision-making
- **RiskState**: Complete game state representation
- **RiskConfig**: Customizable game rules and parameters
- **Territory**: Individual territory with armies and adjacencies
- **Card**: Risk cards for army reinforcement
- **Player**: Player state with cards and elimination status

## Error Handling

The system includes comprehensive error handling:

```python
try:
    # Apply potentially invalid move
    manager.apply_move(risky_move)
except ValueError as e:
    print(f"Invalid move: {e}")
except GameOverError:
    print("Game has already ended")
except InsufficientArmiesError:
    print("Not enough armies for this action")
```

This implementation provides a complete, strategic Risk game experience with intelligent AI agents that can analyze positions, plan campaigns, and execute complex military strategies.
