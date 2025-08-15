games.hold_em.configurable_config
=================================

.. py:module:: games.hold_em.configurable_config

.. autoapi-nested-parse::

   Configurable Hold'em configuration using the generic player agent system.

   This module provides configurable Texas Hold'em game configurations that replace
   hardcoded LLM settings with dynamic, configurable player agents.


   .. autolink-examples:: games.hold_em.configurable_config
      :collapse:


Attributes
----------

.. autoapisummary::

   games.hold_em.configurable_config.EXAMPLE_CONFIGURATIONS
   games.hold_em.configurable_config.config1
   games.hold_em.configurable_config.logger


Classes
-------

.. autoapisummary::

   games.hold_em.configurable_config.ConfigurableHoldemConfig


Functions
---------

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


Module Contents
---------------

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


   .. autolink-examples:: ConfigurableHoldemConfig
      :collapse:

   .. py:method:: _extract_player_names_from_configs()

      Extract player names from player configurations.


      .. autolink-examples:: _extract_player_names_from_configs
         :collapse:


   .. py:method:: _generate_player_names_from_example()

      Generate player names based on example configuration.


      .. autolink-examples:: _generate_player_names_from_example
         :collapse:


   .. py:method:: _generate_player_names_from_models(player1_model: str, player2_model: str)

      Generate player names based on model names.


      .. autolink-examples:: _generate_player_names_from_models
         :collapse:


   .. py:method:: model_post_init(__context: Any) -> None

      Initialize engines after model creation.


      .. autolink-examples:: model_post_init
         :collapse:


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



.. py:function:: create_budget_holdem_config(**kwargs) -> ConfigurableHoldemConfig

   Create a budget-friendly Hold'em configuration.


   .. autolink-examples:: create_budget_holdem_config
      :collapse:

.. py:function:: create_experimental_holdem_config(**kwargs) -> ConfigurableHoldemConfig

   Create an experimental Hold'em configuration with mixed providers.


   .. autolink-examples:: create_experimental_holdem_config
      :collapse:

.. py:function:: create_heads_up_holdem_config(**kwargs) -> ConfigurableHoldemConfig

   Create a heads-up specialized Hold'em configuration.


   .. autolink-examples:: create_heads_up_holdem_config
      :collapse:

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


   .. autolink-examples:: create_holdem_config
      :collapse:

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


   .. autolink-examples:: create_holdem_config_from_example
      :collapse:

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


   .. autolink-examples:: create_holdem_config_from_player_configs
      :collapse:

.. py:function:: create_poker_pro_holdem_config(**kwargs) -> ConfigurableHoldemConfig

   Create a poker professional-style Hold'em configuration with powerful models.


   .. autolink-examples:: create_poker_pro_holdem_config
      :collapse:

.. py:function:: get_example_config(name: str) -> ConfigurableHoldemConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurableHoldemConfig

   :raises ValueError: If the example name is not found


   .. autolink-examples:: get_example_config
      :collapse:

.. py:function:: list_example_configurations() -> dict[str, str]

   List all available example configurations.

   :returns: Mapping of configuration names to descriptions
   :rtype: Dict[str, str]


   .. autolink-examples:: list_example_configurations
      :collapse:

.. py:data:: EXAMPLE_CONFIGURATIONS

.. py:data:: config1

.. py:data:: logger

