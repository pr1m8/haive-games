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
import contextlib
import json
import logging
import os
import time

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
    if subtitle:
        pass


def print_subsection(title: str) -> None:
    """Print a formatted subsection header."""


def display_board_position(state: CheckersState, title: str = "Board Position") -> None:
    """Display board position in a readable format."""
    for _i, _row in enumerate(state.board):
        pass


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

    # Create and run game
    agent = CheckersAgent(config)

    try:
        result = agent.run_game(visualize=True)

        if result.get("move_history"):
            pass

    except Exception as e:
        logger.exception(f"Game execution failed: {e}")


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

    # Run game with personalities
    agent = CheckersAgent(config)

    try:
        time.time()
        result = agent.run_game(visualize=True)
        time.time()

        # Analyze how personalities affected gameplay
        winner = result.get("winner", "Draw")
        if winner in {"player1", "player2"}:
            pass
        else:
            pass

    except Exception as e:
        logger.exception(f"Advanced game execution failed: {e}")


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

    # Run tournament
    for _matchup_idx, (player1, player2) in enumerate(matchups):
        matchup_wins = {"player1": 0, "player2": 0, "draws": 0}
        matchup_times = []

        for _game_num in range(games_per_matchup):
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

            except Exception as e:
                logger.exception(f"Tournament game failed: {e}")

        # Store matchup results
        tournament_results[f"{player1}_vs_{player2}"] = {
            "wins": matchup_wins,
            "avg_time": sum(matchup_times) / len(matchup_times) if matchup_times else 0,
            "total_games": games_per_matchup,
        }

    # Final tournament analysis

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

    for _style, stats in style_performance.items():
        (stats["wins"] / stats["games"]) * 100 if stats["games"] > 0 else 0


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
    display_board_position(initial_state, "Initial Board Position")

    # Simulate some moves to reach an interesting position
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
            current_state = state_manager.make_move(current_state, player, move)
        except Exception:
            break

    display_board_position(current_state, "Position After Opening Moves")

    # Analyze position for both players

    # Create analyzer configuration
    AugLLMConfig(
        model="gpt-4",
        temperature=0.1,
        system_message="You are a master-level checkers analyst who provides detailed position evaluations.",
    )

    # Analyze for both players
    for player in ["player1", "player2"]:
        try:
            # Get position analysis
            analysis = state_manager.analyze_position(current_state, player)

            if analysis.tactical_opportunities:
                for _opportunity in analysis.tactical_opportunities:
                    pass

            if analysis.threats:
                for _threat in analysis.threats:
                    pass

        except Exception:
            pass

    # Test move validation
    test_move_validation = [
        ("player1", "24-19"),  # Should be valid
        ("player1", "22-17"),  # Should be valid
        ("player1", "25-21"),  # Should be valid
        ("player1", "invalid"),  # Should be invalid
        ("player2", "14-18"),  # Should be valid
        ("player2", "20-24"),  # Should be valid
    ]

    for player, move in test_move_validation:
        state_manager.validate_move(current_state, player, move)


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

    # Create state manager for educational demonstrations
    CheckersStateManager()

    # Run educational game
    agent = CheckersAgent(config)

    try:
        # Enable educational mode features
        agent.run_game(visualize=True)

        # Educational summary

    except Exception as e:
        logger.exception(f"Educational game failed: {e}")


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

    for _name, config in configs.items():
        pass

    # Run performance tests
    results = {}
    games_per_config = 5

    for config_name, config in configs.items():
        times = []
        outcomes = []

        for _game_num in range(games_per_config):
            agent = CheckersAgent(config)

            try:
                start_time = time.time()
                result = agent.run_game(visualize=False)
                end_time = time.time()

                game_time = end_time - start_time
                times.append(game_time)
                outcomes.append(result.get("winner", "Draw"))

            except Exception as e:
                logger.exception(f"Performance test failed: {e}")

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

    # Performance comparison

    for config_name, _stats in results.items():
        pass

    # Identify optimal configuration
    if results:
        min(results.keys(), key=lambda x: results[x]["avg_time"])


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
            """  Init  .

Args:
    name: [TODO: Add description]
    description: [TODO: Add description]
"""
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
                    elif cell not in {".", " "}:
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
                        if (player == "player1" and i < 3) or (
                            player == "player2" and i > 4
                        ):
                            piece_activity += 0.3

            return center_control + piece_activity

        def select_move(
            self, state: CheckersState, player: str, valid_moves: list[str]
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

    for _name, strategy in strategies.items():
        pass

    # Test strategies against each other

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
        with contextlib.suppress(Exception):
            test_state = state_manager.make_move(test_state, player, move)

    display_board_position(test_state, "Test Position")

    # Get valid moves for current player
    valid_moves = state_manager.get_valid_moves(test_state, "player1")

    # Test each strategy
    for _name, strategy in strategies.items():
        # Evaluate position
        strategy.evaluate_position(test_state, "player1")

        # Select best move
        if valid_moves:
            strategy.select_move(test_state, "player1", valid_moves)
        else:
            pass


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

    # Create and run partial game
    agent = CheckersAgent(config)

    try:
        # Run game for limited turns
        agent.run_game(visualize=False)

        # Get current state
        current_state = (
            agent.get_current_state() if hasattr(agent, "get_current_state") else None
        )

        if current_state:
            # Serialize state to JSON
            state_dict = current_state.model_dump()

            # Save to file
            with open("checkers_game_state.json", "w") as f:
                json.dump(state_dict, f, indent=2)

            # Display state information

            # Show recent moves
            if current_state.move_history:
                for _i, _move in enumerate(current_state.move_history[-5:]):
                    pass

            # Demonstrate state loading
            with open("checkers_game_state.json") as f:
                loaded_state_dict = json.load(f)

            # Recreate state object
            loaded_state = CheckersState.model_validate(loaded_state_dict)

            # Verify state integrity
            if current_state.model_dump() == loaded_state.model_dump():
                pass
            else:
                pass

        else:
            pass

    except Exception as e:
        logger.exception(f"State management error: {e}")

    # Demonstrate move history analysis

    # Clean up
    try:
        if os.path.exists("checkers_game_state.json"):
            os.remove("checkers_game_state.json")
    except BaseException:
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
        await examples[args.example - 1]()
    elif args.all:
        for i, example in enumerate(examples, 1):
            try:
                await example()
            except Exception as e:
                logger.exception(f"Example {i} execution failed: {e}")

            if i < len(examples):
                input("\nPress Enter to continue to next example...")
    else:
        pass


if __name__ == "__main__":
    asyncio.run(main())
# asyncio.run(main())
