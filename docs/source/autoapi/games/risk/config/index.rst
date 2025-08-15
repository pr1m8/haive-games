games.risk.config
=================

.. py:module:: games.risk.config

.. autoapi-nested-parse::

   Comprehensive configuration system for Risk game variants and customization.

   This module provides extensive configuration options for the Risk board game,
   supporting classic rules, modern variants, tournament settings, and custom
   rule modifications. The configuration system enables fine-tuned control over
   game mechanics, victory conditions, combat rules, and strategic elements.

   The configuration classes use Pydantic for validation and provide factory
   methods for popular Risk variants including classic Risk, Risk 2210 A.D.,
   Risk: Legacy, and tournament configurations.

   .. rubric:: Examples

   Creating a classic Risk configuration::

       config = RiskConfig.classic()
       game = RiskGame(config)

   Creating a modern Risk configuration::

       config = RiskConfig.modern()
       config.player_count = 4
       config.time_limit_per_turn = 300  # 5 minutes
       game = RiskGame(config)

   Creating a custom tournament configuration::

       config = RiskConfig.tournament()
       config.max_game_duration = 7200  # 2 hours
       config.sudden_death_enabled = True
       game = RiskGame(config)

   Creating a fast-paced variant::

       config = RiskConfig(
           player_count=4,
           escalating_card_values=True,
           fast_reinforcement=True,
           time_limit_per_turn=60,
           blitz_mode=True,
           initial_armies_multiplier=1.5
       )

   Custom map configuration::

       config = RiskConfig.modern()
       config.custom_territories = {
           "North America": ["Alaska", "Northwest Territory", "Greenland"],
           "Europe": ["Iceland", "Great Britain", "Northern Europe"]
       }
       config.custom_continent_bonuses = {
           "North America": 5,
           "Europe": 5
       }

   .. note::

      All configuration classes include comprehensive validation to ensure
      game rule consistency and prevent invalid combinations that would
      break gameplay mechanics.


   .. autolink-examples:: games.risk.config
      :collapse:


Classes
-------

.. autoapisummary::

   games.risk.config.RiskConfig


Module Contents
---------------

.. py:class:: RiskConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive configuration for Risk game variants with extensive customization.

   This configuration class provides complete control over Risk game mechanics,
   supporting classic rules, modern variants, tournament settings, and custom
   modifications. It includes validation for rule consistency and provides
   factory methods for popular Risk variants.

   The configuration system supports:
   - Player count and game scaling options
   - Victory conditions and mission systems
   - Combat mechanics and dice rules
   - Card trading and reinforcement systems
   - Time limits and tournament settings
   - Custom maps and continent configurations
   - AI difficulty and strategic parameters

   .. attribute:: player_count

      Number of players participating (2-6 players).
      Affects initial army distribution and strategic dynamics.

      :type: int

   .. attribute:: use_mission_cards

      Enable mission-based victory conditions.
      Modern Risk variant where players win by completing secret missions.

      :type: bool

   .. attribute:: allow_card_trade_anytime

      Allow card trading outside of turn.
      Strategic variant enabling more flexible resource management.

      :type: bool

   .. attribute:: escalating_card_values

      Increase card set values with each trade.
      Classic mechanic that accelerates late-game army acquisition.

      :type: bool

   .. attribute:: fortify_from_multiple_territories

      Allow multi-source fortification.
      Modern rule enabling armies to move from multiple connected territories.

      :type: bool

   .. attribute:: balanced_initial_placement

      Use balanced territory distribution.
      Ensures fair starting positions by equalizing initial territories.

      :type: bool

   .. attribute:: reinforce_conquered_territory

      Minimum armies in conquered territory.
      Prevents territories from being left completely undefended.

      :type: int

   .. attribute:: dice_sides

      Number of sides on combat dice (4-20 sides).
      Affects combat probability and strategic calculation complexity.

      :type: int

   .. attribute:: max_attack_dice

      Maximum dice an attacker can use (1-5).
      Controls maximum attack strength and combat resolution speed.

      :type: int

   .. attribute:: max_defense_dice

      Maximum dice a defender can use (1-3).
      Balances defensive advantage against attacking forces.

      :type: int

   .. attribute:: custom_territories

      Custom map definition.
      Allows completely custom board layouts and territorial relationships.

      :type: Optional[Dict[str, List[str]]]

   .. attribute:: custom_continent_bonuses

      Bonus armies per continent.
      Defines reinforcement bonuses for controlling entire continents.

      :type: Dict[str, int]

   .. attribute:: initial_armies_multiplier

      Multiplier for starting armies.
      Scales initial army distribution for faster or slower games.

      :type: float

   .. attribute:: time_limit_per_turn

      Turn time limit in seconds.
      Tournament setting to maintain game pace and prevent delays.

      :type: Optional[int]

   .. attribute:: max_game_duration

      Maximum game duration in seconds.
      Prevents excessively long games in competitive settings.

      :type: Optional[int]

   .. attribute:: sudden_death_enabled

      Enable sudden death rules for time limits.
      Tournament rule for decisive game endings when time expires.

      :type: bool

   .. attribute:: blitz_mode

      Enable fast-paced gameplay with reduced phases.
      Accelerated variant with streamlined turn structure.

      :type: bool

   .. attribute:: fast_reinforcement

      Allow immediate reinforcement placement.
      Speeds up gameplay by reducing reinforcement calculation time.

      :type: bool

   .. attribute:: ai_difficulty_scaling

      Scale AI difficulty based on game progress.
      Adaptive AI that becomes more challenging as game progresses.

      :type: bool

   .. attribute:: eliminate_weak_players

      Remove players below threshold strength.
      Tournament rule to maintain competitive balance.

      :type: bool

   .. attribute:: alliance_system_enabled

      Allow formal player alliances.
      Diplomatic variant enabling treaty-based cooperation.

      :type: bool

   .. attribute:: fog_of_war

      Hide enemy army counts and movements.
      Strategic variant increasing uncertainty and intelligence gathering.

      :type: bool

   .. rubric:: Examples

   Standard competitive configuration::

       config = RiskConfig(
           player_count=4,
           use_mission_cards=True,
           escalating_card_values=True,
           time_limit_per_turn=180,
           max_game_duration=5400,  # 90 minutes
           balanced_initial_placement=True
       )

   Fast-paced casual configuration::

       config = RiskConfig(
           player_count=3,
           blitz_mode=True,
           fast_reinforcement=True,
           initial_armies_multiplier=2.0,
           time_limit_per_turn=60
       )

   Strategic depth configuration::

       config = RiskConfig(
           player_count=6,
           alliance_system_enabled=True,
           fog_of_war=True,
           use_mission_cards=True,
           fortify_from_multiple_territories=True
       )

   Custom map configuration::

       config = RiskConfig(
           custom_territories={
               "Fantasy Realm": ["Dragon Kingdom", "Elf Forest", "Dwarf Mountains"],
               "Tech Empire": ["Cyber City", "Robot Factory", "AI Core"]
           },
           custom_continent_bonuses={
               "Fantasy Realm": 4,
               "Tech Empire": 3
           }
       )

   .. note::

      Configuration validation ensures rule consistency and prevents
      invalid combinations that would break game mechanics or create
      unfair advantages.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RiskConfig
      :collapse:

   .. py:method:: blitz() -> RiskConfig
      :classmethod:


      Create a configuration for fast-paced blitz gameplay.

      Generates a configuration designed for quick games with accelerated
      mechanics, increased starting armies, and streamlined phases.
      Perfect for casual play or when time is limited.

      :returns: Pre-configured instance for blitz Risk gameplay.
      :rtype: RiskConfig

      .. rubric:: Examples

      Creating a blitz Risk game::

          config = RiskConfig.blitz()
          game = RiskGame(config)

          # Results in:
          # - 3-player fast setup
          # - 50% more starting armies
          # - 1-minute turn limits
          # - Blitz mode enabled
          # - Fast reinforcement
          # - Modern flexible rules

      .. note::

         Blitz configuration typically results in 30-45 minute games
         with high action and strategic decision-making under time pressure.


      .. autolink-examples:: blitz
         :collapse:


   .. py:method:: classic() -> RiskConfig
      :classmethod:


      Create a configuration for classic Risk rules (1959-1993).

      Generates the original Risk configuration with traditional rules,
      unbalanced initial placement, and total conquest victory conditions.
      This configuration emphasizes the original gameplay experience with
      all the strategic depth and potential imbalances of the classic game.

      :returns: Pre-configured instance for classic Risk gameplay.
      :rtype: RiskConfig

      .. rubric:: Examples

      Creating a classic Risk game::

          config = RiskConfig.classic()
          game = RiskGame(config)

          # Results in:
          # - Traditional 3-player setup
          # - Total conquest victory (no missions)
          # - Turn-based card trading only
          # - Escalating card values
          # - Single-territory fortification
          # - Unbalanced initial placement (random)
          # - Standard 6-sided dice combat

      .. note::

         Classic rules can lead to longer games and potential player
         elimination early in the game due to unbalanced starting positions.


      .. autolink-examples:: classic
         :collapse:


   .. py:method:: modern() -> RiskConfig
      :classmethod:


      Create a configuration for modern Risk rules (2008+).

      Generates the contemporary Risk configuration with mission cards,
      flexible trading, balanced placement, and quality-of-life improvements.
      This configuration emphasizes fair gameplay and reduced game length
      through mission-based victory conditions.

      :returns: Pre-configured instance for modern Risk gameplay.
      :rtype: RiskConfig

      .. rubric:: Examples

      Creating a modern Risk game::

          config = RiskConfig.modern()
          config.player_count = 4  # Customize player count
          game = RiskGame(config)

          # Results in:
          # - Mission-based victory conditions
          # - Flexible card trading anytime
          # - Multi-territory fortification
          # - Balanced initial placement
          # - Escalating card values
          # - Standard combat mechanics

      .. note::

         Modern rules generally result in shorter, more balanced games
         with multiple viable victory paths through mission completion.


      .. autolink-examples:: modern
         :collapse:


   .. py:method:: strategic() -> RiskConfig
      :classmethod:


      Create a configuration for deep strategic gameplay.

      Generates a configuration emphasizing strategic depth with alliances,
      fog of war, and complex diplomatic interactions. Designed for
      experienced players who enjoy intricate strategic planning.

      :returns: Pre-configured instance for strategic Risk gameplay.
      :rtype: RiskConfig

      .. rubric:: Examples

      Creating a strategic Risk game::

          config = RiskConfig.strategic()
          game = RiskGame(config)

          # Results in:
          # - 6-player maximum complexity
          # - Alliance system enabled
          # - Fog of war for uncertainty
          # - Mission-based victory
          # - Flexible trading and fortification
          # - Adaptive AI difficulty

      .. note::

         Strategic configuration can result in longer games (2-4 hours)
         with complex diplomatic interactions and shifting alliances.


      .. autolink-examples:: strategic
         :collapse:


   .. py:method:: tournament() -> RiskConfig
      :classmethod:


      Create a configuration for competitive tournament play.

      Generates a configuration optimized for tournament settings with
      time limits, balanced rules, and provisions for decisive game endings.
      This configuration ensures fair competition and manageable game duration.

      :returns: Pre-configured instance for tournament Risk gameplay.
      :rtype: RiskConfig

      .. rubric:: Examples

      Creating a tournament Risk game::

          config = RiskConfig.tournament()
          game = RiskGame(config)

          # Results in:
          # - 4-player balanced setup
          # - 3-minute turn time limits
          # - 2-hour maximum game duration
          # - Sudden death rules enabled
          # - Mission-based victory
          # - Balanced initial placement
          # - Fast reinforcement for efficiency

      .. note::

         Tournament configuration prioritizes fairness, time management,
         and decisive game endings for competitive play environments.


      .. autolink-examples:: tournament
         :collapse:


   .. py:method:: validate_configuration() -> list[str]

      Validate configuration for internal consistency and game balance.

      :returns: List of validation warnings or errors. Empty list means valid.
      :rtype: List[str]

      .. rubric:: Examples

      Checking configuration validity::

          config = RiskConfig(...)
          issues = config.validate_configuration()

          if issues:
              for issue in issues:
                  print(f"Warning: {issue}")
          else:
              print("Configuration is valid")


      .. autolink-examples:: validate_configuration
         :collapse:


   .. py:method:: validate_continent_bonuses(v: dict[str, int]) -> dict[str, int]
      :classmethod:


      Validate continent bonus configuration.

      :param v: Continent bonuses to validate.
      :type v: Dict[str, int]

      :returns: Validated continent bonuses.
      :rtype: Dict[str, int]

      :raises ValueError: If bonus configuration is invalid.


      .. autolink-examples:: validate_continent_bonuses
         :collapse:


   .. py:method:: validate_custom_territories(v: dict[str, list[str]] | None) -> dict[str, list[str]] | None
      :classmethod:


      Validate custom territory configuration.

      :param v: Custom territories to validate.
      :type v: Optional[Dict[str, List[str]]]

      :returns: Validated territories.
      :rtype: Optional[Dict[str, List[str]]]

      :raises ValueError: If territory configuration is invalid.


      .. autolink-examples:: validate_custom_territories
         :collapse:


   .. py:attribute:: ai_difficulty_scaling
      :type:  bool
      :value: None



   .. py:attribute:: alliance_system_enabled
      :type:  bool
      :value: None



   .. py:attribute:: allow_card_trade_anytime
      :type:  bool
      :value: None



   .. py:attribute:: balanced_initial_placement
      :type:  bool
      :value: None



   .. py:attribute:: blitz_mode
      :type:  bool
      :value: None



   .. py:property:: complexity_level
      :type: str


      Calculate game complexity level based on enabled features.

      :returns: Complexity level ("Beginner", "Intermediate", "Advanced", "Expert").
      :rtype: str

      .. rubric:: Examples

      Checking complexity::

          config = RiskConfig.classic()
          complexity = config.complexity_level
          print(f"Game complexity: {complexity}")  # "Intermediate"

      .. autolink-examples:: complexity_level
         :collapse:


   .. py:attribute:: custom_continent_bonuses
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: custom_territories
      :type:  dict[str, list[str]] | None
      :value: None



   .. py:attribute:: dice_sides
      :type:  int
      :value: None



   .. py:attribute:: eliminate_weak_players
      :type:  bool
      :value: None



   .. py:attribute:: escalating_card_values
      :type:  bool
      :value: None



   .. py:property:: estimated_game_duration
      :type: str


      Estimate game duration based on configuration settings.

      :returns: Estimated duration range (e.g., "45-90 minutes").
      :rtype: str

      .. rubric:: Examples

      Checking estimated duration::

          config = RiskConfig.blitz()
          duration = config.estimated_game_duration
          print(f"Expected game time: {duration}")  # "30-60 minutes"

      .. autolink-examples:: estimated_game_duration
         :collapse:


   .. py:attribute:: fast_reinforcement
      :type:  bool
      :value: None



   .. py:attribute:: fog_of_war
      :type:  bool
      :value: None



   .. py:attribute:: fortify_from_multiple_territories
      :type:  bool
      :value: None



   .. py:attribute:: initial_armies_multiplier
      :type:  float
      :value: None



   .. py:attribute:: max_attack_dice
      :type:  int
      :value: None



   .. py:attribute:: max_defense_dice
      :type:  int
      :value: None



   .. py:attribute:: max_game_duration
      :type:  int | None
      :value: None



   .. py:attribute:: player_count
      :type:  int
      :value: None



   .. py:attribute:: reinforce_conquered_territory
      :type:  int
      :value: None



   .. py:attribute:: sudden_death_enabled
      :type:  bool
      :value: None



   .. py:attribute:: time_limit_per_turn
      :type:  int | None
      :value: None



   .. py:attribute:: use_mission_cards
      :type:  bool
      :value: None



