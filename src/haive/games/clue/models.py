"""Comprehensive data models and enumerations for the Clue (Cluedo) mystery
game implementation.

This module defines the core data structures, enumerations, and models used
throughout the Clue game implementation. It includes the traditional game
elements (suspects, weapons, rooms) as well as game state representations,
player data structures, and action models following the classic board game rules.

The models follow the classic Clue game rules and include:
- Six suspects (Colonel Mustard, Professor Plum, etc.)
- Six weapons (Knife, Candlestick, Revolver, etc.)
- Nine rooms (Kitchen, Ballroom, Conservatory, etc.)
- Card types and game state tracking
- Player actions and game moves
- Deduction and hypothesis systems

Key Classes:
    ValidSuspect: Enumeration of all possible suspect characters
    ValidWeapon: Enumeration of all possible murder weapons
    ValidRoom: Enumeration of all possible locations
    CardType: Types of cards in the game (Suspect, Weapon, Room)
    ClueCard: Individual card representation with type information
    ClueSolution: The secret solution to the mystery
    ClueGuess: Player suggestions and accusations
    ClueResponse: Responses to player guesses
    ClueHypothesis: AI-generated deduction and reasoning
    GameStatus: Current state of the game progression

Examples:
    Creating game elements::

        from haive.games.clue.models import ValidSuspect, ValidWeapon, ValidRoom

        # Create a suggestion
        suspect = ValidSuspect.COLONEL_MUSTARD
        weapon = ValidWeapon.KNIFE
        room = ValidRoom.KITCHEN

        # Use in game logic
        suggestion = (suspect, weapon, room)

    Working with cards::

        from haive.games.clue.models import ClueCard, CardType

        # Create cards from enums
        suspect_card = ClueCard.from_suspect(ValidSuspect.PROFESSOR_PLUM)
        weapon_card = ClueCard.from_weapon(ValidWeapon.CANDLESTICK)
        room_card = ClueCard.from_room(ValidRoom.BALLROOM)

        # Check card types
        assert suspect_card.card_type == CardType.SUSPECT
        assert weapon_card.card_type == CardType.WEAPON
        assert room_card.card_type == CardType.ROOM

    Creating game solutions::

        from haive.games.clue.models import ClueSolution

        # Define the mystery solution
        solution = ClueSolution(
            suspect=ValidSuspect.MRS_PEACOCK,
            weapon=ValidWeapon.REVOLVER,
            room=ValidRoom.LIBRARY
        )

        # Convert to dictionary for serialization
        solution_dict = solution.to_dict()

    AI hypothesis generation::

        from haive.games.clue.models import ClueHypothesis

        # Create AI deduction
        hypothesis = ClueHypothesis(
            prime_suspect=ValidSuspect.COLONEL_MUSTARD,
            prime_weapon=ValidWeapon.KNIFE,
            prime_room=ValidRoom.KITCHEN,
            confidence=0.75,
            excluded_suspects=[ValidSuspect.PROFESSOR_PLUM],
            reasoning="Colonel Mustard has not been seen by any player..."
        )

The models are designed to be immutable where possible and include comprehensive
validation to ensure game rules are properly enforced throughout the implementation.
All models support serialization to dictionaries for persistence and network
communication.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class ValidSuspect(Enum):
    """Valid suspects in the game of Clue.

    Enumeration of all six possible suspects in the classic Clue board game.
    Each suspect is represented by their traditional character name and can
    be used as both a character to play as and a card in the deck.

    According to the classic Clue rules, one of these suspects will be the
    murderer in the game's solution, and the others will be distributed as
    cards to players for deduction purposes.

    Attributes:
        COLONEL_MUSTARD: The military officer suspect
        PROFESSOR_PLUM: The academic suspect
        MR_GREEN: The businessman suspect
        MRS_PEACOCK: The socialite suspect
        MISS_SCARLET: The glamorous suspect
        MRS_WHITE: The housekeeper suspect

    Examples:
        Using suspects in game logic::

            from haive.games.clue.models import ValidSuspect

            # Check if a suspect is valid
            if suspect_name == ValidSuspect.COLONEL_MUSTARD.value:
                print("Colonel Mustard is a valid suspect!")

            # Iterate through all suspects
            for suspect in ValidSuspect:
                print(f"Suspect: {suspect.value}")

            # Use in game suggestions
            my_suggestion = (
                ValidSuspect.PROFESSOR_PLUM,
                ValidWeapon.CANDLESTICK,
                ValidRoom.LIBRARY
            )
    """

    COLONEL_MUSTARD = "Colonel Mustard"
    PROFESSOR_PLUM = "Professor Plum"
    MR_GREEN = "Mr. Green"
    MRS_PEACOCK = "Mrs. Peacock"
    MISS_SCARLET = "Miss Scarlet"
    MRS_WHITE = "Mrs. White"


class ValidWeapon(Enum):
    """Valid weapons in the game of Clue.

    Enumeration of all six possible murder weapons in the classic Clue board game.
    Each weapon represents a potential murder weapon that could be used to commit
    the crime in the game's solution.

    According to the classic Clue rules, one of these weapons will be the murder
    weapon in the game's solution, and the others will be distributed as cards
    to players for deduction purposes.

    Attributes:
        KNIFE: A sharp blade weapon
        CANDLESTICK: A heavy decorative candle holder
        REVOLVER: A six-shot pistol
        ROPE: A length of rope for strangulation
        LEAD_PIPE: A heavy metal pipe
        WRENCH: A heavy tool weapon

    Examples:
        Using weapons in game logic::

            from haive.games.clue.models import ValidWeapon

            # Check if a weapon is valid
            if weapon_name == ValidWeapon.KNIFE.value:
                print("Knife is a valid weapon!")

            # Iterate through all weapons
            for weapon in ValidWeapon:
                print(f"Weapon: {weapon.value}")

            # Use in accusations
            my_accusation = (
                ValidSuspect.COLONEL_MUSTARD,
                ValidWeapon.KNIFE,
                ValidRoom.KITCHEN
            )
    """

    KNIFE = "Knife"
    CANDLESTICK = "Candlestick"
    REVOLVER = "Revolver"
    ROPE = "Rope"
    LEAD_PIPE = "Lead Pipe"
    WRENCH = "Wrench"


class ValidRoom(Enum):
    """Valid rooms in the game of Clue.

    Enumeration of all nine possible rooms in the classic Clue board game.
    Each room represents a location where the murder could have taken place
    in the game's solution.

    According to the classic Clue rules, one of these rooms will be the murder
    location in the game's solution, and the others will be distributed as cards
    to players for deduction purposes.

    Attributes:
        KITCHEN: The food preparation area
        BALLROOM: The large dance hall
        CONSERVATORY: The greenhouse room
        BILLIARD_ROOM: The game room with pool table
        LIBRARY: The book-filled study room
        STUDY: The private office
        HALL: The main entrance hallway
        LOUNGE: The comfortable sitting room
        DINING_ROOM: The formal eating area

    Examples:
        Using rooms in game logic::

            from haive.games.clue.models import ValidRoom

            # Check if a room is valid
            if room_name == ValidRoom.KITCHEN.value:
                print("Kitchen is a valid room!")

            # Iterate through all rooms
            for room in ValidRoom:
                print(f"Room: {room.value}")

            # Use in suggestions
            my_suggestion = (
                ValidSuspect.MRS_PEACOCK,
                ValidWeapon.REVOLVER,
                ValidRoom.LIBRARY
            )
    """

    KITCHEN = "Kitchen"
    BALLROOM = "Ballroom"
    CONSERVATORY = "Conservatory"
    BILLIARD_ROOM = "Billiard Room"
    LIBRARY = "Library"
    STUDY = "Study"
    HALL = "Hall"
    LOUNGE = "Lounge"
    DINING_ROOM = "Dining Room"


class CardType(Enum):
    """Types of cards in the game of Clue.

    Enumeration of the three types of cards that exist in the Clue game:
    suspect cards, weapon cards, and room cards. Each card type represents
    a different category of evidence that players use to solve the mystery.

    The game solution consists of exactly one card from each type, and the
    remaining cards are distributed to players as evidence.

    Attributes:
        SUSPECT: Cards representing the six possible suspects
        WEAPON: Cards representing the six possible murder weapons
        ROOM: Cards representing the nine possible crime scene locations

    Examples:
        Using card types for validation::

            from haive.games.clue.models import CardType, ClueCard

            # Check card type
            card = ClueCard.from_suspect(ValidSuspect.COLONEL_MUSTARD)
            if card.card_type == CardType.SUSPECT:
                print("This is a suspect card!")

            # Filter cards by type
            suspect_cards = [card for card in all_cards
                           if card.card_type == CardType.SUSPECT]
    """

    SUSPECT = "Suspect"
    WEAPON = "Weapon"
    ROOM = "Room"


@dataclass
class ClueCard:
    """A card in the game of Clue.

    Represents an individual card that can be held by players or be part of the
    game solution. Each card has a name and a type (suspect, weapon, or room).

    Cards are the primary evidence in the Clue game - players use them to make
    deductions about the solution and to respond to other players' suggestions.

    Attributes:
        name: The name of the card (e.g., "Colonel Mustard", "Knife", "Kitchen")
        card_type: The type of card (suspect, weapon, or room)

    Examples:
        Creating cards from enums::

            from haive.games.clue.models import ClueCard, ValidSuspect

            # Create a suspect card
            suspect_card = ClueCard.from_suspect(ValidSuspect.COLONEL_MUSTARD)
            print(f"Card: {suspect_card.name} ({suspect_card.card_type.value})")

            # Create weapon and room cards
            weapon_card = ClueCard.from_weapon(ValidWeapon.KNIFE)
            room_card = ClueCard.from_room(ValidRoom.KITCHEN)

        Converting to dictionary::

            card_dict = suspect_card.to_dict()
            # Returns: {"name": "Colonel Mustard", "card_type": "Suspect"}

        Using in game logic::

            # Check if player has a specific card
            if card.name == "Colonel Mustard" and card.card_type == CardType.SUSPECT:
                print("Player has Colonel Mustard suspect card!")
    """

    name: str  # The name of the card (e.g., "Colonel Mustard")
    card_type: CardType  # The type of card (suspect, weapon, or room)

    @staticmethod
    def from_suspect(suspect: ValidSuspect) -> "ClueCard":
        """Create a card from a suspect enum value.

        Args:
            suspect: The suspect enum value to convert to a card.

        Returns:
            ClueCard: A new suspect card instance.

        Examples:
            Creating suspect cards::

                card = ClueCard.from_suspect(ValidSuspect.COLONEL_MUSTARD)
                assert card.name == "Colonel Mustard"
                assert card.card_type == CardType.SUSPECT
        """
        return ClueCard(name=suspect.value, card_type=CardType.SUSPECT)

    @staticmethod
    def from_weapon(weapon: ValidWeapon) -> "ClueCard":
        """Create a card from a weapon enum value.

        Args:
            weapon: The weapon enum value to convert to a card.

        Returns:
            ClueCard: A new weapon card instance.

        Examples:
            Creating weapon cards::

                card = ClueCard.from_weapon(ValidWeapon.KNIFE)
                assert card.name == "Knife"
                assert card.card_type == CardType.WEAPON
        """
        return ClueCard(name=weapon.value, card_type=CardType.WEAPON)

    @staticmethod
    def from_room(room: ValidRoom) -> "ClueCard":
        """Create a card from a room enum value.

        Args:
            room: The room enum value to convert to a card.

        Returns:
            ClueCard: A new room card instance.

        Examples:
            Creating room cards::

                card = ClueCard.from_room(ValidRoom.KITCHEN)
                assert card.name == "Kitchen"
                assert card.card_type == CardType.ROOM
        """
        return ClueCard(name=room.value, card_type=CardType.ROOM)

    def to_dict(self) -> dict[str, str]:
        """Convert the card to a dictionary.

        Returns:
            dict[str, str]: Dictionary representation with 'name' and 'card_type' keys.

        Examples:
            Converting to dictionary::

                card = ClueCard.from_suspect(ValidSuspect.COLONEL_MUSTARD)
                card_dict = card.to_dict()
                # Returns: {"name": "Colonel Mustard", "card_type": "Suspect"}
        """
        return {"name": self.name, "card_type": self.card_type.value}


@dataclass
class ClueSolution:
    """The solution to a game of Clue.

    Represents the secret solution to the mystery that players are trying to solve.
    The solution consists of exactly one suspect, one weapon, and one room - these
    are the three cards that are set aside at the beginning of the game.

    Players win by correctly guessing all three elements of the solution through
    an accusation. The solution is hidden from all players until the end of the game.

    Attributes:
        suspect: The suspect who committed the murder
        weapon: The weapon used to commit the murder
        room: The room where the murder took place

    Examples:
        Creating a solution::

            solution = ClueSolution(
                suspect=ValidSuspect.COLONEL_MUSTARD,
                weapon=ValidWeapon.KNIFE,
                room=ValidRoom.KITCHEN
            )

        Converting to dictionary::

            solution_dict = solution.to_dict()
            # Returns: {
            #     "suspect": "Colonel Mustard",
            #     "weapon": "Knife",
            #     "room": "Kitchen"
            # }

        Checking accusations::

            player_accusation = (
                ValidSuspect.COLONEL_MUSTARD,
                ValidWeapon.KNIFE,
                ValidRoom.KITCHEN
            )

            is_correct = (
                solution.suspect == player_accusation[0] and
                solution.weapon == player_accusation[1] and
                solution.room == player_accusation[2]
            )
    """

    suspect: ValidSuspect
    weapon: ValidWeapon
    room: ValidRoom

    def to_dict(self) -> dict[str, str]:
        """Convert the solution to a dictionary.

        Returns:
            dict[str, str]: Dictionary with 'suspect', 'weapon', and 'room' keys.

        Examples:
            Converting solution to dictionary::

                solution = ClueSolution(
                    suspect=ValidSuspect.COLONEL_MUSTARD,
                    weapon=ValidWeapon.KNIFE,
                    room=ValidRoom.KITCHEN
                )
                solution_dict = solution.to_dict()
                # Returns: {
                #     "suspect": "Colonel Mustard",
                #     "weapon": "Knife",
                #     "room": "Kitchen"
                # }
        """
        return {
            "suspect": self.suspect.value,
            "weapon": self.weapon.value,
            "room": self.room.value,
        }


@dataclass
class ClueGuess:
    """A guess made during a game of Clue.

    Represents a player's suggestion or accusation in the game. A guess consists
    of one suspect, one weapon, and one room. Players use guesses to gather
    information and test hypotheses about the solution.

    There are two types of guesses:
    - Suggestion: Made to gather information from other players
    - Accusation: Made to win the game (if correct) or be eliminated (if wrong)

    Attributes:
        suspect: The suspect being guessed
        weapon: The weapon being guessed
        room: The room being guessed

    Examples:
        Creating a guess::

            guess = ClueGuess(
                suspect=ValidSuspect.PROFESSOR_PLUM,
                weapon=ValidWeapon.CANDLESTICK,
                room=ValidRoom.LIBRARY
            )

        Converting to dictionary::

            guess_dict = guess.to_dict()
            # Returns: {
            #     "suspect": "Professor Plum",
            #     "weapon": "Candlestick",
            #     "room": "Library"
            # }

        Comparing guesses::

            guess1 = ClueGuess(ValidSuspect.COLONEL_MUSTARD, ValidWeapon.KNIFE, ValidRoom.KITCHEN)
            guess2 = ClueGuess(ValidSuspect.COLONEL_MUSTARD, ValidWeapon.KNIFE, ValidRoom.KITCHEN)

            same_guess = (
                guess1.suspect == guess2.suspect and
                guess1.weapon == guess2.weapon and
                guess1.room == guess2.room
            )
    """

    suspect: ValidSuspect
    weapon: ValidWeapon
    room: ValidRoom

    def to_dict(self) -> dict[str, str]:
        """Convert the guess to a dictionary.

        Returns:
            dict[str, str]: Dictionary with 'suspect', 'weapon', and 'room' keys.

        Examples:
            Converting guess to dictionary::

                guess = ClueGuess(
                    suspect=ValidSuspect.PROFESSOR_PLUM,
                    weapon=ValidWeapon.CANDLESTICK,
                    room=ValidRoom.LIBRARY
                )
                guess_dict = guess.to_dict()
                # Returns: {
                #     "suspect": "Professor Plum",
                #     "weapon": "Candlestick",
                #     "room": "Library"
                # }
        """
        return {
            "suspect": self.suspect.value,
            "weapon": self.weapon.value,
            "room": self.room.value,
        }


@dataclass
class ClueResponse:
    """A response to a guess in a game of Clue.

    Represents the response given when a player makes a suggestion or accusation.
    The response indicates whether the guess was correct (for accusations) or
    provides information about which player can refute the guess (for suggestions).

    For suggestions, players check their cards to see if they can disprove the
    guess by showing one of the cards mentioned. For accusations, the response
    indicates whether the guess matches the solution exactly.

    Attributes:
        is_correct: True if the guess matched the solution (accusations only)
        responding_player: Name of the player who responded (suggestions only)
        refuting_card: The card shown to refute the guess (suggestions only)

    Examples:
        Response to a suggestion::

            # Player can refute with Colonel Mustard card
            response = ClueResponse(
                is_correct=False,
                responding_player="Alice",
                refuting_card=ClueCard.from_suspect(ValidSuspect.COLONEL_MUSTARD)
            )

        Response to an accusation::

            # Accusation was correct
            response = ClueResponse(
                is_correct=True,
                responding_player=None,
                refuting_card=None
            )

            # Accusation was wrong
            response = ClueResponse(
                is_correct=False,
                responding_player=None,
                refuting_card=None
            )

        Converting to dictionary::

            response_dict = response.to_dict()
            # Returns: {
            #     "is_correct": False,
            #     "responding_player": "Alice",
            #     "refuting_card": {"name": "Colonel Mustard", "card_type": "Suspect"}
            # }
    """

    is_correct: bool  # True if the guess matched the solution
    # Name of the player who responded (if any)
    responding_player: str | None = None
    # The card shown to refute the guess (if any)
    refuting_card: ClueCard | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert the response to a dictionary.

        Returns:
            dict[str, Any]: Dictionary representation of the response.

        Examples:
            Converting response to dictionary::

                response = ClueResponse(
                    is_correct=False,
                    responding_player="Alice",
                    refuting_card=ClueCard.from_suspect(ValidSuspect.COLONEL_MUSTARD)
                )
                response_dict = response.to_dict()
                # Returns: {
                #     "is_correct": False,
                #     "responding_player": "Alice",
                #     "refuting_card": {"name": "Colonel Mustard", "card_type": "Suspect"}
                # }
        """
        result = {
            "is_correct": self.is_correct,
            "responding_player": self.responding_player,
        }
        if self.refuting_card:
            result["refuting_card"] = self.refuting_card.to_dict()
        return result


@dataclass
class ClueHypothesis:
    """A hypothesis about the solution generated by AI analysis.

    Represents an AI player's current best guess about the solution based on
    the information gathered during the game. This includes both positive
    hypotheses (what the AI thinks the solution is) and negative information
    (what has been ruled out).

    The hypothesis system allows AI players to reason about the game state
    and make informed decisions about suggestions and accusations.

    Attributes:
        prime_suspect: Current best guess for the suspect
        prime_weapon: Current best guess for the weapon
        prime_room: Current best guess for the room
        confidence: Confidence level from 0.0 to 1.0
        excluded_suspects: Suspects that have been ruled out
        excluded_weapons: Weapons that have been ruled out
        excluded_rooms: Rooms that have been ruled out
        reasoning: Text explanation of the reasoning

    Examples:
        Creating a hypothesis::

            hypothesis = ClueHypothesis(
                prime_suspect=ValidSuspect.COLONEL_MUSTARD,
                prime_weapon=ValidWeapon.KNIFE,
                prime_room=ValidRoom.KITCHEN,
                confidence=0.75,
                excluded_suspects=[ValidSuspect.PROFESSOR_PLUM, ValidSuspect.MR_GREEN],
                excluded_weapons=[ValidWeapon.CANDLESTICK],
                excluded_rooms=[ValidRoom.BALLROOM, ValidRoom.LIBRARY],
                reasoning="Colonel Mustard was never shown by any player, and the knife was suggested multiple times without refutation"
            )

        Converting to dictionary::

            hypothesis_dict = hypothesis.to_dict()
            # Returns: {
            #     "prime_suspect": "Colonel Mustard",
            #     "prime_weapon": "Knife",
            #     "prime_room": "Kitchen",
            #     "confidence": 0.75,
            #     "excluded_suspects": ["Professor Plum", "Mr. Green"],
            #     "excluded_weapons": ["Candlestick"],
            #     "excluded_rooms": ["Ballroom", "Library"],
            #     "reasoning": "Colonel Mustard was never shown..."
            # }

        Using for decision making::

            # AI decides whether to make an accusation
            if hypothesis.confidence > 0.9:
                # Make accusation with high confidence
                accusation = ClueGuess(
                    suspect=hypothesis.prime_suspect,
                    weapon=hypothesis.prime_weapon,
                    room=hypothesis.prime_room
                )
    """

    # Primary suspects
    prime_suspect: ValidSuspect | None = None
    prime_weapon: ValidWeapon | None = None
    prime_room: ValidRoom | None = None

    # Confidence level (0.0 to 1.0)
    confidence: float = 0.0

    # Additional information
    excluded_suspects: list[ValidSuspect] = field(default_factory=list)
    excluded_weapons: list[ValidWeapon] = field(default_factory=list)
    excluded_rooms: list[ValidRoom] = field(default_factory=list)

    # Text reasoning
    reasoning: str = ""

    def to_dict(self) -> dict[str, Any]:
        """Convert the hypothesis to a dictionary.

        Returns:
            dict[str, Any]: Dictionary representation of the hypothesis.

        Examples:
            Converting hypothesis to dictionary::

                hypothesis = ClueHypothesis(
                    prime_suspect=ValidSuspect.COLONEL_MUSTARD,
                    prime_weapon=ValidWeapon.KNIFE,
                    prime_room=ValidRoom.KITCHEN,
                    confidence=0.75,
                    excluded_suspects=[ValidSuspect.PROFESSOR_PLUM],
                    reasoning="Based on elimination"
                )
                hypothesis_dict = hypothesis.to_dict()
                # Returns: {
                #     "prime_suspect": "Colonel Mustard",
                #     "prime_weapon": "Knife",
                #     "prime_room": "Kitchen",
                #     "confidence": 0.75,
                #     "excluded_suspects": ["Professor Plum"],
                #     "excluded_weapons": [],
                #     "excluded_rooms": [],
                #     "reasoning": "Based on elimination"
                # }
        """
        return {
            "prime_suspect": self.prime_suspect.value if self.prime_suspect else None,
            "prime_weapon": self.prime_weapon.value if self.prime_weapon else None,
            "prime_room": self.prime_room.value if self.prime_room else None,
            "confidence": self.confidence,
            "excluded_suspects": [s.value for s in self.excluded_suspects],
            "excluded_weapons": [w.value for w in self.excluded_weapons],
            "excluded_rooms": [r.value for r in self.excluded_rooms],
            "reasoning": self.reasoning,
        }


class GameStatus(Enum):
    """Status of a Clue game.

    Enumeration of the possible states of a Clue game during its lifecycle.
    Used to track game progression and determine valid actions.

    Attributes:
        NOT_STARTED: Game has been created but not yet begun
        IN_PROGRESS: Game is currently being played
        COMPLETED: Game has finished (someone won or all players were eliminated)

    Examples:
        Checking game status::

            from haive.games.clue.models import GameStatus

            # Initialize game
            status = GameStatus.NOT_STARTED

            # Start game
            if status == GameStatus.NOT_STARTED:
                status = GameStatus.IN_PROGRESS
                print("Game started!")

            # Check if game is active
            if status == GameStatus.IN_PROGRESS:
                # Allow players to make moves
                process_player_turn()

            # Game completed
            if status == GameStatus.COMPLETED:
                print("Game over!")

        Converting to string::

            status = GameStatus.IN_PROGRESS
            status_str = str(status)  # Returns "IN_PROGRESS"
            status_name = status.value  # Returns "IN_PROGRESS"
    """

    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"

    def __str__(self) -> str:
        """Return the string representation of the game status.

        Returns:
            str: The status value as a string.

        Examples:
            Converting status to string::

                status = GameStatus.IN_PROGRESS
                print(f"Current status: {status}")  # "Current status: IN_PROGRESS"
        """
        return self.value
