games.clue.controller
=====================

.. py:module:: games.clue.controller

.. autoapi-nested-parse::

   Controller for the Clue game.

   This module provides the game controller that manages the state and flow of the Clue
   game.


   .. autolink-examples:: games.clue.controller
      :collapse:


Classes
-------

.. autoapisummary::

   games.clue.controller.ClueGameController
   games.clue.controller.ClueGameState
   games.clue.controller.CluePlayer


Module Contents
---------------

.. py:class:: ClueGameController(player_names: list[str], max_turns: int = 20)

   Controller for the Clue game.

   Initialize a new Clue game.

   :param player_names: Names of the players
   :param max_turns: Maximum number of turns before the game ends


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ClueGameController
      :collapse:

   .. py:method:: _setup_game() -> ClueGameState

      Set up a new game with shuffled cards and solution.


      .. autolink-examples:: _setup_game
         :collapse:


   .. py:method:: generate_ai_analysis(player_idx: int) -> haive.games.clue.models.ClueHypothesis
      :async:


      Generate an analysis using the player's AI analysis engine.

      :param player_idx: Index of the AI player

      :returns: The generated analysis


      .. autolink-examples:: generate_ai_analysis
         :collapse:


   .. py:method:: generate_ai_guess(player_idx: int) -> haive.games.clue.models.ClueGuess
      :async:


      Generate a guess using the player's AI engine.

      :param player_idx: Index of the AI player

      :returns: The generated guess


      .. autolink-examples:: generate_ai_guess
         :collapse:


   .. py:method:: generate_board_string() -> str

      Generate a string representation of the game board.


      .. autolink-examples:: generate_board_string
         :collapse:


   .. py:method:: get_game_state() -> ClueGameState

      Get the current game state.


      .. autolink-examples:: get_game_state
         :collapse:


   .. py:method:: get_player_view(player_idx: int) -> dict

      Get the game state from a specific player's point of view.

      :param player_idx: Index of the player

      :returns: A dictionary with the game state visible to the player


      .. autolink-examples:: get_player_view
         :collapse:


   .. py:method:: make_guess(player_idx: int, guess: haive.games.clue.models.ClueGuess) -> haive.games.clue.models.ClueResponse

      Process a player's guess and return the response.

      :param player_idx: Index of the player making the guess
      :param guess: The guess made by the player

      :returns: A response indicating whether the guess was correct or which player refuted it


      .. autolink-examples:: make_guess
         :collapse:


   .. py:attribute:: game_state


   .. py:attribute:: max_turns
      :value: 20



   .. py:attribute:: player_names


.. py:class:: ClueGameState

   Represents the state of a Clue game.


   .. autolink-examples:: ClueGameState
      :collapse:

   .. py:attribute:: current_player_index
      :type:  int
      :value: 0



   .. py:attribute:: current_turn
      :type:  int
      :value: 1



   .. py:attribute:: guess_history
      :type:  list[tuple[haive.games.clue.models.ClueGuess, haive.games.clue.models.ClueResponse]]
      :value: []



   .. py:attribute:: max_turns
      :type:  int
      :value: 20



   .. py:attribute:: players
      :type:  list[CluePlayer]


   .. py:attribute:: solution
      :type:  haive.games.clue.models.ClueSolution


   .. py:attribute:: status
      :type:  haive.games.clue.models.GameStatus


   .. py:attribute:: winner
      :type:  str | None
      :value: None



.. py:class:: CluePlayer

   Represents a player in the Clue game.


   .. autolink-examples:: CluePlayer
      :collapse:

   .. py:attribute:: analysis_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: cards
      :type:  list[haive.games.clue.models.ClueCard]
      :value: []



   .. py:attribute:: name
      :type:  str


   .. py:attribute:: player_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



