
:py:mod:`games.core.game.core_space`
====================================

.. py:module:: games.core.game.core_space

Space models for the game framework.

This module defines the base Space class and specific implementations for different
types of board spaces.


.. autolink-examples:: games.core.game.core_space
   :collapse:

Classes
-------

.. autoapisummary::

   games.core.game.core_space.GridSpace
   games.core.game.core_space.HexSpace
   games.core.game.core_space.Space
   games.core.game.core_space.SpaceProtocol


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GridSpace:

   .. graphviz::
      :align: center

      digraph inheritance_GridSpace {
        node [shape=record];
        "GridSpace" [label="GridSpace"];
        "Space[P, T]" -> "GridSpace";
      }

.. autoclass:: games.core.game.core_space.GridSpace
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HexSpace:

   .. graphviz::
      :align: center

      digraph inheritance_HexSpace {
        node [shape=record];
        "HexSpace" [label="HexSpace"];
        "Space[P, T]" -> "HexSpace";
      }

.. autoclass:: games.core.game.core_space.HexSpace
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Space:

   .. graphviz::
      :align: center

      digraph inheritance_Space {
        node [shape=record];
        "Space" [label="Space"];
        "pydantic.BaseModel" -> "Space";
        "Generic[P, T]" -> "Space";
      }

.. autopydantic_model:: games.core.game.core_space.Space
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

   Inheritance diagram for SpaceProtocol:

   .. graphviz::
      :align: center

      digraph inheritance_SpaceProtocol {
        node [shape=record];
        "SpaceProtocol" [label="SpaceProtocol"];
        "Protocol" -> "SpaceProtocol";
        "Generic[P, T]" -> "SpaceProtocol";
      }

.. autoclass:: games.core.game.core_space.SpaceProtocol
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.core.game.core_space
   :collapse:
   
.. autolink-skip:: next
