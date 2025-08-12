
:py:mod:`games.framework.core.turn`
===================================

.. py:module:: games.framework.core.turn


Classes
-------

.. autoapisummary::

   games.framework.core.turn.Turn
   games.framework.core.turn.TurnPhase


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Turn:

   .. graphviz::
      :align: center

      digraph inheritance_Turn {
        node [shape=record];
        "Turn" [label="Turn"];
        "pydantic.BaseModel" -> "Turn";
        "Generic[M]" -> "Turn";
      }

.. autopydantic_model:: games.framework.core.turn.Turn
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

   Inheritance diagram for TurnPhase:

   .. graphviz::
      :align: center

      digraph inheritance_TurnPhase {
        node [shape=record];
        "TurnPhase" [label="TurnPhase"];
        "str" -> "TurnPhase";
        "enum.Enum" -> "TurnPhase";
      }

.. autoclass:: games.framework.core.turn.TurnPhase
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TurnPhase** is an Enum defined in ``games.framework.core.turn``.





.. rubric:: Related Links

.. autolink-examples:: games.framework.core.turn
   :collapse:
   
.. autolink-skip:: next
