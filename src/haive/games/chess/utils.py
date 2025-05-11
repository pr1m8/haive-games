"""Chess game utility functions.

This module provides helper functions for the chess game, including:
    - Game status determination
    - Board visualization
    - Move validation
"""

import chess


def determine_game_status(board: chess.Board) -> str:
    """Determine the current game status based on the board position.

    Args:
        board: Chess board to analyze

    Returns:
        String indicating the game status
    """
    if board.is_checkmate():
        return "checkmate"
    if board.is_stalemate():
        return "stalemate"
    if board.is_insufficient_material():
        return "draw"
    if board.is_check():
        return "check"
    return "ongoing"


def generate_ascii_board(fen: str, last_move: str | None = None) -> str:
    """Generate an ASCII representation of the chess board.

    Args:
        fen: FEN string representation of the board
        last_move: Last move in UCI notation (optional)

    Returns:
        ASCII representation of the board
    """
    board = chess.Board(fen)

    # Highlight last move if provided
    highlighted_squares = set()
    if last_move:
        try:
            move = chess.Move.from_uci(last_move)
            highlighted_squares.add(move.from_square)
            highlighted_squares.add(move.to_square)
        except ValueError:
            pass

    # Convert the board to ASCII
    board_str = str(board)

    # Add file coordinates at the bottom
    file_coords = "  a b c d e f g h"

    # Add rank coordinates on the left
    lines = board_str.split("\n")
    for i, line in enumerate(lines):
        lines[i] = f"{8-i} {line}"

    # Join the lines and add the file coordinates
    return "\n".join(lines) + "\n" + file_coords


def validate_move(fen: str, move_uci: str) -> tuple[bool, str | None, str | None]:
    """Validate a chess move.

    Args:
        fen: FEN string of the current position
        move_uci: Move in UCI notation

    Returns:
        Tuple of (is_valid, error_message, resulting_fen)
    """
    board = chess.Board(fen)

    try:
        move = chess.Move.from_uci(move_uci)

        if move not in board.legal_moves:
            return False, f"Move {move_uci} is not legal in the current position", None

        board.push(move)
        resulting_fen = board.fen()

        return True, None, resulting_fen

    except ValueError:
        return False, f"Invalid UCI format: {move_uci}", None
