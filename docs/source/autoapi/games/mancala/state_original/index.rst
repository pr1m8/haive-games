games.mancala.state_original
============================

.. py:module:: games.mancala.state_original

.. autoapi-nested-parse::

   State for the Mancala game.

   This module defines the state for the Mancala game, which includes the board, turn, game
   status, move history, free turn, winner, and player analyses.


   .. autolink-examples:: games.mancala.state_original
      :collapse:


Attributes
----------

.. autoapisummary::

   games.mancala.state_original.logger


Classes
-------

.. autoapisummary::

   games.mancala.state_original.MancalaState


Module Contents
---------------

.. py:class:: MancalaState

   Bases: :py:obj:`haive.games.framework.base.state.GameState`


   State for a Mancala game.

   This class defines the structure of the Mancala game state, which includes the
   board, turn, game status, move history, free turn, winner, and player analyses.



   .. autolink-examples:: MancalaState
      :collapse:

   .. py:method:: __repr__() -> str

      Detailed representation of the state.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: __str__() -> str

      String representation of the state.


      .. autolink-examples:: __str__
         :collapse:


   .. py:method:: copy() -> MancalaState

      Create a deep copy of the current state.

      :returns: A new instance with the same values
      :rtype: MancalaState


      .. autolink-examples:: copy
         :collapse:


   .. py:method:: get_valid_moves(player: str | None = None) -> list[int]

      Get valid moves for the current or specified player.

      :param player: Player to get moves for ("player1" or "player2").
                     If None, uses current turn.

      :returns: List of valid pit indices that can be played
      :rtype: List[int]


      .. autolink-examples:: get_valid_moves
         :collapse:


   .. py:method:: get_winner() -> str | None

      Determine the winner of the game.

      :returns: "player1", "player2", "draw", or None if game ongoing
      :rtype: Optional[str]


      .. autolink-examples:: get_winner
         :collapse:


   .. py:method:: handle_analysis_data(data)
      :classmethod:


      Handle conversion of analysis data to proper types.


      .. autolink-examples:: handle_analysis_data
         :collapse:


   .. py:method:: handle_initialization_data(data)
      :classmethod:


      Handle special initialization patterns from the framework.


      .. autolink-examples:: handle_initialization_data
         :collapse:


   .. py:method:: initialize(stones_per_pit: int = 4, **kwargs) -> MancalaState
      :classmethod:


      Initialize a new Mancala game state.

      :param stones_per_pit: Number of stones to place in each pit initially
      :param \*\*kwargs: Additional keyword arguments for customization

      :returns: A new initialized game state
      :rtype: MancalaState


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: is_game_over() -> bool

      Check if the game is over.

      :returns: True if game is over, False otherwise
      :rtype: bool


      .. autolink-examples:: is_game_over
         :collapse:


   .. py:method:: model_dump(**kwargs) -> dict[str, Any]

      Override model_dump to ensure proper serialization.


      .. autolink-examples:: model_dump
         :collapse:


   .. py:method:: validate_board(v)
      :classmethod:


      Validate the board has exactly 14 positions.


      .. autolink-examples:: validate_board
         :collapse:


   .. py:attribute:: board
      :type:  list[int]
      :value: None



   .. py:property:: board_string
      :type: str


      Get a string representation of the board.

      .. autolink-examples:: board_string
         :collapse:


   .. py:attribute:: free_turn
      :type:  bool
      :value: None



   .. py:attribute:: game_status
      :type:  Literal['ongoing', 'player1_win', 'player2_win', 'draw']
      :value: None



   .. py:attribute:: move_history
      :type:  list[haive.games.mancala.models.MancalaMove]
      :value: None



   .. py:attribute:: player1_analysis
      :type:  list[haive.games.mancala.models.MancalaAnalysis]
      :value: None



   .. py:property:: player1_score
      :type: int


      Get player 1's score (store).

      .. autolink-examples:: player1_score
         :collapse:


   .. py:attribute:: player2_analysis
      :type:  list[haive.games.mancala.models.MancalaAnalysis]
      :value: None



   .. py:property:: player2_score
      :type: int


      Get player 2's score (store).

      .. autolink-examples:: player2_score
         :collapse:


   .. py:attribute:: turn
      :type:  Literal['player1', 'player2']
      :value: None



   .. py:attribute:: winner
      :type:  str | None
      :value: None



.. py:data:: logger

