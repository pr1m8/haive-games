"""Comprehensive data models for the Mastermind code-breaking game.

This module defines the complete set of data structures for the classic Mastermind
game, providing robust models for code creation, guessing, feedback calculation,
and strategic analysis. The implementation follows the traditional Mastermind
rules with six available colors and four-peg codes.

The Mastermind game involves:
- A codemaker who creates a secret 4-color code
- A codebreaker who attempts to guess the code
- Feedback system indicating correct positions and colors
- Strategic analysis for optimal guessing patterns

Key Models:
    ValidColor: Type definition for the six available colors
    ColorCode: The secret code that players try to guess
    MastermindGuess: A player's attempt to crack the code
    MastermindFeedback: Response indicating correctness
    MastermindAnalysis: Strategic analysis for AI decision-making

Examples:
    Creating a secret code::

        from haive.games.mastermind.models import ColorCode

        # Random code generation
        secret = ColorCode(code=["red", "blue", "green", "yellow"])

        # Validate code length and colors
        assert len(secret.code) == 4
        assert all(color in ["red", "blue", "green", "yellow", "purple", "orange"]
                  for color in secret.code)

    Making a guess::

        from haive.games.mastermind.models import MastermindGuess

        guess = MastermindGuess(
            colors=["red", "yellow", "blue", "green"],
            player="player1"
        )
        print(guess)  # "player1 guesses: red, yellow, blue, green"

    Feedback calculation::

        from haive.games.mastermind.models import MastermindFeedback

        feedback = MastermindFeedback(
            correct_position=2,  # 2 pegs in correct position
            correct_color=1      # 1 additional peg with correct color
        )

        if feedback.is_winning():
            print("Code cracked!")
        else:
            print(f"Feedback: {feedback}")

    Strategic analysis::

        from haive.games.mastermind.models import MastermindAnalysis

        analysis = MastermindAnalysis(
            possible_combinations=64,
            high_probability_colors=["red", "blue"],
            eliminated_colors=["purple"],
            strategy="Focus on testing remaining color combinations",
            reasoning="Based on previous feedback patterns...",
            confidence=8
        )

The models provide comprehensive validation, strategic context, and integration
with AI decision-making systems for optimal gameplay experience.
"""

from typing import Literal

from pydantic import BaseModel, Field

# Define valid Mastermind colors
ValidColor = Literal["red", "blue", "green", "yellow", "purple", "orange"]
"""Type definition for valid Mastermind colors.

The six available colors in the classic Mastermind game:
- red: Traditional primary color
- blue: Traditional primary color
- green: Traditional secondary color
- yellow: Traditional primary color
- purple: Traditional secondary color
- orange: Traditional secondary color

Examples:
    Using color validation::

        from haive.games.mastermind.models import ValidColor

        def validate_color(color: str) -> ValidColor:
            valid_colors = ["red", "blue", "green", "yellow", "purple", "orange"]
            if color not in valid_colors:
                raise ValueError(f"Invalid color: {color}")
            return color  # type: ignore
"""


class ColorCode(BaseModel):
    """The secret code in Mastermind that players attempt to guess.

    Represents the codemaker's secret combination of four colors that the
    codebreaker must discover through strategic guessing and feedback analysis.
    The code follows traditional Mastermind rules with exactly four positions
    and colors chosen from the six available options.

    The secret code is the core objective of the game - once correctly guessed,
    the codebreaker wins. The code allows duplicate colors, making the game
    more challenging and strategic.

    Attributes:
        code: List of exactly 4 colors from the valid color set.
            Each position can contain any of the six available colors,
            including duplicates.

    Examples:
        Creating secret codes::

            # Code with all different colors
            secret1 = ColorCode(code=["red", "blue", "green", "yellow"])

            # Code with duplicate colors
            secret2 = ColorCode(code=["red", "red", "blue", "blue"])

            # Code with all same color
            secret3 = ColorCode(code=["purple", "purple", "purple", "purple"])

        Code validation::

            # Valid codes
            assert len(secret1.code) == 4
            assert all(color in ["red", "blue", "green", "yellow", "purple", "orange"]
                      for color in secret1.code)

            # Invalid codes will raise validation errors
            try:
                invalid = ColorCode(code=["red", "blue", "green"])  # Too short
            except ValueError:
                print("Code must have exactly 4 colors")

        Game integration::

            def check_guess_against_code(code: ColorCode, guess: MastermindGuess) -> MastermindFeedback:
                correct_position = sum(1 for i, color in enumerate(guess.colors)
                                     if color == code.code[i])
                # ... feedback calculation logic
                return MastermindFeedback(correct_position=correct_position, correct_color=0)

    Note:
        The code is typically hidden from the codebreaker during gameplay,
        only revealed through feedback from guesses. Direct access to the
        code should be restricted to game management and validation functions.
    """

    code: list[ValidColor] = Field(
        ...,
        min_items=4,
        max_items=4,
        description="The secret code: 4 colors chosen from the allowed set",
    )


class MastermindGuess(BaseModel):
    """A codebreaker's attempt to guess the secret code.

    Represents a single guess in the Mastermind game, consisting of four colors
    chosen by a player in their attempt to crack the secret code. Each guess
    is evaluated against the secret code to provide feedback that guides
    subsequent guessing strategy.

    The guess follows the same structure as the secret code but represents
    the player's hypothesis rather than the ground truth. Strategic players
    use information from previous feedback to make informed guesses that
    efficiently narrow down the solution space.

    Attributes:
        colors: List of exactly 4 colors representing the guess.
            Each position corresponds to a position in the secret code.
        player: Identifier for the player making this guess.
            Used for tracking and analysis in multi-player scenarios.

    Examples:
        Making strategic guesses::

            # Initial guess with diverse colors
            first_guess = MastermindGuess(
                colors=["red", "blue", "green", "yellow"],
                player="player1"
            )

            # Follow-up guess based on feedback
            second_guess = MastermindGuess(
                colors=["red", "red", "blue", "purple"],
                player="player1"
            )

        Guess validation::

            guess = MastermindGuess(
                colors=["orange", "purple", "red", "blue"],
                player="player2"
            )

            # Verify guess structure
            assert len(guess.colors) == 4
            assert guess.player in ["player1", "player2"]
            print(guess)  # "player2 guesses: orange, purple, red, blue"

        Strategic analysis::

            def analyze_guess_quality(guess: MastermindGuess, previous_feedback: list) -> float:
                # Calculate information gain potential
                unique_colors = len(set(guess.colors))
                diversity_score = unique_colors / 4.0
                return diversity_score

        Game integration::

            def process_guess(guess: MastermindGuess, secret: ColorCode) -> MastermindFeedback:
                correct_position = sum(1 for i, color in enumerate(guess.colors)
                                     if color == secret.code[i])
                # ... calculate correct_color
                return MastermindFeedback(correct_position=correct_position, correct_color=0)

    Note:
        Good guessing strategy involves balancing information gathering
        (using diverse colors) with hypothesis testing (focusing on
        likely solutions based on previous feedback).
    """

    colors: list[ValidColor] = Field(
        ..., min_items=4, max_items=4, description="List of 4 colors"
    )
    player: Literal["player1", "player2"] = Field(
        ..., description="Player making the guess"
    )

    def __str__(self) -> str:
        """String representation of the guess.

        Returns:
            str: Human-readable guess description.

        Examples:
            Displaying guesses::

                guess = MastermindGuess(colors=["red", "blue", "green", "yellow"], player="player1")
                print(guess)  # "player1 guesses: red, blue, green, yellow"
        """
        return f"{self.player} guesses: {', '.join(self.colors)}"


class MastermindFeedback(BaseModel):
    """Feedback response for a Mastermind guess evaluation.

    Represents the codemaker's response to a codebreaker's guess, providing
    crucial information about the correctness of the guess without revealing
    the exact positions or colors. This feedback is essential for the
    codebreaker's deduction process.

    The feedback follows traditional Mastermind rules:
    - Black pegs (correct_position): Right color in right position
    - White pegs (correct_color): Right color in wrong position
    - No feedback for completely incorrect colors

    Attributes:
        correct_position: Number of pegs with correct color and position (0-4).
            These are traditionally represented by black pegs.
        correct_color: Number of pegs with correct color but wrong position (0-4).
            These are traditionally represented by white pegs.

    Examples:
        Perfect guess feedback::

            # All positions correct - winning feedback
            perfect = MastermindFeedback(correct_position=4, correct_color=0)
            assert perfect.is_winning() == True
            print(perfect)  # "🌟 Correct position: 4, 🔄 Correct color: 0"

        Partial match feedback::

            # 2 correct positions, 1 correct color wrong position
            partial = MastermindFeedback(correct_position=2, correct_color=1)
            assert partial.is_winning() == False
            print(partial)  # "🌟 Correct position: 2, 🔄 Correct color: 1"

        No match feedback::

            # Complete miss - no correct colors
            miss = MastermindFeedback(correct_position=0, correct_color=0)
            assert miss.is_winning() == False

        Strategic interpretation::

            feedback = MastermindFeedback(correct_position=1, correct_color=2)

            # Interpretation:
            # - 1 color is in the correct position
            # - 2 additional colors are in the code but wrong positions
            # - 1 color is not in the code at all

            if feedback.correct_position + feedback.correct_color == 3:
                print("3 out of 4 colors are in the secret code")

    Note:
        The sum of correct_position and correct_color should never exceed 4,
        as there are only 4 positions in the code. The feedback provides
        information about colors, not individual pegs.
    """

    correct_position: int = Field(
        ..., ge=0, le=4, description="Number of pegs with correct color and position"
    )
    correct_color: int = Field(
        ...,
        ge=0,
        le=4,
        description="Number of pegs with correct color but wrong position",
    )

    def __str__(self) -> str:
        """String representation of the feedback.

        Returns:
            str: Human-readable feedback with emoji indicators.

        Examples:
            Feedback display::

                feedback = MastermindFeedback(correct_position=2, correct_color=1)
                print(feedback)  # "🌟 Correct position: 2, 🔄 Correct color: 1"
        """
        return f"🌟 Correct position: {self.correct_position}, 🔄 Correct color: {
            self.correct_color
        }"

    def is_winning(self) -> bool:
        """Check if this feedback indicates a winning guess.

        Returns:
            bool: True if all 4 pegs are in correct positions (game won).

        Examples:
            Winning condition check::

                winning_feedback = MastermindFeedback(correct_position=4, correct_color=0)
                assert winning_feedback.is_winning() == True

                partial_feedback = MastermindFeedback(correct_position=3, correct_color=1)
                assert partial_feedback.is_winning() == False
        """
        return self.correct_position == 4


class MastermindAnalysis(BaseModel):
    """Analysis of a Mastermind position.

    This class defines the structure of an analysis for a Mastermind
    position, which includes the estimated number of possible
    combinations left, the colors with high probability of being in the
    solution, the recommended next guess, the colors likely eliminated,
    and the fixed positions.
    """

    possible_combinations: int = Field(
        ..., description="Estimated number of possible combinations left"
    )
    high_probability_colors: list[ValidColor] = Field(
        ..., description="Colors with high probability of being in the solution"
    )
    eliminated_colors: list[ValidColor] = Field(
        default_factory=list, description="Colors likely eliminated"
    )

    fixed_positions: list[dict[str, ValidColor]] = Field(
        default_factory=list,
        description="List of fixed positions as dicts like {'index': 'color'}",
    )

    strategy: str = Field(..., description="Current strategy recommendation")
    reasoning: str = Field(..., description="Detailed reasoning for the analysis")
    confidence: int = Field(
        ..., ge=1, le=10, description="Confidence level in this analysis (1-10)"
    )
