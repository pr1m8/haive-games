# Troubleshooting Guide

This guide helps resolve common issues when using the Haive Games package.

## Common Issues

### 1. Import Errors

#### Problem: `ModuleNotFoundError: No module named 'haive.games'`

**Solution:**

```bash
# Ensure you're in the correct directory
cd packages/haive-games

# Install with poetry
poetry install

# Verify installation
poetry run python -c "import haive.games; print('Success!')"
```

#### Problem: `ImportError: cannot import name 'GameAgent'`

**Solution:**
Check the correct import path:

```python
# Correct imports
from haive.games.chess import ChessAgent, ChessConfig
from haive.games.poker import PokerAgent, PokerAgentConfig

# NOT this
from haive.games import ChessAgent  # Wrong!
```

### 2. LLM Configuration Issues

#### Problem: `API key not found`

**Solution:**
Set environment variables:

```bash
# Option 1: Export in shell
export AZURE_OPENAI_API_KEY="your-key"
export ANTHROPIC_API_KEY="your-key"

# Option 2: Use .env file
echo "AZURE_OPENAI_API_KEY=your-key" >> .env
echo "ANTHROPIC_API_KEY=your-key" >> .env
```

#### Problem: `Invalid API endpoint`

**Solution:**
Ensure correct endpoint format:

```python
# Azure OpenAI
azure_config = LLMConfig(
    provider=LLMProvider.AZURE,
    api_base="https://your-resource.openai.azure.com/",  # Must end with /
    api_version="2024-08-01-preview"  # Check latest version
)

# Anthropic
anthropic_config = LLMConfig(
    provider=LLMProvider.ANTHROPIC,
    api_key="sk-ant-..."  # Must start with sk-ant-
)
```

### 3. Game-Specific Issues

#### Chess: `Invalid move format`

**Problem:** LLM returns moves in wrong format

**Solution:**
Ensure the LLM is configured with proper chess notation:

```python
# The game expects algebraic notation
# Good: "e2e4", "Nf3", "O-O"
# Bad: "e2 to e4", "knight to f3"

# You can add format validation
def validate_chess_move(move: str) -> bool:
    import re
    pattern = r'^[a-h][1-8][a-h][1-8][qrbn]?$|^[KQRBN][a-h]?[1-8]?x?[a-h][1-8]$|^O-O(-O)?$'
    return bool(re.match(pattern, move))
```

#### Poker: `Invalid bet amount`

**Problem:** Player tries to bet more than they have

**Solution:**
The game automatically caps bets:

```python
# This is handled internally, but you can configure limits
poker_config = PokerAgentConfig(
    min_bet=10,
    max_bet=1000,
    starting_chips=1000
)
```

#### Go: `sente module not found`

**Problem:** Go game requires sente library

**Solution:**
The Go game now uses sgfmill (included). If you see this error, update to latest version:

```bash
git pull
poetry install
```

### 4. Performance Issues

#### Problem: Games running slowly

**Solutions:**

1. **Reduce LLM calls:**

```python
# Cache legal moves
config.cache_legal_moves = True

# Use smaller models for testing
test_config = LLMConfig(
    model="gpt-3.5-turbo"  # Faster than GPT-4
)
```

2. **Enable parallel processing:**

```python
# For tournaments
tournament_config.parallel_games = 4
```

3. **Set timeouts:**

```python
config.move_timeout = 30  # 30 seconds per move
config.game_timeout = 3600  # 1 hour per game
```

### 5. Memory Issues

#### Problem: `MemoryError` during long games

**Solution:**
Limit game history:

```python
config.max_history_length = 100  # Keep only last 100 moves
config.compress_old_states = True  # Compress older states
```

### 6. Tournament Issues

#### Problem: Tournament hanging on specific game

**Solution:**
Add error handling and timeouts:

```python
tournament_config = TournamentConfig(
    game_timeout=1800,  # 30 minutes per game
    skip_on_error=True,  # Skip failed games
    retry_failed=False   # Don't retry to avoid hanging
)
```

#### Problem: Results not saving

**Solution:**
Check directory permissions:

```bash
# Create results directory with correct permissions
mkdir -p tournament_results
chmod 755 tournament_results

# Use absolute path
config.output_dir = "/absolute/path/to/results"
```

### 7. Debugging Tips

#### Enable Debug Logging

```python
import logging

# Set logging level
logging.basicConfig(level=logging.DEBUG)

# Or for specific game
logging.getLogger("haive.games.chess").setLevel(logging.DEBUG)
```

#### Inspect Game State

```python
# Print state at each step
for state in agent.app.stream(initial_state):
    print(f"Turn {state.get('turn_number')}:")
    print(f"State: {state}")
    agent.visualize_state(state)
```

#### Test with Mock LLMs

```python
from haive.testing import MockLLMConfig

# Use deterministic mock for testing
mock_config = MockLLMConfig(
    responses=["e2e4", "Nf3", "Bc4", "O-O"]  # Predefined moves
)

test_agent = ChessAgent(ChessConfig(
    aug_llm_configs={"white": mock_config, "black": mock_config}
))
```

### 8. State Validation Issues

#### Problem: `ValidationError: Invalid state`

**Solution:**
Enable state repair:

```python
config.auto_repair_states = True
config.strict_validation = False  # For testing only
```

### 9. Platform-Specific Issues

#### Windows: Path issues

```python
# Use pathlib for cross-platform paths
from pathlib import Path

game_dir = Path(__file__).parent / "games"
```

#### Linux: Permission denied

```bash
# Fix permissions
chmod +x tournament_tools/scripts/*.py
```

#### macOS: SSL certificate issues

```bash
# Install certificates
pip install --upgrade certifi
```

## Getting Help

### 1. Check Logs

```bash
# View game logs
tail -f game_logs/chess_*.log

# Search for errors
grep -r "ERROR" game_logs/
```

### 2. Run Diagnostics

```python
from haive.games.diagnostics import run_diagnostics

# Check all games
results = run_diagnostics()
print(results.summary())

# Check specific game
chess_diag = run_diagnostics(game="chess")
print(chess_diag.issues)
```

### 3. Minimal Reproduction

Create a minimal example:

```python
# minimal_test.py
from haive.games.tic_tac_toe import TicTacToeAgent, TicTacToeConfig

config = TicTacToeConfig()  # Use defaults
agent = TicTacToeAgent(config)

try:
    state = agent.get_initial_state()
    print("Success!")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
```

### 4. Community Support

- GitHub Issues: File detailed bug reports
- Include: Python version, OS, full error traceback
- Provide: Minimal reproduction code

## Prevention Tips

1. **Keep dependencies updated:**

   ```bash
   poetry update
   ```

2. **Run tests before tournaments:**

   ```bash
   poetry run pytest tests/
   ```

3. **Use configuration validation:**

   ```python
   config.validate()  # Checks all settings
   ```

4. **Monitor resource usage:**

   ```python
   import psutil

   # Check before running games
   if psutil.virtual_memory().percent > 90:
       print("Warning: Low memory!")
   ```
