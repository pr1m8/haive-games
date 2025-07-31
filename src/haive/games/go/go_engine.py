"""Simple Go engine wrapper using sgfmill instead of sente.

This module provides a compatibility layer to replace sente with sgfmill, which is
compatible with Python 3.12.

"""

import logging

import sgfmill.boards
import sgfmill.common
import sgfmill.sgf

# Handle optional sgfmill dependency
try:
    SGFMILL_AVAILABLE = True
except ImportError:
    SGFMILL_AVAILABLE = False

    # Create dummy classes for when sgfmill is not available
    class DummySgfmill:
        def __getattr__(self, name):
            raise ImportError(
                "sgfmill is required for Go game functionality. Please install it with: pip install sgfmill"
            )

    sgfmill = DummySgfmill()

logger = logging.getLogger(__name__)


class GoGame:
    """Simple Go game wrapper using sgfmill."""

    def __init__(self, board_size: int = 19):
        if not SGFMILL_AVAILABLE:
            raise ImportError(
                "sgfmill is required for Go game functionality. Please install it with: pip install sgfmill"
            )

        self.board_size = board_size
        self.board = sgfmill.boards.Board(board_size)
        self.move_history = []
        self.passes = 0
        self.current_player = "b"  # 'b' for black, 'w' for white
        self.captured = {"b": 0, "w": 0}

    def play_move(self, color: str, move: tuple[int, int] | None):
        """Play a move on the board.

        Args:
            color: 'b' for black, 'w' for white
            move: (row, col) tuple or None for pass

        """
        if move is None:
            # Pass
            self.passes += 1
            self.move_history.append((color, None))
        else:
            row, col = move
            # sgfmill uses different coordinate system
            point = (self.board_size - 1 - row, col)

            # Check for captures before playing

            # Play the move
            try:
                self.board.play(point[0], point[1], color)
                self.passes = 0
                self.move_history.append((color, move))

                # Simple capture detection (this is simplified)
                # In a real implementation, you'd check for captured groups

            except ValueError:
                raise ValueError(f"Invalid move at {move}")

        # Switch player
        self.current_player = "w" if color == "b" else "b"

    def to_sgf(self) -> str:
        """Convert game to SGF format."""
        game_tree = sgfmill.sgf.Sgf_game(size=self.board_size)
        root = game_tree.get_root()
        root.set("GM", 1)  # Go game
        root.set("FF", 4)  # File format
        root.set("SZ", self.board_size)
        root.set("KM", 6.5)  # Komi

        node = root
        for color, move in self.move_history:
            node = game_tree.extend_main_sequence()
            if move is None:
                node.set_move(color, None)
            else:
                row, col = move
                # Convert to sgfmill coordinates
                point = (self.board_size - 1 - row, col)
                node.set_move(color, point)

        return game_tree.serialise()

    def turn(self) -> str:
        """Get current player to move."""
        return self.current_player


def loads_sgf(sgf_string: str) -> GoGame:
    """Load a game from SGF string."""
    try:
        sgf_game = sgfmill.sgf.Sgf_game.from_string(sgf_string)
    except (ValueError, AttributeError) as e:
        # If parsing fails, return empty game
        logger.warning(f"Failed to parse SGF string: {e}")
        return GoGame(19)

    size = sgf_game.get_size()
    game = GoGame(size)

    # Replay moves from SGF
    for node in sgf_game.get_main_sequence()[1:]:  # Skip root
        color, move = node.get_move()
        if color is not None:
            if move is None:
                game.play_move(color, None)
            else:
                # Convert from sgfmill to our coordinates
                row = size - 1 - move[0]
                col = move[1]
                game.play_move(color, (row, col))

    return game


def dumps_sgf(game: GoGame) -> str:
    """Convert game to SGF string."""
    return game.to_sgf()


# Constants for compatibility
BLACK = "b"
WHITE = "w"


# Wrapper classes for compatibility
class sgf:
    """SGF compatibility wrapper."""

    @staticmethod
    def loads(sgf_string: str):
        """Load game from SGF."""
        return loads_sgf(sgf_string)

    @staticmethod
    def dumps(game):
        """Save game to SGF."""
        if isinstance(game, GoGame):
            return dumps_sgf(game)
        elif hasattr(game, "to_sgf"):
            return game.to_sgf()
        else:
            # Assume it's already an SGF string
            return str(game)


def Game(board_size: int = 19) -> GoGame:
    """Create a new Go game."""
    return GoGame(board_size)
