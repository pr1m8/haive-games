
:py:mod:`games.mafia.config`
============================

.. py:module:: games.mafia.config

Configuration for the Mafia game agent.

This module provides configuration classes and utilities for the Mafia game
agent, including:
    - Game settings (max days, discussion rounds)
    - LLM engine configurations
    - Role mappings and assignments
    - Debug settings

.. rubric:: Example

>>> from mafia.config import MafiaAgentConfig
>>>
>>> # Create a default configuration for 7 players
>>> config = MafiaAgentConfig.default_config(
...     player_count=7,
...     max_days=3
... )
>>> print(config.max_days)  # Shows 3


.. autolink-examples:: games.mafia.config
   :collapse:

Classes
-------

.. autoapisummary::

   games.mafia.config.MafiaAgentConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MafiaAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MafiaAgentConfig {
        node [shape=record];
        "MafiaAgentConfig" [label="MafiaAgentConfig"];
        "haive.games.framework.multi_player.config.MultiPlayerGameConfig" -> "MafiaAgentConfig";
      }

.. autoclass:: games.mafia.config.MafiaAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.mafia.config
   :collapse:
   
.. autolink-skip:: next
