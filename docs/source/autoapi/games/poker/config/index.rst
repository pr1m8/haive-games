
:py:mod:`games.poker.config`
============================

.. py:module:: games.poker.config

Configuration module for the Poker agent.

This module provides configuration classes and utilities for setting up
poker game agents, including:
    - Game settings (blinds, starting chips, max hands)
    - Player configurations and names
    - LLM engine configurations
    - State management settings
    - Game history and analysis options

The module supports multiple LLM providers and allows customization of
game parameters through a Pydantic-based configuration system.

.. rubric:: Example

>>> from poker.config import PokerAgentConfig
>>>
>>> # Create default config for 6 players
>>> config = PokerAgentConfig.default_config(
...     player_names=["P1", "P2", "P3", "P4", "P5", "P6"],
...     starting_chips=2000,
...     small_blind=10,
...     big_blind=20
... )


.. autolink-examples:: games.poker.config
   :collapse:

Classes
-------

.. autoapisummary::

   games.poker.config.PokerAgentConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PokerAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_PokerAgentConfig {
        node [shape=record];
        "PokerAgentConfig" [label="PokerAgentConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "PokerAgentConfig";
      }

.. autoclass:: games.poker.config.PokerAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.poker.config
   :collapse:
   
.. autolink-skip:: next
