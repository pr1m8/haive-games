core_game
=========

.. py:module:: core_game

Game engine for the game framework.

This module defines the base Game class that serves as the central point for game logic,
integrating all framework components.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">7 classes</span> • <span class="module-stat">6 attributes</span>   </div>

.. autoapi-nested-parse::

   Game engine for the game framework.

   This module defines the base Game class that serves as the central point for game logic,
   integrating all framework components.



      

.. admonition:: Attributes (6)
   :class: tip

   .. autoapisummary::

      core_game.C
      core_game.M
      core_game.P
      core_game.PL
      core_game.S
      core_game.T

            
            

.. admonition:: Classes (7)
   :class: note

   .. autoapisummary::

      core_game.Game
      core_game.GameConfiguration
      core_game.GameFactory
      core_game.GameResult
      core_game.GameStatus
      core_game.RealTimeGame
      core_game.TurnBasedGame

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Game(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`P`\ , :py:obj:`T`\ , :py:obj:`S`\ , :py:obj:`C`\ , :py:obj:`M`\ , :py:obj:`PL`\ ]


            Base class for all games.

            The Game class ties together all game components and implements the core game loop.
            It manages the game state, players, turns, and rules.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: _trigger_event(event: str, **kwargs) -> None

               Trigger an event, calling all registered callbacks.

               :param event: Event name
               :param \*\*kwargs: Event data



            .. py:method:: abort() -> None

               Abort the game.



            .. py:method:: add_player(player: PL) -> None

               Add a player to the game.

               :param player: Player to add



            .. py:method:: check_end_condition() -> bool
               :abstractmethod:


               Check if the game has reached an end condition.

               :returns: True if the game should end, False otherwise



            .. py:method:: create_position(position_data: dict[str, Any]) -> P | None
               :abstractmethod:


               Create a Position object from a dictionary representation.

               :param position_data: Dictionary with position data

               :returns: Position object, or None if invalid



            .. py:method:: determine_winner() -> None
               :abstractmethod:


               Determine the winner(s) of the game.

               This should set the result and winners properties.




            .. py:method:: end_turn() -> None

               End the current turn and move to the next player.



            .. py:method:: finish(result: GameResult, winners: list[str] = None) -> None

               Finish the game with a result.

               :param result: Result of the game
               :param winners: List of winning player IDs



            .. py:method:: get_container(container_id: str) -> C | None

               Get a container by ID.

               :param container_id: ID of the container

               :returns: The container, or None if not found



            .. py:method:: get_current_player() -> PL | None

               Get the current player.



            .. py:method:: get_piece(piece_id: str) -> T | None

               Get a piece by ID.

               :param piece_id: ID of the piece

               :returns: The piece, or None if not found



            .. py:method:: get_property(key: str, default: Any = None) -> Any

               Get a game property.

               :param key: Property name
               :param default: Default value if property doesn't exist

               :returns: Property value or default



            .. py:method:: get_state_for_player(player_id: str) -> dict[str, Any]

               Get a representation of the game state for a specific player.

               This should include only information visible to that player.

               :param player_id: ID of the player

               :returns: Dictionary with game state information



            .. py:method:: get_valid_moves(player_id: str) -> list[M]
               :abstractmethod:


               Get all valid moves for a player.

               :param player_id: ID of the player

               :returns: List of valid moves



            .. py:method:: initialize() -> None

               Initialize the game.

               This should be called after adding players and before starting the game.




            .. py:method:: is_finished() -> bool

               Check if the game is finished.



            .. py:method:: pause() -> None

               Pause the game.



            .. py:method:: process_move(move: M) -> game.core.move.MoveResult[M]

               Process a move from a player.

               :param move: Move to process

               :returns: Result of the move



            .. py:method:: register_callback(event: str, callback: collections.abc.Callable) -> None

               Register a callback for a game event.

               :param event: Event name
               :param callback: Callback function



            .. py:method:: resume() -> None

               Resume a paused game.



            .. py:method:: set_property(key: str, value: Any) -> None

               Set a game property.

               :param key: Property name
               :param value: Property value



            .. py:method:: setup_game() -> None
               :abstractmethod:


               Set up the game-specific components.

               This should be implemented by subclasses to create the board, pieces, and other
               game elements.




            .. py:method:: start() -> None

               Start the game.



            .. py:method:: start_turn() -> None

               Start a new turn.



            .. py:method:: unregister_callback(event: str, callback: collections.abc.Callable) -> None

               Unregister a callback for a game event.

               :param event: Event name
               :param callback: Callback function



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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameConfiguration(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Configuration options for a game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: is_valid_player_count(count: int) -> bool

               Check if a player count is valid for this game.



            .. py:method:: validate_player_count(v: int) -> int
               :classmethod:


               Ensure player counts are valid.



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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameFactory

            Factory for creating game instances.


            .. py:method:: create_game(game_type: type[Game], config: GameConfiguration, **kwargs) -> Game
               :staticmethod:


               Create a game instance.

               :param game_type: Type of game to create
               :param config: Game configuration
               :param \*\*kwargs: Additional arguments for the game constructor

               :returns: Game instance




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameResult

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Result of a finished game.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: DRAW
               :value: 'draw'



            .. py:attribute:: UNDETERMINED
               :value: 'undetermined'



            .. py:attribute:: WIN
               :value: 'win'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameStatus

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Status of a game.

            Initialize self.  See help(type(self)) for accurate signature.


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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: RealTimeGame

            Bases: :py:obj:`Game`\ [\ :py:obj:`P`\ , :py:obj:`T`\ , :py:obj:`S`\ , :py:obj:`C`\ , :py:obj:`M`\ , :py:obj:`PL`\ ]


            Base class for real-time games.

            This adds functionality for games that don't use strict turns.



            .. py:method:: is_action_on_cooldown(player_id: str, action_type: str) -> bool

               Check if an action is on cooldown.

               :param player_id: ID of the player
               :param action_type: Type of action

               :returns: True if the action is on cooldown, False otherwise



            .. py:method:: process_move(move: M) -> game.core.move.MoveResult[M]

               Process a move from a player, checking cooldowns.

               :param move: Move to process

               :returns: Result of the move



            .. py:method:: set_cooldown(player_id: str, action_type: str, ticks: int) -> None

               Set a cooldown for an action.

               :param player_id: ID of the player
               :param action_type: Type of action
               :param ticks: Number of ticks until the action is available again



            .. py:method:: update(delta_time: float) -> None

               Update the game state for a time step.

               :param delta_time: Time in seconds since last update



            .. py:method:: update_game_state(delta_time: float) -> None
               :abstractmethod:


               Update the game state for a time step.

               :param delta_time: Time in seconds since last update



            .. py:attribute:: action_cooldowns
               :type:  dict[str, dict[str, int]]
               :value: None



            .. py:attribute:: current_tick
               :type:  int
               :value: 0



            .. py:attribute:: tick_rate
               :type:  float
               :value: 60.0




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: TurnBasedGame

            Bases: :py:obj:`Game`\ [\ :py:obj:`P`\ , :py:obj:`T`\ , :py:obj:`S`\ , :py:obj:`C`\ , :py:obj:`M`\ , :py:obj:`PL`\ ]


            Base class for turn-based games.

            This adds additional turn management functionality.



            .. py:method:: can_take_action(player_id: str) -> bool

               Check if a player can take another action this turn.

               :param player_id: ID of the player

               :returns: True if the player can take an action, False otherwise



            .. py:method:: end_turn() -> None

               End the current turn and move to the next player.



            .. py:method:: process_move(move: M) -> game.core.move.MoveResult[M]

               Process a move from a player, tracking actions per turn.

               :param move: Move to process

               :returns: Result of the move



            .. py:method:: record_action(player_id: str) -> None

               Record an action taken by a player this turn.

               :param player_id: ID of the player



            .. py:method:: reverse_turn_order() -> None

               Reverse the turn order direction.



            .. py:method:: skip_turn() -> None

               Skip the current player's turn.



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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: C


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: M


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: P


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: PL


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: S


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: T




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from core_game import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

