"""Tests for Tic Tac Toe game models."""

import pytest

from haive.games.tic_tac_toe.models import TicTacToeAnalysis, TicTacToeMove


def test_tic_tac_toe_move():
    """Test TicTacToeMove model creation and string representation."""
    # X move
    move_x = TicTacToeMove(row=0, col=1, player="X")
    assert move_x.row == 0
    assert move_x.col == 1
    assert move_x.player == "X"
    assert "X places at (0, 1)" in str(move_x)

    # O move
    move_o = TicTacToeMove(row=2, col=2, player="O")
    assert move_o.row == 2
    assert move_o.col == 2
    assert move_o.player == "O"
    assert "O places at (2, 2)" in str(move_o)

    # Invalid row (too high)
    with pytest.raises(ValueError):
        TicTacToeMove(row=3, col=1, player="X")

    # Invalid column (too high)
    with pytest.raises(ValueError):
        TicTacToeMove(row=1, col=3, player="X")

    # Invalid player
    with pytest.raises(ValueError):
        TicTacToeMove(row=1, col=1, player="Z")


def test_tic_tac_toe_analysis():
    """Test TicTacToeAnalysis model creation and validation."""
    # Create basic analysis
    analysis = TicTacToeAnalysis(
        winning_moves=[{"row": 0, "col": 0}],
        blocking_moves=[{"row": 2, "col": 0}],
        fork_opportunities=[{"row": 1, "col": 1}],
        center_available=True,
        corner_available=True,
        position_evaluation="winning",
        recommended_move={"row": 0, "col": 0},
        strategy="Go for the win by playing at (0, 0)",
    )

    # Check fields
    assert len(analysis.winning_moves) == 1
    assert analysis.winning_moves[0]["row"] == 0
    assert analysis.winning_moves[0]["col"] == 0

    assert len(analysis.blocking_moves) == 1
    assert analysis.blocking_moves[0]["row"] == 2
    assert analysis.blocking_moves[0]["col"] == 0

    assert len(analysis.fork_opportunities) == 1
    assert analysis.fork_opportunities[0]["row"] == 1
    assert analysis.fork_opportunities[0]["col"] == 1

    assert analysis.center_available is True
    assert analysis.corner_available is True
    assert analysis.position_evaluation == "winning"
    assert analysis.recommended_move["row"] == 0
    assert analysis.recommended_move["col"] == 0
    assert "Go for the win" in analysis.strategy

    # Test with empty lists
    analysis = TicTacToeAnalysis(
        winning_moves=[],
        blocking_moves=[],
        fork_opportunities=[],
        center_available=False,
        corner_available=False,
        position_evaluation="drawing",
        recommended_move=None,
        strategy="Game is heading for a draw",
    )

    assert len(analysis.winning_moves) == 0
    assert len(analysis.blocking_moves) == 0
    assert len(analysis.fork_opportunities) == 0
    assert analysis.center_available is False
    assert analysis.corner_available is False
    assert analysis.position_evaluation == "drawing"
    assert analysis.recommended_move is None
    assert "draw" in analysis.strategy

    # Invalid position evaluation
    with pytest.raises(ValueError):
        TicTacToeAnalysis(
            winning_moves=[],
            blocking_moves=[],
            fork_opportunities=[],
            center_available=False,
            corner_available=False,
            position_evaluation="maybe",  # Invalid value
            recommended_move=None,
            strategy="Game is uncertain",
        )
