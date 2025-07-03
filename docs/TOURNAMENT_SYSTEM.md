# Tournament System

The Haive Games package includes a comprehensive tournament system for running AI vs AI competitions.

## Overview

The tournament system allows you to:

- Run multiple games between different AI models
- Track wins, losses, and draws
- Generate detailed statistics
- Save results for analysis
- Run parallel games for faster execution

## Basic Tournament

### Quick Start

```python
from haive.games.tournament_tools.scripts.tournament_runner import TournamentRunner
from haive.core.models.llm import LLMConfig, LLMProvider

# Configure players
claude = LLMConfig(
    provider=LLMProvider.ANTHROPIC,
    model="claude-3-5-sonnet-20241022"
)

gpt4 = LLMConfig(
    provider=LLMProvider.AZURE,
    model="gpt-4o"
)

# Create tournament
tournament = TournamentRunner(
    player1_config=claude,
    player2_config=gpt4,
    games=["chess", "checkers", "reversi"],
    rounds_per_game=5
)

# Run tournament
results = tournament.run()
print(results.summary())
```

## Tournament Scripts

### 1. Check Working Games

Before running a tournament, verify which games are available:

```bash
poetry run python tournament_tools/scripts/check_working_games.py
```

Output:

```
=== WORKING GAMES (22/24) ===
 1. chess                - Agent: ChessAgent, Config: ChessConfig
 2. checkers             - Agent: CheckersAgent, Config: CheckersAgentConfig
...
SUMMARY: 22/24 games working (91.7% success rate)
```

### 2. Run Full Tournament

Run a complete tournament with all working games:

```python
# tournament_tools/scripts/claude_vs_openai_final_tournament.py

import asyncio
from tournament_runner import run_full_tournament

async def main():
    results = await run_full_tournament(
        games="all",  # or specific list
        output_dir="tournament_results",
        parallel=True
    )

asyncio.run(main())
```

### 3. Custom Tournament Configuration

```python
from haive.games.tournament_tools import TournamentConfig, Tournament

config = TournamentConfig(
    # Player configurations
    players={
        "Claude": claude_config,
        "GPT-4": gpt4_config,
        "Gemini": gemini_config
    },

    # Games to play
    games=[
        "chess", "go", "poker", "risk", "monopoly"
    ],

    # Tournament settings
    rounds_per_game=10,
    time_limit_per_move=30,  # seconds
    save_game_logs=True,
    parallel_games=4,

    # Scoring system
    scoring={
        "win": 3,
        "draw": 1,
        "loss": 0
    }
)

tournament = Tournament(config)
results = tournament.run()
```

## Tournament Results

### Result Format

```json
{
  "tournament": "Claude vs GPT-4",
  "timestamp": "2024-12-30T10:30:00",
  "total_games": 66,
  "completed_games": 65,
  "results": {
    "claude_wins": 35,
    "gpt4_wins": 28,
    "draws": 2,
    "errors": 1
  },
  "claude_win_rate": 0.556,
  "game_details": [
    {
      "game": "chess",
      "rounds": 3,
      "claude_wins": 2,
      "gpt4_wins": 1,
      "average_moves": 47.3,
      "average_duration": "5m 23s"
    }
  ]
}
```

### Analyzing Results

```python
from haive.games.tournament_tools.analysis import TournamentAnalyzer

analyzer = TournamentAnalyzer("tournament_results/")

# Overall statistics
stats = analyzer.get_statistics()
print(f"Claude win rate: {stats.claude_win_rate:.1%}")
print(f"Average game length: {stats.avg_game_length}")

# Per-game analysis
chess_stats = analyzer.get_game_stats("chess")
print(f"Chess: Claude {chess_stats.wins} - {chess_stats.losses} GPT-4")

# Generate report
analyzer.generate_report("tournament_report.html")
```

## Advanced Features

### 1. ELO Rating System

Track player ratings across tournaments:

```python
from haive.games.tournament_tools.elo import EloTracker

elo = EloTracker(initial_rating=1500)

# Update after each game
elo.update_ratings(
    winner="Claude",
    loser="GPT-4",
    game="chess"
)

# Get current ratings
ratings = elo.get_ratings()
print(f"Claude: {ratings['Claude']}")
print(f"GPT-4: {ratings['GPT-4']}")
```

### 2. Round-Robin Tournaments

Run every player against every other player:

```python
from haive.games.tournament_tools import RoundRobinTournament

players = {
    "Claude": claude_config,
    "GPT-4": gpt4_config,
    "Gemini": gemini_config,
    "Llama": llama_config
}

tournament = RoundRobinTournament(
    players=players,
    games=["chess", "go"],
    rounds_per_matchup=2
)

results = tournament.run()
```

### 3. Swiss System Tournaments

For larger player pools:

```python
from haive.games.tournament_tools import SwissTournament

swiss = SwissTournament(
    players=players,  # Can be 10+ players
    rounds=7,
    games=["chess"]
)

results = swiss.run()
```

## Visualization

### Tournament Progress

```python
from haive.games.tournament_tools.visualization import TournamentVisualizer

viz = TournamentVisualizer()

# Live progress tracking
with viz.live_display():
    tournament.run()

# Generate charts
viz.plot_win_rates("win_rates.png")
viz.plot_game_lengths("game_lengths.png")
viz.plot_rating_history("elo_history.png")
```

### Example Visualizations

1. **Win Rate Matrix**

```
         Claude  GPT-4  Gemini
Claude     -     0.65   0.72
GPT-4    0.35     -     0.58
Gemini   0.28   0.42     -
```

2. **Game Performance**

```
Chess:    Claude ████████████ 65%
          GPT-4  ████████ 35%

Poker:    Claude ███████ 45%
          GPT-4  ███████████ 55%
```

## Best Practices

### 1. Resource Management

```python
# Limit concurrent games
config.parallel_games = 4

# Set timeouts
config.game_timeout = 3600  # 1 hour per game
config.move_timeout = 60    # 1 minute per move

# Memory limits
config.max_game_history = 1000  # Moves to keep
```

### 2. Error Handling

```python
tournament = Tournament(config)

tournament.on_game_error = lambda game, error:
    print(f"Error in {game}: {error}")

tournament.retry_failed_games = True
tournament.max_retries = 3
```

### 3. Saving Game Logs

```python
config.save_game_logs = True
config.log_format = "json"  # or "pgn" for chess
config.log_directory = "game_logs/"

# Access logs after tournament
for game_log in tournament.get_game_logs():
    print(f"Game: {game_log.game}")
    print(f"Moves: {len(game_log.moves)}")
```

## Command-Line Interface

Run tournaments from the command line:

```bash
# Run specific tournament
poetry run tournament chess --rounds 10 --player1 claude --player2 gpt4

# Run all games
poetry run tournament all --parallel 4 --output results.json

# Run with custom config
poetry run tournament --config tournament_config.yaml
```

## Integration with CI/CD

Example GitHub Action for automated tournaments:

```yaml
name: AI Tournament
on:
  schedule:
    - cron: "0 0 * * 0" # Weekly

jobs:
  tournament:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Tournament
        run: |
          poetry install
          poetry run tournament all --output results.json
      - name: Upload Results
        uses: actions/upload-artifact@v3
        with:
          name: tournament-results
          path: results.json
```
