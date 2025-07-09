"""Comprehensive configuration system for Risk game variants and customization.

This module provides extensive configuration options for the Risk board game,
supporting classic rules, modern variants, tournament settings, and custom
rule modifications. The configuration system enables fine-tuned control over
game mechanics, victory conditions, combat rules, and strategic elements.

The configuration classes use Pydantic for validation and provide factory
methods for popular Risk variants including classic Risk, Risk 2210 A.D.,
Risk: Legacy, and tournament configurations.

Examples:
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

Note:
    All configuration classes include comprehensive validation to ensure
    game rule consistency and prevent invalid combinations that would
    break gameplay mechanics.
"""

from typing import Dict, List, Optional

from pydantic import BaseModel, Field, computed_field, field_validator


class RiskConfig(BaseModel):
    """Comprehensive configuration for Risk game variants with extensive customization.

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

    Attributes:
        player_count (int): Number of players participating (2-6 players).
            Affects initial army distribution and strategic dynamics.
        use_mission_cards (bool): Enable mission-based victory conditions.
            Modern Risk variant where players win by completing secret missions.
        allow_card_trade_anytime (bool): Allow card trading outside of turn.
            Strategic variant enabling more flexible resource management.
        escalating_card_values (bool): Increase card set values with each trade.
            Classic mechanic that accelerates late-game army acquisition.
        fortify_from_multiple_territories (bool): Allow multi-source fortification.
            Modern rule enabling armies to move from multiple connected territories.
        balanced_initial_placement (bool): Use balanced territory distribution.
            Ensures fair starting positions by equalizing initial territories.
        reinforce_conquered_territory (int): Minimum armies in conquered territory.
            Prevents territories from being left completely undefended.
        dice_sides (int): Number of sides on combat dice (4-20 sides).
            Affects combat probability and strategic calculation complexity.
        max_attack_dice (int): Maximum dice an attacker can use (1-5).
            Controls maximum attack strength and combat resolution speed.
        max_defense_dice (int): Maximum dice a defender can use (1-3).
            Balances defensive advantage against attacking forces.
        custom_territories (Optional[Dict[str, List[str]]]): Custom map definition.
            Allows completely custom board layouts and territorial relationships.
        custom_continent_bonuses (Dict[str, int]): Bonus armies per continent.
            Defines reinforcement bonuses for controlling entire continents.
        initial_armies_multiplier (float): Multiplier for starting armies.
            Scales initial army distribution for faster or slower games.
        time_limit_per_turn (Optional[int]): Turn time limit in seconds.
            Tournament setting to maintain game pace and prevent delays.
        max_game_duration (Optional[int]): Maximum game duration in seconds.
            Prevents excessively long games in competitive settings.
        sudden_death_enabled (bool): Enable sudden death rules for time limits.
            Tournament rule for decisive game endings when time expires.
        blitz_mode (bool): Enable fast-paced gameplay with reduced phases.
            Accelerated variant with streamlined turn structure.
        fast_reinforcement (bool): Allow immediate reinforcement placement.
            Speeds up gameplay by reducing reinforcement calculation time.
        ai_difficulty_scaling (bool): Scale AI difficulty based on game progress.
            Adaptive AI that becomes more challenging as game progresses.
        eliminate_weak_players (bool): Remove players below threshold strength.
            Tournament rule to maintain competitive balance.
        alliance_system_enabled (bool): Allow formal player alliances.
            Diplomatic variant enabling treaty-based cooperation.
        fog_of_war (bool): Hide enemy army counts and movements.
            Strategic variant increasing uncertainty and intelligence gathering.

    Examples:
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

    Note:
        Configuration validation ensures rule consistency and prevents
        invalid combinations that would break game mechanics or create
        unfair advantages.
    """

    # Core game settings
    player_count: int = Field(
        default=3,
        ge=2,
        le=6,
        description="Number of players participating in the game (2-6)",
        examples=[2, 3, 4, 5, 6],
    )

    # Victory and mission systems
    use_mission_cards: bool = Field(
        default=False,
        description="Enable mission-based victory conditions instead of total conquest",
        examples=[True, False],
    )

    # Card and resource management
    allow_card_trade_anytime: bool = Field(
        default=False,
        description="Allow players to trade cards outside of their turn",
        examples=[True, False],
    )

    escalating_card_values: bool = Field(
        default=True,
        description="Increase card set values with each successive trade",
        examples=[True, False],
    )

    # Movement and fortification
    fortify_from_multiple_territories: bool = Field(
        default=False,
        description="Allow armies to move from multiple connected territories during fortification",
        examples=[True, False],
    )

    # Initial setup
    balanced_initial_placement: bool = Field(
        default=True,
        description="Use balanced territory distribution for fair starting positions",
        examples=[True, False],
    )

    initial_armies_multiplier: float = Field(
        default=1.0,
        ge=0.5,
        le=3.0,
        description="Multiplier for starting army distribution (0.5-3.0)",
        examples=[0.5, 1.0, 1.5, 2.0],
    )

    # Combat mechanics
    reinforce_conquered_territory: int = Field(
        default=1,
        ge=1,
        le=5,
        description="Minimum armies that must be placed in a newly conquered territory",
        examples=[1, 2, 3],
    )

    dice_sides: int = Field(
        default=6,
        ge=4,
        le=20,
        description="Number of sides on combat dice (affects probability calculations)",
        examples=[4, 6, 8, 10, 12, 20],
    )

    max_attack_dice: int = Field(
        default=3,
        ge=1,
        le=5,
        description="Maximum number of dice an attacker can use in combat",
        examples=[1, 2, 3, 4, 5],
    )

    max_defense_dice: int = Field(
        default=2,
        ge=1,
        le=3,
        description="Maximum number of dice a defender can use in combat",
        examples=[1, 2, 3],
    )

    # Custom map and territories
    custom_territories: Optional[Dict[str, List[str]]] = Field(
        default=None,
        description="Custom map definition with continent-territory mappings",
        examples=[
            {"North America": ["Alaska", "Canada", "USA"]},
            {"Fantasy Realm": ["Dragon Kingdom", "Elf Forest"]},
        ],
    )

    custom_continent_bonuses: Dict[str, int] = Field(
        default_factory=dict,
        description="Bonus armies awarded for controlling entire continents",
        examples=[
            {"North America": 5, "Europe": 5, "Asia": 7},
            {"Fantasy Realm": 4, "Tech Empire": 3},
        ],
    )

    # Timing and tournament settings
    time_limit_per_turn: Optional[int] = Field(
        default=None,
        ge=30,
        le=1800,
        description="Time limit per turn in seconds (30-1800 seconds, None for unlimited)",
        examples=[60, 120, 300, 600, None],
    )

    max_game_duration: Optional[int] = Field(
        default=None,
        ge=600,
        le=21600,
        description="Maximum game duration in seconds (10 minutes to 6 hours)",
        examples=[3600, 5400, 7200, None],  # 1, 1.5, 2 hours
    )

    sudden_death_enabled: bool = Field(
        default=False,
        description="Enable sudden death rules when time limits are reached",
        examples=[True, False],
    )

    # Gameplay variants
    blitz_mode: bool = Field(
        default=False,
        description="Enable fast-paced gameplay with streamlined phases",
        examples=[True, False],
    )

    fast_reinforcement: bool = Field(
        default=False,
        description="Allow immediate reinforcement placement without calculation delays",
        examples=[True, False],
    )

    # AI and difficulty settings
    ai_difficulty_scaling: bool = Field(
        default=False,
        description="Scale AI difficulty dynamically based on game progress",
        examples=[True, False],
    )

    eliminate_weak_players: bool = Field(
        default=False,
        description="Remove players below minimum strength threshold",
        examples=[True, False],
    )

    # Strategic variants
    alliance_system_enabled: bool = Field(
        default=False,
        description="Allow formal player alliances and treaty agreements",
        examples=[True, False],
    )

    fog_of_war: bool = Field(
        default=False,
        description="Hide enemy army counts and movements for strategic uncertainty",
        examples=[True, False],
    )

    @field_validator("custom_territories")
    @classmethod
    def validate_custom_territories(
        cls, v: Optional[Dict[str, List[str]]]
    ) -> Optional[Dict[str, List[str]]]:
        """Validate custom territory configuration.

        Args:
            v (Optional[Dict[str, List[str]]]): Custom territories to validate.

        Returns:
            Optional[Dict[str, List[str]]]: Validated territories.

        Raises:
            ValueError: If territory configuration is invalid.
        """
        if v is None:
            return v

        if not isinstance(v, dict):
            raise ValueError("Custom territories must be a dictionary")

        total_territories = 0
        for continent, territories in v.items():
            if not isinstance(continent, str) or not continent.strip():
                raise ValueError("Continent names must be non-empty strings")

            if not isinstance(territories, list) or len(territories) == 0:
                raise ValueError(
                    f"Continent '{continent}' must have at least one territory"
                )

            for territory in territories:
                if not isinstance(territory, str) or not territory.strip():
                    raise ValueError(
                        f"Territory names in '{continent}' must be non-empty strings"
                    )

            total_territories += len(territories)

        if total_territories < 10:
            raise ValueError(
                "Custom map must have at least 10 territories for viable gameplay"
            )

        return v

    @field_validator("custom_continent_bonuses")
    @classmethod
    def validate_continent_bonuses(cls, v: Dict[str, int]) -> Dict[str, int]:
        """Validate continent bonus configuration.

        Args:
            v (Dict[str, int]): Continent bonuses to validate.

        Returns:
            Dict[str, int]: Validated continent bonuses.

        Raises:
            ValueError: If bonus configuration is invalid.
        """
        for continent, bonus in v.items():
            if not isinstance(continent, str) or not continent.strip():
                raise ValueError("Continent names must be non-empty strings")

            if not isinstance(bonus, int) or bonus < 1 or bonus > 20:
                raise ValueError(
                    f"Continent '{continent}' bonus must be between 1 and 20"
                )

        return v

    @classmethod
    def classic(cls) -> "RiskConfig":
        """Create a configuration for classic Risk rules (1959-1993).

        Generates the original Risk configuration with traditional rules,
        unbalanced initial placement, and total conquest victory conditions.
        This configuration emphasizes the original gameplay experience with
        all the strategic depth and potential imbalances of the classic game.

        Returns:
            RiskConfig: Pre-configured instance for classic Risk gameplay.

        Examples:
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

        Note:
            Classic rules can lead to longer games and potential player
            elimination early in the game due to unbalanced starting positions.
        """
        return cls(
            player_count=3,
            use_mission_cards=False,
            allow_card_trade_anytime=False,
            escalating_card_values=True,
            fortify_from_multiple_territories=False,
            balanced_initial_placement=False,
            reinforce_conquered_territory=1,
            dice_sides=6,
            max_attack_dice=3,
            max_defense_dice=2,
            initial_armies_multiplier=1.0,
            blitz_mode=False,
            fast_reinforcement=False,
        )

    @classmethod
    def modern(cls) -> "RiskConfig":
        """Create a configuration for modern Risk rules (2008+).

        Generates the contemporary Risk configuration with mission cards,
        flexible trading, balanced placement, and quality-of-life improvements.
        This configuration emphasizes fair gameplay and reduced game length
        through mission-based victory conditions.

        Returns:
            RiskConfig: Pre-configured instance for modern Risk gameplay.

        Examples:
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

        Note:
            Modern rules generally result in shorter, more balanced games
            with multiple viable victory paths through mission completion.
        """
        return cls(
            player_count=3,
            use_mission_cards=True,
            allow_card_trade_anytime=True,
            escalating_card_values=True,
            fortify_from_multiple_territories=True,
            balanced_initial_placement=True,
            reinforce_conquered_territory=1,
            dice_sides=6,
            max_attack_dice=3,
            max_defense_dice=2,
            initial_armies_multiplier=1.0,
            blitz_mode=False,
            fast_reinforcement=True,
        )

    @classmethod
    def tournament(cls) -> "RiskConfig":
        """Create a configuration for competitive tournament play.

        Generates a configuration optimized for tournament settings with
        time limits, balanced rules, and provisions for decisive game endings.
        This configuration ensures fair competition and manageable game duration.

        Returns:
            RiskConfig: Pre-configured instance for tournament Risk gameplay.

        Examples:
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

        Note:
            Tournament configuration prioritizes fairness, time management,
            and decisive game endings for competitive play environments.
        """
        return cls(
            player_count=4,
            use_mission_cards=True,
            allow_card_trade_anytime=True,
            escalating_card_values=True,
            fortify_from_multiple_territories=True,
            balanced_initial_placement=True,
            time_limit_per_turn=180,  # 3 minutes
            max_game_duration=7200,  # 2 hours
            sudden_death_enabled=True,
            fast_reinforcement=True,
            eliminate_weak_players=True,
        )

    @classmethod
    def blitz(cls) -> "RiskConfig":
        """Create a configuration for fast-paced blitz gameplay.

        Generates a configuration designed for quick games with accelerated
        mechanics, increased starting armies, and streamlined phases.
        Perfect for casual play or when time is limited.

        Returns:
            RiskConfig: Pre-configured instance for blitz Risk gameplay.

        Examples:
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

        Note:
            Blitz configuration typically results in 30-45 minute games
            with high action and strategic decision-making under time pressure.
        """
        return cls(
            player_count=3,
            use_mission_cards=True,
            allow_card_trade_anytime=True,
            escalating_card_values=True,
            fortify_from_multiple_territories=True,
            balanced_initial_placement=True,
            initial_armies_multiplier=1.5,
            time_limit_per_turn=60,  # 1 minute
            blitz_mode=True,
            fast_reinforcement=True,
        )

    @classmethod
    def strategic(cls) -> "RiskConfig":
        """Create a configuration for deep strategic gameplay.

        Generates a configuration emphasizing strategic depth with alliances,
        fog of war, and complex diplomatic interactions. Designed for
        experienced players who enjoy intricate strategic planning.

        Returns:
            RiskConfig: Pre-configured instance for strategic Risk gameplay.

        Examples:
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

        Note:
            Strategic configuration can result in longer games (2-4 hours)
            with complex diplomatic interactions and shifting alliances.
        """
        return cls(
            player_count=6,
            use_mission_cards=True,
            allow_card_trade_anytime=True,
            escalating_card_values=True,
            fortify_from_multiple_territories=True,
            balanced_initial_placement=True,
            alliance_system_enabled=True,
            fog_of_war=True,
            ai_difficulty_scaling=True,
            time_limit_per_turn=300,  # 5 minutes for complex decisions
        )

    @computed_field
    @property
    def estimated_game_duration(self) -> str:
        """Estimate game duration based on configuration settings.

        Returns:
            str: Estimated duration range (e.g., "45-90 minutes").

        Examples:
            Checking estimated duration::

                config = RiskConfig.blitz()
                duration = config.estimated_game_duration
                print(f"Expected game time: {duration}")  # "30-60 minutes"
        """
        base_minutes = 60  # Base game duration

        # Adjust for player count
        base_minutes += (self.player_count - 2) * 20

        # Adjust for game mode
        if self.blitz_mode:
            base_minutes *= 0.5
        elif self.use_mission_cards:
            base_minutes *= 0.8
        elif not self.balanced_initial_placement:
            base_minutes *= 1.3  # Classic can run longer

        # Adjust for variants
        if self.alliance_system_enabled:
            base_minutes *= 1.4
        if self.fog_of_war:
            base_minutes *= 1.2
        if self.fast_reinforcement:
            base_minutes *= 0.9

        # Calculate range
        min_duration = int(base_minutes * 0.7)
        max_duration = int(base_minutes * 1.5)

        return f"{min_duration}-{max_duration} minutes"

    @computed_field
    @property
    def complexity_level(self) -> str:
        """Calculate game complexity level based on enabled features.

        Returns:
            str: Complexity level ("Beginner", "Intermediate", "Advanced", "Expert").

        Examples:
            Checking complexity::

                config = RiskConfig.classic()
                complexity = config.complexity_level
                print(f"Game complexity: {complexity}")  # "Intermediate"
        """
        complexity_score = 0

        # Base complexity factors
        complexity_score += self.player_count  # More players = more complex

        # Rule complexity
        if self.use_mission_cards:
            complexity_score += 2
        if self.alliance_system_enabled:
            complexity_score += 3
        if self.fog_of_war:
            complexity_score += 2
        if self.fortify_from_multiple_territories:
            complexity_score += 1
        if self.allow_card_trade_anytime:
            complexity_score += 1

        # Simplifying factors
        if self.blitz_mode:
            complexity_score -= 2
        if self.fast_reinforcement:
            complexity_score -= 1
        if self.balanced_initial_placement:
            complexity_score -= 1

        # Determine complexity level
        if complexity_score <= 4:
            return "Beginner"
        elif complexity_score <= 8:
            return "Intermediate"
        elif complexity_score <= 12:
            return "Advanced"
        else:
            return "Expert"

    def validate_configuration(self) -> List[str]:
        """Validate configuration for internal consistency and game balance.

        Returns:
            List[str]: List of validation warnings or errors. Empty list means valid.

        Examples:
            Checking configuration validity::

                config = RiskConfig(...)
                issues = config.validate_configuration()

                if issues:
                    for issue in issues:
                        print(f"Warning: {issue}")
                else:
                    print("Configuration is valid")
        """
        issues = []

        # Check time limit consistency
        if self.time_limit_per_turn and self.max_game_duration:
            min_turns_needed = self.player_count * 10  # Minimum realistic turns
            total_turn_time = min_turns_needed * self.time_limit_per_turn

            if total_turn_time > self.max_game_duration:
                issues.append(
                    f"Turn time limits may not allow sufficient game time: "
                    f"{total_turn_time}s needed vs {self.max_game_duration}s maximum"
                )

        # Check dice configuration
        if self.max_attack_dice > self.max_defense_dice + 2:
            issues.append(
                "Attack dice significantly exceed defense dice - may create imbalance"
            )

        # Check custom territory configuration
        if self.custom_territories:
            territory_count = sum(
                len(territories) for territories in self.custom_territories.values()
            )
            expected_min = self.player_count * 3  # Minimum territories per player

            if territory_count < expected_min:
                issues.append(
                    f"Custom map may be too small: {territory_count} territories "
                    f"for {self.player_count} players (minimum recommended: {expected_min})"
                )

        # Check blitz mode compatibility
        if self.blitz_mode and self.fog_of_war:
            issues.append(
                "Blitz mode with fog of war may create confusion due to rapid pace"
            )

        # Check alliance system with high player count
        if self.alliance_system_enabled and self.player_count < 4:
            issues.append("Alliance system is most effective with 4+ players")

        return issues
