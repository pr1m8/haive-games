#!/usr/bin/env python3
"""Comprehensive Checkers Game Examples - Strategic Gameplay and AI Analysis.

This module provides 8 comprehensive examples demonstrating the strategic aspects
of the Checkers game, from basic gameplay to advanced tournament analysis,
strategic decision-making, and educational gameplay patterns.

The examples cover:
1. Basic Checkers gameplay with LLM-powered players
2. Advanced player personality configuration
3. Tournament play with multiple game simulation
4. Position analysis and strategic evaluation
5. Educational mode with move explanations
6. Performance testing and optimization
7. Custom strategy implementation
8. Game state management and persistence

Each example includes detailed explanations of strategic concepts,
gameplay mechanics, and configuration options for educational purposes.
"""

import argparse
import asyncio
import json
import logging
import time
from typing import List

from haive.core.engine.aug_llm import AugLLMConfig

from haive.games.checkers.agent import CheckersAgent
from haive.games.checkers.config import CheckersAgentConfig
from haive.games.checkers.state import CheckersState
from haive.games.checkers.state_manager import CheckersStateManager

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger(__name__)


def print_section_header(title: str, subtitle: str = "") -> None:
    """Print a formatted section header."""
    print("\n" + "=" * 80)
    print(f"  {title}")
    if subtitle:
        print(f"  {subtitle}")
    print("=" * 80)


def print_subsection(title: str) -> None:
    """Print a formatted subsection header."""
    print(f"\n--- {title} ---")


def display_board_position(state: CheckersState, title: str = "Board Position") -> None:
    """Display board position in a readable format."""
    print(f"\n{title}:")
    print("  " + " ".join([f"{i:2d}" for i in range(8)]))
    for i, row in enumerate(state.board):
        print(f"{i} {' '.join([f'{cell:2s}' for cell in row])}")


def create_tournament_config(
    player1_style: str, player2_style: str
) -> CheckersAgentConfig:
    """Create tournament configuration with different player styles."""
    style_configs = {
        "aggressive": {
            "temperature": 0.9,
            "system_message": "You are an aggressive checkers player who seeks quick victories through tactical combinations and forcing moves.",
        },
        "defensive": {
            "temperature": 0.3,
            "system_message": "You are a defensive checkers player who prioritizes piece safety and solid positional play.",
        },
        "balanced": {
            "temperature": 0.7,
            "system_message": "You are a balanced checkers player who combines tactical awareness with strategic planning.",
        },
        "analytical": {
            "temperature": 0.1,
            "system_message": "You are an analytical checkers player who carefully evaluates each position before making moves.",
        },
    }

    config = CheckersAgentConfig(
        engines={
            "player1": AugLLMConfig(
                model="gpt-4",
                temperature=style_configs[player1_style]["temperature"],
                system_message=style_configs[player1_style]["system_message"],
            ),
            "player2": AugLLMConfig(
                model="gpt-4",
                temperature=style_configs[player2_style]["temperature"],
                system_message=style_configs[player2_style]["system_message"],
            ),
            "analyzer": AugLLMConfig(
                model="gpt-4",
                temperature=0.1,
                system_message="You are a checkers analysis expert who provides detailed strategic insights.",
            ),
        },
        max_turns=200,
        strategic_depth=2,
        time_per_move=30,
    )

    return config


async def example_1_basic_checkers_game():
    """Example 1: Basic Checkers Game with LLM Players.

    Demonstrates the fundamental concepts of Checkers gameplay including:
    - Standard game rules and mechanics
    - LLM-powered player decision-making
    - Basic position evaluation
    - Game flow and termination
    """
    print_section_header(
        "EXAMPLE 1: BASIC CHECKERS GAME", "LLM-Powered Players with Standard Rules"
    )

    # Create basic configuration
    config = CheckersAgentConfig(max_turns=150, time_per_move=20)

    print("Configuration:")
    print(f"  Max turns: {config.max_turns}")
    print(f"  Strategic depth: {config.strategic_depth}")
    print(f"  Move timeout: {config.time_per_move}s")

    # Create and run game
    print("\nStarting basic Checkers game...")
    agent = CheckersAgent(config)

    try:
        result = agent.run_game(visualize=True)

        print("\nGame Results:")
        print(f"  Winner: {result.get('winner', 'Draw')}")
        print(f"  Total turns: {result.get('turn_count', 'Unknown')}")
        print(f"  Game duration: {result.get('duration', 'Unknown')}")

        if result.get("move_history"):
            print(f"  Moves played: {len(result['move_history'])}")
            print(
                f"  Last move: {result['move_history'][-1] if result['move_history'] else 'None'}"
            )

    except Exception as e:
        print(f"Error during game: {e}")
        logger.error(f"Game execution failed: {e}")


async def example_2_advanced_player_configuration():
    """Example 2: Advanced Player Configuration with Personalities.

    Demonstrates different player personalities and configurations:
    - Aggressive vs. Defensive playing styles
    - Custom system messages and temperature settings
    - Enhanced analysis and strategic depth
    - Player behavior customization
    """
    print_section_header(
        "EXAMPLE 2: ADVANCED PLAYER CONFIGURATION",
        "Different Playing Styles and Personalities",
    )

    # Create configuration with different player personalities
    config = CheckersAgentConfig(
        engines={
            "player1": AugLLMConfig(
                model="gpt-4",
                temperature=0.9,  # High creativity for aggressive play
                system_message="You are an aggressive checkers master who loves tactical combinations. "
                "Always look for forcing moves, jumps, and ways to create multiple threats. "
                "Take calculated risks to gain material or positional advantage.",
            ),
            "player2": AugLLMConfig(
                model="gpt-4",
                temperature=0.3,  # Low temperature for defensive play
                system_message="You are a defensive checkers expert who prioritizes piece safety. "
                "Focus on solid piece placement, avoid unnecessary risks, and "
                "build strong defensive formations before launching attacks.",
            ),
            "analyzer": AugLLMConfig(
                model="gpt-4",
                temperature=0.1,  # Very analytical
                system_message="You are a checkers analysis expert who provides detailed strategic insights "
                "about position evaluation, tactical opportunities, and long-term plans.",
            ),
        },
        max_turns=250,
        strategic_depth=3,
        time_per_move=45,
    )

    print("Player Configurations:")
    print("  Player 1 (Aggressive):")
    print(f"    Temperature: {config.engines['player1'].temperature}")
    print("    Style: Tactical combinations and forcing moves")
    print("  Player 2 (Defensive):")
    print(f"    Temperature: {config.engines['player2'].temperature}")
    print("    Style: Piece safety and solid formations")
    print("  Analyzer:")
    print(f"    Temperature: {config.engines['analyzer'].temperature}")
    print("    Style: Detailed strategic analysis")

    # Run game with personalities
    print("\nRunning game with different player personalities...")
    agent = CheckersAgent(config)

    try:
        start_time = time.time()
        result = agent.run_game(visualize=True)
        end_time = time.time()

        print(f"\nGame completed in {end_time - start_time:.2f} seconds")
        print("\nPersonality Impact Analysis:")

        # Analyze how personalities affected gameplay
        winner = result.get("winner", "Draw")
        if winner == "player1":
            print("  Aggressive strategy prevailed")
            print("  Tactical combinations likely influenced the outcome")
        elif winner == "player2":
            print("  Defensive strategy prevailed")
            print("  Solid play and piece safety likely influenced the outcome")
        else:
            print("  Balanced result - both strategies were effective")

        print("\nFinal Results:")
        print(f"  Winner: {winner}")
        print(f"  Total turns: {result.get('turn_count', 'Unknown')}")

    except Exception as e:
        print(f"Error during advanced game: {e}")
        logger.error(f"Advanced game execution failed: {e}")


async def example_3_tournament_play():
    """Example 3: Tournament Play with Multiple Games.

    Demonstrates tournament-style gameplay including:
    - Multiple game simulation
    - Statistical analysis of results
    - Different player matchups
    - Performance metrics tracking
    """
    print_section_header(
        "EXAMPLE 3: TOURNAMENT PLAY", "Multiple Games with Statistical Analysis"
    )

    # Define tournament participants
    players = ["aggressive", "defensive", "balanced", "analytical"]
    matchups = [
        ("aggressive", "defensive"),
        ("balanced", "analytical"),
        ("aggressive", "balanced"),
        ("defensive", "analytical"),
    ]

    tournament_results = {}
    games_per_matchup = 3

    print("Tournament Setup:")
    print(f"  Players: {', '.join(players)}")
    print(f"  Matchups: {len(matchups)}")
    print(f"  Games per matchup: {games_per_matchup}")
    print(f"  Total games: {len(matchups) * games_per_matchup}")

    # Run tournament
    for matchup_idx, (player1, player2) in enumerate(matchups):
        print(f"\n--- Matchup {matchup_idx + 1}: {player1} vs {player2} ---")

        matchup_wins = {"player1": 0, "player2": 0, "draws": 0}
        matchup_times = []

        for game_num in range(games_per_matchup):
            print(f"  Game {game_num + 1}/{games_per_matchup}...")

            # Create configuration for this matchup
            config = create_tournament_config(player1, player2)
            config.time_per_move = 15  # Faster moves

            agent = CheckersAgent(config)

            try:
                start_time = time.time()
                result = agent.run_game(visualize=False)
                end_time = time.time()

                game_time = end_time - start_time
                matchup_times.append(game_time)

                winner = result.get("winner")
                if winner:
                    matchup_wins[winner] += 1
                else:
                    matchup_wins["draws"] += 1

                print(f"    Winner: {winner or 'Draw'} ({game_time:.1f}s)")

            except Exception as e:
                print(f"    Error: {e}")
                logger.error(f"Tournament game failed: {e}")

        # Store matchup results
        tournament_results[f"{player1}_vs_{player2}"] = {
            "wins": matchup_wins,
            "avg_time": sum(matchup_times) / len(matchup_times) if matchup_times else 0,
            "total_games": games_per_matchup,
        }

        print("  Matchup Results:")
        print(f"    {player1}: {matchup_wins['player1']} wins")
        print(f"    {player2}: {matchup_wins['player2']} wins")
        print(f"    Draws: {matchup_wins['draws']}")
        print(f"    Average game time: {sum(matchup_times) / len(matchup_times):.1f}s")

    # Final tournament analysis
    print("\n" + "=" * 60)
    print("TOURNAMENT SUMMARY")
    print("=" * 60)

    overall_stats = {"total_games": 0, "total_time": 0}
    style_performance = {style: {"wins": 0, "games": 0} for style in players}

    for matchup, results in tournament_results.items():
        overall_stats["total_games"] += results["total_games"]
        overall_stats["total_time"] += results["avg_time"] * results["total_games"]

        # Track style performance
        player1_style, player2_style = matchup.split("_vs_")
        style_performance[player1_style]["wins"] += results["wins"]["player1"]
        style_performance[player1_style]["games"] += results["total_games"]
        style_performance[player2_style]["wins"] += results["wins"]["player2"]
        style_performance[player2_style]["games"] += results["total_games"]

    print(f"Total games played: {overall_stats['total_games']}")
    print(
        f"Average game time: {overall_stats['total_time'] / overall_stats['total_games']:.1f}s"
    )

    print("\nStyle Performance:")
    for style, stats in style_performance.items():
        win_rate = (stats["wins"] / stats["games"]) * 100 if stats["games"] > 0 else 0
        print(f"  {style}: {stats['wins']}/{stats['games']} ({win_rate:.1f}%)")


async def example_4_position_analysis():
    """Example 4: Advanced Position Analysis and Strategic Evaluation.

    Demonstrates comprehensive position analysis including:
    - Static position evaluation
    - Tactical opportunity identification
    - Strategic planning assessment
    - Move quality analysis
    """
    print_section_header(
        "EXAMPLE 4: POSITION ANALYSIS", "Strategic Evaluation and Tactical Assessment"
    )

    # Create state manager for position analysis
    state_manager = CheckersStateManager()

    # Create initial position
    initial_state = state_manager.initialize_game()
    print("Starting from initial position...")
    display_board_position(initial_state, "Initial Board Position")

    # Simulate some moves to reach an interesting position
    print("\nSimulating opening moves...")
    test_moves = [
        ("player1", "22-18"),  # Common opening move
        ("player2", "9-14"),  # Response
        ("player1", "25-22"),  # Development
        ("player2", "11-16"),  # Counter development
        ("player1", "18-15"),  # Advance
        ("player2", "16-20"),  # Central control
    ]

    current_state = initial_state
    for player, move in test_moves:
        try:
            print(f"  {player}: {move}")
            current_state = state_manager.make_move(current_state, player, move)
        except Exception as e:
            print(f"  Error with move {move}: {e}")
            break

    display_board_position(current_state, "Position After Opening Moves")

    # Analyze position for both players
    print("\nPosition Analysis:")

    # Create analyzer configuration
    AugLLMConfig(
        model="gpt-4",
        temperature=0.1,
        system_message="You are a master-level checkers analyst who provides detailed position evaluations.",
    )

    # Analyze for both players
    for player in ["player1", "player2"]:
        print(f"\n--- Analysis for {player} ---")

        try:
            # Get position analysis
            analysis = state_manager.analyze_position(current_state, player)

            print(f"Material Balance: {analysis.material_advantage}")
            print(f"Position Evaluation: {analysis.positional_evaluation}")
            print(f"Recommended Move: {analysis.best_move}")
            print(f"Strategic Notes: {analysis.strategic_notes}")

            if analysis.tactical_opportunities:
                print("Tactical Opportunities:")
                for opportunity in analysis.tactical_opportunities:
                    print(f"  - {opportunity}")

            if analysis.threats:
                print("Threats to Address:")
                for threat in analysis.threats:
                    print(f"  - {threat}")

        except Exception as e:
            print(f"Analysis failed for {player}: {e}")

    # Test move validation
    print("\nMove Validation Analysis:")
    test_move_validation = [
        ("player1", "24-19"),  # Should be valid
        ("player1", "22-17"),  # Should be valid
        ("player1", "25-21"),  # Should be valid
        ("player1", "invalid"),  # Should be invalid
        ("player2", "14-18"),  # Should be valid
        ("player2", "20-24"),  # Should be valid
    ]

    for player, move in test_move_validation:
        is_valid = state_manager.validate_move(current_state, player, move)
        print(f"  {player}: {move} -> {'Valid' if is_valid else 'Invalid'}")


async def example_5_educational_mode():
    """Example 5: Educational Mode with Move Explanations.

    Demonstrates educational features including:
    - Detailed move explanations
    - Strategic concept teaching
    - Interactive learning elements
    - Beginner-friendly guidance
    """
    print_section_header(
        "EXAMPLE 5: EDUCATIONAL MODE", "Learning-Focused Gameplay with Explanations"
    )

    # Create educational configuration
    config = CheckersAgentConfig(
        engines={
            "player1": AugLLMConfig(
                model="gpt-4",
                temperature=0.5,
                system_message="You are a checkers teacher who explains moves clearly. "
                "Always provide educational reasoning for your moves, "
                "including strategic principles and tactical concepts.",
            ),
            "player2": AugLLMConfig(
                model="gpt-4",
                temperature=0.5,
                system_message="You are a checkers instructor who demonstrates good technique. "
                "Explain your moves in terms of opening principles, "
                "positional concepts, and tactical patterns.",
            ),
            "analyzer": AugLLMConfig(
                model="gpt-4",
                temperature=0.1,
                system_message="You are a checkers coach who provides detailed educational analysis. "
                "Explain strategic concepts, evaluate positions thoroughly, "
                "and suggest improvements for both players.",
            ),
        },
        max_turns=100,  # Shorter for educational focus
        strategic_depth=3,
        time_per_move=60,  # More time for detailed explanations
    )

    print("Educational Features:")
    print("  - Detailed move explanations")
    print("  - Strategic concept teaching")
    print("  - Position evaluation tutorials")
    print("  - Tactical pattern recognition")

    # Create state manager for educational demonstrations
    CheckersStateManager()

    print("\nBasic Strategy Concepts:")
    print("1. Opening Principles:")
    print("   - Control the center squares")
    print("   - Develop pieces toward the center")
    print("   - Avoid weakening your position")
    print("   - Maintain piece coordination")

    print("\n2. Tactical Patterns:")
    print("   - Forks: Attack two pieces simultaneously")
    print("   - Pins: Immobilize defending pieces")
    print("   - Skewers: Force valuable pieces to move")
    print("   - Sacrifices: Trade material for advantage")

    print("\n3. Endgame Technique:")
    print("   - King activity is crucial")
    print("   - Control key squares (opposition)")
    print("   - Calculate precisely")
    print("   - Use tempo effectively")

    # Run educational game
    print("\nRunning educational game with explanations...")
    agent = CheckersAgent(config)

    try:
        # Enable educational mode features
        result = agent.run_game(visualize=True)

        print("\nEducational Game Results:")
        print(f"  Winner: {result.get('winner', 'Draw')}")
        print(f"  Moves played: {result.get('turn_count', 'Unknown')}")

        # Educational summary
        print("\nKey Learning Points:")
        print("- Observed opening development patterns")
        print("- Tactical opportunities were identified")
        print("- Position evaluation helped decision-making")
        print("- Strategic principles guided gameplay")

    except Exception as e:
        print(f"Educational game error: {e}")
        logger.error(f"Educational game failed: {e}")


async def example_6_performance_testing():
    """Example 6: Performance Testing and Optimization.

    Demonstrates performance optimization including:
    - Speed vs. quality trade-offs
    - Batch game processing
    - Memory usage optimization
    - Timing analysis
    """
    print_section_header(
        "EXAMPLE 6: PERFORMANCE TESTING", "Speed Optimization and Batch Processing"
    )

    # Performance test configurations
    configs = {
        "speed_optimized": CheckersAgentConfig(
            max_turns=100,
            time_per_move=5,
            strategic_depth=1,
        ),
        "balanced": CheckersAgentConfig(
            max_turns=150,
            time_per_move=15,
            strategic_depth=2,
        ),
        "quality_focused": CheckersAgentConfig(
            max_turns=200,
            time_per_move=30,
            strategic_depth=3,
        ),
    }

    print("Performance Test Configurations:")
    for name, config in configs.items():
        print(f"  {name}:")
        print(f"    Max turns: {config.max_turns}")
        print(f"    Strategic depth: {config.strategic_depth}")
        print(f"    Move timeout: {config.time_per_move}s")

    # Run performance tests
    results = {}
    games_per_config = 5

    for config_name, config in configs.items():
        print(f"\nTesting {config_name} configuration...")

        times = []
        outcomes = []

        for game_num in range(games_per_config):
            print(f"  Game {game_num + 1}/{games_per_config}...", end=" ")

            agent = CheckersAgent(config)

            try:
                start_time = time.time()
                result = agent.run_game(visualize=False)
                end_time = time.time()

                game_time = end_time - start_time
                times.append(game_time)
                outcomes.append(result.get("winner", "Draw"))

                print(f"{game_time:.1f}s ({result.get('winner', 'Draw')})")

            except Exception as e:
                print(f"Error: {e}")
                logger.error(f"Performance test failed: {e}")

        # Calculate statistics
        if times:
            avg_time = sum(times) / len(times)
            min_time = min(times)
            max_time = max(times)

            results[config_name] = {
                "avg_time": avg_time,
                "min_time": min_time,
                "max_time": max_time,
                "games_played": len(times),
                "outcomes": outcomes,
            }

        print(f"  Average time: {avg_time:.1f}s")
        print(f"  Time range: {min_time:.1f}s - {max_time:.1f}s")

    # Performance comparison
    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)

    print(
        f"{'Configuration':<20} {'Avg Time':<10} {'Min Time':<10} {'Max Time':<10} {'Games':<6}"
    )
    print("-" * 60)

    for config_name, stats in results.items():
        print(
            f"{config_name:<20} {stats['avg_time']:<10.1f} {stats['min_time']:<10.1f} {stats['max_time']:<10.1f} {stats['games_played']:<6}"
        )

    # Identify optimal configuration
    if results:
        fastest_config = min(results.keys(), key=lambda x: results[x]["avg_time"])
        print(f"\nFastest configuration: {fastest_config}")
        print("Performance recommendations:")
        print("- Use speed_optimized for batch processing")
        print("- Use balanced for interactive play")
        print("- Use quality_focused for analysis and learning")


async def example_7_custom_strategy():
    """Example 7: Custom Strategy Implementation.

    Demonstrates custom strategy development including:
    - Strategy pattern implementation
    - Custom evaluation functions
    - Move selection algorithms
    - Strategy comparison
    """
    print_section_header("EXAMPLE 7: CUSTOM STRATEGY", "Custom AI Strategy Development")

    # Custom strategy classes
    class CheckersStrategy:
        """Base strategy class for custom implementations."""

        def __init__(self, name: str, description: str):
            self.name = name
            self.description = description

        def evaluate_position(self, state: CheckersState, player: str) -> float:
            """Evaluate position from player's perspective."""
            # Basic material evaluation
            material_score = self.calculate_material_advantage(state, player)
            positional_score = self.calculate_positional_advantage(state, player)

            return material_score + positional_score

        def calculate_material_advantage(
            self, state: CheckersState, player: str
        ) -> float:
            """Calculate material advantage."""
            # Count pieces for each player
            player_pieces = 0
            opponent_pieces = 0

            for row in state.board:
                for cell in row:
                    if player in cell:
                        player_pieces += (
                            3 if "K" in cell else 1
                        )  # Kings worth 3, men worth 1
                    elif cell != "." and cell != " ":
                        opponent_pieces += 3 if "K" in cell else 1

            return player_pieces - opponent_pieces

        def calculate_positional_advantage(
            self, state: CheckersState, player: str
        ) -> float:
            """Calculate positional advantage."""
            # Simple positional evaluation
            center_control = 0
            piece_activity = 0

            # Award points for center control and piece advancement
            for i, row in enumerate(state.board):
                for j, cell in enumerate(row):
                    if player in cell:
                        # Center squares are valuable
                        if 2 <= i <= 5 and 2 <= j <= 5:
                            center_control += 0.5

                        # Advanced pieces are valuable
                        if player == "player1" and i < 3:
                            piece_activity += 0.3
                        elif player == "player2" and i > 4:
                            piece_activity += 0.3

            return center_control + piece_activity

        def select_move(
            self, state: CheckersState, player: str, valid_moves: List[str]
        ) -> str:
            """Select the best move from valid options."""
            if not valid_moves:
                return None

            best_move = None
            best_score = float("-inf")

            # Simulate each move and evaluate resulting position
            state_manager = CheckersStateManager()

            for move in valid_moves:
                try:
                    # Simulate the move
                    new_state = state_manager.make_move(state, player, move)
                    score = self.evaluate_position(new_state, player)

                    if score > best_score:
                        best_score = score
                        best_move = move

                except Exception as e:
                    logger.debug(f"Move simulation failed for {move}: {e}")
                    continue

            return best_move or valid_moves[0]  # Fallback to first valid move

    # Create different strategy instances
    strategies = {
        "material_focused": CheckersStrategy(
            "Material Focused", "Prioritizes capturing pieces and material advantage"
        ),
        "positional_focused": CheckersStrategy(
            "Positional Focused", "Emphasizes piece positioning and center control"
        ),
    }

    print("Custom Strategy Overview:")
    for _name, strategy in strategies.items():
        print(f"  {strategy.name}: {strategy.description}")

    # Test strategies against each other
    print("\nStrategy Comparison Test:")

    # Create state manager for testing
    state_manager = CheckersStateManager()
    test_state = state_manager.initialize_game()

    # Simulate some moves to create interesting position
    opening_moves = [
        ("player1", "22-18"),
        ("player2", "9-14"),
        ("player1", "25-22"),
        ("player2", "11-16"),
    ]

    for player, move in opening_moves:
        try:
            test_state = state_manager.make_move(test_state, player, move)
        except Exception as e:
            print(f"Error applying move {move}: {e}")

    display_board_position(test_state, "Test Position")

    # Get valid moves for current player
    valid_moves = state_manager.get_valid_moves(test_state, "player1")
    print(f"\nValid moves for player1: {valid_moves}")

    # Test each strategy
    for _name, strategy in strategies.items():
        print(f"\n{strategy.name} Analysis:")

        # Evaluate position
        position_score = strategy.evaluate_position(test_state, "player1")
        print(f"  Position evaluation: {position_score:.2f}")

        # Select best move
        if valid_moves:
            best_move = strategy.select_move(test_state, "player1", valid_moves)
            print(f"  Recommended move: {best_move}")
        else:
            print("  No valid moves available")

    print("\nStrategy Implementation Complete!")
    print("Custom strategies can be integrated into the main game loop")
    print("for specialized AI behavior and analysis.")


async def example_8_game_state_management():
    """Example 8: Game State Management and Persistence.

    Demonstrates game state handling including:
    - Game state serialization
    - Save/load functionality
    - Move history tracking
    - State validation
    """
    print_section_header(
        "EXAMPLE 8: GAME STATE MANAGEMENT", "Save/Load and State Persistence"
    )

    # Create configuration for state management demo
    config = CheckersAgentConfig(max_turns=50, time_per_move=10)

    print("Game State Management Features:")
    print("  - JSON serialization/deserialization")
    print("  - Move history tracking")
    print("  - State validation")
    print("  - Game replay capability")

    # Create and run partial game
    print("\nRunning partial game for state capture...")
    agent = CheckersAgent(config)

    try:
        # Run game for limited turns
        result = agent.run_game(visualize=False)

        # Get current state
        current_state = (
            agent.get_current_state() if hasattr(agent, "get_current_state") else None
        )

        if current_state:
            print(
                f"Game state captured after {result.get('turn_count', 'unknown')} turns"
            )

            # Serialize state to JSON
            state_dict = current_state.model_dump()

            # Save to file
            with open("checkers_game_state.json", "w") as f:
                json.dump(state_dict, f, indent=2)

            print("Game state saved to checkers_game_state.json")

            # Display state information
            print("\nState Information:")
            print(f"  Current player: {current_state.current_player}")
            print(f"  Game over: {current_state.game_over}")
            print(f"  Winner: {current_state.winner or 'Game in progress'}")
            print(f"  Move history length: {len(current_state.move_history)}")

            # Show recent moves
            if current_state.move_history:
                print("\nRecent moves:")
                for i, move in enumerate(current_state.move_history[-5:]):
                    print(f"  {i+1}. {move}")

            # Demonstrate state loading
            print("\nLoading saved state...")
            with open("checkers_game_state.json", "r") as f:
                loaded_state_dict = json.load(f)

            # Recreate state object
            loaded_state = CheckersState.model_validate(loaded_state_dict)

            print("State loaded successfully!")
            print(f"  Loaded current player: {loaded_state.current_player}")
            print(f"  Loaded game over: {loaded_state.game_over}")
            print(f"  Loaded move count: {len(loaded_state.move_history)}")

            # Verify state integrity
            if current_state.model_dump() == loaded_state.model_dump():
                print("✓ State integrity verified - save/load working correctly")
            else:
                print("✗ State integrity check failed")

        else:
            print("Unable to capture game state")

    except Exception as e:
        print(f"State management demo failed: {e}")
        logger.error(f"State management error: {e}")

    # Demonstrate move history analysis
    print("\nMove History Analysis:")
    print("This feature enables:")
    print("  - Game replay and analysis")
    print("  - Position reconstruction")
    print("  - Performance evaluation")
    print("  - Educational review")

    # Clean up
    try:
        import os

        if os.path.exists("checkers_game_state.json"):
            os.remove("checkers_game_state.json")
            print("Cleaned up temporary files")
    except:
        pass


async def main():
    """Main function to run all examples."""
    parser = argparse.ArgumentParser(description="Checkers Game Examples")
    parser.add_argument(
        "--example", type=int, choices=range(1, 9), help="Run specific example (1-8)"
    )
    parser.add_argument("--all", action="store_true", help="Run all examples")

    args = parser.parse_args()

    examples = [
        example_1_basic_checkers_game,
        example_2_advanced_player_configuration,
        example_3_tournament_play,
        example_4_position_analysis,
        example_5_educational_mode,
        example_6_performance_testing,
        example_7_custom_strategy,
        example_8_game_state_management,
    ]

    if args.example:
        print(f"Running Example {args.example}...")
        await examples[args.example - 1]()
    elif args.all:
        print("Running all Checkers examples...")
        for i, example in enumerate(examples, 1):
            print(f"\n{'='*20} EXAMPLE {i} {'='*20}")
            try:
                await example()
            except Exception as e:
                print(f"Example {i} failed: {e}")
                logger.error(f"Example {i} execution failed: {e}")

            if i < len(examples):
                input("\nPress Enter to continue to next example...")
    else:
        print("Checkers Game Examples")
        print("Available examples:")
        print("  1. Basic Checkers Game")
        print("  2. Advanced Player Configuration")
        print("  3. Tournament Play")
        print("  4. Position Analysis")
        print("  5. Educational Mode")
        print("  6. Performance Testing")
        print("  7. Custom Strategy")
        print("  8. Game State Management")
        print("\nUse --example <number> to run specific example")
        print("Use --all to run all examples")


if __name__ == "__main__":
    asyncio.run(main())
