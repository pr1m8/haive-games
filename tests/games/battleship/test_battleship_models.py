"""Comprehensive tests for Battleship game models.

This module tests all data models, enumerations, and data structures
used in the Battleship game implementation.
"""

from pydantic import ValidationError
import pytest

from haive.games.battleship.models import (
    Coordinates,
    GamePhase,
    MoveCommand,
    MoveResult,
    PlayerBoard,
    ShipPlacement,
    ShipType,
)


class TestEnumerations:
    """Test all enumeration classes."""

    def test_ship_type_enum_values(self):
        """Test that ShipType enum has all expected values."""
        expected_ships = {
            "Carrier",
            "Battleship",
            "Cruiser",
            "Submarine",
            "Destroyer",
        }
        actual_ships = {ship.value for ship in ShipType}
        assert actual_ships == expected_ships
        assert len(ShipType) == 5

    def test_ship_type_size_property(self):
        """Test that each ship type has correct size."""
        expected_sizes = {
            ShipType.CARRIER: 5,
            ShipType.BATTLESHIP: 4,
            ShipType.CRUISER: 3,
            ShipType.SUBMARINE: 3,
            ShipType.DESTROYER: 2,
        }

        for ship_type, expected_size in expected_sizes.items():
            assert ship_type.size == expected_size

    def test_move_result_enum_values(self):
        """Test that MoveResult enum has all expected values."""
        expected_results = {"HIT", "MISS", "SUNK"}
        actual_results = {result.value for result in MoveResult}
        assert actual_results == expected_results
        assert len(MoveResult) == 3

    def test_game_phase_enum_values(self):
        """Test that GamePhase enum has all expected values."""
        expected_phases = {"SETUP", "PLAYING", "FINISHED"}
        actual_phases = {phase.value for phase in GamePhase}
        assert actual_phases == expected_phases
        assert len(GamePhase) == 3


class TestCoordinates:
    """Test Coordinates model."""

    def test_coordinates_creation(self):
        """Test creating Coordinates instance."""
        coords = Coordinates(row=3, col=5)
        assert coords.row == 3
        assert coords.col == 5

    def test_coordinates_validation_valid_ranges(self):
        """Test coordinates validation with valid ranges."""
        # Test boundary values
        valid_coords = [
            (0, 0),  # Top-left corner
            (9, 9),  # Bottom-right corner
            (5, 3),  # Middle values
            (0, 9),  # Top-right corner
            (9, 0),  # Bottom-left corner
        ]

        for row, col in valid_coords:
            coords = Coordinates(row=row, col=col)
            assert coords.row == row
            assert coords.col == col

    def test_coordinates_validation_invalid_ranges(self):
        """Test coordinates validation with invalid ranges."""
        invalid_coords = [
            (-1, 5),  # Negative row
            (5, -1),  # Negative col
            (10, 5),  # Row too large
            (5, 10),  # Col too large
            (-1, -1),  # Both negative
            (10, 10),  # Both too large
        ]

        for row, col in invalid_coords:
            with pytest.raises(ValidationError):
                Coordinates(row=row, col=col)

    def test_coordinates_equality(self):
        """Test coordinates equality comparison."""
        coords1 = Coordinates(row=3, col=5)
        coords2 = Coordinates(row=3, col=5)
        coords3 = Coordinates(row=3, col=6)

        assert coords1 == coords2
        assert coords1 != coords3

    def test_coordinates_hash(self):
        """Test that coordinates can be used as dictionary keys."""
        coords1 = Coordinates(row=3, col=5)
        coords2 = Coordinates(row=3, col=5)
        coords3 = Coordinates(row=4, col=5)

        coord_dict = {coords1: "value1", coords3: "value2"}
        assert coord_dict[coords2] == "value1"  # Same coordinates
        assert len(coord_dict) == 2


class TestShipPlacement:
    """Test ShipPlacement model."""

    def test_ship_placement_creation(self):
        """Test creating ShipPlacement instance."""
        coords = [
            Coordinates(row=0, col=0),
            Coordinates(row=0, col=1),
            Coordinates(row=0, col=2),
        ]
        placement = ShipPlacement(
            ship_type=ShipType.CRUISER,
            coordinates=coords,
        )

        assert placement.ship_type == ShipType.CRUISER
        assert len(placement.coordinates) == 3
        assert placement.coordinates == coords

    def test_ship_placement_validation_correct_size(self):
        """Test ship placement validation with correct size."""
        # Test each ship type with correct number of coordinates
        test_cases = [
            (ShipType.DESTROYER, 2),
            (ShipType.SUBMARINE, 3),
            (ShipType.CRUISER, 3),
            (ShipType.BATTLESHIP, 4),
            (ShipType.CARRIER, 5),
        ]

        for ship_type, size in test_cases:
            coords = [Coordinates(row=0, col=i) for i in range(size)]
            placement = ShipPlacement(ship_type=ship_type, coordinates=coords)
            assert len(placement.coordinates) == size

    def test_ship_placement_validation_incorrect_size(self):
        """Test ship placement validation with incorrect size."""
        # Try to create cruiser with wrong number of coordinates
        coords_too_few = [Coordinates(row=0, col=0), Coordinates(row=0, col=1)]
        coords_too_many = [
            Coordinates(row=0, col=i) for i in range(5)
        ]  # 5 coords for cruiser (should be 3)

        with pytest.raises(ValidationError, match="must have exactly 3 coordinates"):
            ShipPlacement(ship_type=ShipType.CRUISER, coordinates=coords_too_few)

        with pytest.raises(ValidationError, match="must have exactly 3 coordinates"):
            ShipPlacement(ship_type=ShipType.CRUISER, coordinates=coords_too_many)

    def test_ship_placement_validation_contiguous_horizontal(self):
        """Test ship placement validation for horizontal ships."""
        # Valid horizontal placement
        coords = [
            Coordinates(row=2, col=3),
            Coordinates(row=2, col=4),
            Coordinates(row=2, col=5),
        ]
        placement = ShipPlacement(ship_type=ShipType.CRUISER, coordinates=coords)
        assert len(placement.coordinates) == 3

    def test_ship_placement_validation_contiguous_vertical(self):
        """Test ship placement validation for vertical ships."""
        # Valid vertical placement
        coords = [
            Coordinates(row=1, col=4),
            Coordinates(row=2, col=4),
            Coordinates(row=3, col=4),
        ]
        placement = ShipPlacement(ship_type=ShipType.CRUISER, coordinates=coords)
        assert len(placement.coordinates) == 3

    def test_ship_placement_validation_non_contiguous(self):
        """Test ship placement validation fails for non-contiguous coordinates."""
        # Non-contiguous coordinates
        coords = [
            Coordinates(row=0, col=0),
            Coordinates(row=0, col=2),  # Gap at col=1
            Coordinates(row=0, col=3),
        ]

        with pytest.raises(ValidationError, match="must be contiguous"):
            ShipPlacement(ship_type=ShipType.CRUISER, coordinates=coords)

    def test_ship_placement_validation_diagonal(self):
        """Test ship placement validation fails for diagonal placement."""
        # Diagonal coordinates
        coords = [
            Coordinates(row=0, col=0),
            Coordinates(row=1, col=1),
            Coordinates(row=2, col=2),
        ]

        with pytest.raises(ValidationError, match="must be in a straight line"):
            ShipPlacement(ship_type=ShipType.CRUISER, coordinates=coords)

    def test_ship_placement_empty_coordinates(self):
        """Test ship placement with empty coordinates list."""
        with pytest.raises(ValidationError):
            ShipPlacement(ship_type=ShipType.DESTROYER, coordinates=[])


class TestMoveCommand:
    """Test MoveCommand model."""

    def test_move_command_creation(self):
        """Test creating MoveCommand instance."""
        move = MoveCommand(row=3, col=7)
        assert move.row == 3
        assert move.col == 7

    def test_move_command_validation(self):
        """Test move command validation."""
        # Valid moves
        valid_moves = [(0, 0), (9, 9), (5, 3)]
        for row, col in valid_moves:
            move = MoveCommand(row=row, col=col)
            assert move.row == row
            assert move.col == col

        # Invalid moves
        invalid_moves = [(-1, 5), (10, 5), (5, -1), (5, 10)]
        for row, col in invalid_moves:
            with pytest.raises(ValidationError):
                MoveCommand(row=row, col=col)

    def test_move_command_to_coordinates(self):
        """Test converting MoveCommand to Coordinates."""
        move = MoveCommand(row=4, col=6)
        coords = Coordinates(row=move.row, col=move.col)
        assert coords.row == 4
        assert coords.col == 6


class TestPlayerBoard:
    """Test PlayerBoard model."""

    def test_player_board_creation_default(self):
        """Test creating PlayerBoard with default values."""
        board = PlayerBoard()

        # Check default grid is 10x10 with all False
        assert len(board.grid) == 10
        for row in board.grid:
            assert len(row) == 10
            assert all(cell is False for cell in row)

        # Check default ship positions is empty
        assert len(board.ship_positions) == 10
        for row in board.ship_positions:
            assert len(row) == 10
            assert all(cell is None for cell in row)

    def test_player_board_creation_custom(self):
        """Test creating PlayerBoard with custom values."""
        custom_grid = [
            [True if i == j else False for j in range(10)] for i in range(10)
        ]
        custom_ships = [
            ["ship" if i == j else None for j in range(10)] for i in range(10)
        ]

        board = PlayerBoard(grid=custom_grid, ship_positions=custom_ships)

        assert board.grid == custom_grid
        assert board.ship_positions == custom_ships

    def test_player_board_validation_grid_size(self):
        """Test PlayerBoard validation for grid size."""
        # Invalid grid sizes
        with pytest.raises(ValidationError):
            PlayerBoard(grid=[[False] * 9] * 10)  # Wrong column count

        with pytest.raises(ValidationError):
            PlayerBoard(grid=[[False] * 10] * 9)  # Wrong row count

    def test_player_board_validation_ship_positions_size(self):
        """Test PlayerBoard validation for ship positions size."""
        # Invalid ship position sizes
        with pytest.raises(ValidationError):
            PlayerBoard(ship_positions=[[None] * 9] * 10)  # Wrong column count

        with pytest.raises(ValidationError):
            PlayerBoard(ship_positions=[[None] * 10] * 9)  # Wrong row count

    def test_player_board_mixed_validation(self):
        """Test PlayerBoard with one valid and one invalid field."""
        valid_grid = [[False] * 10] * 10
        invalid_ships = [[None] * 9] * 10  # Wrong size

        with pytest.raises(ValidationError):
            PlayerBoard(grid=valid_grid, ship_positions=invalid_ships)


class TestModelIntegration:
    """Test integration between different model classes."""

    def test_complete_ship_placement_workflow(self):
        """Test complete workflow of placing ships on board."""
        # Create ship placement
        coords = [Coordinates(row=0, col=i) for i in range(3)]
        placement = ShipPlacement(ship_type=ShipType.CRUISER, coordinates=coords)

        # Verify placement
        assert placement.ship_type == ShipType.CRUISER
        assert len(placement.coordinates) == 3

        # Verify coordinates are valid
        for coord in placement.coordinates:
            assert 0 <= coord.row <= 9
            assert 0 <= coord.col <= 9

    def test_move_command_on_board(self):
        """Test using MoveCommand with board coordinates."""
        board = PlayerBoard()
        move = MoveCommand(row=5, col=3)

        # Simulate placing move on board
        board.grid[move.row][move.col] = True

        assert board.grid[5][3] is True
        assert board.grid[5][4] is False  # Adjacent cell unchanged

    def test_all_ship_types_placement(self):
        """Test placing all ship types with correct sizes."""
        ship_placements = []

        # Place each ship type
        row = 0
        for ship_type in ShipType:
            coords = [Coordinates(row=row, col=i) for i in range(ship_type.size)]
            placement = ShipPlacement(ship_type=ship_type, coordinates=coords)
            ship_placements.append(placement)
            row += 1

        # Verify all ships are placed correctly
        assert len(ship_placements) == 5
        total_coordinates = sum(len(p.coordinates) for p in ship_placements)
        expected_total = sum(ship.size for ship in ShipType)
        assert total_coordinates == expected_total

    def test_model_serialization(self):
        """Test that models can be serialized and deserialized."""
        # Test Coordinates
        coords = Coordinates(row=3, col=5)
        coords_dict = (
            coords.model_dump() if hasattr(coords, "model_dump") else coords.dict()
        )
        new_coords = Coordinates(**coords_dict)
        assert new_coords == coords

        # Test ShipPlacement
        placement = ShipPlacement(
            ship_type=ShipType.DESTROYER,
            coordinates=[Coordinates(row=0, col=0), Coordinates(row=0, col=1)],
        )
        placement_dict = (
            placement.model_dump()
            if hasattr(placement, "model_dump")
            else placement.dict()
        )
        new_placement = ShipPlacement(**placement_dict)
        assert new_placement.ship_type == placement.ship_type
        assert len(new_placement.coordinates) == len(placement.coordinates)

    def test_coordinates_in_placement_bounds(self):
        """Test that all coordinates in placements are within board bounds."""
        # Test edge placements
        edge_cases = [
            # Top edge horizontal
            [Coordinates(row=0, col=i) for i in range(3)],
            # Bottom edge horizontal
            [Coordinates(row=9, col=i) for i in range(3)],
            # Left edge vertical
            [Coordinates(row=i, col=0) for i in range(3)],
            # Right edge vertical
            [Coordinates(row=i, col=9) for i in range(3)],
        ]

        for coords in edge_cases:
            placement = ShipPlacement(ship_type=ShipType.CRUISER, coordinates=coords)

            # Verify all coordinates are in bounds
            for coord in placement.coordinates:
                assert 0 <= coord.row <= 9
                assert 0 <= coord.col <= 9
