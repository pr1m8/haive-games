"""Move - TODO: Add brief description

TODO: Add detailed description of module functionality



Example:
    Basic usage::

        from haive.move import module_function
        
        # TODO: Add example


"""

from __future__ import annotations

import time
import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Dict,
    Generic,
    List,
    Optional,
    Protocol,
    Set,
    Tuple,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field, computed_field, field_validator, model_validator

# Type variables for generic relationships
T = TypeVar('T')  # Game type
G = TypeVar('G', bound='Game')  # Game type
B = TypeVar('B', bound='Board')  # Board type
P = TypeVar('P', bound='GamePiece')  # Piece type

# ======================================================
# MOVE BASE MODELS AND PROTOCOLS
# ======================================================

class MoveResult(BaseModel):
    """Result of a move execution."""
    success: bool
    message: str = ""
    affected_positions: List[Any] = Field(default_factory=list)
    points_earned: int = 0
    game_state_changed: bool = False
    additional_data: Dict[str, Any] = Field(default_factory=dict)


class MoveType(str, Enum):
    """Base enum for move types, to be extended by games."""
    PLACE = "place"
    REMOVE = "remove"
    MOVE = "move"
    SPECIAL = "special"


class MoveProtocol(Protocol, Generic[G]):
    """Protocol defining the interface for game moves."""
    id: str
    move_type: str
    timestamp: float
    player_id: Optional[str]
    
    def validate(self, game: G) -> Tuple[bool, str]:
        """Validate if this move is legal in the current game state."""
        ...
    
    def execute(self, game: G) -> MoveResult:
        """Execute this move on the game."""
        ...
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert move to dictionary representation."""
        ...
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'MoveProtocol':
        """Create move from dictionary representation."""
        ...


class Move(BaseModel, Generic[G]):
    """Base class for all game moves."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    move_type: str
    timestamp: float = Field(default_factory=time.time)
    player_id: Optional[str] = None
    
    class Config:
        arbitrary_types_allowed = True
    
    def validate(self, game: G) -> Tuple[bool, str]:
        """
        Validate if this move is legal in the current game state.
        
        Args:
            game: The game to validate against
            
        Returns:
            Tuple of (is_valid, message)
        """
        # Base implementation just checks if the game is over
        if hasattr(game, 'game_over') and game.game_over:
            return False, "Game is over"
        return True, "Move is valid"
    
    def execute(self, game: G) -> MoveResult:
        """
        Execute this move on the game.
        
        Args:
            game: The game to execute the move on
            
        Returns:
            Result of the move execution
        """
        # Base implementation just records the move
        if hasattr(game, 'moves'):
            game.moves.append(self)
        return MoveResult(success=True, message="Move executed")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert move to dictionary representation."""
        return {
            "id": self.id,
            "move_type": self.move_type,
            "timestamp": self.timestamp,
            "player_id": self.player_id,
            "move_class": self.__class__.__name__
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Move':
        """Create move from dictionary representation."""
        # Remove move_class field which is just for type identification
        data_copy = data.copy()
        data_copy.pop("move_class", None)
        return cls(**data_copy)


# ======================================================
# GAME STATE TRACKING WITH MOVES
# ======================================================

class GameHistory(BaseModel, Generic[G]):
    """Tracks the history of moves in a game."""
    moves: List[Move[G]] = Field(default_factory=list)
    current_index: int = -1  # -1 means no moves yet
    
    def add_move(self, move: Move[G]) -> None:
        """
        Add a move to the history.
        
        If we're not at the end of history (i.e., moves have been undone),
        truncate the future moves.
        """
        if self.current_index < len(self.moves) - 1:
            # Truncate future moves
            self.moves = self.moves[:self.current_index + 1]
        
        # Add the new move
        self.moves.append(move)
        self.current_index = len(self.moves) - 1
    
    def can_undo(self) -> bool:
        """Check if there are moves that can be undone."""
        return self.current_index >= 0
    
    def can_redo(self) -> bool:
        """Check if there are moves that can be redone."""
        return self.current_index < len(self.moves) - 1
    
    def get_current_move(self) -> Optional[Move[G]]:
        """Get the current move."""
        if self.current_index >= 0 and self.current_index < len(self.moves):
            return self.moves[self.current_index]
        return None
    
    def get_next_move(self) -> Optional[Move[G]]:
        """Get the next move (for redo)."""
        if self.can_redo():
            return self.moves[self.current_index + 1]
        return None
    
    def get_previous_move(self) -> Optional[Move[G]]:
        """Get the previous move (for undo)."""
        if self.can_undo() and self.current_index > 0:
            return self.moves[self.current_index - 1]
        return None


class Game(BaseModel, Generic[B, P]):
    """Enhanced base class for games with move tracking."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    board: B
    start_time: float = Field(default_factory=time.time)
    end_time: Optional[float] = None
    game_over: bool = False
    winner_id: Optional[str] = None
    
    # History of moves
    history: GameHistory = Field(default_factory=GameHistory)
    
    # Registry of available move types
    available_move_types: ClassVar[Dict[str, Type[Move]]] = {}
    
    class Config:
        arbitrary_types_allowed = True
    
    @computed_field
    @property
    def elapsed_time(self) -> float:
        """Get the elapsed time in seconds."""
        end = self.end_time if self.end_time is not None else time.time()
        return end - self.start_time
    
    def process_move(self, move: Move) -> MoveResult:
        """
        Process a move in the game.
        
        Args:
            move: The move to process
            
        Returns:
            Result of the move execution
        """
        # Validate the move
        is_valid, message = move.validate(self)
        if not is_valid:
            return MoveResult(success=False, message=message)
        
        # Execute the move
        result = move.execute(self)
        
        # If successful, add to history
        if result.success:
            self.history.add_move(move)
            
            # Check if game is over after this move
            self._check_game_over()
            
            # If game is over, set end time
            if self.game_over and self.end_time is None:
                self.end_time = time.time()
        
        return result
    
    def create_move(self, move_type: str, **kwargs) -> Optional[Move]:
        """
        Create a move of the specified type.
        
        Args:
            move_type: Type of move to create
            **kwargs: Additional parameters for the move
            
        Returns:
            Created move or None if type not recognized
        """
        move_class = self.available_move_types.get(move_type)
        if move_class:
            return move_class(**kwargs)
        return None
    
    def undo(self) -> MoveResult:
        """
        Undo the last move.
        
        Returns:
            Result of the undo operation
        """
        if not self.history.can_undo():
            return MoveResult(success=False, message="No moves to undo")
        
        # Get the current state
        current_index = self.history.current_index
        
        # Move back one step
        self.history.current_index -= 1
        
        # Reconstruct the game state from the beginning up to the new current index
        return self._reconstruct_state()
    
    def redo(self) -> MoveResult:
        """
        Redo the previously undone move.
        
        Returns:
            Result of the redo operation
        """
        if not self.history.can_redo():
            return MoveResult(success=False, message="No moves to redo")
        
        # Get the next move
        next_move = self.history.get_next_move()
        if not next_move:
            return MoveResult(success=False, message="No next move")
        
        # Move forward one step
        self.history.current_index += 1
        
        # Execute the move
        return self._apply_move(next_move)
    
    def _reconstruct_state(self) -> MoveResult:
        """
        Reconstruct the game state from the beginning up to the current index.
        
        Returns:
            Result of the reconstruction
        """
        # This is a simplified implementation 
        # In a real implementation, we would reset the game state and replay all moves
        return MoveResult(
            success=True, 
            message="Game state reconstructed",
            game_state_changed=True
        )
    
    def _apply_move(self, move: Move) -> MoveResult:
        """
        Apply a move without validation or history tracking.
        
        Args:
            move: The move to apply
            
        Returns:
            Result of the move execution
        """
        # This is a simplified implementation
        return move.execute(self)
    
    def _check_game_over(self) -> None:
        """Check if the game is over after a move."""
        # Subclasses should implement this
        pass
    
    @classmethod
    def register_move_type(cls, move_type: str, move_class: Type[Move]) -> None:
        """
        Register a move type with the game.
        
        Args:
            move_type: Type identifier for the move
            move_class: Move class to register
        """
        cls.available_move_types[move_type] = move_class


# ======================================================
# EXAMPLE IMPLEMENTATION FOR SPECIFIC GAMES
# ======================================================

# Let's implement some example move types for our existing games

# 1. Sudoku Moves

class SudokuMoveType(str, Enum):
    """Types of moves in Sudoku."""
    SET_VALUE = "set_value"
    CLEAR_CELL = "clear_cell"
    HINT = "hint"


class SudokuMove(Move['SudokuGame']):
    """Base class for Sudoku moves."""
    row: int
    col: int
    
    @field_validator('row', 'col')
    @classmethod
    def validate_position(cls, v: int) -> int:
        """Validate row and column values."""
        if not 0 <= v < 9:
            raise ValueError(f"Position must be between 0 and 8, got {v}")
        return v


class SetValueMove(SudokuMove):
    """Move to set a value in a Sudoku cell."""
    move_type: str = SudokuMoveType.SET_VALUE
    value: int
    
    @field_validator('value')
    @classmethod
    def validate_value(cls, v: int) -> int:
        """Validate the value is between 1 and 9."""
        if not 1 <= v <= 9:
            raise ValueError(f"Value must be between 1 and 9, got {v}")
        return v
    
    def validate(self, game: 'SudokuGame') -> Tuple[bool, str]:
        """Validate if this move is legal."""
        # Check if game is over
        is_valid, message = super().validate(game)
        if not is_valid:
            return is_valid, message
        
        # Check if the cell is fixed
        cell = game.board.get_space_at(self.row, self.col)
        if not cell:
            return False, f"No cell at position ({self.row}, {self.col})"
            
        if cell.is_fixed():
            return False, "Cannot change fixed cells"
            
        # Check if the value is valid for this position
        if not game.board.is_valid_placement(self.row, self.col, self.value):
            return False, f"Value {self.value} is not valid at position ({self.row}, {self.col})"
            
        return True, "Valid move"
    
    def execute(self, game: 'SudokuGame') -> MoveResult:
        """Execute this move on the game."""
        # Set the value in the cell
        success = game.board.set_value(self.row, self.col, self.value)
        
        if success:
            # Check if the puzzle is solved
            is_solved = game.board.is_solved()
            
            return MoveResult(
                success=True,
                message=f"Value {self.value} set at position ({self.row}, {self.col})",
                affected_positions=[(self.row, self.col)],
                game_state_changed=is_solved
            )
        
        return MoveResult(
            success=False,
            message=f"Failed to set value {self.value} at position ({self.row}, {self.col})"
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert move to dictionary representation."""
        data = super().to_dict()
        data.update({
            "row": self.row,
            "col": self.col,
            "value": self.value
        })
        return data


class ClearCellMove(SudokuMove):
    """Move to clear a cell in Sudoku."""
    move_type: str = SudokuMoveType.CLEAR_CELL
    
    def validate(self, game: 'SudokuGame') -> Tuple[bool, str]:
        """Validate if this move is legal."""
        # Check if game is over
        is_valid, message = super().validate(game)
        if not is_valid:
            return is_valid, message
        
        # Check if the cell is fixed
        cell = game.board.get_space_at(self.row, self.col)
        if not cell:
            return False, f"No cell at position ({self.row}, {self.col})"
            
        if cell.is_fixed():
            return False, "Cannot clear fixed cells"
            
        # Check if the cell is already empty
        if not cell.is_occupied():
            return False, "Cell is already empty"
            
        return True, "Valid move"
    
    def execute(self, game: 'SudokuGame') -> MoveResult:
        """Execute this move on the game."""
        # Clear the cell
        success = game.board.clear_cell(self.row, self.col)
        
        if success:
            return MoveResult(
                success=True,
                message=f"Cell cleared at position ({self.row}, {self.