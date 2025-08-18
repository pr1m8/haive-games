games.go.state
==============

.. py:module:: games.go.state

Go game state management.

This module provides state tracking and management for Go games, including:
    - Game state representation
    - Move validation and application
    - Board state tracking in SGF format
    - Capture counting
    - Game status management

.. rubric:: Example

>>> from haive.games.go.state import GoGameState, GoGameStateManager
>>>
>>> # Initialize a new game
>>> state = GoGameStateManager.initialize(board_size=19)
>>>
>>> # Apply moves
>>> state = GoGameStateManager.apply_move(state, (3, 4))  # Black's move
>>> state = GoGameStateManager.apply_move(state, (15, 15))  # White's move
>>>
>>> # Check game status
>>> print(state.game_status)  # 'ongoing'
>>> print(state.captured_stones)  # {'black': 0, 'white': 0}



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Go game state management.

   This module provides state tracking and management for Go games, including:
       - Game state representation
       - Move validation and application
       - Board state tracking in SGF format
       - Capture counting
       - Game status management

   .. rubric:: Example

   >>> from haive.games.go.state import GoGameState, GoGameStateManager
   >>>
   >>> # Initialize a new game
   >>> state = GoGameStateManager.initialize(board_size=19)
   >>>
   >>> # Apply moves
   >>> state = GoGameStateManager.apply_move(state, (3, 4))  # Black's move
   >>> state = GoGameStateManager.apply_move(state, (15, 15))  # White's move
   >>>
   >>> # Check game status
   >>> print(state.game_status)  # 'ongoing'
   >>> print(state.captured_stones)  # {'black': 0, 'white': 0}



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.go.state.GoGameState

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GoGameState(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A model representing the complete state of a Go game.

            This class tracks all aspects of a Go game's state, including:
                - Board configuration and size
                - Move history
                - Captured stones
                - Game status and result
                - Error conditions

            .. attribute:: board_size

               Size of the Go board (default: 19x19).

               :type: int

            .. attribute:: board_sgf

               Current board state in SGF format.

               :type: str

            .. attribute:: move_history

               List of played moves as
               (color, row, col) tuples.

               :type: List[Tuple[str, int, int]]

            .. attribute:: captured_stones

               Count of stones captured by each player.

               :type: Dict[str, int]

            .. attribute:: turn

               Current player to move ("black" or "white").

               :type: str

            .. attribute:: game_status

               Current game status (ongoing/ended/resignation/timeout).

               :type: str

            .. attribute:: passes

               Count of consecutive pass moves.

               :type: int

            .. attribute:: error_message

               Error message if any.

               :type: Optional[str]

            .. attribute:: game_result

               Final game result if game is ended.

               :type: Optional[str]

            .. rubric:: Example

            >>> state = GoGameState(
            ...     board_sgf=sente.sgf.dumps(sente.Game(19)),
            ...     turn="black",
            ...     captured_stones={"black": 0, "white": 0}
            ... )
            >>> state.validate_turn("black", {"board_sgf": state.board_sgf})
            'black'

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: validate_turn(v, info) -> str
               :classmethod:


               Validate that the turn matches the board state.

               This validator ensures the turn field matches the actual board state
               by checking against the SGF representation.

               :param v: The turn value to validate.
               :type v: str
               :param info: Validation context with other field values.
               :type info: ValidationInfo

               :returns: The validated turn value.
               :rtype: str

               :raises ValueError: If turn doesn't match the board state.



            .. py:attribute:: board_sgf
               :type:  str
               :value: None



            .. py:attribute:: board_size
               :type:  int
               :value: None



            .. py:attribute:: captured_stones
               :type:  dict[Literal['black', 'white'], int]
               :value: None



            .. py:attribute:: error_message
               :type:  str | None
               :value: None



            .. py:attribute:: game_result
               :type:  str | None
               :value: None



            .. py:attribute:: game_status
               :type:  Literal['ongoing', 'ended', 'resignation', 'timeout']
               :value: None



            .. py:attribute:: move_history
               :type:  list[tuple[str, int, int]]
               :value: None



            .. py:attribute:: passes
               :type:  int
               :value: None



            .. py:attribute:: turn
               :type:  Literal['black', 'white']
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.go.state import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

