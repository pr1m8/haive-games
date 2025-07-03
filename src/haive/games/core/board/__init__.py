"""Board - TODO: Add brief description

TODO: Add detailed description of module functionality


Key Components:
    * Classes: Space, GridSpace, HexSpace
    * Functions: is_occupied, place_piece, remove_piece


Example:
    Basic usage::

        from haive.board import Space

        instance = Space()
        # TODO: Complete example


"""

from __future__ import annotations

import random
import uuid
from abc import ABC, abstractmethod
from collections import defaultdict
from collections.abc import Callable, Iterable, Mapping, Sequence
from enum import Enum
from functools import cached_property
from typing import (
    Any,
    Dict,
    FrozenSet,
    Generic,
    List,
    Optional,
    Protocol,
    Set,
    Tuple,
    TypeVar,
    Union,
    cast,
)

from pydantic import BaseModel, Field, computed_field, field_validator, model_validator

# Type variables for generic relationships
T = TypeVar("T", bound="GamePiece")
P = TypeVar("P", bound="Position")
S = TypeVar("S", bound="Space")
B = TypeVar("B", bound="Board")
C = TypeVar("C", bound="GamePieceContainer")

# ======================================================
# POSITION TYPES - How locations are represented in games
# ======================================================


# ======================================================
# SPACES - Locations on a board where pieces can be placed
# ======================================================


class Space(BaseModel, Generic[P, T]):
    """Base class for spaces on a board where pieces can be placed."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    position: P
    piece: T | None = None
    properties: dict[str, Any] = Field(default_factory=dict)
    connections: set[str] = Field(default_factory=set)  # IDs of connected spaces

    def is_occupied(self) -> bool:
        """Check if this space is occupied."""
        return self.piece is not None

    def place_piece(self, piece: T) -> bool:
        """Place a piece on this space if it's empty."""
        if not self.is_occupied():
            self.piece = piece
            if piece and hasattr(piece, "position"):
                piece.position = self.position  # Update piece's position
            return True
        return False

    def remove_piece(self) -> T | None:
        """Remove and return the piece from this space."""
        piece = self.piece
        self.piece = None
        return piece

    def has_property(self, key: str) -> bool:
        """Check if this space has a specific property."""
        return key in self.properties

    def get_property(self, key: str, default: Any = None) -> Any:
        """Get a property value."""
        return self.properties.get(key, default)


class GridSpace(Space[GridPosition, T]):
    """A space on a grid-based board."""

    position: GridPosition

    @computed_field
    @property
    def coordinates(self) -> tuple[int, int]:
        """Get the row and column as a tuple."""
        return (self.position.row, self.position.col)


class HexSpace(Space[HexPosition, T]):
    """A space on a hexagonal grid."""

    position: HexPosition

    @computed_field
    @property
    def coordinates(self) -> tuple[int, int]:
        """Get the hex coordinates as a tuple (q, r)."""
        return (self.position.q, self.position.r)

    @computed_field
    @property
    def cube_coords(self) -> tuple[int, int, int]:
        """Get cube coordinates as a tuple (q, r, s)."""
        return (self.position.q, self.position.r, self.position.s)


class NodeSpace(Space[NodePosition, T]):
    """A space on a graph-based board (e.g., Ticket to Ride)."""

    position: NodePosition
    name: str | None = None  # Descriptive name (e.g., city name)


# ======================================================
# BOARDS - Collections of spaces with game-specific layout
# ======================================================


class Board(BaseModel, Generic[S, P, T]):
    """Base class for all game boards."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    spaces: dict[str, S] = Field(default_factory=dict)  # space_id -> Space
    properties: dict[str, Any] = Field(default_factory=dict)

    def add_space(self, space: S) -> str:
        """Add a space to the board."""
        self.spaces[space.id] = space
        return space.id

    def connect_spaces(self, space1_id: str, space2_id: str) -> None:
        """Connect two spaces bidirectionally."""
        if space1_id not in self.spaces or space2_id not in self.spaces:
            raise ValueError("Both spaces must exist on the board")

        self.spaces[space1_id].connections.add(space2_id)
        self.spaces[space2_id].connections.add(space1_id)

    def get_connected_spaces(self, space_id: str) -> list[S]:
        """Get all spaces connected to the given space."""
        if space_id not in self.spaces:
            raise ValueError(f"Space {space_id} not found")

        space = self.spaces[space_id]
        return [
            self.spaces[conn_id]
            for conn_id in space.connections
            if conn_id in self.spaces
        ]

    @abstractmethod
    def get_space_at_position(self, position: P) -> S | None:
        """Get the space at the specified position."""

    def place_piece(self, piece: T, position: P) -> bool:
        """Place a piece at the specified position."""
        space = self.get_space_at_position(position)
        if not space:
            return False

        if hasattr(piece, "can_move_to") and callable(piece.can_move_to):
            if not piece.can_move_to(position, self):
                return False

        return space.place_piece(piece)

    def remove_piece(self, position: P) -> T | None:
        """Remove a piece from the specified position."""
        space = self.get_space_at_position(position)
        if not space:
            return None

        return space.remove_piece()

    def is_position_valid(self, position: P) -> bool:
        """Check if a position is valid on this board."""
        return self.get_space_at_position(position) is not None

    def get_all_pieces(self) -> dict[str, T]:
        """Get all pieces currently on the board."""
        pieces: dict[str, T] = {}
        for space in self.spaces.values():
            if space.piece is not None and hasattr(space.piece, "id"):
                pieces[space.piece.id] = space.piece
        return pieces

    def get_player_pieces(self, player_id: str) -> list[T]:
        """Get all pieces belonging to a specific player."""
        return [
            space.piece
            for space in self.spaces.values()
            if space.piece is not None
            and hasattr(space.piece, "owner_id")
            and space.piece.owner_id == player_id
        ]


class GridBoard(Board[GridSpace[T], GridPosition, T]):
    """A grid-based board (Chess, Checkers, Scrabble)."""

    rows: int
    cols: int

    @field_validator("rows", "cols")
    @classmethod
    def validate_dimensions(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("Board dimensions must be positive")
        return v

    def get_space_at_position(self, position: GridPosition) -> GridSpace[T] | None:
        """Get the space at the specified grid coordinates."""
        for space in self.spaces.values():
            if (
                isinstance(space.position, GridPosition)
                and space.position.row == position.row
                and space.position.col == position.col
            ):
                return space
        return None

    def get_space_at(self, row: int, col: int) -> GridSpace[T] | None:
        """Get the space at the specified grid coordinates."""
        return self.get_space_at_position(GridPosition(row=row, col=col))

    def initialize_grid(self) -> None:
        """Initialize a standard grid with the specified dimensions."""
        for row in range(self.rows):
            for col in range(self.cols):
                position = GridPosition(row=row, col=col)
                space = GridSpace[T](position=position)
                self.add_space(space)

                # Connect to adjacent spaces
                for dr, dc in [(0, 1), (1, 0)]:  # right and down
                    adj_row, adj_col = row + dr, col + dc
                    if 0 <= adj_row < self.rows and 0 <= adj_col < self.cols:
                        # Find adjacent space
                        adj_space = self.get_space_at(adj_row, adj_col)
                        if adj_space:
                            self.connect_spaces(space.id, adj_space.id)

    def is_position_valid(self, position: GridPosition) -> bool:
        """Check if a position is within the grid bounds."""
        return 0 <= position.row < self.rows and 0 <= position.col < self.cols

    @computed_field
    @property
    def size(self) -> int:
        """Get the total number of spaces on the board."""
        return self.rows * self.cols


class HexBoard(Board[HexSpace[T], HexPosition, T]):
    """A hexagonal grid board (Settlers of Catan)."""

    radius: int  # Number of rings from center

    @field_validator("radius")
    @classmethod
    def validate_radius(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("Radius must be positive")
        return v

    def get_space_at_position(self, position: HexPosition) -> HexSpace[T] | None:
        """Get the space at the specified hex coordinates."""
        for space in self.spaces.values():
            if (
                isinstance(space.position, HexPosition)
                and space.position.q == position.q
                and space.position.r == position.r
            ):
                return space
        return None

    def get_space_at(self, q: int, r: int) -> HexSpace[T] | None:
        """Get the space at the specified hex coordinates."""
        return self.get_space_at_position(HexPosition(q=q, r=r))

    def initialize_hex_grid(self) -> None:
        """Initialize a hexagonal grid with the specified radius."""
        # Create all spaces
        for q in range(-self.radius, self.radius + 1):
            r_min = max(-self.radius, -q - self.radius)
            r_max = min(self.radius, -q + self.radius)
            for r in range(r_min, r_max + 1):
                position = HexPosition(q=q, r=r)
                space = HexSpace[T](position=position)
                self.add_space(space)

        # Connect adjacent spaces
        directions = [(1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1)]
        for space in self.spaces.values():
            pos = space.position
            for dq, dr in directions:
                adj_pos = HexPosition(q=pos.q + dq, r=pos.r + dr)
                adj_space = self.get_space_at_position(adj_pos)
                if adj_space:
                    self.connect_spaces(space.id, adj_space.id)

    def is_position_valid(self, position: HexPosition) -> bool:
        """Check if a position is within the hex grid bounds."""
        # In axial coordinates, valid positions satisfy -radius ≤ q, r, s ≤ radius
        # where s = -q - r, and |q| + |r| + |s| = 2*radius
        s = -position.q - position.r
        return (
            abs(position.q) <= self.radius
            and abs(position.r) <= self.radius
            and abs(s) <= self.radius
        )


class GraphBoard(Board[NodeSpace[T], NodePosition, T]):
    """A graph-based board (Ticket to Ride, Pandemic)."""

    def get_space_at_position(self, position: NodePosition) -> NodeSpace[T] | None:
        """Get the space at the specified node."""
        for space in self.spaces.values():
            if (
                isinstance(space.position, NodePosition)
                and space.position.node_id == position.node_id
            ):
                return space
        return None

    def get_space_by_name(self, name: str) -> NodeSpace[T] | None:
        """Get a space by its name."""
        for space in self.spaces.values():
            if space.name == name:
                return space
        return None

    def add_edge(
        self, node1_id: str, node2_id: str, properties: dict[str, Any] | None = None
    ) -> None:
        """Connect two nodes with optional edge properties."""
        self.connect_spaces(node1_id, node2_id)

        # Store edge properties if provided
        if properties:
            edge_key = f"{node1_id}:{node2_id}"
            self.properties[edge_key] = properties

            # Also store for reverse direction
            reverse_key = f"{node2_id}:{node1_id}"
            self.properties[reverse_key] = properties

    def get_edge_properties(self, node1_id: str, node2_id: str) -> dict[str, Any]:
        """Get properties of an edge between two nodes."""
        edge_key = f"{node1_id}:{node2_id}"
        return self.properties.get(edge_key, {})
