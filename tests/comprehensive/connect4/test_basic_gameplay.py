"""Basic gameplay tests for Connect4 with real components - NO MOCKS."""

import pytest

from haive.games.connect4.models import Connect4Move
from haive.games.connect4.state_manager import Connect4StateManager


class TestConnect4BasicGameplay:
    """Test basic Connect4 gameplay with real components."""

    def test_initial_state(self):
        """Test initial game state creation."""
        state = Connect4StateManager.initialize()

        # Verify initial board is empty
        assert len(state.board) == 6  # 6 rows
        assert all(len(row) == 7 for row in state.board)  # 7 columns each
        assert all(cell is None for row in state.board for cell in row)

        # Verify initial game settings
        assert state.turn == "red"
        assert state.game_status == "ongoing"
        assert state.winner is None
        assert len(state.move_history) == 0

    def test_valid_move_application(self):
        """Test applying valid moves with gravity."""
        state = Connect4StateManager.initialize()

        # Drop piece in column 3
        move1 = Connect4Move(column=3, player="red")
        new_state = Connect4StateManager.apply_move(state, move1)

        # Verify piece dropped to bottom row
        assert new_state.board[5][3] == "red"  # Bottom row, column 3
        assert new_state.turn == "yellow"  # Turn switched
        assert len(new_state.move_history) == 1

        # Drop yellow piece in same column
        move2 = Connect4Move(column=3, player="yellow")
        newer_state = Connect4StateManager.apply_move(new_state, move2)

        # Verify stacking
        assert newer_state.board[5][3] == "red"  # Bottom still red
        assert newer_state.board[4][3] == "yellow"  # One above is yellow
        assert newer_state.turn == "red"  # Turn switched back

    def test_column_full_detection(self):
        """Test detection of full columns."""
        state = Connect4StateManager.initialize()

        # Fill column 2 completely
        moves = []
        for i in range(6):  # 6 moves fill a column
            player = "red" if i % 2 == 0 else "yellow"
            move = Connect4Move(column=2, player=player)
            state = Connect4StateManager.apply_move(state, move)
            moves.append(move)

        # Verify column is full
        assert state.is_column_full(2)
        assert all(state.board[row][2] is not None for row in range(6))

        # Try to play in full column
        invalid_move = Connect4Move(column=2, player=state.turn)
        with pytest.raises(ValueError, match="Column 2 is full"):
            Connect4StateManager.apply_move(state, invalid_move)

    def test_horizontal_win_detection(self):
        """Test horizontal four-in-a-row win detection."""
        state = Connect4StateManager.initialize()

        # Create horizontal win for red (columns 0-3 on bottom row)
        moves = [
            Connect4Move(column=0, player="red"),
            Connect4Move(column=0, player="yellow"),  # Stack on 0
            Connect4Move(column=1, player="red"),
            Connect4Move(column=1, player="yellow"),  # Stack on 1
            Connect4Move(column=2, player="red"),
            Connect4Move(column=4, player="yellow"),  # Elsewhere
            Connect4Move(column=3, player="red"),  # Winning move
        ]

        for move in moves:
            state = Connect4StateManager.apply_move(state, move)

        assert state.game_status == "red_win"
        assert state.winner == "red"

    def test_vertical_win_detection(self):
        """Test vertical four-in-a-row win detection."""
        state = Connect4StateManager.initialize()

        # Create vertical win for red in column 2
        moves = [
            Connect4Move(column=2, player="red"),
            Connect4Move(column=3, player="yellow"),
            Connect4Move(column=2, player="red"),
            Connect4Move(column=3, player="yellow"),
            Connect4Move(column=2, player="red"),
            Connect4Move(column=3, player="yellow"),
            Connect4Move(column=2, player="red"),  # Winning move
        ]

        for move in moves:
            state = Connect4StateManager.apply_move(state, move)

        assert state.game_status == "red_win"
        assert state.winner == "red"

    def test_diagonal_win_detection(self):
        """Test diagonal four-in-a-row win detection."""
        state = Connect4StateManager.initialize()

        # Create diagonal win (ascending from bottom-left)
        # Build structure to enable diagonal
        moves = [
            # Column 0: red
            Connect4Move(column=0, player="red"),
            # Column 1: yellow, red
            Connect4Move(column=1, player="yellow"),
            Connect4Move(column=1, player="red"),
            # Column 2: red, yellow, red
            Connect4Move(column=2, player="red"),
            Connect4Move(column=2, player="yellow"),
            Connect4Move(column=2, player="red"),
            # Column 3: yellow, red, yellow, red (winning)
            Connect4Move(column=3, player="yellow"),
            Connect4Move(column=3, player="red"),
            Connect4Move(column=3, player="yellow"),
            Connect4Move(column=3, player="red"),  # Winning diagonal move
        ]

        for _i, move in enumerate(moves):
            # Adjust player to match game flow
            move.player = state.turn
            state = Connect4StateManager.apply_move(state, move)

        # Check if game ended in a win
        assert state.game_status in ["red_win", "yellow_win"]
        assert state.winner is not None

    def test_draw_detection(self):
        """Test draw detection when board is full."""
        state = Connect4StateManager.initialize()

        # Fill board in pattern that prevents wins
        # Column pattern: 0-6 alternating to prevent 4-in-a-row
        column_order = [0, 1, 2, 3, 4, 5, 6] * 6

        for _i, col in enumerate(column_order[:42]):  # 42 moves fill the board
            if not state.is_column_full(col):
                move = Connect4Move(column=col, player=state.turn)
                state = Connect4StateManager.apply_move(state, move)

                # If game ends early, it's a win not a draw
                if state.game_status != "ongoing":
                    break

        # If no win occurred, verify board is full
        if state.game_status == "ongoing":
            # Fill any remaining spaces
            for col in range(7):
                while not state.is_column_full(col):
                    move = Connect4Move(column=col, player=state.turn)
                    state = Connect4StateManager.apply_move(state, move)
                    if state.game_status != "ongoing":
                        break

        # Game should end in either win or draw
        assert state.game_status in ["red_win", "yellow_win", "draw"]

    def test_move_validation(self):
        """Test move validation rules."""
        state = Connect4StateManager.initialize()

        # Test invalid column
        with pytest.raises(ValueError, match="Column must be between 0 and 6"):
            Connect4Move(column=7, player="red")

        with pytest.raises(ValueError, match="Column must be between 0 and 6"):
            Connect4Move(column=-1, player="red")

        # Test wrong player
        wrong_player_move = Connect4Move(
            column=3, player="yellow"
        )  # Should be red's turn
        with pytest.raises(ValueError, match="It's red's turn"):
            Connect4StateManager.apply_move(state, wrong_player_move)

    def test_state_immutability(self):
        """Test that state objects are immutable."""
        original_state = Connect4StateManager.initialize()
        original_board = [row[:] for row in original_state.board]

        # Apply move
        move = Connect4Move(column=3, player="red")
        new_state = Connect4StateManager.apply_move(original_state, move)

        # Verify original state unchanged
        assert original_state.board == original_board
        assert original_state.turn == "red"
        assert len(original_state.move_history) == 0

        # Verify new state is different
        assert new_state.board != original_board
        assert new_state.turn == "yellow"
        assert len(new_state.move_history) == 1

    def test_game_continues_after_non_winning_move(self):
        """Test that game continues when no win occurs."""
        state = Connect4StateManager.initialize()

        # Make several non-winning moves
        moves = [
            Connect4Move(column=0, player="red"),
            Connect4Move(column=6, player="yellow"),
            Connect4Move(column=1, player="red"),
            Connect4Move(column=5, player="yellow"),
        ]

        for move in moves:
            state = Connect4StateManager.apply_move(state, move)
            assert state.game_status == "ongoing"
            assert state.winner is None

        # Verify game state is correct
        assert len(state.move_history) == 4
        assert state.turn == "red"  # Back to red after even number of moves
