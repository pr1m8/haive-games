"""Test cases for Nim game state.

This module tests the NimState class and its properties and methods
for managing the game state and board representation.
"""

from haive.games.nim.models import NimAnalysis, NimMove
from haive.games.nim.state import NimState


class TestNimState:
    """Test cases for NimState class."""

    def test_nim_state_default_creation(self) -> None:
        """Test creating NimState with default values."""
        state = NimState()

        assert state.piles == [3, 5, 7]  # Default pile sizes
        assert state.turn == "player1"
        assert state.game_status == "in_progress"
        assert state.move_history == []
        assert state.player1_analysis == []
        assert state.player2_analysis == []
        assert state.misere_mode is False

    def test_nim_state_custom_creation(self) -> None:
        """Test creating NimState with custom values."""
        custom_piles = [1, 2, 3, 4]
        move = NimMove(pile_index=0, stones_taken=1)
        analysis = NimAnalysis(
            nim_sum=2,
            position_evaluation="winning",
            recommended_move=move,
            explanation="Test analysis",
        )

        state = NimState(
            piles=custom_piles,
            turn="player2",
            game_status="player1_win",
            move_history=[move],
            player1_analysis=[analysis],
            misere_mode=True,
        )

        assert state.piles == custom_piles
        assert state.turn == "player2"
        assert state.game_status == "player1_win"
        assert len(state.move_history) == 1
        assert len(state.player1_analysis) == 1
        assert state.misere_mode is True

    def test_nim_state_empty_piles(self) -> None:
        """Test creating NimState with empty piles."""
        state = NimState(piles=[])

        assert state.piles == []
        assert state.stones_left == 0

    def test_nim_state_single_pile(self) -> None:
        """Test creating NimState with single pile."""
        state = NimState(piles=[10])

        assert state.piles == [10]
        assert state.stones_left == 10
        assert state.nim_sum == 10

    def test_nim_state_zero_piles(self) -> None:
        """Test creating NimState with piles containing zeros."""
        state = NimState(piles=[0, 5, 0, 3])

        assert state.piles == [0, 5, 0, 3]
        assert state.stones_left == 8
        assert state.nim_sum == 6  # 0 XOR 5 XOR 0 XOR 3 = 6

    def test_board_string_default_piles(self) -> None:
        """Test board string representation with default piles."""
        state = NimState()
        board_str = state.board_string

        expected_lines = [
            "Pile 0: O O O ",
            "Pile 1: O O O O O ",
            "Pile 2: O O O O O O O ",
        ]

        lines = board_str.split("\n")
        assert len(lines) == 3
        for i, expected_line in enumerate(expected_lines):
            assert lines[i] == expected_line

    def test_board_string_custom_piles(self) -> None:
        """Test board string representation with custom piles."""
        state = NimState(piles=[1, 4, 2])
        board_str = state.board_string

        expected_lines = [
            "Pile 0: O ",
            "Pile 1: O O O O ",
            "Pile 2: O O ",
        ]

        lines = board_str.split("\n")
        assert len(lines) == 3
        for i, expected_line in enumerate(expected_lines):
            assert lines[i] == expected_line

    def test_board_string_empty_piles(self) -> None:
        """Test board string representation with empty piles."""
        state = NimState(piles=[0, 0, 0])
        board_str = state.board_string

        expected_lines = [
            "Pile 0: ",
            "Pile 1: ",
            "Pile 2: ",
        ]

        lines = board_str.split("\n")
        assert len(lines) == 3
        for i, expected_line in enumerate(expected_lines):
            assert lines[i] == expected_line

    def test_board_string_mixed_piles(self) -> None:
        """Test board string representation with mixed pile sizes."""
        state = NimState(piles=[0, 3, 0, 1, 0])
        board_str = state.board_string

        lines = board_str.split("\n")
        assert len(lines) == 5

        assert lines[0] == "Pile 0: "  # Empty pile
        assert lines[1] == "Pile 1: O O O "  # 3 stones
        assert lines[2] == "Pile 2: "  # Empty pile
        assert lines[3] == "Pile 3: O "  # 1 stone
        assert lines[4] == "Pile 4: "  # Empty pile

    def test_board_string_large_piles(self) -> None:
        """Test board string representation with large piles."""
        state = NimState(piles=[10])
        board_str = state.board_string

        expected = "Pile 0: " + "O " * 10
        assert board_str == expected

    def test_is_game_over_in_progress(self) -> None:
        """Test is_game_over property when game is in progress."""
        state = NimState(game_status="in_progress")

        assert state.is_game_over is False

    def test_is_game_over_player1_win(self) -> None:
        """Test is_game_over property when player1 wins."""
        state = NimState(game_status="player1_win")

        assert state.is_game_over is True

    def test_is_game_over_player2_win(self) -> None:
        """Test is_game_over property when player2 wins."""
        state = NimState(game_status="player2_win")

        assert state.is_game_over is True

    def test_stones_left_default_piles(self) -> None:
        """Test stones_left property with default piles."""
        state = NimState()  # [3, 5, 7]

        assert state.stones_left == 15  # 3 + 5 + 7

    def test_stones_left_custom_piles(self) -> None:
        """Test stones_left property with custom piles."""
        state = NimState(piles=[1, 2, 3, 4, 5])

        assert state.stones_left == 15  # 1 + 2 + 3 + 4 + 5

    def test_stones_left_empty_piles(self) -> None:
        """Test stones_left property with empty piles."""
        state = NimState(piles=[0, 0, 0])

        assert state.stones_left == 0

    def test_stones_left_mixed_piles(self) -> None:
        """Test stones_left property with mixed empty and non-empty piles."""
        state = NimState(piles=[0, 3, 0, 2, 0])

        assert state.stones_left == 5  # 0 + 3 + 0 + 2 + 0

    def test_nim_sum_default_piles(self) -> None:
        """Test nim_sum property with default piles."""
        state = NimState()  # [3, 5, 7]

        # 3 XOR 5 XOR 7 = 1
        assert state.nim_sum == 1

    def test_nim_sum_custom_piles(self) -> None:
        """Test nim_sum property with custom piles."""
        state = NimState(piles=[1, 2, 3])

        # 1 XOR 2 XOR 3 = 0
        assert state.nim_sum == 0

    def test_nim_sum_empty_piles(self) -> None:
        """Test nim_sum property with empty piles."""
        state = NimState(piles=[])

        assert state.nim_sum == 0

    def test_nim_sum_single_pile(self) -> None:
        """Test nim_sum property with single pile."""
        state = NimState(piles=[7])

        assert state.nim_sum == 7

    def test_nim_sum_zero_piles(self) -> None:
        """Test nim_sum property with zero-sized piles."""
        state = NimState(piles=[0, 0, 0])

        assert state.nim_sum == 0

    def test_nim_sum_powers_of_two(self) -> None:
        """Test nim_sum property with powers of two."""
        state = NimState(piles=[1, 2, 4, 8])

        # 1 XOR 2 XOR 4 XOR 8 = 15
        assert state.nim_sum == 15

    def test_nim_sum_identical_pairs(self) -> None:
        """Test nim_sum property with identical pairs."""
        state = NimState(piles=[3, 3, 5, 5])

        # 3 XOR 3 XOR 5 XOR 5 = 0 (identical values cancel out)
        assert state.nim_sum == 0

    def test_nim_sum_calculation_correctness(self) -> None:
        """Test nim_sum calculation with known values."""
        test_cases = [
            ([1, 2], 3),  # 1 XOR 2 = 3
            ([4, 4], 0),  # 4 XOR 4 = 0
            ([1, 2, 3], 0),  # 1 XOR 2 XOR 3 = 0
            ([5, 6, 7], 4),  # 5 XOR 6 XOR 7 = 4
            ([15], 15),  # Single pile
            ([0, 5], 5),  # 0 XOR 5 = 5
        ]

        for piles, expected_nim_sum in test_cases:
            state = NimState(piles=piles)
            assert state.nim_sum == expected_nim_sum, f"Failed for piles {piles}"

    def test_move_history_tracking(self) -> None:
        """Test that move history is properly tracked."""
        move1 = NimMove(pile_index=0, stones_taken=1)
        move2 = NimMove(pile_index=1, stones_taken=2)
        move3 = NimMove(pile_index=2, stones_taken=3)

        state = NimState(move_history=[move1, move2, move3])

        assert len(state.move_history) == 3
        assert state.move_history[0] == move1
        assert state.move_history[1] == move2
        assert state.move_history[2] == move3

    def test_analysis_tracking_player1(self) -> None:
        """Test that player1 analysis is properly tracked."""
        move = NimMove(pile_index=0, stones_taken=1)
        analysis1 = NimAnalysis(
            nim_sum=3,
            position_evaluation="winning",
            recommended_move=move,
            explanation="First analysis",
        )
        analysis2 = NimAnalysis(
            nim_sum=1,
            position_evaluation="losing",
            recommended_move=move,
            explanation="Second analysis",
        )

        state = NimState(player1_analysis=[analysis1, analysis2])

        assert len(state.player1_analysis) == 2
        assert state.player1_analysis[0] == analysis1
        assert state.player1_analysis[1] == analysis2

    def test_analysis_tracking_player2(self) -> None:
        """Test that player2 analysis is properly tracked."""
        move = NimMove(pile_index=1, stones_taken=2)
        analysis = NimAnalysis(
            nim_sum=5,
            position_evaluation="unclear",
            recommended_move=move,
            explanation="Player2 analysis",
        )

        state = NimState(player2_analysis=[analysis])

        assert len(state.player2_analysis) == 1
        assert state.player2_analysis[0] == analysis

    def test_misere_mode_flag(self) -> None:
        """Test misere mode flag."""
        state_normal = NimState(misere_mode=False)
        state_misere = NimState(misere_mode=True)

        assert state_normal.misere_mode is False
        assert state_misere.misere_mode is True

    def test_turn_values(self) -> None:
        """Test valid turn values."""
        state1 = NimState(turn="player1")
        state2 = NimState(turn="player2")

        assert state1.turn == "player1"
        assert state2.turn == "player2"

    def test_game_status_values(self) -> None:
        """Test valid game status values."""
        state1 = NimState(game_status="in_progress")
        state2 = NimState(game_status="player1_win")
        state3 = NimState(game_status="player2_win")

        assert state1.game_status == "in_progress"
        assert state2.game_status == "player1_win"
        assert state3.game_status == "player2_win"

    def test_state_serialization(self) -> None:
        """Test serialization and deserialization of NimState."""
        move = NimMove(pile_index=1, stones_taken=3)
        analysis = NimAnalysis(
            nim_sum=2,
            position_evaluation="winning",
            recommended_move=move,
            explanation="Test serialization",
        )

        original_state = NimState(
            piles=[1, 4, 2],
            turn="player2",
            game_status="in_progress",
            move_history=[move],
            player1_analysis=[analysis],
            misere_mode=True,
        )

        # Serialize to dict
        state_dict = original_state.model_dump()

        # Deserialize from dict
        restored_state = NimState(**state_dict)

        assert restored_state.piles == original_state.piles
        assert restored_state.turn == original_state.turn
        assert restored_state.game_status == original_state.game_status
        assert len(restored_state.move_history) == len(original_state.move_history)
        assert len(restored_state.player1_analysis) == len(
            original_state.player1_analysis
        )
        assert restored_state.misere_mode == original_state.misere_mode

    def test_state_immutability_properties(self) -> None:
        """Test that computed properties don't modify state."""
        original_piles = [3, 5, 7]
        state = NimState(piles=original_piles.copy())

        # Access all properties
        _ = state.board_string
        _ = state.is_game_over
        _ = state.stones_left
        _ = state.nim_sum

        # Piles should remain unchanged
        assert state.piles == original_piles

    def test_large_pile_handling(self) -> None:
        """Test handling of large pile sizes."""
        large_piles = [100, 200, 150]
        state = NimState(piles=large_piles)

        assert state.piles == large_piles
        assert state.stones_left == 450
        assert state.nim_sum == (100 ^ 200 ^ 150)  # XOR calculation

        # Board string should handle large piles (though it would be very long)
        board_str = state.board_string
        assert "Pile 0:" in board_str
        assert "Pile 1:" in board_str
        assert "Pile 2:" in board_str
