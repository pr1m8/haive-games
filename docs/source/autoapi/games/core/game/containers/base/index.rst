
:py:mod:`games.core.game.containers.base`
=========================================

.. py:module:: games.core.game.containers.base

Container models for game pieces in the game framework.

This module defines containers for game pieces like decks of cards, bags of tiles, and
player hands.


.. autolink-examples:: games.core.game.containers.base
   :collapse:

Classes
-------

.. autoapisummary::

   games.core.game.containers.base.Deck
   games.core.game.containers.base.GamePieceContainer
   games.core.game.containers.base.PlayerHand


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Deck:

   .. graphviz::
      :align: center

      digraph inheritance_Deck {
        node [shape=record];
        "Deck" [label="Deck"];
        "GamePieceContainer[C]" -> "Deck";
      }

.. autoclass:: games.core.game.containers.base.Deck
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GamePieceContainer:

   .. graphviz::
      :align: center

      digraph inheritance_GamePieceContainer {
        node [shape=record];
        "GamePieceContainer" [label="GamePieceContainer"];
        "pydantic.BaseModel" -> "GamePieceContainer";
        "Generic[T]" -> "GamePieceContainer";
      }

.. autopydantic_model:: games.core.game.containers.base.GamePieceContainer
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

   Inheritance diagram for PlayerHand:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerHand {
        node [shape=record];
        "PlayerHand" [label="PlayerHand"];
        "GamePieceContainer[T]" -> "PlayerHand";
      }

.. autoclass:: games.core.game.containers.base.PlayerHand
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.core.game.containers.base
   :collapse:
   
.. autolink-skip:: next
