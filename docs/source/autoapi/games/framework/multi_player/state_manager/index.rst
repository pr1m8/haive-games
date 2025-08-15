games.framework.multi_player.state_manager
==========================================

.. py:module:: games.framework.multi_player.state_manager

.. autoapi-nested-parse::

   State management interface for multi-player games.

   This module provides the base state manager interface for multi-player games,
   defining the core operations that game-specific state managers must implement.
   The state manager handles:
       - Game initialization
       - Move application and validation
       - Legal move generation
       - Game status updates
       - Phase transitions
       - Information hiding

   .. rubric:: Example

   >>> from typing import List, Dict, Any
   >>> from haive.agents.agent_games.framework.multi_player.state_manager import MultiPlayerGameStateManager
   >>>
   >>> class MyGameStateManager(MultiPlayerGameStateManager[MyGameState]):
   ...     @classmethod
   ...     def initialize(cls, player_names: List[str], **kwargs) -> MyGameState:
   ...         return MyGameState(players=player_names)


   .. autolink-examples:: games.framework.multi_player.state_manager
      :collapse:


Attributes
----------

.. autoapisummary::

   games.framework.multi_player.state_manager.T


Classes
-------

.. autoapisummary::

   games.framework.multi_player.state_manager.MultiPlayerGameStateManager


Module Contents
---------------

.. py:class:: MultiPlayerGameStateManager

   Bases: :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   Manager for multi-player game states.

   This abstract base class defines the interface for managing game states
   in multi-player games. Game-specific implementations must inherit from
   this class and implement all abstract methods.

   Type Parameters:
       T: The game state type, must be a Pydantic BaseModel.

   .. rubric:: Example

   >>> class ChessStateManager(MultiPlayerGameStateManager[ChessState]):
   ...     @classmethod
   ...     def initialize(cls, player_names: List[str], **kwargs) -> ChessState:
   ...         return ChessState(
   ...             players=player_names,
   ...             board=cls.create_initial_board()
   ...         )


   .. autolink-examples:: MultiPlayerGameStateManager
      :collapse:

   .. py:method:: advance_phase(state: T) -> T
      :classmethod:

      :abstractmethod:


      Advance the game to the next phase.

      This method should handle phase transitions, including any
      necessary state updates or cleanup between phases.

      :param state: Current game state.
      :type state: T

      :returns: Updated game state in the new phase.
      :rtype: T

      :raises NotImplementedError: Must be implemented by subclass.


      .. autolink-examples:: advance_phase
         :collapse:


   .. py:method:: apply_move(state: T, player_id: str, move: Any) -> T
      :classmethod:

      :abstractmethod:


      Apply a move by a specific player.

      :param state: Current game state.
      :type state: T
      :param player_id: ID of the player making the move.
      :type player_id: str
      :param move: The move to apply.
      :type move: Any

      :returns: New game state after applying the move.
      :rtype: T

      :raises NotImplementedError: Must be implemented by subclass.


      .. autolink-examples:: apply_move
         :collapse:


   .. py:method:: check_game_status(state: T) -> T
      :classmethod:

      :abstractmethod:


      Check and update game status.

      This method should check for win conditions, draws, or other
      game-ending conditions and update the state accordingly.

      :param state: Current game state.
      :type state: T

      :returns: Updated game state with current status.
      :rtype: T

      :raises NotImplementedError: Must be implemented by subclass.


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: filter_state_for_player(state: T, player_id: str) -> dict[str, Any]
      :classmethod:

      :abstractmethod:


      Filter the state to include only information visible to a specific player.

      This method should implement information hiding, ensuring players
      only see game information they should have access to.

      :param state: Current game state.
      :type state: T
      :param player_id: ID of the player to filter for.
      :type player_id: str

      :returns: Filtered game state with only visible information.
      :rtype: Dict[str, Any]

      :raises NotImplementedError: Must be implemented by subclass.


      .. autolink-examples:: filter_state_for_player
         :collapse:


   .. py:method:: get_legal_moves(state: T, player_id: str) -> list[Any]
      :classmethod:

      :abstractmethod:


      Get legal moves for a specific player.

      :param state: Current game state.
      :type state: T
      :param player_id: ID of the player to get moves for.
      :type player_id: str

      :returns: List of legal moves for the player.
      :rtype: List[Any]

      :raises NotImplementedError: Must be implemented by subclass.


      .. autolink-examples:: get_legal_moves
         :collapse:


   .. py:method:: initialize(player_names: list[str], **kwargs) -> T
      :classmethod:

      :abstractmethod:


      Initialize a new game state with multiple players.

      :param player_names: List of player names/IDs.
      :type player_names: List[str]
      :param \*\*kwargs: Additional game-specific initialization parameters.

      :returns: A new game state instance.
      :rtype: T

      :raises NotImplementedError: Must be implemented by subclass.


      .. autolink-examples:: initialize
         :collapse:


.. py:data:: T

