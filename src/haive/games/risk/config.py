"""Configuration for Risk game.

This module defines configuration settings for the Risk game,
including customizable game rules and parameters.
"""

from pydantic import BaseModel, Field


class RiskConfig(BaseModel):
    """Configuration for the Risk game.

    Defines customizable parameters and rules for the Risk game,
    allowing for different variants and play styles.

    Attributes:
        player_count: Number of players in the game (2-6).
        use_mission_cards: Whether to use mission cards (Risk 2008+ rules).
        allow_card_trade_anytime: Whether players can trade cards at any time.
        escalating_card_values: Whether card set values increase each trade.
        fortify_from_multiple_territories: Whether armies can fortify from multiple connected territories.
        balanced_initial_placement: Whether to use balanced territory distribution.
        reinforce_conquered_territory: Minimum armies to place in a conquered territory.
        dice_sides: Number of sides on the dice used for combat.
        max_attack_dice: Maximum number of dice an attacker can use.
        max_defense_dice: Maximum number of dice a defender can use.
        custom_territories: Optional custom map configuration.
    """

    player_count: int = Field(default=3, ge=2, le=6)
    use_mission_cards: bool = False
    allow_card_trade_anytime: bool = False
    escalating_card_values: bool = True
    fortify_from_multiple_territories: bool = False
    balanced_initial_placement: bool = True
    reinforce_conquered_territory: int = Field(default=1, ge=1)
    dice_sides: int = Field(default=6, ge=4)
    max_attack_dice: int = Field(default=3, ge=1, le=3)
    max_defense_dice: int = Field(default=2, ge=1, le=2)
    custom_territories: dict[str, list[str]] | None = None

    @classmethod
    def classic(cls) -> "RiskConfig":
        """Create a configuration for classic Risk rules.

        Returns:
            A RiskConfig object with classic Risk game settings.
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
        )

    @classmethod
    def modern(cls) -> "RiskConfig":
        """Create a configuration for modern Risk rules (2008+).

        Returns:
            A RiskConfig object with modern Risk game settings.
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
        )
