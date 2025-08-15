games.base.state_manager
========================

.. py:module:: games.base.state_manager

.. autoapi-nested-parse::

   Base state manager module for game agents.

   This module provides the foundational state manager class that handles
   game state transitions and operations. It defines the interface that all
   game-specific state managers should implement.

   .. rubric:: Example

   >>> class ChessStateManager(GameStateManager[ChessMove]):
   ...     @classmethod
   ...     def initialize(cls) -> ChessState:
   ...         return ChessState.new_game()
   ...
   ...     @classmethod
   ...     def apply_move(cls, state: ChessState, move: ChessMove) -> ChessState:
   ...         return state.apply_move(move)

   Typical usage:
       - Inherit from GameStateManager to create game-specific state managers
       - Implement the required methods for state initialization and transitions
       - Use in conjunction with game agents to manage game flow


   .. autolink-examples:: games.base.state_manager
      :collapse:


Attributes
----------

.. autoapisummary::

   games.base.state_manager.T


Classes
-------

.. autoapisummary::

   games.base.state_manager.GameStateManager


Module Contents
---------------

.. py:class:: GameStateManager

   Bases: :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   Base state manager that implements common game state operations.

   This class provides the interface for managing game state transitions
   and operations. Each game should extend this with game-specific logic
   by implementing the required methods.

   Type Parameters:
       T: The type of the game state, must be a Pydantic BaseModel.

   .. rubric:: Example

   >>> class ChessStateManager(GameStateManager[ChessState]):
   ...     @classmethod
   ...     def initialize(cls) -> ChessState:
   ...         return ChessState.new_game()
   ...
   ...     @classmethod
   ...     def apply_move(cls, state: ChessState, move: ChessMove) -> ChessState:
   ...         return state.apply_move(move)


   .. autolink-examples:: GameStateManager
      :collapse:

   .. py:method:: apply_move(state: T, move: Any) -> T
      :classmethod:

      :abstractmethod:


      Apply a move to the game state.

      This method should create and return a new game state that reflects
      the application of the given move to the current state.

      :param state: The current game state.
      :type state: T
      :param move: The move to apply.
      :type move: Any

      :returns: A new game state after applying the move.
      :rtype: T

      :raises NotImplementedError: This method must be implemented by subclasses.

      .. rubric:: Example

      >>> @classmethod
      ... def apply_move(cls, state: ChessState, move: ChessMove) -> ChessState:
      ...     new_board = state.board.make_move(move)
      ...     return ChessState(
      ...         board=new_board,
      ...         turn="black" if state.turn == "white" else "white",
      ...         move_history=state.move_history + [move]
      ...     )


      .. autolink-examples:: apply_move
         :collapse:


   .. py:method:: check_game_status(state: T) -> T
      :classmethod:

      :abstractmethod:


      Check and update the game status.

      This method should examine the current game state and determine if
      the game status needs to be updated (e.g., if someone has won or
      if the game is a draw).

      :param state: The current game state.
      :type state: T

      :returns: The game state with updated status.
      :rtype: T

      :raises NotImplementedError: This method must be implemented by subclasses.

      .. rubric:: Example

      >>> @classmethod
      ... def check_game_status(cls, state: ChessState) -> ChessState:
      ...     if state.board.is_checkmate():
      ...         state.game_status = "checkmate"
      ...     elif state.board.is_stalemate():
      ...         state.game_status = "stalemate"
      ...     return state


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: get_legal_moves(state: T) -> list[Any]
      :classmethod:

      :abstractmethod:


      Get all legal moves for the current state.

      This method should return a list of all valid moves that can be made
      from the current game state.

      :param state: The current game state.
      :type state: T

      :returns: A list of legal moves.
      :rtype: List[Any]

      :raises NotImplementedError: This method must be implemented by subclasses.

      .. rubric:: Example

      >>> @classmethod
      ... def get_legal_moves(cls, state: ChessState) -> List[ChessMove]:
      ...     return state.board.get_legal_moves(state.turn)


      .. autolink-examples:: get_legal_moves
         :collapse:


   .. py:method:: initialize(**kwargs) -> T
      :classmethod:

      :abstractmethod:


      Initialize a new game state.

      This method should create and return a new instance of the game state
      with initial values set appropriately for the start of a game.

      :param \*\*kwargs: Additional keyword arguments for game-specific initialization.

      :returns: A new instance of the game state.
      :rtype: T

      :raises NotImplementedError: This method must be implemented by subclasses.

      .. rubric:: Example

      >>> @classmethod
      ... def initialize(cls) -> ChessState:
      ...     return ChessState(
      ...         board=Board.initial_setup(),
      ...         turn="white",
      ...         game_status="ongoing"
      ...     )


      .. autolink-examples:: initialize
         :collapse:


.. py:data:: T

