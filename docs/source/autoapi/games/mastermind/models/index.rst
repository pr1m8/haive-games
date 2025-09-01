games.mastermind.models
=======================

.. py:module:: games.mastermind.models

.. autoapi-nested-parse::

   Comprehensive data models for the Mastermind code-breaking game.

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

   .. rubric:: Examples

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



Attributes
----------

.. autoapisummary::

   games.mastermind.models.ValidColor


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/mastermind/models/ColorCode
   /autoapi/games/mastermind/models/MastermindAnalysis
   /autoapi/games/mastermind/models/MastermindFeedback
   /autoapi/games/mastermind/models/MastermindGuess

.. autoapisummary::

   games.mastermind.models.ColorCode
   games.mastermind.models.MastermindAnalysis
   games.mastermind.models.MastermindFeedback
   games.mastermind.models.MastermindGuess


Module Contents
---------------

.. py:data:: ValidColor

   Type definition for valid Mastermind colors.

   The six available colors in the classic Mastermind game:
   - red: Traditional primary color
   - blue: Traditional primary color
   - green: Traditional secondary color
   - yellow: Traditional primary color
   - purple: Traditional secondary color
   - orange: Traditional secondary color

   .. rubric:: Examples

   Using color validation::

       from haive.games.mastermind.models import ValidColor

       def validate_color(color: str) -> ValidColor:
           valid_colors = ["red", "blue", "green", "yellow", "purple", "orange"]
           if color not in valid_colors:
               raise ValueError(f"Invalid color: {color}")
           return color  # type: ignore

