from __future__ import annotations

"""Base core module.

This module provides base functionality for the Haive framework.

Classes:
    PipeDirection: PipeDirection implementation.
    EndpointType: EndpointType implementation.
    FlowPiece: FlowPiece implementation.

Functions:
    validate_color: Validate Color functionality.
    can_move_to: Can Move To functionality.
    can_move_to: Can Move To functionality.
"""


import uuid
from enum import Enum
from typing import Literal

# Import from our base framework
from game_framework_base import (
    Board,
    Game,
    GamePiece,
    GridBoard,
    GridPosition,
    GridSpace,
)
from pydantic import BaseModel, Field, computed_field, field_validator

# ======================================================
# FLOW FREE TYPES AND CONSTANTS
# ======================================================


class PipeDirection(str, Enum):
    """Direction of a pipe segment."""

    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    NONE = "none"  # For endpoints


ConnectionType = Literal["endpoint", "pipe"]


class EndpointType(str, Enum):
    """Type of endpoint."""

    START = "start"
    END = "end"


# ======================================================
# FLOW FREE PIECES
# ======================================================


class FlowPiece(GamePiece[GridPosition]):
    """Base class for Flow Free pieces (endpoints and pipes)."""

    color: str
    flow_id: str  # ID to group related pieces in the same flow
    connection_type: ConnectionType

    @field_validator("color")
    @classmethod
    def validate_color(cls, v: str) -> str:
        """Validate color format."""
        # Allow color names or hex codes
        if not v:
            raise ValueError("Color cannot be empty")
        return v


class FlowEndpoint(FlowPiece):
    """An endpoint (colored dot) in Flow Free."""

    connection_type: Literal[ConnectionType] = "endpoint"
    endpoint_type: EndpointType

    def can_move_to(self, position: GridPosition, board: Board) -> bool:
        """Endpoints can't be moved in Flow Free."""
        return False


class FlowPipe(FlowPiece):
    """A pipe segment in Flow Free."""

    connection_type: Literal[ConnectionType] = "pipe"
    direction: PipeDirection
    connected_directions: set[PipeDirection] = Field(default_factory=set)

    def can_move_to(self, position: GridPosition, board: FlowBoard) -> bool:
        """Check if this pipe segment can be placed at the specified
        position.
        """
        # Get the target space
        space = board.get_space_at_position(position)
        if not space:
            return False

        # Space must be empty
        if space.is_occupied():
            return False

        # Must be adjacent to either an endpoint or another pipe of the same flow
        adjacent_positions = board.get_adjacent_positions(position)
        for adj_pos in adjacent_positions:
            adj_space = board.get_space_at_position(adj_pos)
            if adj_space and adj_space.is_occupied():
                piece = adj_space.piece
                if isinstance(piece, FlowPiece) and piece.flow_id == self.flow_id:
                    return True

        return False

    @computed_field
    @property
    def is_corner(self) -> bool:
        """Check if this pipe forms a corner."""
        if len(self.connected_directions) != 2:
            return False

        # Horizontal and vertical connections indicate a corner
        horizontal = {PipeDirection.LEFT, PipeDirection.RIGHT}
        vertical = {PipeDirection.UP, PipeDirection.DOWN}

        horiz_connection = any(d in horizontal for d in self.connected_directions)
        vert_connection = any(d in vertical for d in self.connected_directions)

        return horiz_connection and vert_connection


# ======================================================
# FLOW FREE SPACES
# ======================================================


class FlowGridSpace(GridSpace[FlowPiece]):
    """A space on a Flow Free board."""

    @computed_field
    @property
    def has_endpoint(self) -> bool:
        """Check if this space contains an endpoint."""
        return (
            self.piece is not None
            and isinstance(self.piece, FlowPiece)
            and self.piece.connection_type == "endpoint"
        )

    @computed_field
    @property
    def has_pipe(self) -> bool:
        """Check if this space contains a pipe."""
        return (
            self.piece is not None
            and isinstance(self.piece, FlowPiece)
            and self.piece.connection_type == "pipe"
        )

    @computed_field
    @property
    def color(self) -> str | None:
        """Get the color of the piece in this space."""
        if self.piece is None or not isinstance(self.piece, FlowPiece):
            return None
        return self.piece.color


# ======================================================
# FLOW FREE BOARD
# ======================================================


class FlowBoard(GridBoard[FlowGridSpace[FlowPiece], GridPosition, FlowPiece]):
    """A Flow Free game board."""

    flows: dict[str, dict[str, any]] = Field(default_factory=dict)

    def initialize_grid(self) -> None:
        """Initialize an empty grid."""
        # Create spaces for each cell
        for row in range(self.rows):
            for col in range(self.cols):
                position = GridPosition(row=row, col=col)
                space = FlowGridSpace[FlowPiece](position=position)
                self.add_space(space)

                # Connect to adjacent spaces
                for dr, dc in [
                    (0, 1),
                    (1, 0),
                    (0, -1),
                    (-1, 0),
                ]:  # right, down, left, up
                    adj_row, adj_col = row + dr, col + dc
                    if 0 <= adj_row < self.rows and 0 <= adj_col < self.cols:
                        # Find adjacent space
                        adj_space = self.get_space_at(adj_row, adj_col)
                        if adj_space:
                            self.connect_spaces(space.id, adj_space.id)

    def add_flow(
        self, color: str, start_pos: GridPosition, end_pos: GridPosition
    ) -> str:
        """Add a new flow (pair of endpoints) to the board."""
        flow_id = str(uuid.uuid4())

        # Create start endpoint
        start_endpoint = FlowEndpoint(
            color=color,
            flow_id=flow_id,
            position=start_pos,
            endpoint_type=EndpointType.START,
        )

        # Create end endpoint
        end_endpoint = FlowEndpoint(
            color=color,
            flow_id=flow_id,
            position=end_pos,
            endpoint_type=EndpointType.END,
        )

        # Place endpoints on the board
        self.place_piece(start_endpoint, start_pos)
        self.place_piece(end_endpoint, end_pos)

        # Store flow information
        self.flows[flow_id] = {
            "color": color,
            "start_pos": start_pos,
            "end_pos": end_pos,
            "completed": False,
            "path": [],
        }

        return flow_id

    def add_pipe_segment(
        self, flow_id: str, position: GridPosition, direction: PipeDirection
    ) -> bool:
        """Add a pipe segment to a flow."""
        if flow_id not in self.flows:
            return False

        # Get flow color
        color = self.flows[flow_id]["color"]

        # Create pipe segment
        pipe = FlowPipe(
            color=color, flow_id=flow_id, position=position, direction=direction
        )

        # Place pipe on the board
        result = self.place_piece(pipe, position)

        if result:
            # Update the flow's path
            self.flows[flow_id]["path"].append(position)

            # Update connections between adjacent pipes
            self._update_pipe_connections(position)

            # Check if the flow is now complete
            self._check_flow_completion(flow_id)

        return result

    def _update_pipe_connections(self, position: GridPosition) -> None:
        """Update the connections between pipes and endpoints."""
        space = self.get_space_at_position(position)
        if not space or not space.is_occupied():
            return

        piece = space.piece
        if not isinstance(piece, FlowPiece):
            return

        # Get adjacent spaces
        adjacent_positions = self.get_adjacent_positions(position)

        # Map directions to relative positions
        direction_map = {
            PipeDirection.UP: GridPosition(row=position.row - 1, col=position.col),
            PipeDirection.DOWN: GridPosition(row=position.row + 1, col=position.col),
            PipeDirection.LEFT: GridPosition(row=position.row, col=position.col - 1),
            PipeDirection.RIGHT: GridPosition(row=position.row, col=position.col + 1),
        }

        # Reverse direction map for connecting from the other side
        reverse_directions = {
            PipeDirection.UP: PipeDirection.DOWN,
            PipeDirection.DOWN: PipeDirection.UP,
            PipeDirection.LEFT: PipeDirection.RIGHT,
            PipeDirection.RIGHT: PipeDirection.LEFT,
        }

        # Check each adjacent space
        for direction, adj_pos in direction_map.items():
            if adj_pos in adjacent_positions:
                adj_space = self.get_space_at_position(adj_pos)
                if adj_space and adj_space.is_occupied():
                    adj_piece = adj_space.piece
                    if (
                        isinstance(adj_piece, FlowPiece)
                        and adj_piece.flow_id == piece.flow_id
                    ):
                        # Connect this piece to the adjacent piece
                        if isinstance(piece, FlowPipe):
                            piece.connected_directions.add(direction)

                        # Connect adjacent piece to this piece
                        if isinstance(adj_piece, FlowPipe):
                            adj_piece.connected_directions.add(
                                reverse_directions[direction]
                            )

    def _check_flow_completion(self, flow_id: str) -> bool:
        """Check if a flow is complete (connects the two endpoints)."""
        if flow_id not in self.flows:
            return False

        flow = self.flows[flow_id]

        # A flow is complete if there's a path from start to end
        start_pos = flow["start_pos"]
        end_pos = flow["end_pos"]

        # Check if there's a path using BFS
        visited = set()
        queue = [start_pos]

        while queue:
            current_pos = queue.pop(0)

            if current_pos == end_pos:
                # Found a path to the end
                flow["completed"] = True
                return True

            if current_pos in visited:
                continue

            visited.add(current_pos)

            # Get adjacent positions with the same flow
            adjacent_positions = self.get_adjacent_positions(current_pos)
            for adj_pos in adjacent_positions:
                adj_space = self.get_space_at_position(adj_pos)
                if (
                    adj_space
                    and adj_space.is_occupied()
                    and isinstance(adj_space.piece, FlowPiece)
                    and adj_space.piece.flow_id == flow_id
                ):
                    queue.append(adj_pos)

        # No path found
        flow["completed"] = False
        return False

    def get_adjacent_positions(self, position: GridPosition) -> list[GridPosition]:
        """Get all valid adjacent positions."""
        adjacent = []
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, down, left, up
            new_row, new_col = position.row + dr, position.col + dc
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                adjacent.append(GridPosition(row=new_row, col=new_col))
        return adjacent

    @computed_field
    @property
    def is_solved(self) -> bool:
        """Check if the puzzle is solved."""
        # All flows must be completed
        if not all(flow["completed"] for flow in self.flows.values()):
            return False

        # All spaces must be filled
        for space in self.spaces.values():
            if not space.is_occupied():
                return False

        return True


# ======================================================
# FLOW FREE GAME
# ======================================================


class FlowFreeMove(BaseModel):
    """A move in Flow Free."""

    flow_id: str
    position: GridPosition


class FlowFreeGame(Game[GridPosition, FlowPiece]):
    """Flow Free game controller."""

    board: FlowBoard
    current_flow_id: str | None = None

    def start_game(self) -> None:
        """Start the game."""
        super().start_game()
        self.board.initialize_grid()

    def add_flow(
        self, color: str, start_pos: GridPosition, end_pos: GridPosition
    ) -> str:
        """Add a new flow to the game."""
        return self.board.add_flow(color, start_pos, end_pos)

    def select_flow(self, flow_id: str) -> bool:
        """Select a flow to work with."""
        if flow_id in self.board.flows:
            self.current_flow_id = flow_id
            return True
        return False

    def is_valid_move(self, move: FlowFreeMove) -> bool:
        """Check if a move is valid."""
        if not self.current_flow_id:
            return False

        # Get the space at the position
        space = self.board.get_space_at_position(move.position)
        if not space:
            return False

        # Space must be empty unless it's the endpoint of the current flow
        if space.is_occupied():
            piece = space.piece
            if (
                not isinstance(piece, FlowEndpoint)
                or piece.flow_id != self.current_flow_id
            ):
                return False

        # Must be adjacent to existing flow pieces
        valid_connection = False
        adjacent_positions = self.board.get_adjacent_positions(move.position)

        for adj_pos in adjacent_positions:
            adj_space = self.board.get_space_at_position(adj_pos)
            if adj_space and adj_space.is_occupied():
                adj_piece = adj_space.piece
                if (
                    isinstance(adj_piece, FlowPiece)
                    and adj_piece.flow_id == self.current_flow_id
                ):
                    valid_connection = True
                    break

        return valid_connection

    def make_move(self, move: FlowFreeMove) -> bool:
        """Make a move in the game."""
        if self.status != "in_progress":
            return False

        # Use the current flow if not specified
        flow_id = move.flow_id if move.flow_id else self.current_flow_id

        if not flow_id:
            return False

        # Determine pipe direction
        direction = self._determine_pipe_direction(move.position)

        # Add pipe segment
        result = self.board.add_pipe_segment(flow_id, move.position, direction)

        if result:
            # Record the move
            self.moves.append(move.model_dump())

            # Check if the puzzle is solved
            if self.board.is_solved:
                self.status = "completed"

        return result

    def _determine_pipe_direction(self, position: GridPosition) -> PipeDirection:
        """Determine the direction of a pipe based on adjacent segments."""
        if not self.current_flow_id:
            return PipeDirection.NONE

        # Get adjacent pieces in the same flow
        adjacent_positions = self.board.get_adjacent_positions(position)
        connected_pieces = []

        for adj_pos in adjacent_positions:
            adj_space = self.board.get_space_at_position(adj_pos)
            if adj_space and adj_space.is_occupied():
                adj_piece = adj_space.piece
                if (
                    isinstance(adj_piece, FlowPiece)
                    and adj_piece.flow_id == self.current_flow_id
                ):
                    connected_pieces.append((adj_pos, adj_piece))

        # Determine direction based on connections
        if len(connected_pieces) == 1:
            # Only one connection - pipe will be straight
            adj_pos, _ = connected_pieces[0]

            if adj_pos.row < position.row:
                return PipeDirection.UP
            if adj_pos.row > position.row:
                return PipeDirection.DOWN
            if adj_pos.col < position.col:
                return PipeDirection.LEFT
            if adj_pos.col > position.col:
                return PipeDirection.RIGHT

        # For multiple connections or no connections, we'll just use NONE
        # (real game would need more logic here)
        return PipeDirection.NONE

    def reset(self) -> None:
        """Reset the game."""
        super().reset()
        self.board.initialize_grid()
        self.current_flow_id = None
        self.board.flows = {}


# ======================================================
# FLOW FREE LEVEL GENERATOR
# ======================================================


class FlowFreeLevel(BaseModel):
    """A pre-defined Flow Free level."""

    rows: int
    cols: int
    flows: list[tuple[str, tuple[int, int], tuple[int, int]]]  # color, start, end

    def create_game(self) -> FlowFreeGame:
        """Create a game from this level."""
        # Create board
        board = FlowBoard(
            name=f"Flow Free {self.rows}x{self.cols}", rows=self.rows, cols=self.cols
        )

        # Create game
        game = FlowFreeGame(name="Flow Free", board=board)
        game.start_game()

        # Add flows
        for color, start, end in self.flows:
            start_pos = GridPosition(row=start[0], col=start[1])
            end_pos = GridPosition(row=end[0], col=end[1])
            game.add_flow(color, start_pos, end_pos)

        return game
