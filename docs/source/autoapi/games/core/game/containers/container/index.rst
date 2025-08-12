
:py:mod:`games.core.game.containers.container`
==============================================

.. py:module:: games.core.game.containers.container


Classes
-------

.. autoapisummary::

   games.core.game.containers.container.Deck
   games.core.game.containers.container.GamePieceContainer
   games.core.game.containers.container.PlayerHand
   games.core.game.containers.container.TileBag


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Deck:

   .. graphviz::
      :align: center

      digraph inheritance_Deck {
        node [shape=record];
        "Deck" [label="Deck"];
        "GamePieceContainer[Card]" -> "Deck";
      }

.. autoclass:: games.core.game.containers.container.Deck
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

.. autopydantic_model:: games.core.game.containers.container.GamePieceContainer
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

.. autoclass:: games.core.game.containers.container.PlayerHand
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TileBag:

   .. graphviz::
      :align: center

      digraph inheritance_TileBag {
        node [shape=record];
        "TileBag" [label="TileBag"];
        "GamePieceContainer[Tile]" -> "TileBag";
      }

.. autoclass:: games.core.game.containers.container.TileBag
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.core.game.containers.container
   :collapse:
   
.. autolink-skip:: next
