"""State for the Clue game.

This module defines the state model for the Clue game,
tracking the game progression, player cards, and game status.
"""

import random
from typing import Any, Literal

from pydantic import Field

from haive.games.framework.base.state import GameState

from .models import ClueGuess, ClueResponse, ClueSolution


class ClueState(GameState):
    """State for a Clue game."""

    solution: ClueSolution = Field(
        ..., description="The correct solution (murderer, weapon, room)"
    )
    guesses: list[ClueGuess] = Field(
        default_factory=list, description="History of guesses"
    )
    responses: list[ClueResponse] = Field(
        default_factory=list, description="Responses to guesses"
    )
    player1_cards: list[str] = Field(
        default_factory=list, description="Cards in player1's hand"
    )
    player2_cards: list[str] = Field(
        default_factory=list, description="Cards in player2's hand"
    )
    current_player: Literal["player1", "player2"] = Field(
        default="player1", description="Current player's turn"
    )
    max_turns: int = Field(default=20, description="Maximum number of turns")
    game_status: Literal["ongoing", "player1_win", "player2_win"] = Field(
        default="ongoing", description="Status of the game"
    )
    winner: str | None = Field(default=None, description="Winner of the game, if any")
    player1_hypotheses: list[dict[str, Any]] = Field(
        default_factory=list, description="Player 1's hypotheses"
    )
    player2_hypotheses: list[dict[str, Any]] = Field(
        default_factory=list, description="Player 2's hypotheses"
    )

    @property
    def current_turn_number(self) -> int:
        """Get the current turn number."""
        return len(self.guesses) + 1

    @property
    def is_game_over(self) -> bool:
        """Check if the game is over."""
        return self.game_status != "ongoing"

    @property
    def board_string(self) -> str:
        """Get a string representation of the game board."""
        lines = []
        for i, (guess, response) in enumerate(
            zip(self.guesses, self.responses, strict=False)
        ):
            turn_str = f"Turn {i+1}: {guess.player} - {guess.suspect}, {guess.weapon}, {guess.room}"
            response_str = f"Response: {response.card_shown if response.card_shown else 'No card shown'}"
            lines.append(f"{turn_str} | {response_str}")

        return "\n".join(lines) if lines else "No guesses yet."

    @classmethod
    def initialize(cls, **kwargs) -> "ClueState":
        """Initialize a new Clue game state.

        Args:
            **kwargs: Keyword arguments for customization

        Returns:
            ClueState: A new game state
        """
        # Define all cards
        all_suspects = [
            "Miss Scarlet",
            "Colonel Mustard",
            "Mrs. White",
            "Mr. Green",
            "Mrs. Peacock",
            "Professor Plum",
        ]
        all_weapons = [
            "Candlestick",
            "Knife",
            "Lead Pipe",
            "Revolver",
            "Rope",
            "Wrench",
        ]
        all_rooms = [
            "Hall",
            "Lounge",
            "Dining Room",
            "Kitchen",
            "Ballroom",
            "Conservatory",
            "Billiard Room",
            "Library",
            "Study",
        ]

        # Create the solution (random or predefined)
        if "solution" in kwargs:
            solution = kwargs["solution"]
        else:
            solution = ClueSolution(
                suspect=random.choice(all_suspects),
                weapon=random.choice(all_weapons),
                room=random.choice(all_rooms),
            )

        # Remove solution cards from the deck
        remaining_cards = all_suspects + all_weapons + all_rooms
        remaining_cards.remove(solution.suspect)
        remaining_cards.remove(solution.weapon)
        remaining_cards.remove(solution.room)

        # Shuffle and deal cards to players
        random.shuffle(remaining_cards)
        midpoint = len(remaining_cards) // 2
        player1_cards = remaining_cards[:midpoint]
        player2_cards = remaining_cards[midpoint:]

        # Set first player
        first_player = kwargs.get("first_player", "player1")

        return cls(
            solution=solution,
            guesses=[],
            responses=[],
            player1_cards=player1_cards,
            player2_cards=player2_cards,
            current_player=first_player,
            max_turns=kwargs.get("max_turns", 20),
            game_status="ongoing",
        )
