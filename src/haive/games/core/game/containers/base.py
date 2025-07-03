"""Container models for game pieces in the game framework.

This module defines containers for game pieces like decks of cards,
bags of tiles, and player hands.
"""

from __future__ import annotations

import random
import uuid
from collections.abc import Callable
from typing import Any, Generic, TypeVar

from game.core.piece import Card, GamePiece
from pydantic import BaseModel, Field

# Type variable for game pieces
T = TypeVar("T", bound=GamePiece)


class GamePieceContainer(BaseModel, Generic[T]):
    """Base container for game pieces.

    This represents a collection of game pieces like a deck of cards,
    a bag of tiles, or a player's hand.
    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    pieces: list[T] = Field(default_factory=list)
    properties: dict[str, Any] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True

    def add(self, piece: T, position: str = "top") -> None:
        """Add a piece to this container.

        Args:
            piece: The piece to add
            position: Where to add the piece ("top", "bottom", or "random")

        Raises:
            ValueError: If position is not valid
        """
        if position == "top":
            self.pieces.insert(0, piece)
        elif position == "bottom":
            self.pieces.append(piece)
        elif position == "random":
            idx = random.randint(0, len(self.pieces))
            self.pieces.insert(idx, piece)
        else:
            raise ValueError(f"Unknown position: {position}")

    def remove(self, piece_id: str) -> T | None:
        """Remove a piece by ID.

        Args:
            piece_id: ID of the piece to remove

        Returns:
            The removed piece, or None if not found
        """
        for i, piece in enumerate(self.pieces):
            if piece.id == piece_id:
                return self.pieces.pop(i)
        return None

    def count(self) -> int:
        """Count pieces in the container.

        Returns:
            Number of pieces in the container
        """
        return len(self.pieces)

    def is_empty(self) -> bool:
        """Check if container is empty.

        Returns:
            True if the container is empty, False otherwise
        """
        return len(self.pieces) == 0

    def shuffle(self) -> None:
        """Shuffle the pieces in the container."""
        random.shuffle(self.pieces)

    def peek(self, count: int = 1) -> list[T]:
        """Look at the top pieces without removing them.

        Args:
            count: Number of pieces to peek at

        Returns:
            List of pieces from the top
        """
        return self.pieces[: min(count, len(self.pieces))]

    def draw(self) -> T | None:
        """Draw the top piece.

        Returns:
            The top piece, or None if container is empty
        """
        if not self.pieces:
            return None
        return self.pieces.pop(0)

    def draw_many(self, count: int) -> list[T]:
        """Draw multiple pieces from the top.

        Args:
            count: Number of pieces to draw

        Returns:
            List of drawn pieces
        """
        result = []
        for _ in range(min(count, len(self.pieces))):
            result.append(self.draw())
        return [p for p in result if p is not None]

    def find(self, predicate: Callable[[T], bool]) -> T | None:
        """Find a piece matching the predicate.

        Args:
            predicate: Function that returns True for the desired piece

        Returns:
            The first matching piece, or None if not found
        """
        for piece in self.pieces:
            if predicate(piece):
                return piece
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        """Filter pieces by predicate.

        Args:
            predicate: Function that returns True for pieces to include

        Returns:
            List of pieces matching the predicate
        """
        return [piece for piece in self.pieces if predicate(piece)]

    def clear(self) -> None:
        """Remove all pieces from the container."""
        self.pieces.clear()

    def set_property(self, key: str, value: Any) -> None:
        """Set a container property.

        Args:
            key: Property name
            value: Property value
        """
        self.properties[key] = value

    def get_property(self, key: str, default: Any = None) -> Any:
        """Get a container property.

        Args:
            key: Property name
            default: Default value if property doesn't exist

        Returns:
            Property value or default
        """
        return self.properties.get(key, default)


C = TypeVar("C", bound=Card)


class Deck(GamePieceContainer[C]):
    """A deck of cards.

    This represents a collection of cards that can be drawn, shuffled, and dealt.
    """

    face_down: bool = True  # Whether cards are hidden by default
    discard_pile: list[C] = Field(default_factory=list)

    def draw(self) -> C | None:
        """Draw the top card and set its face up/down based on deck configuration.

        Returns:
            The drawn card, or None if deck is empty
        """
        if not self.pieces:
            return None
        card = self.pieces.pop(0)
        card.face_up = not self.face_down
        return card

    def deal(self, num_players: int, cards_per_player: int) -> list[list[C]]:
        """Deal cards to multiple players.

        Args:
            num_players: Number of players to deal to
            cards_per_player: Number of cards per player

        Returns:
            List of lists, where each inner list contains a player's cards
        """
        hands = [[] for _ in range(num_players)]
        for _i in range(cards_per_player):
            for player in range(num_players):
                if self.pieces:
                    card = self.draw()
                    if card:
                        hands[player].append(card)
        return hands

    def discard(self, card: C) -> None:
        """Add a card to the discard pile.

        Args:
            card: Card to discard
        """
        self.discard_pile.append(card)

    def recycle_discards(self, shuffle: bool = True) -> None:
        """Move all cards from discard pile back into the deck.

        Args:
            shuffle: Whether to shuffle the deck after recycling
        """
        self.pieces.extend(self.discard_pile)
        self.discard_pile.clear()
        if shuffle:
            self.shuffle()

    def peek_top(self, count: int = 1) -> list[C]:
        """Look at top cards without drawing.

        Args:
            count: Number of cards to peek at

        Returns:
            List of cards from the top
        """
        return self.peek(count)

    def peek_bottom(self, count: int = 1) -> list[C]:
        """Look at bottom cards without drawing.

        Args:
            count: Number of cards to peek at

        Returns:
            List of cards from the bottom
        """
        return self.pieces[-count:] if count <= len(self.pieces) else self.pieces.copy()

    def draw_bottom(self) -> C | None:
        """Draw the bottom card.

        Returns:
            The bottom card, or None if deck is empty
        """
        if not self.pieces:
            return None
        card = self.pieces.pop()
        card.face_up = not self.face_down
        return card


class PlayerHand(GamePieceContainer[T]):
    """A player's hand of pieces.

    This represents the collection of pieces a player holds,
    such as cards in a card game or tiles in Scrabble.
    """

    player_id: str

    def add_piece(self, piece: T) -> None:
        """Add a piece to the hand and assign ownership to the player.

        Args:
            piece: The piece to add
        """
        piece.assign_to_player(self.player_id)
        self.pieces.append(piece)

    def play_piece(self, piece_id: str) -> T | None:
        """Play a piece (remove from hand).

        Args:
            piece_id: ID of the piece to play

        Returns:
            The played piece, or None if not found
        """
        return self.remove(piece_id)

    def play_pieces(self, piece_ids: list[str]) -> list[T]:
        """Play multiple pieces.

        Args:
            piece_ids: List of piece IDs to play

        Returns:
            List of played pieces
        """
        result = []
        for piece_id in piece_ids:
            piece = self.play_piece(piece_id)
            if piece:
                result.append(piece)
        return result
