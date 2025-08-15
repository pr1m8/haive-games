games.hold_em.config
====================

.. py:module:: games.hold_em.config

.. autoapi-nested-parse::

   Texas Hold'em configuration module.

   This module provides configuration classes for the Hold'em game, including:
       - Game agent configuration
       - Player agent configurations
       - Engine configurations


   .. autolink-examples:: games.hold_em.config
      :collapse:


Attributes
----------

.. autoapisummary::

   games.hold_em.config.logger


Classes
-------

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

.. py:class:: HoldemGameSettings(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Settings for customizing Hold'em games.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HoldemGameSettings
      :collapse:

   .. py:method:: to_game_config() -> haive.games.hold_em.game_agent.HoldemGameAgentConfig

      Convert settings to a game configuration.


      .. autolink-examples:: to_game_config
         :collapse:


   .. py:attribute:: ai_aggression
      :type:  float
      :value: None



   .. py:attribute:: ai_variance
      :type:  float
      :value: None



   .. py:attribute:: big_blind
      :type:  int
      :value: None



   .. py:attribute:: decision_time
      :type:  float
      :value: None



   .. py:attribute:: enable_hand_analysis
      :type:  bool
      :value: None



   .. py:attribute:: enable_opponent_modeling
      :type:  bool
      :value: None



   .. py:attribute:: enable_position_analysis
      :type:  bool
      :value: None



   .. py:attribute:: fast_fold
      :type:  bool
      :value: None



   .. py:attribute:: heads_up
      :type:  bool
      :value: None



   .. py:attribute:: max_hands
      :type:  int
      :value: None



   .. py:attribute:: num_players
      :type:  int
      :value: None



   .. py:attribute:: small_blind
      :type:  int
      :value: None



   .. py:attribute:: starting_chips
      :type:  int
      :value: None



   .. py:attribute:: tournament_mode
      :type:  bool
      :value: None



.. py:function:: create_cash_game_config(num_players: int = 6, big_blind: int = 20, max_buy_in: int = 2000, min_buy_in: int = 400) -> haive.games.hold_em.game_agent.HoldemGameAgentConfig

   Create a cash game configuration.


   .. autolink-examples:: create_cash_game_config
      :collapse:

.. py:function:: create_custom_holdem_config(settings: HoldemGameSettings) -> haive.games.hold_em.game_agent.HoldemGameAgentConfig

   Create a custom Hold'em configuration from settings.


   .. autolink-examples:: create_custom_holdem_config
      :collapse:

.. py:function:: create_default_holdem_config(num_players: int = 4, starting_chips: int = 1000, small_blind: int = 10, big_blind: int = 20) -> haive.games.hold_em.game_agent.HoldemGameAgentConfig

   Create a default Hold'em game configuration.


   .. autolink-examples:: create_default_holdem_config
      :collapse:

.. py:function:: create_fallback_engines(player_name: str, player_style: str) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create minimal fallback engines if the main engine creation fails.


   .. autolink-examples:: create_fallback_engines
      :collapse:

.. py:function:: create_fallback_game_engines() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create minimal fallback game engines.


   .. autolink-examples:: create_fallback_game_engines
      :collapse:

.. py:function:: create_heads_up_config(player1_name: str = 'Alice', player2_name: str = 'Bob', starting_chips: int = 1000, big_blind: int = 20) -> haive.games.hold_em.game_agent.HoldemGameAgentConfig

   Create a heads-up (2 player) configuration.


   .. autolink-examples:: create_heads_up_config
      :collapse:

.. py:function:: create_tournament_config(num_players: int = 6, starting_chips: int = 1500, blind_levels: list[tuple[int, int]] | None = None) -> haive.games.hold_em.game_agent.HoldemGameAgentConfig

   Create a tournament-style configuration with escalating blinds.


   .. autolink-examples:: create_tournament_config
      :collapse:

.. py:function:: validate_config(config: haive.games.hold_em.game_agent.HoldemGameAgentConfig) -> tuple[bool, list[str]]

   Validate a game configuration and return issues found.


   .. autolink-examples:: validate_config
      :collapse:

.. py:function:: validate_player_engines(engines: dict[str, haive.core.engine.aug_llm.AugLLMConfig]) -> bool

   Validate that player engines are properly configured.


   .. autolink-examples:: validate_player_engines
      :collapse:

.. py:data:: logger

