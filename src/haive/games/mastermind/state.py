import operator
import random
from typing import Annotated, Literal

from pydantic import Field, computed_field

from haive.games.framework.base.state import GameState
from haive.games.mastermind.models import (
    ColorCode,
    MastermindAnalysis,
    MastermindFeedback,
    MastermindGuess,
)


class MastermindState(GameState):
    """Comprehensive state management for Mastermind code-breaking games.

    This class manages the complete state of a Mastermind game, including the
    secret code, guess history, feedback tracking, and game progression. The
    state supports both traditional codemaker/codebreaker roles and maintains
    detailed analytics for AI decision-making.

    The state tracks the classic Mastermind game flow:
    - Secret code generation and protection
    - Sequential guess validation and feedback
    - Turn-based progression with role separation
    - Win condition evaluation and game termination
    - Strategic analysis for AI players

    Attributes:
        secret_code: The hidden 4-color code that players attempt to guess.
            Kept secret from the codebreaker throughout the game.
        guesses: Complete history of all guesses made during the game.
            Maintains chronological order for analysis and replay.
        feedback: Corresponding feedback for each guess made.
            Provides positional and color correctness information.
        turn: Current player's turn (the active codebreaker).
            Alternates between players in multi-player scenarios.
        codemaker: Player who created the secret code.
            Remains constant throughout the game session.
        max_turns: Maximum number of guesses allowed before game ends.
            Typically 10-12 turns in standard Mastermind.
        game_status: Current state of the game progression.
            Tracks ongoing play, completion, and winner determination.
        winner: The victorious player, if any.
            Set when code is cracked or maximum turns reached.
        player1_analysis: AI analysis history for player 1.
            Tracks strategic reasoning and decision-making process.
        player2_analysis: AI analysis history for player 2.
            Tracks strategic reasoning and decision-making process.

    Examples:
        Game initialization::

            from haive.games.mastermind.state import MastermindState

            # Initialize with random secret code
            state = MastermindState.initialize(
                codemaker="player1",
                colors=None,  # Random generation
                max_turns=10
            )

            # Initialize with specific code
            state = MastermindState.initialize(
                codemaker="player1",
                colors=["red", "blue", "green", "yellow"],
                max_turns=12
            )

        Game progression tracking::

            # Check current game state
            if state.is_game_over:
                print(f"Game ended! Winner: {state.winner}")
            else:
                print(f"Turn {state.current_turn}: {state.turn} to guess")
                print(f"Guesses remaining: {state.turns_remaining}")

        Strategic analysis::

            # Access game statistics
            stats = state.game_statistics
            print(f"Guess accuracy: {stats['accuracy']:.2%}")
            print(f"Information gain: {stats['information_efficiency']:.2f}")

    Note:
        The secret code is accessible to the game engine for validation
        but should remain hidden from the codebreaker during gameplay.
        The state maintains immutability for core game data while
        supporting dynamic updates for game progression.
    """

    secret_code: list[str] = Field(
        ..., min_items=4, max_items=4, description="Secret color code (4 colors)"
    )
    guesses: Annotated[list[MastermindGuess], operator.add] = Field(
        default_factory=list, description="History of guesses"
    )
    feedback: Annotated[list[MastermindFeedback], operator.add] = Field(
        default_factory=list, description="Feedback for each guess"
    )
    turn: Literal["player1", "player2"] = Field(
        ..., description="Current player's turn (codebreaker)"
    )
    codemaker: Literal["player1", "player2"] = Field(
        ..., description="Player who created the code"
    )
    max_turns: int = Field(default=10, description="Maximum number of turns")
    game_status: Literal["ongoing", "player1_win", "player2_win"] = Field(
        default="ongoing", description="Status of the game"
    )
    winner: str | None = Field(default=None, description="Winner of the game, if any")
    player1_analysis: Annotated[list[MastermindAnalysis], operator.add] = Field(
        default_factory=list, description="Analyses by player1"
    )
    player2_analysis: Annotated[list[MastermindAnalysis], operator.add] = Field(
        default_factory=list, description="Analyses by player2"
    )

    @classmethod
    def initialize(
        cls,
        codemaker: str = "player1",
        colors: list[str] | None = None,
        code_length: int = 4,
        max_turns: int = 10,
        secret_code: list[str] | ColorCode | dict | None = None,
    ) -> "MastermindState":
        colors = colors or ["red", "blue", "green", "yellow", "purple", "orange"]
        codebreaker = "player2" if codemaker == "player1" else "player1"

        # Unwrap or generate secret code
        if isinstance(secret_code, ColorCode):
            secret_code = secret_code.code
        elif isinstance(secret_code, dict) and "code" in secret_code:
            secret_code = secret_code["code"]
        elif not secret_code:
            secret_code = random.choices(colors, k=code_length)

        return cls(
            secret_code=secret_code,
            guesses=[],
            feedback=[],
            turn=codebreaker,
            codemaker=codemaker,
            max_turns=max_turns,
            game_status="ongoing",
        )

    @property
    @computed_field
    def current_turn_number(self) -> int:
        """Get the current turn number."""
        return len(self.guesses) + 1

    @property
    @computed_field
    def turns_remaining(self) -> int:
        """Get the number of turns remaining."""
        return max(0, self.max_turns - len(self.guesses))

    @property
    @computed_field
    def is_game_over(self) -> bool:
        """Check if the game is over."""
        return self.game_status != "ongoing"

    @property
    @computed_field
    def last_guess(self) -> MastermindGuess | None:
        """Get the last guess made."""
        return self.guesses[-1] if self.guesses else None

    @property
    @computed_field
    def last_feedback(self) -> MastermindFeedback | None:
        """Get the feedback for the last guess."""
        return self.feedback[-1] if self.feedback else None

    @property
    @computed_field
    def board_string(self) -> str:
        """Get a string representation of the board."""
        if not self.guesses:
            return "No guesses yet."

        result = []
        result.append("Turn | Guess                     | Feedback")
        result.append("-" * 50)

        for i, (guess, feedback) in enumerate(
            zip(self.guesses, self.feedback, strict=False)
        ):
            guess_str = f"{', '.join(guess.colors)}"
            feedback_str = (
                f"🎯 {feedback.correct_position} | 🔄 {feedback.correct_color}"
            )
            result.append(f"{i+1:4d} | {guess_str:25s} | {feedback_str}")

        return "\n".join(result)
