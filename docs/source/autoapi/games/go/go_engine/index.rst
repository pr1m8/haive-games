games.go.go_engine
==================

.. py:module:: games.go.go_engine

.. autoapi-nested-parse::

   Simple Go engine wrapper using sgfmill instead of sente.

   This module provides a compatibility layer to replace sente with sgfmill, which is
   compatible with Python 3.12.


   .. autolink-examples:: games.go.go_engine
      :collapse:


Attributes
----------

.. autoapisummary::

   games.go.go_engine.BLACK
   games.go.go_engine.SGFMILL_AVAILABLE
   games.go.go_engine.WHITE
   games.go.go_engine.logger


Classes
-------

.. autoapisummary::

   games.go.go_engine.GoGame
   games.go.go_engine.sgf


Functions
---------

.. autoapisummary::

   games.go.go_engine.Game
   games.go.go_engine.dumps_sgf
   games.go.go_engine.loads_sgf


Module Contents
---------------

.. py:class:: GoGame(board_size: int = 19)

   Simple Go game wrapper using sgfmill.


   .. autolink-examples:: GoGame
      :collapse:

   .. py:method:: play_move(color: str, move: tuple[int, int] | None)

      Play a move on the board.

      :param color: 'b' for black, 'w' for white
      :param move: (row, col) tuple or None for pass


      .. autolink-examples:: play_move
         :collapse:


   .. py:method:: to_sgf() -> str

      Convert game to SGF format.


      .. autolink-examples:: to_sgf
         :collapse:


   .. py:method:: turn() -> str

      Get current player to move.


      .. autolink-examples:: turn
         :collapse:


   .. py:attribute:: board


   .. py:attribute:: board_size
      :value: 19



   .. py:attribute:: captured


   .. py:attribute:: current_player
      :value: 'b'



   .. py:attribute:: move_history
      :value: []



   .. py:attribute:: passes
      :value: 0



.. py:class:: sgf

   SGF compatibility wrapper.


   .. autolink-examples:: sgf
      :collapse:

   .. py:method:: dumps(game)
      :staticmethod:


      Save game to SGF.


      .. autolink-examples:: dumps
         :collapse:


   .. py:method:: loads(sgf_string: str)
      :staticmethod:


      Load game from SGF.


      .. autolink-examples:: loads
         :collapse:


.. py:function:: Game(board_size: int = 19) -> GoGame

   Create a new Go game.


   .. autolink-examples:: Game
      :collapse:

.. py:function:: dumps_sgf(game: GoGame) -> str

   Convert game to SGF string.


   .. autolink-examples:: dumps_sgf
      :collapse:

.. py:function:: loads_sgf(sgf_string: str) -> GoGame

   Load a game from SGF string.


   .. autolink-examples:: loads_sgf
      :collapse:

.. py:data:: BLACK
   :value: 'b'


.. py:data:: SGFMILL_AVAILABLE
   :value: True


.. py:data:: WHITE
   :value: 'w'


.. py:data:: logger

