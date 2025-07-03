"""Tests for the Risk game state module."""

import pytest

from haive.games.risk.state import RiskState


def test_risk_state_initialization():
    """Test initialization of Risk game state."""
    # Test with valid player count
    player_names = ["Player1", "Player2", "Player3"]
    state = RiskState.initialize(player_names)

    # Check players
    assert len(state.players) == 3
    assert "Player1" in state.players
    assert "Player2" in state.players
    assert "Player3" in state.players

    # Check current player
    assert state.current_player == "Player1"

    # Check territories
    assert len(state.territories) == 42  # Standard Risk board has 42 territories

    # Check continents
    assert len(state.continents) == 6  # Standard Risk board has 6 continents

    # Check deck
    assert len(state.deck) > 0

    # Check initial armies
    assert state.players["Player1"].unplaced_armies == 35  # For 3 players


def test_risk_state_initialization_invalid_players():
    """Test initialization with invalid player count."""
    # Test with too few players
    with pytest.raises(ValueError):
        RiskState.initialize(["Player1"])

    # Test with too many players
    with pytest.raises(ValueError):
        RiskState.initialize(["P1", "P2", "P3", "P4", "P5", "P6", "P7"])


def test_get_controlled_territories():
    """Test getting territories controlled by a player."""
    player_names = ["Player1", "Player2"]
    state = RiskState.initialize(player_names)

    # Initially no player controls any territory
    assert len(state.get_controlled_territories("Player1")) == 0

    # Assign a territory to Player1
    territory = list(state.territories.values())[0]
    territory.owner = "Player1"
    territory.armies = 3

    # Check controlled territories
    controlled = state.get_controlled_territories("Player1")
    assert len(controlled) == 1
    assert controlled[0].name == territory.name
    assert controlled[0].armies == 3


def test_get_controlled_continents():
    """Test getting continents controlled by a player."""
    player_names = ["Player1", "Player2"]
    state = RiskState.initialize(player_names)

    # Initially no player controls any continent
    assert len(state.get_controlled_continents("Player1")) == 0

    # Assign all territories in Australia to Player1
    for territory_name in state.continents["Australia"].territories:
        state.territories[territory_name].owner = "Player1"
        state.territories[territory_name].armies = 1

    # Check controlled continents
    controlled = state.get_controlled_continents("Player1")
    assert len(controlled) == 1
    assert controlled[0].name == "Australia"
    assert controlled[0].bonus == 2


def test_game_over_and_winner():
    """Test game over detection and winner determination."""
    player_names = ["Player1", "Player2"]
    state = RiskState.initialize(player_names)

    # Initially game is not over
    assert not state.is_game_over()
    assert state.get_winner() is None

    # Eliminate Player2
    state.players["Player2"].eliminated = True

    # Game should now be over with Player1 as winner
    state.game_status = state.GameStatus.FINISHED
    assert state.is_game_over()
    assert state.get_winner() == "Player1"
