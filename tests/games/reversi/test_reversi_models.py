"""Tests for Reversi game models."""

import pytest

from haive.games.reversi.models import Position, ReversiAnalysis, ReversiMove


def test_position():
    """Test Position model creation and validation."""
    # Valid position
    pos = Position(row=3, col=4)
    assert pos.row == 3
    assert pos.col == 4

    # Invalid row (too high)
    with pytest.raises(ValueError):
        Position(row=8, col=4)

    # Invalid row (negative)
    with pytest.raises(ValueError):
        Position(row=-1, col=4)

    # Invalid column (too high)
    with pytest.raises(ValueError):
        Position(row=3, col=8)

    # Invalid column (negative)
    with pytest.raises(ValueError):
        Position(row=3, col=-1)


def test_reversi_move():
    """Test ReversiMove model creation and string representation."""
    # Black move
    move_b = ReversiMove(row=2, col=3, player="B")
    assert move_b.row == 2
    assert move_b.col == 3
    assert move_b.player == "B"
    assert "B places at C4" in str(move_b)

    # White move
    move_w = ReversiMove(row=5, col=6, player="W")
    assert move_w.row == 5
    assert move_w.col == 6
    assert move_w.player == "W"
    assert "W places at F7" in str(move_w)

    # Invalid player
    with pytest.raises(ValueError):
        ReversiMove(row=2, col=3, player="X")


def test_reversi_analysis():
    """Test ReversiAnalysis model creation and validation."""
    # Create position objects for recommendations
    pos1 = Position(row=2, col=3)
    pos2 = Position(row=5, col=4)

    # Create position objects for danger zones
    danger1 = Position(row=0, col=1)
    danger2 = Position(row=1, col=0)

    # Create analysis
    analysis = ReversiAnalysis(
        mobility=5,
        frontier_discs=8,
        corner_discs=1,
        stable_discs=4,
        positional_score=10,
        position_evaluation="winning",
        recommended_moves=[pos1, pos2],
        danger_zones=[danger1, danger2],
        strategy="Focus on controlling the corners and edges",
        reasoning="Player has strong corner control and good mobility",
    )

    # Verify fields
    assert analysis.mobility == 5
    assert analysis.frontier_discs == 8
    assert analysis.corner_discs == 1
    assert analysis.stable_discs == 4
    assert analysis.positional_score == 10
    assert analysis.position_evaluation == "winning"
    assert len(analysis.recommended_moves) == 2
    assert analysis.recommended_moves[0].row == 2
    assert analysis.recommended_moves[0].col == 3
    assert analysis.recommended_moves[1].row == 5
    assert analysis.recommended_moves[1].col == 4
    assert len(analysis.danger_zones) == 2
    assert analysis.danger_zones[0].row == 0
    assert analysis.danger_zones[0].col == 1
    assert "Focus on controlling the corners" in analysis.strategy
    assert "Player has strong corner control" in analysis.reasoning

    # Invalid position evaluation
    with pytest.raises(ValueError):
        ReversiAnalysis(
            mobility=5,
            frontier_discs=8,
            corner_discs=1,
            stable_discs=4,
            positional_score=10,
            position_evaluation="dominating",  # not a valid enum value
            recommended_moves=[pos1, pos2],
            danger_zones=[danger1, danger2],
            strategy="Focus on controlling the corners and edges",
            reasoning="Player has strong corner control and good mobility",
        )
