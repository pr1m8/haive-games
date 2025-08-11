"""Go game state management module.

This module provides comprehensive state management functionality for the ancient
strategy game of Go (also known as Weiqi or Baduk), including move validation,
stone capture mechanics, and game progression tracking.

Go is an abstract strategy board game for two players in which the aim is to
surround more territory than the opponent. The game is played on a 19×19 grid
(though 13×13 and 9×9 are common variants) where players alternate placing black
and white stones. Players capture opponents' stones by completely surrounding them.

Classes:
    GoGameStateManager: Main state management class for Go game operations.

Example:
    Basic Go game setup and play:

        >>> from haive.games.go.state_manager import GoGameStateManager
        >>> from haive.games.go.models import GoMove
        >>>
        >>> # Initialize standard 19×19 Go game
        >>> state = GoGameStateManager.initialize(board_size=19)
        >>> print(f"Board size: {state.board_size}×{state.board_size}")
        >>> print(f"Current player: {state.turn}")  # "black"
        >>>
        >>> # Make a move (place stone at coordinates)
        >>> move_coords = (3, 4)  # (row, col)
        >>> new_state = GoGameStateManager.apply_move(state, move_coords)
        >>> print(f"Stone placed at {move_coords}")
        >>>
        >>> # Pass turn (no stone placed)
        >>> pass_state = GoGameStateManager.apply_move(new_state, None)
        >>> print(f"Pass count: {pass_state.passes}")

Note:
    - Standard board sizes: 19×19 (professional), 13×13, 9×9 (beginners)
    - Players are "black" and "white" with black moving first
    - Coordinates are (row, col) tuples using 0-based indexing
    - Pass moves are represented as None coordinates
    - Game ends when both players pass consecutively
    - Stone capture follows the rule of liberty (breathing spaces)
    - Uses Sente library for Go game logic and SGF format
"""

from haive.games.go import go_engine as sente
from haive.games.go.state import GoGameState


class GoGameStateManager:
    """Manager class for Go game state operations.

    This class provides static methods for initializing and modifying
    Go game states, including:
        - Game initialization
        - Move application and validation
        - Pass move handling
        - Game end detection

    Example:
        >>> # Initialize a new game
        >>> state = GoGameStateManager.initialize(board_size=19)
        >>>
        >>> # Apply a move
        >>> new_state = GoGameStateManager.apply_move(state, (3, 4))
        >>> print(new_state.turn)  # 'white'

    """

    @staticmethod
    def initialize(board_size: int = 19) -> GoGameState:
        """Initialize a new Go game state.

        Args:
            board_size (int): Size of the board (default: 19).

        Returns:
            GoGameState: Initial game state.

        Example:
            >>> state = GoGameStateManager.initialize(board_size=13)
            >>> print(state.board_size)  # 13
            >>> print(state.turn)  # 'black'

        """
        game = sente.Game(board_size)
        return GoGameState(board_sgf=sente.sgf.dumps(game), turn="black")

    @staticmethod
    def apply_move(state: GoGameState, move: tuple[int, int] | None) -> GoGameState:
        """Apply a move to the current game state.

        This method handles:
            - Move validation and application
            - Pass moves (when move is None)
            - Capture counting
            - Turn alternation
            - Game end detection

        Args:
            state (GoGameState): Current game state.
            move (Optional[Tuple[int, int]]): Move coordinates or None for pass.

        Returns:
            GoGameState: New game state after applying the move.

        Example:
            >>> state = GoGameStateManager.initialize()
            >>> # Play a move at (3, 4)
            >>> new_state = GoGameStateManager.apply_move(state, (3, 4))
            >>> print(new_state.turn)  # 'white'
            >>>
            >>> # Pass move
            >>> pass_state = GoGameStateManager.apply_move(new_state, None)
            >>> print(pass_state.passes)  # 1

        """
        game = sente.sgf.loads(state.board_sgf)
        player = state.turn  # Current player

        # Handle pass move
        if move is None:
            new_passes = state.passes + 1
            return GoGameState(
                **state.dict(),
                turn="white" if player == "black" else "black",
                passes=new_passes,
                game_status="ended" if new_passes >= 2 else "ongoing",
                game_result="Draw" if new_passes >= 2 else None,
            )

        new_passes = 0  # Reset pass count

        try:
            color = "b" if player == "black" else "w"
            game.play_move(color, move)
        except Exception as e:
            return GoGameState(**state.dict(), error_message=f"Invalid move: {e!s}")

        # Capture tracking (simplified for now)
        captured_count = 0

        return GoGameState(
            board_sgf=sente.sgf.dumps(game),
            move_history=state.move_history + [(player, move)],
            captured_stones={
                "black": state.captured_stones["black"]
                + (captured_count if player == "white" else 0),
                "white": state.captured_stones["white"]
                + (captured_count if player == "black" else 0),
            },
            turn="white" if player == "black" else "black",
            passes=new_passes,
            game_status="ongoing",
            game_result=None,
        )
