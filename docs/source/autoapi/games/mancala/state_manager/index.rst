games.mancala.state_manager
===========================

.. py:module:: games.mancala.state_manager

.. autoapi-nested-parse::

   State manager for the Mancala game.

   This module defines the state manager for the Mancala game, which manages the state of
   the game and provides methods for initializing, updating, and analyzing the game state.


   .. autolink-examples:: games.mancala.state_manager
      :collapse:


Attributes
----------

.. autoapisummary::

   games.mancala.state_manager.logger


Classes
-------

.. autoapisummary::

   games.mancala.state_manager.MancalaStateManager


Module Contents
---------------

.. py:class:: MancalaStateManager

   Bases: :py:obj:`haive.games.framework.base.state_manager.GameStateManager`\ [\ :py:obj:`haive.games.mancala.state.MancalaState`\ ]


   Manager for Mancala game state.

   This class provides methods for initializing, updating, and analyzing the game
   state.



   .. autolink-examples:: MancalaStateManager
      :collapse:

   .. py:method:: add_analysis(state: haive.games.mancala.state.MancalaState, player: str, analysis: Any) -> haive.games.mancala.state.MancalaState
      :classmethod:


      Add an analysis to the state.

      :param state: The current game state.
      :param player: The player who performed the analysis.
      :param analysis: The analysis to add.

      :returns: Updated state with the analysis added.
      :rtype: MancalaState


      .. autolink-examples:: add_analysis
         :collapse:


   .. py:method:: apply_move(state: haive.games.mancala.state.MancalaState, move: haive.games.mancala.models.MancalaMove) -> haive.games.mancala.state.MancalaState
      :classmethod:


      Apply a move to the current state according to Mancala rules.

      This method distributes stones from the selected pit, handles captures,
      checks for free turns, and updates the game status.

      :param state: The current game state.
      :param move: The move to apply, containing pit_index (0-5) and player.

      :returns: A new game state after applying the move.
      :rtype: MancalaState

      :raises ValueError: If the move is invalid (wrong player's turn, empty pit, etc.).

      Game Rules Implemented:
          1. Stones are distributed counterclockwise, one per pit.
          2. Player's own store is included; opponent's store is skipped.
          3. If the last stone lands in the player's store, they get another turn.
          4. If the last stone lands in an empty pit on the player's side, they
             capture that stone and all stones in the opposite pit.
          5. Game ends when all pits on one side are empty.



      .. autolink-examples:: apply_move
         :collapse:


   .. py:method:: check_game_status(state: haive.games.mancala.state.MancalaState) -> haive.games.mancala.state.MancalaState
      :classmethod:


      Check and update the game status.

      :param state: The current game state.

      :returns: The game state with updated status.
      :rtype: MancalaState


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: get_legal_moves(state: haive.games.mancala.state.MancalaState) -> list[haive.games.mancala.models.MancalaMove]
      :classmethod:


      Get all legal moves for the current player in the given state.

      :param state: The current game state.

      :returns: A list of all legal moves for the current player.
                Each move is represented as a MancalaMove object with pit_index (0-5)
                and player fields.
      :rtype: List[MancalaMove]

      .. note::

         Pit indices are always 0-5 for both players, representing the six pits
         on their side of the board (not including their store).


      .. autolink-examples:: get_legal_moves
         :collapse:


   .. py:method:: get_winner(state: haive.games.mancala.state.MancalaState) -> str | None
      :classmethod:


      Get the winner of the game, if any.

      :param state: The current game state.

      :returns: The winner, or None if the game is ongoing or a draw.
      :rtype: Optional[str]


      .. autolink-examples:: get_winner
         :collapse:


   .. py:method:: initialize(**kwargs) -> haive.games.mancala.state.MancalaState
      :classmethod:


      Initialize a new Mancala game with a fresh board and default settings.

      :param \*\*kwargs: Keyword arguments for game initialization.
                         stones_per_pit: Number of stones per pit initially. Defaults to 4.
                         Other keyword arguments are passed to the MancalaState constructor.

      :returns: A new Mancala game state ready to play.
      :rtype: MancalaState

      .. note::

         The board is initialized with the following layout:
         - Indices 0-5: Player 1's pits (bottom row, left to right)
         - Index 6: Player 1's store (right)
         - Indices 7-12: Player 2's pits (top row, right to left)
         - Index 13: Player 2's store (left)


      .. autolink-examples:: initialize
         :collapse:


.. py:data:: logger

