games.hold_em.config
====================

.. py:module:: games.hold_em.config

.. autoapi-nested-parse::

   Texas Hold'em configuration module.

   This module provides configuration classes for the Hold'em game, including:
       - Game agent configuration
       - Player agent configurations
       - Engine configurations



Attributes
----------

.. autoapisummary::

   games.hold_em.config.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/hold_em/config/HoldemGameSettings

.. autoapisummary::

   games.hold_em.config.HoldemGameSettings


Functions
---------

.. autoapisummary::

   games.hold_em.config.create_cash_game_config
   games.hold_em.config.create_custom_holdem_config
   games.hold_em.config.create_default_holdem_config
   games.hold_em.config.create_fallback_engines
   games.hold_em.config.create_fallback_game_engines
   games.hold_em.config.create_heads_up_config
   games.hold_em.config.create_tournament_config
   games.hold_em.config.validate_config
   games.hold_em.config.validate_player_engines


Module Contents
---------------

.. py:function:: create_cash_game_config(num_players: int = 6, big_blind: int = 20, max_buy_in: int = 2000, min_buy_in: int = 400) -> haive.games.hold_em.game_agent.HoldemGameAgentConfig

   Create a cash game configuration.


.. py:function:: create_custom_holdem_config(settings: HoldemGameSettings) -> haive.games.hold_em.game_agent.HoldemGameAgentConfig

   Create a custom Hold'em configuration from settings.


.. py:function:: create_default_holdem_config(num_players: int = 4, starting_chips: int = 1000, small_blind: int = 10, big_blind: int = 20) -> haive.games.hold_em.game_agent.HoldemGameAgentConfig

   Create a default Hold'em game configuration.


.. py:function:: create_fallback_engines(player_name: str, player_style: str) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create minimal fallback engines if the main engine creation fails.


.. py:function:: create_fallback_game_engines() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create minimal fallback game engines.


.. py:function:: create_heads_up_config(player1_name: str = 'Alice', player2_name: str = 'Bob', starting_chips: int = 1000, big_blind: int = 20) -> haive.games.hold_em.game_agent.HoldemGameAgentConfig

   Create a heads-up (2 player) configuration.


.. py:function:: create_tournament_config(num_players: int = 6, starting_chips: int = 1500, blind_levels: list[tuple[int, int]] | None = None) -> haive.games.hold_em.game_agent.HoldemGameAgentConfig

   Create a tournament-style configuration with escalating blinds.


.. py:function:: validate_config(config: haive.games.hold_em.game_agent.HoldemGameAgentConfig) -> tuple[bool, list[str]]

   Validate a game configuration and return issues found.


.. py:function:: validate_player_engines(engines: dict[str, haive.core.engine.aug_llm.AugLLMConfig]) -> bool

   Validate that player engines are properly configured.


.. py:data:: logger

