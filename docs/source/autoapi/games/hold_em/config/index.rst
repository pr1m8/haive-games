games.hold_em.config
====================

.. py:module:: games.hold_em.config

Texas Hold'em configuration module.

This module provides configuration classes for the Hold'em game, including:
    - Game agent configuration
    - Player agent configurations
    - Engine configurations



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">9 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Texas Hold'em configuration module.

   This module provides configuration classes for the Hold'em game, including:
       - Game agent configuration
       - Player agent configurations
       - Engine configurations



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.hold_em.config.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.hold_em.config.HoldemGameSettings

            

.. admonition:: Functions (9)
   :class: info

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

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HoldemGameSettings(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Settings for customizing Hold'em games.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: to_game_config() -> haive.games.hold_em.game_agent.HoldemGameAgentConfig

               Convert settings to a game configuration.



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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_cash_game_config(num_players: int = 6, big_blind: int = 20, max_buy_in: int = 2000, min_buy_in: int = 400) -> haive.games.hold_em.game_agent.HoldemGameAgentConfig

            Create a cash game configuration.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_custom_holdem_config(settings: HoldemGameSettings) -> haive.games.hold_em.game_agent.HoldemGameAgentConfig

            Create a custom Hold'em configuration from settings.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_default_holdem_config(num_players: int = 4, starting_chips: int = 1000, small_blind: int = 10, big_blind: int = 20) -> haive.games.hold_em.game_agent.HoldemGameAgentConfig

            Create a default Hold'em game configuration.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_fallback_engines(player_name: str, player_style: str) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create minimal fallback engines if the main engine creation fails.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_fallback_game_engines() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create minimal fallback game engines.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_heads_up_config(player1_name: str = 'Alice', player2_name: str = 'Bob', starting_chips: int = 1000, big_blind: int = 20) -> haive.games.hold_em.game_agent.HoldemGameAgentConfig

            Create a heads-up (2 player) configuration.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_tournament_config(num_players: int = 6, starting_chips: int = 1500, blind_levels: list[tuple[int, int]] | None = None) -> haive.games.hold_em.game_agent.HoldemGameAgentConfig

            Create a tournament-style configuration with escalating blinds.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: validate_config(config: haive.games.hold_em.game_agent.HoldemGameAgentConfig) -> tuple[bool, list[str]]

            Validate a game configuration and return issues found.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: validate_player_engines(engines: dict[str, haive.core.engine.aug_llm.AugLLMConfig]) -> bool

            Validate that player engines are properly configured.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.hold_em.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

