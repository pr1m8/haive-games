#!/usr/bin/env python3
"""Quick diagnostic to identify working vs non-working games."""

import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

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


def quick_test_game(
    game_name: str, example_path: str, timeout: int = 30
) -> dict[str, Any]:
    """Quick test of a single game with short timeout."""
    start_time = time.time()

    result = {
        "game_name": game_name,
        "example_path": example_path,
        "file_exists": Path(example_path).exists(),
        "timeout": timeout,
        "start_time": start_time,
    }

    if not result["file_exists"]:
        result.update(
            {
                "status": "MISSING_FILE",
                "execution_time": time.time() - start_time,
                "error": f"File not found: {example_path}",
            }
        )
        return result

    try:
        # Set environment to disable visualization
        env = os.environ.copy()
        env["HAIVE_DISABLE_VISUALIZATION"] = "1"

        # Run with short timeout
        process = subprocess.run(
            ["poetry", "run", "python", example_path],
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=Path.cwd(),
            env=env,
        )

        execution_time = time.time() - start_time

        # Determine status based on results
        if process.returncode == 0:
            status = "SUCCESS"
        else:
            status = "FAILED"

        # Analyze output to determine if it's a real game
        stdout = process.stdout or ""
        stderr = process.stderr or ""
        combined = stdout + stderr

        # Detect if this is a real game with LLM calls
        has_llm_calls = any(
            indicator in combined.lower()
            for indicator in [
                "engine returned",
                "llm response",
                "ai move",
                "thinking",
                "analysis",
                "move generation",
                "strategy",
                "decision",
                "reasoning",
            ]
        )

        # Detect game completion indicators
        game_completed = any(
            indicator in combined.lower()
            for indicator in [
                "winner",
                "game over",
                "final score",
                "victory",
                "defeat",
                "draw",
                "tie",
                "match complete",
                "game finished",
            ]
        )

        # Estimate actual game depth
        move_count = combined.lower().count("move") + combined.lower().count("turn")

        # Classify the type of test
        if execution_time < 2:
            test_type = "QUICK_TEST"  # Too fast to be real
        elif has_llm_calls and game_completed and move_count >= 5:
            test_type = "FULL_GAME"  # Real complete game
        elif has_llm_calls and move_count >= 2:
            test_type = "PARTIAL_GAME"  # Some LLM gameplay
        elif "agent created" in combined.lower() or "agent ready" in combined.lower():
            test_type = "AGENT_INIT_ONLY"  # Just agent creation test
        else:
            test_type = "BASIC_TEST"  # Just testing game mechanics

        result.update(
            {
                "status": status,
                "exit_code": process.returncode,
                "execution_time": execution_time,
                "stdout_lines": (
                    len(process.stdout.splitlines()) if process.stdout else 0
                ),
                "stderr_lines": (
                    len(process.stderr.splitlines()) if process.stderr else 0
                ),
                "stdout_sample": process.stdout[:300] if process.stdout else "",
                "stderr_sample": process.stderr[:300] if process.stderr else "",
                "test_type": test_type,
                "has_llm_calls": has_llm_calls,
                "game_completed": game_completed,
                "move_count_estimate": move_count,
            }
        )

    except subprocess.TimeoutExpired:
        execution_time = time.time() - start_time
        result.update(
            {
                "status": "TIMEOUT",
                "execution_time": execution_time,
                "error": f"Process timed out after {timeout}s",
            }
        )

    except Exception as e:
        execution_time = time.time() - start_time
        result.update(
            {"status": "ERROR", "execution_time": execution_time, "error": str(e)}
        )

    return result


def main():
    """Test all games and categorize them."""
    print("🔍 IDENTIFYING WORKING VS NON-WORKING GAMES")
    print("=" * 80)
    print(f"⏰ Started at: {datetime.now()}")
    print(f"🎯 Testing {len(GAME_EXAMPLES)} games with 30s timeout each")
    print()

    results = []
    working_games = []
    failed_games = []
    timeout_games = []
    missing_games = []

    # Detailed categorization
    full_games = []
    partial_games = []
    agent_init_only = []
    basic_tests = []
    quick_tests = []

    for i, (game_name, example_path) in enumerate(GAME_EXAMPLES, 1):
        print(f"[{i:2d}/{len(GAME_EXAMPLES)}] Testing {game_name}...", end=" ")
        sys.stdout.flush()

        result = quick_test_game(game_name, example_path)
        results.append(result)

        # Categorize results
        status = result["status"]
        exec_time = result.get("execution_time", 0)

        if status == "SUCCESS":
            working_games.append(result)
            print(f"✅ SUCCESS ({exec_time:.1f}s)")
        elif status == "FAILED":
            failed_games.append(result)
            exit_code = result.get("exit_code", "?")
            print(f"❌ FAILED (exit {exit_code}, {exec_time:.1f}s)")
        elif status == "TIMEOUT":
            timeout_games.append(result)
            print(f"⏱️ TIMEOUT ({exec_time:.1f}s)")
        elif status == "MISSING_FILE":
            missing_games.append(result)
            print("📁 MISSING FILE")
        else:
            failed_games.append(result)
            print(f"❓ {status}")

    # Categorize by test types
    for result in results:
        test_type = result.get("test_type", "UNKNOWN")
        if test_type == "FULL_GAME":
            full_games.append(result)
        elif test_type == "PARTIAL_GAME":
            partial_games.append(result)
        elif test_type == "AGENT_INIT_ONLY":
            agent_init_only.append(result)
        elif test_type == "BASIC_TEST":
            basic_tests.append(result)
        elif test_type == "QUICK_TEST":
            quick_tests.append(result)

    # Summary
    print("\n" + "=" * 80)
    print("📊 GAME STATUS SUMMARY")
    print("=" * 80)

    total = len(results)
    working_count = len(working_games)
    failed_count = len(failed_games)
    timeout_count = len(timeout_games)
    missing_count = len(missing_games)

    print(f"📈 TOTAL GAMES: {total}")
    print(f"✅ WORKING: {working_count} ({working_count/total*100:.1f}%)")
    print(f"❌ FAILED: {failed_count} ({failed_count/total*100:.1f}%)")
    print(f"⏱️ TIMEOUT: {timeout_count} ({timeout_count/total*100:.1f}%)")
    print(f"📁 MISSING: {missing_count} ({missing_count/total*100:.1f}%)")

    print("\n" + "=" * 80)
    print("🎮 GAME DEPTH ANALYSIS")
    print("=" * 80)

    print(
        f"🏆 FULL GAMES (Complete LLM gameplay): {len(full_games)} ({len(full_games)/total*100:.1f}%)"
    )
    print(
        f"⚡ PARTIAL GAMES (Some LLM calls): {len(partial_games)} ({len(partial_games)/total*100:.1f}%)"
    )
    print(
        f"🤖 AGENT INIT ONLY (Just setup): {len(agent_init_only)} ({len(agent_init_only)/total*100:.1f}%)"
    )
    print(
        f"🔧 BASIC TESTS (Mechanics only): {len(basic_tests)} ({len(basic_tests)/total*100:.1f}%)"
    )
    print(
        f"⚡ QUICK TESTS (Too fast): {len(quick_tests)} ({len(quick_tests)/total*100:.1f}%)"
    )

    # Detailed game analysis
    if full_games:
        print(f"\n🏆 FULL GAMES - READY FOR DATA COLLECTION ({len(full_games)}):")
        full_games.sort(key=lambda x: x["execution_time"])
        for game in full_games:
            exec_time = game["execution_time"]
            move_count = game.get("move_count_estimate", 0)
            print(
                f"   • {game['game_name']:20} ({exec_time:5.1f}s, ~{move_count} moves)"
            )

    if partial_games:
        print(f"\n⚡ PARTIAL GAMES - SOME LLM GAMEPLAY ({len(partial_games)}):")
        partial_games.sort(key=lambda x: x["execution_time"])
        for game in partial_games:
            exec_time = game["execution_time"]
            move_count = game.get("move_count_estimate", 0)
            print(
                f"   • {game['game_name']:20} ({exec_time:5.1f}s, ~{move_count} moves)"
            )

    # Working games details (old classification)
    if working_games:
        print(f"\n✅ ALL WORKING GAMES (includes tests) ({len(working_games)}):")
        working_games.sort(key=lambda x: x["execution_time"])
        for game in working_games:
            test_type = game.get("test_type", "UNKNOWN")
            exec_time = game["execution_time"]
            print(f"   • {game['game_name']:20} ({exec_time:5.1f}s) - {test_type}")

    # Failed games details
    if failed_games:
        print(f"\n❌ FAILED GAMES ({len(failed_games)}):")
        for game in failed_games:
            exit_code = game.get("exit_code", "?")
            stderr_preview = game.get("stderr_sample", "")[:50]
            print(f"   • {game['game_name']:20} (exit {exit_code}) - {stderr_preview}")

    # Timeout games details
    if timeout_games:
        print(f"\n⏱️ TIMEOUT GAMES ({len(timeout_games)}):")
        for game in timeout_games:
            print(f"   • {game['game_name']:20} (>{game['timeout']}s)")

    # Missing games
    if missing_games:
        print(f"\n📁 MISSING GAMES ({len(missing_games)}):")
        for game in missing_games:
            print(f"   • {game['game_name']:20} - {game['example_path']}")

    # Save detailed results
    output_file = f"game_status_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, "w") as f:
        json.dump(
            {
                "timestamp": datetime.now().isoformat(),
                "summary": {
                    "total": total,
                    "working": working_count,
                    "failed": failed_count,
                    "timeout": timeout_count,
                    "missing": missing_count,
                },
                "working_games": [g["game_name"] for g in working_games],
                "failed_games": [g["game_name"] for g in failed_games],
                "timeout_games": [g["game_name"] for g in timeout_games],
                "missing_games": [g["game_name"] for g in missing_games],
                "categorized_games": {
                    "full_games": [g["game_name"] for g in full_games],
                    "partial_games": [g["game_name"] for g in partial_games],
                    "agent_init_only": [g["game_name"] for g in agent_init_only],
                    "basic_tests": [g["game_name"] for g in basic_tests],
                    "quick_tests": [g["game_name"] for g in quick_tests],
                },
                "data_collection_ready": [
                    g["game_name"] for g in full_games + partial_games
                ],
                "detailed_results": results,
            },
            f,
            indent=2,
        )

    print(f"\n📄 Detailed report saved to: {output_file}")

    # Recommendations based on actual game depth
    print("\n🎯 DATA COLLECTION RECOMMENDATIONS:")

    full_game_count = len(full_games)
    partial_game_count = len(partial_games)
    real_games = full_game_count + partial_game_count

    if full_game_count >= 5:
        print(
            f"   🏆 EXCELLENT! {full_game_count} full games available - proceed with comprehensive data collection"
        )
        if full_games:
            top_games = [g["game_name"] for g in full_games[:5]]
            print(
                f"   🎯 Recommended games for data collection: {', '.join(top_games)}"
            )
    elif real_games >= 3:
        print(
            f"   ⚡ GOOD! {real_games} games with LLM gameplay - collect data from these"
        )
        if full_games and partial_games:
            games_to_use = [g["game_name"] for g in (full_games + partial_games)[:5]]
            print(f"   🎯 Use these games: {', '.join(games_to_use)}")
    else:
        print(
            f"   ⚠️  CAUTION! Only {real_games} games have real LLM gameplay - limited data collection"
        )
        print(
            "   🔧 Most 'working' games are just testing basic mechanics, not full gameplay"
        )

    # Issue recommendations
    if failed_games:
        print("\n🔧 DEBUG ISSUES:")
        print(
            f"   • Fix failed games: {', '.join([g['game_name'] for g in failed_games[:3]])}"
        )
    if timeout_games:
        print(
            f"   • Check timeout games (may need longer runs): {', '.join([g['game_name'] for g in timeout_games[:2]])}"
        )

    # Classification insights
    quick_test_count = len(quick_tests)
    basic_test_count = len(basic_tests)
    if quick_test_count + basic_test_count > real_games:
        print(
            f"\n💡 INSIGHT: {quick_test_count + basic_test_count} games are just running tests, not full games"
        )
        print(
            "   • This explains why execution times seemed 'too small' - they're not playing complete games!"
        )
        print(
            f"   • For data collection, focus on the {real_games} games with actual LLM gameplay"
        )

    return results


if __name__ == "__main__":
    results = main()
