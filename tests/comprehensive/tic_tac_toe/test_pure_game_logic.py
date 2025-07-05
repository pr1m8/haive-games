"""Pure Tic Tac Toe Game Logic Implementation and Tests.

This file implements and tests the complete Tic Tac Toe game logic without any
external dependencies. It serves as both a reference implementation and
comprehensive test suite for the core game mechanics.
"""

from dataclasses import dataclass
from enum import Enum
from typing import List, Literal, Optional, Tuple


class GameStatus(Enum):
    """Game status enumeration."""

    ONGOING = "ongoing"
    X_WIN = "X_win"
    O_WIN = "O_win"
    DRAW = "draw"


@dataclass
class Move:
    """Represents a move in the game."""

    row: int
    col: int
    player: Literal["X", "O"]

    def __post_init__(self):
        """Validate move parameters."""
        if not (0 <= self.row <= 2):
            raise ValueError(f"Row must be 0-2, got {self.row}")
        if not (0 <= self.col <= 2):
            raise ValueError(f"Column must be 0-2, got {self.col}")
        if self.player not in ["X", "O"]:
            raise ValueError(f"Player must be 'X' or 'O', got {self.player}")


@dataclass
class GameState:
    """Represents the complete state of a Tic Tac Toe game."""

    board: List[List[Optional[str]]]
    current_player: Literal["X", "O"]
    status: GameStatus
    winner: Optional[Literal["X", "O"]]
    move_history: List[Move]

    def __post_init__(self):
        """Validate game state."""
        if len(self.board) != 3 or any(len(row) != 3 for row in self.board):
            raise ValueError("Board must be 3x3")

        for row in self.board:
            for cell in row:
                if cell is not None and cell not in ["X", "O"]:
                    raise ValueError(f"Invalid cell value: {cell}")

    @property
    def board_string(self) -> str:
        """Create a visual representation of the board."""
        lines = []
        for i, row in enumerate(self.board):
            line = " | ".join([cell if cell else " " for cell in row])
            lines.append(line)
            if i < 2:  # Add separator between rows
                lines.append("-" * 9)
        return "\n".join(lines)

    def copy(self) -> "GameState":
        """Create a deep copy of the game state."""
        return GameState(
            board=[row[:] for row in self.board],
            current_player=self.current_player,
            status=self.status,
            winner=self.winner,
            move_history=self.move_history[:],
        )


class TicTacToeGame:
    """Pure Tic Tac Toe game implementation."""

    @staticmethod
    def create_initial_state(starting_player: Literal["X", "O"] = "X") -> GameState:
        """Create a new game state."""
        return GameState(
            board=[[None, None, None], [None, None, None], [None, None, None]],
            current_player=starting_player,
            status=GameStatus.ONGOING,
            winner=None,
            move_history=[],
        )

    @staticmethod
    def get_legal_moves(state: GameState) -> List[Move]:
        """Get all legal moves for the current player."""
        if state.status != GameStatus.ONGOING:
            return []

        legal_moves = []
        for row in range(3):
            for col in range(3):
                if state.board[row][col] is None:
                    legal_moves.append(Move(row, col, state.current_player))

        return legal_moves

    @staticmethod
    def is_valid_move(state: GameState, move: Move) -> Tuple[bool, str]:
        """Check if a move is valid."""
        # Check if game is ongoing
        if state.status != GameStatus.ONGOING:
            return False, "Game is not ongoing"

        # Check if it's the right player's turn
        if move.player != state.current_player:
            return False, f"It's {state.current_player}'s turn, not {move.player}'s"

        # Check bounds (should be caught by Move validation, but double-check)
        if not (0 <= move.row <= 2 and 0 <= move.col <= 2):
            return False, "Move is out of bounds"

        # Check if cell is empty
        if state.board[move.row][move.col] is not None:
            return False, "Cell is already occupied"

        return True, "Valid move"

    @staticmethod
    def apply_move(state: GameState, move: Move) -> GameState:
        """Apply a move and return the new game state."""
        # Validate move
        is_valid, error_msg = TicTacToeGame.is_valid_move(state, move)
        if not is_valid:
            raise ValueError(error_msg)

        # Create new state
        new_state = state.copy()

        # Apply the move
        new_state.board[move.row][move.col] = move.player
        new_state.move_history.append(move)

        # Check for win/draw
        new_state.status, new_state.winner = TicTacToeGame._check_game_status(
            new_state.board
        )

        # Switch players if game is still ongoing
        if new_state.status == GameStatus.ONGOING:
            new_state.current_player = "O" if new_state.current_player == "X" else "X"

        return new_state

    @staticmethod
    def _check_game_status(
        board: List[List[Optional[str]]],
    ) -> Tuple[GameStatus, Optional[Literal["X", "O"]]]:
        """Check the current game status."""
        # Check for wins
        for player in ["X", "O"]:
            if TicTacToeGame._has_won(board, player):
                status = GameStatus.X_WIN if player == "X" else GameStatus.O_WIN
                return status, player

        # Check for draw (board full)
        if TicTacToeGame._is_board_full(board):
            return GameStatus.DRAW, None

        # Game is ongoing
        return GameStatus.ONGOING, None

    @staticmethod
    def _has_won(board: List[List[Optional[str]]], player: str) -> bool:
        """Check if a player has won."""
        # Check rows
        for row in board:
            if all(cell == player for cell in row):
                return True

        # Check columns
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True

        # Check main diagonal (top-left to bottom-right)
        if all(board[i][i] == player for i in range(3)):
            return True

        # Check anti-diagonal (top-right to bottom-left)
        if all(board[i][2 - i] == player for i in range(3)):
            return True

        return False

    @staticmethod
    def _is_board_full(board: List[List[Optional[str]]]) -> bool:
        """Check if the board is completely filled."""
        for row in board:
            for cell in row:
                if cell is None:
                    return False
        return True

    @staticmethod
    def find_winning_moves(state: GameState, player: Literal["X", "O"]) -> List[Move]:
        """Find all moves that would result in an immediate win."""
        winning_moves = []

        for move in TicTacToeGame.get_legal_moves(state):
            if move.player != player:
                # Create a move for the specified player
                test_move = Move(move.row, move.col, player)
            else:
                test_move = move

            # Test the move (temporarily)
            test_board = [row[:] for row in state.board]
            test_board[test_move.row][test_move.col] = test_move.player

            if TicTacToeGame._has_won(test_board, player):
                winning_moves.append(test_move)

        return winning_moves


class TestTicTacToeGame:
    """Comprehensive test suite for Tic Tac Toe game logic."""

    def test_game_initialization(self):
        """Test game initialization."""
        # Default initialization
        state = TicTacToeGame.create_initial_state()

        assert state.current_player == "X"
        assert state.status == GameStatus.ONGOING
        assert state.winner is None
        assert len(state.move_history) == 0

        # Check empty board
        for row in state.board:
            for cell in row:
                assert cell is None

        # Custom starting player
        state_o = TicTacToeGame.create_initial_state("O")
        assert state_o.current_player == "O"

    def test_legal_moves_generation(self):
        """Test legal move generation."""
        # Empty board
        state = TicTacToeGame.create_initial_state()
        legal_moves = TicTacToeGame.get_legal_moves(state)

        assert len(legal_moves) == 9

        # Check all positions are included
        positions = {(move.row, move.col) for move in legal_moves}
        expected = {(r, c) for r in range(3) for c in range(3)}
        assert positions == expected

        # Check all moves are for current player
        assert all(move.player == "X" for move in legal_moves)

        # Partially filled board
        state.board[1][1] = "X"
        state.board[0][0] = "O"
        legal_moves = TicTacToeGame.get_legal_moves(state)

        assert len(legal_moves) == 7
        positions = {(move.row, move.col) for move in legal_moves}
        assert (1, 1) not in positions  # Occupied by X
        assert (0, 0) not in positions  # Occupied by O

        # Finished game - no legal moves
        state.status = GameStatus.X_WIN
        legal_moves = TicTacToeGame.get_legal_moves(state)
        assert len(legal_moves) == 0

    def test_move_validation(self):
        """Test move validation."""
        state = TicTacToeGame.create_initial_state()

        # Valid move
        valid_move = Move(1, 1, "X")
        is_valid, msg = TicTacToeGame.is_valid_move(state, valid_move)
        assert is_valid == True
        assert msg == "Valid move"

        # Wrong player turn
        wrong_player = Move(1, 1, "O")
        is_valid, msg = TicTacToeGame.is_valid_move(state, wrong_player)
        assert is_valid == False
        assert "turn" in msg.lower()

        # Occupy a cell and test occupied cell validation
        state.board[1][1] = "X"
        occupied_move = Move(1, 1, "X")
        is_valid, msg = TicTacToeGame.is_valid_move(state, occupied_move)
        assert is_valid == False
        assert "occupied" in msg.lower()

        # Test finished game
        state.status = GameStatus.X_WIN
        finished_game_move = Move(0, 0, "X")
        is_valid, msg = TicTacToeGame.is_valid_move(state, finished_game_move)
        assert is_valid == False
        assert "ongoing" in msg.lower()

    def test_move_application(self):
        """Test move application and state updates."""
        state = TicTacToeGame.create_initial_state()

        # Apply first move
        move1 = Move(1, 1, "X")
        new_state = TicTacToeGame.apply_move(state, move1)

        # Check move was applied
        assert new_state.board[1][1] == "X"
        assert state.board[1][1] is None  # Original state unchanged

        # Check state updates
        assert new_state.current_player == "O"  # Switched
        assert len(new_state.move_history) == 1
        assert new_state.move_history[0].row == 1
        assert new_state.move_history[0].col == 1
        assert new_state.move_history[0].player == "X"

        # Apply second move
        move2 = Move(0, 0, "O")
        newer_state = TicTacToeGame.apply_move(new_state, move2)

        assert newer_state.board[0][0] == "O"
        assert newer_state.current_player == "X"
        assert len(newer_state.move_history) == 2

    def test_win_detection(self):
        """Test win detection for all win conditions."""
        # Horizontal wins
        for row in range(3):
            state = TicTacToeGame.create_initial_state()
            # Fill row with X
            for col in range(3):
                state.board[row][col] = "X"

            status, winner = TicTacToeGame._check_game_status(state.board)
            assert status == GameStatus.X_WIN
            assert winner == "X"

        # Vertical wins
        for col in range(3):
            state = TicTacToeGame.create_initial_state()
            # Fill column with O
            for row in range(3):
                state.board[row][col] = "O"

            status, winner = TicTacToeGame._check_game_status(state.board)
            assert status == GameStatus.O_WIN
            assert winner == "O"

        # Main diagonal win
        state = TicTacToeGame.create_initial_state()
        for i in range(3):
            state.board[i][i] = "X"

        status, winner = TicTacToeGame._check_game_status(state.board)
        assert status == GameStatus.X_WIN
        assert winner == "X"

        # Anti-diagonal win
        state = TicTacToeGame.create_initial_state()
        for i in range(3):
            state.board[i][2 - i] = "O"

        status, winner = TicTacToeGame._check_game_status(state.board)
        assert status == GameStatus.O_WIN
        assert winner == "O"

    def test_draw_detection(self):
        """Test draw detection."""
        state = TicTacToeGame.create_initial_state()

        # Create a draw board
        draw_board = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
        state.board = draw_board

        status, winner = TicTacToeGame._check_game_status(state.board)
        assert status == GameStatus.DRAW
        assert winner is None

    def test_complete_game_simulation(self):
        """Test a complete game from start to finish."""
        state = TicTacToeGame.create_initial_state()

        # Game sequence: X wins with diagonal
        moves = [
            Move(1, 1, "X"),  # X center
            Move(0, 0, "O"),  # O top-left
            Move(0, 1, "X"),  # X top-center
            Move(2, 2, "O"),  # O bottom-right
            Move(2, 1, "X"),  # X bottom-center - X wins!
        ]

        for i, move in enumerate(moves):
            print(f"Move {i+1}: {move.player} plays ({move.row}, {move.col})")

            # Verify move is legal
            legal_moves = TicTacToeGame.get_legal_moves(state)
            legal_positions = {(m.row, m.col) for m in legal_moves}
            assert (move.row, move.col) in legal_positions

            # Apply move
            state = TicTacToeGame.apply_move(state, move)

            print(f"Board after move:\n{state.board_string}")
            print(f"Status: {state.status.value}")
            if state.winner:
                print(f"Winner: {state.winner}")
            print()

            # Check if game ended
            if state.status != GameStatus.ONGOING:
                assert i == 4  # Should end on 5th move
                assert state.status == GameStatus.X_WIN
                assert state.winner == "X"
                break

        # Verify final state
        assert len(state.move_history) == 5
        assert state.board[1][1] == "X"  # Center
        assert state.board[0][1] == "X"  # Top-center
        assert state.board[2][1] == "X"  # Bottom-center (winning move)

    def test_winning_moves_detection(self):
        """Test detection of winning moves."""
        state = TicTacToeGame.create_initial_state()

        # Set up a board where X can win
        state.board = [
            ["X", "X", None],  # X can win at (0,2)
            ["O", "O", None],  # O can win at (1,2)
            [None, None, None],
        ]

        # Find winning moves for X
        x_winning = TicTacToeGame.find_winning_moves(state, "X")
        assert len(x_winning) == 1
        assert x_winning[0].row == 0
        assert x_winning[0].col == 2

        # Find winning moves for O
        o_winning = TicTacToeGame.find_winning_moves(state, "O")
        assert len(o_winning) == 1
        assert o_winning[0].row == 1
        assert o_winning[0].col == 2

    def test_board_string_representation(self):
        """Test board string representation."""
        state = TicTacToeGame.create_initial_state()

        # Empty board
        board_str = state.board_string
        assert " | " in board_str  # Check for pipe separators
        assert "-" in board_str  # Row separators

        # Partially filled board
        state.board = [["X", None, "O"], [None, "X", None], ["O", None, "X"]]
        board_str = state.board_string
        assert "X" in board_str
        assert "O" in board_str
        assert " " in board_str  # Empty cells
        assert "|" in board_str  # Column separators

        print("Sample board representation:")
        print(board_str)

    def test_edge_cases(self):
        """Test edge cases and error conditions."""
        # Invalid move creation
        try:
            Move(-1, 0, "X")  # Out of bounds
            assert False, "Should have raised ValueError"
        except ValueError:
            pass

        try:
            Move(0, 0, "Y")  # Invalid player
            assert False, "Should have raised ValueError"
        except ValueError:
            pass

        # Invalid move application - occupied cell
        state = TicTacToeGame.create_initial_state()
        state.board[0][0] = "X"

        try:
            occupied_move = Move(0, 0, "X")  # Same player, but cell is occupied
            TicTacToeGame.apply_move(state, occupied_move)
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert "occupied" in str(e).lower()


def run_all_tests():
    """Run all tests and report results."""
    print("=== Pure Tic Tac Toe Game Logic Tests ===\n")

    test_suite = TestTicTacToeGame()

    tests = [
        ("Game Initialization", test_suite.test_game_initialization),
        ("Legal Moves Generation", test_suite.test_legal_moves_generation),
        ("Move Validation", test_suite.test_move_validation),
        ("Move Application", test_suite.test_move_application),
        ("Win Detection", test_suite.test_win_detection),
        ("Draw Detection", test_suite.test_draw_detection),
        ("Complete Game Simulation", test_suite.test_complete_game_simulation),
        ("Winning Moves Detection", test_suite.test_winning_moves_detection),
        ("Board String Representation", test_suite.test_board_string_representation),
        ("Edge Cases", test_suite.test_edge_cases),
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        try:
            test_func()
            print(f"✓ {test_name}")
            passed += 1
        except Exception as e:
            print(f"✗ {test_name}: {e}")
            import traceback

            traceback.print_exc()

    print(f"\n=== Test Results ===")
    print(f"Passed: {passed}/{total}")

    if passed == total:
        print("🎉 All pure game logic tests passed!")
        print("\nThis validates that the core Tic Tac Toe game logic is sound.")
        print(
            "Next step: Test the actual haive-games implementation against this reference."
        )
        return True
    else:
        print("❌ Some tests failed")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
