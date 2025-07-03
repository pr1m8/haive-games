# Getting Started with Haive Games

This guide will help you get started with the Haive Games package.

## Installation

The Haive Games package is part of the main Haive installation. Ensure you have the Haive backend installed:

```bash
cd packages/haive-games
poetry install
```

## Basic Usage

### 1. Import Required Components

```python
from haive.games.chess import ChessAgent, ChessConfig
from haive.core.models.llm import LLMConfig, LLMProvider
```

### 2. Configure LLMs

Each player needs an LLM configuration:

```python
# Azure OpenAI Configuration
azure_llm = LLMConfig(
    provider=LLMProvider.AZURE,
    model="gpt-4o",
    api_key="your-api-key",
    api_base="https://your-endpoint.openai.azure.com/",
    api_version="2024-08-01-preview"
)

# Anthropic Configuration
claude_llm = LLMConfig(
    provider=LLMProvider.ANTHROPIC,
    model="claude-3-5-sonnet-20241022",
    api_key="your-api-key"
)
```

### 3. Create Game Configuration

Each game has specific configuration requirements:

```python
# Chess example
chess_config = ChessConfig(
    aug_llm_configs={
        "white": azure_llm,
        "black": claude_llm
    },
    max_moves=200
)

# Poker example
poker_config = PokerAgentConfig(
    aug_llm_configs={
        "player_1": azure_llm,
        "player_2": claude_llm
    },
    starting_chips=1000,
    max_rounds=20
)
```

### 4. Run a Game

```python
# Create agent
agent = ChessAgent(chess_config)

# Get initial state
initial_state = agent.get_initial_state()

# Run the game
for state in agent.app.stream(initial_state):
    # The state contains all game information
    print(f"Current turn: {state.get('current_player')}")
    print(f"Last move: {state.get('last_move')}")

    # Check for game over
    if state.get('game_over'):
        print(f"Game Over! Winner: {state.get('winner')}")
        break
```

## Simple Examples

### Tic-Tac-Toe Game

```python
from haive.games.tic_tac_toe import TicTacToeAgent, TicTacToeConfig

# Quick setup with default configs
config = TicTacToeConfig(
    aug_llm_configs={
        "player_1": azure_llm,
        "player_2": claude_llm
    }
)

agent = TicTacToeAgent(config)
initial_state = agent.get_initial_state()

# Run game
for state in agent.app.stream(initial_state):
    board = state.get('board')
    print(f"Board:\n{board}")

    if state.get('winner'):
        print(f"Winner: {state.get('winner')}")
        break
```

### Running a Tournament

```python
from haive.games.tournament_tools.scripts.tournament_runner import run_tournament

# Define games to play
games = ["chess", "checkers", "reversi"]

# Run tournament
results = run_tournament(
    games=games,
    player1_config=azure_llm,
    player2_config=claude_llm,
    rounds_per_game=3
)

print(f"Tournament Results: {results}")
```

## Common Patterns

### 1. State Access

All games provide state information in a consistent format:

```python
state = {
    "board": ...,           # Game board/cards/pieces
    "current_player": ...,  # Whose turn it is
    "last_move": ...,       # Previous action
    "game_over": False,     # Is game finished?
    "winner": None,         # Who won (if game_over)
    "turn_number": ...,     # Current turn/round
    "legal_moves": ...,     # Available actions
}
```

### 2. Custom Configurations

Many games support additional options:

```python
# Monopoly with custom settings
monopoly_config = MonopolyAgentConfig(
    aug_llm_configs={...},
    starting_money=1500,
    max_turns=100,
    enable_trading=True,
    house_rules={
        "free_parking_bonus": True,
        "double_salary_on_go": False
    }
)

# Mafia with specific roles
mafia_config = MafiaAgentConfig(
    aug_llm_configs={...},
    player_count=9,
    role_distribution={
        "mafia": 2,
        "detective": 1,
        "doctor": 1,
        "villager": 5
    }
)
```

### 3. Visualization

Some games provide visualization capabilities:

```python
# Chess with board visualization
for state in agent.app.stream(initial_state):
    agent.visualize_state(state)  # Prints ASCII board

# Games with rich UI (Hold'em)
from haive.games.hold_em.ui import HoldemRichUI
ui = HoldemRichUI()
ui.run(agent, delay=2.0)  # Live UI with 2-second delay
```

## Environment Variables

Set these environment variables for LLM access:

```bash
# Azure OpenAI
export AZURE_OPENAI_API_KEY="your-key"
export AZURE_OPENAI_ENDPOINT="https://your-endpoint.openai.azure.com/"

# Anthropic
export ANTHROPIC_API_KEY="your-key"

# Or use .env file
AZURE_OPENAI_API_KEY=your-key
ANTHROPIC_API_KEY=your-key
```

## Next Steps

- Explore [specific game examples](./examples/)
- Read about [game architecture](./ARCHITECTURE.md)
- Learn to [create new games](./DEVELOPMENT_GUIDE.md)
- Run [AI tournaments](./TOURNAMENT_SYSTEM.md)
