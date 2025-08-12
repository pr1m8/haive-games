
:py:mod:`games.core.game.core_board`
====================================

.. py:module:: games.core.game.core_board

Board models for the game framework.

This module defines the base Board class and specific implementations for different
types of game boards.


.. autolink-examples:: games.core.game.core_board
   :collapse:

Classes
-------

.. autoapisummary::

   games.core.game.core_board.Board
   games.core.game.core_board.GridBoard


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Board:

   .. graphviz::
      :align: center

      digraph inheritance_Board {
        node [shape=record];
        "Board" [label="Board"];
        "pydantic.BaseModel" -> "Board";
        "Generic[S, P, T]" -> "Board";
      }

.. autopydantic_model:: games.core.game.core_board.Board
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GridBoard:

   .. graphviz::
      :align: center

      digraph inheritance_GridBoard {
        node [shape=record];
        "GridBoard" [label="GridBoard"];
        "Board[haive.games.core.game.core.space.GridSpace[P, T], P, T]" -> "GridBoard";
      }

.. autoclass:: games.core.game.core_board.GridBoard
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.core.game.core_board
   :collapse:
   
.. autolink-skip:: next
