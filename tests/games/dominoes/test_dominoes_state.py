"""Test cases for Dominoes game state.

This module tests the DominoesState class and its properties and methods
for managing the game state and board representation.
"""

from haive.games.dominoes.models import DominoesAnalysis, DominoMove, DominoTile
from haive.games.dominoes.state import DominoesState


class TestDominoesState:
    """Test cases for DominoesState class."""

    def test_dominoes_state_default_creation(self) -> None:
        """Test creating DominoesState with minimal required fields."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [DominoTile(left=3, right=5), DominoTile(left=2, right=4)],
                "player2": [DominoTile(left=1, right=3), DominoTile(left=0, right=2)],
            },
            board=[],
            boneyard=[DominoTile(left=6, right=6)],
            turn="player1",
            game_status="in_progress",
        )

        assert state.players == ["player1", "player2"]
        assert len(state.hands["player1"]) == 2
        assert len(state.hands["player2"]) == 2
        assert state.board == []
        assert len(state.boneyard) == 1
        assert state.turn == "player1"
        assert state.game_status == "in_progress"

    def test_dominoes_state_with_board(self) -> None:
        """Test creating DominoesState with tiles on board."""
        board_tiles = [
            DominoTile(left=3, right=5),
            DominoTile(left=5, right=2),
            DominoTile(left=2, right=6),
        ]

        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=board_tiles,
            boneyard=[],
            turn="player2",
            game_status="in_progress",
        )

        assert len(state.board) == 3
        assert state.board[0].left == 3
        assert state.board[-1].right == 6

    def test_dominoes_state_game_over(self) -> None:
        """Test state when game is over."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[DominoTile(left=3, right=5)],
            boneyard=[],
            turn="player1",
            game_status="player1_win",
            winner="player1",
        )

        assert state.game_status == "player1_win"
        assert state.winner == "player1"

    def test_dominoes_state_with_analysis(self) -> None:
        """Test state with player analysis."""
        analysis = DominoesAnalysis(
            hand_strength=7,
            pip_count_assessment="High",
            open_ends=["3", "5"],
            missing_values=[],
            suggested_strategy="Play doubles",
            blocking_potential="Medium",
            reasoning="Good position",
        )

        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
            player1_analysis=[analysis],
            player2_analysis=[],
        )

        assert len(state.player1_analysis) == 1
        assert state.player1_analysis[0] == analysis

    def test_dominoes_state_with_move_history(self) -> None:
        """Test state with move history."""
        moves = [
            DominoMove(tile=DominoTile(left=3, right=5), end="left"),
            DominoMove(tile=DominoTile(left=5, right=2), end="right"),
            "pass",
        ]

        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[],
            boneyard=[],
            turn="player2",
            game_status="in_progress",
            move_history=moves,
        )

        assert len(state.move_history) == 3
        assert isinstance(state.move_history[0], DominoMove)
        assert state.move_history[2] == "pass"

    def test_is_game_over_in_progress(self) -> None:
        """Test is_game_over when game is ongoing."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [DominoTile(left=3, right=5)], "player2": []},
            board=[],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        assert state.is_game_over is False

    def test_is_game_over_player_win(self) -> None:
        """Test is_game_over when a player wins."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[],
            boneyard=[],
            turn="player1",
            game_status="player2_win",
        )

        assert state.is_game_over is True

    def test_is_game_over_draw(self) -> None:
        """Test is_game_over when game is a draw."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[],
            boneyard=[],
            turn="player1",
            game_status="draw",
        )

        assert state.is_game_over is True

    def test_open_ends_empty_board(self) -> None:
        """Test open_ends property with empty board."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        assert state.open_ends == (None, None)

    def test_open_ends_single_tile(self) -> None:
        """Test open_ends with single tile on board."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[DominoTile(left=3, right=5)],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        assert state.open_ends == (3, 5)

    def test_open_ends_single_double(self) -> None:
        """Test open_ends with single double tile on board."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[DominoTile(left=6, right=6)],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        assert state.open_ends == (6, 6)

    def test_open_ends_multiple_tiles(self) -> None:
        """Test open_ends with multiple tiles on board."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[
                DominoTile(left=3, right=5),
                DominoTile(left=5, right=2),
                DominoTile(left=2, right=6),
            ],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        assert state.open_ends == (3, 6)

    def test_board_string_empty(self) -> None:
        """Test board_string with empty board."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        board_str = state.board_string
        assert "Board: (empty)" in board_str
        assert "Open ends: None" in board_str

    def test_board_string_single_tile(self) -> None:
        """Test board_string with single tile."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[DominoTile(left=3, right=5)],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        board_str = state.board_string
        assert "[3|5]" in board_str
        assert "Open ends: 3 and 5" in board_str

    def test_board_string_multiple_tiles(self) -> None:
        """Test board_string with multiple tiles."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[
                DominoTile(left=3, right=5),
                DominoTile(left=5, right=2),
                DominoTile(left=2, right=6),
            ],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        board_str = state.board_string
        assert "[3|5]-[5|2]-[2|6]" in board_str
        assert "Open ends: 3 and 6" in board_str

    def test_board_string_with_doubles(self) -> None:
        """Test board_string with double tiles."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[DominoTile(left=3, right=3), DominoTile(left=3, right=5)],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        board_str = state.board_string
        assert "[3|3]-[3|5]" in board_str
        assert "Open ends: 3 and 5" in board_str

    def test_state_with_four_players(self) -> None:
        """Test state with four players."""
        state = DominoesState(
            players=["player1", "player2", "player3", "player4"],
            hands={
                "player1": [DominoTile(left=1, right=1)],
                "player2": [DominoTile(left=2, right=2)],
                "player3": [DominoTile(left=3, right=3)],
                "player4": [DominoTile(left=4, right=4)],
            },
            board=[],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        assert len(state.players) == 4
        assert all(player in state.hands for player in state.players)

    def test_state_empty_hands(self) -> None:
        """Test state where all players have empty hands."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[DominoTile(left=3, right=5)],
            boneyard=[],
            turn="player1",
            game_status="draw",
        )

        assert all(len(hand) == 0 for hand in state.hands.values())
        assert state.game_status == "draw"

    def test_state_large_boneyard(self) -> None:
        """Test state with many tiles in boneyard."""
        boneyard_tiles = [
            DominoTile(left=i, right=j) for i in range(7) for j in range(i, 7)
        ]

        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[],
            boneyard=boneyard_tiles,
            turn="player1",
            game_status="in_progress",
        )

        assert len(state.boneyard) == 28  # Standard domino set

    def test_state_serialization(self) -> None:
        """Test serialization and deserialization of DominoesState."""
        move = DominoMove(tile=DominoTile(left=3, right=5), end="left")
        analysis = DominoesAnalysis(
            hand_strength=6,
            pip_count_assessment="Average",
            open_ends=["2", "4"],
            missing_values=[0],
            suggested_strategy="Test",
            blocking_potential="Low",
            reasoning="Test",
        )

        original_state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [DominoTile(left=1, right=2)],
                "player2": [DominoTile(left=3, right=4)],
            },
            board=[DominoTile(left=5, right=6)],
            boneyard=[DominoTile(left=0, right=0)],
            turn="player2",
            game_status="in_progress",
            move_history=[move, "pass"],
            player1_analysis=[analysis],
            winner=None,
        )

        # Serialize to dict
        state_dict = original_state.model_dump()

        # Deserialize from dict
        restored_state = DominoesState(**state_dict)

        assert restored_state.players == original_state.players
        assert len(restored_state.hands["player1"]) == 1
        assert len(restored_state.board) == 1
        assert len(restored_state.move_history) == 2
        assert restored_state.turn == "player2"

    def test_state_game_progression(self) -> None:
        """Test state through a game progression."""
        # Initial state
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [DominoTile(left=3, right=5), DominoTile(left=2, right=4)],
                "player2": [DominoTile(left=5, right=6), DominoTile(left=1, right=3)],
            },
            board=[],
            boneyard=[DominoTile(left=0, right=0)],
            turn="player1",
            game_status="in_progress",
        )

        assert state.open_ends == (None, None)
        assert not state.is_game_over

        # After first move
        state.board.append(DominoTile(left=3, right=5))
        state.hands["player1"].pop(0)
        state.turn = "player2"

        assert state.open_ends == (3, 5)
        assert len(state.hands["player1"]) == 1

        # After second move
        state.board.append(DominoTile(left=5, right=6))
        state.hands["player2"].pop(0)
        state.turn = "player1"

        assert state.open_ends == (3, 6)

        # Player1 wins
        state.hands["player1"] = []
        state.game_status = "player1_win"
        state.winner = "player1"

        assert state.is_game_over is True
        assert state.winner == "player1"

    def test_state_pip_calculations(self) -> None:
        """Test calculations involving pip counts."""
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [
                    DominoTile(left=6, right=6),  # 12 pips
                    DominoTile(left=5, right=4),  # 9 pips
                    DominoTile(left=3, right=2),  # 5 pips
                ],  # Total: 26 pips
                "player2": [
                    DominoTile(left=1, right=1),  # 2 pips
                    DominoTile(left=0, right=3),  # 3 pips
                ],  # Total: 5 pips
            },
            board=[],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        # Calculate pip counts
        player1_pips = sum(tile.left + tile.right for tile in state.hands["player1"])
        player2_pips = sum(tile.left + tile.right for tile in state.hands["player2"])

        assert player1_pips == 26
        assert player2_pips == 5
