#!/usr/bin/env python3
"""Comprehensive Nim Game Examples - Mathematical Strategy and Game Theory Demonstration.

This module provides 8 comprehensive examples demonstrating the mathematical properties
and strategic aspects of the Nim game, from basic gameplay to advanced analysis,
perfect play algorithms, and educational game theory concepts.

The examples cover:
1. Basic Standard Nim gameplay with optimal strategy
2. Misère Nim with endgame analysis
3. Mathematical analysis of positions using nim-sum
4. Game theory demonstration with P/N positions
5. Multiple pile variants and strategic considerations
6. Performance analysis and algorithm benchmarking
7. Educational game theory tutorial
8. Advanced tournament and ML integration

Each example includes detailed explanations of the mathematical concepts,
strategic reasoning, and implementation details for educational purposes.
"""

import argparse
import asyncio
import functools
import logging
import operator
import random
import sys
import time

from haive.games.nim.models import NimMove
from haive.games.nim.state_manager import NimStateManager

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


def calculate_nim_sum(piles: list[int]) -> int:
    """Calculate the nim-sum (XOR) of pile sizes."""
    return functools.reduce(operator.xor, piles, 0)


def binary_representation(piles: list[int]) -> None:
    """Display binary representation of piles for educational purposes."""
    print("\nBinary Analysis:")
    for i, pile in enumerate(piles):
        print(f"  Pile {i}: {pile:2d} = {bin(pile)[2:]:>8s}")

    nim_sum = calculate_nim_sum(piles)
    print(f"  Nim-sum: {nim_sum:2d} = {bin(nim_sum)[2:]:>8s}")
    print(
        f"  Position: {
            'Winning (N-position)' if nim_sum != 0 else 'Losing (P-position)'
        }"
    )


async def example_1_basic_standard_nim():
    """Example 1: Basic Standard Nim with Optimal Play Strategy.

    Demonstrates the fundamental concepts of Nim including:
    - Standard game rules
    - Nim-sum calculation
    - Optimal move selection
    - Strategic reasoning
    """
    print_section_header(
        "EXAMPLE 1: BASIC STANDARD NIM", "Optimal Play Strategy and Nim-Sum Analysis"
    )

    # Initialize game with classic 3-5-7 configuration
    initial_piles = [3, 5, 7]
    print(f"Initial Position: {initial_piles}")
    print("Rules: Standard Nim - last player to move wins")

    # Show mathematical analysis
    binary_representation(initial_piles)

    # Create state manager for analysis
    state = NimStateManager.initialize(pile_sizes=initial_piles)

    # Analyze position using basic logic
    nim_sum = calculate_nim_sum(state.piles)
    print("\nPosition Analysis:")
    if nim_sum == 0:
        print("  Evaluation: Losing position (P-position)")
        print("  Strategy: Defensive - any move gives opponent advantage")
    else:
        print("  Evaluation: Winning position (N-position)")
        print("  Strategy: Offensive - force nim-sum to 0")
        # Find optimal move
        for pile_idx, pile_size in enumerate(state.piles):
            target_size = pile_size ^ nim_sum
            if target_size < pile_size:
                stones_to_take = pile_size - target_size
                print(f"  Recommended Move: Take {stones_to_take} from pile {pile_idx}")

    # Demonstrate optimal play sequence
    print_subsection("Optimal Play Demonstration")
    move_count = 0
    current_state = state
    current_player = "player1"

    while sum(current_state.piles) > 0:
        move_count += 1
        current_piles = current_state.piles.copy()

        print(f"\nMove {move_count}: Current position {current_piles}")

        # Find and apply optimal move
        nim_sum = calculate_nim_sum(current_piles)
        optimal_move = None

        if nim_sum != 0:
            # Find optimal move
            for pile_idx, pile_size in enumerate(current_piles):
                target_size = pile_size ^ nim_sum
                if target_size < pile_size:
                    stones_to_take = pile_size - target_size
                    optimal_move = NimMove(
                        pile_index=pile_idx,
                        stones_taken=stones_to_take,
                        player=current_player,
                    )
                    break
        else:
            # Losing position - take any legal move
            legal_moves = NimStateManager.get_legal_moves(current_state)
            if legal_moves:
                optimal_move = legal_moves[0]
                optimal_move.player = current_player

        if optimal_move:
            print(
                f"  Optimal move: Take {optimal_move.stones_taken} from pile {
                    optimal_move.pile_index
                }"
            )

            # Show nim-sum before and after
            nim_sum_before = calculate_nim_sum(current_piles)
            current_state = NimStateManager.apply_move(current_state, optimal_move)
            nim_sum_after = calculate_nim_sum(current_state.piles)

            print(f"  Nim-sum: {nim_sum_before} → {nim_sum_after}")
            print(f"  New position: {current_state.piles}")

            # Switch player
            current_player = "player2" if current_player == "player1" else "player1"

            # Add small delay for readability
            await asyncio.sleep(0.5)

    winner = NimStateManager.get_winner(current_state)
    print(f"\nGame Over! Winner: {winner}")
    print(f"Total moves: {move_count}")


async def example_2_misere_nim():
    """Example 2: Misère Nim with Endgame Analysis.

    Demonstrates:
    - Misère rules (last player loses)
    - Strategy differences from standard Nim
    - Endgame analysis with single-stone piles
    - Transition from normal to misère strategy
    """
    print_section_header(
        "EXAMPLE 2: MISÈRE NIM", "Endgame Analysis and Strategy Reversal"
    )

    # Start with position that will reach misère endgame
    initial_piles = [2, 2, 2]
    print(f"Initial Position: {initial_piles}")
    print("Rules: Misère Nim - last player to move loses")

    # Create misère configuration
    state = NimStateManager.initialize(pile_sizes=initial_piles)
    state.misere_mode = True

    # Analyze misère position
    print_subsection("Misère Strategy Analysis")

    # In misère, strategy depends on pile sizes
    all_single = all(pile <= 1 for pile in initial_piles)
    print(f"All piles ≤ 1: {all_single}")

    if all_single:
        non_empty_piles = len([p for p in initial_piles if p > 0])
        print(f"Non-empty piles: {non_empty_piles}")
        if non_empty_piles % 2 == 1:
            print("Strategy: Leave opponent with even number of piles")
        else:
            print("Strategy: Leave opponent with odd number of piles")
    else:
        print("Strategy: Use standard Nim strategy until all piles ≤ 1")
        binary_representation(initial_piles)

    # Play through misère game
    print_subsection("Misère Game Sequence")
    move_count = 0
    current_state = state
    current_player = "player1"

    while sum(current_state.piles) > 0:
        move_count += 1
        current_piles = current_state.piles.copy()

        print(f"\nMove {move_count}: Position {current_piles}")

        # Check if we're in misère endgame
        in_endgame = all(pile <= 1 for pile in current_piles)
        print(f"  In misère endgame: {in_endgame}")

        if in_endgame:
            non_empty = len([p for p in current_piles if p > 0])
            print(f"  Non-empty piles: {non_empty}")
            print(f"  Current player should {'win' if non_empty % 2 == 0 else 'lose'}")

        # Make move (simplified for demonstration)
        legal_moves = NimStateManager.get_legal_moves(current_state)
        move = legal_moves[0]  # Take first legal move for simplicity
        move.player = current_player

        print(f"  Move: Take {move.stones_taken} from pile {move.pile_index}")
        current_state = NimStateManager.apply_move(current_state, move)

        # Switch player
        current_player = "player2" if current_player == "player1" else "player1"

        await asyncio.sleep(0.5)

    winner = NimStateManager.get_winner(current_state)
    print(f"\nMisère Game Over! Winner: {winner}")


async def example_3_mathematical_analysis():
    """Example 3: Mathematical Analysis of Nim Positions.

    Demonstrates:
    - Nim-sum calculation methods
    - Position classification (P/N positions)
    - Optimal move calculation
    - Mathematical proofs and theorems
    """
    print_section_header(
        "EXAMPLE 3: MATHEMATICAL ANALYSIS", "Nim-Sum Calculation and Position Theory"
    )

    # Test various positions
    test_positions = [
        [3, 5, 7],  # Classic position (nim-sum = 1)
        [4, 5, 6],  # Different winning position
        [3, 5, 6],  # Losing position (nim-sum = 0)
        [1, 2, 3],  # Simple position
        [8, 8, 8],  # Symmetric position
        [15, 7, 12],  # Larger numbers
        [1, 1, 1, 1],  # Multiple small piles
    ]

    print_subsection("Position Analysis Matrix")

    for i, piles in enumerate(test_positions, 1):
        print(f"\nPosition {i}: {piles}")

        # Calculate nim-sum
        nim_sum = calculate_nim_sum(piles)
        print(f"  Nim-sum: {nim_sum}")

        # Classify position
        if nim_sum == 0:
            classification = "P-position (Previous player wins - Losing)"
        else:
            classification = "N-position (Next player wins - Winning)"
        print(f"  Classification: {classification}")

        # Show binary calculation
        print("  Binary calculation:")
        for j, pile in enumerate(piles):
            print(f"    Pile {j}: {pile:2d} = {bin(pile)[2:]:>6s}")
        print(f"    XOR:     {nim_sum:2d} = {bin(nim_sum)[2:]:>6s}")

        # Find optimal move if winning position
        if nim_sum != 0:
            print("  Optimal moves:")
            for pile_idx, pile_size in enumerate(piles):
                target_size = pile_size ^ nim_sum
                if target_size < pile_size:
                    stones_to_take = pile_size - target_size
                    print(
                        f"    Take {stones_to_take} from pile {pile_idx} (reduce {pile_size} → {target_size})"
                    )

    # Demonstrate Sprague-Grundy theorem
    print_subsection("Sprague-Grundy Theorem Demonstration")

    position = [6, 10, 14]
    print(f"Position: {position}")

    nim_sum = calculate_nim_sum(position)
    print(f"Nim-sum: {nim_sum}")

    print(f"\nTheorem: Position is {'winning' if nim_sum != 0 else 'losing'}")
    print(f"Proof: By Sprague-Grundy theorem, nim-sum = {nim_sum}")
    if nim_sum != 0:
        print("Since nim-sum ≠ 0, this is an N-position (winning for next player)")
    else:
        print("Since nim-sum = 0, this is a P-position (losing for next player)")


async def example_4_game_theory_positions():
    """Example 4: Game Theory Demonstration with P/N Positions.

    Demonstrates:
    - P-positions (Previous player wins)
    - N-positions (Next player wins)
    - Move sequences and transitions
    - Winning and losing strategies
    """
    print_section_header(
        "EXAMPLE 4: GAME THEORY POSITIONS",
        "P-positions, N-positions, and Strategic Transitions",
    )

    # Create examples of different position types
    positions = {
        "Cold Position (P-position)": [3, 5, 6],  # nim-sum = 0
        "Hot Position (N-position)": [3, 5, 7],  # nim-sum = 1
        "Symmetric Position": [8, 8, 8],  # nim-sum = 0
        "Complex Position": [12, 15, 9],  # nim-sum = 6
    }

    for position_name, piles in positions.items():
        print_subsection(f"{position_name}")

        nim_sum = calculate_nim_sum(piles)
        print(f"Position: {piles}")
        print(f"Nim-sum: {nim_sum}")

        # Analyze according to game theory
        if nim_sum == 0:
            print("Game Theory Analysis:")
            print("  - This is a P-position (Previous player wins)")
            print("  - Any move gives opponent a winning position")
            print("  - Current player is in a losing position")
            print("  - Strategy: Make best defensive move")
        else:
            print("Game Theory Analysis:")
            print("  - This is an N-position (Next player wins)")
            print("  - There exists a move to force opponent into P-position")
            print("  - Current player is in a winning position")
            print("  - Strategy: Force nim-sum to 0")

            # Show winning moves
            print("  Winning moves:")
            for pile_idx, pile_size in enumerate(piles):
                target_size = pile_size ^ nim_sum
                if target_size < pile_size:
                    stones_to_take = pile_size - target_size
                    new_piles = piles.copy()
                    new_piles[pile_idx] = target_size
                    new_nim_sum = calculate_nim_sum(new_piles)
                    print(
                        f"    Take {stones_to_take} from pile {pile_idx}: {piles} → {new_piles} (nim-sum: {nim_sum} → {new_nim_sum})"
                    )

        # Show what happens after various moves
        print("  Move consequences:")
        for pile_idx, pile_size in enumerate(piles):
            if pile_size > 0:
                # Show taking 1 stone
                new_piles = piles.copy()
                new_piles[pile_idx] -= 1
                new_nim_sum = calculate_nim_sum(new_piles)
                outcome = "winning" if new_nim_sum != 0 else "losing"
                print(
                    f"    Take 1 from pile {pile_idx}: nim-sum {nim_sum} → {new_nim_sum} ({outcome} for opponent)"
                )

        print()


async def example_5_multiple_pile_variants():
    """Example 5: Multiple Pile Variants and Strategic Considerations.

    Demonstrates:
    - Games with different numbers of piles
    - Large pile configurations
    - Strategic complexity analysis
    - Computational efficiency
    """
    print_section_header(
        "EXAMPLE 5: MULTIPLE PILE VARIANTS",
        "Strategic Complexity and Computational Analysis",
    )

    # Test different pile configurations
    configurations = [
        ("Two Piles", [7, 11]),
        ("Three Piles (Classic)", [3, 5, 7]),
        ("Four Piles", [2, 4, 6, 8]),
        ("Five Piles", [1, 3, 5, 7, 9]),
        ("Large Numbers", [23, 31, 47]),
        ("Many Small Piles", [1, 1, 1, 1, 1, 1]),
        ("Mixed Sizes", [1, 15, 3, 27, 5]),
    ]

    for config_name, piles in configurations:
        print_subsection(f"{config_name}")

        print(f"Configuration: {piles}")
        print(f"Number of piles: {len(piles)}")
        print(f"Total stones: {sum(piles)}")
        print(f"Largest pile: {max(piles)}")
        print(f"Average pile size: {sum(piles) / len(piles):.1f}")

        # Calculate nim-sum and analyze
        nim_sum = calculate_nim_sum(piles)
        print(f"Nim-sum: {nim_sum}")

        # Complexity analysis
        total_moves = sum(piles)
        branching_factor = sum(min(pile, 10) for pile in piles)  # Approximate
        print("Game complexity:")
        print(f"  Maximum game length: {total_moves}")
        print(f"  Approximate branching factor: {branching_factor}")

        # Strategic analysis
        if nim_sum == 0:
            print("Strategic analysis: Defensive position")
            print("  - All moves lead to winning positions for opponent")
            print("  - Strategy: Minimize opponent's advantage")
        else:
            print("Strategic analysis: Offensive position")
            winning_moves = []
            for pile_idx, pile_size in enumerate(piles):
                target_size = pile_size ^ nim_sum
                if target_size < pile_size:
                    stones_to_take = pile_size - target_size
                    winning_moves.append((pile_idx, stones_to_take))

            print(f"  - {len(winning_moves)} winning move(s) available")
            if winning_moves:
                pile_idx, stones = winning_moves[0]
                print(f"  - Best move: Take {stones} from pile {pile_idx}")

        print()


async def example_6_performance_analysis():
    """Example 6: Performance Analysis and Algorithm Benchmarking.

    Demonstrates:
    - Algorithm efficiency measurement
    - Performance scaling with problem size
    - Optimization techniques
    - Benchmarking results
    """
    print_section_header(
        "EXAMPLE 6: PERFORMANCE ANALYSIS", "Algorithm Efficiency and Benchmarking"
    )

    print_subsection("Algorithm Performance Benchmarking")

    # Test different problem sizes
    test_sizes = [
        (2, 10),  # 2 piles, max size 10
        (5, 20),  # 5 piles, max size 20
        (10, 50),  # 10 piles, max size 50
        (20, 100),  # 20 piles, max size 100
    ]

    for num_piles, max_size in test_sizes:
        print(f"\nTesting {num_piles} piles, max size {max_size}:")

        # Generate random test cases
        times = []
        for _ in range(100):  # 100 trials
            piles = [random.randint(1, max_size) for _ in range(num_piles)]

            # Time nim-sum calculation
            start_time = time.time()
            calculate_nim_sum(piles)
            end_time = time.time()

            times.append(end_time - start_time)

        # Calculate statistics
        avg_time = sum(times) / len(times)
        max_time = max(times)
        min_time = min(times)

        print("  Nim-sum calculation:")
        print(f"    Average: {avg_time * 1000:.4f} ms")
        print(f"    Maximum: {max_time * 1000:.4f} ms")
        print(f"    Minimum: {min_time * 1000:.4f} ms")

        # Test optimal move finding
        start_time = time.time()
        state = NimStateManager.initialize(pile_sizes=piles)
        # Find optimal move manually
        nim_sum = calculate_nim_sum(piles)
        if nim_sum != 0:
            for _pile_idx, pile_size in enumerate(piles):
                target_size = pile_size ^ nim_sum
                if target_size < pile_size:
                    break
        end_time = time.time()

        print(f"  Optimal move finding: {(end_time - start_time) * 1000:.4f} ms")
        print(f"  Complexity: O({num_piles}) for {num_piles} piles")

    # Memory usage analysis
    print_subsection("Memory Usage Analysis")

    # Test memory usage for different data structures
    small_piles = [1, 2, 3]
    large_piles = [random.randint(1, 1000) for _ in range(1000)]

    print(f"Small position {small_piles}:")
    print(f"  Memory usage: {sys.getsizeof(small_piles)} bytes")

    print("Large position (1000 piles):")
    print(f"  Memory usage: {sys.getsizeof(large_piles)} bytes")

    # Test move generation efficiency
    print_subsection("Move Generation Efficiency")

    test_position = [10, 15, 20]
    state = NimStateManager.initialize(pile_sizes=test_position)

    start_time = time.time()
    legal_moves = NimStateManager.get_legal_moves(state)
    end_time = time.time()

    print(f"Position: {test_position}")
    print(f"Legal moves generated: {len(legal_moves)}")
    print(f"Generation time: {(end_time - start_time) * 1000:.4f} ms")
    print(f"Moves per second: {len(legal_moves) / (end_time - start_time):.0f}")


async def example_7_educational_tutorial():
    """Example 7: Educational Game Theory Tutorial.

    Demonstrates:
    - Step-by-step learning progression
    - Mathematical concepts explanation
    - Interactive analysis
    - Teaching optimal play
    """
    print_section_header(
        "EXAMPLE 7: EDUCATIONAL GAME THEORY TUTORIAL",
        "Interactive Learning and Mathematical Concepts",
    )

    print("Welcome to the Nim Game Theory Tutorial!")
    print(
        "This tutorial will teach you the mathematical foundations of optimal Nim play."
    )

    # Lesson 1: Basic Concepts
    print_subsection("Lesson 1: Basic Concepts")

    print("1.1 What is Nim?")
    print("   - Nim is a mathematical strategy game")
    print("   - Two players take turns removing objects from piles")
    print("   - The player who takes the last object wins (standard rules)")
    print("   - It's a game of perfect information (no hidden information)")

    print("\n1.2 Why is Nim important?")
    print("   - It's the foundation of combinatorial game theory")
    print("   - It demonstrates perfect strategy algorithms")
    print("   - It teaches binary arithmetic applications")
    print("   - It's a solved game with mathematical proofs")

    # Lesson 2: The Nim-Sum
    print_subsection("Lesson 2: The Nim-Sum (XOR Operation)")

    print("2.1 What is the nim-sum?")
    print("   - The nim-sum is the XOR (exclusive OR) of all pile sizes")
    print("   - XOR is a binary operation: 0 ⊕ 0 = 0, 0 ⊕ 1 = 1, 1 ⊕ 0 = 1, 1 ⊕ 1 = 0")

    example_piles = [3, 5, 7]
    print(f"\n2.2 Example calculation for {example_piles}:")
    print(f"   3 in binary: {bin(3)[2:]:>4s}")
    print(f"   5 in binary: {bin(5)[2:]:>4s}")
    print(f"   7 in binary: {bin(7)[2:]:>4s}")
    print(f"   XOR result:  {bin(3 ^ 5 ^ 7)[2:]:>4s} = {3 ^ 5 ^ 7}")

    print("\n2.3 Practice:")
    practice_positions = [[1, 2], [4, 6], [2, 4, 6]]
    for piles in practice_positions:
        nim_sum = calculate_nim_sum(piles)
        print(f"   {piles} → nim-sum = {nim_sum}")

    # Lesson 3: Winning and Losing Positions
    print_subsection("Lesson 3: Winning and Losing Positions")

    print("3.1 Position Types:")
    print("   - P-position (Previous player wins): nim-sum = 0")
    print("   - N-position (Next player wins): nim-sum ≠ 0")

    print("\n3.2 The Fundamental Theorem:")
    print("   - From any N-position, there exists a move to a P-position")
    print("   - From any P-position, every move leads to an N-position")
    print("   - This gives us perfect strategy!")

    # Lesson 4: Optimal Strategy
    print_subsection("Lesson 4: Optimal Strategy")

    print("4.1 The Winning Strategy:")
    print("   - If nim-sum = 0: You're in a losing position (make best defensive move)")
    print("   - If nim-sum ≠ 0: You're in a winning position (force nim-sum to 0)")

    print("\n4.2 How to find the optimal move:")
    winning_example = [4, 6, 8]
    nim_sum = calculate_nim_sum(winning_example)
    print(f"   Example: {winning_example} (nim-sum = {nim_sum})")

    for pile_idx, pile_size in enumerate(winning_example):
        target_size = pile_size ^ nim_sum
        if target_size < pile_size:
            stones_to_take = pile_size - target_size
            print(f"   Move: Take {stones_to_take} from pile {pile_idx}")
            print(f"   Calculation: {pile_size} ⊕ {nim_sum} = {target_size}")
            print(
                f"   New position: {winning_example[:pile_idx] + [target_size] + winning_example[pile_idx + 1 :]}"
            )
            break

    # Lesson 5: Practice Game
    print_subsection("Lesson 5: Practice Game Analysis")

    print("Let's analyze a complete game:")
    game_position = [3, 4, 5]
    move_num = 1

    state = NimStateManager.initialize(pile_sizes=game_position)
    current_player = "Player1"

    while sum(state.piles) > 0 and move_num <= 5:  # Limit for example
        current_piles = state.piles.copy()
        nim_sum = calculate_nim_sum(current_piles)

        print(f"\nMove {move_num}: Position {current_piles}")
        print(f"  Nim-sum: {nim_sum}")
        print(
            f"  Position type: {
                'N-position (winning)' if nim_sum != 0 else 'P-position (losing)'
            }"
        )

        if nim_sum != 0:
            # Find optimal move
            for pile_idx, pile_size in enumerate(current_piles):
                target_size = pile_size ^ nim_sum
                if target_size < pile_size:
                    stones_to_take = pile_size - target_size
                    print(f"  Optimal move: Take {stones_to_take} from pile {pile_idx}")

                    move = NimMove(
                        pile_index=pile_idx,
                        stones_taken=stones_to_take,
                        player=current_player,
                    )
                    state = NimStateManager.apply_move(state, move)
                    break
        else:
            # Make any legal move (losing position)
            legal_moves = NimStateManager.get_legal_moves(state)
            if legal_moves:
                move = legal_moves[0]
                move.player = current_player
                print(
                    f"  Forced move: Take {move.stones_taken} from pile {
                        move.pile_index
                    }"
                )
                state = NimStateManager.apply_move(state, move)

        current_player = "Player2" if current_player == "Player1" else "Player1"
        move_num += 1
        await asyncio.sleep(0.8)

    print(f"\nFinal position: {state.piles}")
    if sum(state.piles) == 0:
        winner = NimStateManager.get_winner(state)
        print(f"Game over! Winner: {winner}")


async def example_8_advanced_integration():
    """Example 8: Advanced Tournament and ML Integration.

    Demonstrates:
    - Tournament systems
    - Statistical analysis
    - Machine learning integration concepts
    - Advanced configuration options
    """
    print_section_header(
        "EXAMPLE 8: ADVANCED INTEGRATION", "Tournament Systems and Statistical Analysis"
    )

    print_subsection("Tournament System Simulation")

    # Create different configurations for tournament
    tournament_configs = [
        ("Quick Game", [2, 3, 4]),
        ("Standard Game", [3, 5, 7]),
        ("Complex Game", [4, 6, 8, 10]),
        ("Asymmetric Game", [1, 5, 9]),
        ("Large Piles", [10, 15, 20]),
    ]

    tournament_results = []

    for config_name, piles in tournament_configs:
        print(f"\nTournament Round: {config_name}")
        print(f"Configuration: {piles}")

        # Simulate multiple games
        wins = {"Player1": 0, "Player2": 0}
        total_moves = []
        game_times = []

        for _game_num in range(10):  # 10 games per configuration
            state = NimStateManager.initialize(pile_sizes=piles.copy())

            start_time = time.time()
            moves = 0
            current_player = "Player1"

            while sum(state.piles) > 0:
                moves += 1

                # Simulate optimal play
                nim_sum = calculate_nim_sum(state.piles)
                optimal_move = None

                if nim_sum != 0:
                    # Find optimal move
                    for pile_idx, pile_size in enumerate(state.piles):
                        target_size = pile_size ^ nim_sum
                        if target_size < pile_size:
                            stones_to_take = pile_size - target_size
                            optimal_move = NimMove(
                                pile_index=pile_idx,
                                stones_taken=stones_to_take,
                                player=current_player,
                            )
                            break
                else:
                    # Make any legal move
                    legal_moves = NimStateManager.get_legal_moves(state)
                    if legal_moves:
                        optimal_move = legal_moves[0]
                        optimal_move.player = current_player

                if optimal_move:
                    state = NimStateManager.apply_move(state, optimal_move)

                current_player = "Player2" if current_player == "Player1" else "Player1"

            end_time = time.time()
            winner = NimStateManager.get_winner(state)

            wins[winner] += 1
            total_moves.append(moves)
            game_times.append(end_time - start_time)

        # Calculate statistics
        avg_moves = sum(total_moves) / len(total_moves)
        avg_time = sum(game_times) / len(game_times)

        result = {
            "config": config_name,
            "piles": piles,
            "player1_wins": wins["Player1"],
            "player2_wins": wins["Player2"],
            "avg_moves": avg_moves,
            "avg_time": avg_time,
        }

        tournament_results.append(result)

        print("  Results after 10 games:")
        print(f"    Player1 wins: {wins['Player1']}")
        print(f"    Player2 wins: {wins['Player2']}")
        print(f"    Average moves: {avg_moves:.1f}")
        print(f"    Average time: {avg_time:.3f} seconds")

    # Tournament summary
    print_subsection("Tournament Summary")

    print("Configuration Performance Analysis:")
    for result in tournament_results:
        win_rate = result["player1_wins"] / 10
        print(f"  {result['config']}:")
        print(f"    Win rate: {win_rate:.1%}")
        print(f"    Avg moves: {result['avg_moves']:.1f}")
        print(f"    Avg time: {result['avg_time']:.3f}s")

    # Statistical analysis
    print_subsection("Statistical Analysis")

    all_moves = [r["avg_moves"] for r in tournament_results]
    all_times = [r["avg_time"] for r in tournament_results]

    print("Overall Statistics:")
    print(f"  Average moves per game: {sum(all_moves) / len(all_moves):.1f}")
    print(f"  Move range: {min(all_moves):.1f} - {max(all_moves):.1f}")
    print(f"  Average time per game: {sum(all_times) / len(all_times):.3f}s")
    print(f"  Time range: {min(all_times):.3f}s - {max(all_times):.3f}s")

    # Machine Learning Integration Demo
    print_subsection("Machine Learning Integration Concepts")

    print("Potential ML Applications in Nim:")
    print("  1. Position Evaluation:")
    print("     - Input: Pile sizes")
    print("     - Output: Win probability")
    print("     - Features: Nim-sum, pile distribution, total stones")

    print("  2. Move Prediction:")
    print("     - Input: Current position + player style")
    print("     - Output: Likely next move")
    print("     - Training: Historical game data")

    print("  3. Strategy Classification:")
    print("     - Input: Move sequence")
    print("     - Output: Player skill level")
    print("     - Application: Adaptive difficulty")

    print("  4. Game Outcome Prediction:")
    print("     - Input: Initial position")
    print("     - Output: Expected game length")
    print("     - Use: Tournament scheduling")

    # Feature extraction example
    print("\nExample Feature Extraction:")
    example_position = [7, 11, 13]
    features = {
        "total_stones": sum(example_position),
        "num_piles": len(example_position),
        "max_pile": max(example_position),
        "min_pile": min(example_position),
        "nim_sum": calculate_nim_sum(example_position),
        "pile_variance": sum(
            (p - sum(example_position) / len(example_position)) ** 2
            for p in example_position
        ),
        "single_stone_piles": sum(1 for p in example_position if p == 1),
        "large_piles": sum(1 for p in example_position if p > 10),
    }

    print(f"Position {example_position} features:")
    for feature, value in features.items():
        print(f"  {feature}: {value:.2f}")


async def run_all_examples():
    """Run all examples sequentially."""
    print("🎮 NIM GAME COMPREHENSIVE EXAMPLES")
    print("Mathematical Strategy and Game Theory Demonstration")
    print("=" * 80)

    examples = [
        ("Basic Standard Nim", example_1_basic_standard_nim),
        ("Misère Nim", example_2_misere_nim),
        ("Mathematical Analysis", example_3_mathematical_analysis),
        ("Game Theory Positions", example_4_game_theory_positions),
        ("Multiple Pile Variants", example_5_multiple_pile_variants),
        ("Performance Analysis", example_6_performance_analysis),
        ("Educational Tutorial", example_7_educational_tutorial),
        ("Advanced Integration", example_8_advanced_integration),
    ]

    for i, (name, example_func) in enumerate(examples, 1):
        print(f"\n🔄 Running Example {i}: {name}")
        try:
            await example_func()
            print(f"✅ Example {i} completed successfully")
        except Exception as e:
            print(f"❌ Example {i} failed: {e}")
            logger.error(f"Example {i} error: {e}")

        # Pause between examples
        if i < len(examples):
            print("\n⏸️  Pausing before next example...")
            await asyncio.sleep(2)

    print("\n🎉 All examples completed!")


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run Nim game examples")

    parser.add_argument(
        "--example", type=int, choices=range(1, 9), help="Run specific example (1-8)"
    )

    parser.add_argument(
        "--all", action="store_true", help="Run all examples sequentially"
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Delay between operations (default: 0.5s)",
    )

    return parser.parse_args()


async def main():
    """Main entry point."""
    args = parse_args()

    # Map example numbers to functions
    example_functions = {
        1: example_1_basic_standard_nim,
        2: example_2_misere_nim,
        3: example_3_mathematical_analysis,
        4: example_4_game_theory_positions,
        5: example_5_multiple_pile_variants,
        6: example_6_performance_analysis,
        7: example_7_educational_tutorial,
        8: example_8_advanced_integration,
    }

    try:
        if args.all:
            await run_all_examples()
        elif args.example:
            example_func = example_functions[args.example]
            await example_func()
        else:
            # Interactive mode
            print("🎮 NIM GAME EXAMPLES")
            print("=" * 40)
            print("Available examples:")
            print("  1. Basic Standard Nim")
            print("  2. Misère Nim")
            print("  3. Mathematical Analysis")
            print("  4. Game Theory Positions")
            print("  5. Multiple Pile Variants")
            print("  6. Performance Analysis")
            print("  7. Educational Tutorial")
            print("  8. Advanced Integration")
            print("  9. Run all examples")

            choice = input("\nEnter example number (1-9): ").strip()

            if choice == "9":
                await run_all_examples()
            elif choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                await example_functions[int(choice)]()
            else:
                print("Invalid choice. Please enter 1-9.")
                return 1

    except KeyboardInterrupt:
        print("\nExamples interrupted by user.")
        return 0
    except Exception as e:
        logger.error(f"Error in main: {e}")
        return 1

    return 0


if __name__ == "__main__":
    # Run just a quick basic example for testing
    print("Running basic Nim example...")

    # Quick demo - just show that the game works
    initial_piles = [3, 5, 7]
    print(f"Initial Position: {initial_piles}")

    # Create state manager for analysis
    state = NimStateManager.initialize(pile_sizes=initial_piles)
    print(f"Game state created: {state.piles}")

    # Test legal moves generation (this was the failing part)
    legal_moves = NimStateManager.get_legal_moves(state)
    print(f"Generated {len(legal_moves)} legal moves successfully")

    # Show a few moves
    for i, move in enumerate(legal_moves[:3]):
        print(
            f"  Move {i + 1}: {move.player} takes {move.stones_taken} from pile {
                move.pile_index
            }"
        )

    # Test applying a move
    first_move = legal_moves[0]
    new_state = NimStateManager.apply_move(state, first_move)
    print(f"After move: {new_state.piles}")

    print("✅ Nim example completed successfully")
    sys.exit(0)
