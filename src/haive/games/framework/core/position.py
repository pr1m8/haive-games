# game_framework/core/position.py
from __future__ import annotations
from typing import Dict, Any
from pydantic import BaseModel, Field
import uuid

class Position(BaseModel):
    """
    Base class for all position types in games.
    
    A Position represents a location in a game, with different games
    using different coordinate systems.
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    
    class Config:
        frozen = True  # Positions should be immutable
    
    def __eq__(self, other: object) -> bool:
        """
        Equality check must be implemented by subclasses.
        The base implementation just checks if the IDs match.
        """
        if not isinstance(other, Position):
            return False
        return self.id == other.id
    
    def __hash__(self) -> int:
        """
        Hash implementation must be consistent with __eq__.
        The base implementation uses the ID.
        """
        return hash(self.id)
    
    def serialize(self) -> Dict[str, Any]:
        """Convert the position to a serializable dictionary."""
        return self.model_dump()