
:py:mod:`games.core.agent.game_config`
======================================

.. py:module:: games.core.agent.game_config


Classes
-------

.. autoapisummary::

   games.core.agent.game_config.GameAgentConfig
   games.core.agent.game_config.GamePlayerType
   games.core.agent.game_config.PlayerType


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_GameAgentConfig {
        node [shape=record];
        "GameAgentConfig" [label="GameAgentConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "GameAgentConfig";
        "abc.ABC" -> "GameAgentConfig";
      }

.. autoclass:: games.core.agent.game_config.GameAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GamePlayerType:

   .. graphviz::
      :align: center

      digraph inheritance_GamePlayerType {
        node [shape=record];
        "GamePlayerType" [label="GamePlayerType"];
        "enum.Enum" -> "GamePlayerType";
      }

.. autoclass:: games.core.agent.game_config.GamePlayerType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GamePlayerType** is an Enum defined in ``games.core.agent.game_config``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlayerType:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerType {
        node [shape=record];
        "PlayerType" [label="PlayerType"];
        "str" -> "PlayerType";
        "enum.Enum" -> "PlayerType";
      }

.. autoclass:: games.core.agent.game_config.PlayerType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PlayerType** is an Enum defined in ``games.core.agent.game_config``.





.. rubric:: Related Links

.. autolink-examples:: games.core.agent.game_config
   :collapse:
   
.. autolink-skip:: next
