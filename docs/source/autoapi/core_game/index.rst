core_game
=========

.. py:module:: core_game

.. autoapi-nested-parse::

   Game engine for the game framework.

   This module defines the base Game class that serves as the central point for game logic,
   integrating all framework components.


   .. autolink-examples:: core_game
      :collapse:


Attributes
----------

.. autoapisummary::

   core_game.C
   core_game.M
   core_game.P
   core_game.PL
   core_game.S
   core_game.T


Classes
-------

.. autoapisummary::

   core_game.Game
   core_game.GameConfiguration
   core_game.GameFactory
   core_game.GameResult
   core_game.GameStatus
   core_game.RealTimeGame
   core_game.TurnBasedGame


Module Contents
---------------

.. py:class:: Game(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`P`\ , :py:obj:`T`\ , :py:obj:`S`\ , :py:obj:`C`\ , :py:obj:`M`\ , :py:obj:`PL`\ ]


   Base class for all games.

   The Game class ties together all game components and implements the core game loop.
   It manages the game state, players, turns, and rules.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Game
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: _trigger_event(event: str, **kwargs) -> None

      Trigger an event, calling all registered callbacks.

      :param event: Event name
      :param \*\*kwargs: Event data


      .. autolink-examples:: _trigger_event
         :collapse:


   .. py:method:: abort() -> None

      Abort the game.


      .. autolink-examples:: abort
         :collapse:


   .. py:method:: add_player(player: PL) -> None

      Add a player to the game.

      :param player: Player to add


      .. autolink-examples:: add_player
         :collapse:


   .. py:method:: check_end_condition() -> bool
      :abstractmethod:


      Check if the game has reached an end condition.

      :returns: True if the game should end, False otherwise


      .. autolink-examples:: check_end_condition
         :collapse:


   .. py:method:: create_position(position_data: dict[str, Any]) -> P | None
      :abstractmethod:


      Create a Position object from a dictionary representation.

      :param position_data: Dictionary with position data

      :returns: Position object, or None if invalid


      .. autolink-examples:: create_position
         :collapse:


   .. py:method:: determine_winner() -> None
      :abstractmethod:


      Determine the winner(s) of the game.

      This should set the result and winners properties.



      .. autolink-examples:: determine_winner
         :collapse:


   .. py:method:: end_turn() -> None

      End the current turn and move to the next player.


      .. autolink-examples:: end_turn
         :collapse:


   .. py:method:: finish(result: GameResult, winners: list[str] = None) -> None

      Finish the game with a result.

      :param result: Result of the game
      :param winners: List of winning player IDs


      .. autolink-examples:: finish
         :collapse:


   .. py:method:: get_container(container_id: str) -> C | None

      Get a container by ID.

      :param container_id: ID of the container

      :returns: The container, or None if not found


      .. autolink-examples:: get_container
         :collapse:


   .. py:method:: get_current_player() -> PL | None

      Get the current player.


      .. autolink-examples:: get_current_player
         :collapse:


   .. py:method:: get_piece(piece_id: str) -> T | None

      Get a piece by ID.

      :param piece_id: ID of the piece

      :returns: The piece, or None if not found


      .. autolink-examples:: get_piece
         :collapse:


   .. py:method:: get_property(key: str, default: Any = None) -> Any

      Get a game property.

      :param key: Property name
      :param default: Default value if property doesn't exist

      :returns: Property value or default


      .. autolink-examples:: get_property
         :collapse:


   .. py:method:: get_state_for_player(player_id: str) -> dict[str, Any]

      Get a representation of the game state for a specific player.

      This should include only information visible to that player.

      :param player_id: ID of the player

      :returns: Dictionary with game state information


      .. autolink-examples:: get_state_for_player
         :collapse:


   .. py:method:: get_valid_moves(player_id: str) -> list[M]
      :abstractmethod:


      Get all valid moves for a player.

      :param player_id: ID of the player

      :returns: List of valid moves


      .. autolink-examples:: get_valid_moves
         :collapse:


   .. py:method:: initialize() -> None

      Initialize the game.

      This should be called after adding players and before starting the game.



      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: is_finished() -> bool

      Check if the game is finished.


      .. autolink-examples:: is_finished
         :collapse:


   .. py:method:: pause() -> None

      Pause the game.


      .. autolink-examples:: pause
         :collapse:


   .. py:method:: process_move(move: M) -> game.core.move.MoveResult[M]

      Process a move from a player.

      :param move: Move to process

      :returns: Result of the move


      .. autolink-examples:: process_move
         :collapse:


   .. py:method:: register_callback(event: str, callback: collections.abc.Callable) -> None

      Register a callback for a game event.

      :param event: Event name
      :param callback: Callback function


      .. autolink-examples:: register_callback
         :collapse:


   .. py:method:: resume() -> None

      Resume a paused game.


      .. autolink-examples:: resume
         :collapse:


   .. py:method:: set_property(key: str, value: Any) -> None

      Set a game property.

      :param key: Property name
      :param value: Property value


      .. autolink-examples:: set_property
         :collapse:


   .. py:method:: setup_game() -> None
      :abstractmethod:


      Set up the game-specific components.

      This should be implemented by subclasses to create the board, pieces, and other
      game elements.



      .. autolink-examples:: setup_game
         :collapse:


   .. py:method:: start() -> None

      Start the game.


      .. autolink-examples:: start
         :collapse:


   .. py:method:: start_turn() -> None

      Start a new turn.


      .. autolink-examples:: start_turn
         :collapse:


   .. py:method:: unregister_callback(event: str, callback: collections.abc.Callable) -> None

      Unregister a callback for a game event.

      :param event: Event name
      :param callback: Callback function


      .. autolink-examples:: unregister_callback
         :collapse:


   .. py:attribute:: board
      :type:  game.core.board.Board[S, P, T] | None
      :value: None



   .. py:attribute:: callbacks
      :type:  dict[str, list[collections.abc.Callable]]
      :value: None



   .. py:attribute:: config
      :type:  GameConfiguration


   .. py:attribute:: containers
      :type:  dict[str, C]
      :value: None



   .. py:attribute:: current_player_index
      :type:  int
      :value: 0



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: move_history
      :type:  list[game.core.move.MoveResult[M]]
      :value: None



   .. py:attribute:: name
      :type:  str


   .. py:attribute:: pieces
      :type:  dict[str, T]
      :value: None



   .. py:attribute:: players
      :type:  list[PL]
      :value: None



   .. py:attribute:: properties
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: result
      :type:  GameResult


   .. py:attribute:: round_number
      :type:  int
      :value: 0



   .. py:attribute:: scores
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: status
      :type:  GameStatus


   .. py:attribute:: turn_number
      :type:  int
      :value: 0



   .. py:attribute:: winners
      :type:  list[str]
      :value: None



.. py:class:: GameConfiguration(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration options for a game.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GameConfiguration
      :collapse:

   .. py:method:: is_valid_player_count(count: int) -> bool

      Check if a player count is valid for this game.


      .. autolink-examples:: is_valid_player_count
         :collapse:


   .. py:method:: validate_player_count(v: int) -> int
      :classmethod:


      Ensure player counts are valid.


      .. autolink-examples:: validate_player_count
         :collapse:


   .. py:attribute:: allow_ai_players
      :type:  bool
      :value: True



   .. py:attribute:: allow_network_players
      :type:  bool
      :value: True



   .. py:attribute:: enable_observers
      :type:  bool
      :value: True



   .. py:attribute:: max_players
      :type:  int
      :value: 2



   .. py:attribute:: min_players
      :type:  int
      :value: 1



   .. py:attribute:: name
      :type:  str


   .. py:attribute:: options
      :type:  dict[str, Any]
      :value: None



.. py:class:: GameFactory

   Factory for creating game instances.


   .. autolink-examples:: GameFactory
      :collapse:

   .. py:method:: create_game(game_type: type[Game], config: GameConfiguration, **kwargs) -> Game
      :staticmethod:


      Create a game instance.

      :param game_type: Type of game to create
      :param config: Game configuration
      :param \*\*kwargs: Additional arguments for the game constructor

      :returns: Game instance


      .. autolink-examples:: create_game
         :collapse:


.. py:class:: GameResult

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Result of a finished game.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GameResult
      :collapse:

   .. py:attribute:: DRAW
      :value: 'draw'



   .. py:attribute:: UNDETERMINED
      :value: 'undetermined'



   .. py:attribute:: WIN
      :value: 'win'



.. py:class:: GameStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Status of a game.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GameStatus
      :collapse:

   .. py:attribute:: ABORTED
      :value: 'aborted'



   .. py:attribute:: FINISHED
      :value: 'finished'



   .. py:attribute:: IN_PROGRESS
      :value: 'in_progress'



   .. py:attribute:: NOT_STARTED
      :value: 'not_started'



   .. py:attribute:: PAUSED
      :value: 'paused'



.. py:class:: RealTimeGame

   Bases: :py:obj:`Game`\ [\ :py:obj:`P`\ , :py:obj:`T`\ , :py:obj:`S`\ , :py:obj:`C`\ , :py:obj:`M`\ , :py:obj:`PL`\ ]


   Base class for real-time games.

   This adds functionality for games that don't use strict turns.



   .. autolink-examples:: RealTimeGame
      :collapse:

   .. py:method:: is_action_on_cooldown(player_id: str, action_type: str) -> bool

      Check if an action is on cooldown.

      :param player_id: ID of the player
      :param action_type: Type of action

      :returns: True if the action is on cooldown, False otherwise


      .. autolink-examples:: is_action_on_cooldown
         :collapse:


   .. py:method:: process_move(move: M) -> game.core.move.MoveResult[M]

      Process a move from a player, checking cooldowns.

      :param move: Move to process

      :returns: Result of the move


      .. autolink-examples:: process_move
         :collapse:


   .. py:method:: set_cooldown(player_id: str, action_type: str, ticks: int) -> None

      Set a cooldown for an action.

      :param player_id: ID of the player
      :param action_type: Type of action
      :param ticks: Number of ticks until the action is available again


      .. autolink-examples:: set_cooldown
         :collapse:


   .. py:method:: update(delta_time: float) -> None

      Update the game state for a time step.

      :param delta_time: Time in seconds since last update


      .. autolink-examples:: update
         :collapse:


   .. py:method:: update_game_state(delta_time: float) -> None
      :abstractmethod:


      Update the game state for a time step.

      :param delta_time: Time in seconds since last update


      .. autolink-examples:: update_game_state
         :collapse:


   .. py:attribute:: action_cooldowns
      :type:  dict[str, dict[str, int]]
      :value: None



   .. py:attribute:: current_tick
      :type:  int
      :value: 0



   .. py:attribute:: tick_rate
      :type:  float
      :value: 60.0



.. py:class:: TurnBasedGame

   Bases: :py:obj:`Game`\ [\ :py:obj:`P`\ , :py:obj:`T`\ , :py:obj:`S`\ , :py:obj:`C`\ , :py:obj:`M`\ , :py:obj:`PL`\ ]


   Base class for turn-based games.

   This adds additional turn management functionality.



   .. autolink-examples:: TurnBasedGame
      :collapse:

   .. py:method:: can_take_action(player_id: str) -> bool

      Check if a player can take another action this turn.

      :param player_id: ID of the player

      :returns: True if the player can take an action, False otherwise


      .. autolink-examples:: can_take_action
         :collapse:


   .. py:method:: end_turn() -> None

      End the current turn and move to the next player.


      .. autolink-examples:: end_turn
         :collapse:


   .. py:method:: process_move(move: M) -> game.core.move.MoveResult[M]

      Process a move from a player, tracking actions per turn.

      :param move: Move to process

      :returns: Result of the move


      .. autolink-examples:: process_move
         :collapse:


   .. py:method:: record_action(player_id: str) -> None

      Record an action taken by a player this turn.

      :param player_id: ID of the player


      .. autolink-examples:: record_action
         :collapse:


   .. py:method:: reverse_turn_order() -> None

      Reverse the turn order direction.


      .. autolink-examples:: reverse_turn_order
         :collapse:


   .. py:method:: skip_turn() -> None

      Skip the current player's turn.


      .. autolink-examples:: skip_turn
         :collapse:


   .. py:attribute:: max_actions_per_turn
      :type:  int
      :value: 1



   .. py:attribute:: turn_actions
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: turn_direction
      :type:  int
      :value: 1



   .. py:attribute:: turn_timeout
      :type:  int | None
      :value: None



.. py:data:: C

.. py:data:: M

.. py:data:: P

.. py:data:: PL

.. py:data:: S

.. py:data:: T

