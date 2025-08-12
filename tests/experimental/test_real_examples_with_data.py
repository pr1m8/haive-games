#!/usr/bin/env python3
"""Test all game example.py files with comprehensive data collection.

This script runs each game's actual example.py file, captures output, errors,
execution time, and saves detailed results to organized JSON files.
"""

import json
import subprocess
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path
from typing import Any

# Create data directory structure
DATA_DIR = Path(__file__).parent / "real_example_test_data"
DATA_DIR.mkdir(exist_ok=True)

# All discovered example.py files
EXAMPLE_FILES = [
    ("Nim", "src/haive/games/nim/example.py"),
    ("Tic Tac Toe", "src/haive/games/tic_tac_toe/example.py"),
    ("Connect4", "src/haive/games/connect4/example.py"),
    ("Chess", "src/haive/games/chess/example.py"),
    ("Checkers", "src/haive/games/checkers/example.py"),
    ("Reversi", "src/haive/games/reversi/example.py"),
    ("Battleship", "src/haive/games/battleship/example.py"),
    ("Go", "src/haive/games/go/example.py"),
    ("Among Us", "src/haive/games/among_us/example.py"),
    ("Clue", "src/haive/games/clue/example.py"),
    ("Debate", "src/haive/games/debate/example.py"),
    ("Debate V2", "src/haive/games/debate_v2/example.py"),
    ("Dominoes", "src/haive/games/dominoes/example.py"),
    ("Fox and Geese", "src/haive/games/fox_and_geese/example.py"),
    ("Texas Hold'em", "src/haive/games/hold_em/example.py"),
    ("Mafia", "src/haive/games/mafia/example.py"),
    ("Mancala", "src/haive/games/mancala/example.py"),
    ("Mastermind", "src/haive/games/mastermind/example.py"),
    ("Poker", "src/haive/games/poker/example.py"),
    ("Risk", "src/haive/games/risk/example.py"),
    ("Flow Free", "src/haive/games/single_player/flow_free/example.py"),
    ("Wordle", "src/haive/games/single_player/wordle/example.py"),
    ("BS (Bullshit)", "src/haive/games/cards/standard/bs/example.py"),
]


def save_example_results(game_name: str, results: dict[str, Any]) -> None:
    """Save example test results to organized JSON files."""
    # Create game-specific directory
    game_dir = DATA_DIR / game_name.lower().replace(" ", "_").replace("(", "").replace(
        ")", ""
    )
    game_dir.mkdir(exist_ok=True)

    # Save main results
    results_file = game_dir / "example_results.json"
    with open(results_file, "w") as f:
        json.dump(results, f, indent=2, default=str)

    # Save stdout separately if it exists
    if "stdout" in results and results["stdout"]:
        stdout_file = game_dir / "stdout.txt"
        with open(stdout_file, "w") as f:
            f.write(results["stdout"])

    # Save stderr separately if it exists
    if "stderr" in results and results["stderr"]:
        stderr_file = game_dir / "stderr.txt"
        with open(stderr_file, "w") as f:
            f.write(results["stderr"])


def run_example_with_timeout(
    example_path: str, timeout_seconds: int = 30
) -> tuple[int, str, str, float]:
    """Run an example.py file with timeout and capture output."""
    start_time = time.time()

    try:
        # Run with poetry and timeout
        result = subprocess.run(
            ["poetry", "run", "python", example_path],
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )

        end_time = time.time()
        execution_time = end_time - start_time

        return result.returncode, result.stdout, result.stderr, execution_time

    except subprocess.TimeoutExpired:
        end_time = time.time()
        execution_time = end_time - start_time
        return (
            -1,
            "",
            f"Process timed out after {timeout_seconds} seconds",
            execution_time,
        )

    except Exception as e:
        end_time = time.time()
        execution_time = end_time - start_time
        return -2, "", f"Process execution failed: {str(e)}", execution_time


def test_example_with_data_collection(
    game_name: str, example_path: str
) -> dict[str, Any]:
    """Test a game example and collect comprehensive execution data."""
    print(f"\n{'='*80}")
    print(f"🎮 Testing {game_name} Example")
    print(f"{'='*80}")

    start_time = datetime.now()
    results = {
        "game_name": game_name,
        "example_path": example_path,
        "test_timestamp": start_time.isoformat(),
        "success": False,
        "exit_code": None,
        "execution_time_seconds": 0,
        "stdout": "",
        "stderr": "",
        "stdout_lines": 0,
        "stderr_lines": 0,
        "timeout": False,
        "error_details": None,
        "file_exists": False,
        "file_size_bytes": 0,
    }

    try:
        print(f"📁 Example path: {example_path}")
        print(f"⏰ Started at: {start_time}")

        # Check if file exists
        file_path = Path(example_path)
        if file_path.exists():
            results["file_exists"] = True
            results["file_size_bytes"] = file_path.stat().st_size
            print(f"📄 File size: {results['file_size_bytes']} bytes")
        else:
            print(f"❌ File does not exist: {example_path}")
            results["error_details"] = f"File not found: {example_path}"
            return results

        # Run the example
        print("🚀 Running example...")
        exit_code, stdout, stderr, execution_time = run_example_with_timeout(
            example_path, timeout_seconds=45
        )

        end_time = datetime.now()

        # Process results
        results.update(
            {
                "exit_code": exit_code,
                "execution_time_seconds": execution_time,
                "stdout": stdout,
                "stderr": stderr,
                "stdout_lines": len(stdout.splitlines()) if stdout else 0,
                "stderr_lines": len(stderr.splitlines()) if stderr else 0,
                "timeout": exit_code == -1,
                "end_timestamp": end_time.isoformat(),
            }
        )

        # Determine success
        if exit_code == 0:
            results["success"] = True
            print(f"✅ {game_name}: SUCCESS")
            print(f"⚡ Execution time: {execution_time:.3f}s")
            print(
                f"📊 Output lines: {results['stdout_lines']} stdout, {results['stderr_lines']} stderr"
            )

            # Show first few lines of output
            if stdout:
                lines = stdout.splitlines()[:3]
                for line in lines:
                    print(f"   📝 {line[:100]}{'...' if len(line) > 100 else ''}")

        elif exit_code == -1:
            print(f"⏱️ {game_name}: TIMEOUT (45s)")
            print(f"⚡ Execution time: {execution_time:.3f}s")

        else:
            print(f"❌ {game_name}: FAILED (exit code {exit_code})")
            print(f"⚡ Execution time: {execution_time:.3f}s")

            # Show error details
            if stderr:
                error_lines = stderr.splitlines()[:5]
                for line in error_lines:
                    print(f"   ❌ {line[:100]}{'...' if len(line) > 100 else ''}")

    except Exception as e:
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()

        error_details = {
            "exception_type": type(e).__name__,
            "exception_message": str(e),
            "traceback": traceback.format_exc(),
            "execution_time_seconds": execution_time,
        }

        results.update(
            {
                "success": False,
                "execution_time_seconds": execution_time,
                "error_details": error_details,
                "end_timestamp": end_time.isoformat(),
            }
        )

        print(f"❌ {game_name}: EXCEPTION - {e}")
        print(f"⏰ Failed after: {execution_time:.3f}s")

    return results


def analyze_output_content(stdout: str, stderr: str) -> dict[str, Any]:
    """Analyze output content for insights."""
    analysis = {
        "contains_error": False,
        "contains_success": False,
        "contains_game_output": False,
        "contains_llm_interaction": False,
        "execution_indicators": [],
        "error_indicators": [],
        "game_specific_indicators": [],
    }

    combined_output = (stdout + "\n" + stderr).lower()

    # Check for common patterns
    if any(
        word in combined_output
        for word in ["error", "exception", "failed", "traceback"]
    ):
        analysis["contains_error"] = True

    if any(
        word in combined_output for word in ["success", "completed", "finished", "✅"]
    ):
        analysis["contains_success"] = True

    if any(
        word in combined_output for word in ["game", "move", "player", "board", "win"]
    ):
        analysis["contains_game_output"] = True

    if any(
        word in combined_output
        for word in ["llm", "openai", "claude", "model", "token"]
    ):
        analysis["contains_llm_interaction"] = True

    # Extract specific indicators
    lines = combined_output.splitlines()
    for line in lines:
        if "running" in line or "starting" in line:
            analysis["execution_indicators"].append(line.strip()[:100])
        if "error" in line or "exception" in line:
            analysis["error_indicators"].append(line.strip()[:100])
        if any(word in line for word in ["move", "position", "board", "score"]):
            analysis["game_specific_indicators"].append(line.strip()[:100])

    return analysis


def main():
    """Run comprehensive example testing with data collection."""
    print("🎮 HAIVE GAMES - REAL EXAMPLE.PY TESTING WITH DATA COLLECTION")
    print("=" * 80)
    print(f"📁 Data will be saved to: {DATA_DIR}")
    print("Testing all game example.py files with real execution...")

    # Run all tests and collect data
    all_results = []
    successful_examples = []
    failed_examples = []
    timeout_examples = []

    for game_name, example_path in EXAMPLE_FILES:
        results = test_example_with_data_collection(game_name, example_path)

        # Add content analysis
        if results.get("stdout") or results.get("stderr"):
            content_analysis = analyze_output_content(
                results.get("stdout", ""), results.get("stderr", "")
            )
            results["content_analysis"] = content_analysis

        # Save individual example results
        save_example_results(game_name, results)

        all_results.append(results)

        if results["success"]:
            successful_examples.append(game_name)
        elif results.get("timeout"):
            timeout_examples.append(game_name)
        else:
            failed_examples.append(game_name)

    # Create comprehensive summary
    summary = {
        "test_run_summary": {
            "timestamp": datetime.now().isoformat(),
            "total_examples": len(EXAMPLE_FILES),
            "successful_examples": len(successful_examples),
            "failed_examples": len(failed_examples),
            "timeout_examples": len(timeout_examples),
            "success_rate": len(successful_examples) / len(EXAMPLE_FILES) * 100,
            "successful_example_list": successful_examples,
            "failed_example_list": failed_examples,
            "timeout_example_list": timeout_examples,
        },
        "execution_statistics": {
            "total_execution_time": sum(
                r["execution_time_seconds"] for r in all_results
            ),
            "average_execution_time": sum(
                r["execution_time_seconds"] for r in all_results
            )
            / len(all_results),
            "fastest_example": min(
                all_results, key=lambda x: x["execution_time_seconds"]
            )["game_name"],
            "slowest_example": max(
                all_results, key=lambda x: x["execution_time_seconds"]
            )["game_name"],
            "total_stdout_lines": sum(r.get("stdout_lines", 0) for r in all_results),
            "total_stderr_lines": sum(r.get("stderr_lines", 0) for r in all_results),
        },
        "detailed_results": all_results,
    }

    # Save master summary
    summary_file = DATA_DIR / "example_test_summary.json"
    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=2, default=str)

    # Print final summary
    print(f"\n{'='*80}")
    print("📊 COMPREHENSIVE EXAMPLE TEST SUMMARY")
    print("=" * 80)

    print("\n📈 Results:")
    print(f"   Total Examples: {len(EXAMPLE_FILES)}")
    print(f"   Successful: {len(successful_examples)}")
    print(f"   Failed: {len(failed_examples)}")
    print(f"   Timeouts: {len(timeout_examples)}")
    print(f"   Success Rate: {len(successful_examples)/len(EXAMPLE_FILES)*100:.1f}%")

    print("\n⚡ Execution Statistics:")
    print(
        f"   Total execution time: {summary['execution_statistics']['total_execution_time']:.1f}s"
    )
    print(
        f"   Average time per example: {summary['execution_statistics']['average_execution_time']:.1f}s"
    )
    print(f"   Fastest: {summary['execution_statistics']['fastest_example']}")
    print(f"   Slowest: {summary['execution_statistics']['slowest_example']}")

    print("\n📄 Output Statistics:")
    print(
        f"   Total stdout lines: {summary['execution_statistics']['total_stdout_lines']}"
    )
    print(
        f"   Total stderr lines: {summary['execution_statistics']['total_stderr_lines']}"
    )

    if successful_examples:
        print("\n✅ Successful Examples:")
        for i, game in enumerate(successful_examples, 1):
            execution_time = next(
                r["execution_time_seconds"]
                for r in all_results
                if r["game_name"] == game
            )
            print(f"   {i:2d}. {game:<20} ({execution_time:.3f}s)")

    if timeout_examples:
        print("\n⏱️ Timeout Examples:")
        for i, game in enumerate(timeout_examples, 1):
            print(f"   {i:2d}. {game}")

    if failed_examples:
        print("\n❌ Failed Examples:")
        for i, game in enumerate(failed_examples, 1):
            result = next(r for r in all_results if r["game_name"] == game)
            exit_code = result.get("exit_code", "unknown")
            print(f"   {i:2d}. {game:<20} (exit code: {exit_code})")

    print("\n📂 Individual example data saved:")
    for result in all_results:
        game_dir = (
            result["game_name"]
            .lower()
            .replace(" ", "_")
            .replace("(", "")
            .replace(")", "")
        )
        status_icon = (
            "✅" if result["success"] else "⏱️" if result.get("timeout") else "❌"
        )
        print(f"   {status_icon} {game_dir}/ - {result['game_name']}")

    # Show examples that need attention
    if failed_examples or timeout_examples:
        print("\n🔧 Examples Needing Attention:")
        for game in failed_examples + timeout_examples:
            result = next(r for r in all_results if r["game_name"] == game)
            issue = (
                "timeout"
                if result.get("timeout")
                else f"exit code {result.get('exit_code')}"
            )
            print(f"   🔍 {game}: {issue}")

    return len(failed_examples) + len(timeout_examples) == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
