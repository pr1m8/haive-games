games.nim.state_manager
=======================

.. py:module:: games.nim.state_manager

.. autoapi-nested-parse::

   Nim game state management module.

   This module provides comprehensive state management functionality for the Nim game,
   including game initialization, move validation, and game status tracking.

   The Nim game is a mathematical strategy game where players take turns removing
   stones from piles. The goal varies by game mode:
   - Standard mode: The player who takes the last stone wins
   - Misère mode: The player who takes the last stone loses

   Classes:
       NimStateManager: Main state management class for Nim game operations.

   .. rubric:: Example

   Basic Nim game setup and play:

       >>> from haive.games.nim.state_manager import NimStateManager
       >>> from haive.games.nim.models import NimMove
       >>>
       >>> # Initialize game with custom pile sizes
       >>> state = NimStateManager.initialize(pile_sizes=[3, 5, 7])
       >>> print(f"Starting piles: {state.piles}")
       >>>
       >>> # Get legal moves for current player
       >>> legal_moves = NimStateManager.get_legal_moves(state)
       >>> print(f"Available moves: {len(legal_moves)}")
       >>>
       >>> # Make a move
       >>> move = NimMove(pile_index=1, stones_taken=3, player="player1")
       >>> new_state = NimStateManager.apply_move(state, move)
       >>> print(f"New piles: {new_state.piles}")

   .. note::

      This implementation follows the Game State Manager pattern used throughout
      the haive-games package, providing consistent interfaces across all games.


   .. autolink-examples:: games.nim.state_manager
      :collapse:


Classes
-------

.. autoapisummary::

   games.nim.state_manager.NimStateManager


Module Contents
---------------

.. py:class:: NimStateManager

   Bases: :py:obj:`haive.games.framework.base.state_manager.GameStateManager`\ [\ :py:obj:`haive.games.nim.state.NimState`\ ]


   Manager for Nim game state.

   This class provides methods for initializing a new Nim game, retrieving legal moves,
   applying moves, adding analyses, and checking game status.



   .. autolink-examples:: NimStateManager
      :collapse:

   .. py:method:: add_analysis(state: haive.games.nim.state.NimState, player: str, analysis: haive.games.nim.models.NimAnalysis) -> haive.games.nim.state.NimState
      :classmethod:


      Add an analysis to the state.

      :param state: The current game state.
      :param player: The player who performed the analysis.
      :param analysis: The analysis to add.

      :returns: Updated state with the analysis added.
      :rtype: NimState


      .. autolink-examples:: add_analysis
         :collapse:


   .. py:method:: apply_move(state: haive.games.nim.state.NimState, move: haive.games.nim.models.NimMove) -> haive.games.nim.state.NimState
      :classmethod:


      Apply a move to the current state and return the new state.

      :param state: The current game state.
      :param move: The move to apply.

      :returns: A new game state after applying the move.
      :rtype: NimState

      :raises ValueError: If the move is invalid.


      .. autolink-examples:: apply_move
         :collapse:


   .. py:method:: check_game_status(state: haive.games.nim.state.NimState) -> haive.games.nim.state.NimState
      :classmethod:


      Check and update the game status.

      :param state: The current game state.

      :returns: The game state with updated status.
      :rtype: NimState


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: get_legal_moves(state: haive.games.nim.state.NimState, player: str = None) -> list[haive.games.nim.models.NimMove]
      :classmethod:


      Get all legal moves for the current state.

      :param state: The current game state.
      :param player: The player making the moves. If None, uses current player from state.

      :returns: A list of all legal moves.
      :rtype: List[NimMove]


      .. autolink-examples:: get_legal_moves
         :collapse:


   .. py:method:: get_winner(state: haive.games.nim.state.NimState) -> str | None
      :classmethod:


      Get the winner of the game, if any.

      :param state: The current game state.

      :returns: The winner, or None if the game is ongoing.
      :rtype: Optional[str]


      .. autolink-examples:: get_winner
         :collapse:


   .. py:method:: initialize(**kwargs) -> haive.games.nim.state.NimState
      :classmethod:


      Initialize a new Nim game with the given pile sizes.

      :param \*\*kwargs: Keyword arguments for game initialization.
                         pile_sizes: Optional list of pile sizes. Defaults to [3, 5, 7].

      :returns: A new Nim game state.
      :rtype: NimState


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: make_move(state: haive.games.nim.state.NimState | dict[str, Any], player: str, move: haive.games.nim.models.NimMove) -> langgraph.types.Command
      :classmethod:


      Make a move and return a Command with the updated state.

      :param state: The current game state.
      :param player: The player making the move.
      :param move: The move to make.

      :returns: Command with the updated state.
      :rtype: Command

      :raises ValueError: If it's not the player's turn.


      .. autolink-examples:: make_move
         :collapse:


