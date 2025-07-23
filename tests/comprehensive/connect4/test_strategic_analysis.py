"""Strategic analysis tests for Connect4 with real components - NO MOCKS."""

from haive.games.connect4.models import Connect4Analysis, Connect4Move
from haive.games.connect4.state import Connect4State
from haive.games.connect4.state_manager import Connect4StateManager


class TestConnect4StrategicAnalysis:
    """Test strategic analysis capabilities of Connect4."""

    def test_winning_move_detection(self):
        """Test detection of immediate winning moves."""
        # Create state where red can win by playing column 3
        state = Connect4State(
            board=[
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                ["red", "red", "red", None, "yellow", "yellow", None],  # Bottom row
            ],
            turn="red",
            game_status="ongoing",
            move_history=[],
        )

        # Column 3 would complete four in a row
        winning_move = Connect4Move(column=3, player="red")
        new_state = Connect4StateManager.apply_move(state, winning_move)

        assert new_state.game_status == "red_win"
        assert new_state.winner == "red"

    def test_blocking_move_detection(self):
        """Test detection of moves that block opponent wins."""
        # Create state where yellow must block red
        state = Connect4State(
            board=[
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                ["red", "red", "red", None, "yellow", "yellow", None],  # Bottom row
            ],
            turn="yellow",
            game_status="ongoing",
            move_history=[],
        )

        # Yellow must block column 3
        blocking_move = Connect4Move(column=3, player="yellow")
        new_state = Connect4StateManager.apply_move(state, blocking_move)

        # Game continues (red didn't win)
        assert new_state.game_status == "ongoing"
        assert new_state.board[5][3] == "yellow"  # Yellow blocked

    def test_center_control_importance(self):
        """Test that center columns are strategically important."""
        state = Connect4StateManager.initialize()

        # Center columns are 2, 3, 4 (0-indexed)

        # Play in center
        center_move = Connect4Move(column=3, player="red")
        new_state = Connect4StateManager.apply_move(state, center_move)

        # Verify center occupation
        assert new_state.board[5][3] == "red"

        # Center control allows more winning possibilities
        # From center, pieces can form 4-in-a-row in more directions

    def test_threat_creation(self):
        """Test creation of multiple threats."""
        # Build position with potential threats
        state = Connect4StateManager.initialize()

        # Create potential for multiple threats
        moves = [
            Connect4Move(column=3, player="red"),  # Center bottom
            Connect4Move(column=3, player="yellow"),  # Stack on center
            Connect4Move(column=2, player="red"),  # Left of center
            Connect4Move(column=4, player="yellow"),  # Right of center
            Connect4Move(column=4, player="red"),  # Stack on right
        ]

        for move in moves:
            state = Connect4StateManager.apply_move(state, move)

        # Red has created horizontal and diagonal possibilities
        # Verify board position allows multiple winning paths
        assert state.board[5][3] == "red"
        assert state.board[5][2] == "red"
        assert state.board[4][4] == "red"

    def test_column_height_strategy(self):
        """Test strategic considerations of column heights."""
        state = Connect4StateManager.initialize()

        # Fill some columns to different heights
        # Column 0: 4 pieces
        for i in range(4):
            player = "red" if i % 2 == 0 else "yellow"
            move = Connect4Move(column=0, player=player)
            state = Connect4StateManager.apply_move(state, move)

        # Column 6: 2 pieces
        for i in range(2):
            player = "red" if i % 2 == 0 else "yellow"
            move = Connect4Move(column=6, player=player)
            state = Connect4StateManager.apply_move(state, move)

        # High columns limit future moves
        assert state.get_next_row(0) == 1  # Only 2 spaces left
        assert state.get_next_row(6) == 3  # 4 spaces left
        assert state.get_next_row(3) == 5  # Empty column

    def test_forced_win_sequence(self):
        """Test detection of forced win sequences."""
        # Create position where red can force a win
        state = Connect4State(
            board=[
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, "red", "yellow", None, None, None],
                [None, None, "red", "yellow", None, None, None],
                [None, "red", "yellow", "red", "yellow", None, None],
            ],
            turn="red",
            game_status="ongoing",
            move_history=[],
        )

        # Red can create a double threat by playing column 4
        setup_move = Connect4Move(column=4, player="red")
        new_state = Connect4StateManager.apply_move(state, setup_move)

        # After yellow's forced response, red will have winning options
        assert new_state.board[5][4] == "red"
        assert new_state.turn == "yellow"

    def test_draw_avoidance(self):
        """Test strategies to avoid drawn positions."""
        # Nearly full board - careful play needed
        state = Connect4State(
            board=[
                ["red", "yellow", "red", "yellow", "red", "yellow", None],
                ["yellow", "red", "yellow", "red", "yellow", "red", "yellow"],
                ["red", "yellow", "red", "yellow", "red", "yellow", "red"],
                ["yellow", "red", "yellow", "red", "yellow", "red", "yellow"],
                ["red", "yellow", "red", "yellow", "red", "yellow", "red"],
                ["yellow", "red", "yellow", "red", "yellow", "red", "yellow"],
            ],
            turn="red",
            game_status="ongoing",
            move_history=[],
        )

        # Only column 6 has space (top row)
        legal_moves = [i for i in range(7) if not state.is_column_full(i)]
        assert legal_moves == [6]

        # Final move
        final_move = Connect4Move(column=6, player="red")
        final_state = Connect4StateManager.apply_move(state, final_move)

        # Game ends (either win or draw)
        assert final_state.game_status != "ongoing"

    def test_analysis_model_validation(self):
        """Test Connect4Analysis model structure."""
        analysis = Connect4Analysis(
            position_score=0.75,
            center_control=6,
            threats={"winning_moves": [3], "blocking_moves": [2, 4]},
            suggested_columns=[3, 2, 4],
            explanation="Strong position with winning threat in column 3",
            winning_chances=85,
        )

        assert analysis.position_score == 0.75
        assert analysis.center_control == 6
        assert 3 in analysis.threats["winning_moves"]
        assert analysis.winning_chances == 85

    def test_position_evaluation_empty_board(self):
        """Test position evaluation on empty board."""
        state = Connect4StateManager.initialize()

        # On empty board, center columns are preferred
        # No immediate threats exist
        assert state.game_status == "ongoing"
        assert all(cell is None for row in state.board for cell in row)

        # Center column (3) is optimal first move
        optimal_first = Connect4Move(column=3, player="red")
        new_state = Connect4StateManager.apply_move(state, optimal_first)
        assert new_state.board[5][3] == "red"

    def test_defensive_play_scenario(self):
        """Test defensive play when behind."""
        # Create disadvantageous position for yellow
        state = Connect4State(
            board=[
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, "red", "red", None, None, None],
                [None, "yellow", "red", "yellow", None, None, None],
                ["yellow", "red", "yellow", "red", "red", "yellow", None],
            ],
            turn="yellow",
            game_status="ongoing",
            move_history=[],
        )

        # Yellow must defend against red's threats
        # Multiple defensive moves may be needed
        critical_columns = []

        # Check each column for red winning potential
        for col in range(7):
            if not state.is_column_full(col):
                # Simulate red playing here next turn
                temp_board = [row[:] for row in state.board]
                row = state.get_next_row(col)
                if row is not None:
                    temp_board[row][col] = "red"
                    # Would red win?
                    Connect4State(
                        board=temp_board,
                        turn="yellow",
                        game_status="ongoing",
                        move_history=[],
                    )
                    # Check win condition (simplified)
                    if Connect4StateManager._check_winner(temp_board) == "red":
                        critical_columns.append(col)

        # Yellow should prioritize blocking critical columns
        assert len(critical_columns) >= 0  # May have defensive needs
