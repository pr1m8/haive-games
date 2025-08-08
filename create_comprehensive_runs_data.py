#!/usr/bin/env python3
"""Comprehensive game data collection with runs/ folder structure and real agent execution."""

import json
import os
import subprocess
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

# Create runs directory structure
RUNS_DIR = Path(__file__).parent / "runs"
RUNS_DIR.mkdir(exist_ok=True)

# Current run directory
RUN_TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
CURRENT_RUN = RUNS_DIR / f"run_{RUN_TIMESTAMP}"
CURRENT_RUN.mkdir(exist_ok=True)

# All game examples with their paths
GAME_EXAMPLES = [
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


def create_game_run_directory(game_name: str) -> Path:
    """Create directory for individual game run."""
    safe_name = game_name.lower().replace(" ", "_").replace("(", "").replace(")", "")
    game_dir = CURRENT_RUN / safe_name
    game_dir.mkdir(exist_ok=True)
    return game_dir


def run_game_example_with_timeout(
    example_path: str, timeout_seconds: int = 90, disable_visualization: bool = True
) -> Dict[str, Any]:
    """Run game example with subprocess and capture comprehensive data."""
    start_time = time.time()

    result_data = {
        "example_path": example_path,
        "start_timestamp": datetime.now().isoformat(),
        "timeout_seconds": timeout_seconds,
        "success": False,
        "exit_code": None,
        "execution_time_seconds": 0,
        "stdout": "",
        "stderr": "",
        "stdout_lines": 0,
        "stderr_lines": 0,
        "timeout_occurred": False,
        "process_error": None,
        "file_exists": Path(example_path).exists(),
        "file_size_bytes": (
            0 if not Path(example_path).exists() else Path(example_path).stat().st_size
        ),
    }

    if not result_data["file_exists"]:
        result_data["process_error"] = f"File not found: {example_path}"
        result_data["execution_time_seconds"] = time.time() - start_time
        return result_data

    try:
        print(f"   🚀 Running: {example_path}")
        print(f"   ⏰ Timeout: {timeout_seconds}s")

        # Set environment to disable visualization for data collection
        env = os.environ.copy()
        if disable_visualization:
            env["HAIVE_DISABLE_VISUALIZATION"] = "1"

        # Run with subprocess and timeout
        process = subprocess.run(
            ["poetry", "run", "python", example_path],
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            cwd=Path.cwd(),
            env=env,
        )

        end_time = time.time()

        # Process results
        result_data.update(
            {
                "exit_code": process.returncode,
                "execution_time_seconds": end_time - start_time,
                "stdout": process.stdout,
                "stderr": process.stderr,
                "stdout_lines": (
                    len(process.stdout.splitlines()) if process.stdout else 0
                ),
                "stderr_lines": (
                    len(process.stderr.splitlines()) if process.stderr else 0
                ),
                "success": process.returncode == 0,
                "end_timestamp": datetime.now().isoformat(),
            }
        )

        print(f"   ⚡ Completed in {result_data['execution_time_seconds']:.3f}s")
        print(f"   📊 Exit code: {result_data['exit_code']}")
        print(
            f"   📝 Output: {result_data['stdout_lines']} stdout, {result_data['stderr_lines']} stderr lines"
        )

    except subprocess.TimeoutExpired:
        end_time = time.time()
        result_data.update(
            {
                "timeout_occurred": True,
                "execution_time_seconds": end_time - start_time,
                "process_error": f"Process timed out after {timeout_seconds} seconds",
                "end_timestamp": datetime.now().isoformat(),
            }
        )
        print(f"   ⏱️ TIMEOUT after {result_data['execution_time_seconds']:.3f}s")

    except Exception as e:
        end_time = time.time()
        result_data.update(
            {
                "execution_time_seconds": end_time - start_time,
                "process_error": str(e),
                "end_timestamp": datetime.now().isoformat(),
            }
        )
        print(f"   ❌ ERROR: {e}")

    return result_data


def save_game_run_data(
    game_dir: Path, game_name: str, run_data: Dict[str, Any]
) -> None:
    """Save comprehensive game run data to structured files."""

    # Main run results
    results_file = game_dir / "run_results.json"
    with open(results_file, "w") as f:
        json.dump(run_data, f, indent=2, default=str)

    # Save stdout separately if exists
    if run_data.get("stdout"):
        stdout_file = game_dir / "stdout.txt"
        with open(stdout_file, "w") as f:
            f.write(run_data["stdout"])

    # Save stderr separately if exists
    if run_data.get("stderr"):
        stderr_file = game_dir / "stderr.txt"
        with open(stderr_file, "w") as f:
            f.write(run_data["stderr"])

    # Extract state history from output if possible
    extract_state_history(game_dir, run_data)

    # Analyze output content
    content_analysis = analyze_game_output(
        run_data.get("stdout", ""), run_data.get("stderr", "")
    )

    analysis_file = game_dir / "content_analysis.json"
    with open(analysis_file, "w") as f:
        json.dump(content_analysis, f, indent=2)


def extract_state_history(game_dir: Path, run_data: Dict[str, Any]) -> None:
    """Extract state history and agent execution data from output."""
    stdout = run_data.get("stdout", "")
    stderr = run_data.get("stderr", "")
    combined = stdout + "\n" + stderr

    state_history = []
    agent_execution_data = {
        "agent_ready_detected": "Agent Ready" in combined,
        "graph_compiled": "Graph compiled successfully" in combined,
        "engine_initialization": "Engine Initialization" in combined,
        "llm_api_calls": "DEBUG" in combined and "Engine returned" in combined,
        "move_history": [],
        "game_status_changes": [],
        "error_patterns": [],
    }

    # Extract moves and game states
    lines = combined.split("\n")
    for line in lines:
        if "[DEBUG] Engine returned move:" in line:
            agent_execution_data["move_history"].append(line.strip())
        elif "game_status" in line.lower():
            agent_execution_data["game_status_changes"].append(line.strip())
        elif "error" in line.lower() or "exception" in line.lower():
            agent_execution_data["error_patterns"].append(line.strip())

    # Save state history
    state_file = game_dir / "state_history.json"
    with open(state_file, "w") as f:
        json.dump(agent_execution_data, f, indent=2)


def analyze_game_output(stdout: str, stderr: str) -> Dict[str, Any]:
    """Analyze game output for patterns and insights."""
    combined = (stdout + "\n" + stderr).lower()

    analysis = {
        "execution_patterns": {
            "real_llm_calls": "engine returned" in combined,
            "game_moves_detected": "move" in combined
            and ("x places" in combined or "o places" in combined),
            "agent_initialization": "agent ready" in combined,
            "graph_visualization": "graph compiled" in combined,
            "error_recovery": "error" in combined and "success" in combined,
            "timeout_issues": "timeout" in combined or "recursion limit" in combined,
        },
        "performance_indicators": {
            "postgres_connection": "postgresql connection pool" in combined,
            "engine_status_success": "status ✓" in combined,
            "schema_composition": "schema definitions" in combined,
            "persistence_active": "postgres" in combined and "sync mode" in combined,
        },
        "issue_detection": {
            "hanging_detected": len(stdout) > 5000 and "timeout" in combined,
            "visualization_issues": "mermaid" in combined or "draw" in combined,
            "recursion_errors": "recursion limit" in combined,
            "import_errors": "importerror" in combined
            or "modulenotfounderror" in combined,
            "validation_errors": "validationerror" in combined,
        },
        "game_completion": {
            "winner_detected": "win" in combined or "winner" in combined,
            "game_finished": "completed" in combined or "finished" in combined,
            "moves_count": combined.count("places at"),
            "analysis_performed": "analysis" in combined,
        },
    }

    return analysis


def create_master_run_index(all_results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Create master index for the entire run."""
    successful_runs = [r for r in all_results if r["run_data"]["success"]]
    failed_runs = [r for r in all_results if not r["run_data"]["success"]]
    timeout_runs = [
        r for r in all_results if r["run_data"].get("timeout_occurred", False)
    ]

    master_index = {
        "run_metadata": {
            "run_id": f"run_{RUN_TIMESTAMP}",
            "timestamp": datetime.now().isoformat(),
            "total_games": len(all_results),
            "successful_runs": len(successful_runs),
            "failed_runs": len(failed_runs),
            "timeout_runs": len(timeout_runs),
            "success_rate_percent": (
                (len(successful_runs) / len(all_results)) * 100 if all_results else 0
            ),
        },
        "execution_summary": {
            "total_execution_time": sum(
                r["run_data"]["execution_time_seconds"] for r in all_results
            ),
            "average_execution_time": (
                sum(r["run_data"]["execution_time_seconds"] for r in all_results)
                / len(all_results)
                if all_results
                else 0
            ),
            "fastest_game": (
                min(all_results, key=lambda x: x["run_data"]["execution_time_seconds"])[
                    "game_name"
                ]
                if all_results
                else None
            ),
            "slowest_game": (
                max(all_results, key=lambda x: x["run_data"]["execution_time_seconds"])[
                    "game_name"
                ]
                if all_results
                else None
            ),
        },
        "categorized_results": {
            "successful_games": [r["game_name"] for r in successful_runs],
            "failed_games": [
                {
                    "game": r["game_name"],
                    "reason": r["run_data"].get("process_error", "Unknown"),
                }
                for r in failed_runs
            ],
            "timeout_games": [r["game_name"] for r in timeout_runs],
        },
        "detailed_results": all_results,
    }

    return master_index


def main():
    """Run comprehensive game data collection with runs/ structure."""
    print(f"🎮 COMPREHENSIVE GAME RUNS DATA COLLECTION")
    print(f"=" * 80)
    print(f"📁 Run directory: {CURRENT_RUN}")
    print(f"⏰ Started at: {datetime.now()}")
    print(f"🎯 Testing {len(GAME_EXAMPLES)} games with real agent execution")

    all_results = []

    for i, (game_name, example_path) in enumerate(GAME_EXAMPLES, 1):
        print(f"\n{'='*60}")
        print(f"🎮 [{i:2d}/{len(GAME_EXAMPLES)}] {game_name}")
        print(f"{'='*60}")

        # Create game directory
        game_dir = create_game_run_directory(game_name)
        print(f"📁 Game directory: {game_dir.name}")

        # Run the game example with visualization disabled for data collection
        run_data = run_game_example_with_timeout(
            example_path, timeout_seconds=120, disable_visualization=True
        )  # 2 minute timeout

        # Save comprehensive data
        save_game_run_data(game_dir, game_name, run_data)

        # Track results
        all_results.append(
            {
                "game_name": game_name,
                "example_path": example_path,
                "game_directory": game_dir.name,
                "run_data": run_data,
            }
        )

        # Show immediate results
        if run_data["success"]:
            print(f"   ✅ SUCCESS: {run_data['execution_time_seconds']:.3f}s")
        elif run_data.get("timeout_occurred"):
            print(f"   ⏱️ TIMEOUT: {run_data['execution_time_seconds']:.3f}s")
        else:
            print(f"   ❌ FAILED: {run_data.get('process_error', 'Unknown error')}")

    # Create master index
    print(f"\n{'='*80}")
    print(f"📊 CREATING MASTER RUN INDEX")
    print(f"{'='*80}")

    master_index = create_master_run_index(all_results)

    # Save master index
    master_file = CURRENT_RUN / "master_index.json"
    with open(master_file, "w") as f:
        json.dump(master_index, f, indent=2, default=str)

    # Create summary report
    summary_file = CURRENT_RUN / "SUMMARY.md"
    create_summary_report(summary_file, master_index)

    # Print final results
    print(f"\n🎉 RUN COMPLETED!")
    print(
        f"📊 Results: {master_index['run_metadata']['successful_runs']}/{master_index['run_metadata']['total_games']} successful ({master_index['run_metadata']['success_rate_percent']:.1f}%)"
    )
    print(
        f"⚡ Total time: {master_index['execution_summary']['total_execution_time']:.1f}s"
    )
    print(f"📁 Data saved to: {CURRENT_RUN}")
    print(f"📋 Master index: {master_file}")
    print(f"📄 Summary report: {summary_file}")

    return master_index


def create_summary_report(summary_file: Path, master_index: Dict[str, Any]) -> None:
    """Create markdown summary report."""
    content = f"""# Game Runs Summary Report

**Run ID**: {master_index['run_metadata']['run_id']}  
**Timestamp**: {master_index['run_metadata']['timestamp']}  
**Total Games**: {master_index['run_metadata']['total_games']}

## 📊 Overview

- **Successful**: {master_index['run_metadata']['successful_runs']} games
- **Failed**: {master_index['run_metadata']['failed_runs']} games  
- **Timeouts**: {master_index['run_metadata']['timeout_runs']} games
- **Success Rate**: {master_index['run_metadata']['success_rate_percent']:.1f}%

## ⚡ Performance

- **Total Execution Time**: {master_index['execution_summary']['total_execution_time']:.1f}s
- **Average Time per Game**: {master_index['execution_summary']['average_execution_time']:.1f}s
- **Fastest Game**: {master_index['execution_summary']['fastest_game']}
- **Slowest Game**: {master_index['execution_summary']['slowest_game']}

## ✅ Successful Games

{chr(10).join(f"- {game}" for game in master_index['categorized_results']['successful_games'])}

## ❌ Failed Games

{chr(10).join(f"- **{result['game']}**: {result['reason']}" for result in master_index['categorized_results']['failed_games'])}

## ⏱️ Timeout Games

{chr(10).join(f"- {game}" for game in master_index['categorized_results']['timeout_games'])}

## 📁 Data Structure

```
{master_index['run_metadata']['run_id']}/
├── master_index.json          # Complete run data
├── SUMMARY.md                 # This report
└── [game_name]/               # Individual game directories
    ├── run_results.json       # Game execution results
    ├── state_history.json     # Agent state and execution data
    ├── content_analysis.json  # Output analysis
    ├── stdout.txt            # Game output
    └── stderr.txt            # Error output
```

---
Generated: {datetime.now().isoformat()}
"""

    with open(summary_file, "w") as f:
        f.write(content)


if __name__ == "__main__":
    try:
        results = main()
    except KeyboardInterrupt:
        print(f"\n⏹️  Run interrupted by user")
    except Exception as e:
        print(f"\n❌ Run failed with error: {e}")
        traceback.print_exc()
