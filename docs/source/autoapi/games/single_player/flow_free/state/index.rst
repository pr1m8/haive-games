
:py:mod:`games.single_player.flow_free.state`
=============================================

.. py:module:: games.single_player.flow_free.state

State model for Flow Free game.

This module defines the game state for Flow Free, tracking the board, flows, and game
progress.


.. autolink-examples:: games.single_player.flow_free.state
   :collapse:

Classes
-------

.. autoapisummary::

   games.single_player.flow_free.state.Cell
   games.single_player.flow_free.state.Flow
   games.single_player.flow_free.state.FlowEndpoint
   games.single_player.flow_free.state.FlowFreeState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Cell:

   .. graphviz::
      :align: center

      digraph inheritance_Cell {
        node [shape=record];
        "Cell" [label="Cell"];
        "pydantic.BaseModel" -> "Cell";
      }

.. autopydantic_model:: games.single_player.flow_free.state.Cell
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

   Inheritance diagram for Flow:

   .. graphviz::
      :align: center

      digraph inheritance_Flow {
        node [shape=record];
        "Flow" [label="Flow"];
        "pydantic.BaseModel" -> "Flow";
      }

.. autopydantic_model:: games.single_player.flow_free.state.Flow
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

   Inheritance diagram for FlowEndpoint:

   .. graphviz::
      :align: center

      digraph inheritance_FlowEndpoint {
        node [shape=record];
        "FlowEndpoint" [label="FlowEndpoint"];
        "pydantic.BaseModel" -> "FlowEndpoint";
      }

.. autopydantic_model:: games.single_player.flow_free.state.FlowEndpoint
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

   Inheritance diagram for FlowFreeState:

   .. graphviz::
      :align: center

      digraph inheritance_FlowFreeState {
        node [shape=record];
        "FlowFreeState" [label="FlowFreeState"];
        "haive.games.single_player.base.SinglePlayerGameState" -> "FlowFreeState";
      }

.. autoclass:: games.single_player.flow_free.state.FlowFreeState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.single_player.flow_free.state
   :collapse:
   
.. autolink-skip:: next
