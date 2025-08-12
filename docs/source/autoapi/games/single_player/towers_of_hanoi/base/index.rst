
:py:mod:`games.single_player.towers_of_hanoi.base`
==================================================

.. py:module:: games.single_player.towers_of_hanoi.base


Classes
-------

.. autoapisummary::

   games.single_player.towers_of_hanoi.base.Disk
   games.single_player.towers_of_hanoi.base.Game
   games.single_player.towers_of_hanoi.base.GameStatus
   games.single_player.towers_of_hanoi.base.HanoiBoard
   games.single_player.towers_of_hanoi.base.HanoiGame
   games.single_player.towers_of_hanoi.base.HanoiMove
   games.single_player.towers_of_hanoi.base.HanoiSolver
   games.single_player.towers_of_hanoi.base.Peg
   games.single_player.towers_of_hanoi.base.PegPosition
   games.single_player.towers_of_hanoi.base.PegSpace


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Disk:

   .. graphviz::
      :align: center

      digraph inheritance_Disk {
        node [shape=record];
        "Disk" [label="Disk"];
        "haive.games.framework.core.piece.GamePiece[PegPosition]" -> "Disk";
      }

.. autoclass:: games.single_player.towers_of_hanoi.base.Disk
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Game:

   .. graphviz::
      :align: center

      digraph inheritance_Game {
        node [shape=record];
        "Game" [label="Game"];
        "pydantic.BaseModel" -> "Game";
        "Generic[P, re.T]" -> "Game";
      }

.. autopydantic_model:: games.single_player.towers_of_hanoi.base.Game
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

.. autoclass:: games.single_player.towers_of_hanoi.base.GameStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GameStatus** is an Enum defined in ``games.single_player.towers_of_hanoi.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HanoiBoard:

   .. graphviz::
      :align: center

      digraph inheritance_HanoiBoard {
        node [shape=record];
        "HanoiBoard" [label="HanoiBoard"];
        "haive.games.framework.core.board.Board[PegSpace[Disk], PegPosition, Disk]" -> "HanoiBoard";
      }

.. autoclass:: games.single_player.towers_of_hanoi.base.HanoiBoard
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HanoiGame:

   .. graphviz::
      :align: center

      digraph inheritance_HanoiGame {
        node [shape=record];
        "HanoiGame" [label="HanoiGame"];
        "Game[PegPosition, Disk]" -> "HanoiGame";
      }

.. autoclass:: games.single_player.towers_of_hanoi.base.HanoiGame
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HanoiMove:

   .. graphviz::
      :align: center

      digraph inheritance_HanoiMove {
        node [shape=record];
        "HanoiMove" [label="HanoiMove"];
        "pydantic.BaseModel" -> "HanoiMove";
      }

.. autopydantic_model:: games.single_player.towers_of_hanoi.base.HanoiMove
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

   Inheritance diagram for HanoiSolver:

   .. graphviz::
      :align: center

      digraph inheritance_HanoiSolver {
        node [shape=record];
        "HanoiSolver" [label="HanoiSolver"];
        "pydantic.BaseModel" -> "HanoiSolver";
      }

.. autopydantic_model:: games.single_player.towers_of_hanoi.base.HanoiSolver
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

   Inheritance diagram for Peg:

   .. graphviz::
      :align: center

      digraph inheritance_Peg {
        node [shape=record];
        "Peg" [label="Peg"];
        "haive.games.framework.core.container.GamePieceContainer[Disk]" -> "Peg";
      }

.. autoclass:: games.single_player.towers_of_hanoi.base.Peg
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PegPosition:

   .. graphviz::
      :align: center

      digraph inheritance_PegPosition {
        node [shape=record];
        "PegPosition" [label="PegPosition"];
        "haive.games.framework.core.position.Position" -> "PegPosition";
      }

.. autoclass:: games.single_player.towers_of_hanoi.base.PegPosition
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PegSpace:

   .. graphviz::
      :align: center

      digraph inheritance_PegSpace {
        node [shape=record];
        "PegSpace" [label="PegSpace"];
        "haive.games.framework.core.space.Space[PegPosition, Disk]" -> "PegSpace";
      }

.. autoclass:: games.single_player.towers_of_hanoi.base.PegSpace
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.single_player.towers_of_hanoi.base
   :collapse:
   
.. autolink-skip:: next
