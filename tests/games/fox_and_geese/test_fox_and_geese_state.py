"""Tests for Fox and Geese state with real component validation.

This module provides comprehensive tests for Fox and Geese state management including:
    - State initialization and structure
    - Board representation and piece positions
    - Turn management and game status
    - Move history tracking
    - Win condition detection

All tests use real components without mocks, following the no-mocks methodology.
"""

from haive.games.fox_and_geese.models import FoxAndGeeseMove, FoxAndGeesePosition
from haive.games.fox_and_geese.state import FoxAndGeeseState


class TestFoxAndGeeseState:
    """Test suite for FoxAndGeeseState with real state validation."""

    def test_fox_and_geese_state_initialization_default(self):
        """Test FoxAndGeeseState initialization with default values."""
        state = FoxAndGeeseState()

        # Check initial positions
        assert isinstance(state.fox_position, FoxAndGeesePosition)
        assert state.fox_position.row == 3
        assert state.fox_position.col == 3

        # Check geese positions
        assert isinstance(state.geese_positions, set)
        assert len(state.geese_positions) > 0

        # Check game state
        assert state.current_player == "fox"
        assert state.move_history == []
        assert state.game_status == "ongoing"
        assert state.winner is None

    def test_fox_and_geese_state_initialization_custom(self):
        """Test FoxAndGeeseState initialization with custom values."""
        fox_pos = FoxAndGeesePosition(row=2, col=2)
        geese_positions = {
            FoxAndGeesePosition(row=0, col=0),
            FoxAndGeesePosition(row=0, col=2),
            FoxAndGeesePosition(row=0, col=4),
        }
        moves = [
            FoxAndGeeseMove(
                from_position=FoxAndGeesePosition(row=3, col=3),
                to_position=FoxAndGeesePosition(row=2, col=2),
            )
        ]

        state = FoxAndGeeseState(
            fox_position=fox_pos,
            geese_positions=geese_positions,
            current_player="geese",
            move_history=moves,
            game_status="ongoing",
        )

        assert state.fox_position == fox_pos
        assert state.geese_positions == geese_positions
        assert state.current_player == "geese"
        assert len(state.move_history) == 1
        assert state.game_status == "ongoing"

    def test_fox_and_geese_state_fox_position_validation(self):
        """Test FoxAndGeeseState fox position validation."""
        # Valid positions
        valid_positions = [
            FoxAndGeesePosition(row=0, col=0),
            FoxAndGeesePosition(row=3, col=3),
            FoxAndGeesePosition(row=6, col=6),
        ]

        for pos in valid_positions:
            state = FoxAndGeeseState(fox_position=pos)
            assert state.fox_position == pos

    def test_fox_and_geese_state_geese_positions_validation(self):
        """Test FoxAndGeeseState geese positions validation."""
        # Single goose
        single_goose = {FoxAndGeesePosition(row=0, col=0)}
        state = FoxAndGeeseState(geese_positions=single_goose)
        assert state.geese_positions == single_goose

        # Multiple geese
        multiple_geese = {
            FoxAndGeesePosition(row=0, col=0),
            FoxAndGeesePosition(row=0, col=2),
            FoxAndGeesePosition(row=0, col=4),
            FoxAndGeesePosition(row=1, col=1),
            FoxAndGeesePosition(row=1, col=3),
        }
        state = FoxAndGeeseState(geese_positions=multiple_geese)
        assert state.geese_positions == multiple_geese

    def test_fox_and_geese_state_geese_positions_set_uniqueness(self):
        """Test FoxAndGeeseState geese positions maintain set uniqueness."""
        # Duplicate positions should be automatically deduplicated
        duplicate_list = [
            FoxAndGeesePosition(row=0, col=0),
            FoxAndGeesePosition(row=0, col=2),
            FoxAndGeesePosition(row=0, col=0),  # Duplicate
            FoxAndGeesePosition(row=0, col=4),
        ]

        # Convert to set manually for testing
        geese_set = set(duplicate_list)
        state = FoxAndGeeseState(geese_positions=geese_set)

        # Should have 3 unique positions
        assert len(state.geese_positions) == 3
        expected_positions = {
            FoxAndGeesePosition(row=0, col=0),
            FoxAndGeesePosition(row=0, col=2),
            FoxAndGeesePosition(row=0, col=4),
        }
        assert state.geese_positions == expected_positions

    def test_fox_and_geese_state_current_player_validation(self):
        """Test FoxAndGeeseState current player validation."""
        # Valid players
        valid_players = ["fox", "geese"]

        for player in valid_players:
            state = FoxAndGeeseState(current_player=player)
            assert state.current_player == player

    def test_fox_and_geese_state_game_status_validation(self):
        """Test FoxAndGeeseState game status validation."""
        # Valid game statuses
        valid_statuses = ["ongoing", "fox_wins", "geese_win"]

        for status in valid_statuses:
            state = FoxAndGeeseState(game_status=status)
            assert state.game_status == status

    def test_fox_and_geese_state_move_history_management(self):
        """Test FoxAndGeeseState move history management."""
        state = FoxAndGeeseState()

        # Initially empty
        assert state.move_history == []

        # Add moves
        move1 = FoxAndGeeseMove(
            from_position=FoxAndGeesePosition(row=3, col=3),
            to_position=FoxAndGeesePosition(row=3, col=4),
        )
        move2 = FoxAndGeeseMove(
            from_position=FoxAndGeesePosition(row=0, col=0),
            to_position=FoxAndGeesePosition(row=1, col=0),
        )

        state.move_history = [move1, move2]

        assert len(state.move_history) == 2
        assert state.move_history[0] == move1
        assert state.move_history[1] == move2

    def test_fox_and_geese_state_winner_field_usage(self):
        """Test FoxAndGeeseState winner field usage."""
        state = FoxAndGeeseState()

        # Initially no winner
        assert state.winner is None

        # Set fox as winner
        state.winner = "fox"
        state.game_status = "fox_wins"
        assert state.winner == "fox"
        assert state.game_status == "fox_wins"

        # Set geese as winner
        state.winner = "geese"
        state.game_status = "geese_win"
        assert state.winner == "geese"
        assert state.game_status == "geese_win"

    def test_fox_and_geese_state_complex_board_scenario(self):
        """Test FoxAndGeeseState with complex board scenario."""
        # Create a mid-game scenario
        fox_pos = FoxAndGeesePosition(row=4, col=2)
        geese_positions = {
            FoxAndGeesePosition(row=0, col=0),
            FoxAndGeesePosition(row=0, col=2),
            FoxAndGeesePosition(row=0, col=4),
            FoxAndGeesePosition(row=1, col=1),
            FoxAndGeesePosition(row=1, col=3),
            FoxAndGeesePosition(row=2, col=0),
            FoxAndGeesePosition(row=2, col=2),
            FoxAndGeesePosition(row=3, col=1),
        }

        moves = [
            FoxAndGeeseMove(
                from_position=FoxAndGeesePosition(row=3, col=3),
                to_position=FoxAndGeesePosition(row=4, col=3),
            ),
            FoxAndGeeseMove(
                from_position=FoxAndGeesePosition(row=1, col=5),
                to_position=FoxAndGeesePosition(row=1, col=3),
            ),
            FoxAndGeeseMove(
                from_position=FoxAndGeesePosition(row=4, col=3),
                to_position=FoxAndGeesePosition(row=4, col=2),
            ),
        ]

        state = FoxAndGeeseState(
            fox_position=fox_pos,
            geese_positions=geese_positions,
            current_player="geese",
            move_history=moves,
            game_status="ongoing",
        )

        # Verify complex state
        assert state.fox_position == fox_pos
        assert len(state.geese_positions) == 8
        assert state.current_player == "geese"
        assert len(state.move_history) == 3
        assert state.game_status == "ongoing"

    def test_fox_and_geese_state_board_boundaries(self):
        """Test FoxAndGeeseState with pieces at board boundaries."""
        # Fox at corner
        fox_corner = FoxAndGeesePosition(row=0, col=0)

        # Geese at various edges
        geese_edges = {
            FoxAndGeesePosition(row=0, col=6),  # Top-right corner
            FoxAndGeesePosition(row=6, col=0),  # Bottom-left corner
            FoxAndGeesePosition(row=6, col=6),  # Bottom-right corner
            FoxAndGeesePosition(row=3, col=0),  # Left edge
            FoxAndGeesePosition(row=3, col=6),  # Right edge
            FoxAndGeesePosition(row=0, col=3),  # Top edge
            FoxAndGeesePosition(row=6, col=3),  # Bottom edge
        }

        state = FoxAndGeeseState(fox_position=fox_corner, geese_positions=geese_edges)

        assert state.fox_position == fox_corner
        assert state.geese_positions == geese_edges

    def test_fox_and_geese_state_empty_geese_positions(self):
        """Test FoxAndGeeseState with empty geese positions."""
        # Empty set of geese (unusual but should be valid)
        empty_geese = set()
        state = FoxAndGeeseState(geese_positions=empty_geese)

        assert state.geese_positions == empty_geese
        assert len(state.geese_positions) == 0

    def test_fox_and_geese_state_maximum_geese_scenario(self):
        """Test FoxAndGeeseState with maximum number of geese."""
        # Fill many positions with geese (but not all, fox needs space)
        max_geese = set()
        for row in range(7):
            for col in range(7):
                if not (row == 3 and col == 3):  # Leave center for fox
                    max_geese.add(FoxAndGeesePosition(row=row, col=col))

        state = FoxAndGeeseState(geese_positions=max_geese)

        # Should have 48 geese (49 total positions - 1 for fox)
        assert len(state.geese_positions) == 48

    def test_fox_and_geese_state_serialization(self):
        """Test FoxAndGeeseState serialization to dictionary."""
        fox_pos = FoxAndGeesePosition(row=3, col=4)
        geese_positions = {
            FoxAndGeesePosition(row=0, col=0),
            FoxAndGeesePosition(row=0, col=2),
        }
        move = FoxAndGeeseMove(
            from_position=FoxAndGeesePosition(row=3, col=3),
            to_position=FoxAndGeesePosition(row=3, col=4),
        )

        state = FoxAndGeeseState(
            fox_position=fox_pos,
            geese_positions=geese_positions,
            current_player="geese",
            move_history=[move],
            game_status="ongoing",
        )

        state_dict = state.model_dump()

        assert state_dict["fox_position"]["row"] == 3
        assert state_dict["fox_position"]["col"] == 4
        assert len(state_dict["geese_positions"]) == 2
        assert state_dict["current_player"] == "geese"
        assert len(state_dict["move_history"]) == 1
        assert state_dict["game_status"] == "ongoing"

    def test_fox_and_geese_state_deserialization(self):
        """Test FoxAndGeeseState deserialization from dictionary."""
        state_dict = {
            "fox_position": {"row": 3, "col": 4},
            "geese_positions": [
                {"row": 0, "col": 0},
                {"row": 0, "col": 2},
            ],
            "current_player": "geese",
            "move_history": [
                {
                    "from_position": {"row": 3, "col": 3},
                    "to_position": {"row": 3, "col": 4},
                    "explanation": "Fox move",
                }
            ],
            "game_status": "ongoing",
            "winner": None,
        }

        state = FoxAndGeeseState(**state_dict)

        assert state.fox_position.row == 3
        assert state.fox_position.col == 4
        assert len(state.geese_positions) == 2
        assert state.current_player == "geese"
        assert len(state.move_history) == 1
        assert state.move_history[0].explanation == "Fox move"
        assert state.game_status == "ongoing"
        assert state.winner is None

    def test_fox_and_geese_state_turn_alternation_tracking(self):
        """Test FoxAndGeeseState supports turn alternation tracking."""
        state = FoxAndGeeseState()

        # Start with fox
        assert state.current_player == "fox"

        # Switch to geese
        state.current_player = "geese"
        assert state.current_player == "geese"

        # Switch back to fox
        state.current_player = "fox"
        assert state.current_player == "fox"

    def test_fox_and_geese_state_win_condition_scenarios(self):
        """Test FoxAndGeeseState win condition scenarios."""
        # Fox wins scenario
        fox_wins_state = FoxAndGeeseState(game_status="fox_wins", winner="fox")
        assert fox_wins_state.game_status == "fox_wins"
        assert fox_wins_state.winner == "fox"

        # Geese win scenario
        geese_win_state = FoxAndGeeseState(game_status="geese_win", winner="geese")
        assert geese_win_state.game_status == "geese_win"
        assert geese_win_state.winner == "geese"

    def test_fox_and_geese_state_position_overlap_prevention(self):
        """Test FoxAndGeeseState allows same position for fox and geese (for validation)."""
        # This tests the model allows overlapping positions
        # (game logic should prevent this, but model should be flexible)
        overlap_position = FoxAndGeesePosition(row=3, col=3)
        geese_with_overlap = {overlap_position}

        state = FoxAndGeeseState(
            fox_position=overlap_position, geese_positions=geese_with_overlap
        )

        # Model should allow this (game rules will prevent it)
        assert state.fox_position == overlap_position
        assert overlap_position in state.geese_positions

    def test_fox_and_geese_state_move_history_chronological_order(self):
        """Test FoxAndGeeseState maintains chronological move order."""
        moves = [
            FoxAndGeeseMove(
                from_position=FoxAndGeesePosition(row=3, col=3),
                to_position=FoxAndGeesePosition(row=3, col=4),
                explanation="Fox move 1",
            ),
            FoxAndGeeseMove(
                from_position=FoxAndGeesePosition(row=0, col=0),
                to_position=FoxAndGeesePosition(row=1, col=0),
                explanation="Goose move 1",
            ),
            FoxAndGeeseMove(
                from_position=FoxAndGeesePosition(row=3, col=4),
                to_position=FoxAndGeesePosition(row=4, col=4),
                explanation="Fox move 2",
            ),
        ]

        state = FoxAndGeeseState(move_history=moves)

        # Verify order is maintained
        assert len(state.move_history) == 3
        assert state.move_history[0].explanation == "Fox move 1"
        assert state.move_history[1].explanation == "Goose move 1"
        assert state.move_history[2].explanation == "Fox move 2"

    def test_fox_and_geese_state_geese_position_iteration(self):
        """Test FoxAndGeeseState geese positions can be iterated."""
        geese_positions = {
            FoxAndGeesePosition(row=0, col=0),
            FoxAndGeesePosition(row=0, col=2),
            FoxAndGeesePosition(row=0, col=4),
        }

        state = FoxAndGeeseState(geese_positions=geese_positions)

        # Should be able to iterate over geese positions
        positions_list = list(state.geese_positions)
        assert len(positions_list) == 3

        # Should be able to check membership
        assert FoxAndGeesePosition(row=0, col=0) in state.geese_positions
        assert FoxAndGeesePosition(row=1, col=1) not in state.geese_positions

    def test_fox_and_geese_state_board_coordinate_validation(self):
        """Test FoxAndGeeseState with all valid board coordinates."""
        # Test all positions on a 7x7 board
        for row in range(7):
            for col in range(7):
                position = FoxAndGeesePosition(row=row, col=col)

                # Test as fox position
                state_fox = FoxAndGeeseState(fox_position=position)
                assert state_fox.fox_position == position

                # Test as goose position
                state_goose = FoxAndGeeseState(geese_positions={position})
                assert position in state_goose.geese_positions
