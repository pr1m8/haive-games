
:py:mod:`games.go.go_engine`
============================

.. py:module:: games.go.go_engine

Simple Go engine wrapper using sgfmill instead of sente.

This module provides a compatibility layer to replace sente with sgfmill, which is
compatible with Python 3.12.


.. autolink-examples:: games.go.go_engine
   :collapse:

Classes
-------

.. autoapisummary::

   games.go.go_engine.GoGame
   games.go.go_engine.sgf


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GoGame:

   .. graphviz::
      :align: center

      digraph inheritance_GoGame {
        node [shape=record];
        "GoGame" [label="GoGame"];
      }

.. autoclass:: games.go.go_engine.GoGame
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for sgf:

   .. graphviz::
      :align: center

      digraph inheritance_sgf {
        node [shape=record];
        "sgf" [label="sgf"];
      }

.. autoclass:: games.go.go_engine.sgf
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.go.go_engine.Game
   games.go.go_engine.dumps_sgf
   games.go.go_engine.loads_sgf

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



.. rubric:: Related Links

.. autolink-examples:: games.go.go_engine
   :collapse:
   
.. autolink-skip:: next
