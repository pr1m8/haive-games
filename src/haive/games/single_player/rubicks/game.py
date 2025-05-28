# game_framework/games/rubiks_cube/game.py
import random
import time
from datetime import datetime
from typing import Any, Dict, List, Optional

from game_framework.core.game import Game, GameStatus

from .models import Color, CubeMove, Face
from .player import RubiksCubePlayer
from .state import CubeGameState


class RubiksCubeGame(Game[CubeGameState, CubeMove]):
    """Rubik's Cube single-player game implementation."""

    def __init__(self, player: RubiksCubePlayer, scramble_length: int = 20):
        """Initialize game with player and scramble length."""
        # Initialize with solved cube
        initial_state = CubeGameState()

        # Create game
        super().__init__(name="Rubik's Cube", players=[player], state=initial_state)

        self.scramble_length = scramble_length
        self.visualization_enabled = True

    def start_game(self) -> None:
        """Start game by scrambling the cube."""
        if self.status == GameStatus.NOT_STARTED:
            self.status = GameStatus.IN_PROGRESS
            self._scramble_cube()

            if self.visualization_enabled:
                self.display_cube()

    def _scramble_cube(self) -> None:
        """Apply random scramble to the cube."""
        print(f"\nScrambling cube with {self.scramble_length} moves...")

        valid_moves = self.get_valid_moves()
        scramble_moves = []

        for i in range(self.scramble_length):
            # Avoid immediate move reversals
            if scramble_moves:
                last_move = scramble_moves[-1]
                inverse = self._get_inverse_move(last_move)
                filtered_moves = [
                    m for m in valid_moves if m.notation != inverse.notation
                ]
                move = random.choice(filtered_moves)
            else:
                move = random.choice(valid_moves)

            scramble_moves.append(move)
            self.state = self._apply_move_to_state(self.state, move)

        # Record scramble
        self.state.scramble_moves = scramble_moves
        self.state.is_scrambled = True

        # Display scramble
        scramble_notation = " ".join([m.notation for m in scramble_moves])
        print(f"Scramble: {scramble_notation}")

    def get_valid_moves(self) -> List[CubeMove]:
        """Get all 18 valid cube moves."""
        moves = []
        notations = [
            "U",
            "U'",
            "U2",
            "D",
            "D'",
            "D2",
            "F",
            "F'",
            "F2",
            "B",
            "B'",
            "B2",
            "L",
            "L'",
            "L2",
            "R",
            "R'",
            "R2",
        ]
        for notation in notations:
            moves.append(CubeMove(notation=notation))
        return moves

    def make_move(self, move: CubeMove) -> bool:
        """Apply a move to the game."""
        if self.status != GameStatus.IN_PROGRESS:
            return False

        # Apply move
        self.state = self._apply_move_to_state(self.state, move)
        self.state.move_history.append(move)

        # Check if solved
        if self.state.is_solved:
            self.status = GameStatus.COMPLETED
            solve_time = (datetime.now() - self.state.start_time).total_seconds()
            self.state.solve_time = solve_time

            print(
                f"\n🎉 Congratulations! Cube solved in {self.state.move_count} moves!"
            )
            print(f"Time: {solve_time:.1f} seconds")

        return True

    def display_cube(self) -> None:
        """Display the cube in terminal with colors."""
        print("\n" + "=" * 50)
        print("RUBIK'S CUBE STATE")
        print("=" * 50)

        # Display in unfolded format
        # Show UP face
        self._display_face(Face.UP, offset=6)

        # Show LEFT, FRONT, RIGHT, BACK in a row
        for row in range(3):
            line = ""
            for face in [Face.LEFT, Face.FRONT, Face.RIGHT, Face.BACK]:
                face_colors = self.state.faces[face]
                for col in range(3):
                    color = face_colors[row][col]
                    line += f"{color.ansi_color}■ \033[0m"
                line += "  "
            print(line)

        # Show DOWN face
        self._display_face(Face.DOWN, offset=6)

        # Show status
        print(f"\nPhase: {self.state.current_phase}")
        print(f"Moves: {self.state.move_count}")

        if self.state.move_history:
            recent_moves = " ".join([m.notation for m in self.state.move_history[-5:]])
            print(f"Recent: {recent_moves}")

    def _display_face(self, face: Face, offset: int = 0) -> None:
        """Display a single face with offset."""
        face_colors = self.state.faces[face]
        for row in face_colors:
            line = " " * offset
            for color in row:
                line += f"{color.ansi_color}■ \033[0m"
            print(line)

    def _apply_move_to_state(
        self, state: CubeGameState, move: CubeMove
    ) -> CubeGameState:
        """Apply a move to create new state."""
        new_state = state.model_copy(deep=True)

        # Get face and number of turns
        face = move.face
        turns = move.turns

        # Apply rotation
        for _ in range(turns):
            self._rotate_face_clockwise(new_state, face)

        return new_state

    def _rotate_face_clockwise(self, state: CubeGameState, face: Face) -> None:
        """Rotate a face 90 degrees clockwise."""
        # Rotate the face itself
        face_colors = state.faces[face]
        rotated = [[face_colors[2 - j][i] for j in range(3)] for i in range(3)]
        state.faces[face] = rotated

        # Rotate adjacent edges
        self._rotate_adjacent_edges(state, face)

    def _rotate_adjacent_edges(self, state: CubeGameState, face: Face) -> None:
        """Rotate the edges around a face."""
        # This is complex - simplified version
        # In a real implementation, this would handle all edge rotations
        pass

    def _get_inverse_move(self, move: CubeMove) -> CubeMove:
        """Get the inverse of a move."""
        notation = move.notation
        if notation.endswith("'"):
            inverse = notation[0]
        elif notation.endswith("2"):
            inverse = notation
        else:
            inverse = notation + "'"
        return CubeMove(notation=inverse)

    def check_game_over(self) -> bool:
        """Check if game is complete."""
        return self.state.is_solved
