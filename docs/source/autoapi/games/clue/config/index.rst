
:py:mod:`games.clue.config`
===========================

.. py:module:: games.clue.config

Comprehensive configuration system for the Clue (Cluedo) mystery game agent.

This module defines the configuration system for the Clue game agent, providing
complete control over game mechanics, AI behavior, analysis settings, and
visualization options. The configuration system supports both casual and
competitive gameplay modes with extensive customization options.

The configuration manages:
- Game state schema and persistence
- AI engine configurations and behavior
- Analysis and reasoning settings
- Visualization and UI options
- Game flow and turn management
- Solution generation and validation
- Player interaction modes

Key Features:
    - Flexible game parameter configuration
    - Multiple AI difficulty levels
    - Comprehensive analysis and logging
    - Customizable visualization options
    - Solution pre-configuration for testing
    - Turn limit and timeout management
    - Player order customization

.. rubric:: Examples

Basic configuration::

    from haive.games.clue.config import ClueConfig

    # Create default configuration
    config = ClueConfig()
    print(f"Game: {config.name} v{config.version}")
    print(f"Max turns: {config.max_turns}")
    print(f"Analysis enabled: {config.enable_analysis}")

Custom configuration::

    from haive.games.clue.models import ClueSolution, ValidSuspect, ValidWeapon, ValidRoom

    # Create custom game configuration
    custom_solution = {
        "suspect": ValidSuspect.COLONEL_MUSTARD.value,
        "weapon": ValidWeapon.KNIFE.value,
        "room": ValidRoom.KITCHEN.value
    }

    config = ClueConfig(
        max_turns=15,
        first_player="player2",
        solution=custom_solution,
        enable_analysis=False,
        visualize=False
    )

Configuration validation::

    config = ClueConfig()

    # Validate configuration
    assert config.max_turns > 0
    assert config.first_player in ["player1", "player2"]
    assert config.state_schema == ClueState
    assert isinstance(config.enable_analysis, bool)

The configuration system integrates seamlessly with the game engine and provides
all necessary parameters for consistent and customizable gameplay experiences.


.. autolink-examples:: games.clue.config
   :collapse:

Classes
-------

.. autoapisummary::

   games.clue.config.ClueConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ClueConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ClueConfig {
        node [shape=record];
        "ClueConfig" [label="ClueConfig"];
        "haive.games.framework.base.config.GameConfig" -> "ClueConfig";
      }

.. autoclass:: games.clue.config.ClueConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.clue.config
   :collapse:
   
.. autolink-skip:: next
