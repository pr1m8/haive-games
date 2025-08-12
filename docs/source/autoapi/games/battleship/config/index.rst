
:py:mod:`games.battleship.config`
=================================

.. py:module:: games.battleship.config

Battleship game agent configuration.

This module defines comprehensive configuration classes for Battleship game agents,
providing extensive customization options for game rules, AI behavior, UI preferences,
and performance settings.

The configuration system supports:
    - Board size and ship placement customization
    - Multiple difficulty levels and AI strategies
    - Turn time limits and timeout handling
    - Analysis and logging capabilities
    - UI themes and display preferences
    - Performance optimization settings

Classes:
    BattleshipAgentConfig: Main configuration class for Battleship agents
    ShipConfiguration: Configuration for ship types and placement rules
    GameRuleConfiguration: Game rule and validation settings
    UIConfiguration: User interface and display settings
    PerformanceConfiguration: Performance and optimization settings

.. rubric:: Example

Creating a basic Battleship agent configuration:

    config = BattleshipAgentConfig(
        player_name="Admiral Hayes",
        difficulty="intermediate",
        board_size=10,
        enable_analysis=True,
        turn_timeout=30.0,
    )

    agent = BattleshipAgent(config)

.. note::

   All configuration classes include comprehensive validation to ensure
   game rule consistency and prevent invalid combinations that would
   break gameplay mechanics.


.. autolink-examples:: games.battleship.config
   :collapse:

Classes
-------

.. autoapisummary::

   games.battleship.config.BattleshipAgentConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BattleshipAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_BattleshipAgentConfig {
        node [shape=record];
        "BattleshipAgentConfig" [label="BattleshipAgentConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "BattleshipAgentConfig";
      }

.. autoclass:: games.battleship.config.BattleshipAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.battleship.config
   :collapse:
   
.. autolink-skip:: next
