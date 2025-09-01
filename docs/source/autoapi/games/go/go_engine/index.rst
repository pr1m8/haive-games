games.go.go_engine
==================

.. py:module:: games.go.go_engine

.. autoapi-nested-parse::

   Simple Go engine wrapper using sgfmill instead of sente.

   This module provides a compatibility layer to replace sente with sgfmill, which is
   compatible with Python 3.12.



Attributes
----------

.. autoapisummary::

   games.go.go_engine.BLACK
   games.go.go_engine.SGFMILL_AVAILABLE
   games.go.go_engine.WHITE
   games.go.go_engine.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/go/go_engine/GoGame
   /autoapi/games/go/go_engine/sgf

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

.. py:function:: Game(board_size: int = 19) -> GoGame

   Create a new Go game.


.. py:function:: dumps_sgf(game: GoGame) -> str

   Convert game to SGF string.


.. py:function:: loads_sgf(sgf_string: str) -> GoGame

   Load a game from SGF string.


.. py:data:: BLACK
   :value: 'b'


.. py:data:: SGFMILL_AVAILABLE
   :value: True


.. py:data:: WHITE
   :value: 'w'


.. py:data:: logger

