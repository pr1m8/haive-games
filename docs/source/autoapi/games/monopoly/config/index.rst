games.monopoly.config
=====================

.. py:module:: games.monopoly.config

Module documentation for games.monopoly.config


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">4 classes</span>   </div>


      
            
            

.. admonition:: Classes (4)
   :class: note

   .. autoapisummary::

      games.monopoly.config.GameDifficulty
      games.monopoly.config.GameVariant
      games.monopoly.config.MonopolyGameAgentConfig
      games.monopoly.config.MonopolyPlayerAgentConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameDifficulty

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Enumeration of game difficulty levels for AI strategy.

            Defines different difficulty levels that affect AI decision-making,
            strategic depth, and negotiation complexity.

            Values:
                EASY: Simple decision-making, basic property management
                MEDIUM: Balanced strategy with moderate complexity
                HARD: Advanced strategic analysis and complex negotiations
                EXPERT: Maximum strategic depth with economic optimization


            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: EASY
               :value: 'easy'



            .. py:attribute:: EXPERT
               :value: 'expert'



            .. py:attribute:: HARD
               :value: 'hard'



            .. py:attribute:: MEDIUM
               :value: 'medium'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameVariant

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Enumeration of popular Monopoly game variants.

            Defines different rule sets and game configurations based on
            popular Monopoly variants and house rules.

            Values:
                CLASSIC: Traditional Monopoly rules
                SPEED: Fast-paced variant with reduced game time
                CITY: Modern urban-focused property themes
                ELECTRONIC: Digital banking and modern features
                CUSTOM: User-defined rule combinations


            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: CITY
               :value: 'city'



            .. py:attribute:: CLASSIC
               :value: 'classic'



            .. py:attribute:: CUSTOM
               :value: 'custom'



            .. py:attribute:: ELECTRONIC
               :value: 'electronic'



            .. py:attribute:: SPEED
               :value: 'speed'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MonopolyGameAgentConfig

            Bases: :py:obj:`haive.core.engine.agent.config.AgentConfig`


            Advanced configuration system for Monopoly game agents with comprehensive rule.
            support.

            This class provides complete configuration management for Monopoly gameplay,
            supporting multiple rule variants, economic simulation parameters, and strategic
            AI customization. The configuration system enables flexible game setups from
            casual family games to competitive tournaments and economic research.

            The configuration supports:
            - International rule variants and house rules
            - Advanced economic simulation parameters
            - Multi-player AI configurations with different personalities
            - Trading and negotiation system customization
            - Property development and auction mechanics
            - Performance optimization for different scenarios
            - Comprehensive validation and error handling

            .. attribute:: name

               Unique identifier for the game agent.

               :type: str

            .. attribute:: game_variant

               Selected game variant (classic, speed, city, etc.).

               :type: GameVariant

            .. attribute:: difficulty

               AI difficulty level affecting strategic depth.

               :type: GameDifficulty

            .. attribute:: player_names

               Names of players participating in the game.

               :type: List[str]

            .. attribute:: max_turns

               Maximum number of turns before forcing game end.

               :type: int

            .. attribute:: max_rounds

               Maximum number of complete rounds before game end.

               :type: int

            .. attribute:: starting_money

               Initial money for each player ($1500 in classic).

               :type: int

            .. attribute:: go_salary

               Money collected for passing GO ($200 in classic).

               :type: int

            .. attribute:: enable_trading

               Whether to enable property trading between players.

               :type: bool

            .. attribute:: enable_building

               Whether to enable house and hotel construction.

               :type: bool

            .. attribute:: enable_auctions

               Whether to enable property auctions.

               :type: bool

            .. attribute:: enable_jail_bail

               Whether players can pay bail to leave jail.

               :type: bool

            .. attribute:: free_parking_bonus

               Whether Free Parking collects tax money.

               :type: bool

            .. attribute:: double_go_salary

               Whether landing on GO gives double salary.

               :type: bool

            .. attribute:: income_tax_rate

               Income tax rate as percentage of net worth.

               :type: float

            .. attribute:: luxury_tax_amount

               Fixed luxury tax amount.

               :type: int

            .. attribute:: jail_bail_amount

               Amount to pay for jail bail.

               :type: int

            .. attribute:: house_shortage_rules

               Whether to enforce building shortages.

               :type: bool

            .. attribute:: mortgage_interest_rate

               Interest rate for mortgage redemption.

               :type: float

            .. attribute:: state_schema

               State schema for the game.

               :type: type[BaseModel]

            .. attribute:: player_agent_config

               Configuration for player agents.

               :type: MonopolyPlayerAgentConfig

            .. attribute:: runnable_config

               Runtime configuration.

               :type: RunnableConfig

            .. rubric:: Examples

            Standard family game configuration::\n

                config = MonopolyGameAgentConfig.family_game()
                assert config.difficulty == GameDifficulty.MEDIUM
                assert config.enable_trading == True
                assert config.starting_money == 1500

            Tournament-level competitive play::\n

                config = MonopolyGameAgentConfig.tournament()
                assert config.difficulty == GameDifficulty.EXPERT
                assert config.enable_auctions == True
                assert config.max_turns == 2000

            Economic simulation for research::\n

                config = MonopolyGameAgentConfig.economic_simulation()
                assert config.house_shortage_rules == True
                assert config.mortgage_interest_rate == 0.1
                assert len(config.player_names) == 6

            Custom house rules variant::\n

                config = MonopolyGameAgentConfig(
                    game_variant=GameVariant.CUSTOM,
                    starting_money=2000,
                    free_parking_bonus=True,
                    double_go_salary=True,
                    enable_trading=True
                )

            Speed game configuration::\n

                config = MonopolyGameAgentConfig.speed_game()
                assert config.max_turns == 200
                assert config.starting_money == 1000
                assert config.go_salary == 400

            .. note::

               All configurations use Pydantic for validation and support both JSON
               serialization and integration with distributed tournament systems.


            .. py:method:: _calculate_economic_velocity() -> float

               Calculate economic velocity factor.

               :returns: Economic velocity multiplier.
               :rtype: float



            .. py:method:: _estimate_game_duration() -> str

               Estimate game duration based on configuration.

               :returns: Estimated game duration category.
               :rtype: str



            .. py:method:: casual_game() -> MonopolyGameAgentConfig
               :classmethod:


               Create configuration for casual, relaxed gameplay.

               Casual game features:
               - Easy AI difficulty
               - Generous house rules
               - Shorter game duration
               - Simplified mechanics

               :returns: Configuration for casual gameplay.
               :rtype: MonopolyGameAgentConfig



            .. py:method:: create_initial_state() -> haive.games.monopoly.state.MonopolyState

               Create the initial game state with all required fields and proper validation.

               :returns: Fully initialized game state ready for gameplay.
               :rtype: MonopolyState

               :raises ValueError: If state creation or validation fails.

               .. rubric:: Examples

               Creating initial state::\n

                   config = MonopolyGameAgentConfig.family_game()
                   state = config.create_initial_state()
                   assert len(state.players) == 4
                   assert state.current_player_index == 0
                   assert state.turn_number == 1

               Validating state consistency::\n

                   state = config.create_initial_state()
                   issues = state.validate_state_consistency()
                   assert len(issues) == 0  # No validation issues



            .. py:method:: create_player_agent() -> Any

               Create the player decision agent with configured engines.

               :returns: Configured player agent for decision-making.
               :rtype: MonopolyPlayerAgent

               .. rubric:: Examples

               Creating player agent::\n

                   config = MonopolyGameAgentConfig.tournament()
                   agent = config.create_player_agent()
                   # Agent has advanced AI capabilities



            .. py:method:: default() -> MonopolyGameAgentConfig
               :classmethod:


               Create a default configuration for Monopoly.

               :returns: Default configuration for standard gameplay.
               :rtype: MonopolyGameAgentConfig



            .. py:method:: economic_simulation() -> MonopolyGameAgentConfig
               :classmethod:


               Create configuration for economic research simulation.

               Economic simulation features:
               - Multiple players for market dynamics
               - Realistic economic parameters
               - All advanced features enabled
               - Detailed logging for analysis
               - Extended duration for pattern analysis

               :returns: Configuration for economic simulation.
               :rtype: MonopolyGameAgentConfig



            .. py:method:: family_game() -> MonopolyGameAgentConfig
               :classmethod:


               Create configuration for family-friendly Monopoly game.

               Family game features:
               - Balanced difficulty for all skill levels
               - Standard rules with optional house rules
               - Moderate game duration
               - All major features enabled

               :returns: Configuration for family gameplay.
               :rtype: MonopolyGameAgentConfig

               .. rubric:: Examples

               Creating family game::\n

                   config = MonopolyGameAgentConfig.family_game()
                   agent = MonopolyGameAgent(config)
                   result = agent.run_game()



            .. py:method:: setup_player_agent_engines() -> None

               Set up the engines for the player agent if not already configured.

               This method ensures that the player agent has the necessary LLM engines
               configured for different types of decisions (property, trading, building, etc.).




            .. py:method:: speed_game() -> MonopolyGameAgentConfig
               :classmethod:


               Create configuration for fast-paced Monopoly game.

               Speed game features:
               - Reduced game duration
               - Increased starting money and GO salary
               - Simplified decision-making
               - Limited turns and rounds

               :returns: Configuration for speed gameplay.
               :rtype: MonopolyGameAgentConfig



            .. py:method:: tournament() -> MonopolyGameAgentConfig
               :classmethod:


               Create configuration for tournament-level competitive play.

               Tournament features:
               - Expert AI difficulty
               - Strict official rules
               - Extended game duration
               - All advanced features enabled
               - No house rules

               :returns: Configuration for competitive tournament play.
               :rtype: MonopolyGameAgentConfig



            .. py:method:: validate_max_turns(v: int, info: pydantic.ValidationInfo) -> int
               :classmethod:


               Validate max turns is reasonable for the number of players.

               :param v: Maximum turns to validate.
               :type v: int
               :param info: Validation context containing other field values.
               :type info: ValidationInfo

               :returns: Validated max turns value.
               :rtype: int



            .. py:method:: validate_player_names(v: list[str]) -> list[str]
               :classmethod:


               Validate player names are unique and reasonable.

               :param v: List of player names to validate.
               :type v: List[str]

               :returns: Validated list of player names.
               :rtype: List[str]

               :raises ValueError: If player names are not unique or invalid.



            .. py:attribute:: bankruptcy_elimination
               :type:  bool
               :value: None



            .. py:attribute:: difficulty
               :type:  GameDifficulty
               :value: None



            .. py:attribute:: double_go_salary
               :type:  bool
               :value: None



            .. py:property:: economic_parameters
               :type: dict[str, int | float]


               Calculate economic parameters for the game.

               :returns: Economic settings and derived values.
               :rtype: Dict[str, Union[int, float]]


            .. py:attribute:: enable_auctions
               :type:  bool
               :value: None



            .. py:attribute:: enable_building
               :type:  bool
               :value: None



            .. py:attribute:: enable_detailed_logging
               :type:  bool
               :value: None



            .. py:attribute:: enable_jail_bail
               :type:  bool
               :value: None



            .. py:attribute:: enable_trading
               :type:  bool
               :value: None



            .. py:attribute:: free_parking_bonus
               :type:  bool
               :value: None



            .. py:property:: game_profile
               :type: dict[str, str | int | float | bool]


               Generate comprehensive game profile summary.

               :returns: Game characteristics and settings.
               :rtype: Dict[str, Union[str, int, float, bool]]


            .. py:attribute:: game_variant
               :type:  GameVariant
               :value: None



            .. py:attribute:: go_salary
               :type:  int
               :value: None



            .. py:attribute:: house_shortage_rules
               :type:  bool
               :value: None



            .. py:attribute:: income_tax_rate
               :type:  float
               :value: None



            .. py:attribute:: jail_bail_amount
               :type:  int
               :value: None



            .. py:attribute:: luxury_tax_amount
               :type:  int
               :value: None



            .. py:attribute:: max_rounds
               :type:  int
               :value: None



            .. py:attribute:: max_turns
               :type:  int
               :value: None



            .. py:attribute:: model_config


            .. py:attribute:: mortgage_interest_rate
               :type:  float
               :value: None



            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: player_agent_config
               :type:  MonopolyPlayerAgentConfig
               :value: None



            .. py:attribute:: player_names
               :type:  list[str]
               :value: None



            .. py:attribute:: runnable_config
               :type:  langchain_core.runnables.RunnableConfig
               :value: None



            .. py:attribute:: should_visualize_graph
               :type:  bool
               :value: None



            .. py:attribute:: snake_eyes_bonus
               :type:  bool
               :value: None



            .. py:attribute:: starting_money
               :type:  int
               :value: None



            .. py:attribute:: state_schema
               :type:  type[pydantic.BaseModel]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MonopolyPlayerAgentConfig

            Bases: :py:obj:`haive.core.engine.agent.config.AgentConfig`


            Advanced configuration for individual Monopoly player AI agents.

            This class provides comprehensive configuration for AI players, including
            strategic parameters, personality traits, and decision-making preferences.
            The configuration enables realistic player behavior simulation with varying
            skill levels and strategic approaches.

            The configuration supports:
            - Strategic personality profiles for realistic gameplay
            - Risk tolerance and investment preferences
            - Negotiation styles and trading behavior
            - Property development strategies
            - Economic analysis depth and decision speed

            .. attribute:: name

               Unique identifier for the player agent.

               :type: str

            .. attribute:: strategic_personality

               AI personality type affecting decisions.

               :type: Literal

            .. attribute:: risk_tolerance

               Risk preference for investments (0.0-1.0).

               :type: float

            .. attribute:: negotiation_aggressiveness

               Trading aggressiveness (0.0-1.0).

               :type: float

            .. attribute:: property_development_focus

               Whether to prioritize building development.

               :type: bool

            .. attribute:: cash_reserve_preference

               Preferred cash reserve ratio (0.0-1.0).

               :type: float

            .. attribute:: trading_willingness

               Likelihood to engage in trades (0.0-1.0).

               :type: float

            .. attribute:: state_schema

               State schema for decision-making.

               :type: type[BaseModel]

            .. attribute:: input_schema

               Input schema for processing.

               :type: type[BaseModel]

            .. attribute:: output_schema

               Output schema for responses.

               :type: type[BaseModel]

            .. attribute:: engines

               LLM engines for different decision types.

               :type: Dict[str, AugLLMConfig]

            .. rubric:: Examples

            Conservative player configuration::\n

                config = MonopolyPlayerAgentConfig(
                    name="conservative_player",
                    strategic_personality="conservative",
                    risk_tolerance=0.3,
                    cash_reserve_preference=0.4,
                    trading_willingness=0.2
                )

            Aggressive trader configuration::\n

                config = MonopolyPlayerAgentConfig(
                    name="aggressive_trader",
                    strategic_personality="aggressive",
                    risk_tolerance=0.8,
                    negotiation_aggressiveness=0.9,
                    trading_willingness=0.9
                )


            .. py:method:: _classify_player_type() -> str

               Classify player type based on configuration parameters.

               :returns: Player type classification.
               :rtype: str



            .. py:attribute:: cash_reserve_preference
               :type:  float
               :value: None



            .. py:attribute:: engines
               :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
               :value: None



            .. py:attribute:: input_schema
               :type:  type[pydantic.BaseModel]
               :value: None



            .. py:attribute:: model_config


            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: negotiation_aggressiveness
               :type:  float
               :value: None



            .. py:attribute:: output_schema
               :type:  type[pydantic.BaseModel]
               :value: None



            .. py:property:: player_profile
               :type: dict[str, str | float | bool]


               Generate comprehensive player profile summary.

               :returns: Player characteristics and preferences.
               :rtype: Dict[str, Union[str, float, bool]]


            .. py:attribute:: property_development_focus
               :type:  bool
               :value: None



            .. py:attribute:: risk_tolerance
               :type:  float
               :value: None



            .. py:attribute:: state_schema
               :type:  type[pydantic.BaseModel]
               :value: None



            .. py:attribute:: strategic_personality
               :type:  Literal['conservative', 'aggressive', 'balanced', 'opportunistic']
               :value: None



            .. py:attribute:: trading_willingness
               :type:  float
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.monopoly.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

