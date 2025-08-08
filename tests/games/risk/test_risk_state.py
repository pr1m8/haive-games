"""Test cases for Risk game state.

This module tests the RiskState class and its methods for managing
the game board, territories, and player information.
"""

import pytest

from haive.games.risk.models import GameStatus, PhaseType
from haive.games.risk.state import RiskState


class TestRiskState:
    """Test cases for RiskState class."""

    def test_risk_state_initialization_valid_players(self) -> None:
        """Test initializing RiskState with valid number of players."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        assert len(state.players) == 3
        assert "Alice" in state.players
        assert "Bob" in state.players
        assert "Charlie" in state.players
        assert state.current_player == "Alice"
        assert state.phase == PhaseType.SETUP
        assert state.game_status == GameStatus.IN_PROGRESS
        assert state.turn_number == 1

        # Check that all players have initial armies
        for player in state.players.values():
            assert player.unplaced_armies == 35  # 35 for 3 players

    def test_risk_state_initialization_two_players(self) -> None:
        """Test initializing RiskState with two players."""
        player_names = ["Alice", "Bob"]
        state = RiskState.initialize(player_names)

        assert len(state.players) == 2
        for player in state.players.values():
            assert player.unplaced_armies == 40  # 40 for 2 players

    def test_risk_state_initialization_six_players(self) -> None:
        """Test initializing RiskState with six players."""
        player_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
        state = RiskState.initialize(player_names)

        assert len(state.players) == 6
        for player in state.players.values():
            assert player.unplaced_armies == 20  # 20 for 6 players

    def test_risk_state_initialization_invalid_too_few_players(self) -> None:
        """Test that initialization fails with too few players."""
        with pytest.raises(ValueError, match="Risk requires 2-6 players"):
            RiskState.initialize(["Alice"])

    def test_risk_state_initialization_invalid_too_many_players(self) -> None:
        """Test that initialization fails with too many players."""
        player_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
        with pytest.raises(ValueError, match="Risk requires 2-6 players"):
            RiskState.initialize(player_names)

    def test_risk_state_territories_initialization(self) -> None:
        """Test that territories are properly initialized."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Check that all standard Risk territories exist
        expected_territories = 42  # Standard Risk has 42 territories
        assert len(state.territories) == expected_territories

        # Check specific territories
        assert "Alaska" in state.territories
        assert "Brazil" in state.territories
        assert "Egypt" in state.territories
        assert "China" in state.territories
        assert "Eastern Australia" in state.territories

        # Check territory properties
        alaska = state.territories["Alaska"]
        assert alaska.name == "Alaska"
        assert alaska.continent == "North America"
        assert alaska.owner is None
        assert alaska.armies == 0
        assert "Alberta" in alaska.adjacent
        assert "Kamchatka" in alaska.adjacent

    def test_risk_state_continents_initialization(self) -> None:
        """Test that continents are properly initialized."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Check that all continents exist
        expected_continents = [
            "North America",
            "South America",
            "Europe",
            "Africa",
            "Asia",
            "Australia",
        ]
        assert len(state.continents) == 6
        for continent_name in expected_continents:
            assert continent_name in state.continents

        # Check continent bonuses
        assert state.continents["North America"].bonus == 5
        assert state.continents["South America"].bonus == 2
        assert state.continents["Europe"].bonus == 5
        assert state.continents["Africa"].bonus == 3
        assert state.continents["Asia"].bonus == 7
        assert state.continents["Australia"].bonus == 2

        # Check territory counts
        assert len(state.continents["North America"].territories) == 9
        assert len(state.continents["South America"].territories) == 4
        assert len(state.continents["Europe"].territories) == 7
        assert len(state.continents["Africa"].territories) == 6
        assert len(state.continents["Asia"].territories) == 12
        assert len(state.continents["Australia"].territories) == 4

    def test_risk_state_deck_initialization(self) -> None:
        """Test that the card deck is properly initialized."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Should have 42 territory cards + 2 wild cards = 44 total
        assert len(state.deck) == 44

        # Check that cards are shuffled (deck should be randomized)
        # We can't test randomness directly, but we can check structure
        territory_cards = [
            card for card in state.deck if card.territory_name is not None
        ]
        wild_cards = [card for card in state.deck if card.territory_name is None]

        assert len(territory_cards) == 42
        assert len(wild_cards) == 2

    def test_get_controlled_territories_empty(self) -> None:
        """Test getting controlled territories when player controls none."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        territories = state.get_controlled_territories("Alice")
        assert territories == []

    def test_get_controlled_territories_some(self) -> None:
        """Test getting controlled territories when player controls some."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Assign some territories to Alice
        state.territories["Alaska"].owner = "Alice"
        state.territories["Alberta"].owner = "Alice"
        state.territories["Brazil"].owner = "Bob"

        alice_territories = state.get_controlled_territories("Alice")
        bob_territories = state.get_controlled_territories("Bob")
        charlie_territories = state.get_controlled_territories("Charlie")

        assert len(alice_territories) == 2
        assert len(bob_territories) == 1
        assert len(charlie_territories) == 0

        territory_names = [t.name for t in alice_territories]
        assert "Alaska" in territory_names
        assert "Alberta" in territory_names

    def test_get_controlled_continents_none(self) -> None:
        """Test getting controlled continents when player controls none."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Give Alice some territories but not a full continent
        state.territories["Alaska"].owner = "Alice"
        state.territories["Alberta"].owner = "Alice"

        continents = state.get_controlled_continents("Alice")
        assert continents == []

    def test_get_controlled_continents_full_continent(self) -> None:
        """Test getting controlled continents when player controls full continent."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Give Alice all of Australia (4 territories)
        australia_territories = [
            "Eastern Australia",
            "Western Australia",
            "New Guinea",
            "Indonesia",
        ]
        for territory_name in australia_territories:
            state.territories[territory_name].owner = "Alice"

        continents = state.get_controlled_continents("Alice")
        assert len(continents) == 1
        assert continents[0].name == "Australia"
        assert continents[0].bonus == 2

    def test_get_controlled_continents_multiple_continents(self) -> None:
        """Test getting controlled continents when player controls multiple."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Give Alice all of Australia and South America
        australia_territories = [
            "Eastern Australia",
            "Western Australia",
            "New Guinea",
            "Indonesia",
        ]
        south_america_territories = ["Argentina", "Brazil", "Peru", "Venezuela"]

        for territory_name in australia_territories + south_america_territories:
            state.territories[territory_name].owner = "Alice"

        continents = state.get_controlled_continents("Alice")
        continent_names = [c.name for c in continents]

        assert len(continents) == 2
        assert "Australia" in continent_names
        assert "South America" in continent_names

    def test_is_game_over_in_progress(self) -> None:
        """Test game over check when game is still in progress."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        assert not state.is_game_over()
        assert state.game_status == GameStatus.IN_PROGRESS

    def test_is_game_over_finished(self) -> None:
        """Test game over check when game is finished."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        state.game_status = GameStatus.FINISHED
        assert state.is_game_over()

    def test_get_winner_game_not_over(self) -> None:
        """Test getting winner when game is not over."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        winner = state.get_winner()
        assert winner is None

    def test_get_winner_game_finished_one_active_player(self) -> None:
        """Test getting winner when only one player remains active."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Eliminate Bob and Charlie
        state.players["Bob"].eliminated = True
        state.players["Charlie"].eliminated = True
        state.game_status = GameStatus.FINISHED

        winner = state.get_winner()
        assert winner == "Alice"

    def test_get_winner_game_finished_multiple_active_players(self) -> None:
        """Test getting winner when multiple players are still active."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Only eliminate Charlie
        state.players["Charlie"].eliminated = True
        state.game_status = GameStatus.FINISHED

        winner = state.get_winner()
        assert winner is None  # Still multiple active players

    def test_adjacency_relationships(self) -> None:
        """Test that territory adjacency relationships are symmetric."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Test a few known adjacencies
        alaska = state.territories["Alaska"]
        alberta = state.territories["Alberta"]
        kamchatka = state.territories["Kamchatka"]

        # Alaska should be adjacent to Alberta and Kamchatka
        assert "Alberta" in alaska.adjacent
        assert "Kamchatka" in alaska.adjacent

        # Alberta should be adjacent to Alaska
        assert "Alaska" in alberta.adjacent

        # Kamchatka should be adjacent to Alaska
        assert "Alaska" in kamchatka.adjacent

    def test_territory_continent_assignment(self) -> None:
        """Test that territories are correctly assigned to continents."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Test specific territory-continent assignments
        assert state.territories["Alaska"].continent == "North America"
        assert state.territories["Brazil"].continent == "South America"
        assert state.territories["Great Britain"].continent == "Europe"
        assert state.territories["Egypt"].continent == "Africa"
        assert state.territories["China"].continent == "Asia"
        assert state.territories["Eastern Australia"].continent == "Australia"

        # Test that continent territory lists match
        for continent in state.continents.values():
            for territory_name in continent.territories:
                territory = state.territories[territory_name]
                assert territory.continent == continent.name
