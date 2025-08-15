games.single_player.state_manager
=================================

.. py:module:: games.single_player.state_manager


Classes
-------

.. autoapisummary::

   games.single_player.state_manager.SinglePlayerStateManager


Module Contents
---------------

.. py:class:: SinglePlayerStateManager

   Bases: :py:obj:`haive.games.framework.base.state_manager.GameStateManager`\ [\ :py:obj:`haive.games.base.state.WordConnectionsState`\ ]


   Base state manager for single-player games.

   This class extends the base GameStateManager with single-player specific
   functionality such as hint generation, difficulty scaling, and interactive
   input handling.

   .. method:: initialize

      Initialize a new game state

   .. method:: apply_move

      Apply a move to the game state

   .. method:: generate_hint

      Generate a hint for the current game state

   .. method:: check_game_status

      Check and update the game status

   .. method:: interactive_input

      Process interactive input from the player
      
      


   .. autolink-examples:: SinglePlayerStateManager
      :collapse:

   .. py:method:: apply_move(state: re.T, move: Any) -> re.T
      :classmethod:

      :abstractmethod:


      Apply a move to the game state.

      :param state: Current game state
      :param move: Move to apply

      :returns: Updated game state


      .. autolink-examples:: apply_move
         :collapse:


   .. py:method:: check_game_status(state: re.T) -> re.T
      :classmethod:

      :abstractmethod:


      Check and update the game status.

      :param state: Current game state

      :returns: Updated game state with status checked


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: generate_hint(state: re.T) -> tuple[re.T, str]
      :classmethod:


      Generate a hint for the current game state.

      :param state: Current game state

      :returns: Tuple of (updated state, hint text)


      .. autolink-examples:: generate_hint
         :collapse:


   .. py:method:: get_legal_moves(state: re.T) -> list[Any]
      :classmethod:

      :abstractmethod:


      Get all legal moves for the current state.

      :param state: Current game state

      :returns: List of legal moves


      .. autolink-examples:: get_legal_moves
         :collapse:


   .. py:method:: initialize(difficulty: GameDifficulty = GameDifficulty.MEDIUM, player_type: PlayerType = PlayerType.LLM, **kwargs) -> re.T
      :classmethod:

      :abstractmethod:


      Initialize a new game state.

      :param difficulty: Difficulty level of the game
      :param player_type: Type of player
      :param \*\*kwargs: Additional game-specific initialization parameters

      :returns: A new game state


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: interactive_input(state: re.T, user_input: str) -> re.T
      :classmethod:


      Process interactive input from the player.

      This method handles general commands like 'hint', 'quit', etc.
      Game-specific commands should be handled by overriding this method.

      :param state: Current game state
      :param user_input: User input string

      :returns: Updated game state


      .. autolink-examples:: interactive_input
         :collapse:


