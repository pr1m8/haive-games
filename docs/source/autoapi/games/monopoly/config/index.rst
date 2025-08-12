
:py:mod:`games.monopoly.config`
===============================

.. py:module:: games.monopoly.config


Classes
-------

.. autoapisummary::

   games.monopoly.config.GameDifficulty
   games.monopoly.config.GameVariant
   games.monopoly.config.MonopolyGameAgentConfig
   games.monopoly.config.MonopolyPlayerAgentConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameDifficulty:

   .. graphviz::
      :align: center

      digraph inheritance_GameDifficulty {
        node [shape=record];
        "GameDifficulty" [label="GameDifficulty"];
        "str" -> "GameDifficulty";
        "enum.Enum" -> "GameDifficulty";
      }

.. autoclass:: games.monopoly.config.GameDifficulty
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GameDifficulty** is an Enum defined in ``games.monopoly.config``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameVariant:

   .. graphviz::
      :align: center

      digraph inheritance_GameVariant {
        node [shape=record];
        "GameVariant" [label="GameVariant"];
        "str" -> "GameVariant";
        "enum.Enum" -> "GameVariant";
      }

.. autoclass:: games.monopoly.config.GameVariant
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GameVariant** is an Enum defined in ``games.monopoly.config``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MonopolyGameAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MonopolyGameAgentConfig {
        node [shape=record];
        "MonopolyGameAgentConfig" [label="MonopolyGameAgentConfig"];
        "haive.core.engine.agent.config.AgentConfig" -> "MonopolyGameAgentConfig";
      }

.. autoclass:: games.monopoly.config.MonopolyGameAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MonopolyPlayerAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MonopolyPlayerAgentConfig {
        node [shape=record];
        "MonopolyPlayerAgentConfig" [label="MonopolyPlayerAgentConfig"];
        "haive.core.engine.agent.config.AgentConfig" -> "MonopolyPlayerAgentConfig";
      }

.. autoclass:: games.monopoly.config.MonopolyPlayerAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.monopoly.config
   :collapse:
   
.. autolink-skip:: next
