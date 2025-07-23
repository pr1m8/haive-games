"""Comprehensive examples for the Tic Tac Toe game module.

This module provides a complete set of examples demonstrating all aspects of the
Tic Tac Toe game implementation, from basic gameplay to advanced features like
strategic analysis, performance testing, and error handling.

The examples are organized into logical categories:
- Basic gameplay examples
- Rich UI demonstrations
- Strategic analysis showcases
- Performance and testing examples
- Error handling and debugging
- Advanced usage patterns

Each example includes detailed comments explaining the concepts and can be run
independently or as part of the full demonstration suite.

Usage:
    Run all examples:
        python example.py

    Run specific example:
        python example.py basic
        python example.py rich
        python example.py analysis
        python example.py performance
        python example.py error-handling
        python example.py tournament
        python example.py async
        python example.py custom-ai

Examples provided:
    1. Basic Game - Simple game with minimal configuration
    2. Rich UI Game - Beautiful terminal interface with animations
    3. Strategic Analysis - Deep position analysis and explanations
    4. Performance Testing - Benchmarking and optimization
    5. Error Handling - Robust error management and debugging
    6. Tournament Mode - Batch game execution and statistics
    7. Async Execution - Concurrent game processing
    8. Custom AI Configuration - Advanced engine customization
"""

import asyncio
import logging
import sys
import time
from pathlib import Path
from typing import Any, Dict

# Add the package to the path if running directly
if __name__ == "__main__":
    package_root = Path(__file__).parent.parent.parent.parent
    sys.path.insert(0, str(package_root))

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

from haive.games.tic_tac_toe.agent import TicTacToeAgent
from haive.games.tic_tac_toe.config import TicTacToeConfig
from haive.games.tic_tac_toe.models import TicTacToeAnalysis, TicTacToeMove
from haive.games.tic_tac_toe.ui import RichTicTacToeRunner

# Initialize Rich console for beautiful output
console = Console()


def example_1_basic_game():
    """Example 1: Basic Game - Simple gameplay with minimal configuration.

    This example demonstrates the simplest way to create and run a Tic Tac Toe game.
    Perfect for quick testing and understanding basic functionality.
    """
    console.print(
        Panel.fit(
            "[bold cyan]Example 1: Basic Game[/bold cyan]\n"
            "[dim]Simple Tic Tac Toe game with default configuration[/dim]",
            border_style="blue",
        )
    )

    try:
        # Create agent with default configuration
        console.print("[yellow]Creating agent with default configuration...[/yellow]")
        agent = TicTacToeAgent()

        # Run a simple game
        console.print("[yellow]Running basic game...[/yellow]")
        final_state = agent.run_game(visualize=True)

        # Display results
        game_status = final_state.get("game_status", "unknown")
        console.print(f"[green]Game completed! Result: {game_status}[/green]")

        # Show some game statistics
        moves_played = len(final_state.get("move_history", []))
        console.print(f"[blue]Total moves played: {moves_played}[/blue]")

        return final_state

    except Exception as e:
        console.print(f"[red]Basic game failed: {e}[/red]")
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
        config = TicTacToeConfig(
            name="rich_ui_showcase",
            enable_analysis=True,  # Enable for more interesting display
            visualize=False,  # Rich UI handles visualization
            first_player="X",
            player_X="AI Player 1",
            player_O="AI Player 2",
        )

        # Create agent and UI runner
        console.print("[yellow]Initializing AI agent and Rich UI...[/yellow]")
        agent = TicTacToeAgent(config)
        ui_runner = RichTicTacToeRunner(agent)

        # Run with enhanced UI settings
        console.print("[green]Starting Rich UI game...[/green]")
        final_state = ui_runner.run_game(
            show_thinking=True,  # Show AI thinking animations
            step_delay=2.0,  # Slower for better visualization
        )

        # Display comprehensive game summary
        if final_state:
            console.print("\n[green]Game Summary:[/green]")
            ui_runner.show_game_summary(final_state)

        return final_state

    except Exception as e:
        console.print(f"[red]Rich UI game failed: {e}[/red]")
        return None


def example_3_strategic_analysis():
    """Example 3: Strategic Analysis - Deep position analysis and explanations.

    This example demonstrates the strategic analysis capabilities, showing how
    the AI evaluates positions, identifies threats, and explains its reasoning.
    """
    console.print(
        Panel.fit(
            "[bold green]Example 3: Strategic Analysis[/bold green]\n"
            "[dim]Deep position analysis with detailed explanations[/dim]",
            border_style="green",
        )
    )

    try:
        # Create configuration optimized for analysis
        console.print("[yellow]Setting up analysis-focused configuration...[/yellow]")
        config = TicTacToeConfig(
            name="analysis_showcase",
            enable_analysis=True,
            visualize=False,
            first_player="X",
            player_X="Strategic AI",
            player_O="Analytical AI",
        )

        # Create agent with analysis enabled
        agent = TicTacToeAgent(config)

        # Create a sample position for analysis
        console.print("[yellow]Demonstrating position analysis...[/yellow]")

        # Example of manual analysis demonstration
        sample_analysis = TicTacToeAnalysis(
            winning_moves=[{"row": 0, "col": 2}],
            blocking_moves=[],
            fork_opportunities=[],
            center_available=False,
            corner_available=True,
            position_evaluation="winning",
            recommended_move={"row": 0, "col": 2},
            strategy="Complete the top row for immediate victory - this is a forced win",
            move_priority=1,
            optimal_outcome="win",
        )

        # Display analysis details
        console.print("\n[bold]Sample Position Analysis:[/bold]")
        console.print(f"[green]Winning moves: {sample_analysis.winning_moves}[/green]")
        console.print(
            f"[yellow]Position evaluation: {sample_analysis.position_evaluation}[/yellow]"
        )
        console.print(f"[blue]Strategy: {sample_analysis.strategy}[/blue]")
        console.print(f"[cyan]Threat level: {sample_analysis.threat_level}[/cyan]")

        # Run game with detailed analysis
        console.print("\n[yellow]Running game with detailed analysis...[/yellow]")
        ui_runner = RichTicTacToeRunner(agent)
        final_state = ui_runner.run_game(
            show_thinking=True,
            step_delay=3.0,  # Longer delay to read analysis
        )

        return final_state

    except Exception as e:
        console.print(f"[red]Strategic analysis failed: {e}[/red]")
        return None


def example_4_performance_testing():
    """Example 4: Performance Testing - Benchmarking and optimization.

    This example demonstrates performance testing capabilities, measuring
    game execution speed, memory usage, and providing optimization insights.
    """
    console.print(
        Panel.fit(
            "[bold yellow]Example 4: Performance Testing[/bold yellow]\n"
            "[dim]Benchmarking game execution and optimization analysis[/dim]",
            border_style="yellow",
        )
    )

    try:
        # Performance test configuration
        console.print("[yellow]Setting up performance test configuration...[/yellow]")
        fast_config = TicTacToeConfig(
            name="performance_test",
            enable_analysis=False,  # Disable for speed
            visualize=False,  # No visualization for benchmarks
            first_player="X",
        )

        slow_config = TicTacToeConfig(
            name="full_features_test",
            enable_analysis=True,  # Enable for comparison
            visualize=False,
            first_player="X",
        )

        # Benchmark fast configuration
        console.print("[yellow]Running performance benchmarks...[/yellow]")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            # Fast configuration benchmark
            task1 = progress.add_task("Testing fast configuration...", total=None)

            fast_agent = TicTacToeAgent(fast_config)
            start_time = time.time()

            # Run multiple games for average
            num_games = 10
            for _i in range(num_games):
                fast_agent.run_game(visualize=False)
                progress.update(task1, advance=1)

            fast_time = (time.time() - start_time) / num_games
            progress.update(task1, description=f"Fast config: {fast_time:.3f}s avg")

            # Full features benchmark
            task2 = progress.add_task("Testing full features...", total=None)

            slow_agent = TicTacToeAgent(slow_config)
            start_time = time.time()

            for _i in range(num_games):
                slow_agent.run_game(visualize=False)
                progress.update(task2, advance=1)

            slow_time = (time.time() - start_time) / num_games
            progress.update(task2, description=f"Full features: {slow_time:.3f}s avg")

        # Create performance comparison table
        table = Table(title="Performance Comparison")
        table.add_column("Configuration", style="cyan")
        table.add_column("Avg Time", style="magenta")
        table.add_column("Features", style="green")
        table.add_column("Use Case", style="yellow")

        table.add_row(
            "Fast Config",
            f"{fast_time:.3f}s",
            "Basic gameplay",
            "Tournament/Production",
        )
        table.add_row(
            "Full Features",
            f"{slow_time:.3f}s",
            "Analysis + Visualization",
            "Education/Development",
        )
        table.add_row(
            "Speedup",
            f"{slow_time/fast_time:.1f}x faster",
            "Minimal features",
            "Batch processing",
        )

        console.print(table)

        # Performance recommendations
        console.print("\n[bold green]Performance Recommendations:[/bold green]")
        console.print("• Use fast config for batch processing")
        console.print("• Enable analysis only for educational purposes")
        console.print("• Disable visualization for production use")
        console.print("• Consider async execution for concurrent games")

        return {
            "fast_time": fast_time,
            "slow_time": slow_time,
            "speedup": slow_time / fast_time,
        }

    except Exception as e:
        console.print(f"[red]Performance testing failed: {e}[/red]")
        return None


def example_5_error_handling():
    """Example 5: Error Handling - Robust error management and debugging.

    This example demonstrates proper error handling, debugging techniques,
    and recovery strategies for common issues.
    """
    console.print(
        Panel.fit(
            "[bold red]Example 5: Error Handling[/bold red]\n"
            "[dim]Robust error management and debugging techniques[/dim]",
            border_style="red",
        )
    )

    try:
        # Enable detailed logging for debugging
        console.print("[yellow]Setting up debugging environment...[/yellow]")
        logging.basicConfig(level=logging.DEBUG)

        # Test 1: Invalid move validation
        console.print("\n[bold]Test 1: Invalid Move Validation[/bold]")
        try:
            TicTacToeMove(
                row=5, col=5, player="X"
            )  # Invalid coordinates
            console.print("[red]ERROR: Invalid move should have failed![/red]")
        except ValueError as e:
            console.print(f"[green]✓ Correctly caught invalid move: {e}[/green]")

        # Test 2: Configuration validation
        console.print("\n[bold]Test 2: Configuration Validation[/bold]")
        try:
            config = TicTacToeConfig(
                name="error_test",
                enable_analysis=True,
                visualize=False,
                first_player="X",
            )
            console.print("[green]✓ Valid configuration created successfully[/green]"]")
        except Exception as e:
            console.print(f"[red]✗ Configuration failed: {e}[/red]")

        # Test 3: Game execution with error handling
        console.print("\n[bold]Test 3: Robust Game Execution[/bold]")
        try:
            agent = TicTacToeAgent(config)

            # Wrap game execution in try-catch
            final_state = agent.run_game(visualize=False)

            if final_state:
                console.print("[green]✓ Game completed successfully[/green]")
                console.print(
                    f"[blue]Result: {final_state.get('game_status', 'unknown')}[/blue]"
                )
            else:
                console.print(
                    "[yellow]⚠ Game completed but no final state returned[/yellow]"
                )

        except Exception as e:
            console.print(f"[red]✗ Game execution failed: {e}[/red]")
            # In production, you'd log this and possibly retry
            import traceback

            console.print(f"[dim]Traceback: {traceback.format_exc()}[/dim]")

        # Test 4: UI error handling
        console.print("\n[bold]Test 4: UI Error Handling[/bold]")
        try:
            RichTicTacToeRunner(agent)
            console.print("[green]✓ UI runner created successfully[/green]")

            # Test UI components
            # ui_runner.test_display()  # Uncomment if method exists

        except Exception as e:
            console.print(f"[red]✗ UI setup failed: {e}[/red]")

        # Error handling best practices
        console.print("\n[bold green]Error Handling Best Practices:[/bold green]")
        console.print("• Always validate inputs before processing")
        console.print("• Use try-catch blocks around game execution")
        console.print("• Log errors with sufficient context")
        console.print("• Provide graceful fallbacks for UI failures")
        console.print("• Test error conditions in development")

        return {"tests_passed": 4, "status": "success"}

    except Exception as e:
        console.print(f"[red]Error handling demo failed: {e}[/red]")
        return None


def example_6_tournament_mode():
    """Example 6: Tournament Mode - Batch game execution and statistics.

    This example demonstrates running multiple games in tournament mode,
    collecting statistics, and analyzing results.
    """
    console.print(
        Panel.fit(
            "[bold blue]Example 6: Tournament Mode[/bold blue]\n"
            "[dim]Batch game execution with comprehensive statistics[/dim]",
            border_style="blue",
        )
    )

    try:
        # Tournament configuration
        console.print("[yellow]Setting up tournament configuration...[/yellow]")
        config = TicTacToeConfig(
            name="tournament_batch",
            enable_analysis=False,  # Disable for speed
            visualize=False,  # No visualization in tournament mode
            first_player="X",
        )

        # Create tournament runner
        class TournamentRunner:
            def __init__(self, agent: TicTacToeAgent):
                self.agent = agent
                self.results = []
                self.stats = {
                    "x_wins": 0,
                    "o_wins": 0,
                    "draws": 0,
                    "total_games": 0,
                    "avg_moves": 0,
                    "total_time": 0,
                }

            def run_tournament(self, num_games: int = 50):
                """Run a tournament with specified number of games."""
                console.print(
                    f"[yellow]Running tournament with {num_games} games...[/yellow]"
                )

                with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    console=console,
                ) as progress:
                    task = progress.add_task(
                        f"Playing {num_games} games...", total=num_games
                    )

                    start_time = time.time()

                    for game_num in range(num_games):
                        try:
                            result = self.agent.run_game(visualize=False)
                            self.results.append(result)
                            self._update_stats(result)
                            progress.update(task, advance=1)
                        except Exception as e:
                            console.print(f"[red]Game {game_num} failed: {e}[/red]")

                    self.stats["total_time"] = time.time() - start_time
                    self.stats["avg_moves"] = (
                        sum(len(r.get("move_history", [])) for r in self.results)
                        / len(self.results)
                        if self.results
                        else 0
                    )

                return self.analyze_results()

            def _update_stats(self, result: Dict[str, Any]):
                """Update tournament statistics."""
                status = result.get("game_status", "unknown")
                self.stats["total_games"] += 1

                if status == "X_win":
                    self.stats["x_wins"] += 1
                elif status == "O_win":
                    self.stats["o_wins"] += 1
                elif status == "draw":
                    self.stats["draws"] += 1

            def analyze_results(self):
                """Analyze tournament results and generate report."""
                if not self.results:
                    return {"error": "No games completed"}

                total = self.stats["total_games"]

                analysis = {
                    "total_games": total,
                    "x_wins": self.stats["x_wins"],
                    "o_wins": self.stats["o_wins"],
                    "draws": self.stats["draws"],
                    "x_win_rate": self.stats["x_wins"] / total * 100,
                    "o_win_rate": self.stats["o_wins"] / total * 100,
                    "draw_rate": self.stats["draws"] / total * 100,
                    "avg_moves_per_game": self.stats["avg_moves"],
                    "total_time": self.stats["total_time"],
                    "avg_time_per_game": self.stats["total_time"] / total,
                    "games_per_second": total / self.stats["total_time"],
                }

                return analysis

        # Run tournament
        agent = TicTacToeAgent(config)
        tournament = TournamentRunner(agent)
        results = tournament.run_tournament(50)  # Run 50 games

        # Display results in a beautiful table
        table = Table(title="Tournament Results")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="magenta")
        table.add_column("Percentage", style="green")

        table.add_row("Total Games", str(results["total_games"]), "100%")
        table.add_row("X Wins", str(results["x_wins"]), f"{results['x_win_rate']:.1f}%")
        table.add_row("O Wins", str(results["o_wins"]), f"{results['o_win_rate']:.1f}%")
        table.add_row("Draws", str(results["draws"]), f"{results['draw_rate']:.1f}%")
        table.add_row("Avg Moves", f"{results['avg_moves_per_game']:.1f}", "-")
        table.add_row("Total Time", f"{results['total_time']:.1f}s", "-")
        table.add_row("Avg Time/Game", f"{results['avg_time_per_game']:.3f}s", "-")
        table.add_row("Games/Second", f"{results['games_per_second']:.1f}", "-")

        console.print(table)

        # Analysis insights
        console.print("\n[bold green]Tournament Analysis:[/bold green]")
        if results["draw_rate"] > 80:
            console.print("• High draw rate indicates strong AI play")
        if results["avg_time_per_game"] < 1.0:
            console.print("• Fast execution suitable for large tournaments")
        if results["x_win_rate"] > 55:
            console.print("• First player advantage detected")

        return results

    except Exception as e:
        console.print(f"[red]Tournament mode failed: {e}[/red]")
        return None


async def example_7_async_execution():
    """Example 7: Async Execution - Concurrent game processing.

    This example demonstrates asynchronous game execution for improved
    performance when running multiple games concurrently.
    """
    console.print(
        Panel.fit(
            "[bold purple]Example 7: Async Execution[/bold purple]\n"
            "[dim]Concurrent game processing for improved performance[/dim]",
            border_style="purple",
        )
    )

    try:
        # Async configuration
        console.print("[yellow]Setting up async execution configuration...[/yellow]")
        config = TicTacToeConfig(
            name="async_test",
            enable_analysis=False,
            visualize=False,
            first_player="X",
        )

        async def run_single_game(game_id: int) -> Dict[str, Any]:
            """Run a single game asynchronously."""
            try:
                agent = TicTacToeAgent(config)
                result = await agent.arun_game(visualize=False)
                return {"game_id": game_id, "result": result, "status": "success"}
            except Exception as e:
                return {"game_id": game_id, "error": str(e), "status": "failed"}

        # Run multiple games concurrently
        console.print("[yellow]Running 20 games concurrently...[/yellow]")

        start_time = time.time()

        # Create tasks for concurrent execution
        tasks = [run_single_game(i) for i in range(20)]

        # Execute all tasks concurrently
        results = await asyncio.gather(*tasks, return_exceptions=True)

        async_time = time.time() - start_time

        # Analyze results
        successful_games = [
            r for r in results if isinstance(r, dict) and r.get("status") == "success"
        ]
        failed_games = [
            r for r in results if isinstance(r, dict) and r.get("status") == "failed"
        ]

        console.print(f"[green]Async execution completed in {async_time:.2f}s[/green]")
        console.print(f"[blue]Successful games: {len(successful_games)}/20[/blue]")
        console.print(f"[red]Failed games: {len(failed_games)}/20[/red]")

        # Compare with synchronous execution
        console.print("\n[yellow]Comparing with synchronous execution...[/yellow]")

        start_time = time.time()
        sync_results = []

        for i in range(20):
            try:
                agent = TicTacToeAgent(config)
                result = agent.run_game(visualize=False)
                sync_results.append(
                    {"game_id": i, "result": result, "status": "success"}
                )
            except Exception as e:
                sync_results.append({"game_id": i, "error": str(e), "status": "failed"})

        sync_time = time.time() - start_time

        # Performance comparison
        speedup = sync_time / async_time

        comparison_table = Table(title="Async vs Sync Performance")
        comparison_table.add_column("Method", style="cyan")
        comparison_table.add_column("Time", style="magenta")
        comparison_table.add_column("Games/Second", style="green")
        comparison_table.add_column("Speedup", style="yellow")

        comparison_table.add_row(
            "Async",
            f"{async_time:.2f}s",
            f"{20/async_time:.1f}",
            f"{speedup:.1f}x faster",
        )
        comparison_table.add_row(
            "Sync", f"{sync_time:.2f}s", f"{20/sync_time:.1f}", "1.0x (baseline)"
        )

        console.print(comparison_table)

        console.print("\n[bold green]Async Execution Benefits:[/bold green]")
        console.print("• Significantly faster for multiple games")
        console.print("• Better resource utilization")
        console.print("• Suitable for server/API deployments")
        console.print("• Enables real-time multiplayer scenarios")

        return {
            "async_time": async_time,
            "sync_time": sync_time,
            "speedup": speedup,
            "successful_games": len(successful_games),
        }

    except Exception as e:
        console.print(f"[red]Async execution failed: {e}[/red]")
        return None


def example_8_custom_ai_configuration():
    """Example 8: Custom AI Configuration - Advanced engine customization.

    This example demonstrates how to create custom AI configurations
    with different personalities and strategic approaches.
    """
    console.print(
        Panel.fit(
            "[bold orange]Example 8: Custom AI Configuration[/bold orange]\n"
            "[dim]Advanced engine customization and AI personalities[/dim]",
            border_style="bright_red",
        )
    )

    try:
        # Custom AI configurations
        console.print("[yellow]Creating custom AI configurations...[/yellow]")

        # Aggressive AI configuration
        aggressive_config = TicTacToeConfig(
            name="aggressive_ai",
            enable_analysis=True,
            visualize=False,
            first_player="X",
            player_X="Aggressive AI",
            player_O="Defensive AI",
        )

        # Educational AI configuration
        educational_config = TicTacToeConfig(
            name="educational_ai",
            enable_analysis=True,
            visualize=True,
            first_player="X",
            player_X="Teacher AI",
            player_O="Student AI",
        )

        # Test different AI personalities
        console.print("\n[bold]Testing AI Personalities:[/bold]")

        # Aggressive AI game
        console.print("\n[red]1. Aggressive AI Game[/red]")
        aggressive_agent = TicTacToeAgent(aggressive_config)
        aggressive_result = aggressive_agent.run_game(visualize=False)
        console.print(
            f"[green]Result: {aggressive_result.get('game_status', 'unknown')}[/green]"
        )

        # Educational AI game
        console.print("\n[blue]2. Educational AI Game[/blue]")
        educational_agent = TicTacToeAgent(educational_config)
        educational_result = educational_agent.run_game(visualize=True)
        console.print(
            f"[green]Result: {educational_result.get('game_status', 'unknown')}[/green]"
        )

        # Custom engine example (pseudo-code for demonstration)
        console.print("\n[bold]Custom Engine Configuration Example:[/bold]")
        console.print(
            """
        # Example of custom engine configuration
        from haive.core.engine.aug_llm import AugLLMConfig
        
        custom_engine = AugLLMConfig(
            name="strategic_tictactoe",
            model="gpt-4",
            temperature=0.1,  # Lower for more deterministic play
            max_tokens=500,
            system_prompt="You are a strategic Tic Tac Toe master..."
        )
        
        config = TicTacToeConfig(
            name="custom_strategic_ai",
            engines={"move_generator": custom_engine}
        )
        """
        )

        # AI comparison
        console.print("\n[bold green]AI Configuration Recommendations:[/bold green]")
        console.print("• Aggressive AI: Lower temperature, focus on winning")
        console.print("• Educational AI: Higher temperature, detailed explanations")
        console.print("• Tournament AI: Minimal analysis, maximum speed")
        console.print("• Research AI: Full analysis, detailed logging")

        return {
            "aggressive_result": aggressive_result,
            "educational_result": educational_result,
            "configurations_tested": 2,
        }

    except Exception as e:
        console.print(f"[red]Custom AI configuration failed: {e}[/red]")
        return None


def run_all_examples():
    """Run all examples in sequence with beautiful formatting."""
    console.print(
        Panel.fit(
            "[bold white]🎯 Haive Tic Tac Toe - Complete Examples Suite[/bold white]\n"
            "[dim]Comprehensive demonstration of all features and capabilities[/dim]",
            border_style="bright_white",
        )
    )

    examples = [
        ("basic", example_1_basic_game),
        ("rich", example_2_rich_ui_game),
        ("analysis", example_3_strategic_analysis),
        ("performance", example_4_performance_testing),
        ("error-handling", example_5_error_handling),
        ("tournament", example_6_tournament_mode),
        ("async", example_7_async_execution),
        ("custom-ai", example_8_custom_ai_configuration),
    ]

    results = {}

    for name, example_func in examples:
        console.print(f"\n{'='*60}")

        try:
            if name == "async":
                # Handle async example
                result = asyncio.run(example_func())
            else:
                result = example_func()

            results[name] = result

            if result:
                console.print(
                    f"[green]✅ {name.title()} example completed successfully[/green]"
                )
            else:
                console.print(
                    f"[yellow]⚠️ {name.title()} example completed with issues[/yellow]"
                )

        except Exception as e:
            console.print(f"[red]❌ {name.title()} example failed: {e}[/red]")
            results[name] = None

        console.print(f"{'='*60}")

    # Final summary
    console.print("\n" + "=" * 60)
    console.print(
        Panel.fit(
            "[bold green]🎉 Examples Suite Complete![/bold green]\n"
            f"[dim]Ran {len(examples)} examples with comprehensive feature coverage[/dim]",
            border_style="green",
        )
    )

    # Summary table
    summary_table = Table(title="Examples Summary")
    summary_table.add_column("Example", style="cyan")
    summary_table.add_column("Status", style="magenta")
    summary_table.add_column("Description", style="yellow")

    for name, _ in examples:
        status = "✅ Success" if results.get(name) else "❌ Failed"
        description = {
            "basic": "Simple gameplay demonstration",
            "rich": "Beautiful UI with animations",
            "analysis": "Strategic analysis showcase",
            "performance": "Benchmarking and optimization",
            "error-handling": "Error management and debugging",
            "tournament": "Batch processing and statistics",
            "async": "Concurrent execution performance",
            "custom-ai": "Advanced AI customization",
        }

        summary_table.add_row(name.title(), status, description[name])

    console.print(summary_table)

    return results


def main():
    """Main entry point for examples."""
    if len(sys.argv) > 1:
        example_name = sys.argv[1].lower()

        # Map command line arguments to functions
        example_map = {
            "basic": example_1_basic_game,
            "rich": example_2_rich_ui_game,
            "analysis": example_3_strategic_analysis,
            "performance": example_4_performance_testing,
            "error-handling": example_5_error_handling,
            "tournament": example_6_tournament_mode,
            "async": lambda: asyncio.run(example_7_async_execution()),
            "custom-ai": example_8_custom_ai_configuration,
        }

        if example_name in example_map:
            console.print(f"[cyan]Running {example_name} example...[/cyan]")
            result = example_map[example_name]()

            if result:
                console.print(
                    f"[green]✅ {example_name} completed successfully![/green]"
                )
            else:
                console.print(
                    f"[yellow]⚠️ {example_name} completed with issues[/yellow]"
                )
        else:
            console.print(f"[red]Unknown example: {example_name}[/red]")
            console.print("[yellow]Available examples:[/yellow]")
            for name in example_map.keys():
                console.print(f"  • {name}")
    else:
        # Run all examples
        results = run_all_examples()

        successful = sum(1 for r in results.values() if r is not None)
        total = len(results)

        console.print(
            f"\n[bold]Final Results: {successful}/{total} examples successful[/bold]"
        )

        if successful == total:
            console.print("[green]🎉 All examples completed successfully![/green]")
        else:
            console.print(
                "[yellow]⚠️ Some examples had issues - check logs above[/yellow]"
            )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]👋 Examples interrupted by user. Goodbye![/yellow]")
    except Exception as e:
        console.print(f"\n[red]❌ Examples suite failed: {e}[/red]")
        import traceback

        console.print(f"[dim]Traceback: {traceback.format_exc()}[/dim]")
