games.mafia.config
==================

.. py:module:: games.mafia.config

Configuration for the Mafia game agent.

This module provides configuration classes and utilities for the Mafia game
agent, including:
    - Game settings (max days, discussion rounds)
    - LLM engine configurations
    - Role mappings and assignments
    - Debug settings

.. rubric:: Example

>>> from mafia.config import MafiaAgentConfig
>>>
>>> # Create a default configuration for 7 players
>>> config = MafiaAgentConfig.default_config(
...     player_count=7,
...     max_days=3
... )
>>> print(config.max_days)  # Shows 3



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Configuration for the Mafia game agent.

   This module provides configuration classes and utilities for the Mafia game
   agent, including:
       - Game settings (max days, discussion rounds)
       - LLM engine configurations
       - Role mappings and assignments
       - Debug settings

   .. rubric:: Example

   >>> from mafia.config import MafiaAgentConfig
   >>>
   >>> # Create a default configuration for 7 players
   >>> config = MafiaAgentConfig.default_config(
   ...     player_count=7,
   ...     max_days=3
   ... )
   >>> print(config.max_days)  # Shows 3



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.mafia.config.MafiaAgentConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MafiaAgentConfig

            Bases: :py:obj:`haive.games.framework.multi_player.config.MultiPlayerGameConfig`


            Configuration for the Mafia game agent.

            This class extends MultiPlayerGameConfig to provide Mafia-specific
            configuration options and defaults.

            .. attribute:: max_days

               Maximum number of days before forcing game end

               :type: int

            .. attribute:: day_discussion_rounds

               Number of discussion rounds per day

               :type: int

            .. attribute:: engines

               LLM configs by role

               :type: Dict[str, Dict[str, AugLLMConfig]]

            .. attribute:: state_schema

               State schema for the game

               :type: Type[MafiaGameState]

            .. attribute:: role_mapping

               Engine key to role mapping

               :type: Dict[str, PlayerRole]

            .. attribute:: debug

               Enable debug mode for detailed logging

               :type: bool

            .. rubric:: Example

            >>> config = MafiaAgentConfig(
            ...     name="mafia_game",
            ...     max_days=3,
            ...     engines=aug_llm_configs,
            ...     initial_player_count=7
            ... )
            >>> print(config.max_days)  # Shows 3


            .. py:method:: default_config(player_count: int = 7, max_days: int = 3) -> MafiaAgentConfig
               :classmethod:


               Create a default configuration for a Mafia game.

               This method creates a standard configuration with appropriate role
               mappings and engine configurations for the specified number of players.

               :param player_count: Number of players including narrator.
                                    Defaults to 7.
               :type player_count: int, optional
               :param max_days: Maximum number of days before forcing
                                game end. Defaults to 3.
               :type max_days: int, optional

               :returns: Configured agent ready for game initialization
               :rtype: MafiaAgentConfig

               .. rubric:: Example

               >>> config = MafiaAgentConfig.default_config(
               ...     player_count=9,
               ...     max_days=4
               ... )
               >>> print(len(config.role_mapping))  # Shows 5 (all roles)



            .. py:attribute:: day_discussion_rounds
               :type:  int
               :value: None



            .. py:attribute:: debug
               :type:  bool
               :value: None



            .. py:attribute:: engines
               :type:  dict[str, dict[str, haive.core.engine.aug_llm.AugLLMConfig]]
               :value: None



            .. py:attribute:: max_days
               :type:  int
               :value: None



            .. py:attribute:: role_mapping
               :type:  dict[str, haive.games.mafia.models.PlayerRole]
               :value: None



            .. py:attribute:: state_schema
               :type:  type[haive.games.mafia.state.MafiaGameState]
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.mafia.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

