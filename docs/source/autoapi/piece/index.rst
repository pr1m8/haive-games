piece
=====

.. py:module:: piece


Classes
-------

.. autoapisummary::

   piece.CrosswordLetter


Module Contents
---------------

.. py:class:: CrosswordLetter

   Bases: :py:obj:`haive.games.core.piece.base.GamePiece`\ [\ :py:obj:`haive.games.core.position.base.GridPosition`\ ]


   A letter in a crossword puzzle.


   .. autolink-examples:: CrosswordLetter
      :collapse:

   .. py:method:: can_move_to(position: haive.games.core.position.base.GridPosition, board: haive.games.single_player.crossword_puzzle.game.board.CrosswordBoard) -> bool

      Check if this letter can be placed at this position.


      .. autolink-examples:: can_move_to
         :collapse:


   .. py:method:: validate_letter(v: str) -> str
      :classmethod:


      Ensure letter is a single uppercase character.


      .. autolink-examples:: validate_letter
         :collapse:


   .. py:attribute:: is_filled
      :type:  bool
      :value: False



   .. py:attribute:: letter
      :type:  str


