
:py:mod:`games.framework.multi_player.config`
=============================================

.. py:module:: games.framework.multi_player.config

Configuration for multi-player game agents.

This module provides the configuration class for multi-player game agents,
supporting features like:
    - Role-based player configurations
    - LLM engine configurations per role
    - Game state schema definitions
    - Visualization settings
    - Game flow control

.. rubric:: Example

>>> from haive.agents.agent_games.framework.multi_player.config import MultiPlayerGameConfig
>>> from haive.core.engine.aug_llm import AugLLMConfig
>>>
>>> # Create a game configuration
>>> config = MultiPlayerGameConfig(
...     state_schema=MyGameState,
...     engines={
...         "player": {"move": player_llm_config},
...         "narrator": {"narrate": narrator_llm_config}
...     }
... )


.. autolink-examples:: games.framework.multi_player.config
   :collapse:

Classes
-------

.. autoapisummary::

   games.framework.multi_player.config.MultiPlayerGameConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiPlayerGameConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MultiPlayerGameConfig {
        node [shape=record];
        "MultiPlayerGameConfig" [label="MultiPlayerGameConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "MultiPlayerGameConfig";
      }

.. autoclass:: games.framework.multi_player.config.MultiPlayerGameConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.framework.multi_player.config
   :collapse:
   
.. autolink-skip:: next
