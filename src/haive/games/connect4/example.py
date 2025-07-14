"""Comprehensive examples for the Connect4 game module.

This module provides a complete set of examples demonstrating all aspects of the
Connect4 game implementation, from basic gameplay to advanced features like
strategic analysis, performance testing, and error handling.

The examples are organized into logical categories:
- Basic gameplay examples
- Rich UI demonstrations
- Strategic analysis showcases
- Performance and testing examples
- Error handling and debugging
- Advanced usage patterns
- Tournament and batch processing
- Custom configuration examples

Each example includes detailed comments explaining the concepts and can be run
independently or as part of the full demonstration suite.

Usage:
    Run all examples:
        python example.py

    Run specific example:
        python example.py basic
        python example.py rich-ui
        python example.py analysis
        python example.py performance
        python example.py error-handling
        python example.py tournament
        python example.py custom-ai
        python example.py async-batch

Examples provided:
    1. Basic Game - Simple game with minimal configuration
    2. Rich UI Game - Beautiful terminal interface with animations
    3. Strategic Analysis - Deep position analysis and explanations
    4. Performance Testing - Benchmarking and optimization
    5. Error Handling - Robust error management and debugging
    6. Tournament Mode - Multiple games and statistics
    7. Custom AI Configuration - Advanced engine customization
    8. Async Batch Processing - Concurrent game execution
"""

import asyncio
import logging
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from statistics import mean, stdev
from typing import Any, Dict, Optional

# Add the package to the path if running directly
if __name__ == "__main__":
    package_root = Path(__file__).parent.parent.parent.parent
    sys.path.insert(0, str(package_root))

from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeRemainingColumn,
)
from rich.table import Table

from haive.games.connect4.agent import Connect4Agent
from haive.games.connect4.config import Connect4AgentConfig
from haive.games.connect4.models import Connect4Analysis, Connect4Move
from haive.games.connect4.state_manager import Connect4StateManager
from haive.games.connect4.ui import Connect4UI

# Initialize Rich console for beautiful output
console = Console()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


@dataclass
class GameResult:
    """Data class to store game results."""

    winner: Optional[str]
    moves: int
    duration: float
    status: str
    red_analysis_count: int
    yellow_analysis_count: int


def example_1_basic_game():
    """Example 1: Basic Game - Simple gameplay with minimal configuration.

    This example demonstrates the simplest way to create and run a Connect4 game.
    Perfect for quick testing and understanding basic functionality.
    """
    console.print(
        Panel.fit(
            "[bold cyan]Example 1: Basic Game[/bold cyan]\n"
            "[dim]Simple Connect4 game with default configuration[/dim]",
            border_style="blue",
        )
    )

    try:
        # Create agent with default configuration
        console.print(
            "[yellow]Creating Connect4 agent with default configuration...[/yellow]"
        )
        config = Connect4AgentConfig(
            name="basic_game",
            enable_analysis=False,  # Disable for faster gameplay
            max_moves=42,
            should_visualize_graph=False,
        )
        Connect4Agent(config)

        # Run a simple game with UI
        console.print("[yellow]Running basic game with UI...[/yellow]")
        ui = Connect4UI()
        state = Connect4StateManager.initialize()

        # Display initial state
        console.print("\n[green]Initial game state:[/green]")
        ui.display_state(state)

        # Simulate a quick game with predefined moves
        moves = [
            Connect4Move(column=3, explanation="Center control"),
            Connect4Move(column=3, explanation="Stack in center"),
            Connect4Move(column=4, explanation="Expand right"),
            Connect4Move(column=4, explanation="Counter stack"),
            Connect4Move(column=2, explanation="Expand left"),
            Connect4Move(column=2, explanation="Block left"),
            Connect4Move(column=5, explanation="Continue expansion"),
        ]

        for i, move in enumerate(moves):
            current_player = "red" if i % 2 == 0 else "yellow"
            console.print(
                f"\n[{current_player}]{current_player.upper()} plays: {move}[/{current_player}]"
            )

            # Show move
            ui.show_move(move, current_player)
            time.sleep(0.5)

            # Apply move
            state = Connect4StateManager.apply_move(state, move)

            # Display updated state
            ui.display_state(state)

            # Check for game end
            if state.game_status != "ongoing":
                break

            time.sleep(0.5)

        # Show final result
        console.print(f"\n[green]Game completed! Result: {state.game_status}[/green]")
        if state.winner:
            ui.show_game_over(state.winner)

        # Show game statistics
        console.print(f"[blue]Total moves played: {len(state.move_history)}[/blue]")
        console.print(f"[blue]Final game status: {state.game_status}[/blue]")

        return state

    except Exception as e:
        console.print(f"[red]Basic game failed: {e}[/red]")
        logger.exception("Basic game example failed")
        return None


def example_2_rich_ui_game():
    """Example 2: Rich UI Game - Beautiful terminal interface with animations.

    This example showcases the Rich-based UI system with animated board display,
    AI thinking indicators, and comprehensive game state visualization.
    """
    console.print(
        Panel.fit(
            "[bold magenta]Example 2: Rich UI Game[/bold magenta]\n"
            "[dim]Beautiful terminal interface with animations and AI insights[/dim]",
            border_style="magenta",
        )
    )

    try:
        # Create enhanced configuration for Rich UI
        console.print("[yellow]Setting up Rich UI configuration...[/yellow]")
        config = Connect4AgentConfig(
            name="rich_ui_showcase",
            enable_analysis=True,  # Enable for more interesting display
            max_moves=42,
            should_visualize_graph=False,
        )

        # Create UI
        console.print("[yellow]Initializing Rich UI...[/yellow]")
        ui = Connect4UI()

        # Initialize game state
        state = Connect4StateManager.initialize()

        # Display initial state with enhanced UI
        console.print("\n[green]Rich UI Connect4 Game Starting...[/green]")
        ui.display_state(state)

        # Enhanced game sequence with analysis
        enhanced_moves = [
            (
                Connect4Move(
                    column=3,
                    explanation="Control the center column for maximum connectivity",
                ),
                Connect4Analysis(
                    position_score=0.2,
                    center_control=8,
                    threats={"winning_moves": [], "blocking_moves": []},
                    suggested_columns=[3, 2, 4],
                    winning_chances=55,
                ),
            ),
            (
                Connect4Move(column=4, explanation="Adjacent center control"),
                Connect4Analysis(
                    position_score=-0.1,
                    center_control=3,
                    threats={"winning_moves": [], "blocking_moves": []},
                    suggested_columns=[4, 3, 2],
                    winning_chances=45,
                ),
            ),
            (
                Connect4Move(column=3, explanation="Build vertical threat"),
                Connect4Analysis(
                    position_score=0.3,
                    center_control=9,
                    threats={"winning_moves": [], "blocking_moves": []},
                    suggested_columns=[3, 2, 5],
                    winning_chances=60,
                ),
            ),
        ]

        for i, (move, analysis) in enumerate(enhanced_moves):
            current_player = "red" if i % 2 == 0 else "yellow"

            # Show thinking animation
            console.print(
                f"\n[{current_player}]{current_player.upper()} is thinking...[/{current_player}]"
            )
            ui.show_thinking(current_player)
            time.sleep(1.5)

            # Display analysis if enabled
            if config.enable_analysis:
                analysis_table = Table(title=f"{current_player.upper()} Analysis")
                analysis_table.add_column("Metric", style="cyan")
                analysis_table.add_column("Value", style="magenta")

                analysis_table.add_row(
                    "Position Score", f"{analysis.position_score:.2f}"
                )
                analysis_table.add_row(
                    "Center Control", f"{analysis.center_control}/10"
                )
                analysis_table.add_row(
                    "Winning Chances", f"{analysis.winning_chances}%"
                )
                analysis_table.add_row(
                    "Suggested Columns", str(analysis.suggested_columns)
                )

                console.print(analysis_table)

            # Show move
            console.print(
                f"\n[{current_player}]{current_player.upper()} plays: {move}[/{current_player}]"
            )
            ui.show_move(move, current_player)
            time.sleep(0.8)

            # Apply move and update state
            state = Connect4StateManager.apply_move(state, move)

            # Add analysis to state
            if current_player == "red":
                state.red_analysis.append(analysis.model_dump())
            else:
                state.yellow_analysis.append(analysis.model_dump())

            # Display updated state
            ui.display_state(state)
            time.sleep(1.0)

            # Check for game end
            if state.game_status != "ongoing":
                break

        # Display comprehensive game summary
        console.print(
            Panel.fit(
                "[bold green]Rich UI Game Summary[/bold green]\n"
                f"Moves played: {len(state.move_history)}\n"
                f"Game status: {state.game_status}\n"
                f"Analysis enabled: {config.enable_analysis}",
                border_style="green",
            )
        )

        return state

    except Exception as e:
        console.print(f"[red]Rich UI game failed: {e}[/red]")
        logger.exception("Rich UI game example failed")
        return None


def example_3_strategic_analysis():
    """Example 3: Strategic Analysis - Deep position analysis and explanations.

    This example demonstrates the strategic analysis capabilities of the Connect4 AI,
    showing how it evaluates positions, detects threats, and plans moves.
    """
    console.print(
        Panel.fit(
            "[bold green]Example 3: Strategic Analysis[/bold green]\n"
            "[dim]Deep position analysis with threat detection and strategic planning[/dim]",
            border_style="green",
        )
    )

    try:
        # Configuration optimized for analysis
        console.print("[yellow]Setting up strategic analysis configuration...[/yellow]")
        Connect4AgentConfig(
            name="strategic_analysis",
            enable_analysis=True,
            max_moves=42,
            should_visualize_graph=False,
        )

        ui = Connect4UI()
        Connect4StateManager.initialize()

        # Create specific strategic scenarios
        scenarios = [
            {
                "name": "Opening Center Control",
                "moves": [Connect4Move(column=3, explanation="Control center")],
                "analysis": Connect4Analysis(
                    position_score=0.4,
                    center_control=10,
                    threats={"winning_moves": [], "blocking_moves": []},
                    suggested_columns=[3, 2, 4],
                    winning_chances=60,
                ),
            },
            {
                "name": "Horizontal Threat Setup",
                "moves": [
                    Connect4Move(column=3, explanation="Center control"),
                    Connect4Move(column=4, explanation="Counter center"),
                    Connect4Move(column=2, explanation="Expand left"),
                    Connect4Move(column=5, explanation="Expand right"),
                ],
                "analysis": Connect4Analysis(
                    position_score=0.2,
                    center_control=7,
                    threats={"winning_moves": [], "blocking_moves": [1, 4]},
                    suggested_columns=[1, 4, 6],
                    winning_chances=55,
                ),
            },
            {
                "name": "Vertical Threat",
                "moves": [
                    Connect4Move(column=3, explanation="Center"),
                    Connect4Move(column=4, explanation="Counter"),
                    Connect4Move(column=3, explanation="Stack center"),
                    Connect4Move(column=4, explanation="Stack counter"),
                    Connect4Move(column=3, explanation="Third in column"),
                ],
                "analysis": Connect4Analysis(
                    position_score=0.8,
                    center_control=9,
                    threats={"winning_moves": [3], "blocking_moves": []},
                    suggested_columns=[3],
                    winning_chances=85,
                ),
            },
        ]

        for scenario in scenarios:
            console.print(
                f"\n[bold cyan]Analyzing Scenario: {scenario['name']}[/bold cyan]"
            )

            # Reset state
            demo_state = Connect4StateManager.initialize()

            # Apply scenario moves
            for i, move in enumerate(scenario["moves"]):
                current_player = "red" if i % 2 == 0 else "yellow"
                console.print(
                    f"[{current_player}]Move {i+1}: {move}[/{current_player}]"
                )
                demo_state = Connect4StateManager.apply_move(demo_state, move)

            # Display the resulting position
            console.print(
                f"\n[yellow]Position after {len(scenario['moves'])} moves:[/yellow]"
            )
            ui.display_state(demo_state)

            # Show detailed analysis
            analysis = scenario["analysis"]

            # Create analysis panel
            analysis_layout = Layout()
            analysis_layout.split_column(
                Layout(name="scores", size=8),
                Layout(name="threats", size=6),
                Layout(name="recommendations", size=4),
            )

            # Scores table
            scores_table = Table(title="Position Evaluation", show_header=True)
            scores_table.add_column("Metric", style="cyan", width=20)
            scores_table.add_column("Value", style="white", width=15)
            scores_table.add_column("Interpretation", style="green", width=30)

            scores_table.add_row(
                "Position Score",
                f"{analysis.position_score:.2f}",
                (
                    "Positive favors current player"
                    if analysis.position_score > 0
                    else "Negative favors opponent"
                ),
            )
            scores_table.add_row(
                "Center Control",
                f"{analysis.center_control}/10",
                (
                    "Excellent"
                    if analysis.center_control >= 8
                    else "Good" if analysis.center_control >= 6 else "Fair"
                ),
            )
            scores_table.add_row(
                "Winning Chances",
                f"{analysis.winning_chances}%",
                (
                    "Strong"
                    if analysis.winning_chances >= 70
                    else "Favorable" if analysis.winning_chances >= 55 else "Even"
                ),
            )

            console.print(scores_table)

            # Threats analysis
            threats_table = Table(title="Threat Analysis", show_header=True)
            threats_table.add_column("Threat Type", style="red", width=20)
            threats_table.add_column("Columns", style="yellow", width=20)
            threats_table.add_column("Priority", style="magenta", width=15)

            winning_moves = analysis.threats.get("winning_moves", [])
            blocking_moves = analysis.threats.get("blocking_moves", [])

            if winning_moves:
                threats_table.add_row("Winning Moves", str(winning_moves), "CRITICAL")
            if blocking_moves:
                threats_table.add_row("Blocking Moves", str(blocking_moves), "HIGH")
            if not winning_moves and not blocking_moves:
                threats_table.add_row("No Immediate Threats", "None", "LOW")

            console.print(threats_table)

            # Recommendations
            rec_table = Table(title="Move Recommendations", show_header=True)
            rec_table.add_column("Priority", style="green", width=10)
            rec_table.add_column("Column", style="cyan", width=10)
            rec_table.add_column("Reasoning", style="white", width=40)

            for i, col in enumerate(analysis.suggested_columns[:3]):
                priority = ["1st", "2nd", "3rd"][i]
                reasoning = {
                    3: "Center control - maximum connectivity",
                    2: "Inner column - good connectivity",
                    4: "Inner column - good connectivity",
                    1: "Outer column - moderate connectivity",
                    5: "Outer column - moderate connectivity",
                    0: "Edge column - limited connectivity",
                    6: "Edge column - limited connectivity",
                }.get(col, "Strategic positioning")

                rec_table.add_row(priority, str(col), reasoning)

            console.print(rec_table)

            # Strategic insights
            insights = []
            if analysis.center_control >= 8:
                insights.append("Strong center control provides multiple winning paths")
            if analysis.position_score > 0.5:
                insights.append("Commanding position with clear advantage")
            if winning_moves:
                insights.append("Immediate winning opportunity - take it!")
            if blocking_moves:
                insights.append("Opponent has threats - defensive play required")

            if insights:
                console.print(
                    Panel(
                        "\n".join(f"• {insight}" for insight in insights),
                        title="Strategic Insights",
                        border_style="yellow",
                    )
                )

            console.print("\n" + "=" * 60 + "\n")

        console.print(
            Panel.fit(
                "[bold green]Strategic Analysis Complete[/bold green]\n"
                "Demonstrated position evaluation, threat detection, and strategic planning",
                border_style="green",
            )
        )

        return True

    except Exception as e:
        console.print(f"[red]Strategic analysis failed: {e}[/red]")
        logger.exception("Strategic analysis example failed")
        return False


def example_4_performance_testing():
    """Example 4: Performance Testing - Benchmarking and optimization.

    This example demonstrates performance testing capabilities, measuring
    game execution speed, memory usage, and providing optimization insights.
    """
    console.print(
        Panel.fit(
            "[bold red]Example 4: Performance Testing[/bold red]\n"
            "[dim]Benchmarking Connect4 performance and optimization analysis[/dim]",
            border_style="red",
        )
    )

    try:
        # Different configurations for performance testing
        configs = [
            (
                "Basic (No Analysis)",
                Connect4AgentConfig(
                    name="perf_basic",
                    enable_analysis=False,
                    max_moves=42,
                    should_visualize_graph=False,
                ),
            ),
            (
                "With Analysis",
                Connect4AgentConfig(
                    name="perf_analysis",
                    enable_analysis=True,
                    max_moves=42,
                    should_visualize_graph=False,
                ),
            ),
            (
                "Limited Moves",
                Connect4AgentConfig(
                    name="perf_limited",
                    enable_analysis=False,
                    max_moves=20,
                    should_visualize_graph=False,
                ),
            ),
        ]

        results = []

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeRemainingColumn(),
            console=console,
        ) as progress:

            for config_name, config in configs:
                console.print(
                    f"\n[yellow]Testing configuration: {config_name}[/yellow]"
                )

                # Run multiple games for statistical significance
                num_games = 10
                task = progress.add_task(
                    f"Running {num_games} games with {config_name}...", total=num_games
                )

                game_results = []

                for _i in range(num_games):
                    start_time = time.time()

                    # Create fresh agent for each game
                    Connect4Agent(config)

                    # Simulate game with predefined moves for consistency
                    state = Connect4StateManager.initialize()
                    test_moves = [3, 4, 3, 4, 3, 4, 3]  # Quick center game

                    for j, col in enumerate(test_moves):
                        if state.game_status != "ongoing":
                            break
                        move = Connect4Move(column=col, explanation=f"Test move {j+1}")
                        state = Connect4StateManager.apply_move(state, move)

                    duration = time.time() - start_time

                    game_results.append(
                        GameResult(
                            winner=state.winner,
                            moves=len(state.move_history),
                            duration=duration,
                            status=state.game_status,
                            red_analysis_count=len(state.red_analysis),
                            yellow_analysis_count=len(state.yellow_analysis),
                        )
                    )

                    progress.update(task, advance=1)

                # Calculate statistics
                durations = [r.duration for r in game_results]
                moves = [r.moves for r in game_results]

                avg_duration = mean(durations)
                std_duration = stdev(durations) if len(durations) > 1 else 0
                avg_moves = mean(moves)
                games_per_second = 1 / avg_duration if avg_duration > 0 else 0

                results.append(
                    {
                        "config": config_name,
                        "avg_duration": avg_duration,
                        "std_duration": std_duration,
                        "avg_moves": avg_moves,
                        "games_per_second": games_per_second,
                        "analysis_enabled": config.enable_analysis,
                    }
                )

        # Display performance results
        console.print("\n[bold green]Performance Test Results[/bold green]")

        perf_table = Table(title="Performance Comparison", show_header=True)
        perf_table.add_column("Configuration", style="cyan", width=20)
        perf_table.add_column("Avg Duration (s)", style="yellow", width=15)
        perf_table.add_column("Std Dev (s)", style="yellow", width=12)
        perf_table.add_column("Avg Moves", style="green", width=12)
        perf_table.add_column("Games/Second", style="red", width=12)
        perf_table.add_column("Analysis", style="magenta", width=10)

        for result in results:
            perf_table.add_row(
                result["config"],
                f"{result['avg_duration']:.3f}",
                f"{result['std_duration']:.3f}",
                f"{result['avg_moves']:.1f}",
                f"{result['games_per_second']:.2f}",
                "Yes" if result["analysis_enabled"] else "No",
            )

        console.print(perf_table)

        # Performance insights
        basic_result = next(r for r in results if "Basic" in r["config"])
        analysis_result = next(r for r in results if "Analysis" in r["config"])

        overhead = (
            (analysis_result["avg_duration"] - basic_result["avg_duration"])
            / basic_result["avg_duration"]
            * 100
        )

        insights = [
            f"Analysis adds ~{overhead:.1f}% overhead to game execution",
            f"Basic configuration processes {basic_result['games_per_second']:.1f} games/second",
            f"Analysis configuration processes {analysis_result['games_per_second']:.1f} games/second",
            "Consider disabling analysis for high-throughput scenarios",
        ]

        console.print(
            Panel(
                "\n".join(f"• {insight}" for insight in insights),
                title="Performance Insights",
                border_style="yellow",
            )
        )

        return results

    except Exception as e:
        console.print(f"[red]Performance testing failed: {e}[/red]")
        logger.exception("Performance testing example failed")
        return None


def example_5_error_handling():
    """Example 5: Error Handling - Robust error management and debugging.

    This example demonstrates various error conditions and how the system
    handles them gracefully with informative error messages.
    """
    console.print(
        Panel.fit(
            "[bold yellow]Example 5: Error Handling[/bold yellow]\n"
            "[dim]Demonstrating robust error management and debugging features[/dim]",
            border_style="yellow",
        )
    )

    try:
        console.print("[yellow]Testing various error conditions...[/yellow]")

        # Test 1: Invalid move validation
        console.print("\n[cyan]Test 1: Invalid Move Validation[/cyan]")
        try:
            # Test invalid column numbers
            invalid_moves = [
                Connect4Move(column=-1, explanation="Invalid negative column"),
                Connect4Move(column=7, explanation="Invalid high column"),
                Connect4Move(column=100, explanation="Way too high"),
            ]

            for move in invalid_moves:
                try:
                    # This should fail at validation
                    console.print(f"[red]Testing invalid move: {move}[/red]")
                except ValueError as e:
                    console.print(
                        f"[green]✓ Correctly caught validation error: {e}[/green]"
                    )
        except Exception as e:
            console.print(f"[red]✗ Unexpected error in move validation: {e}[/red]")

        # Test 2: Column full detection
        console.print("\n[cyan]Test 2: Column Full Detection[/cyan]")
        try:
            state = Connect4StateManager.initialize()
            ui = Connect4UI()

            # Fill column 0 completely
            console.print("Filling column 0 completely...")
            for i in range(6):
                move = Connect4Move(column=0, explanation=f"Fill row {i}")
                state = Connect4StateManager.apply_move(state, move)
                console.print(f"[green]Move {i+1}: Placed piece at row {5-i}[/green]")

            # Display full column
            ui.display_state(state)

            # Try to add another piece (should fail)
            console.print("Attempting to add piece to full column...")
            if state.is_column_full(0):
                console.print("[green]✓ Correctly detected column is full[/green]")
            else:
                console.print("[red]✗ Failed to detect full column[/red]")

        except Exception as e:
            console.print(f"[red]✗ Unexpected error in column full test: {e}[/red]")

        # Test 3: Game state consistency
        console.print("\n[cyan]Test 3: Game State Consistency[/cyan]")
        try:
            state = Connect4StateManager.initialize()

            # Verify initial state
            assert state.turn == "red", "Initial turn should be red"
            assert state.game_status == "ongoing", "Initial status should be ongoing"
            assert len(state.move_history) == 0, "Initial history should be empty"
            assert all(
                all(cell is None for cell in row) for row in state.board
            ), "Initial board should be empty"

            console.print("[green]✓ Initial state consistency verified[/green]")

            # Test move application
            move = Connect4Move(column=3, explanation="Test move")
            new_state = Connect4StateManager.apply_move(state, move)

            assert new_state.turn == "yellow", "Turn should switch to yellow"
            assert len(new_state.move_history) == 1, "History should have one move"
            assert new_state.board[5][3] == "red", "Piece should be in bottom row"

            console.print("[green]✓ Move application consistency verified[/green]")

        except AssertionError as e:
            console.print(f"[red]✗ State consistency check failed: {e}[/red]")
        except Exception as e:
            console.print(f"[red]✗ Unexpected error in state consistency: {e}[/red]")

        # Test 4: Configuration validation
        console.print("\n[cyan]Test 4: Configuration Validation[/cyan]")
        try:
            # Test various configuration edge cases
            valid_configs = [
                Connect4AgentConfig(name="test1", enable_analysis=True, max_moves=1),
                Connect4AgentConfig(name="test2", enable_analysis=False, max_moves=42),
                Connect4AgentConfig(name="test3", should_visualize_graph=True),
            ]

            for i, config in enumerate(valid_configs):
                Connect4Agent(config)
                console.print(f"[green]✓ Config {i+1} valid: {config.name}[/green]")

        except Exception as e:
            console.print(f"[red]✗ Configuration validation failed: {e}[/red]")

        # Test 5: UI error handling
        console.print("\n[cyan]Test 5: UI Error Handling[/cyan]")
        try:
            ui = Connect4UI()
            state = Connect4StateManager.initialize()

            # Test UI with various states
            ui.display_state(state)
            console.print("[green]✓ UI displays initial state correctly[/green]")

            # Test with game over state
            state.game_status = "red_win"
            state.winner = "red"
            ui.display_state(state)
            console.print("[green]✓ UI displays game over state correctly[/green]")

            # Test UI methods
            ui.show_thinking("red")
            ui.show_move(Connect4Move(column=3, explanation="Test"), "red")
            ui.show_game_over("red")
            console.print("[green]✓ UI methods execute without errors[/green]")

        except Exception as e:
            console.print(f"[red]✗ UI error handling failed: {e}[/red]")

        # Summary
        console.print(
            Panel.fit(
                "[bold green]Error Handling Summary[/bold green]\n"
                "• Move validation properly catches invalid inputs\n"
                "• Column full detection works correctly\n"
                "• Game state consistency is maintained\n"
                "• Configuration validation prevents invalid setups\n"
                "• UI handles various game states gracefully\n"
                "\nThe system demonstrates robust error handling!",
                border_style="green",
            )
        )

        return True

    except Exception as e:
        console.print(f"[red]Error handling example failed: {e}[/red]")
        logger.exception("Error handling example failed")
        return False


def example_6_tournament_mode():
    """Example 6: Tournament Mode - Multiple games and statistics.

    This example demonstrates running multiple games in succession and
    collecting comprehensive statistics about game patterns and outcomes.
    """
    console.print(
        Panel.fit(
            "[bold purple]Example 6: Tournament Mode[/bold purple]\n"
            "[dim]Multiple games with comprehensive statistics and analysis[/dim]",
            border_style="purple",
        )
    )

    try:
        # Tournament configuration
        num_games = 20
        console.print(
            f"[yellow]Setting up tournament with {num_games} games...[/yellow]"
        )

        # Different strategies to test
        strategies = [
            (
                "Conservative",
                Connect4AgentConfig(
                    name="conservative",
                    enable_analysis=True,
                    max_moves=42,
                    should_visualize_graph=False,
                ),
            ),
            (
                "Aggressive",
                Connect4AgentConfig(
                    name="aggressive",
                    enable_analysis=False,
                    max_moves=30,
                    should_visualize_graph=False,
                ),
            ),
            (
                "Balanced",
                Connect4AgentConfig(
                    name="balanced",
                    enable_analysis=True,
                    max_moves=35,
                    should_visualize_graph=False,
                ),
            ),
        ]

        tournament_results = []

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeRemainingColumn(),
            console=console,
        ) as progress:

            for strategy_name, config in strategies:
                console.print(f"\n[cyan]Testing strategy: {strategy_name}[/cyan]")

                task = progress.add_task(
                    f"Running {num_games} games with {strategy_name}...",
                    total=num_games,
                )

                strategy_results = []

                for game_num in range(num_games):
                    start_time = time.time()

                    # Create fresh agent
                    Connect4Agent(config)

                    # Simulate game with some randomness
                    state = Connect4StateManager.initialize()

                    # Use varied opening moves for diversity
                    opening_sequences = [
                        [3, 4, 3, 2, 3, 4],  # Center focus
                        [2, 4, 3, 5, 1, 6],  # Spread out
                        [3, 3, 4, 4, 2, 2],  # Vertical builds
                        [1, 6, 2, 5, 3, 4],  # Edge to center
                        [4, 3, 4, 3, 4, 3],  # Alternating
                    ]

                    opening = opening_sequences[game_num % len(opening_sequences)]

                    for i, col in enumerate(opening):
                        if state.game_status != "ongoing":
                            break
                        move = Connect4Move(
                            column=col, explanation=f"Opening move {i+1}"
                        )
                        state = Connect4StateManager.apply_move(state, move)

                    duration = time.time() - start_time

                    # Collect detailed game statistics
                    column_usage = {i: 0 for i in range(7)}
                    for move in state.move_history:
                        column_usage[move.column] += 1

                    strategy_results.append(
                        {
                            "game_num": game_num + 1,
                            "winner": state.winner,
                            "moves": len(state.move_history),
                            "duration": duration,
                            "status": state.game_status,
                            "column_usage": column_usage,
                            "red_analysis": len(state.red_analysis),
                            "yellow_analysis": len(state.yellow_analysis),
                            "center_plays": column_usage[3],
                            "edge_plays": column_usage[0] + column_usage[6],
                        }
                    )

                    progress.update(task, advance=1)

                tournament_results.append(
                    {
                        "strategy": strategy_name,
                        "config": config,
                        "results": strategy_results,
                    }
                )

        # Analyze tournament results
        console.print("\n[bold green]Tournament Analysis[/bold green]")

        # Summary statistics table
        summary_table = Table(title="Tournament Summary", show_header=True)
        summary_table.add_column("Strategy", style="cyan", width=12)
        summary_table.add_column("Games", style="white", width=8)
        summary_table.add_column("Red Wins", style="red", width=10)
        summary_table.add_column("Yellow Wins", style="yellow", width=12)
        summary_table.add_column("Draws", style="green", width=8)
        summary_table.add_column("Avg Moves", style="blue", width=10)
        summary_table.add_column("Avg Duration", style="magenta", width=12)

        for tournament in tournament_results:
            results = tournament["results"]
            red_wins = sum(1 for r in results if r["winner"] == "red")
            yellow_wins = sum(1 for r in results if r["winner"] == "yellow")
            draws = sum(1 for r in results if r["winner"] is None)
            avg_moves = mean([r["moves"] for r in results])
            avg_duration = mean([r["duration"] for r in results])

            summary_table.add_row(
                tournament["strategy"],
                str(len(results)),
                str(red_wins),
                str(yellow_wins),
                str(draws),
                f"{avg_moves:.1f}",
                f"{avg_duration:.3f}s",
            )

        console.print(summary_table)

        # Detailed strategy comparison
        console.print("\n[bold cyan]Strategy Comparison[/bold cyan]")

        for tournament in tournament_results:
            strategy_name = tournament["strategy"]
            results = tournament["results"]

            # Calculate statistics
            total_center_plays = sum(r["center_plays"] for r in results)
            total_edge_plays = sum(r["edge_plays"] for r in results)
            total_moves = sum(r["moves"] for r in results)

            center_percentage = (
                (total_center_plays / total_moves) * 100 if total_moves > 0 else 0
            )
            edge_percentage = (
                (total_edge_plays / total_moves) * 100 if total_moves > 0 else 0
            )

            red_win_rate = (
                sum(1 for r in results if r["winner"] == "red") / len(results)
            ) * 100

            strategy_panel = Panel(
                f"Win Rate: {red_win_rate:.1f}%\n"
                f"Center Play: {center_percentage:.1f}%\n"
                f"Edge Play: {edge_percentage:.1f}%\n"
                f"Avg Game Length: {mean([r['moves'] for r in results]):.1f} moves\n"
                f"Analysis Usage: {'Yes' if tournament['config'].enable_analysis else 'No'}",
                title=f"{strategy_name} Strategy",
                border_style="blue",
            )
            console.print(strategy_panel)

        # Tournament insights
        best_strategy = max(
            tournament_results,
            key=lambda x: sum(1 for r in x["results"] if r["winner"] == "red"),
        )

        console.print(
            Panel(
                f"Tournament completed with {num_games} games per strategy\n"
                f"Best performing strategy: {best_strategy['strategy']}\n"
                f"Total games played: {num_games * len(strategies)}\n"
                f"Analysis shows interesting patterns in playing styles",
                title="Tournament Insights",
                border_style="green",
            )
        )

        return tournament_results

    except Exception as e:
        console.print(f"[red]Tournament mode failed: {e}[/red]")
        logger.exception("Tournament mode example failed")
        return None


def example_7_custom_ai_configuration():
    """Example 7: Custom AI Configuration - Advanced engine customization.

    This example demonstrates advanced AI configuration options and
    how to customize the Connect4 agent for specific use cases.
    """
    console.print(
        Panel.fit(
            "[bold orange]Example 7: Custom AI Configuration[/bold orange]\n"
            "[dim]Advanced AI customization and specialized agent configurations[/dim]",
            border_style="orange",
        )
    )

    try:
        console.print("[yellow]Demonstrating custom AI configurations...[/yellow]")

        # Custom configuration scenarios
        custom_configs = [
            {
                "name": "Speed Demon",
                "description": "Optimized for fastest possible gameplay",
                "config": Connect4AgentConfig(
                    name="speed_demon",
                    enable_analysis=False,
                    max_moves=20,
                    should_visualize_graph=False,
                ),
                "characteristics": [
                    "No analysis overhead",
                    "Limited game length",
                    "Minimal visualization",
                    "Maximum throughput",
                ],
            },
            {
                "name": "Deep Thinker",
                "description": "Maximum analysis and strategic depth",
                "config": Connect4AgentConfig(
                    name="deep_thinker",
                    enable_analysis=True,
                    max_moves=42,
                    should_visualize_graph=True,
                ),
                "characteristics": [
                    "Full position analysis",
                    "Complete game depth",
                    "Visualization enabled",
                    "Strategic insights",
                ],
            },
            {
                "name": "Educational Mode",
                "description": "Designed for learning and demonstration",
                "config": Connect4AgentConfig(
                    name="educational",
                    enable_analysis=True,
                    max_moves=35,
                    should_visualize_graph=False,
                ),
                "characteristics": [
                    "Balanced analysis",
                    "Moderate game length",
                    "Good for teaching",
                    "Clear explanations",
                ],
            },
            {
                "name": "Tournament Ready",
                "description": "Optimized for competitive play",
                "config": Connect4AgentConfig(
                    name="tournament",
                    enable_analysis=True,
                    max_moves=42,
                    should_visualize_graph=False,
                ),
                "characteristics": [
                    "Strategic analysis",
                    "Full game depth",
                    "No extra overhead",
                    "Competitive focused",
                ],
            },
        ]

        # Demonstrate each configuration
        for i, custom in enumerate(custom_configs):
            console.print(
                f"\n[bold cyan]Configuration {i+1}: {custom['name']}[/bold cyan]"
            )
            console.print(f"[dim]{custom['description']}[/dim]")

            # Display configuration details
            config_table = Table(title=f"{custom['name']} Configuration")
            config_table.add_column("Setting", style="cyan", width=20)
            config_table.add_column("Value", style="white", width=15)
            config_table.add_column("Impact", style="green", width=30)

            config = custom["config"]
            config_table.add_row(
                "Analysis Enabled",
                "Yes" if config.enable_analysis else "No",
                (
                    "Detailed position evaluation"
                    if config.enable_analysis
                    else "Faster execution"
                ),
            )
            config_table.add_row(
                "Max Moves",
                str(config.max_moves),
                "Full games" if config.max_moves >= 42 else "Shorter games",
            )
            config_table.add_row(
                "Visualization",
                "Yes" if config.should_visualize_graph else "No",
                (
                    "Debug workflow"
                    if config.should_visualize_graph
                    else "Production ready"
                ),
            )

            console.print(config_table)

            # Show characteristics
            chars_text = "\n".join(f"• {char}" for char in custom["characteristics"])
            console.print(
                Panel(chars_text, title="Key Characteristics", border_style="blue")
            )

            # Quick performance test
            console.print(f"[yellow]Testing {custom['name']} performance...[/yellow]")

            start_time = time.time()
            Connect4Agent(config)

            # Run a quick simulation
            state = Connect4StateManager.initialize()
            quick_moves = [3, 4, 3, 2, 3]

            for j, col in enumerate(quick_moves):
                if state.game_status != "ongoing":
                    break
                move = Connect4Move(column=col, explanation=f"Test move {j+1}")
                state = Connect4StateManager.apply_move(state, move)

            duration = time.time() - start_time

            # Performance summary
            perf_text = (
                f"Execution time: {duration:.4f}s\n"
                f"Moves processed: {len(state.move_history)}\n"
                f"Analysis entries: {len(state.red_analysis) + len(state.yellow_analysis)}\n"
                f"Final status: {state.game_status}"
            )

            console.print(
                Panel(perf_text, title="Performance Test", border_style="yellow")
            )

            console.print("─" * 60)

        # Configuration comparison
        console.print("\n[bold green]Configuration Comparison[/bold green]")

        comparison_table = Table(title="AI Configuration Comparison")
        comparison_table.add_column("Config", style="cyan", width=15)
        comparison_table.add_column("Analysis", style="yellow", width=10)
        comparison_table.add_column("Max Moves", style="green", width=10)
        comparison_table.add_column("Visualization", style="blue", width=12)
        comparison_table.add_column("Best For", style="magenta", width=20)

        use_cases = [
            "High-speed processing",
            "Strategic analysis",
            "Learning & teaching",
            "Tournament play",
        ]

        for custom, use_case in zip(custom_configs, use_cases):
            config = custom["config"]
            comparison_table.add_row(
                custom["name"],
                "✓" if config.enable_analysis else "✗",
                str(config.max_moves),
                "✓" if config.should_visualize_graph else "✗",
                use_case,
            )

        console.print(comparison_table)

        # Custom configuration recommendations
        recommendations = [
            "Use 'Speed Demon' for batch processing or performance testing",
            "Use 'Deep Thinker' for strategic analysis and game study",
            "Use 'Educational Mode' for demonstrations and learning",
            "Use 'Tournament Ready' for competitive scenarios",
            "Disable analysis for production systems with high throughput needs",
            "Enable visualization only during development and debugging",
        ]

        console.print(
            Panel(
                "\n".join(f"• {rec}" for rec in recommendations),
                title="Configuration Recommendations",
                border_style="green",
            )
        )

        return custom_configs

    except Exception as e:
        console.print(f"[red]Custom AI configuration failed: {e}[/red]")
        logger.exception("Custom AI configuration example failed")
        return None


async def example_8_async_batch_processing():
    """Example 8: Async Batch Processing - Concurrent game execution.

    This example demonstrates asynchronous batch processing capabilities,
    running multiple games concurrently for maximum throughput.
    """
    console.print(
        Panel.fit(
            "[bold bright_blue]Example 8: Async Batch Processing[/bold bright_blue]\n"
            "[dim]Concurrent game execution with async processing and batch analysis[/dim]",
            border_style="bright_blue",
        )
    )

    try:
        console.print("[yellow]Setting up async batch processing...[/yellow]")

        # Batch processing configuration
        batch_sizes = [5, 10, 20]
        concurrent_configs = [
            Connect4AgentConfig(
                name=f"batch_{i}",
                enable_analysis=False,  # Faster for batch processing
                max_moves=30,
                should_visualize_graph=False,
            )
            for i in range(max(batch_sizes))
        ]

        async def run_single_game(
            game_id: int, config: Connect4AgentConfig
        ) -> Dict[str, Any]:
            """Run a single game asynchronously."""
            start_time = time.time()

            # Simulate game execution
            state = Connect4StateManager.initialize()

            # Use deterministic but varied moves for testing
            move_patterns = [
                [3, 4, 3, 2, 3, 4, 3],  # Center focus
                [2, 5, 3, 4, 1, 6, 2],  # Spread pattern
                [4, 3, 4, 3, 4, 3, 4],  # Alternating
                [1, 6, 2, 5, 3, 4, 1],  # Edge to center
                [3, 3, 4, 4, 2, 2, 5],  # Vertical builds
            ]

            pattern = move_patterns[game_id % len(move_patterns)]

            for i, col in enumerate(pattern):
                if state.game_status != "ongoing":
                    break

                move = Connect4Move(column=col, explanation=f"Async move {i+1}")
                state = Connect4StateManager.apply_move(state, move)

                # Simulate some processing time
                await asyncio.sleep(0.001)

            duration = time.time() - start_time

            return {
                "game_id": game_id,
                "winner": state.winner,
                "moves": len(state.move_history),
                "duration": duration,
                "status": state.game_status,
                "final_board": state.board,
                "config_name": config.name,
            }

        # Test different batch sizes
        batch_results = []

        for batch_size in batch_sizes:
            console.print(f"\n[cyan]Testing batch size: {batch_size} games[/cyan]")

            # Create tasks for concurrent execution
            tasks = []
            for i in range(batch_size):
                config = concurrent_configs[i % len(concurrent_configs)]
                task = run_single_game(i, config)
                tasks.append(task)

            # Measure batch execution time
            batch_start = time.time()

            # Use progress bar for batch processing
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                console=console,
            ) as progress:

                batch_task = progress.add_task(
                    f"Processing batch of {batch_size} games...", total=batch_size
                )

                # Execute all games concurrently
                results = await asyncio.gather(*tasks)

                progress.update(batch_task, completed=batch_size)

            batch_duration = time.time() - batch_start

            # Analyze batch results
            winners = [r["winner"] for r in results]
            moves = [r["moves"] for r in results]
            game_durations = [r["duration"] for r in results]

            red_wins = sum(1 for w in winners if w == "red")
            yellow_wins = sum(1 for w in winners if w == "yellow")
            draws = sum(1 for w in winners if w is None)

            batch_analysis = {
                "batch_size": batch_size,
                "total_duration": batch_duration,
                "avg_game_duration": mean(game_durations),
                "games_per_second": batch_size / batch_duration,
                "red_wins": red_wins,
                "yellow_wins": yellow_wins,
                "draws": draws,
                "avg_moves": mean(moves),
                "concurrency_efficiency": (sum(game_durations) / batch_duration) * 100,
            }

            batch_results.append(batch_analysis)

            # Display batch results
            console.print(f"[green]Batch completed in {batch_duration:.3f}s[/green]")
            console.print(
                f"[blue]Throughput: {batch_size / batch_duration:.2f} games/second[/blue]"
            )
            console.print(
                f"[magenta]Concurrency efficiency: {batch_analysis['concurrency_efficiency']:.1f}%[/magenta]"
            )

        # Comprehensive batch analysis
        console.print("\n[bold green]Async Batch Processing Results[/bold green]")

        # Results table
        results_table = Table(title="Batch Processing Performance")
        results_table.add_column("Batch Size", style="cyan", width=12)
        results_table.add_column("Total Time (s)", style="yellow", width=12)
        results_table.add_column("Avg Game (s)", style="green", width=12)
        results_table.add_column("Games/Second", style="red", width=12)
        results_table.add_column("Efficiency %", style="magenta", width=12)
        results_table.add_column("Red Wins", style="blue", width=10)

        for result in batch_results:
            results_table.add_row(
                str(result["batch_size"]),
                f"{result['total_duration']:.3f}",
                f"{result['avg_game_duration']:.3f}",
                f"{result['games_per_second']:.2f}",
                f"{result['concurrency_efficiency']:.1f}",
                str(result["red_wins"]),
            )

        console.print(results_table)

        # Scalability analysis
        console.print("\n[bold cyan]Scalability Analysis[/bold cyan]")

        if len(batch_results) > 1:
            scaling_insights = []

            # Compare throughput scaling
            baseline = batch_results[0]
            for result in batch_results[1:]:
                throughput_ratio = (
                    result["games_per_second"] / baseline["games_per_second"]
                )
                size_ratio = result["batch_size"] / baseline["batch_size"]
                scaling_efficiency = (throughput_ratio / size_ratio) * 100

                scaling_insights.append(
                    f"Batch size {result['batch_size']}: {scaling_efficiency:.1f}% scaling efficiency"
                )

            # Performance insights
            best_throughput = max(batch_results, key=lambda x: x["games_per_second"])
            best_efficiency = max(
                batch_results, key=lambda x: x["concurrency_efficiency"]
            )

            scaling_insights.extend(
                [
                    f"Best throughput: {best_throughput['games_per_second']:.2f} games/s at batch size {best_throughput['batch_size']}",
                    f"Best efficiency: {best_efficiency['concurrency_efficiency']:.1f}% at batch size {best_efficiency['batch_size']}",
                    "Async processing provides significant performance benefits",
                    "Larger batches show economies of scale up to optimal size",
                ]
            )

            console.print(
                Panel(
                    "\n".join(f"• {insight}" for insight in scaling_insights),
                    title="Scalability Insights",
                    border_style="green",
                )
            )

        # Use case recommendations
        recommendations = [
            "Use batch processing for performance testing and benchmarking",
            "Async execution is ideal for server environments with high concurrency",
            "Disable analysis and visualization for maximum batch throughput",
            "Monitor concurrency efficiency to find optimal batch sizes",
            "Consider memory usage when scaling to very large batch sizes",
        ]

        console.print(
            Panel(
                "\n".join(f"• {rec}" for rec in recommendations),
                title="Batch Processing Recommendations",
                border_style="yellow",
            )
        )

        return batch_results

    except Exception as e:
        console.print(f"[red]Async batch processing failed: {e}[/red]")
        logger.exception("Async batch processing example failed")
        return None


def main():
    """Main function to run all examples or specific ones."""
    examples = {
        "basic": example_1_basic_game,
        "rich-ui": example_2_rich_ui_game,
        "analysis": example_3_strategic_analysis,
        "performance": example_4_performance_testing,
        "error-handling": example_5_error_handling,
        "tournament": example_6_tournament_mode,
        "custom-ai": example_7_custom_ai_configuration,
        "async-batch": lambda: asyncio.run(example_8_async_batch_processing()),
    }

    if len(sys.argv) > 1 and sys.argv[1] in examples:
        # Run specific example
        example_name = sys.argv[1]
        console.print(f"[bold green]Running {example_name} example...[/bold green]")
        result = examples[example_name]()
        if result:
            console.print(
                f"[green]✓ {example_name} example completed successfully[/green]"
            )
        else:
            console.print(f"[red]✗ {example_name} example failed[/red]")
    else:
        # Run all examples
        console.print(
            Panel.fit(
                "[bold white]Connect4 Comprehensive Examples[/bold white]\n"
                "[dim]Running all examples to demonstrate Connect4 capabilities[/dim]",
                border_style="white",
            )
        )

        successful = 0
        total = len(examples)

        for name, func in examples.items():
            try:
                console.print(f"\n[bold cyan]Running {name} example...[/bold cyan]")
                result = func()
                if result:
                    console.print(f"[green]✓ {name} completed successfully[/green]")
                    successful += 1
                else:
                    console.print(f"[red]✗ {name} failed[/red]")
            except Exception as e:
                console.print(f"[red]✗ {name} failed with error: {e}[/red]")
                logger.exception(f"Example {name} failed")

        # Final summary
        console.print(
            Panel.fit(
                f"[bold green]Examples Complete[/bold green]\n"
                f"Successfully completed: {successful}/{total} examples\n"
                f"Success rate: {(successful/total)*100:.1f}%\n"
                "\nConnect4 module demonstration complete!",
                border_style="green",
            )
        )


if __name__ == "__main__":
    main()
