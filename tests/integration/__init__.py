"""Module exports."""

from integration.quick_game_test import (
    main,
    save_quick_result,
    test_mastermind,
    test_nim,
    test_tic_tac_toe,
)
from integration.validate_games import main

__all__ = [
    "main",
    "save_quick_result",
    "test_mastermind",
    "test_nim",
    "test_tic_tac_toe",
]
