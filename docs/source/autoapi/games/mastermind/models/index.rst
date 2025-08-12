
:py:mod:`games.mastermind.models`
=================================

.. py:module:: games.mastermind.models

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


.. autolink-examples:: games.mastermind.models
   :collapse:

Classes
-------

.. autoapisummary::

   games.mastermind.models.ColorCode
   games.mastermind.models.MastermindAnalysis
   games.mastermind.models.MastermindFeedback
   games.mastermind.models.MastermindGuess


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ColorCode:

   .. graphviz::
      :align: center

      digraph inheritance_ColorCode {
        node [shape=record];
        "ColorCode" [label="ColorCode"];
        "pydantic.BaseModel" -> "ColorCode";
      }

.. autopydantic_model:: games.mastermind.models.ColorCode
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MastermindAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_MastermindAnalysis {
        node [shape=record];
        "MastermindAnalysis" [label="MastermindAnalysis"];
        "pydantic.BaseModel" -> "MastermindAnalysis";
      }

.. autopydantic_model:: games.mastermind.models.MastermindAnalysis
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MastermindFeedback:

   .. graphviz::
      :align: center

      digraph inheritance_MastermindFeedback {
        node [shape=record];
        "MastermindFeedback" [label="MastermindFeedback"];
        "pydantic.BaseModel" -> "MastermindFeedback";
      }

.. autopydantic_model:: games.mastermind.models.MastermindFeedback
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MastermindGuess:

   .. graphviz::
      :align: center

      digraph inheritance_MastermindGuess {
        node [shape=record];
        "MastermindGuess" [label="MastermindGuess"];
        "pydantic.BaseModel" -> "MastermindGuess";
      }

.. autopydantic_model:: games.mastermind.models.MastermindGuess
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. rubric:: Related Links

.. autolink-examples:: games.mastermind.models
   :collapse:
   
.. autolink-skip:: next
