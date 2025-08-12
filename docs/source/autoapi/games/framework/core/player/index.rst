
:py:mod:`games.framework.core.player`
=====================================

.. py:module:: games.framework.core.player


Classes
-------

.. autoapisummary::

   games.framework.core.player.AIPlayer
   games.framework.core.player.HumanPlayer
   games.framework.core.player.Player
   games.framework.core.player.RandomAIPlayer
   games.framework.core.player.RuleBasedAIPlayer


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AIPlayer:

   .. graphviz::
      :align: center

      digraph inheritance_AIPlayer {
        node [shape=record];
        "AIPlayer" [label="AIPlayer"];
        "Player" -> "AIPlayer";
        "Generic[S, M]" -> "AIPlayer";
      }

.. autoclass:: games.framework.core.player.AIPlayer
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HumanPlayer:

   .. graphviz::
      :align: center

      digraph inheritance_HumanPlayer {
        node [shape=record];
        "HumanPlayer" [label="HumanPlayer"];
        "Player" -> "HumanPlayer";
      }

.. autoclass:: games.framework.core.player.HumanPlayer
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Player:

   .. graphviz::
      :align: center

      digraph inheritance_Player {
        node [shape=record];
        "Player" [label="Player"];
        "pydantic.BaseModel" -> "Player";
        "abc.ABC" -> "Player";
      }

.. autopydantic_model:: games.framework.core.player.Player
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

   Inheritance diagram for RandomAIPlayer:

   .. graphviz::
      :align: center

      digraph inheritance_RandomAIPlayer {
        node [shape=record];
        "RandomAIPlayer" [label="RandomAIPlayer"];
        "AIPlayer[S, M]" -> "RandomAIPlayer";
      }

.. autoclass:: games.framework.core.player.RandomAIPlayer
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RuleBasedAIPlayer:

   .. graphviz::
      :align: center

      digraph inheritance_RuleBasedAIPlayer {
        node [shape=record];
        "RuleBasedAIPlayer" [label="RuleBasedAIPlayer"];
        "AIPlayer[S, M]" -> "RuleBasedAIPlayer";
      }

.. autoclass:: games.framework.core.player.RuleBasedAIPlayer
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.framework.core.player
   :collapse:
   
.. autolink-skip:: next
