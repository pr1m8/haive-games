"""State manager for Flow Free game logic and mechanics.

This module handles game initialization, move validation, and state transitions for the
Flow Free puzzle game.

"""

import random

from haive.games.single_player.base import (
    GameDifficulty,
    PlayerType,
    SinglePlayerStateManager,
)
from haive.games.single_player.flow_free.models import (
    FlowFreeMove,
    PipeDirection,
    Position,
)
from haive.games.single_player.flow_free.state import (
    Cell,
    Flow,
    FlowEndpoint,
    FlowFreeState,
)


class FlowFreeStateManager(SinglePlayerStateManager[FlowFreeState]):
    """Manager for Flow Free game state."""

    # Sample puzzles of different sizes
    SAMPLE_PUZZLES = {
        "5x5_easy": [
            ("red", (0, 0), (4, 4)),
            ("blue", (0, 4), (4, 0)),
            ("green", (1, 1), (3, 3)),
            ("yellow", (1, 3), (3, 1)),
        ],
        "5x5_medium": [
            ("red", (0, 0), (4, 4)),
            ("blue", (0, 4), (4, 0)),
            ("green", (1, 1), (3, 3)),
            ("yellow", (1, 3), (3, 1)),
            ("purple", (2, 0), (2, 4)),
        ],
        "6x6_easy": [
            ("red", (0, 0), (5, 5)),
            ("blue", (0, 5), (5, 0)),
            ("green", (1, 1), (4, 4)),
            ("yellow", (1, 4), (4, 1)),
            ("purple", (2, 2), (3, 3)),
        ],
        "7x7_medium": [
            ("red", (0, 0), (6, 6)),
            ("blue", (0, 6), (6, 0)),
            ("green", (1, 1), (5, 5)),
            ("yellow", (1, 5), (5, 1)),
            ("purple", (2, 2), (4, 4)),
            ("orange", (2, 4), (4, 2)),
            ("cyan", (3, 0), (3, 6)),
        ],
    }

    @classmethod
    def initialize(
        cls,
        difficulty: GameDifficulty = GameDifficulty.MEDIUM,
        player_type: PlayerType = PlayerType.LLM,
        rows: int = 5,
        cols: int = 5,
        num_flows: int | None = None,
        **kwargs,
    ) -> FlowFreeState:
        """Initialize a new Flow Free game state.

        Args:
            difficulty: Difficulty level of the game.
            player_type: Type of player.
            rows: Number of rows in the grid.
            cols: Number of columns in the grid.
            num_flows: Number of flows to include. If None, determined by difficulty.
            **kwargs: Additional initialization parameters.

        Returns:
            A new Flow Free game state.

        """
        # Determine board size and flows based on difficulty
        if difficulty == GameDifficulty.EASY:
            puzzle_key = "5x5_easy"
            if rows == 6:
                puzzle_key = "6x6_easy"
        elif difficulty == GameDifficulty.MEDIUM:
            puzzle_key = "5x5_medium"
            if rows == 7:
                puzzle_key = "7x7_medium"
        else:  # HARD or EXPERT
            # For now, use medium puzzles but could add harder ones
            puzzle_key = "7x7_medium"

        # Create initial state
        state = FlowFreeState(
            player_type=player_type,
            difficulty=difficulty,
            rows=rows,
            cols=cols,
            grid=[],
            flows={},
            game_status="ongoing",
        )

        # Initialize the grid
        state.grid = [
            [Cell(position=Position(row=r, col=c)) for c in range(cols)]
            for r in range(rows)
        ]

        # Add flows based on the selected puzzle
        puzzle_flows = cls.SAMPLE_PUZZLES.get(
            puzzle_key, cls.SAMPLE_PUZZLES["5x5_easy"]
        )

        # Limit flows if requested
        if num_flows is not None:
            puzzle_flows = puzzle_flows[:num_flows]

        for color, start_coords, end_coords in puzzle_flows:
            start_pos = Position(row=start_coords[0], col=start_coords[1])
            end_pos = Position(row=end_coords[0], col=end_coords[1])

            # Create flow
            flow = Flow(
                color=color,
                start=FlowEndpoint(position=start_pos, is_start=True),
                end=FlowEndpoint(position=end_pos, is_start=False),
            )

            # Add flow to state
            state.flows[flow.id] = flow

            # Mark endpoints in grid
            start_cell = state.get_cell(start_pos)
            end_cell = state.get_cell(end_pos)

            if start_cell and end_cell:
                start_cell.flow_id = flow.id
                start_cell.is_endpoint = True

                end_cell.flow_id = flow.id
                end_cell.is_endpoint = True

        return state

    @classmethod
    def get_legal_moves(cls, state: FlowFreeState) -> list[FlowFreeMove]:
        """Get all legal moves for the current state.

        Args:
            state: Current game state.

        Returns:
            List of all legal moves.

        """
        legal_moves = []

        # If game is over, no legal moves
        if state.game_status != "ongoing":
            return []

        # For each flow that's not completed
        for flow_id, flow in state.flows.items():
            if flow.completed:
                continue

            # Find potential next positions
            potential_positions = cls._get_potential_positions(state, flow_id)

            # Add legal moves for this flow
            for position in potential_positions:
                legal_moves.append(FlowFreeMove(flow_id=flow_id, position=position))

        return legal_moves

    @classmethod
    def _get_potential_positions(
        cls, state: FlowFreeState, flow_id: str
    ) -> list[Position]:
        """Get potential positions for the next segment of a flow.

        Args:
            state: Current game state.
            flow_id: ID of the flow to extend.

        Returns:
            List of potential positions.

        """
        flow = state.flows.get(flow_id)
        if not flow:
            return []

        # If flow has no path yet, can only start from the endpoints
        if not flow.path:
            positions = []

            # Check adjacent positions to the start endpoint
            for pos in state.get_adjacent_positions(flow.start.position):
                if state.is_cell_empty(pos):
                    positions.append(pos)

            # Check adjacent positions to the end endpoint
            for pos in state.get_adjacent_positions(flow.end.position):
                if state.is_cell_empty(pos):
                    positions.append(pos)

            return positions

        # If flow has path segments, can only extend from the last segment
        last_pos = flow.path[-1]
        positions = []

        # Check adjacent positions to the last segment
        for pos in state.get_adjacent_positions(last_pos):
            # Must be empty or the other endpoint
            cell = state.get_cell(pos)
            if cell and (
                cell.flow_id is None or (cell.is_endpoint and cell.flow_id == flow_id)
            ):
                positions.append(pos)

        return positions

    @classmethod
    def apply_move(cls, state: FlowFreeState, move: FlowFreeMove) -> FlowFreeState:
        """Apply a move to the current state.

        Args:
            state: Current game state.
            move: Move to apply.

        Returns:
            Updated game state.

        Raises:
            ValueError: If the move is invalid.

        """
        # Create a copy of the state
        new_state = state.model_copy(deep=True)

        # Validate move
        flow = new_state.flows.get(move.flow_id)
        if not flow:
            raise ValueError(f"Invalid flow ID: {move.flow_id}")

        # Check if the target cell is valid
        cell = new_state.get_cell(move.position)
        if not cell:
            raise ValueError(f"Invalid position: {move.position}")

        # Cell must be empty or the endpoint of this flow
        if cell.flow_id is not None and not (
            cell.is_endpoint and cell.flow_id == move.flow_id
        ):
            raise ValueError(f"Cell already occupied: {move.position}")

        # Check if move connects to existing flow
        is_valid_connection = False

        # If no path yet, must connect to an endpoint
        if not flow.path:
            is_adjacent_to_start = any(
                p == move.position
                for p in new_state.get_adjacent_positions(flow.start.position)
            )
            is_adjacent_to_end = any(
                p == move.position
                for p in new_state.get_adjacent_positions(flow.end.position)
            )

            if is_adjacent_to_start or is_adjacent_to_end:
                is_valid_connection = True
        else:
            # Must connect to the last path segment
            last_pos = flow.path[-1]
            is_adjacent_to_last = any(
                p == move.position for p in new_state.get_adjacent_positions(last_pos)
            )

            if is_adjacent_to_last:
                is_valid_connection = True

        if not is_valid_connection:
            raise ValueError(f"Invalid connection: {move.position}")

        # Apply the move
        if cell.is_endpoint and cell.flow_id == move.flow_id:
            # Completing the flow
            flow.completed = True
        else:
            # Add to the path
            flow.path.append(move.position)

            # Mark the cell
            cell.flow_id = move.flow_id
            cell.is_endpoint = False

            # Determine pipe direction
            if flow.path:
                cell.pipe_direction = cls._calculate_pipe_direction(
                    prev_pos=(
                        flow.path[-2]
                        if len(flow.path) > 1
                        else (
                            flow.start.position
                            if flow.path[0] != flow.start.position
                            else flow.end.position
                        )
                    ),
                    curr_pos=move.position,
                )

        # Check if flow is completed by checking for a path from start to end
        if not flow.completed:
            flow.completed = cls._is_flow_completed(new_state, flow)

        # Check if puzzle is solved
        if new_state.is_solved:
            new_state.game_status = "victory"

        # Add move to history
        new_state.move_history.append(move.model_dump())
        new_state.move_count += 1

        # Set current flow ID
        new_state.current_flow_id = move.flow_id

        return new_state

    @classmethod
    def _calculate_pipe_direction(
        cls, prev_pos: Position, curr_pos: Position
    ) -> PipeDirection:
        """Calculate the direction of a pipe segment.

        Args:
            prev_pos: Previous position in the path.
            curr_pos: Current position in the path.

        Returns:
            Direction of the pipe.

        """
        if prev_pos.row < curr_pos.row:
            return PipeDirection.DOWN
        if prev_pos.row > curr_pos.row:
            return PipeDirection.UP
        if prev_pos.col < curr_pos.col:
            return PipeDirection.RIGHT
        if prev_pos.col > curr_pos.col:
            return PipeDirection.LEFT
        return PipeDirection.NONE

    @classmethod
    def _is_flow_completed(cls, state: FlowFreeState, flow: Flow) -> bool:
        """Check if a flow is completed.

        A flow is completed if there's a path from the start endpoint to the end endpoint.

        Args:
            state: Current game state.
            flow: Flow to check.

        Returns:
            True if the flow is completed, False otherwise.

        """
        # If we already know it's completed
        if flow.completed:
            return True

        # Using BFS to find a path
        visited = set()
        queue = [flow.start.position]

        while queue:
            current_pos = queue.pop(0)

            # If we've reached the end, flow is completed
            if (
                current_pos.row == flow.end.position.row
                and current_pos.col == flow.end.position.col
            ):
                return True

            # Skip positions we've already visited
            pos_key = (current_pos.row, current_pos.col)
            if pos_key in visited:
                continue

            visited.add(pos_key)

            # Add adjacent positions that are part of this flow
            for adj_pos in state.get_adjacent_positions(current_pos):
                cell = state.get_cell(adj_pos)
                if cell and cell.flow_id == flow.id:
                    queue.append(adj_pos)

        # No path found
        return False

    @classmethod
    def check_game_status(cls, state: FlowFreeState) -> FlowFreeState:
        """Check and update the game status.

        Args:
            state: Current game state.

        Returns:
            Updated game state with status checked.

        """
        # Create a copy of the state
        new_state = state.model_copy(deep=True)

        # Check if all flows are completed
        all_completed = all(flow.completed for flow in new_state.flows.values())

        # Check if all cells are filled
        all_filled = all(
            cell.flow_id is not None for row in new_state.grid for cell in row
        )

        # Update game status
        if all_completed and all_filled:
            new_state.game_status = "victory"

        return new_state

    @classmethod
    def generate_hint(cls, state: FlowFreeState) -> tuple[FlowFreeState, str]:
        """Generate a hint for the current game state.

        Args:
            state: Current game state.

        Returns:
            Tuple of (updated state, hint text).

        """
        # Create a copy of the state
        new_state = state.model_copy(deep=True)
        new_state.hint_count += 1

        # Find incomplete flows
        incomplete_flows = [
            flow_id for flow_id, flow in new_state.flows.items() if not flow.completed
        ]

        # No incomplete flows
        if not incomplete_flows:
            return new_state, "All flows are already complete!"

        # Choose a flow to hint about
        hint_flow_id = random.choice(incomplete_flows)
        hint_flow = new_state.flows[hint_flow_id]

        # Get potential next positions
        potential_positions = cls._get_potential_positions(new_state, hint_flow_id)

        if not potential_positions:
            return (
                new_state,
                f"No valid moves for the {hint_flow.color} flow. Try another flow.",
            )

        # Create hint text
        if not hint_flow.path:
            hint = (
                f"Try extending the {hint_flow.color} flow from one of its endpoints. "
                f"Look at positions {', '.join(str(p) for p in potential_positions)}."
            )
        else:
            hint = (
                f"Continue the {hint_flow.color} flow from its current end. "
                f"Valid next positions: {
                    ', '.join(str(p) for p in potential_positions)
                }."
            )

        return new_state, hint

    @classmethod
    def interactive_input(cls, state: FlowFreeState, user_input: str) -> FlowFreeState:
        """Process interactive input from the player.

        Args:
            state: Current game state.
            user_input: User input string.

        Returns:
            Updated game state.

        """
        # Handle common commands first
        new_state = super().interactive_input(state, user_input)

        # If common command was handled, return
        if new_state.error_message:
            return new_state

        # Process game-specific commands
        input_parts = user_input.strip().lower().split()

        # Command to select a flow: "flow <color>"
        if len(input_parts) == 2 and input_parts[0] == "flow":
            color_name = input_parts[1]
            for flow_id, flow in new_state.flows.items():
                if flow.color.lower() == color_name:
                    new_state.current_flow_id = flow_id
                    new_state.error_message = f"Selected {flow.color} flow"
                    return new_state

            new_state.error_message = f"No flow with color {color_name}"
            return new_state

        # Command to make a move: "move <row> <col>"
        if len(input_parts) == 3 and input_parts[0] == "move":
            try:
                row = int(input_parts[1])
                col = int(input_parts[2])

                # Check if coordinates are valid
                if 0 <= row < new_state.rows and 0 <= col < new_state.cols:
                    # Check if current flow is selected
                    if not new_state.current_flow_id:
                        new_state.error_message = (
                            "No flow selected. Use 'flow <color>' first."
                        )
                        return new_state

                    position = Position(row=row, col=col)
                    move = FlowFreeMove(
                        flow_id=new_state.current_flow_id, position=position
                    )

                    try:
                        # Apply the move
                        new_state = cls.apply_move(new_state, move)
                        return new_state
                    except ValueError as e:
                        new_state.error_message = str(e)
                        return new_state
                else:
                    new_state.error_message = "Invalid coordinates"
                    return new_state
            except ValueError:
                new_state.error_message = "Invalid move format. Use 'move <row> <col>'"
                return new_state

        # Command to show the board: "board"
        if user_input.strip().lower() == "board":
            new_state.error_message = "\n" + new_state.to_display_string()
            return new_state

        # Command to list flows: "flows"
        if user_input.strip().lower() == "flows":
            flow_list = []
            for flow_id, flow in new_state.flows.items():
                status = "✓" if flow.completed else " "
                flow_list.append(
                    f" {status} {flow.color}: {flow.start.position} → {
                        flow.end.position
                    }"
                )

            new_state.error_message = "Flows:\n" + "\n".join(flow_list)
            return new_state

        # Command to restart: "restart"
        if user_input.strip().lower() == "restart":
            # Initialize a new game with the same parameters
            reset_state = cls.initialize(
                difficulty=new_state.difficulty,
                player_type=new_state.player_type,
                rows=new_state.rows,
                cols=new_state.cols,
            )

            # Copy over the puzzle ID to track that it's the same puzzle
            reset_state.puzzle_id = new_state.puzzle_id

            return reset_state

        # Unknown command
        new_state.error_message = f"Unknown command: {user_input}"
        return new_state
