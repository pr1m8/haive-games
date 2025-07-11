# Nim Game Module

A comprehensive implementation of the mathematical strategy game Nim with advanced AI analysis, perfect play algorithms, and multi-variant support using the Haive framework.

## Table of Contents

1. [Overview](#overview)
2. [Mathematical Foundations](#mathematical-foundations)
3. [Game Theory and Strategy](#game-theory-and-strategy)
4. [Installation](#installation)
5. [Quick Start](#quick-start)
6. [API Reference](#api-reference)
7. [Game Variants](#game-variants)
8. [Strategic Analysis](#strategic-analysis)
9. [Examples](#examples)
10. [Performance Considerations](#performance-considerations)
11. [Testing](#testing)
12. [Advanced Usage](#advanced-usage)
13. [Contributing](#contributing)
14. [Version History](#version-history)

## Overview

Nim is a mathematical strategy game of perfect information where two players take turns removing objects from distinct piles. The game has profound mathematical properties that make it a cornerstone of combinatorial game theory and an excellent testbed for AI algorithms.

### Key Features

- **Perfect Play Algorithm**: Implementation of optimal strategy using nim-sum calculations
- **Multi-Variant Support**: Standard, Misère, Fibonacci, Kayles, and Subtraction variants
- **Advanced AI Analysis**: LLM-based strategic reasoning with mathematical proofs
- **Rich Terminal UI**: Beautiful visualization with Real-time analysis display
- **Performance Optimized**: Efficient algorithms for large pile configurations
- **Educational Tools**: Comprehensive explanations of game theory concepts
- **Tournament Ready**: Full game state management and replay capabilities

### Mathematical Significance

Nim is fundamental to understanding:

- **Sprague-Grundy Theorem**: Universal framework for impartial games
- **Nimber Theory**: Algebraic structure of game positions
- **Combinatorial Game Theory**: Foundation for analyzing perfect information games
- **Optimal Strategy**: Algorithmic approach to perfect play

## Mathematical Foundations

### The Nim-Sum

The nim-sum is the binary XOR (exclusive OR) of all pile sizes, which forms the mathematical foundation of optimal Nim play:

```
nim_sum = pile_1 ⊕ pile_2 ⊕ ... ⊕ pile_n
```

**Example**: For piles [3, 5, 7]:

```
3 = 011₂
5 = 101₂
7 = 111₂
─────────
XOR = 001₂ = 1
```

### Sprague-Grundy Theorem

The Sprague-Grundy theorem provides the theoretical foundation for Nim analysis:

1. **Cold Positions (P-positions)**: Nim-sum = 0, losing for the current player
2. **Hot Positions (N-positions)**: Nim-sum ≠ 0, winning for the current player

**Theorem**: A position is a P-position if and only if its nim-sum is 0.

### Optimal Play Strategy

The optimal strategy follows these principles:

1. **If nim-sum = 0**: Any move gives opponent a winning position
2. **If nim-sum ≠ 0**: Find a move that makes nim-sum = 0
3. **Winning Move Calculation**: For pile i, take `pile_i - (pile_i ⊕ nim_sum)` stones

## Game Theory and Strategy

### Position Classification

```python
def classify_position(piles: List[int]) -> str:
    """Classify position using game theory principles."""
    nim_sum = functools.reduce(operator.xor, piles)

    if nim_sum == 0:
        return "P-position (Previous player wins)"
    else:
        return "N-position (Next player wins)"
```

### Strategic Principles

1. **Maintain Cold Positions**: Always leave opponent with nim-sum = 0
2. **Symmetric Play**: Create mirror positions when possible
3. **Endgame Analysis**: Special considerations for small pile configurations
4. **Bluffing Defense**: Optimal play against suboptimal opponents

### Complexity Analysis

- **State Space**: O(∏pile_i) possible positions
- **Move Generation**: O(∑pile_i) possible moves
- **Optimal Move**: O(n) calculation time where n = number of piles
- **Game Tree Depth**: O(∑pile_i) maximum game length

## Installation

```bash
# Install with poetry (recommended)
poetry install --extras haive-games

# Or install with pip
pip install haive-games

# Install with development dependencies
poetry install --extras "haive-games dev"
```

### Dependencies

- **Core Requirements**:
  - Python 3.8+
  - Pydantic >= 2.0
  - Haive Framework
  - LangGraph

- **Optional Dependencies**:
  - Rich (for terminal UI)
  - Matplotlib (for position visualization)
  - Jupyter (for interactive analysis)

## Quick Start

### Basic Game

```python
from haive.games.nim import NimAgent, NimConfig

# Create and run a basic game
agent = NimAgent()
result = agent.run_game(visualize=True)
```

### With Rich UI

```python
from haive.games.nim import NimAgent, NimConfig

# Configure game with Rich UI
config = NimConfig(
    pile_sizes=[3, 5, 7],
    misere_mode=False,
    enable_analysis=True,
    visualize=True
)

agent = NimAgent(config=config)
agent.run_game_with_ui(show_analysis=True)
```

### Strategic Analysis

```python
from haive.games.nim import NimStateManager, NimAnalysis

# Analyze a position
manager = NimStateManager()
manager.initialize_game([4, 6, 8])

# Get optimal move
analysis = manager.analyze_position()
print(f"Nim-sum: {analysis.nim_sum}")
print(f"Position: {analysis.position_evaluation}")
print(f"Strategy: {analysis.winning_strategy}")
```

## API Reference

### Core Classes

#### NimAgent

The main agent class for running Nim games with AI analysis.

```python
class NimAgent(Agent[NimState]):
    """Advanced Nim game agent with strategic analysis."""

    def __init__(self, config: NimConfig = None):
        """Initialize Nim agent with configuration."""

    def run_game(self, visualize: bool = False) -> Dict[str, Any]:
        """Run a complete Nim game."""

    def run_game_with_ui(self, show_analysis: bool = True) -> Dict[str, Any]:
        """Run game with Rich terminal UI."""

    def analyze_position(self, piles: List[int]) -> NimAnalysis:
        """Analyze current position for optimal play."""
```

#### NimStateManager

Manages game state and rule enforcement.

```python
class NimStateManager:
    """Comprehensive Nim game state management."""

    def initialize_game(self, pile_sizes: List[int]) -> None:
        """Initialize game with specified pile sizes."""

    def make_move(self, move: NimMove) -> bool:
        """Apply move and update game state."""

    def get_legal_moves(self) -> List[NimMove]:
        """Generate all legal moves from current position."""

    def is_game_over(self) -> bool:
        """Check if game has ended."""

    def get_winner(self) -> Optional[str]:
        """Get winner if game is over."""

    def calculate_nim_sum(self) -> int:
        """Calculate nim-sum of current position."""

    def find_optimal_move(self) -> NimMove:
        """Find mathematically optimal move."""
```

#### NimMove

Represents a move in the game with strategic context.

```python
class NimMove(BaseModel):
    """Comprehensive move representation."""

    pile_index: int                    # Pile to take from (0-based)
    stones_taken: int                  # Number of stones to take
    player: str                        # Player making the move
    reasoning: Optional[str]           # Strategic reasoning
    move_quality: Optional[str]        # Quality assessment
    alternative_moves: List[Dict]      # Other moves considered
    time_taken: Optional[float]        # Time to make move

    @property
    def move_notation(self) -> str:
        """Algebraic notation (e.g., 'P0-3')."""

    @property
    def has_strategic_context(self) -> bool:
        """Check if move includes analysis."""
```

#### NimAnalysis

Advanced position analysis with mathematical proofs.

```python
class NimAnalysis(BaseModel):
    """Comprehensive position analysis."""

    nim_sum: int                       # XOR of all pile sizes
    position_evaluation: str           # winning/losing/drawn/complex
    recommended_move: NimMove          # Optimal move
    explanation: str                   # Detailed explanation
    winning_strategy: str              # High-level strategy
    mathematical_proof: Optional[str]  # Formal proof
    alternative_moves: List[NimMove]   # Other strong moves
    position_complexity: PositionType  # Complexity classification
    variant_considerations: Optional[str] # Variant-specific notes

    @property
    def is_winning_position(self) -> bool:
        """True if position is winning."""

    @property
    def analysis_confidence(self) -> str:
        """Confidence level of analysis."""

    @property
    def strategic_summary(self) -> Dict:
        """Concise strategic summary."""
```

#### NimConfig

Configuration for game setup and AI behavior.

```python
class NimConfig(BaseModel):
    """Comprehensive game configuration."""

    pile_sizes: List[int] = [3, 5, 7]  # Initial pile sizes
    misere_mode: bool = False          # Misère variant
    enable_analysis: bool = True       # Strategic analysis
    visualize: bool = False            # Visual feedback
    max_moves: int = 1000             # Move limit
    time_limit: Optional[float] = None # Time limit
    difficulty_level: str = "expert"   # AI difficulty
    variant: NimVariant = NimVariant.STANDARD # Game variant

    @field_validator("pile_sizes")
    def validate_pile_sizes(cls, v):
        """Validate pile configuration."""

    @field_validator("difficulty_level")
    def validate_difficulty(cls, v):
        """Validate difficulty setting."""
```

## Game Variants

### Standard Nim

Classic Nim where the last player to move wins.

```python
config = NimConfig(
    pile_sizes=[3, 5, 7],
    misere_mode=False,
    variant=NimVariant.STANDARD
)
```

### Misère Nim

Variant where the last player to move loses.

```python
config = NimConfig(
    pile_sizes=[3, 5, 7],
    misere_mode=True,
    variant=NimVariant.MISERE
)
```

**Strategic Differences**:

- Standard strategy applies until all piles have size ≤ 1
- In endgame, leave opponent with odd number of piles

### Fibonacci Nim

Players can only take 1 or 2 stones per turn.

```python
config = NimConfig(
    pile_sizes=[8, 13, 21],
    variant=NimVariant.FIBONACCI
)
```

### Kayles

Variant where players can split piles.

```python
config = NimConfig(
    pile_sizes=[10, 15, 20],
    variant=NimVariant.KAYLES
)
```

### Subtraction Game

Players can only take from a predefined set of numbers.

```python
config = NimConfig(
    pile_sizes=[12, 18, 24],
    variant=NimVariant.SUBTRACTION,
    allowed_moves=[1, 2, 3, 5]  # Can only take 1, 2, 3, or 5 stones
)
```

## Strategic Analysis

### Position Evaluation

```python
def evaluate_position(piles: List[int], misere: bool = False) -> Dict[str, Any]:
    """Comprehensive position evaluation."""

    nim_sum = functools.reduce(operator.xor, piles)
    total_stones = sum(piles)
    non_empty_piles = len([p for p in piles if p > 0])

    if not misere:
        # Standard Nim analysis
        if nim_sum == 0:
            return {
                "evaluation": "losing",
                "strategy": "Any move gives opponent advantage",
                "theorem": "P-position by Sprague-Grundy"
            }
        else:
            optimal_move = find_optimal_move(piles, nim_sum)
            return {
                "evaluation": "winning",
                "strategy": f"Take {optimal_move.stones_taken} from pile {optimal_move.pile_index}",
                "theorem": "N-position by Sprague-Grundy"
            }
    else:
        # Misère Nim analysis
        if all(p <= 1 for p in piles):
            # Endgame: count piles
            if non_empty_piles % 2 == 1:
                return {"evaluation": "losing", "strategy": "Odd number of piles in endgame"}
            else:
                return {"evaluation": "winning", "strategy": "Even number of piles in endgame"}
        else:
            # Use standard strategy until endgame
            return evaluate_position(piles, misere=False)
```

### Optimal Move Calculation

```python
def find_optimal_move(piles: List[int]) -> NimMove:
    """Find mathematically optimal move."""

    nim_sum = functools.reduce(operator.xor, piles)

    if nim_sum == 0:
        # No winning move exists - return best try
        return find_best_defensive_move(piles)

    # Find pile that can be reduced to make nim-sum = 0
    for i, pile_size in enumerate(piles):
        target_size = pile_size ^ nim_sum
        if target_size < pile_size:
            stones_to_take = pile_size - target_size
            return NimMove(
                pile_index=i,
                stones_taken=stones_to_take,
                player="AI",
                reasoning=f"Reduce pile {i} from {pile_size} to {target_size} to make nim-sum = 0",
                move_quality="optimal"
            )

    # Should never reach here in valid position
    raise ValueError("No optimal move found - invalid position")
```

### Game Tree Analysis

```python
def analyze_game_tree(piles: List[int], depth: int = 10) -> Dict[str, Any]:
    """Analyze game tree to given depth."""

    def minimax(position: List[int], depth: int, maximizing: bool) -> Tuple[int, List[int]]:
        """Minimax algorithm with alpha-beta pruning."""

        if depth == 0 or sum(position) == 0:
            nim_sum = functools.reduce(operator.xor, position)
            return (1 if nim_sum != 0 else -1), position

        if maximizing:
            max_eval = float('-inf')
            best_move = None

            for move in generate_moves(position):
                new_position = apply_move(position, move)
                eval_score, _ = minimax(new_position, depth - 1, False)

                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move

            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None

            for move in generate_moves(position):
                new_position = apply_move(position, move)
                eval_score, _ = minimax(new_position, depth - 1, True)

                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = move

            return min_eval, best_move

    return minimax(piles, depth, True)
```

## Examples

### Example 1: Basic Game Setup

```python
from haive.games.nim import NimAgent, NimConfig

# Simple game with visualization
agent = NimAgent(
    config=NimConfig(
        pile_sizes=[3, 5, 7],
        visualize=True
    )
)

# Run the game
result = agent.run_game()
print(f"Winner: {result['winner']}")
print(f"Moves: {result['move_count']}")
```

### Example 2: Strategic Analysis

```python
from haive.games.nim import NimStateManager, NimAnalysis

# Analyze specific position
manager = NimStateManager()
manager.initialize_game([4, 6, 8])

# Get comprehensive analysis
analysis = manager.analyze_position()

print(f"Nim-sum: {analysis.nim_sum}")
print(f"Position: {analysis.position_evaluation}")
print(f"Recommended move: {analysis.recommended_move}")
print(f"Strategy: {analysis.winning_strategy}")

if analysis.mathematical_proof:
    print(f"Proof: {analysis.mathematical_proof}")
```

### Example 3: Misère Nim Tournament

```python
from haive.games.nim import NimAgent, NimConfig, NimVariant

# Tournament configuration
configs = [
    NimConfig(pile_sizes=[3, 5, 7], misere_mode=True),
    NimConfig(pile_sizes=[4, 6, 8], misere_mode=True),
    NimConfig(pile_sizes=[2, 4, 6, 8], misere_mode=True)
]

results = []
for i, config in enumerate(configs):
    agent = NimAgent(config=config)
    result = agent.run_game()
    results.append({
        'game': i + 1,
        'winner': result['winner'],
        'moves': result['move_count'],
        'final_position': result['final_state']
    })

# Analyze tournament results
for result in results:
    print(f"Game {result['game']}: {result['winner']} won in {result['moves']} moves")
```

### Example 4: Custom AI vs Human

```python
from haive.games.nim import NimAgent, NimConfig
from haive.games.nim.ui import NimUI

# Human vs AI setup
config = NimConfig(
    pile_sizes=[5, 7, 9],
    enable_analysis=True,
    visualize=True
)

agent = NimAgent(config=config)

# Interactive game with analysis
agent.run_game_with_ui(
    show_analysis=True,
    human_player=True
)
```

### Example 5: Batch Position Analysis

```python
from haive.games.nim import NimStateManager
import itertools

# Analyze multiple positions
positions = [
    [1, 2, 3],
    [4, 5, 6],
    [3, 3, 3],
    [7, 7, 7],
    [1, 1, 1, 1]
]

manager = NimStateManager()
analyses = []

for piles in positions:
    manager.initialize_game(piles)
    analysis = manager.analyze_position()
    analyses.append({
        'position': piles,
        'nim_sum': analysis.nim_sum,
        'evaluation': analysis.position_evaluation,
        'complexity': analysis.position_complexity,
        'optimal_move': str(analysis.recommended_move)
    })

# Summary report
for analysis in analyses:
    print(f"Position {analysis['position']}: {analysis['evaluation']} (nim-sum: {analysis['nim_sum']})")
    print(f"  Complexity: {analysis['complexity']}")
    print(f"  Optimal move: {analysis['optimal_move']}")
    print()
```

### Example 6: Performance Benchmarking

```python
from haive.games.nim import NimStateManager
import time
import random

def benchmark_analysis(max_piles: int = 10, max_size: int = 100, trials: int = 1000):
    """Benchmark position analysis performance."""

    manager = NimStateManager()
    times = []

    for _ in range(trials):
        # Generate random position
        num_piles = random.randint(2, max_piles)
        piles = [random.randint(1, max_size) for _ in range(num_piles)]

        # Time analysis
        start_time = time.time()
        manager.initialize_game(piles)
        analysis = manager.analyze_position()
        end_time = time.time()

        times.append(end_time - start_time)

    return {
        'mean_time': sum(times) / len(times),
        'max_time': max(times),
        'min_time': min(times),
        'total_time': sum(times)
    }

# Run benchmark
results = benchmark_analysis()
print(f"Average analysis time: {results['mean_time']:.4f} seconds")
print(f"Max analysis time: {results['max_time']:.4f} seconds")
print(f"Min analysis time: {results['min_time']:.4f} seconds")
```

### Example 7: Educational Game Theory Demo

```python
from haive.games.nim import NimStateManager, NimAnalysis
from haive.games.nim.ui import NimUI

def educational_demo():
    """Demonstrate game theory concepts."""

    print("=== NIM GAME THEORY DEMONSTRATION ===\n")

    # Cold position (P-position)
    print("1. Cold Position (P-position - Losing):")
    manager = NimStateManager()
    manager.initialize_game([3, 5, 6])  # nim-sum = 0
    analysis = manager.analyze_position()

    print(f"   Piles: {manager.state.piles}")
    print(f"   Nim-sum: {analysis.nim_sum}")
    print(f"   Evaluation: {analysis.position_evaluation}")
    print(f"   Explanation: {analysis.explanation}")
    print()

    # Hot position (N-position)
    print("2. Hot Position (N-position - Winning):")
    manager.initialize_game([3, 5, 7])  # nim-sum = 1
    analysis = manager.analyze_position()

    print(f"   Piles: {manager.state.piles}")
    print(f"   Nim-sum: {analysis.nim_sum}")
    print(f"   Evaluation: {analysis.position_evaluation}")
    print(f"   Optimal move: {analysis.recommended_move}")
    print(f"   Strategy: {analysis.winning_strategy}")
    print()

    # Demonstrate nim-sum calculation
    print("3. Nim-sum Calculation:")
    piles = [3, 5, 7]
    print(f"   Piles: {piles}")
    print(f"   Binary: {[bin(p) for p in piles]}")
    print(f"   XOR calculation: {piles[0]} ⊕ {piles[1]} ⊕ {piles[2]} = {piles[0] ^ piles[1] ^ piles[2]}")
    print()

    # Misère endgame
    print("4. Misère Endgame:")
    manager.initialize_game([1, 1, 1])
    config = manager.config
    config.misere_mode = True
    analysis = manager.analyze_position()

    print(f"   Piles: {manager.state.piles}")
    print(f"   Mode: Misère")
    print(f"   Evaluation: {analysis.position_evaluation}")
    print(f"   Strategy: {analysis.winning_strategy}")

# Run educational demo
educational_demo()
```

### Example 8: Advanced AI Configuration

```python
from haive.games.nim import NimAgent, NimConfig
from haive.games.nim.engines import create_expert_engine

# Configure expert-level AI
config = NimConfig(
    pile_sizes=[10, 15, 20],
    enable_analysis=True,
    difficulty_level="expert",
    analysis_depth=15,
    time_limit=30.0
)

# Create agent with custom engine
expert_engine = create_expert_engine(
    model_name="gpt-4",
    temperature=0.1,
    max_tokens=2000
)

agent = NimAgent(
    config=config,
    engine=expert_engine
)

# Run high-level game
result = agent.run_game(
    visualize=True,
    detailed_analysis=True
)

print(f"Expert game completed:")
print(f"Winner: {result['winner']}")
print(f"Total moves: {result['move_count']}")
print(f"Average analysis time: {result['avg_analysis_time']:.2f}s")
print(f"Strategic accuracy: {result['strategic_accuracy']:.1%}")
```

## Performance Considerations

### Algorithmic Complexity

- **Nim-sum calculation**: O(n) where n = number of piles
- **Optimal move finding**: O(n) for standard Nim
- **Position analysis**: O(n) for most cases, O(n²) for complex variants
- **Game tree search**: O(b^d) where b = branching factor, d = depth

### Memory Usage

- **State representation**: O(n) for n piles
- **Move history**: O(m) for m moves
- **Analysis cache**: O(k) for k analyzed positions

### Optimization Strategies

1. **Memoization**: Cache analysis results for repeated positions
2. **Early termination**: Stop analysis when optimal move is found
3. **Pruning**: Use alpha-beta pruning for game tree search
4. **Bit operations**: Use bitwise XOR for nim-sum calculations

### Scalability

```python
# Efficient implementation for large pile counts
def efficient_nim_sum(piles: List[int]) -> int:
    """Compute nim-sum efficiently using reduce."""
    return functools.reduce(operator.xor, piles, 0)

# Optimized move generation
def generate_moves_optimized(piles: List[int]) -> Iterator[NimMove]:
    """Generate moves efficiently using iterators."""
    for pile_index, pile_size in enumerate(piles):
        if pile_size > 0:
            for stones in range(1, pile_size + 1):
                yield NimMove(
                    pile_index=pile_index,
                    stones_taken=stones,
                    player="AI"
                )
```

## Testing

### Unit Tests

```bash
# Run all Nim tests
poetry run pytest packages/haive-games/tests/test_nim/ -v

# Run specific test categories
poetry run pytest packages/haive-games/tests/test_nim/test_models.py -v
poetry run pytest packages/haive-games/tests/test_nim/test_state_manager.py -v
poetry run pytest packages/haive-games/tests/test_nim/test_analysis.py -v

# Run with coverage
poetry run pytest packages/haive-games/tests/test_nim/ --cov=haive.games.nim --cov-report=html
```

### Integration Tests

```bash
# Test complete game flows
poetry run pytest packages/haive-games/tests/test_nim/test_integration.py -v

# Test UI components
poetry run pytest packages/haive-games/tests/test_nim/test_ui.py -v
```

### Performance Tests

```bash
# Run performance benchmarks
poetry run pytest packages/haive-games/tests/test_nim/test_performance.py -v

# Profile memory usage
poetry run pytest packages/haive-games/tests/test_nim/test_memory.py -v
```

### Standalone Testing

```bash
# Run without full framework
python packages/haive-games/src/haive/games/nim/standalone_game.py --test

# Manual testing script
python packages/haive-games/src/haive/games/nim/example.py --pile-sizes 3 5 7 --misere
```

## Advanced Usage

### Custom Analysis Engines

```python
from haive.games.nim.engines import BaseAnalysisEngine

class CustomAnalysisEngine(BaseAnalysisEngine):
    """Custom analysis engine with specialized algorithms."""

    def analyze_position(self, piles: List[int]) -> NimAnalysis:
        """Custom analysis implementation."""

        # Implement custom analysis logic
        nim_sum = self.calculate_nim_sum(piles)

        # Custom strategic evaluation
        if nim_sum == 0:
            return self.create_defensive_analysis(piles)
        else:
            return self.create_offensive_analysis(piles, nim_sum)

    def create_offensive_analysis(self, piles: List[int], nim_sum: int) -> NimAnalysis:
        """Create analysis for winning positions."""

        optimal_move = self.find_optimal_move(piles, nim_sum)

        return NimAnalysis(
            nim_sum=nim_sum,
            position_evaluation="winning",
            recommended_move=optimal_move,
            explanation=f"Position has nim-sum {nim_sum}, indicating a winning position",
            winning_strategy="Force opponent into cold position (nim-sum = 0)",
            mathematical_proof="By Sprague-Grundy theorem, nim-sum ≠ 0 is N-position"
        )
```

### Tournament System

```python
from haive.games.nim import NimAgent, NimConfig
from typing import List, Dict, Any

class NimTournament:
    """Tournament system for Nim competitions."""

    def __init__(self, configurations: List[NimConfig]):
        self.configurations = configurations
        self.results = []

    def run_tournament(self, rounds: int = 10) -> Dict[str, Any]:
        """Run complete tournament."""

        for round_num in range(rounds):
            for config in self.configurations:
                agent = NimAgent(config=config)
                result = agent.run_game()

                self.results.append({
                    'round': round_num + 1,
                    'config': config,
                    'result': result
                })

        return self.analyze_results()

    def analyze_results(self) -> Dict[str, Any]:
        """Analyze tournament results."""

        # Statistical analysis
        total_games = len(self.results)
        win_rates = {}
        avg_moves = {}

        # Calculate metrics
        for result in self.results:
            config_key = str(result['config'])
            if config_key not in win_rates:
                win_rates[config_key] = []
                avg_moves[config_key] = []

            win_rates[config_key].append(result['result']['winner'] == 'AI')
            avg_moves[config_key].append(result['result']['move_count'])

        return {
            'total_games': total_games,
            'configurations': len(self.configurations),
            'win_rates': {k: sum(v) / len(v) for k, v in win_rates.items()},
            'avg_moves': {k: sum(v) / len(v) for k, v in avg_moves.items()}
        }
```

### Machine Learning Integration

```python
from haive.games.nim import NimStateManager, NimAnalysis
import numpy as np
from sklearn.ensemble import RandomForestRegressor

class NimMLAnalyzer:
    """Machine learning-based Nim analyzer."""

    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100)
        self.trained = False

    def generate_training_data(self, num_samples: int = 10000) -> tuple:
        """Generate training data from known positions."""

        X = []  # Features: pile sizes, nim-sum, etc.
        y = []  # Labels: position evaluation scores

        manager = NimStateManager()

        for _ in range(num_samples):
            # Generate random position
            piles = [random.randint(1, 20) for _ in range(random.randint(2, 6))]
            manager.initialize_game(piles)

            # Extract features
            features = self.extract_features(piles)

            # Get ground truth analysis
            analysis = manager.analyze_position()
            score = 1 if analysis.is_winning_position else -1

            X.append(features)
            y.append(score)

        return np.array(X), np.array(y)

    def extract_features(self, piles: List[int]) -> List[float]:
        """Extract features from position."""

        features = []

        # Basic features
        features.extend(piles + [0] * (10 - len(piles)))  # Pad to fixed length
        features.append(sum(piles))  # Total stones
        features.append(len(piles))  # Number of piles
        features.append(max(piles))  # Largest pile
        features.append(min(piles))  # Smallest pile
        features.append(functools.reduce(operator.xor, piles))  # Nim-sum

        # Advanced features
        features.append(sum(1 for p in piles if p == 1))  # Single stone piles
        features.append(sum(1 for p in piles if p > 1))   # Multi-stone piles
        features.append(np.var(piles))  # Pile variance

        return features

    def train(self, X: np.ndarray, y: np.ndarray) -> None:
        """Train the ML model."""

        self.model.fit(X, y)
        self.trained = True

    def predict(self, piles: List[int]) -> float:
        """Predict position evaluation."""

        if not self.trained:
            raise ValueError("Model not trained")

        features = np.array([self.extract_features(piles)])
        return self.model.predict(features)[0]
```

## Educational Value and Game Theory Applications

### Teaching Mathematical Concepts

Nim serves as an excellent pedagogical tool for introducing fundamental mathematical concepts:

#### Binary Arithmetic and XOR Operations

```python
def demonstrate_binary_xor():
    """Educational demonstration of XOR in Nim."""

    piles = [3, 5, 7]
    print("Understanding XOR in Nim:")
    print(f"Piles: {piles}")

    # Show binary representation
    for i, pile in enumerate(piles):
        print(f"Pile {i}: {pile} = {bin(pile)[2:].zfill(4)}")

    # Calculate XOR step by step
    print("\nXOR Calculation:")
    print(f"Step 1: {piles[0]} ⊕ {piles[1]} = {piles[0] ^ piles[1]}")
    print(f"Binary: {bin(piles[0])[2:].zfill(4)} ⊕ {bin(piles[1])[2:].zfill(4)} = {bin(piles[0] ^ piles[1])[2:].zfill(4)}")

    intermediate = piles[0] ^ piles[1]
    print(f"Step 2: {intermediate} ⊕ {piles[2]} = {intermediate ^ piles[2]}")
    print(f"Binary: {bin(intermediate)[2:].zfill(4)} ⊕ {bin(piles[2])[2:].zfill(4)} = {bin(intermediate ^ piles[2])[2:].zfill(4)}")

    nim_sum = intermediate ^ piles[2]
    print(f"\nFinal nim-sum: {nim_sum}")
    print(f"Position is {'winning' if nim_sum != 0 else 'losing'}")
```

#### Combinatorial Game Theory Fundamentals

```python
def demonstrate_game_theory_principles():
    """Demonstrate core game theory principles through Nim."""

    print("Game Theory in Nim:")
    print("1. Perfect Information: All game state is visible to both players")
    print("2. Deterministic: No randomness in game mechanics")
    print("3. Zero-sum: One player's gain equals other's loss")
    print("4. Finite: Game always terminates")
    print("5. Impartial: Same moves available to both players")

    # Demonstrate position values
    positions = [
        ([1, 2, 3], "P-position"),
        ([1, 2, 4], "N-position"),
        ([5, 5, 5], "P-position"),
        ([7, 7, 7], "P-position")
    ]

    print("\nPosition Classification Examples:")
    for piles, classification in positions:
        nim_sum = functools.reduce(operator.xor, piles)
        print(f"  {piles}: nim-sum = {nim_sum}, {classification}")

        # Explain why
        if nim_sum == 0:
            print(f"    → P-position: Previous player (who just moved) is in winning position")
        else:
            print(f"    → N-position: Next player (about to move) is in winning position")
```

#### Algorithmic Thinking and Strategy

```python
def demonstrate_strategic_thinking():
    """Show how to think strategically about Nim positions."""

    print("Strategic Analysis Framework:")
    print("1. Calculate nim-sum of current position")
    print("2. Determine position type (P or N)")
    print("3. If N-position, find move that creates P-position")
    print("4. If P-position, minimize opponent's advantage")

    # Example strategic analysis
    position = [4, 6, 8]
    nim_sum = functools.reduce(operator.xor, position)

    print(f"\nExample Analysis: {position}")
    print(f"Nim-sum: {nim_sum}")

    if nim_sum != 0:
        print("This is an N-position (winning)")
        print("Winning moves:")

        for pile_idx, pile_size in enumerate(position):
            target_size = pile_size ^ nim_sum
            if target_size < pile_size:
                stones_to_take = pile_size - target_size
                new_position = position.copy()
                new_position[pile_idx] = target_size
                new_nim_sum = functools.reduce(operator.xor, new_position)

                print(f"  Take {stones_to_take} from pile {pile_idx}:")
                print(f"    {position} → {new_position}")
                print(f"    Nim-sum: {nim_sum} → {new_nim_sum}")
                print(f"    Opponent now faces P-position")
```

### Advanced Mathematical Concepts

#### Sprague-Grundy Theory

```python
def demonstrate_sprague_grundy():
    """Demonstrate Sprague-Grundy theorem applications."""

    print("Sprague-Grundy Theorem in Nim:")
    print("- Every impartial game position has a Grundy number")
    print("- Grundy number of 0 indicates losing position")
    print("- Grundy number > 0 indicates winning position")
    print("- For Nim, Grundy number equals nim-sum")

    # Show Grundy numbers for various positions
    test_positions = [
        [0, 0, 0],      # All empty
        [1, 0, 0],      # Single stone
        [1, 1, 0],      # Two single stones
        [2, 1, 0],      # Mixed
        [3, 5, 7],      # Classic
    ]

    print("\nGrundy Numbers for Nim Positions:")
    for piles in test_positions:
        grundy = functools.reduce(operator.xor, piles)
        evaluation = "Losing (P)" if grundy == 0 else "Winning (N)"
        print(f"  {piles}: G = {grundy} ({evaluation})")
```

#### Nim-Sum Properties and Theorems

```python
def demonstrate_nim_sum_properties():
    """Demonstrate mathematical properties of nim-sum."""

    print("Nim-Sum Mathematical Properties:")
    print("1. Associativity: (a ⊕ b) ⊕ c = a ⊕ (b ⊕ c)")
    print("2. Commutativity: a ⊕ b = b ⊕ a")
    print("3. Identity: a ⊕ 0 = a")
    print("4. Self-inverse: a ⊕ a = 0")
    print("5. Distributivity over addition: a ⊕ (b + c) ≠ (a ⊕ b) + (a ⊕ c)")

    # Demonstrate properties with examples
    a, b, c = 5, 3, 7

    print(f"\nExamples with a={a}, b={b}, c={c}:")
    print(f"Associativity: ({a} ⊕ {b}) ⊕ {c} = {(a ^ b) ^ c}, {a} ⊕ ({b} ⊕ {c}) = {a ^ (b ^ c)}")
    print(f"Commutativity: {a} ⊕ {b} = {a ^ b}, {b} ⊕ {a} = {b ^ a}")
    print(f"Identity: {a} ⊕ 0 = {a ^ 0}")
    print(f"Self-inverse: {a} ⊕ {a} = {a ^ a}")

    # Show why nim-sum works for move calculation
    print(f"\nMove Calculation Using Properties:")
    position = [a, b, c]
    nim_sum = functools.reduce(operator.xor, position)
    print(f"Position: {position}, nim-sum: {nim_sum}")

    if nim_sum != 0:
        # Find optimal move using self-inverse property
        for i, pile in enumerate(position):
            target = pile ^ nim_sum
            if target < pile:
                print(f"Optimal move: reduce pile {i} from {pile} to {target}")
                print(f"Calculation: {pile} ⊕ {nim_sum} = {target}")
                print(f"Why it works: new nim-sum = {target} ⊕ {b} ⊕ {c} = {target ^ b ^ c}")
                print(f"This equals: ({pile} ⊕ {nim_sum}) ⊕ {b} ⊕ {c} = {pile} ⊕ ({nim_sum} ⊕ {b} ⊕ {c}) = {pile} ⊕ {pile} = 0")
                break
```

### Computational Complexity and Optimization

#### Algorithmic Efficiency Analysis

```python
def analyze_computational_complexity():
    """Analyze the computational complexity of Nim algorithms."""

    print("Computational Complexity Analysis:")

    # Time complexity
    print("\nTime Complexity:")
    print("- Nim-sum calculation: O(n) where n = number of piles")
    print("- Optimal move finding: O(n) for each pile check")
    print("- Legal move generation: O(∑pile_sizes)")
    print("- Game tree evaluation: O(b^d) where b = branching factor, d = depth")

    # Space complexity
    print("\nSpace Complexity:")
    print("- Position storage: O(n) for n piles")
    print("- Move history: O(m) for m moves")
    print("- Game tree: O(b^d) in worst case")

    # Optimization strategies
    print("\nOptimization Strategies:")
    print("1. Bit manipulation for faster XOR operations")
    print("2. Memoization for repeated position analysis")
    print("3. Alpha-beta pruning for game tree search")
    print("4. Iterative deepening for controlled search depth")

    # Demonstrate optimized nim-sum calculation
    import time

    def optimized_nim_sum(piles):
        """Optimized nim-sum using reduce."""
        return functools.reduce(operator.xor, piles, 0)

    def naive_nim_sum(piles):
        """Naive nim-sum calculation."""
        result = 0
        for pile in piles:
            result ^= pile
        return result

    # Benchmark different implementations
    large_position = [random.randint(1, 1000) for _ in range(1000)]

    # Time optimized version
    start = time.time()
    for _ in range(1000):
        optimized_nim_sum(large_position)
    optimized_time = time.time() - start

    # Time naive version
    start = time.time()
    for _ in range(1000):
        naive_nim_sum(large_position)
    naive_time = time.time() - start

    print(f"\nBenchmark Results (1000 iterations on 1000-pile position):")
    print(f"Optimized: {optimized_time:.4f} seconds")
    print(f"Naive: {naive_time:.4f} seconds")
    print(f"Speedup: {naive_time / optimized_time:.2f}x")
```

#### Parallel and Distributed Nim

```python
def demonstrate_parallel_nim():
    """Demonstrate parallel computation concepts in Nim."""

    print("Parallel Nim Computation:")
    print("1. Move generation can be parallelized across piles")
    print("2. Position evaluation can be distributed")
    print("3. Game tree search benefits from parallel alpha-beta")

    # Example: Parallel optimal move finding
    import concurrent.futures

    def find_optimal_move_for_pile(pile_info):
        """Find optimal move for a single pile."""
        pile_idx, pile_size, nim_sum = pile_info
        target_size = pile_size ^ nim_sum

        if target_size < pile_size:
            return {
                'pile_index': pile_idx,
                'stones_taken': pile_size - target_size,
                'is_optimal': True
            }
        return None

    def parallel_optimal_move_finder(piles):
        """Find optimal move using parallel computation."""
        nim_sum = functools.reduce(operator.xor, piles)

        if nim_sum == 0:
            return None  # No winning move

        # Prepare data for parallel processing
        pile_info = [(i, pile, nim_sum) for i, pile in enumerate(piles)]

        # Use thread pool for parallel computation
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(find_optimal_move_for_pile, info)
                      for info in pile_info]

            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result and result['is_optimal']:
                    return result

        return None

    # Demonstrate parallel vs sequential
    test_position = [15, 23, 31, 47, 59, 71, 83, 97]

    print(f"\nTesting position: {test_position}")

    # Sequential timing
    start = time.time()
    sequential_result = None
    nim_sum = functools.reduce(operator.xor, test_position)
    if nim_sum != 0:
        for i, pile in enumerate(test_position):
            target = pile ^ nim_sum
            if target < pile:
                sequential_result = {
                    'pile_index': i,
                    'stones_taken': pile - target
                }
                break
    sequential_time = time.time() - start

    # Parallel timing
    start = time.time()
    parallel_result = parallel_optimal_move_finder(test_position)
    parallel_time = time.time() - start

    print(f"Sequential time: {sequential_time:.6f} seconds")
    print(f"Parallel time: {parallel_time:.6f} seconds")
    print(f"Results match: {sequential_result == parallel_result}")
```

## Research Applications and Extensions

### Game Theory Research

```python
def demonstrate_research_applications():
    """Show how Nim applies to broader game theory research."""

    print("Nim in Game Theory Research:")
    print("1. Foundation for analyzing impartial games")
    print("2. Basis for understanding combinatorial game theory")
    print("3. Model for perfect information games")
    print("4. Example of solved game with optimal strategy")

    # Connection to other games
    print("\nConnections to Other Games:")
    print("- Hackenbush: Nim-like game with graph structures")
    print("- Kayles: Nim variant with splitting moves")
    print("- Dawson's Game: Nim-like with restricted moves")
    print("- Green Hackenbush: Partisan game extension")

    # Research questions
    print("\nActive Research Areas:")
    print("- Quantum Nim: Quantum mechanical extensions")
    print("- Continuous Nim: Real-valued pile sizes")
    print("- Misère variants: Last-player-loses games")
    print("- Multi-player Nim: Beyond two-player games")
    print("- Stochastic Nim: Random elements in gameplay")
```

### Machine Learning Applications

```python
def demonstrate_ml_applications():
    """Show machine learning applications with Nim."""

    print("Machine Learning in Nim:")
    print("1. Reinforcement Learning: Agent learns optimal strategy")
    print("2. Neural Networks: Pattern recognition in positions")
    print("3. Genetic Algorithms: Evolving playing strategies")
    print("4. Monte Carlo Methods: Statistical game analysis")

    # Feature engineering example
    print("\nFeature Engineering for ML:")
    position = [7, 11, 13, 17]

    features = {
        'pile_count': len(position),
        'total_stones': sum(position),
        'max_pile': max(position),
        'min_pile': min(position),
        'pile_range': max(position) - min(position),
        'pile_variance': sum((p - sum(position)/len(position))**2 for p in position) / len(position),
        'nim_sum': functools.reduce(operator.xor, position),
        'single_stone_piles': sum(1 for p in position if p == 1),
        'even_piles': sum(1 for p in position if p % 2 == 0),
        'power_of_two_piles': sum(1 for p in position if p & (p - 1) == 0),
        'pile_sum_mod_4': sum(position) % 4,
        'largest_bit_position': max(position).bit_length() if position else 0
    }

    print(f"Position: {position}")
    print("Extracted features:")
    for feature, value in features.items():
        print(f"  {feature}: {value}")

    # Training data generation
    print("\nTraining Data Generation:")
    print("- Generate random positions")
    print("- Calculate optimal moves")
    print("- Extract features from positions")
    print("- Label with win/loss outcomes")
    print("- Train model to predict optimal moves")
```

## Contributing

### Development Setup

```bash
# Clone repository
git clone https://github.com/your-org/haive.git
cd haive

# Install development dependencies
poetry install --extras "dev haive-games"

# Run tests
poetry run pytest packages/haive-games/tests/test_nim/ -v

# Run linting
poetry run ruff check packages/haive-games/src/haive/games/nim/
poetry run black packages/haive-games/src/haive/games/nim/

# Type checking
poetry run mypy packages/haive-games/src/haive/games/nim/
```

### Code Style

- Follow PEP 8 conventions
- Use type hints for all public APIs
- Write comprehensive docstrings
- Include examples in docstrings
- Add unit tests for new features

### Pull Request Process

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Make changes with tests
4. Run full test suite
5. Update documentation
6. Submit pull request

### Testing Requirements

- Minimum 90% test coverage
- All tests must pass
- Include integration tests
- Performance tests for algorithmic changes
- Documentation tests for examples

## Version History

### Version 2.0.0 (Current)

- Complete rewrite with Pydantic v2
- Advanced strategic analysis
- Multi-variant support
- Rich terminal UI
- Performance optimizations
- Comprehensive documentation

### Version 1.5.0

- Added Misère Nim support
- Improved AI analysis
- Bug fixes in state management
- Enhanced visualization

### Version 1.0.0

- Initial release
- Basic Nim gameplay
- Simple AI player
- Console interface

### Planned Features (v2.1.0)

- Web-based UI
- Network multiplayer
- Advanced ML integration
- Tournament bracket system
- Mobile app support

---

**License**: Same as the Haive framework license.

**Maintainers**: Haive Development Team

**Issues**: Please report bugs and feature requests on the GitHub issue tracker.

**Documentation**: Full API documentation available at [docs.haive.ai](https://docs.haive.ai)
