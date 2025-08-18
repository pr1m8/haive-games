games.core.agent.player_agent
=============================

.. py:module:: games.core.agent.player_agent

Configurable player agent system for games.

This module provides a flexible player agent abstraction that allows games to use
different LLM configurations for players without hardcoding them in engines.

The system supports:
- Dynamic LLM configuration per player
- Role-based agent configuration (player, analyzer, etc.)
- Easy swapping of LLMs and models
- Integration with the new LLM factory system



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">5 classes</span> • <span class="module-stat">3 functions</span>   </div>

.. autoapi-nested-parse::

   Configurable player agent system for games.

   This module provides a flexible player agent abstraction that allows games to use
   different LLM configurations for players without hardcoding them in engines.

   The system supports:
   - Dynamic LLM configuration per player
   - Role-based agent configuration (player, analyzer, etc.)
   - Easy swapping of LLMs and models
   - Integration with the new LLM factory system



      
            
            

.. admonition:: Classes (5)
   :class: note

   .. autoapisummary::

      games.core.agent.player_agent.ConfigurableGameAgent
      games.core.agent.player_agent.GamePlayerRole
      games.core.agent.player_agent.PlayerAgentConfig
      games.core.agent.player_agent.PlayerAgentFactory
      games.core.agent.player_agent.PlayerRole

            

.. admonition:: Functions (3)
   :class: info

   .. autoapisummary::

      games.core.agent.player_agent.create_llm_config
      games.core.agent.player_agent.create_player_config
      games.core.agent.player_agent.create_simple_player_configs

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ConfigurableGameAgent

            Bases: :py:obj:`abc.ABC`


            Abstract base for game agents with configurable players.

            This class provides the interface for game agents that support configurable player
            agents instead of hardcoded engines.



            .. py:method:: create_engines_from_player_configs(player_configs: dict[str, PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]
               :abstractmethod:


               Create engines from player configurations.

               :param player_configs: Dictionary of role name to player agent config

               :returns: Dictionary of engines
               :rtype: Dict[str, AugLLMConfig]



            .. py:method:: get_role_definitions() -> dict[str, GamePlayerRole]
               :abstractmethod:


               Get the role definitions for this game.

               :returns: Dictionary of role name to role definition
               :rtype: Dict[str, GamePlayerRole]




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GamePlayerRole(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Standard implementation of a player role in a game.

            This class defines a specific role that a player can take in a game, such as
            'white_player', 'black_analyzer', etc.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:attribute:: description
               :type:  str
               :value: None



            .. py:attribute:: prompt_template
               :type:  Any
               :value: None



            .. py:attribute:: role_name
               :type:  str
               :value: None



            .. py:attribute:: structured_output_model
               :type:  type | None
               :value: None



            .. py:attribute:: temperature
               :type:  float | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PlayerAgentConfig(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Configuration for a player agent.

            This allows specifying which LLM configuration to use for a player without
            hardcoding it in the engine definitions.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: create_llm_config() -> haive.core.models.llm.LLMConfig

               Create an LLMConfig instance from the configuration.

               :returns: Configured LLM instance
               :rtype: LLMConfig



            .. py:attribute:: llm_config
               :type:  str | haive.core.models.llm.LLMConfig | dict[str, Any]
               :value: None



            .. py:attribute:: model_provider
               :type:  str | None
               :value: None



            .. py:attribute:: player_name
               :type:  str | None
               :value: None



            .. py:attribute:: temperature
               :type:  float | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PlayerAgentFactory

            Factory for creating configurable player agents.

            This factory creates AugLLMConfig instances for game roles using configurable player
            agents instead of hardcoded LLM configurations.



            .. py:method:: create_engines_from_player_configs(roles: dict[str, GamePlayerRole], player_configs: dict[str, PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]
               :staticmethod:


               Create a complete set of engines from role definitions and player configs.

               :param roles: Dictionary of role name to role definition
               :param player_configs: Dictionary of role name to player agent config

               :returns: Dictionary of engines
               :rtype: Dict[str, AugLLMConfig]

               .. rubric:: Example

               >>> roles = {
               ...     "white_player": GamePlayerRole(
               ...         role_name="white_player",
               ...         prompt_template=white_move_prompt,
               ...         structured_output_model=ChessPlayerDecision
               ...     )
               ... }
               >>> configs = {
               ...     "white_player": PlayerAgentConfig(llm_config="gpt-4")
               ... }
               >>> engines = PlayerAgentFactory.create_engines_from_player_configs(roles, configs)



            .. py:method:: create_player_engine(role: GamePlayerRole, agent_config: PlayerAgentConfig, **kwargs) -> haive.core.engine.aug_llm.AugLLMConfig
               :staticmethod:


               Create an AugLLMConfig for a player role.

               :param role: The game role definition
               :param agent_config: The player agent configuration
               :param \*\*kwargs: Additional parameters for AugLLMConfig

               :returns: Configured engine for the role
               :rtype: AugLLMConfig




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PlayerRole

            Bases: :py:obj:`Protocol`


            Protocol defining the interface for player roles.


            .. py:method:: get_prompt_template() -> Any

               Get the prompt template for this role.



            .. py:method:: get_role_name() -> str

               Get the name of this role.



            .. py:method:: get_structured_output_model() -> type | None

               Get the structured output model for this role.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_llm_config(model: str, **kwargs) -> haive.core.models.llm.LLMConfig

            Create an LLM config based on model string.

            This is a simple helper to create configs until a proper factory is available.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_player_config(model: str | haive.core.models.llm.LLMConfig, temperature: float | None = None, player_name: str | None = None, **kwargs) -> PlayerAgentConfig

            Create a player agent configuration.

            :param model: Model string, LLMConfig instance, or config dict
            :param temperature: Temperature setting
            :param player_name: Human-readable name for the player
            :param \*\*kwargs: Additional configuration parameters

            :returns: Configured player agent
            :rtype: PlayerAgentConfig

            .. rubric:: Examples

            >>> config = create_player_config("gpt-4", temperature=0.7)
            >>> config = create_player_config("anthropic:claude-3-opus")
            >>> config = create_player_config({"model": "gpt-4", "provider": "openai"})



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_simple_player_configs(white_model: str | haive.core.models.llm.LLMConfig = 'gpt-4', black_model: str | haive.core.models.llm.LLMConfig = 'claude-3-opus', temperature: float | None = None, **kwargs) -> dict[str, PlayerAgentConfig]

            Create simple player configurations for two-player games.

            :param white_model: Model for white/first player
            :param black_model: Model for black/second player
            :param temperature: Temperature for both players
            :param \*\*kwargs: Additional configuration parameters

            :returns: Player configurations
            :rtype: Dict[str, PlayerAgentConfig]

            .. rubric:: Example

            >>> configs = create_simple_player_configs("gpt-4", "claude-3-opus", temperature=0.7)
            >>> # Creates configs for white_player, black_player, white_analyzer, black_analyzer





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.core.agent.player_agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

