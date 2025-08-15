games.mancala.state
===================

.. py:module:: games.mancala.state

.. autoapi-nested-parse::

   State for the Mancala game.

   This module defines the state for the Mancala game, which includes the board, turn, game
   status, move history, free turn, winner, and player analyses.


   .. autolink-examples:: games.mancala.state
      :collapse:


Attributes
----------

.. autoapisummary::

   games.mancala.state.logger


Classes
-------

.. autoapisummary::

   games.mancala.state.MancalaState


Functions
---------

.. autoapisummary::

   games.mancala.state.extract_analysis_from_message


Module Contents
---------------

.. py:class:: MancalaState

   Bases: :py:obj:`haive.games.framework.base.state.GameState`


   State for a Mancala game.

   This class defines the structure of the Mancala game state,
   which includes the board, turn, game status, move history,
   free turn, winner, and player analyses.

   .. attribute:: board

      List of 14 integers representing the game board.

   .. attribute:: turn

      The current player's turn.

   .. attribute:: game_status

      The status of the game.

   .. attribute:: move_history

      List of moves made in the game.

   .. attribute:: free_turn

      Whether the current player gets a free turn.

   .. attribute:: winner

      The winner of the game, if any.

   .. attribute:: player1_analysis

      Analysis data for player 1.

   .. attribute:: player2_analysis

      Analysis data for player 2.


   .. autolink-examples:: MancalaState
      :collapse:

   .. py:method:: _convert_analysis_list(analyses: list[Any], player: str) -> list[dict[str, Any]]
      :classmethod:


      Convert a list of analysis objects to proper format.

      :param analyses: List of analysis objects to convert.
      :param player: Player name for logging.

      :returns: List of converted analysis dictionaries.


      .. autolink-examples:: _convert_analysis_list
         :collapse:


   .. py:method:: _create_initial_board(stones_per_pit: int) -> list[int]
      :classmethod:


      Create the initial board configuration.

      :param stones_per_pit: Number of stones per pit.

      :returns: Initial board configuration.


      .. autolink-examples:: _create_initial_board
         :collapse:


   .. py:method:: determine_winner() -> Literal['player1', 'player2', 'draw']

      Determine the winner of the game.

      :returns: The winner of the game or 'draw' if tied.


      .. autolink-examples:: determine_winner
         :collapse:


   .. py:method:: display_board() -> str

      Display the board in a human-readable format.

      :returns: A string representation of the current board state.


      .. autolink-examples:: display_board
         :collapse:


   .. py:method:: get_scores() -> dict[str, int]

      Get the current scores for both players.

      :returns: Dictionary with player1 and player2 scores.


      .. autolink-examples:: get_scores
         :collapse:


   .. py:method:: get_valid_moves(player: Literal['player1', 'player2']) -> list[int]

      Get valid moves for the specified player.

      :param player: The player to get valid moves for.

      :returns: List of valid pit indices the player can choose from.


      .. autolink-examples:: get_valid_moves
         :collapse:


   .. py:method:: handle_analysis_data(data: Any) -> Any
      :classmethod:


      Handle conversion of analysis data to proper types.


      .. autolink-examples:: handle_analysis_data
         :collapse:


   .. py:method:: handle_initialization_data(data: Any) -> Any
      :classmethod:


      Handle special initialization patterns from the framework.


      .. autolink-examples:: handle_initialization_data
         :collapse:


   .. py:method:: initialize(**kwargs) -> MancalaState
      :classmethod:


      Initialize the Mancala game state.

      :param \*\*kwargs: Optional parameters including stones_per_pit.

      :returns: A fully initialized Mancala game state.
      :rtype: MancalaState


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: is_game_over() -> bool

      Check if the game is over.

      :returns: True if the game is over, False otherwise.


      .. autolink-examples:: is_game_over
         :collapse:


   .. py:method:: validate_board(v: list[int]) -> list[int]
      :classmethod:


      Validate that the board has exactly 14 positions.

      :param v: The board to validate.

      :returns: The validated board.

      :raises ValueError: If board doesn't have exactly 14 positions.


      .. autolink-examples:: validate_board
         :collapse:


   .. py:attribute:: board
      :type:  list[int]
      :value: None



   .. py:attribute:: free_turn
      :type:  bool
      :value: None



   .. py:attribute:: game_status
      :type:  Literal['ongoing', 'ended']
      :value: None



   .. py:attribute:: move_history
      :type:  list[haive.games.mancala.models.MancalaMove]
      :value: None



   .. py:attribute:: player1_analyses
      :type:  list[haive.games.mancala.models.MancalaAnalysis]
      :value: None



   .. py:attribute:: player2_analyses
      :type:  list[haive.games.mancala.models.MancalaAnalysis]
      :value: None



   .. py:attribute:: turn
      :type:  Literal['player1', 'player2']
      :value: None



   .. py:attribute:: winner
      :type:  Literal['player1', 'player2', 'draw', None]
      :value: None



.. py:function:: extract_analysis_from_message(analysis: Any) -> dict[str, Any] | None

   Extract analysis data from an AIMessage object.

   :param analysis: The analysis object to extract from.

   :returns: Extracted analysis data or None if extraction fails.


   .. autolink-examples:: extract_analysis_from_message
      :collapse:

.. py:data:: logger

