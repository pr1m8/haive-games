games.go.models
===============

.. py:module:: games.go.models

Go game data models.

This module provides Pydantic models for representing Go game concepts:
    - Move coordinates and validation
    - Player decisions
    - Position analysis and evaluation
    - Territory control tracking

.. rubric:: Example

>>> from haive.games.go.models import GoMoveModel, GoAnalysis
>>>
>>> # Create and validate a move
>>> move = GoMoveModel(move=(3, 4), board_size=19)
>>> move.to_tuple()
(3, 4)
>>>
>>> # Create a position analysis
>>> analysis = GoAnalysis(
...     territory_control={"black": 45, "white": 40},
...     strong_positions=[(3, 3), (15, 15)],
...     weak_positions=[(0, 0)],
...     suggested_strategies=["Strengthen the center group"]
... )



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">3 classes</span>   </div>

.. autoapi-nested-parse::

   Go game data models.

   This module provides Pydantic models for representing Go game concepts:
       - Move coordinates and validation
       - Player decisions
       - Position analysis and evaluation
       - Territory control tracking

   .. rubric:: Example

   >>> from haive.games.go.models import GoMoveModel, GoAnalysis
   >>>
   >>> # Create and validate a move
   >>> move = GoMoveModel(move=(3, 4), board_size=19)
   >>> move.to_tuple()
   (3, 4)
   >>>
   >>> # Create a position analysis
   >>> analysis = GoAnalysis(
   ...     territory_control={"black": 45, "white": 40},
   ...     strong_positions=[(3, 3), (15, 15)],
   ...     weak_positions=[(0, 0)],
   ...     suggested_strategies=["Strengthen the center group"]
   ... )



      
            
            

.. admonition:: Classes (3)
   :class: note

   .. autoapisummary::

      games.go.models.GoAnalysis
      games.go.models.GoMoveModel
      games.go.models.GoPlayerDecision

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GoAnalysis(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A model for storing Go position analysis.

            This model captures a comprehensive analysis of a Go position,
            including territory control, key positions, and strategic advice.

            .. attribute:: territory_control

               Estimated territory for each player.

               :type: Dict[str, int]

            .. attribute:: strong_positions

               List of strong positions.

               :type: List[Tuple[int, int]]

            .. attribute:: weak_positions

               List of vulnerable positions.

               :type: List[Tuple[int, int]]

            .. attribute:: suggested_strategies

               List of strategic recommendations.

               :type: List[str]

            .. rubric:: Example

            >>> analysis = GoAnalysis(
            ...     territory_control={"black": 45, "white": 40},
            ...     strong_positions=[(3, 3), (15, 15)],
            ...     weak_positions=[(0, 0)],
            ...     suggested_strategies=[
            ...         "Strengthen the center group",
            ...         "Consider invading the top right"
            ...     ]
            ... )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: strong_positions
               :type:  list[tuple[int, int]]
               :value: None



            .. py:attribute:: suggested_strategies
               :type:  list[str]
               :value: None



            .. py:attribute:: territory_control
               :type:  dict[Literal['black', 'white'], int]
               :value: None



            .. py:attribute:: weak_positions
               :type:  list[tuple[int, int]]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GoMoveModel(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A model representing a move in Go.

            This model validates and stores move coordinates, ensuring they are
            within the bounds of the game board.

            .. attribute:: move

               The (row, col) coordinates of the move.

               :type: Tuple[int, int]

            .. attribute:: board_size

               Size of the game board (default 19x19).

               :type: int

            .. rubric:: Example

            >>> move = GoMoveModel(move=(3, 4))
            >>> move.validate_move((3, 4), {"board_size": 19})
            (3, 4)
            >>> move.to_tuple()
            (3, 4)
            >>>
            >>> # Invalid move raises error
            >>> GoMoveModel(move=(19, 19))  # Out of bounds
            ValueError: Move (19, 19) is out of bounds for a 19x19 board.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: to_tuple() -> tuple[int, int]

               Convert the move to a simple coordinate tuple.

               :returns: The move coordinates as (row, col).
               :rtype: Tuple[int, int]



            .. py:method:: validate_move(move: tuple[int, int], values) -> tuple[int, int]
               :classmethod:


               Validate that a move is within board bounds.

               :param move: The move coordinates to validate.
               :type move: Tuple[int, int]
               :param values: Dictionary containing model field values.
               :type values: dict

               :returns: The validated move coordinates.
               :rtype: Tuple[int, int]

               :raises ValueError: If move coordinates are outside board bounds.



            .. py:attribute:: board_size
               :type:  int
               :value: None



            .. py:attribute:: move
               :type:  tuple[int, int]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GoPlayerDecision(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A model representing a player's move decision.

            This model encapsulates a player's decision about their next move,
            including validation of the move coordinates.

            .. attribute:: move

               The chosen move coordinates and validation.

               :type: GoMoveModel

            .. rubric:: Example

            >>> decision = GoPlayerDecision(
            ...     move=GoMoveModel(move=(3, 4))
            ... )
            >>> decision.move.to_tuple()
            (3, 4)

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: move
               :type:  GoMoveModel
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.go.models import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

