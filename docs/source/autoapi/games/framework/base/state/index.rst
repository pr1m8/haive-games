games.framework.base.state
==========================

.. py:module:: games.framework.base.state

.. autoapi-nested-parse::

   Base state module for game agents.

   This module provides the foundational state class for game agents,
   defining the core state attributes that all games need to track.

   .. rubric:: Example

   >>> # GameState is abstract - inherit from it:
   >>> class ConcreteGameState(GameState):
   ...     @classmethod
   ...     def initialize(cls, **kwargs):
   ...         return cls(turn="player1", game_status="ongoing")

   Typical usage:
       - Inherit from GameState to create game-specific state classes
       - Use as the state schema in game configurations
       - Track game progress and history


   .. autolink-examples:: games.framework.base.state
      :collapse:


Classes
-------

.. autoapisummary::

   games.framework.base.state.GameState


Module Contents
---------------

.. py:class:: GameState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`abc.ABC`


   Base game state that all game states should inherit from.

   This class defines the core state attributes that all games need to track,
   including the current turn, game status, move history, and error handling.

   .. attribute:: players

      List of players in the game.

      :type: List[str]

   .. attribute:: turn

      Current player's turn.

      :type: str

   .. attribute:: game_status

      Status of the game (e.g., "ongoing", "finished").

      :type: str

   .. attribute:: move_history

      History of moves made in the game.

      :type: List[Any]

   .. attribute:: error_message

      Error message if any error occurred.

      :type: Optional[str]

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GameState
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: initialize(**kwargs) -> GameState
      :classmethod:

      :abstractmethod:


      Abstract method that all subclasses must implement to initialize the game.
      state.

      :returns: A fully initialized game state object.
      :rtype: GameState

      .. rubric:: Example

      >>> return Connect4State.initialize(first_player="red")


      .. autolink-examples:: initialize
         :collapse:


   .. py:attribute:: error_message
      :type:  str | None
      :value: None



   .. py:attribute:: game_status
      :type:  str
      :value: None



   .. py:attribute:: move_history
      :type:  list[Any]
      :value: None



   .. py:attribute:: players
      :type:  list[str]
      :value: None



   .. py:attribute:: turn
      :type:  str
      :value: None



