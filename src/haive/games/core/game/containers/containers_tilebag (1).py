"""Tile bag classes for tile-based games in the game framework.

This module defines the TileBag container type for games like Scrabble and Mahjong.
"""

from __future__ import annotations

import random
from typing import TypeVar

from game_framework.containers.base import GamePieceContainer
from game_framework.pieces.tile import Tile

# Type variable for tiles
T = TypeVar("T", bound=Tile)


class TileBag(GamePieceContainer[T]):
    """A bag of tiles.

    This represents a collection of tiles that can be randomly drawn,
    used in games like Scrabble and Mahjong.
    """

    def draw_random(self) -> T | None:
        """Draw a random tile from the bag.

        Returns:
            A random tile, or None if the bag is empty
        """
        if not self.pieces:
            return None
        idx = random.randint(0, len(self.pieces) - 1)
        return self.pieces.pop(idx)

    def draw_many_random(self, count: int) -> list[T]:
        """Draw multiple random tiles from the bag.

        Args:
            count: Number of tiles to draw

        Returns:
            List of randomly drawn tiles
        """
        result = []
        for _ in range(min(count, len(self.pieces))):
            result.append(self.draw_random())
        return [t for t in result if t is not None]

    def peek_random(self) -> T | None:
        """Look at a random tile without removing it.

        Returns:
            A random tile, or None if the bag is empty
        """
        if not self.pieces:
            return None
        idx = random.randint(0, len(self.pieces) - 1)
        return self.pieces[idx]

    def add_all(self, tiles: list[T]) -> None:
        """Add multiple tiles to the bag.

        Args:
            tiles: List of tiles to add
        """
        for tile in tiles:
            self.add(tile, position="bottom")

    @classmethod
    def create_from_distribution(cls, tile_factory, distribution: dict) -> TileBag:
        """Create a tile bag from a distribution dictionary.

        Args:
            tile_factory: Function to create tiles
            distribution: Dictionary mapping values to (count, points) tuples

        Returns:
            A new TileBag instance
        """
        bag = cls(name="Tile Bag")

        for value, (count, points) in distribution.items():
            for _ in range(count):
                tile = tile_factory(value, points)
                bag.add(tile, "bottom")

        # Shuffle the bag
        bag.shuffle()
        return bag
