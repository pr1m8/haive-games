"""Test cases for Risk game models.

This module tests all the data models and enums used in the Risk game,
ensuring they behave correctly and validate input properly.
"""

from pydantic import ValidationError
import pytest

from haive.games.risk.models import (
    Card,
    CardType,
    Continent,
    GameStatus,
    MoveType,
    PhaseType,
    Player,
    RiskAnalysis,
    RiskMove,
    Territory,
)


class TestCardType:
    """Test cases for CardType enum."""

    def test_card_type_values(self) -> None:
        """Test that CardType enum has correct values."""
        assert CardType.INFANTRY == "infantry"
        assert CardType.CAVALRY == "cavalry"
        assert CardType.ARTILLERY == "artillery"
        assert CardType.WILD == "wild"

    def test_card_type_string_representation(self) -> None:
        """Test CardType string representation."""
        assert str(CardType.INFANTRY) == "infantry"
        assert str(CardType.CAVALRY) == "cavalry"
        assert str(CardType.ARTILLERY) == "artillery"
        assert str(CardType.WILD) == "wild"


class TestCard:
    """Test cases for Card model."""

    def test_card_creation_with_territory(self) -> None:
        """Test creating a card with territory name."""
        card = Card(card_type=CardType.INFANTRY, territory_name="Alaska")
        assert card.card_type == CardType.INFANTRY
        assert card.territory_name == "Alaska"

    def test_card_creation_without_territory(self) -> None:
        """Test creating a card without territory name."""
        card = Card(card_type=CardType.WILD)
        assert card.card_type == CardType.WILD
        assert card.territory_name is None

    def test_card_string_representation_with_territory(self) -> None:
        """Test Card string representation with territory."""
        card = Card(card_type=CardType.CAVALRY, territory_name="Brazil")
        assert str(card) == "Cavalry (Brazil)"

    def test_card_string_representation_without_territory(self) -> None:
        """Test Card string representation without territory."""
        card = Card(card_type=CardType.WILD)
        assert str(card) == "Wild"

    def test_card_validation_invalid_type(self) -> None:
        """Test that invalid card types raise validation error."""
        with pytest.raises(ValidationError):
            Card(card_type="invalid_type")


class TestTerritory:
    """Test cases for Territory model."""

    def test_territory_creation_basic(self) -> None:
        """Test creating a basic territory."""
        territory = Territory(name="Alaska", continent="North America")
        assert territory.name == "Alaska"
        assert territory.continent == "North America"
        assert territory.owner is None
        assert territory.armies == 0
        assert territory.adjacent == []

    def test_territory_creation_with_all_fields(self) -> None:
        """Test creating a territory with all fields."""
        adjacent = ["Alberta", "Northwest Territory"]
        territory = Territory(
            name="Alaska",
            continent="North America",
            owner="Player1",
            armies=3,
            adjacent=adjacent,
        )
        assert territory.name == "Alaska"
        assert territory.continent == "North America"
        assert territory.owner == "Player1"
        assert territory.armies == 3
        assert territory.adjacent == adjacent

    def test_territory_string_representation_with_owner(self) -> None:
        """Test Territory string representation with owner."""
        territory = Territory(
            name="Alaska", continent="North America", owner="Player1", armies=5
        )
        assert str(territory) == "Alaska (Player1, 5 armies)"

    def test_territory_string_representation_without_owner(self) -> None:
        """Test Territory string representation without owner."""
        territory = Territory(name="Alaska", continent="North America", armies=2)
        assert str(territory) == "Alaska (Unoccupied, 2 armies)"


class TestContinent:
    """Test cases for Continent model."""

    def test_continent_creation_basic(self) -> None:
        """Test creating a basic continent."""
        continent = Continent(name="North America", bonus=5)
        assert continent.name == "North America"
        assert continent.bonus == 5
        assert continent.territories == []

    def test_continent_creation_with_territories(self) -> None:
        """Test creating a continent with territories."""
        territories = ["Alaska", "Alberta", "Quebec"]
        continent = Continent(name="North America", bonus=5, territories=territories)
        assert continent.name == "North America"
        assert continent.bonus == 5
        assert continent.territories == territories

    def test_continent_string_representation(self) -> None:
        """Test Continent string representation."""
        continent = Continent(name="Europe", bonus=5)
        assert str(continent) == "Europe (Bonus: 5)"


class TestPlayer:
    """Test cases for Player model."""

    def test_player_creation_basic(self) -> None:
        """Test creating a basic player."""
        player = Player(name="TestPlayer")
        assert player.name == "TestPlayer"
        assert player.cards == []
        assert player.unplaced_armies == 0
        assert player.eliminated is False

    def test_player_creation_with_all_fields(self) -> None:
        """Test creating a player with all fields."""
        cards = [Card(card_type=CardType.INFANTRY)]
        player = Player(
            name="TestPlayer", cards=cards, unplaced_armies=10, eliminated=True
        )
        assert player.name == "TestPlayer"
        assert player.cards == cards
        assert player.unplaced_armies == 10
        assert player.eliminated is True

    def test_player_string_representation_active(self) -> None:
        """Test Player string representation when active."""
        cards = [Card(card_type=CardType.CAVALRY), Card(card_type=CardType.WILD)]
        player = Player(name="TestPlayer", cards=cards, unplaced_armies=5)
        assert str(player) == "TestPlayer (Active, 5 unplaced armies, 2 cards)"

    def test_player_string_representation_eliminated(self) -> None:
        """Test Player string representation when eliminated."""
        player = Player(name="TestPlayer", eliminated=True)
        assert str(player) == "TestPlayer (Eliminated, 0 unplaced armies, 0 cards)"


class TestMoveType:
    """Test cases for MoveType enum."""

    def test_move_type_values(self) -> None:
        """Test that MoveType enum has correct values."""
        assert MoveType.PLACE_ARMIES == "place_armies"
        assert MoveType.ATTACK == "attack"
        assert MoveType.FORTIFY == "fortify"
        assert MoveType.TRADE_CARDS == "trade_cards"


class TestRiskMove:
    """Test cases for RiskMove model."""

    def test_risk_move_place_armies(self) -> None:
        """Test creating a place armies move."""
        move = RiskMove(
            move_type=MoveType.PLACE_ARMIES,
            player="Player1",
            to_territory="Alaska",
            armies=3,
        )
        assert move.move_type == MoveType.PLACE_ARMIES
        assert move.player == "Player1"
        assert move.to_territory == "Alaska"
        assert move.armies == 3
        assert str(move) == "Player1 places 3 armies on Alaska"

    def test_risk_move_attack(self) -> None:
        """Test creating an attack move."""
        move = RiskMove(
            move_type=MoveType.ATTACK,
            player="Player1",
            from_territory="Alaska",
            to_territory="Alberta",
            attack_dice=2,
        )
        assert move.move_type == MoveType.ATTACK
        assert move.player == "Player1"
        assert move.from_territory == "Alaska"
        assert move.to_territory == "Alberta"
        assert move.attack_dice == 2
        assert str(move) == "Player1 attacks from Alaska to Alberta with 2 dice"

    def test_risk_move_fortify(self) -> None:
        """Test creating a fortify move."""
        move = RiskMove(
            move_type=MoveType.FORTIFY,
            player="Player1",
            from_territory="Alaska",
            to_territory="Alberta",
            armies=2,
        )
        assert move.move_type == MoveType.FORTIFY
        assert move.player == "Player1"
        assert move.from_territory == "Alaska"
        assert move.to_territory == "Alberta"
        assert move.armies == 2
        assert str(move) == "Player1 fortifies Alberta with 2 armies from Alaska"

    def test_risk_move_trade_cards(self) -> None:
        """Test creating a trade cards move."""
        cards = [
            Card(card_type=CardType.INFANTRY),
            Card(card_type=CardType.CAVALRY),
            Card(card_type=CardType.ARTILLERY),
        ]
        move = RiskMove(move_type=MoveType.TRADE_CARDS, player="Player1", cards=cards)
        assert move.move_type == MoveType.TRADE_CARDS
        assert move.player == "Player1"
        assert move.cards == cards
        expected_str = "Player1 trades in cards: Infantry, Cavalry, Artillery"
        assert str(move) == expected_str


class TestPhaseType:
    """Test cases for PhaseType enum."""

    def test_phase_type_values(self) -> None:
        """Test that PhaseType enum has correct values."""
        assert PhaseType.SETUP == "setup"
        assert PhaseType.REINFORCE == "reinforce"
        assert PhaseType.ATTACK == "attack"
        assert PhaseType.FORTIFY == "fortify"
        assert PhaseType.GAME_OVER == "game_over"


class TestGameStatus:
    """Test cases for GameStatus enum."""

    def test_game_status_values(self) -> None:
        """Test that GameStatus enum has correct values."""
        assert GameStatus.IN_PROGRESS == "in_progress"
        assert GameStatus.FINISHED == "finished"


class TestRiskAnalysis:
    """Test cases for RiskAnalysis model."""

    def test_risk_analysis_creation(self) -> None:
        """Test creating a RiskAnalysis object."""
        move = RiskMove(
            move_type=MoveType.PLACE_ARMIES,
            player="Player1",
            to_territory="Alaska",
            armies=1,
        )
        analysis = RiskAnalysis(
            player="Player1",
            controlled_continents=["North America"],
            controlled_territories=9,
            total_armies=25,
            position_evaluation="winning",
            recommended_move=move,
            explanation="Control of North America provides strong position",
        )

        assert analysis.player == "Player1"
        assert analysis.controlled_continents == ["North America"]
        assert analysis.controlled_territories == 9
        assert analysis.total_armies == 25
        assert analysis.position_evaluation == "winning"
        assert analysis.recommended_move == move
        assert "Control of North America" in analysis.explanation

    def test_risk_analysis_string_representation(self) -> None:
        """Test RiskAnalysis string representation."""
        move = RiskMove(
            move_type=MoveType.ATTACK,
            player="Player1",
            from_territory="Alaska",
            to_territory="Alberta",
            attack_dice=1,
        )
        analysis = RiskAnalysis(
            player="Player1",
            controlled_continents=["Australia"],
            controlled_territories=4,
            total_armies=12,
            position_evaluation="neutral",
            recommended_move=move,
            explanation="Focus on expanding in Asia",
        )

        result = str(analysis)
        assert "Analysis for Player1:" in result
        assert "Controlled continents: Australia" in result
        assert "Controlled territories: 4" in result
        assert "Total armies: 12" in result
        assert "Position evaluation: neutral" in result
        assert "Focus on expanding in Asia" in result

    def test_risk_analysis_empty_continents(self) -> None:
        """Test RiskAnalysis with no controlled continents."""
        move = RiskMove(
            move_type=MoveType.FORTIFY,
            player="Player1",
            from_territory="Alaska",
            to_territory="Alberta",
            armies=1,
        )
        analysis = RiskAnalysis(
            player="Player1",
            controlled_continents=[],
            controlled_territories=3,
            total_armies=8,
            position_evaluation="losing",
            recommended_move=move,
            explanation="Need to focus on defense",
        )

        result = str(analysis)
        assert "Controlled continents: None" in result
