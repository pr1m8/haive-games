games.chess.models
==================

.. py:module:: games.chess.models

Chess game models module.

This module provides data models for the chess game, including:
    - Move representation
    - Player decisions
    - Position analysis
    - Structured output models for LLMs



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">5 classes</span>   </div>

.. autoapi-nested-parse::

   Chess game models module.

   This module provides data models for the chess game, including:
       - Move representation
       - Player decisions
       - Position analysis
       - Structured output models for LLMs



      
            
            

.. admonition:: Classes (5)
   :class: note

   .. autoapisummary::

      games.chess.models.ChessAnalysis
      games.chess.models.ChessMoveModel
      games.chess.models.ChessMoveValidation
      games.chess.models.ChessPlayerDecision
      games.chess.models.SegmentedAnalysis

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ChessAnalysis(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Model for chess position analysis.

            This class represents a detailed analysis of a chess position:
                - Material evaluation
                - Positional assessment
                - Tactical opportunities
                - Strategic plans

            .. attribute:: material_eval

               Material evaluation in pawns

               :type: float

            .. attribute:: position_eval

               Qualitative position assessment

               :type: str

            .. attribute:: tactics

               List of tactical opportunities

               :type: List[str]

            .. attribute:: strategy

               Long-term strategic plan

               :type: str

            .. attribute:: best_moves

               Suggested best moves

               :type: List[str]

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: best_moves
               :type:  list[str]
               :value: None



            .. py:attribute:: material_eval
               :type:  float
               :value: None



            .. py:attribute:: position_eval
               :type:  str
               :value: None



            .. py:attribute:: strategy
               :type:  str
               :value: None



            .. py:attribute:: tactics
               :type:  list[str]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ChessMoveModel(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Model for chess moves with validation.

            This class represents a chess move with:
                - UCI notation (e.g., "e2e4")
                - Optional explanation
                - Move validation

            .. attribute:: move

               Move in UCI notation

               :type: str

            .. attribute:: explanation

               Explanation of the move's purpose

               :type: Optional[str]

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: from_move(move: chess.Move, explanation: str | None = None) -> ChessMoveModel
               :classmethod:


               Create from a chess.Move object.



            .. py:method:: to_move() -> chess.Move

               Convert to a chess.Move object.



            .. py:method:: validate_move(v: str) -> str
               :classmethod:


               Validate the move format.

               :param v: The move string to validate

               :returns: The validated move string

               :raises ValueError: If move is not a string or too short



            .. py:attribute:: explanation
               :type:  str | None
               :value: None



            .. py:attribute:: move
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ChessMoveValidation(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Model for chess move validation results.

            This class represents the validation of a chess move:
                - Move legality
                - Error messages
                - Resulting position

            .. attribute:: is_valid

               Whether the move is legal

               :type: bool

            .. attribute:: error_message

               Error message if move is invalid

               :type: Optional[str]

            .. attribute:: resulting_fen

               FEN of position after move

               :type: Optional[str]

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: error_message
               :type:  str | None
               :value: None



            .. py:attribute:: is_valid
               :type:  bool
               :value: None



            .. py:attribute:: resulting_fen
               :type:  str | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ChessPlayerDecision(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Model for chess player decisions.

            This class represents a player's decision-making process:
                - Move selection
                - Position evaluation
                - Alternative moves considered
                - Reasoning process

            .. attribute:: selected_move

               Chosen move with explanation

               :type: ChessMoveModel

            .. attribute:: position_eval

               Player's assessment of the position

               :type: str

            .. attribute:: alternatives

               Alternative moves considered

               :type: List[ChessMoveModel]

            .. attribute:: reasoning

               Detailed reasoning for the move choice

               :type: str

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: alternatives
               :type:  list[ChessMoveModel]
               :value: None



            .. py:attribute:: position_eval
               :type:  str
               :value: None



            .. py:attribute:: reasoning
               :type:  str
               :value: None



            .. py:attribute:: selected_move
               :type:  ChessMoveModel
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: SegmentedAnalysis(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Structured analysis of a chess position in segments.

            This class breaks down position analysis into distinct categories:
                - Numerical position score
                - Attacking chances
                - Defensive needs
                - Strategic plans

            .. attribute:: position_score

               The score evaluation of the position

               :type: float

            .. attribute:: attacking_chances

               Likelihood of a successful attack

               :type: str

            .. attribute:: suggested_plans

               Recommended next plans

               :type: List[str]

            .. attribute:: defensive_needs

               Defensive needs and counterplay ideas

               :type: Optional[str]

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: attacking_chances
               :type:  str
               :value: None



            .. py:attribute:: defensive_needs
               :type:  str | None
               :value: None



            .. py:attribute:: position_score
               :type:  float
               :value: None



            .. py:attribute:: suggested_plans
               :type:  list[str]
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.chess.models import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

