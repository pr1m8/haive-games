games.hold_em.configurable_config
=================================

.. py:module:: games.hold_em.configurable_config

Configurable Hold'em configuration using the generic player agent system.

This module provides configurable Texas Hold'em game configurations that replace
hardcoded LLM settings with dynamic, configurable player agents.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">9 functions</span> • <span class="module-stat">3 attributes</span>   </div>

.. autoapi-nested-parse::

   Configurable Hold'em configuration using the generic player agent system.

   This module provides configurable Texas Hold'em game configurations that replace
   hardcoded LLM settings with dynamic, configurable player agents.



      

.. admonition:: Attributes (3)
   :class: tip

   .. autoapisummary::

      games.hold_em.configurable_config.EXAMPLE_CONFIGURATIONS
      games.hold_em.configurable_config.config1
      games.hold_em.configurable_config.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.hold_em.configurable_config.ConfigurableHoldemConfig

            

.. admonition:: Functions (9)
   :class: info

   .. autoapisummary::

      games.hold_em.configurable_config.create_budget_holdem_config
      games.hold_em.configurable_config.create_experimental_holdem_config
      games.hold_em.configurable_config.create_heads_up_holdem_config
      games.hold_em.configurable_config.create_holdem_config
      games.hold_em.configurable_config.create_holdem_config_from_example
      games.hold_em.configurable_config.create_holdem_config_from_player_configs
      games.hold_em.configurable_config.create_poker_pro_holdem_config
      games.hold_em.configurable_config.get_example_config
      games.hold_em.configurable_config.list_example_configurations

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ConfigurableHoldemConfig

            Bases: :py:obj:`haive.games.hold_em.config.HoldemGameAgentConfig`


            Configurable Hold'em configuration with dynamic LLM selection.

            This configuration allows users to specify different LLMs for different
            roles in the Texas Hold'em game, providing flexibility and avoiding hardcoded models.

            .. attribute:: player1_model

               Model for player 1 (can be string or LLMConfig)

            .. attribute:: player2_model

               Model for player 2 (can be string or LLMConfig)

            .. attribute:: player1_name

               Name for player 1

            .. attribute:: player2_name

               Name for player 2

            .. attribute:: example_config

               Optional example configuration name

            .. attribute:: player_configs

               Optional detailed player configurations

            .. attribute:: temperature

               Temperature for LLM generation

            .. attribute:: enable_analysis

               Whether to enable strategic analysis

            .. attribute:: heads_up_mode

               Whether this is heads-up play

            .. attribute:: recursion_limit

               Python recursion limit for game execution


            .. py:method:: _extract_player_names_from_configs()

               Extract player names from player configurations.



            .. py:method:: _generate_player_names_from_example()

               Generate player names based on example configuration.



            .. py:method:: _generate_player_names_from_models(player1_model: str, player2_model: str)

               Generate player names based on model names.



            .. py:method:: model_post_init(__context: Any) -> None

               Initialize engines after model creation.



            .. py:attribute:: example_config
               :type:  str | None
               :value: None



            .. py:attribute:: heads_up_mode
               :type:  bool
               :value: None



            .. py:attribute:: player1_model
               :type:  str | None
               :value: None



            .. py:attribute:: player2_model
               :type:  str | None
               :value: None



            .. py:attribute:: player_configs
               :type:  dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig] | None
               :value: None



            .. py:attribute:: recursion_limit
               :type:  int
               :value: None



            .. py:attribute:: temperature
               :type:  float
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_budget_holdem_config(**kwargs) -> ConfigurableHoldemConfig

            Create a budget-friendly Hold'em configuration.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_experimental_holdem_config(**kwargs) -> ConfigurableHoldemConfig

            Create an experimental Hold'em configuration with mixed providers.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_heads_up_holdem_config(**kwargs) -> ConfigurableHoldemConfig

            Create a heads-up specialized Hold'em configuration.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_holdem_config(player1_model: str = 'gpt-4o', player2_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableHoldemConfig

            Create a configurable Hold'em configuration with simple model specifications.

            :param player1_model: Model for player 1 and analyzer
            :param player2_model: Model for player 2 and analyzer
            :param \*\*kwargs: Additional configuration parameters

            :returns: Configured Hold'em game
            :rtype: ConfigurableHoldemConfig

            .. rubric:: Example

            >>> config = create_holdem_config("gpt-4o", "claude-3-opus", temperature=0.5)
            >>> config = create_holdem_config(
            ...     "openai:gpt-4o",
            ...     "anthropic:claude-3-5-sonnet-20240620",
            ...     heads_up_mode=True
            ... )



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_holdem_config_from_example(example_name: str, **kwargs) -> ConfigurableHoldemConfig

            Create a configurable Hold'em configuration from a predefined example.

            :param example_name: Name of the example configuration
            :param \*\*kwargs: Additional configuration parameters to override

            :returns: Configured Hold'em game
            :rtype: ConfigurableHoldemConfig

            Available examples:
                - "gpt_vs_claude": GPT vs Claude
                - "gpt_only": GPT for both players
                - "claude_only": Claude for both players
                - "budget": Cost-effective models
                - "mixed": Different provider per role
                - "poker_pros": High-powered models for strategic gameplay
                - "heads_up": Specialized for heads-up play

            .. rubric:: Example

            >>> config = create_holdem_config_from_example("budget", temperature=0.3)
            >>> config = create_holdem_config_from_example("poker_pros", heads_up_mode=True)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_holdem_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurableHoldemConfig

            Create a configurable Hold'em configuration from detailed player configurations.

            :param player_configs: Dictionary mapping role names to player configurations
            :param \*\*kwargs: Additional configuration parameters

            :returns: Configured Hold'em game
            :rtype: ConfigurableHoldemConfig

            Expected roles:
                - "player1_player": Player 1 configuration
                - "player2_player": Player 2 configuration
                - "player1_analyzer": Player 1 analyzer configuration
                - "player2_analyzer": Player 2 analyzer configuration

            .. rubric:: Example

            >>> player_configs = {
            ...     "player1_player": PlayerAgentConfig(
            ...         llm_config="gpt-4o",
            ...         temperature=0.7,
            ...         player_name="Poker Pro"
            ...     ),
            ...     "player2_player": PlayerAgentConfig(
            ...         llm_config="claude-3-opus",
            ...         temperature=0.3,
            ...         player_name="Card Shark"
            ...     ),
            ...     "player1_analyzer": PlayerAgentConfig(
            ...         llm_config="gpt-4o",
            ...         temperature=0.2,
            ...         player_name="Strategic Analyst"
            ...     ),
            ...     "player2_analyzer": PlayerAgentConfig(
            ...         llm_config="claude-3-opus",
            ...         temperature=0.2,
            ...         player_name="Game Theory Expert"
            ...     ),
            ... }
            >>> config = create_holdem_config_from_player_configs(player_configs)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_poker_pro_holdem_config(**kwargs) -> ConfigurableHoldemConfig

            Create a poker professional-style Hold'em configuration with powerful models.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_example_config(name: str) -> ConfigurableHoldemConfig

            Get a predefined example configuration by name.

            :param name: Name of the example configuration

            :returns: The example configuration
            :rtype: ConfigurableHoldemConfig

            :raises ValueError: If the example name is not found



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: list_example_configurations() -> dict[str, str]

            List all available example configurations.

            :returns: Mapping of configuration names to descriptions
            :rtype: Dict[str, str]



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: EXAMPLE_CONFIGURATIONS


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: config1


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.hold_em.configurable_config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

