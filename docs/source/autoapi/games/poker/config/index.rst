games.poker.config
==================

.. py:module:: games.poker.config

.. autoapi-nested-parse::

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

.. py:class:: PokerAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration class for the poker agent.

   This class defines all necessary parameters and settings for running
   a poker game, including player setup, game rules, and LLM configurations.
   It inherits from the base AgentConfig class and adds poker-specific
   parameters.

   .. attribute:: engines

      Mapping of agent names to their
      LLM configurations. Default is an empty dict.

      :type: Dict[str, AugLLMConfig]

   .. attribute:: player_names

      List of player names in the game.
      Default is ["Alice", "Bob", "Charlie", "Dave"].

      :type: List[str]

   .. attribute:: state_schema

      Schema class for game state.
      Default is PokerState.

      :type: Type[BaseModel]

   .. attribute:: state_schema_manager

      Manager for handling state transitions.
      Default is PokerStateManager().

      :type: Any

   .. attribute:: starting_chips

      Initial chip count for each player.
      Default is 1000.

      :type: int

   .. attribute:: small_blind

      Small blind amount. Default is 5.

      :type: int

   .. attribute:: big_blind

      Big blind amount. Default is 10.

      :type: int

   .. attribute:: max_hands

      Maximum number of hands to play.
      Default is 10.

      :type: int

   .. attribute:: enable_detailed_analysis

      Whether to log detailed hand
      analysis. Default is True.

      :type: bool

   .. attribute:: save_game_history

      Whether to save game history to disk.
      Default is True.

      :type: bool

   .. rubric:: Example

   >>> config = PokerAgentConfig(
   ...     name="high_stakes_game",
   ...     starting_chips=5000,
   ...     small_blind=25,
   ...     big_blind=50,
   ...     max_hands=20
   ... )


   .. autolink-examples:: PokerAgentConfig
      :collapse:

   .. py:method:: default_config(**kwargs) -> PokerAgentConfig
      :classmethod:


      Create a default configuration for poker agents.

      This class method generates a default configuration with reasonable
      starting values for all parameters. Any parameter can be overridden
      by passing it as a keyword argument.

      :param \*\*kwargs: Override default configuration parameters. Valid keys
                         include all attributes of PokerAgentConfig.

      :returns:

                A new configuration instance with default
                    values and any specified overrides.
      :rtype: PokerAgentConfig

      .. rubric:: Example

      >>> config = PokerAgentConfig.default_config(
      ...     player_names=["Player1", "Player2", "Player3"],
      ...     starting_chips=2000,
      ...     max_hands=15
      ... )


      .. autolink-examples:: default_config
         :collapse:


   .. py:attribute:: big_blind
      :type:  int
      :value: None



   .. py:attribute:: enable_detailed_analysis
      :type:  bool
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: max_hands
      :type:  int
      :value: None



   .. py:attribute:: player_names
      :type:  list[str]
      :value: None



   .. py:attribute:: save_game_history
      :type:  bool
      :value: None



   .. py:attribute:: small_blind
      :type:  int
      :value: None



   .. py:attribute:: starting_chips
      :type:  int
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: state_schema_manager
      :type:  Any
      :value: None



