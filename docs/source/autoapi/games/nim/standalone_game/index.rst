
:py:mod:`games.nim.standalone_game`
===================================

.. py:module:: games.nim.standalone_game

Standalone game implementation of Nim.

This script allows playing Nim without requiring the full Haive framework.


.. autolink-examples:: games.nim.standalone_game
   :collapse:

Classes
-------

.. autoapisummary::

   games.nim.standalone_game.NimGameManager
   games.nim.standalone_game.NimMove
   games.nim.standalone_game.NimState
   games.nim.standalone_game.NimUI


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for NimGameManager:

   .. graphviz::
      :align: center

      digraph inheritance_NimGameManager {
        node [shape=record];
        "NimGameManager" [label="NimGameManager"];
      }

.. autoclass:: games.nim.standalone_game.NimGameManager
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for NimMove:

   .. graphviz::
      :align: center

      digraph inheritance_NimMove {
        node [shape=record];
        "NimMove" [label="NimMove"];
        "pydantic.BaseModel" -> "NimMove";
      }

.. autopydantic_model:: games.nim.standalone_game.NimMove
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

   Inheritance diagram for NimState:

   .. graphviz::
      :align: center

      digraph inheritance_NimState {
        node [shape=record];
        "NimState" [label="NimState"];
        "pydantic.BaseModel" -> "NimState";
      }

.. autopydantic_model:: games.nim.standalone_game.NimState
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

   Inheritance diagram for NimUI:

   .. graphviz::
      :align: center

      digraph inheritance_NimUI {
        node [shape=record];
        "NimUI" [label="NimUI"];
      }

.. autoclass:: games.nim.standalone_game.NimUI
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.nim.standalone_game.main
   games.nim.standalone_game.parse_args

.. py:function:: main()

   Run the Nim game.


   .. autolink-examples:: main
      :collapse:

.. py:function:: parse_args()

   Parse command line arguments.


   .. autolink-examples:: parse_args
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.nim.standalone_game
   :collapse:
   
.. autolink-skip:: next
