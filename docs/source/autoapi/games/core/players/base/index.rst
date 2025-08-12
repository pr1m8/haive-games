
:py:mod:`games.core.players.base`
=================================

.. py:module:: games.core.players.base


Classes
-------

.. autoapisummary::

   games.core.players.base.AIPlayer
   games.core.players.base.HumanPlayer
   games.core.players.base.Player
   games.core.players.base.PlayerTypes


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
      }

.. autoclass:: games.core.players.base.AIPlayer
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

.. autoclass:: games.core.players.base.HumanPlayer
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
      }

.. autopydantic_model:: games.core.players.base.Player
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

   Inheritance diagram for PlayerTypes:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerTypes {
        node [shape=record];
        "PlayerTypes" [label="PlayerTypes"];
        "str" -> "PlayerTypes";
        "enum.Enum" -> "PlayerTypes";
      }

.. autoclass:: games.core.players.base.PlayerTypes
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PlayerTypes** is an Enum defined in ``games.core.players.base``.





.. rubric:: Related Links

.. autolink-examples:: games.core.players.base
   :collapse:
   
.. autolink-skip:: next
