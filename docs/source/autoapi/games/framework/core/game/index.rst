
:py:mod:`games.framework.core.game`
===================================

.. py:module:: games.framework.core.game


Classes
-------

.. autoapisummary::

   games.framework.core.game.Game
   games.framework.core.game.GameStatus
   games.framework.core.game.Player


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Game:

   .. graphviz::
      :align: center

      digraph inheritance_Game {
        node [shape=record];
        "Game" [label="Game"];
        "pydantic.BaseModel" -> "Game";
        "Generic[S, M]" -> "Game";
      }

.. autopydantic_model:: games.framework.core.game.Game
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

   Inheritance diagram for GameStatus:

   .. graphviz::
      :align: center

      digraph inheritance_GameStatus {
        node [shape=record];
        "GameStatus" [label="GameStatus"];
        "str" -> "GameStatus";
        "enum.Enum" -> "GameStatus";
      }

.. autoclass:: games.framework.core.game.GameStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GameStatus** is an Enum defined in ``games.framework.core.game``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Player:

   .. graphviz::
      :align: center

      digraph inheritance_Player {
        node [shape=record];
        "Player" [label="Player"];
        "pydantic.BaseModel" -> "Player";
      }

.. autopydantic_model:: games.framework.core.game.Player
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

.. autolink-examples:: games.framework.core.game
   :collapse:
   
.. autolink-skip:: next
