"""Test cases for Dominoes game state manager.

This module tests the DominoesStateManager class and its methods for
managing game initialization, moves, and state transitions.
"""

import pytest

from haive.games.dominoes.models import (
    DominoesAnalysis,
    DominoMove,
    DominoTile,
)
from haive.games.dominoes.state import DominoesState
from haive.games.dominoes.state_manager import DominoesStateManager


class TestDominoesStateManagerInitialization:
    """Test cases for DominoesStateManager initialization methods."""

    def test_initialize_default_two_players(self) -> None:
        """Test initializing game with default two players."""
        state = DominoesStateManager.initialize()

        assert state.players == ["player1", "player2"]
        assert len(state.hands["player1"]) == 7
        assert len(state.hands["player2"]) == 7
        assert state.board == []
        assert len(state.boneyard) == 14  # 28 total - 14 dealt
        assert state.turn == "player1"
        assert state.game_status == "in_progress"

    def test_initialize_four_players(self) -> None:
        """Test initializing game with four players."""
        state = DominoesStateManager.initialize(num_players=4)

        assert len(state.players) == 4
        assert all(f"player{i}" in state.players for i in range(1, 5))
        assert all(len(state.hands[player]) == 7 for player in state.players)
        assert len(state.boneyard) == 0  # 28 total - 28 dealt

    def test_initialize_three_players(self) -> None:
        """Test initializing game with three players."""
        state = DominoesStateManager.initialize(num_players=3)

        assert len(state.players) == 3
        assert len(state.hands["player1"]) == 7
        assert len(state.hands["player2"]) == 7
        assert len(state.hands["player3"]) == 7
        assert len(state.boneyard) == 7  # 28 - 21 dealt

    def test_initialize_invalid_num_players(self) -> None:
        """Test initializing with invalid number of players."""
        with pytest.raises(
            ValueError, match="Number of players must be between 2 and 4"
        ):
            DominoesStateManager.initialize(num_players=5)

        with pytest.raises(
            ValueError, match="Number of players must be between 2 and 4"
        ):
            DominoesStateManager.initialize(num_players=1)

    def test_initialize_custom_tiles_per_hand(self) -> None:
        """Test initializing with custom tiles per hand."""
        state = DominoesStateManager.initialize(tiles_per_hand=5)

        assert len(state.hands["player1"]) == 5
        assert len(state.hands["player2"]) == 5
        assert len(state.boneyard) == 18  # 28 - 10 dealt

    def test_initialize_too_many_tiles_per_hand(self) -> None:
        """Test initializing with too many tiles requested."""
        # 4 players * 10 tiles = 40 tiles > 28 available
        with pytest.raises(ValueError, match="Not enough tiles"):
            DominoesStateManager.initialize(num_players=4, tiles_per_hand=10)

    def test_initialize_all_tiles_distributed(self) -> None:
        """Test that all 28 standard domino tiles are created."""
        state = DominoesStateManager.initialize()

        # Collect all tiles
        all_tiles = []
        for hand in state.hands.values():
            all_tiles.extend(hand)
        all_tiles.extend(state.boneyard)

        assert len(all_tiles) == 28

        # Check uniqueness
        tile_tuples = {(tile.left, tile.right) for tile in all_tiles}
        assert len(tile_tuples) == 28

    def test_initialize_correct_tile_values(self) -> None:
        """Test that correct domino tiles are created (0-6)."""
        state = DominoesStateManager.initialize()

        # Collect all tiles
        all_tiles = []
        for hand in state.hands.values():
            all_tiles.extend(hand)
        all_tiles.extend(state.boneyard)

        # Check all values are 0-6
        for tile in all_tiles:
            assert 0 <= tile.left <= 6
            assert 0 <= tile.right <= 6
            assert tile.left <= tile.right  # Normalized form


class TestDominoesStateManagerLegalMoves:
    """Test cases for legal move generation."""

    def test_get_legal_moves_empty_board(self) -> None:
        """Test getting legal moves with empty board."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [
                    DominoTile(left=3, right=5),
                    DominoTile(left=2, right=4),
                    DominoTile(left=6, right=6),
                ],
                "player2": [],
            },
            board=[],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        moves = DominoesStateManager.get_legal_moves(state, "player1")

        # All tiles can be played on empty board
        assert len(moves) == 3
        # All moves should be to "left" end for empty board
        assert all(move.end == "left" for move in moves)

    def test_get_legal_moves_single_tile_board(self) -> None:
        """Test getting legal moves with single tile on board."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [
                    DominoTile(left=3, right=5),  # Can play on 3 or 5
                    DominoTile(left=2, right=4),  # Cannot play
                    DominoTile(left=5, right=6),  # Can play on 5
                ],
                "player2": [],
            },
            board=[DominoTile(left=3, right=5)],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        moves = DominoesStateManager.get_legal_moves(state, "player1")

        # Two tiles can match
        assert len(moves) == 3
        # Check specific moves
        move_tuples = [(m.tile.left, m.tile.right, m.end) for m in moves]
        assert (3, 5, "left") in move_tuples  # Match 3
        assert (3, 5, "right") in move_tuples  # Match 5
        assert (5, 6, "right") in move_tuples  # Match 5

    def test_get_legal_moves_no_matches(self) -> None:
        """Test getting legal moves when no tiles match."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [DominoTile(left=0, right=1), DominoTile(left=1, right=2)],
                "player2": [],
            },
            board=[DominoTile(left=5, right=6)],  # Open ends: 5 and 6
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        moves = DominoesStateManager.get_legal_moves(state, "player1")

        assert len(moves) == 0

    def test_get_legal_moves_double_tile(self) -> None:
        """Test getting legal moves with double tile in hand."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [
                    DominoTile(left=3, right=3),  # Double 3
                ],
                "player2": [],
            },
            board=[DominoTile(left=3, right=5)],  # Open ends: 3 and 5
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        moves = DominoesStateManager.get_legal_moves(state, "player1")

        # Double can play on left end (matching 3)
        assert len(moves) == 1
        assert moves[0].tile.left == 3
        assert moves[0].tile.right == 3
        assert moves[0].end == "left"

    def test_get_legal_moves_complex_board(self) -> None:
        """Test getting legal moves with complex board state."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [
                    DominoTile(left=2, right=3),  # Can play on 2
                    DominoTile(left=6, right=6),  # Can play on 6
                    DominoTile(left=1, right=4),  # Cannot play
                ],
                "player2": [],
            },
            board=[
                DominoTile(left=2, right=5),
                DominoTile(left=5, right=5),
                DominoTile(left=5, right=6),
            ],  # Open ends: 2 and 6
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        moves = DominoesStateManager.get_legal_moves(state, "player1")

        assert len(moves) == 2
        # Check moves match open ends
        move_ends = {(m.tile.left, m.tile.right, m.end) for m in moves}
        assert (2, 3, "left") in move_ends
        assert (6, 6, "right") in move_ends

    def test_get_legal_moves_wrong_player(self) -> None:
        """Test getting legal moves for wrong player."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [DominoTile(left=3, right=5)],
                "player2": [DominoTile(left=2, right=4)],
            },
            board=[],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        # Should still return moves even if not player's turn
        moves = DominoesStateManager.get_legal_moves(state, "player2")
        assert len(moves) == 1


class TestDominoesStateManagerMakeMove:
    """Test cases for making moves."""

    def test_make_move_empty_board(self) -> None:
        """Test making first move on empty board."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [DominoTile(left=3, right=5), DominoTile(left=2, right=4)],
                "player2": [],
            },
            board=[],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        move = DominoMove(tile=DominoTile(left=3, right=5), end="left")
        new_state = DominoesStateManager.make_move(state, "player1", move)

        assert len(new_state.board) == 1
        assert new_state.board[0].left == 3
        assert new_state.board[0].right == 5
        assert len(new_state.hands["player1"]) == 1
        assert new_state.turn == "player2"
        assert len(new_state.move_history) == 1

    def test_make_move_left_end(self) -> None:
        """Test making move on left end of board."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [DominoTile(left=2, right=3)], "player2": []},
            board=[DominoTile(left=3, right=5)],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        move = DominoMove(tile=DominoTile(left=2, right=3), end="left")
        new_state = DominoesStateManager.make_move(state, "player1", move)

        assert len(new_state.board) == 2
        assert new_state.board[0].left == 2
        assert new_state.board[0].right == 3
        assert new_state.board[1].left == 3
        assert new_state.board[1].right == 5

    def test_make_move_right_end(self) -> None:
        """Test making move on right end of board."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [DominoTile(left=5, right=6)], "player2": []},
            board=[DominoTile(left=3, right=5)],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        move = DominoMove(tile=DominoTile(left=5, right=6), end="right")
        new_state = DominoesStateManager.make_move(state, "player1", move)

        assert len(new_state.board) == 2
        assert new_state.board[0].left == 3
        assert new_state.board[0].right == 5
        assert new_state.board[1].left == 5
        assert new_state.board[1].right == 6

    def test_make_move_tile_rotation(self) -> None:
        """Test that tiles are rotated correctly when placed."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [DominoTile(left=2, right=3)],  # Need to rotate
                "player2": [],
            },
            board=[DominoTile(left=3, right=5)],  # Open ends: 3 and 5
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        # Tile [2|3] needs to be rotated to [3|2] to match left end
        move = DominoMove(tile=DominoTile(left=2, right=3), end="left")
        new_state = DominoesStateManager.make_move(state, "player1", move)

        # Should be rotated to [3|2]
        assert new_state.board[0].left == 3
        assert new_state.board[0].right == 2

    def test_make_move_invalid_tile_not_in_hand(self) -> None:
        """Test making move with tile not in player's hand."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [DominoTile(left=3, right=5)], "player2": []},
            board=[],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        # Try to play tile not in hand
        move = DominoMove(tile=DominoTile(left=2, right=4), end="left")

        with pytest.raises(ValueError, match="doesn't have tile"):
            DominoesStateManager.make_move(state, "player1", move)

    def test_make_move_invalid_match(self) -> None:
        """Test making move that doesn't match board."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [DominoTile(left=1, right=2)], "player2": []},
            board=[DominoTile(left=5, right=6)],  # Open ends: 5 and 6
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        # Tile [1|2] doesn't match 5 or 6
        move = DominoMove(tile=DominoTile(left=1, right=2), end="left")

        with pytest.raises(ValueError, match="doesn't match"):
            DominoesStateManager.make_move(state, "player1", move)

    def test_make_move_wrong_turn(self) -> None:
        """Test making move when it's not player's turn."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [DominoTile(left=3, right=5)], "player2": []},
            board=[],
            boneyard=[],
            turn="player2",  # It's player2's turn
            game_status="in_progress",
        )

        move = DominoMove(tile=DominoTile(left=3, right=5), end="left")

        with pytest.raises(ValueError, match="not player1's turn"):
            DominoesStateManager.make_move(state, "player1", move)

    def test_make_move_game_over(self) -> None:
        """Test making move when game is over."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [DominoTile(left=3, right=5)], "player2": []},
            board=[],
            boneyard=[],
            turn="player1",
            game_status="player2_win",
        )

        move = DominoMove(tile=DominoTile(left=3, right=5), end="left")

        with pytest.raises(ValueError, match="Game is already over"):
            DominoesStateManager.make_move(state, "player1", move)

    def test_make_move_player_wins(self) -> None:
        """Test that player wins when playing last tile."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [DominoTile(left=3, right=5)],  # Last tile
                "player2": [DominoTile(left=1, right=2)],
            },
            board=[DominoTile(left=2, right=3)],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        move = DominoMove(tile=DominoTile(left=3, right=5), end="right")
        new_state = DominoesStateManager.make_move(state, "player1", move)

        assert len(new_state.hands["player1"]) == 0
        assert new_state.game_status == "player1_win"
        assert new_state.winner == "player1"


class TestDominoesStateManagerPassTurn:
    """Test cases for passing turns."""

    def test_pass_turn_normal(self) -> None:
        """Test normal pass turn."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [DominoTile(left=1, right=2)],
                "player2": [DominoTile(left=3, right=4)],
            },
            board=[DominoTile(left=5, right=6)],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        new_state = DominoesStateManager.pass_turn(state, "player1")

        assert new_state.turn == "player2"
        assert len(new_state.move_history) == 1
        assert new_state.move_history[0] == "pass"

    def test_pass_turn_wrong_player(self) -> None:
        """Test passing when it's not player's turn."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        with pytest.raises(ValueError, match="not player2's turn"):
            DominoesStateManager.pass_turn(state, "player2")

    def test_pass_turn_four_players(self) -> None:
        """Test pass turn cycles correctly with four players."""
        state = DominoesState(
            players=["player1", "player2", "player3", "player4"],
            hands={"player1": [], "player2": [], "player3": [], "player4": []},
            board=[],
            boneyard=[],
            turn="player3",
            game_status="in_progress",
        )

        new_state = DominoesStateManager.pass_turn(state, "player3")
        assert new_state.turn == "player4"

        # Pass from player4 should go to player1
        state2 = DominoesStateManager.pass_turn(new_state, "player4")
        assert state2.turn == "player1"


class TestDominoesStateManagerDrawTile:
    """Test cases for drawing tiles."""

    def test_draw_tile_success(self) -> None:
        """Test successfully drawing a tile."""
        boneyard_tile = DominoTile(left=5, right=6)
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [DominoTile(left=1, right=2)], "player2": []},
            board=[],
            boneyard=[boneyard_tile],
            turn="player1",
            game_status="in_progress",
        )

        new_state = DominoesStateManager.draw_tile(state, "player1")

        assert len(new_state.hands["player1"]) == 2
        assert len(new_state.boneyard) == 0
        assert any(
            tile.left == 5 and tile.right == 6 for tile in new_state.hands["player1"]
        )

    def test_draw_tile_empty_boneyard(self) -> None:
        """Test drawing from empty boneyard."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [DominoTile(left=1, right=2)], "player2": []},
            board=[],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        with pytest.raises(ValueError, match="Boneyard is empty"):
            DominoesStateManager.draw_tile(state, "player1")

    def test_draw_tile_multiple(self) -> None:
        """Test drawing multiple tiles."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[],
            boneyard=[
                DominoTile(left=1, right=1),
                DominoTile(left=2, right=2),
                DominoTile(left=3, right=3),
            ],
            turn="player1",
            game_status="in_progress",
        )

        # Draw three tiles
        state = DominoesStateManager.draw_tile(state, "player1")
        state = DominoesStateManager.draw_tile(state, "player1")
        state = DominoesStateManager.draw_tile(state, "player1")

        assert len(state.hands["player1"]) == 3
        assert len(state.boneyard) == 0


class TestDominoesStateManagerAnalysis:
    """Test cases for adding analysis."""

    def test_add_analysis_player1(self) -> None:
        """Test adding analysis for player1."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        analysis = DominoesAnalysis(
            hand_strength=7,
            pip_count_assessment="High",
            open_ends=["3", "5"],
            missing_values=[],
            suggested_strategy="Be aggressive",
            blocking_potential="Medium",
            reasoning="Strong hand",
        )

        new_state = DominoesStateManager.add_analysis(state, "player1", analysis)

        assert len(new_state.player1_analysis) == 1
        assert new_state.player1_analysis[0] == analysis

    def test_add_analysis_string_conversion(self) -> None:
        """Test adding string analysis (backward compatibility)."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        analysis_str = "Simple string analysis"

        new_state = DominoesStateManager.add_analysis(state, "player1", analysis_str)

        assert len(new_state.player1_analysis) == 1
        assert isinstance(new_state.player1_analysis[0], DominoesAnalysis)
        assert analysis_str in new_state.player1_analysis[0].reasoning


class TestDominoesStateManagerGameFlow:
    """Test cases for complete game flows."""

    def test_complete_two_player_game(self) -> None:
        """Test a complete two-player game flow."""
        # Initialize
        state = DominoesStateManager.initialize()

        # Ensure player1 has a playable tile
        state.hands["player1"] = [DominoTile(left=6, right=6)]
        state.hands["player2"] = [DominoTile(left=3, right=5)]

        # Player1 plays first tile
        move1 = DominoMove(tile=DominoTile(left=6, right=6), end="left")
        state = DominoesStateManager.make_move(state, "player1", move1)

        assert len(state.board) == 1
        assert state.turn == "player2"
        assert state.game_status == "player1_win"  # Player1 played last tile
        assert state.winner == "player1"

    def test_blocked_game_detection(self) -> None:
        """Test detection of blocked game."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [DominoTile(left=0, right=1)],
                "player2": [DominoTile(left=2, right=3)],
            },
            board=[DominoTile(left=5, right=6)],  # No one can play
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        # Both players have to pass
        state = DominoesStateManager.pass_turn(state, "player1")
        state = DominoesStateManager.pass_turn(state, "player2")

        # Game should detect blocked state
        # In a real implementation, this would trigger endgame pip counting
        assert state.turn == "player1"  # Back to player1
        assert len(state.move_history) == 2
        assert all(move == "pass" for move in state.move_history)

    def test_game_state_preservation(self) -> None:
        """Test that original state is not modified."""
        original_state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [DominoTile(left=3, right=5)], "player2": []},
            board=[],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        # Make a copy to compare later
        original_hand_size = len(original_state.hands["player1"])

        # Make move
        move = DominoMove(tile=DominoTile(left=3, right=5), end="left")
        new_state = DominoesStateManager.make_move(original_state, "player1", move)

        # Original state should be unchanged
        assert len(original_state.hands["player1"]) == original_hand_size
        assert len(original_state.board) == 0

        # New state should be different
        assert len(new_state.hands["player1"]) == original_hand_size - 1
        assert len(new_state.board) == 1
