games.battleship.config
=======================

.. py:module:: games.battleship.config

Battleship game agent configuration.

This module defines comprehensive configuration classes for Battleship game agents,
providing extensive customization options for game rules, AI behavior, UI preferences,
and performance settings.

The configuration system supports:
    - Board size and ship placement customization
    - Multiple difficulty levels and AI strategies
    - Turn time limits and timeout handling
    - Analysis and logging capabilities
    - UI themes and display preferences
    - Performance optimization settings

Classes:
    BattleshipAgentConfig: Main configuration class for Battleship agents
    ShipConfiguration: Configuration for ship types and placement rules
    GameRuleConfiguration: Game rule and validation settings
    UIConfiguration: User interface and display settings
    PerformanceConfiguration: Performance and optimization settings

.. rubric:: Example

Creating a basic Battleship agent configuration:

    config = BattleshipAgentConfig(
        player_name="Admiral Hayes",
        difficulty="intermediate",
        board_size=10,
        enable_analysis=True,
        turn_timeout=30.0,
    )

    agent = BattleshipAgent(config)

.. note::

   All configuration classes include comprehensive validation to ensure
   game rule consistency and prevent invalid combinations that would
   break gameplay mechanics.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Battleship game agent configuration.

   This module defines comprehensive configuration classes for Battleship game agents,
   providing extensive customization options for game rules, AI behavior, UI preferences,
   and performance settings.

   The configuration system supports:
       - Board size and ship placement customization
       - Multiple difficulty levels and AI strategies
       - Turn time limits and timeout handling
       - Analysis and logging capabilities
       - UI themes and display preferences
       - Performance optimization settings

   Classes:
       BattleshipAgentConfig: Main configuration class for Battleship agents
       ShipConfiguration: Configuration for ship types and placement rules
       GameRuleConfiguration: Game rule and validation settings
       UIConfiguration: User interface and display settings
       PerformanceConfiguration: Performance and optimization settings

   .. rubric:: Example

   Creating a basic Battleship agent configuration:

       config = BattleshipAgentConfig(
           player_name="Admiral Hayes",
           difficulty="intermediate",
           board_size=10,
           enable_analysis=True,
           turn_timeout=30.0,
       )

       agent = BattleshipAgent(config)

   .. note::

      All configuration classes include comprehensive validation to ensure
      game rule consistency and prevent invalid combinations that would
      break gameplay mechanics.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.battleship.config.BattleshipAgentConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: BattleshipAgentConfig

            Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


            Comprehensive configuration for Battleship game agents with extensive.
            customization.

            This configuration class provides complete control over Battleship game mechanics,
            supporting various game modes, strategic analysis settings, visualization options,
            and LLM engine configurations. It includes validation for game consistency and
            provides factory methods for common Battleship scenarios.

            The configuration system supports:
            - Player identification and naming
            - Strategic analysis and decision-making options
            - Visualization and debugging settings
            - LLM engine configurations for different game actions
            - Performance optimization parameters
            - Game state management and persistence

            .. attribute:: name

               Unique identifier for the agent instance.
               Used for logging, debugging, and multi-agent coordination.

               :type: str

            .. attribute:: state_schema

               Pydantic model class for game state management.
               Defines the structure and validation rules for game state.

               :type: type

            .. attribute:: player1_name

               Display name for the first player.
               Used in visualization and game logging. Auto-generated from engine config.

               :type: str

            .. attribute:: player2_name

               Display name for the second player.
               Used in visualization and game logging. Auto-generated from engine config.

               :type: str

            .. attribute:: enable_analysis

               Enable strategic analysis during gameplay.
               When True, agents will perform detailed position analysis before moves.

               :type: bool

            .. attribute:: visualize_board

               Enable board visualization during gameplay.
               When True, displays game boards and move history in console.

               :type: bool

            .. attribute:: runnable_config

               LangChain runnable configuration.
               Controls execution parameters including recursion limits and thread IDs.

               :type: RunnableConfig

            .. attribute:: engines

               LLM engine configurations for game actions.
               Contains engines for ship placement, move generation, and analysis.

               :type: Dict[str, AugLLMConfig]

            .. rubric:: Examples

            Standard competitive configuration::\n

                config = BattleshipAgentConfig(
                    name="tournament_battleship",
                    player1_name="Strategic_AI",
                    player2_name="Tactical_AI",
                    enable_analysis=True,
                    visualize_board=False
                )

            Training and debugging configuration::\n

                config = BattleshipAgentConfig(
                    name="training_battleship",
                    enable_analysis=True,
                    visualize_board=True,
                    player1_name="Learning_Agent",
                    player2_name="Reference_Agent"
                )

            Performance-optimized configuration::\n

                config = BattleshipAgentConfig(
                    name="speed_battleship",
                    enable_analysis=False,
                    visualize_board=False,
                    runnable_config={
                        "configurable": {
                            "recursion_limit": 5000,
                            "thread_id": "speed_session"
                        }
                    }
                )

            .. note::

               Configuration validation ensures game rule consistency and prevents
               invalid combinations that would break gameplay mechanics or create
               unfair advantages.


            .. py:class:: Config

               Pydantic configuration for flexible validation and type handling.


               .. py:attribute:: arbitrary_types_allowed
                  :value: True



               .. py:attribute:: validate_assignment
                  :value: True




            .. py:method:: competitive() -> BattleshipAgentConfig
               :classmethod:


               Create a configuration optimized for competitive gameplay.

               Generates a configuration suitable for tournaments and competitive matches,
               with analysis enabled but visualization disabled for performance.

               :returns: Configuration optimized for competitive play.
               :rtype: BattleshipAgentConfig

               .. rubric:: Examples

               Creating a tournament-ready configuration::\n

                   config = BattleshipAgentConfig.competitive()
                   agent = BattleshipAgent(config)

                   # Results in:
                   # - Analysis enabled for strategic depth
                   # - Visualization disabled for performance
                   # - Optimized recursion limits
                   # - Tournament-appropriate naming



            .. py:method:: performance() -> BattleshipAgentConfig
               :classmethod:


               Create a configuration optimized for maximum performance.

               Generates a configuration suitable for high-speed gameplay and benchmarking,
               with analysis and visualization disabled for optimal performance.

               :returns: Configuration optimized for performance.
               :rtype: BattleshipAgentConfig

               .. rubric:: Examples

               Creating a performance-optimized configuration::\n

                   config = BattleshipAgentConfig.performance()
                   agent = BattleshipAgent(config)

                   # Results in:
                   # - Analysis disabled for speed
                   # - Visualization disabled for performance
                   # - Reduced recursion limits
                   # - Performance-appropriate naming



            .. py:method:: training() -> BattleshipAgentConfig
               :classmethod:


               Create a configuration optimized for training and development.

               Generates a configuration suitable for agent training, debugging, and
               development work, with full analysis and visualization enabled.

               :returns: Configuration optimized for training scenarios.
               :rtype: BattleshipAgentConfig

               .. rubric:: Examples

               Creating a training configuration::\n

                   config = BattleshipAgentConfig.training()
                   agent = BattleshipAgent(config)

                   # Results in:
                   # - Analysis enabled for learning
                   # - Visualization enabled for monitoring
                   # - Extended recursion limits
                   # - Training-appropriate naming



            .. py:method:: update_player_names_from_engines() -> Any

               Update player names based on LLM provider and model from engines.

               Automatically generates meaningful player names based on the configured
               LLM engines, creating identifiers that include provider and model information.
               Also ensures thread_id is set for proper session management.

               :returns: Self with updated player names and thread configuration.
               :rtype: BattleshipAgentConfig

               .. rubric:: Examples

               Configuration with OpenAI engines::\n

                   config = BattleshipAgentConfig()
                   # After validation, player names might be:
                   # player1_name = "azure-gpt-4o"
                   # player2_name = "Player 2"



            .. py:property:: configuration_summary
               :type: dict[str, str]


               Get a summary of the current configuration settings.

               :returns: Summary of key configuration parameters.
               :rtype: Dict[str, str]

               .. rubric:: Examples

               Checking configuration summary::\n

                   config = BattleshipAgentConfig.competitive()
                   summary = config.configuration_summary
                   print(f"Mode: {summary['mode']}")
                   print(f"Analysis: {summary['analysis_enabled']}")


            .. py:attribute:: enable_analysis
               :type:  bool
               :value: None



            .. py:attribute:: engines
               :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
               :value: None



            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: player1_name
               :type:  str
               :value: None



            .. py:attribute:: player2_name
               :type:  str
               :value: None



            .. py:attribute:: runnable_config
               :type:  langchain_core.runnables.RunnableConfig
               :value: None



            .. py:attribute:: state_schema
               :type:  type
               :value: None



            .. py:attribute:: visualize_board
               :type:  bool
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.battleship.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

