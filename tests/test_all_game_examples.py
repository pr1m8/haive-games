"""Test all game examples can at least import and initialize."""

import importlib
import subprocess
import sys
import os
import signal
import pytest

os.environ["HAIVE_DEBUG"] = "0"

GAMES = [
    ("among_us", "haive.games.among_us.demo"),
    ("poker", "haive.games.poker.example"),
    ("chess", "haive.games.chess.example"),
    ("nim", "haive.games.nim.example"),
    ("reversi", "haive.games.reversi.example"),
    ("clue", "haive.games.clue.example"),
    ("mafia", "haive.games.mafia.example"),
    ("tic_tac_toe", "haive.games.tic_tac_toe.example"),
    ("connect4", "haive.games.connect4.example"),
    ("checkers", "haive.games.checkers.example"),
    ("go", "haive.games.go.example"),
    ("battleship", "haive.games.battleship.example"),
    ("mancala", "haive.games.mancala.example"),
    ("hold_em", "haive.games.hold_em.example"),
    ("dominoes", "haive.games.dominoes.example"),
    ("risk", "haive.games.risk.example"),
    ("monopoly", "haive.games.monopoly.example"),
    ("fox_and_geese", "haive.games.fox_and_geese.example"),
    ("mastermind", "haive.games.mastermind.example"),
    ("debate", "haive.games.debate.example"),
    ("debate_v2", "haive.games.debate_v2.example"),
    ("debate_v2_judges", "haive.games.debate_v2.example_with_judges"),
]


@pytest.mark.parametrize("game_name,module_path", GAMES, ids=[g[0] for g in GAMES])
def test_game_example_runs(game_name, module_path):
    """Test that each game example can run via subprocess with 60s timeout."""
    result = subprocess.run(
        [sys.executable, "-m", module_path],
        capture_output=True,
        text=True,
        timeout=60,
        env={**os.environ, "HAIVE_DEBUG": "0"},
        cwd="/home/will/Projects/haive",
    )

    # Print output for debugging
    if result.stdout:
        print(f"\n=== {game_name} STDOUT ===")
        print(result.stdout[-2000:] if len(result.stdout) > 2000 else result.stdout)
    if result.stderr:
        print(f"\n=== {game_name} STDERR ===")
        print(result.stderr[-2000:] if len(result.stderr) > 2000 else result.stderr)

    assert result.returncode == 0, f"{game_name} failed with return code {result.returncode}"
