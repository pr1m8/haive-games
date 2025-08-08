"""Comprehensive tests for Battleship game state manager.

This module tests the BattleshipStateManager class and its methods
for managing game state transitions and game logic.
"""

import pytest

from haive.games.battleship.models import (
    Coordinates,
    GamePhase,
    MoveCommand,
    MoveResult,
    ShipPlacement,
    ShipType,
)
from haive.games.battleship.state import BattleshipState
from haive.games.battleship.state_manager import BattleshipStateManager


class TestBattleshipStateManagerInitialization:
    """Test BattleshipStateManager initialization methods."""

    def test_create_initial_state(self):
        """Test creating initial game state."""
        state = BattleshipStateManager.create_initial_state()

        assert isinstance(state, BattleshipState)
        assert state.game_phase == GamePhase.SETUP
        assert state.current_player == "player1"
        assert state.turn_count == 0
        assert not state.game_over
        assert state.winner is None
        assert not state.player1.has_placed_ships
        assert not state.player2.has_placed_ships

    def test_multiple_initial_states_are_independent(self):
        """Test that multiple initial states are independent."""
        state1 = BattleshipStateManager.create_initial_state()
        state2 = BattleshipStateManager.create_initial_state()

        # Modify state1
        state1.turn_count = 5
        state1.current_player = "player2"

        # Verify state2 is unaffected
        assert state2.turn_count == 0
        assert state2.current_player == "player1"


class TestBattleshipStateManagerShipPlacement:
    """Test ship placement functionality."""

    def test_place_ships_valid_placement(self):
        """Test placing ships with valid placements."""
        state = BattleshipStateManager.create_initial_state()

        # Create valid ship placements
        placements = [
            ShipPlacement(
                ship_type=ShipType.DESTROYER,
                coordinates=[Coordinates(row=0, col=0), Coordinates(row=0, col=1)],
            ),
            ShipPlacement(
                ship_type=ShipType.SUBMARINE,
                coordinates=[
                    Coordinates(row=2, col=0),
                    Coordinates(row=3, col=0),
                    Coordinates(row=4, col=0),
                ],
            ),
        ]

        # Place ships for player1
        new_state = BattleshipStateManager.place_ships(state, "player1", placements)

        # Verify ships are placed
        assert new_state.player1.has_placed_ships
        assert len(new_state.player1.ship_placements) == 2
        assert new_state.player1.ship_placements[0].ship_type == ShipType.DESTROYER
        assert new_state.player1.ship_placements[1].ship_type == ShipType.SUBMARINE

        # Verify board is updated
        assert new_state.player1.board.ship_positions[0][0] == "Destroyer"
        assert new_state.player1.board.ship_positions[0][1] == "Destroyer"
        assert new_state.player1.board.ship_positions[2][0] == "Submarine"

    def test_place_ships_all_ship_types(self):
        """Test placing all required ship types."""
        state = BattleshipStateManager.create_initial_state()

        # Create placements for all ship types
        placements = [
            ShipPlacement(
                ship_type=ShipType.CARRIER,
                coordinates=[Coordinates(row=0, col=i) for i in range(5)],
            ),
            ShipPlacement(
                ship_type=ShipType.BATTLESHIP,
                coordinates=[Coordinates(row=1, col=i) for i in range(4)],
            ),
            ShipPlacement(
                ship_type=ShipType.CRUISER,
                coordinates=[Coordinates(row=2, col=i) for i in range(3)],
            ),
            ShipPlacement(
                ship_type=ShipType.SUBMARINE,
                coordinates=[Coordinates(row=3, col=i) for i in range(3)],
            ),
            ShipPlacement(
                ship_type=ShipType.DESTROYER,
                coordinates=[Coordinates(row=4, col=i) for i in range(2)],
            ),
        ]

        new_state = BattleshipStateManager.place_ships(state, "player1", placements)

        # Verify all ships are placed
        assert new_state.player1.has_placed_ships
        assert len(new_state.player1.ship_placements) == 5

        # Verify all ship types are present
        placed_types = {p.ship_type for p in new_state.player1.ship_placements}
        expected_types = set(ShipType)
        assert placed_types == expected_types

    def test_place_ships_missing_ship_types(self):
        """Test placing ships with missing ship types."""
        state = BattleshipStateManager.create_initial_state()

        # Only place destroyer (missing others)
        placements = [
            ShipPlacement(
                ship_type=ShipType.DESTROYER,
                coordinates=[Coordinates(row=0, col=0), Coordinates(row=0, col=1)],
            )
        ]

        with pytest.raises(ValueError, match="Missing ship types"):
            BattleshipStateManager.place_ships(state, "player1", placements)

    def test_place_ships_duplicate_ship_types(self):
        """Test placing ships with duplicate ship types."""
        state = BattleshipStateManager.create_initial_state()

        # Place two destroyers (duplicate)
        placements = [
            ShipPlacement(
                ship_type=ShipType.DESTROYER,
                coordinates=[Coordinates(row=0, col=0), Coordinates(row=0, col=1)],
            ),
            ShipPlacement(
                ship_type=ShipType.DESTROYER,
                coordinates=[Coordinates(row=2, col=0), Coordinates(row=2, col=1)],
            ),
        ]

        with pytest.raises(ValueError, match="Duplicate ship types"):
            BattleshipStateManager.place_ships(state, "player1", placements)

    def test_place_ships_overlapping_coordinates(self):
        """Test placing ships with overlapping coordinates."""
        state = BattleshipStateManager.create_initial_state()

        # Create overlapping placements
        placements = [
            ShipPlacement(
                ship_type=ShipType.DESTROYER,
                coordinates=[Coordinates(row=0, col=0), Coordinates(row=0, col=1)],
            ),
            ShipPlacement(
                ship_type=ShipType.SUBMARINE,
                coordinates=[
                    Coordinates(row=0, col=1),  # Overlaps with destroyer
                    Coordinates(row=1, col=1),
                    Coordinates(row=2, col=1),
                ],
            ),
        ]

        with pytest.raises(ValueError, match="Overlapping coordinates"):
            BattleshipStateManager.place_ships(state, "player1", placements)

    def test_place_ships_invalid_player(self):
        """Test placing ships for invalid player."""
        state = BattleshipStateManager.create_initial_state()
        placements = []

        with pytest.raises(ValueError, match="Invalid player"):
            BattleshipStateManager.place_ships(state, "player3", placements)

    def test_place_ships_both_players_setup_complete(self):
        """Test that game phase changes when both players place ships."""
        state = BattleshipStateManager.create_initial_state()

        # Create minimal valid placements for each ship type
        placements = [
            ShipPlacement(
                ship_type=ShipType.CARRIER,
                coordinates=[Coordinates(row=0, col=i) for i in range(5)],
            ),
            ShipPlacement(
                ship_type=ShipType.BATTLESHIP,
                coordinates=[Coordinates(row=1, col=i) for i in range(4)],
            ),
            ShipPlacement(
                ship_type=ShipType.CRUISER,
                coordinates=[Coordinates(row=2, col=i) for i in range(3)],
            ),
            ShipPlacement(
                ship_type=ShipType.SUBMARINE,
                coordinates=[Coordinates(row=3, col=i) for i in range(3)],
            ),
            ShipPlacement(
                ship_type=ShipType.DESTROYER,
                coordinates=[Coordinates(row=4, col=i) for i in range(2)],
            ),
        ]

        # Place ships for player1
        state = BattleshipStateManager.place_ships(state, "player1", placements)
        assert state.game_phase == GamePhase.SETUP  # Still in setup

        # Place ships for player2 (different positions)
        placements_p2 = [
            ShipPlacement(
                ship_type=ShipType.CARRIER,
                coordinates=[Coordinates(row=5, col=i) for i in range(5)],
            ),
            ShipPlacement(
                ship_type=ShipType.BATTLESHIP,
                coordinates=[Coordinates(row=6, col=i) for i in range(4)],
            ),
            ShipPlacement(
                ship_type=ShipType.CRUISER,
                coordinates=[Coordinates(row=7, col=i) for i in range(3)],
            ),
            ShipPlacement(
                ship_type=ShipType.SUBMARINE,
                coordinates=[Coordinates(row=8, col=i) for i in range(3)],
            ),
            ShipPlacement(
                ship_type=ShipType.DESTROYER,
                coordinates=[Coordinates(row=9, col=i) for i in range(2)],
            ),
        ]

        state = BattleshipStateManager.place_ships(state, "player2", placements_p2)
        assert state.game_phase == GamePhase.PLAYING  # Should transition to playing


class TestBattleshipStateManagerMoveExecution:
    """Test move execution functionality."""

    def test_execute_move_miss(self):
        """Test executing a move that misses."""
        state = self._create_state_with_ships()

        # Make a move that misses (empty cell)
        move = MoveCommand(row=5, col=5)
        new_state = BattleshipStateManager.execute_move(state, "player1", move)

        # Verify move result
        assert new_state.last_move_result == MoveResult.MISS
        assert new_state.player2.board.grid[5][5] is True  # Mark as hit
        assert new_state.player2.board.ship_positions[5][5] is None  # No ship
        assert new_state.turn_count == state.turn_count + 1
        assert new_state.current_player == "player2"  # Switch players

    def test_execute_move_hit(self):
        """Test executing a move that hits a ship."""
        state = self._create_state_with_ships()

        # Make a move that hits (where player2 has a ship)
        move = MoveCommand(row=0, col=0)  # Player2 has destroyer here
        new_state = BattleshipStateManager.execute_move(state, "player1", move)

        # Verify move result
        assert new_state.last_move_result == MoveResult.HIT
        assert new_state.player2.board.grid[0][0] is True  # Mark as hit
        assert new_state.turn_count == state.turn_count + 1
        assert new_state.current_player == "player1"  # Same player continues

    def test_execute_move_sunk_ship(self):
        """Test executing a move that sinks a ship."""
        state = self._create_state_with_ships()

        # Hit first part of destroyer
        move1 = MoveCommand(row=0, col=0)
        state = BattleshipStateManager.execute_move(state, "player1", move1)

        # Hit second part of destroyer to sink it
        move2 = MoveCommand(row=0, col=1)
        new_state = BattleshipStateManager.execute_move(state, "player1", move2)

        # Verify ship is sunk
        assert new_state.last_move_result == MoveResult.SUNK

    def test_execute_move_invalid_coordinates(self):
        """Test executing move with invalid coordinates."""
        state = self._create_state_with_ships()

        # Move out of bounds
        move = MoveCommand(row=10, col=5)

        with pytest.raises(ValueError, match="Invalid move coordinates"):
            BattleshipStateManager.execute_move(state, "player1", move)

    def test_execute_move_already_hit(self):
        """Test executing move on already hit position."""
        state = self._create_state_with_ships()

        # Hit a position
        move = MoveCommand(row=5, col=5)
        state = BattleshipStateManager.execute_move(state, "player1", move)

        # Try to hit same position again
        with pytest.raises(ValueError, match="Position already hit"):
            BattleshipStateManager.execute_move(state, "player2", move)

    def test_execute_move_invalid_player(self):
        """Test executing move for invalid player."""
        state = self._create_state_with_ships()
        move = MoveCommand(row=5, col=5)

        with pytest.raises(ValueError, match="Invalid player"):
            BattleshipStateManager.execute_move(state, "player3", move)

    def test_execute_move_wrong_turn(self):
        """Test executing move when it's not player's turn."""
        state = self._create_state_with_ships()
        move = MoveCommand(row=5, col=5)

        # It's player1's turn, try to move as player2
        with pytest.raises(ValueError, match="Not player2's turn"):
            BattleshipStateManager.execute_move(state, "player2", move)

    def test_execute_move_game_over(self):
        """Test executing move when game is over."""
        state = self._create_state_with_ships()
        state.game_over = True
        state.winner = "player1"

        move = MoveCommand(row=5, col=5)

        with pytest.raises(ValueError, match="Game is already over"):
            BattleshipStateManager.execute_move(state, "player1", move)

    def test_execute_move_wins_game(self):
        """Test executing move that wins the game."""
        state = self._create_state_with_ships()

        # Manually set up a state where player2 has only one ship position left
        # Hit all positions except one
        for placement in state.player2.ship_placements:
            for coord in placement.coordinates:
                state.player2.board.grid[coord.row][coord.col] = True

        # Leave one position unhit
        last_coord = state.player2.ship_placements[0].coordinates[0]
        state.player2.board.grid[last_coord.row][last_coord.col] = False

        # Hit the last position
        move = MoveCommand(row=last_coord.row, col=last_coord.col)
        new_state = BattleshipStateManager.execute_move(state, "player1", move)

        # Verify game is won
        assert new_state.game_over
        assert new_state.winner == "player1"
        assert new_state.game_phase == GamePhase.FINISHED


class TestBattleshipStateManagerAnalysis:
    """Test analysis functionality."""

    def test_add_analysis(self):
        """Test adding strategic analysis."""
        state = BattleshipStateManager.create_initial_state()

        analysis = "Enemy likely has ships in top-left quadrant"
        new_state = BattleshipStateManager.add_analysis(state, "player1", analysis)

        assert len(new_state.player1.strategic_analysis) == 1
        assert new_state.player1.strategic_analysis[0] == analysis
        assert len(new_state.player2.strategic_analysis) == 0

    def test_add_multiple_analyses(self):
        """Test adding multiple strategic analyses."""
        state = BattleshipStateManager.create_initial_state()

        # Add multiple analyses
        analyses = [
            "Enemy favors edge placements",
            "Likely has carrier horizontally placed",
            "Focus search on rows 3-7",
        ]

        for analysis in analyses:
            state = BattleshipStateManager.add_analysis(state, "player1", analysis)

        assert len(state.player1.strategic_analysis) == 3
        assert state.player1.strategic_analysis == analyses

    def test_add_analysis_different_players(self):
        """Test adding analysis for different players."""
        state = BattleshipStateManager.create_initial_state()

        analysis1 = "Player 1 analysis"
        analysis2 = "Player 2 analysis"

        state = BattleshipStateManager.add_analysis(state, "player1", analysis1)
        state = BattleshipStateManager.add_analysis(state, "player2", analysis2)

        assert len(state.player1.strategic_analysis) == 1
        assert len(state.player2.strategic_analysis) == 1
        assert state.player1.strategic_analysis[0] == analysis1
        assert state.player2.strategic_analysis[0] == analysis2

    def test_add_analysis_invalid_player(self):
        """Test adding analysis for invalid player."""
        state = BattleshipStateManager.create_initial_state()

        with pytest.raises(ValueError, match="Invalid player"):
            BattleshipStateManager.add_analysis(state, "player3", "test analysis")


class TestBattleshipStateManagerUtilities:
    """Test utility methods."""

    def test_is_valid_move_coordinates(self):
        """Test coordinate validation for moves."""
        # Valid coordinates
        assert BattleshipStateManager._is_valid_move_coordinates(0, 0)
        assert BattleshipStateManager._is_valid_move_coordinates(9, 9)
        assert BattleshipStateManager._is_valid_move_coordinates(5, 3)

        # Invalid coordinates
        assert not BattleshipStateManager._is_valid_move_coordinates(-1, 5)
        assert not BattleshipStateManager._is_valid_move_coordinates(10, 5)
        assert not BattleshipStateManager._is_valid_move_coordinates(5, -1)
        assert not BattleshipStateManager._is_valid_move_coordinates(5, 10)

    def test_is_ship_sunk(self):
        """Test ship sunk detection."""
        state = self._create_state_with_ships()

        # Initially ship not sunk
        destroyer_coords = [Coordinates(row=0, col=0), Coordinates(row=0, col=1)]
        assert not BattleshipStateManager._is_ship_sunk(state.player2, destroyer_coords)

        # Hit one part
        state.player2.board.grid[0][0] = True
        assert not BattleshipStateManager._is_ship_sunk(state.player2, destroyer_coords)

        # Hit all parts
        state.player2.board.grid[0][1] = True
        assert BattleshipStateManager._is_ship_sunk(state.player2, destroyer_coords)

    def _create_state_with_ships(self) -> BattleshipState:
        """Helper method to create state with ships placed."""
        state = BattleshipStateManager.create_initial_state()

        # Place ships for both players
        placements = [
            ShipPlacement(
                ship_type=ShipType.CARRIER,
                coordinates=[Coordinates(row=0, col=i) for i in range(5)],
            ),
            ShipPlacement(
                ship_type=ShipType.BATTLESHIP,
                coordinates=[Coordinates(row=1, col=i) for i in range(4)],
            ),
            ShipPlacement(
                ship_type=ShipType.CRUISER,
                coordinates=[Coordinates(row=2, col=i) for i in range(3)],
            ),
            ShipPlacement(
                ship_type=ShipType.SUBMARINE,
                coordinates=[Coordinates(row=3, col=i) for i in range(3)],
            ),
            ShipPlacement(
                ship_type=ShipType.DESTROYER,
                coordinates=[Coordinates(row=4, col=i) for i in range(2)],
            ),
        ]

        # Player 1 ships at top
        state = BattleshipStateManager.place_ships(state, "player1", placements)

        # Player 2 ships at bottom (offset by 5 rows)
        placements_p2 = [
            ShipPlacement(
                ship_type=placement.ship_type,
                coordinates=[
                    Coordinates(row=coord.row + 5, col=coord.col)
                    for coord in placement.coordinates
                ],
            )
            for placement in placements
        ]

        state = BattleshipStateManager.place_ships(state, "player2", placements_p2)

        return state


class TestBattleshipStateManagerEdgeCases:
    """Test edge cases and error conditions."""

    def test_state_manager_with_empty_state(self):
        """Test state manager methods with minimal state."""
        state = BattleshipState()

        # Should handle basic operations
        assert not state.is_setup_complete()
        assert state.current_player == "player1"

    def test_concurrent_modifications_independence(self):
        """Test that state modifications are independent."""
        initial_state = BattleshipStateManager.create_initial_state()

        # Create two separate modification paths
        state1 = BattleshipStateManager.add_analysis(
            initial_state, "player1", "Analysis 1"
        )
        state2 = BattleshipStateManager.add_analysis(
            initial_state, "player2", "Analysis 2"
        )

        # Verify states are independent
        assert len(state1.player1.strategic_analysis) == 1
        assert len(state1.player2.strategic_analysis) == 0
        assert len(state2.player1.strategic_analysis) == 0
        assert len(state2.player2.strategic_analysis) == 1

    def test_large_ship_placement_validation(self):
        """Test validation with maximum size ship (carrier)."""
        state = BattleshipStateManager.create_initial_state()

        # Place carrier at edge of board
        placements = [
            ShipPlacement(
                ship_type=ShipType.CARRIER,
                coordinates=[Coordinates(row=0, col=i) for i in range(5, 10)],
            ),
        ]

        # Should raise error due to missing ship types
        with pytest.raises(ValueError, match="Missing ship types"):
            BattleshipStateManager.place_ships(state, "player1", placements)
