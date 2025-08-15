games.mastermind.state_manager
==============================

.. py:module:: games.mastermind.state_manager

.. autoapi-nested-parse::

   State manager for the Mastermind game.

   This module defines the state manager for the Mastermind game, which manages the state
   of the game and provides methods for initializing, updating, and analyzing the game
   state.


   .. autolink-examples:: games.mastermind.state_manager
      :collapse:


Classes
-------

.. autoapisummary::

   games.mastermind.state_manager.MastermindStateManager


Module Contents
---------------

.. py:class:: MastermindStateManager

   Bases: :py:obj:`haive.games.framework.base.state_manager.GameStateManager`\ [\ :py:obj:`haive.games.mastermind.state.MastermindState`\ ]


   Manager for Mastermind game state.

   This class provides methods for initializing, updating, and analyzing the game
   state.



   .. autolink-examples:: MastermindStateManager
      :collapse:

   .. py:method:: _calculate_feedback(secret_code: list[str], guess: list[str]) -> haive.games.mastermind.models.MastermindFeedback
      :classmethod:


      Calculate feedback for a guess compared to the secret code.

      :param secret_code: The secret code to guess.
      :param guess: The player's guess.

      :returns: Feedback with correct position and color counts.
      :rtype: MastermindFeedback


      .. autolink-examples:: _calculate_feedback
         :collapse:


   .. py:method:: _is_consistent_with_feedback(code: tuple[str, Ellipsis], guess: tuple[str, Ellipsis], feedback: haive.games.mastermind.models.MastermindFeedback) -> bool
      :classmethod:


      Check if a potential code is consistent with a guess and its feedback.

      :param code: Potential secret code.
      :param guess: A previous guess.
      :param feedback: Feedback for the guess.

      :returns: True if the code is consistent with the guess and feedback.
      :rtype: bool


      .. autolink-examples:: _is_consistent_with_feedback
         :collapse:


   .. py:method:: add_analysis(state: haive.games.mastermind.state.MastermindState, player: str, analysis: haive.games.mastermind.models.MastermindAnalysis) -> haive.games.mastermind.state.MastermindState
      :classmethod:


      Add an analysis to the state.

      :param state: The current game state.
      :param player: The player who performed the analysis.
      :param analysis: The analysis to add.

      :returns: Updated state with the analysis added.
      :rtype: MastermindState


      .. autolink-examples:: add_analysis
         :collapse:


   .. py:method:: apply_move(state: haive.games.mastermind.state.MastermindState, move: haive.games.mastermind.models.MastermindGuess) -> haive.games.mastermind.state.MastermindState
      :classmethod:


      Apply a guess to the current state and return the new state.

      :param state: The current game state.
      :param move: The guess to apply.

      :returns: A new game state after applying the guess.
      :rtype: MastermindState

      :raises ValueError: If the move is invalid.


      .. autolink-examples:: apply_move
         :collapse:


   .. py:method:: check_game_status(state: haive.games.mastermind.state.MastermindState) -> haive.games.mastermind.state.MastermindState
      :classmethod:


      Check and update the game status.

      For Mastermind, this is handled in apply_move, so this method just returns the state.

      :param state: The current game state.

      :returns: The game state (unchanged).
      :rtype: MastermindState


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: get_legal_moves(state: haive.games.mastermind.state.MastermindState) -> list[haive.games.mastermind.models.MastermindGuess]
      :classmethod:


      Get all legal moves for the current state.

      For Mastermind, this is impractical to enumerate all possible color combinations,
      so this method returns an empty list. The agent will generate guesses based on analysis.

      :param state: The current game state.

      :returns: An empty list (agent should generate its own guesses).
      :rtype: List[MastermindGuess]


      .. autolink-examples:: get_legal_moves
         :collapse:


   .. py:method:: get_possible_codes(state: haive.games.mastermind.state.MastermindState) -> set[tuple[str, Ellipsis]]
      :classmethod:


      Get all possible secret codes that are consistent with all guesses and.
      feedback so far.

      This is computationally expensive for a full game, so it's limited to use for analysis.

      :param state: The current game state.

      :returns: Set of possible codes as tuples.
      :rtype: Set[Tuple[str, ...]]


      .. autolink-examples:: get_possible_codes
         :collapse:


   .. py:method:: get_winner(state: haive.games.mastermind.state.MastermindState) -> str | None
      :classmethod:


      Get the winner of the game, if any.

      :param state: The current game state.

      :returns: The winner, or None if the game is ongoing.
      :rtype: Optional[str]


      .. autolink-examples:: get_winner
         :collapse:


   .. py:method:: initialize(**kwargs) -> haive.games.mastermind.state.MastermindState
      :classmethod:


      Initialize a new Mastermind game.

      :param \*\*kwargs: Keyword arguments for game initialization.
                         codemaker: Player who creates the code (player1 or player2). Default is player1.
                         colors: List of valid colors. Default is standard 6 colors.
                         code_length: Length of the secret code. Default is 4.
                         max_turns: Maximum number of turns. Default is 10.
                         secret_code: Optional predetermined secret code (List[str] or ColorCode).

      :returns: A new Mastermind game state.
      :rtype: MastermindState


      .. autolink-examples:: initialize
         :collapse:


   .. py:attribute:: VALID_COLORS
      :value: ['red', 'blue', 'green', 'yellow', 'purple', 'orange']



