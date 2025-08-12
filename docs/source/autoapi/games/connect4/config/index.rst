
:py:mod:`games.connect4.config`
===============================

.. py:module:: games.connect4.config

Connect4 agent configuration module.

This module provides configuration classes for the Connect4 game agent, including:
    - Base configuration for Connect4 agents
    - LLM configuration for players and analyzers
    - Game settings and visualization options

.. rubric:: Example

>>> from haive.games.connect4 import Connect4AgentConfig
>>>
>>> # Create a config with analysis enabled
>>> config = Connect4AgentConfig(
...     enable_analysis=True,
...     should_visualize_graph=True,
...     max_moves=42  # Maximum possible moves in Connect4
... )


.. autolink-examples:: games.connect4.config
   :collapse:

Classes
-------

.. autoapisummary::

   games.connect4.config.Connect4AgentConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Connect4AgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_Connect4AgentConfig {
        node [shape=record];
        "Connect4AgentConfig" [label="Connect4AgentConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "Connect4AgentConfig";
      }

.. autoclass:: games.connect4.config.Connect4AgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.connect4.config
   :collapse:
   
.. autolink-skip:: next
