"""Test cases for Nim game state manager.

This module tests the NimStateManager class and its methods for
managing game initialization, moves, analysis, and state transitions.
"""

import pytest

from haive.games.nim.models import NimAnalysis, NimMove
from haive.games.nim.state import NimState
from haive.games.nim.state_manager import NimStateManager


class TestNimStateManagerInitialization:
    """Test cases for NimStateManager initialization methods."""

    def test_initialize_default_piles(self) -> None:
        """Test initializing game with default pile sizes."""
        state = NimStateManager.initialize()

        assert state.piles == [3, 5, 7]
        assert state.turn == "player1"
        assert state.game_status == "in_progress"
        assert state.move_history == []
        assert state.player1_analysis == []
        assert state.player2_analysis == []
        assert state.misere_mode is False

    def test_initialize_custom_piles(self) -> None:
        """Test initializing game with custom pile sizes."""
        custom_piles = [1, 2, 3, 4]
        state = NimStateManager.initialize(pile_sizes=custom_piles)

        assert state.piles == custom_piles
        assert state.turn == "player1"
        assert state.game_status == "in_progress"

    def test_initialize_single_pile(self) -> None:
        """Test initializing game with single pile."""
        state = NimStateManager.initialize(pile_sizes=[10])

        assert state.piles == [10]
        assert state.stones_left == 10

    def test_initialize_empty_piles(self) -> None:
        """Test initializing game with empty piles."""
        state = NimStateManager.initialize(pile_sizes=[])

        assert state.piles == []
        assert state.stones_left == 0

    def test_initialize_zero_piles(self) -> None:
        """Test initializing game with zero-sized piles."""
        state = NimStateManager.initialize(pile_sizes=[0, 0, 0])

        assert state.piles == [0, 0, 0]
        assert state.stones_left == 0

    def test_initialize_mixed_piles(self) -> None:
        """Test initializing game with mixed pile sizes."""
        mixed_piles = [0, 5, 0, 3, 0]
        state = NimStateManager.initialize(pile_sizes=mixed_piles)

        assert state.piles == mixed_piles
        assert state.stones_left == 8

    def test_initialize_large_piles(self) -> None:
        """Test initializing game with large pile sizes."""
        large_piles = [100, 200, 150]
        state = NimStateManager.initialize(pile_sizes=large_piles)

        assert state.piles == large_piles
        assert state.stones_left == 450


class TestNimStateManagerLegalMoves:
    """Test cases for NimStateManager legal move generation."""

    def test_get_legal_moves_default_piles(self) -> None:
        """Test getting legal moves with default piles."""
        state = NimState(piles=[3, 5, 7])
        legal_moves = NimStateManager.get_legal_moves(state)

        # Should have 3 + 5 + 7 = 15 legal moves
        assert len(legal_moves) == 15

        # Check pile 0 moves
        pile_0_moves = [move for move in legal_moves if move.pile_index == 0]
        assert len(pile_0_moves) == 3
        assert all(move.stones_taken in [1, 2, 3] for move in pile_0_moves)

        # Check pile 1 moves
        pile_1_moves = [move for move in legal_moves if move.pile_index == 1]
        assert len(pile_1_moves) == 5
        assert all(move.stones_taken in [1, 2, 3, 4, 5] for move in pile_1_moves)

        # Check pile 2 moves
        pile_2_moves = [move for move in legal_moves if move.pile_index == 2]
        assert len(pile_2_moves) == 7
        assert all(move.stones_taken in range(1, 8) for move in pile_2_moves)

    def test_get_legal_moves_empty_piles(self) -> None:
        """Test getting legal moves with empty piles."""
        state = NimState(piles=[0, 0, 0])
        legal_moves = NimStateManager.get_legal_moves(state)

        assert len(legal_moves) == 0

    def test_get_legal_moves_single_pile(self) -> None:
        """Test getting legal moves with single pile."""
        state = NimState(piles=[5])
        legal_moves = NimStateManager.get_legal_moves(state)

        assert len(legal_moves) == 5
        assert all(move.pile_index == 0 for move in legal_moves)
        assert all(move.stones_taken in [1, 2, 3, 4, 5] for move in legal_moves)

    def test_get_legal_moves_mixed_piles(self) -> None:
        """Test getting legal moves with mixed empty and non-empty piles."""
        state = NimState(piles=[0, 3, 0, 2, 0])
        legal_moves = NimStateManager.get_legal_moves(state)

        # Should have 3 + 2 = 5 legal moves
        assert len(legal_moves) == 5

        # Check that no moves are generated for empty piles
        pile_indices = {move.pile_index for move in legal_moves}
        assert pile_indices == {1, 3}

        # Check pile 1 moves (3 stones)
        pile_1_moves = [move for move in legal_moves if move.pile_index == 1]
        assert len(pile_1_moves) == 3

        # Check pile 3 moves (2 stones)
        pile_3_moves = [move for move in legal_moves if move.pile_index == 3]
        assert len(pile_3_moves) == 2

    def test_get_legal_moves_single_stone_piles(self) -> None:
        """Test getting legal moves with single stone in each pile."""
        state = NimState(piles=[1, 1, 1])
        legal_moves = NimStateManager.get_legal_moves(state)

        assert len(legal_moves) == 3
        assert all(move.stones_taken == 1 for move in legal_moves)
        pile_indices = {move.pile_index for move in legal_moves}
        assert pile_indices == {0, 1, 2}

    def test_get_legal_moves_large_pile(self) -> None:
        """Test getting legal moves with large pile."""
        state = NimState(piles=[100])
        legal_moves = NimStateManager.get_legal_moves(state)

        assert len(legal_moves) == 100
        assert all(move.pile_index == 0 for move in legal_moves)
        stones_taken = {move.stones_taken for move in legal_moves}
        assert stones_taken == set(range(1, 101))


class TestNimStateManagerApplyMove:
    """Test cases for NimStateManager move application."""

    def test_apply_move_valid(self) -> None:
        """Test applying a valid move."""
        state = NimState(piles=[3, 5, 7], turn="player1")
        move = NimMove(pile_index=1, stones_taken=2)

        new_state = NimStateManager.apply_move(state, move)

        assert new_state.piles == [3, 3, 7]  # Pile 1 reduced from 5 to 3
        assert new_state.turn == "player2"  # Turn switched
        assert len(new_state.move_history) == 1
        assert new_state.move_history[0] == move
        assert new_state.game_status == "in_progress"

    def test_apply_move_take_all_stones(self) -> None:
        """Test applying move that takes all stones from a pile."""
        state = NimState(piles=[3, 5, 7], turn="player2")
        move = NimMove(pile_index=0, stones_taken=3)

        new_state = NimStateManager.apply_move(state, move)

        assert new_state.piles == [0, 5, 7]
        assert new_state.turn == "player1"
        assert new_state.move_history[0] == move

    def test_apply_move_invalid_pile_index_negative(self) -> None:
        """Test applying move with negative pile index."""
        state = NimState(piles=[3, 5, 7])
        move = NimMove(pile_index=-1, stones_taken=1)

        with pytest.raises(ValueError, match="Invalid pile index: -1"):
            NimStateManager.apply_move(state, move)

    def test_apply_move_invalid_pile_index_too_high(self) -> None:
        """Test applying move with pile index too high."""
        state = NimState(piles=[3, 5, 7])
        move = NimMove(pile_index=3, stones_taken=1)

        with pytest.raises(ValueError, match="Invalid pile index: 3"):
            NimStateManager.apply_move(state, move)

    def test_apply_move_invalid_stones_zero(self) -> None:
        """Test applying move with zero stones."""
        state = NimState(piles=[3, 5, 7])
        move = NimMove(pile_index=0, stones_taken=0)

        with pytest.raises(ValueError, match="Invalid number of stones: 0"):
            NimStateManager.apply_move(state, move)

    def test_apply_move_invalid_stones_too_many(self) -> None:
        """Test applying move with too many stones."""
        state = NimState(piles=[3, 5, 7])
        move = NimMove(pile_index=1, stones_taken=6)  # Pile 1 only has 5 stones

        with pytest.raises(ValueError, match="Invalid number of stones: 6"):
            NimStateManager.apply_move(state, move)

    def test_apply_move_to_empty_pile(self) -> None:
        """Test applying move to empty pile."""
        state = NimState(piles=[0, 5, 7])
        move = NimMove(pile_index=0, stones_taken=1)

        with pytest.raises(ValueError, match="Invalid number of stones: 1"):
            NimStateManager.apply_move(state, move)

    def test_apply_move_sequence(self) -> None:
        """Test applying sequence of moves."""
        state = NimState(piles=[3, 5, 7])

        # Move 1: Player1 takes 2 from pile 1
        move1 = NimMove(pile_index=1, stones_taken=2)
        state = NimStateManager.apply_move(state, move1)
        assert state.piles == [3, 3, 7]
        assert state.turn == "player2"

        # Move 2: Player2 takes 3 from pile 2
        move2 = NimMove(pile_index=2, stones_taken=3)
        state = NimStateManager.apply_move(state, move2)
        assert state.piles == [3, 3, 4]
        assert state.turn == "player1"

        # Move 3: Player1 takes 1 from pile 0
        move3 = NimMove(pile_index=0, stones_taken=1)
        state = NimStateManager.apply_move(state, move3)
        assert state.piles == [2, 3, 4]
        assert state.turn == "player2"

        # Check move history
        assert len(state.move_history) == 3
        assert state.move_history == [move1, move2, move3]

    def test_apply_move_preserves_original_state(self) -> None:
        """Test that applying move doesn't modify original state."""
        original_state = NimState(piles=[3, 5, 7], turn="player1")
        move = NimMove(pile_index=1, stones_taken=2)

        new_state = NimStateManager.apply_move(original_state, move)

        # Original state should be unchanged
        assert original_state.piles == [3, 5, 7]
        assert original_state.turn == "player1"
        assert original_state.move_history == []

        # New state should be different
        assert new_state.piles == [3, 3, 7]
        assert new_state.turn == "player2"
        assert len(new_state.move_history) == 1


class TestNimStateManagerGameStatus:
    """Test cases for NimStateManager game status checking."""

    def test_check_game_status_in_progress(self) -> None:
        """Test checking game status when game is still in progress."""
        state = NimState(piles=[3, 5, 7])
        checked_state = NimStateManager.check_game_status(state)

        assert checked_state.game_status == "in_progress"

    def test_check_game_status_standard_mode_game_over(self) -> None:
        """Test checking game status when game is over in standard mode."""
        # Last move was made by player1, so turn is now player2
        state = NimState(piles=[0, 0, 0], turn="player2", misere_mode=False)
        checked_state = NimStateManager.check_game_status(state)

        # In standard mode, last player to move (player1) wins
        assert checked_state.game_status == "player1_win"

    def test_check_game_status_misere_mode_game_over(self) -> None:
        """Test checking game status when game is over in misere mode."""
        # Last move was made by player2, so turn is now player1
        state = NimState(piles=[0, 0, 0], turn="player1", misere_mode=True)
        checked_state = NimStateManager.check_game_status(state)

        # In misere mode, last player to move (player2) loses, so player1 wins
        assert checked_state.game_status == "player1_win"

    def test_check_game_status_single_stone_remaining(self) -> None:
        """Test checking game status with single stone remaining."""
        state = NimState(piles=[0, 0, 1])
        checked_state = NimStateManager.check_game_status(state)

        assert checked_state.game_status == "in_progress"

    def test_check_game_status_empty_piles_different_turns(self) -> None:
        """Test game over status with different turn states."""
        # Player1's turn after player2 made last move
        state1 = NimState(piles=[0, 0, 0], turn="player1", misere_mode=False)
        checked_state1 = NimStateManager.check_game_status(state1)
        assert checked_state1.game_status == "player2_win"

        # Player2's turn after player1 made last move
        state2 = NimState(piles=[0, 0, 0], turn="player2", misere_mode=False)
        checked_state2 = NimStateManager.check_game_status(state2)
        assert checked_state2.game_status == "player1_win"


class TestNimStateManagerAnalysis:
    """Test cases for NimStateManager analysis methods."""

    def test_add_analysis_player1(self) -> None:
        """Test adding analysis for player1."""
        state = NimState(piles=[3, 5, 7])
        move = NimMove(pile_index=1, stones_taken=2)
        analysis = NimAnalysis(
            nim_sum=1,
            position_evaluation="winning",
            recommended_move=move,
            explanation="Test analysis for player1",
        )

        new_state = NimStateManager.add_analysis(state, "player1", analysis)

        assert len(new_state.player1_analysis) == 1
        assert new_state.player1_analysis[0] == analysis
        assert new_state.player2_analysis == []

    def test_add_analysis_player2(self) -> None:
        """Test adding analysis for player2."""
        state = NimState(piles=[3, 5, 7])
        move = NimMove(pile_index=0, stones_taken=1)
        analysis = NimAnalysis(
            nim_sum=0,
            position_evaluation="losing",
            recommended_move=move,
            explanation="Test analysis for player2",
        )

        new_state = NimStateManager.add_analysis(state, "player2", analysis)

        assert len(new_state.player2_analysis) == 1
        assert new_state.player2_analysis[0] == analysis
        assert new_state.player1_analysis == []

    def test_add_multiple_analyses(self) -> None:
        """Test adding multiple analyses for the same player."""
        state = NimState(piles=[3, 5, 7])
        move1 = NimMove(pile_index=1, stones_taken=2)
        move2 = NimMove(pile_index=2, stones_taken=3)

        analysis1 = NimAnalysis(
            nim_sum=1,
            position_evaluation="winning",
            recommended_move=move1,
            explanation="First analysis",
        )
        analysis2 = NimAnalysis(
            nim_sum=2,
            position_evaluation="unclear",
            recommended_move=move2,
            explanation="Second analysis",
        )

        # Add first analysis
        state = NimStateManager.add_analysis(state, "player1", analysis1)
        assert len(state.player1_analysis) == 1

        # Add second analysis
        state = NimStateManager.add_analysis(state, "player1", analysis2)
        assert len(state.player1_analysis) == 2
        assert state.player1_analysis[0] == analysis1
        assert state.player1_analysis[1] == analysis2

    def test_add_analysis_preserves_original_state(self) -> None:
        """Test that adding analysis doesn't modify original state."""
        original_state = NimState(piles=[3, 5, 7])
        move = NimMove(pile_index=1, stones_taken=2)
        analysis = NimAnalysis(
            nim_sum=1,
            position_evaluation="winning",
            recommended_move=move,
            explanation="Test analysis",
        )

        new_state = NimStateManager.add_analysis(original_state, "player1", analysis)

        # Original state should be unchanged
        assert original_state.player1_analysis == []
        assert original_state.player2_analysis == []

        # New state should have the analysis
        assert len(new_state.player1_analysis) == 1
        assert new_state.player1_analysis[0] == analysis


class TestNimStateManagerMakeMove:
    """Test cases for NimStateManager make_move method."""

    def test_make_move_valid_player1(self) -> None:
        """Test making a valid move for player1."""
        state = NimState(piles=[3, 5, 7], turn="player1")
        move = NimMove(pile_index=1, stones_taken=2)

        command = NimStateManager.make_move(state, "player1", move)

        assert hasattr(command, "update")
        updated_state_dict = command.update
        updated_state = NimState(**updated_state_dict)

        assert updated_state.piles == [3, 3, 7]
        assert updated_state.turn == "player2"
        assert len(updated_state.move_history) == 1

    def test_make_move_valid_player2(self) -> None:
        """Test making a valid move for player2."""
        state = NimState(piles=[3, 5, 7], turn="player2")
        move = NimMove(pile_index=2, stones_taken=3)

        command = NimStateManager.make_move(state, "player2", move)

        updated_state_dict = command.update
        updated_state = NimState(**updated_state_dict)

        assert updated_state.piles == [3, 5, 4]
        assert updated_state.turn == "player1"

    def test_make_move_wrong_turn(self) -> None:
        """Test making move when it's not the player's turn."""
        state = NimState(piles=[3, 5, 7], turn="player1")
        move = NimMove(pile_index=1, stones_taken=2)

        with pytest.raises(ValueError, match="Not player2's turn"):
            NimStateManager.make_move(state, "player2", move)

    def test_make_move_from_dict(self) -> None:
        """Test making move from dictionary state."""
        state_dict = {
            "piles": [3, 5, 7],
            "turn": "player1",
            "game_status": "in_progress",
            "move_history": [],
            "player1_analysis": [],
            "player2_analysis": [],
            "misere_mode": False,
        }
        move = NimMove(pile_index=0, stones_taken=1)

        command = NimStateManager.make_move(state_dict, "player1", move)

        updated_state_dict = command.update
        updated_state = NimState(**updated_state_dict)

        assert updated_state.piles == [2, 5, 7]
        assert updated_state.turn == "player2"


class TestNimStateManagerGetWinner:
    """Test cases for NimStateManager get_winner method."""

    def test_get_winner_in_progress(self) -> None:
        """Test getting winner when game is in progress."""
        state = NimState(piles=[3, 5, 7], game_status="in_progress")
        winner = NimStateManager.get_winner(state)

        assert winner is None

    def test_get_winner_player1_wins(self) -> None:
        """Test getting winner when player1 wins."""
        state = NimState(piles=[0, 0, 0], game_status="player1_win")
        winner = NimStateManager.get_winner(state)

        assert winner == "player1"

    def test_get_winner_player2_wins(self) -> None:
        """Test getting winner when player2 wins."""
        state = NimState(piles=[0, 0, 0], game_status="player2_win")
        winner = NimStateManager.get_winner(state)

        assert winner == "player2"


class TestNimStateManagerEndToEnd:
    """Test cases for end-to-end NimStateManager workflows."""

    def test_complete_game_workflow_standard(self) -> None:
        """Test complete game workflow in standard mode."""
        # Initialize game
        state = NimStateManager.initialize(pile_sizes=[1, 1, 1])
        assert state.game_status == "in_progress"

        # Player1 takes from pile 0
        move1 = NimMove(pile_index=0, stones_taken=1)
        state = NimStateManager.apply_move(state, move1)
        assert state.piles == [0, 1, 1]
        assert state.turn == "player2"
        assert state.game_status == "in_progress"

        # Player2 takes from pile 1
        move2 = NimMove(pile_index=1, stones_taken=1)
        state = NimStateManager.apply_move(state, move2)
        assert state.piles == [0, 0, 1]
        assert state.turn == "player1"
        assert state.game_status == "in_progress"

        # Player1 takes last stone (wins in standard mode)
        move3 = NimMove(pile_index=2, stones_taken=1)
        state = NimStateManager.apply_move(state, move3)
        assert state.piles == [0, 0, 0]
        assert state.game_status == "player1_win"

    def test_complete_game_workflow_misere(self) -> None:
        """Test complete game workflow in misere mode."""
        # Initialize game with misere mode
        state = NimStateManager.initialize(pile_sizes=[1, 1])
        state.misere_mode = True

        # Player1 takes from pile 0
        move1 = NimMove(pile_index=0, stones_taken=1)
        state = NimStateManager.apply_move(state, move1)
        assert state.piles == [0, 1]
        assert state.turn == "player2"

        # Player2 takes last stone (loses in misere mode)
        move2 = NimMove(pile_index=1, stones_taken=1)
        state = NimStateManager.apply_move(state, move2)
        assert state.piles == [0, 0]
        assert state.game_status == "player1_win"  # Player2 lost by taking last stone

    def test_workflow_with_analysis(self) -> None:
        """Test workflow including move and analysis."""
        state = NimStateManager.initialize(pile_sizes=[3, 5])

        # Add analysis for player1
        move = NimMove(pile_index=1, stones_taken=3)
        analysis = NimAnalysis(
            nim_sum=6,
            position_evaluation="winning",
            recommended_move=move,
            explanation="Take 3 from pile 1 to get nim-sum of 0",
        )
        state = NimStateManager.add_analysis(state, "player1", analysis)

        # Apply the recommended move
        state = NimStateManager.apply_move(state, move)
        assert state.piles == [3, 2]
        assert state.turn == "player2"
        assert len(state.player1_analysis) == 1
        assert len(state.move_history) == 1

    def test_legal_moves_throughout_game(self) -> None:
        """Test that legal moves are correctly generated throughout game."""
        state = NimStateManager.initialize(pile_sizes=[2, 2])

        # Initial legal moves
        legal_moves = NimStateManager.get_legal_moves(state)
        assert len(legal_moves) == 4  # 2 + 2

        # After one move
        move = NimMove(pile_index=0, stones_taken=2)
        state = NimStateManager.apply_move(state, move)
        legal_moves = NimStateManager.get_legal_moves(state)
        assert len(legal_moves) == 2  # Only pile 1 has stones

        # After another move
        move = NimMove(pile_index=1, stones_taken=1)
        state = NimStateManager.apply_move(state, move)
        legal_moves = NimStateManager.get_legal_moves(state)
        assert len(legal_moves) == 1  # Only one stone left

        # After final move
        move = NimMove(pile_index=1, stones_taken=1)
        state = NimStateManager.apply_move(state, move)
        legal_moves = NimStateManager.get_legal_moves(state)
        assert len(legal_moves) == 0  # No moves left
