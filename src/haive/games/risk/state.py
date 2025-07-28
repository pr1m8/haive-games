"""State model for the Risk game.

This module defines the state model for the Risk game, tracking the game
board, player information, and game status.
"""

import random

from pydantic import BaseModel, Field

from haive.games.risk.models import (
    Card,
    CardType,
    Continent,
    GameStatus,
    PhaseType,
    Player,
    RiskAnalysis,
    RiskMove,
    Territory,
)


class RiskState(BaseModel):
    """State for the Risk game.

    Attributes:
        territories: Dictionary of territory objects, keyed by name.
        continents: Dictionary of continent objects, keyed by name.
        players: Dictionary of player objects, keyed by name.
        current_player: Name of the player whose turn it is.
        phase: Current phase of the game.
        game_status: Current status of the game.
        turn_number: Current turn number.
        deck: List of cards in the deck.
        next_card_set_value: Value of the next set of cards to be traded in.
        move_history: List of moves that have been made.
        player_analyses: Dictionary of player analyses, keyed by player name.
        attacker_captured_territory: Whether the attacker captured a territory this turn.
    """

    territories: dict[str, Territory] = Field(default_factory=dict)
    continents: dict[str, Continent] = Field(default_factory=dict)
    players: dict[str, Player] = Field(default_factory=dict)
    current_player: str = ""
    phase: PhaseType = PhaseType.SETUP
    game_status: GameStatus = GameStatus.IN_PROGRESS
    turn_number: int = 1
    deck: list[Card] = Field(default_factory=list)
    next_card_set_value: int = 4  # First set is worth 4 armies
    move_history: list[RiskMove] = Field(default_factory=list)
    player_analyses: dict[str, list[RiskAnalysis]] = Field(default_factory=dict)
    attacker_captured_territory: bool = False

    @classmethod
    def initialize(cls, player_names: list[str]) -> "RiskState":
        """Initialize a new Risk game state.

        Args:
            player_names: List of player names.

        Returns:
            A new RiskState object with default values.
        """
        if len(player_names) < 2 or len(player_names) > 6:
            raise ValueError("Risk requires 2-6 players")

        state = cls()

        # Add players
        for name in player_names:
            state.players[name] = Player(name=name)

        # Set current player
        state.current_player = player_names[0]

        # Set up player analyses
        for name in player_names:
            state.player_analyses[name] = []

        # Initialize with default Risk map
        state._initialize_map()

        # Initialize the card deck
        state._initialize_deck()

        # Calculate initial armies per player
        state._initialize_armies()

        return state

    def _initialize_map(self) -> None:
        """Initialize the Risk map with territories and continents."""
        # Define continents
        continent_data = {
            "North America": {
                "bonus": 5,
                "territories": [
                    "Alaska",
                    "Alberta",
                    "Central America",
                    "Eastern United States",
                    "Greenland",
                    "Northwest Territory",
                    "Ontario",
                    "Quebec",
                    "Western United States",
                ],
            },
            "South America": {
                "bonus": 2,
                "territories": ["Argentina", "Brazil", "Peru", "Venezuela"],
            },
            "Europe": {
                "bonus": 5,
                "territories": [
                    "Great Britain",
                    "Iceland",
                    "Northern Europe",
                    "Scandinavia",
                    "Southern Europe",
                    "Ukraine",
                    "Western Europe",
                ],
            },
            "Africa": {
                "bonus": 3,
                "territories": [
                    "Congo",
                    "East Africa",
                    "Egypt",
                    "Madagascar",
                    "North Africa",
                    "South Africa",
                ],
            },
            "Asia": {
                "bonus": 7,
                "territories": [
                    "Afghanistan",
                    "China",
                    "India",
                    "Irkutsk",
                    "Japan",
                    "Kamchatka",
                    "Middle East",
                    "Mongolia",
                    "Siam",
                    "Siberia",
                    "Ural",
                    "Yakutsk",
                ],
            },
            "Australia": {
                "bonus": 2,
                "territories": [
                    "Eastern Australia",
                    "Indonesia",
                    "New Guinea",
                    "Western Australia",
                ],
            },
        }

        # Define adjacency list for territories
        adjacency = {
            "Alaska": ["Northwest Territory", "Alberta", "Kamchatka"],
            "Alberta": [
                "Alaska",
                "Northwest Territory",
                "Ontario",
                "Western United States",
            ],
            "Central America": [
                "Western United States",
                "Eastern United States",
                "Venezuela",
            ],
            "Eastern United States": [
                "Western United States",
                "Ontario",
                "Quebec",
                "Central America",
            ],
            "Greenland": ["Northwest Territory", "Ontario", "Quebec", "Iceland"],
            "Northwest Territory": ["Alaska", "Alberta", "Ontario", "Greenland"],
            "Ontario": [
                "Northwest Territory",
                "Alberta",
                "Western United States",
                "Eastern United States",
                "Quebec",
                "Greenland",
            ],
            "Quebec": ["Ontario", "Eastern United States", "Greenland"],
            "Western United States": [
                "Alberta",
                "Ontario",
                "Eastern United States",
                "Central America",
            ],
            "Argentina": ["Peru", "Brazil"],
            "Brazil": ["Venezuela", "Peru", "Argentina", "North Africa"],
            "Peru": ["Venezuela", "Brazil", "Argentina"],
            "Venezuela": ["Central America", "Brazil", "Peru"],
            "Great Britain": [
                "Iceland",
                "Scandinavia",
                "Northern Europe",
                "Western Europe",
            ],
            "Iceland": ["Greenland", "Great Britain", "Scandinavia"],
            "Northern Europe": [
                "Great Britain",
                "Scandinavia",
                "Ukraine",
                "Southern Europe",
                "Western Europe",
            ],
            "Scandinavia": ["Iceland", "Great Britain", "Northern Europe", "Ukraine"],
            "Southern Europe": [
                "Western Europe",
                "Northern Europe",
                "Ukraine",
                "Middle East",
                "Egypt",
                "North Africa",
            ],
            "Ukraine": [
                "Scandinavia",
                "Northern Europe",
                "Southern Europe",
                "Middle East",
                "Afghanistan",
                "Ural",
            ],
            "Western Europe": [
                "Great Britain",
                "Northern Europe",
                "Southern Europe",
                "North Africa",
            ],
            "Congo": ["North Africa", "East Africa", "South Africa"],
            "East Africa": [
                "Egypt",
                "Middle East",
                "North Africa",
                "Congo",
                "South Africa",
                "Madagascar",
            ],
            "Egypt": ["North Africa", "East Africa", "Middle East", "Southern Europe"],
            "Madagascar": ["East Africa", "South Africa"],
            "North Africa": [
                "Western Europe",
                "Southern Europe",
                "Egypt",
                "East Africa",
                "Congo",
                "Brazil",
            ],
            "South Africa": ["Congo", "East Africa", "Madagascar"],
            "Afghanistan": [
                "Ukraine",
                "Ural",
                "Siberia",
                "China",
                "India",
                "Middle East",
            ],
            "China": ["Afghanistan", "Siberia", "Mongolia", "Siam", "India"],
            "India": ["Middle East", "Afghanistan", "China", "Siam"],
            "Irkutsk": ["Siberia", "Yakutsk", "Kamchatka", "Mongolia"],
            "Japan": ["Kamchatka", "Mongolia"],
            "Kamchatka": ["Yakutsk", "Irkutsk", "Mongolia", "Japan", "Alaska"],
            "Middle East": [
                "Southern Europe",
                "Ukraine",
                "Afghanistan",
                "India",
                "East Africa",
                "Egypt",
            ],
            "Mongolia": ["Siberia", "Irkutsk", "Kamchatka", "Japan", "China"],
            "Siam": ["India", "China", "Indonesia"],
            "Siberia": [
                "Ural",
                "Yakutsk",
                "Irkutsk",
                "Mongolia",
                "China",
                "Afghanistan",
            ],
            "Ural": ["Ukraine", "Siberia", "Afghanistan"],
            "Yakutsk": ["Siberia", "Irkutsk", "Kamchatka"],
            "Eastern Australia": ["Western Australia", "New Guinea"],
            "Indonesia": ["Siam", "New Guinea", "Western Australia"],
            "New Guinea": ["Indonesia", "Western Australia", "Eastern Australia"],
            "Western Australia": ["Indonesia", "New Guinea", "Eastern Australia"],
        }

        # Create continents
        for continent_name, data in continent_data.items():
            self.continents[continent_name] = Continent(
                name=continent_name,
                bonus=data["bonus"],
                territories=data["territories"],
            )

        # Create territories
        for continent_name, data in continent_data.items():
            for territory_name in data["territories"]:
                self.territories[territory_name] = Territory(
                    name=territory_name,
                    continent=continent_name,
                    adjacent=adjacency[territory_name],
                )

    def _initialize_deck(self) -> None:
        """Initialize the deck of Risk cards."""
        # Create territory cards
        for territory_name in self.territories.keys():
            # Assign card types evenly across territories
            if len(self.deck) % 3 == 0:
                card_type = CardType.INFANTRY
            elif len(self.deck) % 3 == 1:
                card_type = CardType.CAVALRY
            else:
                card_type = CardType.ARTILLERY

            self.deck.append(Card(card_type=card_type, territory_name=territory_name))

        # Add two wild cards
        self.deck.append(Card(card_type=CardType.WILD))
        self.deck.append(Card(card_type=CardType.WILD))

        # Shuffle the deck
        random.shuffle(self.deck)

    def _initialize_armies(self) -> None:
        """Calculate and assign initial armies to players."""
        num_players = len(self.players)

        # Set initial armies based on player count
        armies_per_player = {
            2: 40,  # 2 players
            3: 35,  # 3 players
            4: 30,  # 4 players
            5: 25,  # 5 players
            6: 20,  # 6 players
        }

        initial_armies = armies_per_player.get(num_players, 20)

        # Assign armies to players
        for player in self.players.values():
            player.unplaced_armies = initial_armies

    def get_controlled_territories(self, player_name: str) -> list[Territory]:
        """Get all territories controlled by a player.

        Args:
            player_name: Name of the player.

        Returns:
            List of territories controlled by the player.
        """
        return [t for t in self.territories.values() if t.owner == player_name]

    def get_controlled_continents(self, player_name: str) -> list[Continent]:
        """Get all continents controlled by a player.

        Args:
            player_name: Name of the player.

        Returns:
            List of continents controlled by the player.
        """
        controlled_continents = []

        for continent in self.continents.values():
            # Check if player controls all territories in this continent
            all_controlled = all(
                self.territories[t].owner == player_name for t in continent.territories
            )
            if all_controlled:
                controlled_continents.append(continent)

        return controlled_continents

    def is_game_over(self) -> bool:
        """Check if the game is over.

        Returns:
            True if the game is over, False otherwise.
        """
        return self.game_status == GameStatus.FINISHED

    def get_winner(self) -> str | None:
        """Get the winner of the game.

        Returns:
            Name of the winner, or None if the game is not over.
        """
        if not self.is_game_over():
            return None

        # Find the player who controls all territories
        active_players = [p.name for p in self.players.values() if not p.eliminated]
        if len(active_players) == 1:
            return active_players[0]

        return None
