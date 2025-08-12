
:py:mod:`games.core.components.cards.scoring`
=============================================

.. py:module:: games.core.components.cards.scoring


Classes
-------

.. autoapisummary::

   games.core.components.cards.scoring.HandEvaluator
   games.core.components.cards.scoring.HandRank


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HandEvaluator:

   .. graphviz::
      :align: center

      digraph inheritance_HandEvaluator {
        node [shape=record];
        "HandEvaluator" [label="HandEvaluator"];
        "pydantic.BaseModel" -> "HandEvaluator";
        "Generic[haive.games.core.components.models.TCard]" -> "HandEvaluator";
      }

.. autopydantic_model:: games.core.components.cards.scoring.HandEvaluator
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

   Inheritance diagram for HandRank:

   .. graphviz::
      :align: center

      digraph inheritance_HandRank {
        node [shape=record];
        "HandRank" [label="HandRank"];
        "pydantic.BaseModel" -> "HandRank";
        "Generic[haive.games.core.components.models.TCard]" -> "HandRank";
      }

.. autopydantic_model:: games.core.components.cards.scoring.HandRank
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





.. rubric:: Related Links

.. autolink-examples:: games.core.components.cards.scoring
   :collapse:
   
.. autolink-skip:: next
