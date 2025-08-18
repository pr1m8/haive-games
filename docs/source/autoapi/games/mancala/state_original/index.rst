games.mancala.state_original
============================

.. py:module:: games.mancala.state_original

State for the Mancala game.

This module defines the state for the Mancala game, which includes the board, turn, game
status, move history, free turn, winner, and player analyses.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   State for the Mancala game.

   This module defines the state for the Mancala game, which includes the board, turn, game
   status, move history, free turn, winner, and player analyses.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.mancala.state_original.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.mancala.state_original.MancalaState

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MancalaState(/, **data: Any)

            Bases: :py:obj:`haive.games.framework.base.state.GameState`


            State for a Mancala game.

            This class defines the structure of the Mancala game state, which includes the
            board, turn, game status, move history, free turn, winner, and player analyses.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __repr__() -> str

               Detailed representation of the state.



            .. py:method:: __str__() -> str

               String representation of the state.



            .. py:method:: copy() -> MancalaState

               Create a deep copy of the current state.

               :returns: A new instance with the same values
               :rtype: MancalaState



            .. py:method:: get_valid_moves(player: str | None = None) -> list[int]

               Get valid moves for the current or specified player.

               :param player: Player to get moves for ("player1" or "player2").
                              If None, uses current turn.

               :returns: List of valid pit indices that can be played
               :rtype: List[int]



            .. py:method:: get_winner() -> str | None

               Determine the winner of the game.

               :returns: "player1", "player2", "draw", or None if game ongoing
               :rtype: Optional[str]



            .. py:method:: handle_analysis_data(data)
               :classmethod:


               Handle conversion of analysis data to proper types.



            .. py:method:: handle_initialization_data(data)
               :classmethod:


               Handle special initialization patterns from the framework.



            .. py:method:: initialize(stones_per_pit: int = 4, **kwargs) -> MancalaState
               :classmethod:


               Initialize a new Mancala game state.

               :param stones_per_pit: Number of stones to place in each pit initially
               :param \*\*kwargs: Additional keyword arguments for customization

               :returns: A new initialized game state
               :rtype: MancalaState



            .. py:method:: is_game_over() -> bool

               Check if the game is over.

               :returns: True if game is over, False otherwise
               :rtype: bool



            .. py:method:: model_dump(**kwargs) -> dict[str, Any]

               Override model_dump to ensure proper serialization.



            .. py:method:: validate_board(v)
               :classmethod:


               Validate the board has exactly 14 positions.



            .. py:attribute:: board
               :type:  list[int]
               :value: None



            .. py:property:: board_string
               :type: str


               Get a string representation of the board.


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


            .. py:attribute:: player2_analysis
               :type:  list[haive.games.mancala.models.MancalaAnalysis]
               :value: None



            .. py:property:: player2_score
               :type: int


               Get player 2's score (store).


            .. py:attribute:: turn
               :type:  Literal['player1', 'player2']
               :value: None



            .. py:attribute:: winner
               :type:  str | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.mancala.state_original import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

