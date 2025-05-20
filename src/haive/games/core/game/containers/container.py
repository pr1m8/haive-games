from typing import Generic, List, Optional
from uuid import uuid4

from pydantic import BaseModel, Field

from haive.games.core.piece.base import GamePiece

# ======================================================
# GAME PIECE CONTAINERS - Collections of game pieces
# ==================================Generic=============


class GamePieceContainer(BaseModel, Generic[T]):
    """Base container for game pieces."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    pieces: List[T] = Field(default_factory=list)

    def add(self, piece: T, position: str = "top") -> None:
        """Add a piece to this container."""
        if position == "top":
            self.pieces.insert(0, piece)
        elif position == "bottom":
            self.pieces.append(piece)
        elif position == "random":
            idx = random.randint(0, len(self.pieces))
            self.pieces.insert(idx, piece)
        else:
            raise ValueError(f"Unknown position: {position}")

    def remove(self, piece_id: str) -> Optional[T]:
        """Remove a piece by ID."""
        for i, piece in enumerate(self.pieces):
            if piece.id == piece_id:
                return self.pieces.pop(i)
        return None

    def count(self) -> int:
        """Count pieces in the container."""
        return len(self.pieces)

    def is_empty(self) -> bool:
        """Check if container is empty."""
        return len(self.pieces) == 0

    def shuffle(self) -> None:
        """Shuffle the pieces."""
        random.shuffle(self.pieces)

    def peek(self, count: int = 1) -> List[T]:
        """Look at the top pieces without removing them."""
        return self.pieces[: min(count, len(self.pieces))]

    def draw(self) -> Optional[T]:
        """Draw the top piece."""
        if not self.pieces:
            return None
        return self.pieces.pop(0)

    def draw_many(self, count: int) -> List[T]:
        """Draw multiple pieces."""
        result = []
        for _ in range(min(count, len(self.pieces))):
            result.append(self.draw())
        return [p for p in result if p is not None]

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """Find a piece matching the predicate."""
        for piece in self.pieces:
            if predicate(piece):
                return piece
        return None

    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        """Filter pieces by predicate."""
        return [piece for piece in self.pieces if predicate(piece)]


class Deck(GamePieceContainer[Card]):
    """A deck of cards."""

    face_down: bool = True

    def draw(self) -> Optional[Card]:
        """Draw the top card."""
        if not self.pieces:
            return None
        card = self.pieces.pop(0)
        card.face_up = not self.face_down
        return card

    def deal(self, num_players: int, cards_per_player: int) -> List[List[Card]]:
        """Deal cards to multiple players."""
        hands = [[] for _ in range(num_players)]
        for i in range(cards_per_player):
            for player in range(num_players):
                if self.pieces:
                    card = self.draw()
                    if card:
                        hands[player].append(card)
        return hands

    @classmethod
    def create_standard_deck(cls) -> "Deck":
        """Create a standard 52-card deck."""
        deck = cls(name="Standard Deck")
        for suit in PlayingCard.Suit:
            for rank in PlayingCard.Rank:
                card = PlayingCard(suit=suit, rank=rank)
                deck.add(card, "bottom")
        deck.shuffle()
        return deck


class TileBag(GamePieceContainer[Tile]):
    """A bag of tiles (Scrabble, Mahjong)."""

    def draw_random(self) -> Optional[Tile]:
        """Draw a random tile from the bag."""
        if not self.pieces:
            return None
        idx = random.randint(0, len(self.pieces) - 1)
        return self.pieces.pop(idx)

    def draw_many_random(self, count: int) -> List[Tile]:
        """Draw multiple random tiles."""
        result = []
        for _ in range(min(count, len(self.pieces))):
            result.append(self.draw_random())
        return [t for t in result if t is not None]


class PlayerHand(GamePieceContainer[T]):
    """A player's hand of pieces."""

    player_id: str

    def add_piece(self, piece: T) -> None:
        """Add a piece to the hand and assign ownership."""
        piece.owner_id = self.player_id
        self.pieces.append(piece)

    def play_piece(self, piece_id: str) -> Optional[T]:
        """Play a piece (remove from hand)."""
        return self.remove(piece_id)

    def can_play(self, piece_id: str, position: Position, board: Board) -> bool:
        """Check if a piece can be played at the given position."""
        piece = next((p for p in self.pieces if p.id == piece_id), None)
        if not piece:
            return False

        if hasattr(piece, "can_move_to") and callable(piece.can_move_to):
            return piece.can_move_to(position, board)
        return False
