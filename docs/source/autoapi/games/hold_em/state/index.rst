
:py:mod:`games.hold_em.state`
=============================

.. py:module:: games.hold_em.state

Fixed Texas Hold'em game state models.

Key fixes:
1. Added Annotated type for current_player_index to handle concurrent updates
2. Fixed reducer setup for fields that might be updated concurrently
3. Added proper field annotations for LangGraph compatibility


.. autolink-examples:: games.hold_em.state
   :collapse:

Classes
-------

.. autoapisummary::

   games.hold_em.state.GamePhase
   games.hold_em.state.HoldemState
   games.hold_em.state.PlayerAction
   games.hold_em.state.PlayerDecision
   games.hold_em.state.PlayerState
   games.hold_em.state.PlayerStatus
   games.hold_em.state.PokerAction


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GamePhase:

   .. graphviz::
      :align: center

      digraph inheritance_GamePhase {
        node [shape=record];
        "GamePhase" [label="GamePhase"];
        "str" -> "GamePhase";
        "enum.Enum" -> "GamePhase";
      }

.. autoclass:: games.hold_em.state.GamePhase
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GamePhase** is an Enum defined in ``games.hold_em.state``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HoldemState:

   .. graphviz::
      :align: center

      digraph inheritance_HoldemState {
        node [shape=record];
        "HoldemState" [label="HoldemState"];
        "pydantic.BaseModel" -> "HoldemState";
      }

.. autopydantic_model:: games.hold_em.state.HoldemState
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

   Inheritance diagram for PlayerAction:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerAction {
        node [shape=record];
        "PlayerAction" [label="PlayerAction"];
        "pydantic.BaseModel" -> "PlayerAction";
      }

.. autopydantic_model:: games.hold_em.state.PlayerAction
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

   Inheritance diagram for PlayerDecision:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerDecision {
        node [shape=record];
        "PlayerDecision" [label="PlayerDecision"];
        "pydantic.BaseModel" -> "PlayerDecision";
      }

.. autopydantic_model:: games.hold_em.state.PlayerDecision
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

   Inheritance diagram for PlayerState:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerState {
        node [shape=record];
        "PlayerState" [label="PlayerState"];
        "pydantic.BaseModel" -> "PlayerState";
      }

.. autopydantic_model:: games.hold_em.state.PlayerState
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

   Inheritance diagram for PlayerStatus:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerStatus {
        node [shape=record];
        "PlayerStatus" [label="PlayerStatus"];
        "str" -> "PlayerStatus";
        "enum.Enum" -> "PlayerStatus";
      }

.. autoclass:: games.hold_em.state.PlayerStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PlayerStatus** is an Enum defined in ``games.hold_em.state``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PokerAction:

   .. graphviz::
      :align: center

      digraph inheritance_PokerAction {
        node [shape=record];
        "PokerAction" [label="PokerAction"];
        "str" -> "PokerAction";
        "enum.Enum" -> "PokerAction";
      }

.. autoclass:: games.hold_em.state.PokerAction
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PokerAction** is an Enum defined in ``games.hold_em.state``.



Functions
---------

.. autoapisummary::

   games.hold_em.state.last_value_reducer

.. py:function:: last_value_reducer(a: Any, b: Any) -> Any

   Reducer that takes the last value - for fields that should be overwritten.


   .. autolink-examples:: last_value_reducer
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.hold_em.state
   :collapse:
   
.. autolink-skip:: next
