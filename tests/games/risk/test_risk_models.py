"""Tests for the Risk game models module."""

from haive.games.risk.models import (
    Card,
    CardType,
    Continent,
    MoveType,
    Player,
    RiskAnalysis,
    RiskMove,
    Territory,
)


def test_card_type():
    """Test CardType enum."""
    assert CardType.INFANTRY.value == "infantry"
    assert CardType.CAVALRY.value == "cavalry"
    assert CardType.ARTILLERY.value == "artillery"
    assert CardType.WILD.value == "wild"


def test_card():
    """Test Card model."""
    # Test card with territory
    card = Card(card_type=CardType.INFANTRY, territory_name="Alaska")
    assert card.card_type == CardType.INFANTRY
    assert card.territory_name == "Alaska"
    assert str(card) == "Infantry (Alaska)"

    # Test wild card
    wild_card = Card(card_type=CardType.WILD)
    assert wild_card.card_type == CardType.WILD
    assert wild_card.territory_name is None
    assert str(wild_card) == "Wild"


def test_territory():
    """Test Territory model."""
    # Create territory
    territory = Territory(
        name="Alaska",
        continent="North America",
        owner="Player1",
        armies=5,
        adjacent=["Northwest Territory", "Alberta", "Kamchatka"],
    )

    assert territory.name == "Alaska"
    assert territory.continent == "North America"
    assert territory.owner == "Player1"
    assert territory.armies == 5
    assert len(territory.adjacent) == 3
    assert "Northwest Territory" in territory.adjacent
    assert str(territory) == "Alaska (Player1, 5 armies)"

    # Test unoccupied territory
    unoccupied = Territory(name="Ukraine", continent="Europe")
    assert unoccupied.owner is None
    assert unoccupied.armies == 0
    assert str(unoccupied) == "Ukraine (Unoccupied, 0 armies)"


def test_continent():
    """Test Continent model."""
    continent = Continent(
        name="Australia",
        bonus=2,
        territories=[
            "Eastern Australia",
            "Western Australia",
            "New Guinea",
            "Indonesia",
        ],
    )

    assert continent.name == "Australia"
    assert continent.bonus == 2
    assert len(continent.territories) == 4
    assert "Eastern Australia" in continent.territories
    assert str(continent) == "Australia (Bonus: 2)"


def test_player():
    """Test Player model."""
    # Create player
    player = Player(
        name="Player1",
        cards=[
            Card(card_type=CardType.INFANTRY, territory_name="Alaska"),
            Card(card_type=CardType.WILD),
        ],
        unplaced_armies=10,
    )

    assert player.name == "Player1"
    assert len(player.cards) == 2
    assert player.unplaced_armies == 10
    assert not player.eliminated
    assert str(player) == "Player1 (Active, 10 unplaced armies, 2 cards)"

    # Test eliminated player
    eliminated = Player(name="Player2", eliminated=True)
    assert eliminated.eliminated
    assert str(eliminated) == "Player2 (Eliminated, 0 unplaced armies, 0 cards)"


def test_risk_move():
    """Test RiskMove model."""
    # Test place armies move
    place_move = RiskMove(
        move_type=MoveType.PLACE_ARMIES,
        player="Player1",
        to_territory="Alaska",
        armies=3,
    )

    assert place_move.move_type == MoveType.PLACE_ARMIES
    assert place_move.player == "Player1"
    assert place_move.to_territory == "Alaska"
    assert place_move.armies == 3
    assert str(place_move) == "Player1 places 3 armies on Alaska"

    # Test attack move
    attack_move = RiskMove(
        move_type=MoveType.ATTACK,
        player="Player1",
        from_territory="Alaska",
        to_territory="Kamchatka",
        attack_dice=3,
    )

    assert attack_move.move_type == MoveType.ATTACK
    assert attack_move.from_territory == "Alaska"
    assert attack_move.to_territory == "Kamchatka"
    assert attack_move.attack_dice == 3
    assert str(attack_move) == "Player1 attacks from Alaska to Kamchatka with 3 dice"

    # Test fortify move
    fortify_move = RiskMove(
        move_type=MoveType.FORTIFY,
        player="Player1",
        from_territory="Alaska",
        to_territory="Northwest Territory",
        armies=2,
    )

    assert fortify_move.move_type == MoveType.FORTIFY
    assert fortify_move.from_territory == "Alaska"
    assert fortify_move.to_territory == "Northwest Territory"
    assert fortify_move.armies == 2
    assert (
        str(fortify_move)
        == "Player1 fortifies Northwest Territory with 2 armies from Alaska"
    )

    # Test trade cards move
    cards = [
        Card(card_type=CardType.INFANTRY, territory_name="Alaska"),
        Card(card_type=CardType.CAVALRY, territory_name="Ukraine"),
        Card(card_type=CardType.ARTILLERY, territory_name="Brazil"),
    ]

    trade_move = RiskMove(move_type=MoveType.TRADE_CARDS, player="Player1", cards=cards)

    assert trade_move.move_type == MoveType.TRADE_CARDS
    assert len(trade_move.cards) == 3
    assert (
        "Player1 trades in cards: Infantry (Alaska), Cavalry (Ukraine), Artillery (Brazil)"
        in str(trade_move)
    )


def test_risk_analysis():
    """Test RiskAnalysis model."""
    # Create sample move for recommendation
    move = RiskMove(
        move_type=MoveType.ATTACK,
        player="Player1",
        from_territory="Alaska",
        to_territory="Kamchatka",
        attack_dice=3,
    )

    # Create analysis
    analysis = RiskAnalysis(
        player="Player1",
        controlled_continents=["Australia", "South America"],
        controlled_territories=15,
        total_armies=45,
        position_evaluation="winning",
        recommended_move=move,
        explanation="Player controls two continents and has a strong position in Asia.",
    )

    assert analysis.player == "Player1"
    assert len(analysis.controlled_continents) == 2
    assert "Australia" in analysis.controlled_continents
    assert analysis.controlled_territories == 15
    assert analysis.total_armies == 45
    assert analysis.position_evaluation == "winning"
    assert analysis.recommended_move == move
    assert "Player controls two continents" in analysis.explanation

    # Test string representation
    assert "Analysis for Player1" in str(analysis)
    assert "Controlled continents: Australia, South America" in str(analysis)
    assert "Controlled territories: 15" in str(analysis)
    assert "Total armies: 45" in str(analysis)
    assert "Position evaluation: winning" in str(analysis)
