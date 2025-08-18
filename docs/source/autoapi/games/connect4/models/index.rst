games.connect4.models
=====================

.. py:module:: games.connect4.models

Connect4 game models module.

This module provides data models for the Connect4 game implementation, including:
    - Move validation and representation
    - Player decisions and analysis
    - Game state components
    - Structured output models for LLMs

.. rubric:: Example

>>> from haive.games.connect4.models import Connect4Move
>>>
>>> # Create and validate a move
>>> move = Connect4Move(
...     column=3,
...     explanation="Control the center column"
... )



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">3 classes</span>   </div>

.. autoapi-nested-parse::

   Connect4 game models module.

   This module provides data models for the Connect4 game implementation, including:
       - Move validation and representation
       - Player decisions and analysis
       - Game state components
       - Structured output models for LLMs

   .. rubric:: Example

   >>> from haive.games.connect4.models import Connect4Move
   >>>
   >>> # Create and validate a move
   >>> move = Connect4Move(
   ...     column=3,
   ...     explanation="Control the center column"
   ... )



      
            
            

.. admonition:: Classes (3)
   :class: note

   .. autoapisummary::

      games.connect4.models.Connect4Analysis
      games.connect4.models.Connect4Move
      games.connect4.models.Connect4PlayerDecision

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Connect4Analysis(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Model for Connect4 position analysis.

            This class represents a detailed analysis of a Connect4 position:
                - Position evaluation
                - Center control assessment
                - Threat detection
                - Strategic plans

            .. attribute:: position_score

               Position evaluation (-1.0 to 1.0).

               :type: float

            .. attribute:: center_control

               Center control rating (0-10).

               :type: int

            .. attribute:: threats

               Detected threats and opportunities.

               :type: Dict[str, List[int]]

            .. attribute:: suggested_columns

               Recommended columns to play.

               :type: List[int]

            .. attribute:: winning_chances

               Estimated winning chances (0-100).

               :type: int

            .. rubric:: Example

            >>> analysis = Connect4Analysis(
            ...     position_score=0.5,
            ...     center_control=8,
            ...     threats={
            ...         "winning_moves": [3],
            ...         "blocking_moves": [4]
            ...     },
            ...     suggested_columns=[3, 2, 4],
            ...     winning_chances=75
            ... )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: _default_threats() -> dict[str, list[int]]
               :staticmethod:


               Create default threats dictionary.

               :returns: Dictionary with empty lists for winning and blocking moves.
               :rtype: dict[str, list[int]]



            .. py:method:: validate_center_control(v: int) -> int
               :classmethod:


               Validate the center control rating.

               :param v: Center control rating to validate.
               :type v: int

               :returns: Validated center control rating.
               :rtype: int

               :raises ValueError: If the rating is not between 0 and 10.



            .. py:method:: validate_winning_chances(v: int) -> int
               :classmethod:


               Validate the winning chances percentage.

               :param v: Winning chances percentage to validate.
               :type v: int

               :returns: Validated winning chances percentage.
               :rtype: int

               :raises ValueError: If the percentage is not between 0 and 100.



            .. py:attribute:: center_control
               :type:  int
               :value: None



            .. py:attribute:: position_score
               :type:  float
               :value: None



            .. py:attribute:: suggested_columns
               :type:  list[int]
               :value: None



            .. py:attribute:: threats
               :type:  dict[str, list[int]]
               :value: None



            .. py:attribute:: winning_chances
               :type:  int
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Connect4Move(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Model for Connect4 moves with validation.

            This class represents a Connect4 move with:
                - Column number (0-6)
                - Optional explanation
                - Move validation

            .. attribute:: column

               Column number (0-6).

               :type: int

            .. attribute:: explanation

               Explanation of the move's purpose.

               :type: Optional[str]

            .. rubric:: Example

            >>> move = Connect4Move(
            ...     column=3,
            ...     explanation="Control the center column"
            ... )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of the move.

               :returns: Human-readable move description.
               :rtype: str



            .. py:method:: validate_column(v: int) -> int
               :classmethod:


               Validate the column number.

               :param v: Column number to validate.
               :type v: int

               :returns: Validated column number.
               :rtype: int

               :raises ValueError: If the column number is not between 0 and 6.



            .. py:attribute:: column
               :type:  int
               :value: None



            .. py:attribute:: explanation
               :type:  str | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Connect4PlayerDecision(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Model for Connect4 player decisions.

            This class represents a player's decision-making process:
                - Move selection
                - Position evaluation
                - Alternative moves considered
                - Reasoning process

            .. attribute:: move

               Chosen move with explanation.

               :type: Connect4Move

            .. attribute:: position_eval

               Player's assessment of the position.

               :type: str

            .. attribute:: alternatives

               Alternative moves considered.

               :type: List[Connect4Move]

            .. attribute:: reasoning

               Detailed reasoning for the move choice.

               :type: str

            .. rubric:: Example

            >>> decision = Connect4PlayerDecision(
            ...     move=Connect4Move(column=3, explanation="Control center"),
            ...     position_eval="Strong position with center control",
            ...     alternatives=[
            ...         Connect4Move(column=2, explanation="Alternative center approach")
            ...     ],
            ...     reasoning="Playing in column 3 maintains center control"
            ... )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: alternatives
               :type:  list[Connect4Move]
               :value: None



            .. py:attribute:: move
               :type:  Connect4Move
               :value: None



            .. py:attribute:: position_eval
               :type:  str
               :value: None



            .. py:attribute:: reasoning
               :type:  str
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.connect4.models import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

