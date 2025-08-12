
:py:mod:`games.risk.config`
===========================

.. py:module:: games.risk.config

Comprehensive configuration system for Risk game variants and customization.

This module provides extensive configuration options for the Risk board game,
supporting classic rules, modern variants, tournament settings, and custom
rule modifications. The configuration system enables fine-tuned control over
game mechanics, victory conditions, combat rules, and strategic elements.

The configuration classes use Pydantic for validation and provide factory
methods for popular Risk variants including classic Risk, Risk 2210 A.D.,
Risk: Legacy, and tournament configurations.

.. rubric:: Examples

Creating a classic Risk configuration::

    config = RiskConfig.classic()
    game = RiskGame(config)

Creating a modern Risk configuration::

    config = RiskConfig.modern()
    config.player_count = 4
    config.time_limit_per_turn = 300  # 5 minutes
    game = RiskGame(config)

Creating a custom tournament configuration::

    config = RiskConfig.tournament()
    config.max_game_duration = 7200  # 2 hours
    config.sudden_death_enabled = True
    game = RiskGame(config)

Creating a fast-paced variant::

    config = RiskConfig(
        player_count=4,
        escalating_card_values=True,
        fast_reinforcement=True,
        time_limit_per_turn=60,
        blitz_mode=True,
        initial_armies_multiplier=1.5
    )

Custom map configuration::

    config = RiskConfig.modern()
    config.custom_territories = {
        "North America": ["Alaska", "Northwest Territory", "Greenland"],
        "Europe": ["Iceland", "Great Britain", "Northern Europe"]
    }
    config.custom_continent_bonuses = {
        "North America": 5,
        "Europe": 5
    }

.. note::

   All configuration classes include comprehensive validation to ensure
   game rule consistency and prevent invalid combinations that would
   break gameplay mechanics.


.. autolink-examples:: games.risk.config
   :collapse:

Classes
-------

.. autoapisummary::

   games.risk.config.RiskConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RiskConfig:

   .. graphviz::
      :align: center

      digraph inheritance_RiskConfig {
        node [shape=record];
        "RiskConfig" [label="RiskConfig"];
        "pydantic.BaseModel" -> "RiskConfig";
      }

.. autopydantic_model:: games.risk.config.RiskConfig
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

.. autolink-examples:: games.risk.config
   :collapse:
   
.. autolink-skip:: next
