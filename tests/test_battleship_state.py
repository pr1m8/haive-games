"""Comprehensive tests for Battleship game state.

This module tests the BattleshipState class and PlayerState,
including initialization, properties, and methods.
"""

import pytest

from haive.games.battleship.models import (
    Coordinates,
    GamePhase,
    MoveResult,
    PlayerBoard,
    ShipPlacement,
    ShipType,
)
from haive.games.battleship.state import BattleshipState, PlayerState


class TestPlayerState:
    """Test PlayerState class."""

    def test_player_state_creation_default(self):
        """Test creating PlayerState with default values."""
        state = PlayerState()

        assert isinstance(state.board, PlayerBoard)
        assert state.strategic_analysis == []
        assert state.has_placed_ships is False
        assert state.ship_placements == []

    def test_player_state_creation_with_values(self):
        """Test creating PlayerState with specific values."""
        board = PlayerBoard()
        board.grid[0][0] = True

        analysis = ["Enemy likely has ships in quadrant 2"]
        placements = [
            ShipPlacement(
                ship_type=ShipType.DESTROYER,
                coordinates=[Coordinates(row=0, col=0), Coordinates(row=0, col=1)],
            )
        ]

        state = PlayerState(
            board=board,
            strategic_analysis=analysis,
            has_placed_ships=True,
            ship_placements=placements,
        )

        assert state.board.grid[0][0] is True
        assert state.strategic_analysis == analysis
        assert state.has_placed_ships is True
        assert len(state.ship_placements) == 1
        assert state.ship_placements[0].ship_type == ShipType.DESTROYER

    def test_player_state_independent_instances(self):
        """Test that PlayerState instances are independent."""
        state1 = PlayerState()
        state2 = PlayerState()

        # Modify state1
        state1.strategic_analysis.append("Test analysis")
        state1.has_placed_ships = True

        # Verify state2 is unaffected
        assert state2.strategic_analysis == []
        assert state2.has_placed_ships is False

    def test_player_state_board_modification(self):
        """Test modifying player board state."""
        state = PlayerState()

        # Initially all False
        assert not any(any(row) for row in state.board.grid)

        # Modify board
        state.board.grid[5][3] = True
        state.board.ship_positions[5][3] = "Destroyer"

        assert state.board.grid[5][3] is True
        assert state.board.ship_positions[5][3] == "Destroyer"


class TestBattleshipState:
    """Test BattleshipState class."""

    def test_battleship_state_creation_default(self):
        """Test creating BattleshipState with default values."""
        state = BattleshipState()

        assert isinstance(state.player1, PlayerState)
        assert isinstance(state.player2, PlayerState)
        assert state.current_player == "player1"
        assert state.game_phase == GamePhase.SETUP
        assert state.turn_count == 0
        assert state.last_move_result is None
        assert state.error_message is None
        assert state.game_over is False
        assert state.winner is None

    def test_battleship_state_creation_with_values(self):
        """Test creating BattleshipState with specific values."""
        player1 = PlayerState(has_placed_ships=True)
        player2 = PlayerState(has_placed_ships=True)

        state = BattleshipState(
            player1=player1,
            player2=player2,
            current_player="player2",
            game_phase=GamePhase.PLAYING,
            turn_count=5,
            last_move_result=MoveResult.HIT,
            winner="player1",
            game_over=True,
        )

        assert state.player1.has_placed_ships is True
        assert state.player2.has_placed_ships is True
        assert state.current_player == "player2"
        assert state.game_phase == GamePhase.PLAYING
        assert state.turn_count == 5
        assert state.last_move_result == MoveResult.HIT
        assert state.winner == "player1"
        assert state.game_over is True

    def test_get_current_player_state(self):
        """Test getting current player's state."""
        state = BattleshipState()

        # Initially player1's turn
        current = state.get_current_player_state()
        assert current is state.player1

        # Switch to player2
        state.current_player = "player2"
        current = state.get_current_player_state()
        assert current is state.player2

    def test_get_player_state_by_name(self):
        """Test getting player state by name."""
        state = BattleshipState()

        player1_state = state.get_player_state("player1")
        assert player1_state is state.player1

        player2_state = state.get_player_state("player2")
        assert player2_state is state.player2

    def test_get_player_state_invalid_name(self):
        """Test getting player state with invalid name."""
        state = BattleshipState()

        with pytest.raises(ValueError, match="Invalid player"):
            state.get_player_state("player3")

    def test_get_opponent_name(self):
        """Test getting opponent's name."""
        state = BattleshipState()

        assert state.get_opponent("player1") == "player2"
        assert state.get_opponent("player2") == "player1"

    def test_get_opponent_invalid_name(self):
        """Test getting opponent with invalid name."""
        state = BattleshipState()

        with pytest.raises(ValueError, match="Invalid player"):
            state.get_opponent("player3")

    def test_is_setup_complete(self):
        """Test checking if setup is complete."""
        state = BattleshipState()

        # Initially setup not complete
        assert not state.is_setup_complete()

        # Place ships for player1 only
        state.player1.has_placed_ships = True
        assert not state.is_setup_complete()

        # Place ships for both players
        state.player2.has_placed_ships = True
        assert state.is_setup_complete()

    def test_switch_player(self):
        """Test switching between players."""
        state = BattleshipState()

        # Initially player1's turn
        assert state.current_player == "player1"

        state.switch_player()
        assert state.current_player == "player2"

        state.switch_player()
        assert state.current_player == "player1"

    def test_increment_turn(self):
        """Test incrementing turn count."""
        state = BattleshipState()

        assert state.turn_count == 0

        state.increment_turn()
        assert state.turn_count == 1

        state.increment_turn()
        assert state.turn_count == 2

    def test_get_public_state_for_player(self):
        """Test getting public state for a player."""
        state = BattleshipState()

        # Set up some game state
        state.player1.board.grid[0][0] = True
        state.player2.board.grid[1][1] = True
        state.turn_count = 3
        state.last_move_result = MoveResult.MISS

        # Get public state for player1
        public_state = state.get_public_state_for_player("player1")

        # Should contain own board and opponent's hits/misses
        assert "own_board" in public_state
        assert "opponent_board" in public_state
        assert "turn_count" in public_state
        assert "last_move_result" in public_state
        assert "game_phase" in public_state
        assert "current_player" in public_state

    def test_get_public_state_different_players(self):
        """Test that public state is different for different players."""
        state = BattleshipState()

        public1 = state.get_public_state_for_player("player1")
        public2 = state.get_public_state_for_player("player2")

        # Should be different dictionaries
        assert public1 is not public2

    def test_all_ships_sunk_no_ships(self):
        """Test all_ships_sunk with no ships placed."""
        state = BattleshipState()

        # No ships placed yet
        assert not state.all_ships_sunk("player1")
        assert not state.all_ships_sunk("player2")

    def test_all_ships_sunk_with_ships_intact(self):
        """Test all_ships_sunk with ships still intact."""
        state = BattleshipState()

        # Place a ship for player1
        placement = ShipPlacement(
            ship_type=ShipType.DESTROYER,
            coordinates=[Coordinates(row=0, col=0), Coordinates(row=0, col=1)],
        )
        state.player1.ship_placements = [placement]

        # Ship positions on board (not hit)
        state.player1.board.ship_positions[0][0] = "Destroyer"
        state.player1.board.ship_positions[0][1] = "Destroyer"

        # Ships not hit, so not all sunk
        assert not state.all_ships_sunk("player1")

    def test_all_ships_sunk_with_ships_destroyed(self):
        """Test all_ships_sunk with all ships destroyed."""
        state = BattleshipState()

        # Place a ship for player1
        placement = ShipPlacement(
            ship_type=ShipType.DESTROYER,
            coordinates=[Coordinates(row=0, col=0), Coordinates(row=0, col=1)],
        )
        state.player1.ship_placements = [placement]

        # Ship positions on board (both hit)
        state.player1.board.ship_positions[0][0] = "Destroyer"
        state.player1.board.ship_positions[0][1] = "Destroyer"
        state.player1.board.grid[0][0] = True  # Hit
        state.player1.board.grid[0][1] = True  # Hit

        # All ship positions hit, so all sunk
        assert state.all_ships_sunk("player1")


class TestBattleshipStateIntegration:
    """Test integration scenarios for BattleshipState."""

    def test_complete_game_setup_flow(self):
        """Test complete game setup workflow."""
        state = BattleshipState()

        # Initially in setup phase
        assert state.game_phase == GamePhase.SETUP
        assert not state.is_setup_complete()

        # Place ships for both players
        destroyer = ShipPlacement(
            ship_type=ShipType.DESTROYER,
            coordinates=[Coordinates(row=0, col=0), Coordinates(row=0, col=1)],
        )

        state.player1.ship_placements = [destroyer]
        state.player1.has_placed_ships = True

        state.player2.ship_placements = [destroyer]
        state.player2.has_placed_ships = True

        # Setup should now be complete
        assert state.is_setup_complete()

    def test_game_progression_flow(self):
        """Test game progression from setup to playing."""
        state = BattleshipState()

        # Setup complete
        state.player1.has_placed_ships = True
        state.player2.has_placed_ships = True
        state.game_phase = GamePhase.PLAYING

        # Make some moves
        assert state.turn_count == 0
        assert state.current_player == "player1"

        # Player 1 makes a move
        state.increment_turn()
        state.last_move_result = MoveResult.MISS
        state.switch_player()

        assert state.turn_count == 1
        assert state.current_player == "player2"
        assert state.last_move_result == MoveResult.MISS

    def test_game_end_conditions(self):
        """Test various game end conditions."""
        state = BattleshipState()

        # Game initially not over
        assert not state.game_over
        assert state.winner is None

        # Set game over with winner
        state.game_over = True
        state.winner = "player1"
        state.game_phase = GamePhase.FINISHED

        assert state.game_over
        assert state.winner == "player1"
        assert state.game_phase == GamePhase.FINISHED

    def test_state_serialization(self):
        """Test that state can be serialized and deserialized."""
        state = BattleshipState()

        # Modify some state
        state.current_player = "player2"
        state.turn_count = 5
        state.game_phase = GamePhase.PLAYING
        state.last_move_result = MoveResult.HIT

        # Serialize to dict
        state_dict = (
            state.model_dump() if hasattr(state, "model_dump") else state.dict()
        )

        # Deserialize back
        new_state = BattleshipState(**state_dict)

        # Verify fields match
        assert new_state.current_player == state.current_player
        assert new_state.turn_count == state.turn_count
        assert new_state.game_phase == state.game_phase
        assert new_state.last_move_result == state.last_move_result

    def test_multiple_ships_placement(self):
        """Test placing multiple ships for players."""
        state = BattleshipState()

        # Place multiple ships for player1
        ships = [
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

        state.player1.ship_placements = ships
        state.player1.has_placed_ships = True

        # Verify ships are placed
        assert len(state.player1.ship_placements) == 2
        assert state.player1.ship_placements[0].ship_type == ShipType.DESTROYER
        assert state.player1.ship_placements[1].ship_type == ShipType.SUBMARINE

    def test_strategic_analysis_tracking(self):
        """Test tracking strategic analysis for players."""
        state = BattleshipState()

        # Add analysis for both players
        state.player1.strategic_analysis.append("Enemy ships likely in bottom half")
        state.player1.strategic_analysis.append("Focus on grid squares 5-9")

        state.player2.strategic_analysis.append("Player 1 seems to target edges")

        # Verify analysis is tracked
        assert len(state.player1.strategic_analysis) == 2
        assert len(state.player2.strategic_analysis) == 1
        assert "bottom half" in state.player1.strategic_analysis[0]

    def test_error_handling_state(self):
        """Test error message handling in state."""
        state = BattleshipState()

        # Initially no error
        assert state.error_message is None

        # Set error message
        state.error_message = "Invalid ship placement"
        assert state.error_message == "Invalid ship placement"

        # Clear error message
        state.error_message = None
        assert state.error_message is None

    def test_state_copy_independence(self):
        """Test that copied states are independent."""
        state = BattleshipState()

        # Modify original state
        state.player1.strategic_analysis.append("Test analysis")
        state.turn_count = 3

        # Create copy using pydantic
        state_copy = (
            state.model_copy() if hasattr(state, "model_copy") else state.copy()
        )

        # Modify copy
        state_copy.turn_count = 5
        state_copy.current_player = "player2"

        # Verify original is unchanged
        assert state.turn_count == 3
        assert state.current_player == "player1"
        assert state_copy.turn_count == 5
        assert state_copy.current_player == "player2"
