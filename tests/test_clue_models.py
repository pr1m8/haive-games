"""Comprehensive tests for Clue game models.

This module tests all data models, enumerations, and data structures
used in the Clue game implementation.
"""

from haive.games.clue.models import (
    CardType,
    ClueCard,
    ClueGuess,
    ClueHypothesis,
    ClueResponse,
    ClueSolution,
    GameStatus,
    ValidRoom,
    ValidSuspect,
    ValidWeapon,
)


class TestEnumerations:
    """Test all enumeration classes."""

    def test_valid_suspect_enum_values(self):
        """Test that ValidSuspect enum has all expected values."""
        expected_suspects = {
            "Colonel Mustard",
            "Professor Plum",
            "Mr. Green",
            "Mrs. Peacock",
            "Miss Scarlet",
            "Mrs. White",
        }
        actual_suspects = {suspect.value for suspect in ValidSuspect}
        assert actual_suspects == expected_suspects
        assert len(ValidSuspect) == 6

    def test_valid_weapon_enum_values(self):
        """Test that ValidWeapon enum has all expected values."""
        expected_weapons = {
            "Knife",
            "Candlestick",
            "Revolver",
            "Rope",
            "Lead Pipe",
            "Wrench",
        }
        actual_weapons = {weapon.value for weapon in ValidWeapon}
        assert actual_weapons == expected_weapons
        assert len(ValidWeapon) == 6

    def test_valid_room_enum_values(self):
        """Test that ValidRoom enum has all expected values."""
        expected_rooms = {
            "Kitchen",
            "Ballroom",
            "Conservatory",
            "Billiard Room",
            "Library",
            "Study",
            "Hall",
            "Lounge",
            "Dining Room",
        }
        actual_rooms = {room.value for room in ValidRoom}
        assert actual_rooms == expected_rooms
        assert len(ValidRoom) == 9

    def test_card_type_enum_values(self):
        """Test that CardType enum has all expected values."""
        expected_types = {"Suspect", "Weapon", "Room"}
        actual_types = {card_type.value for card_type in CardType}
        assert actual_types == expected_types
        assert len(CardType) == 3

    def test_game_status_enum_values(self):
        """Test that GameStatus enum has all expected values."""
        expected_statuses = {"NOT_STARTED", "IN_PROGRESS", "COMPLETED"}
        actual_statuses = {status.value for status in GameStatus}
        assert actual_statuses == expected_statuses
        assert len(GameStatus) == 3

    def test_game_status_string_representation(self):
        """Test GameStatus string representation."""
        assert str(GameStatus.NOT_STARTED) == "NOT_STARTED"
        assert str(GameStatus.IN_PROGRESS) == "IN_PROGRESS"
        assert str(GameStatus.COMPLETED) == "COMPLETED"


class TestClueCard:
    """Test ClueCard dataclass and methods."""

    def test_clue_card_creation(self):
        """Test creating a ClueCard instance."""
        card = ClueCard(name="Colonel Mustard", card_type=CardType.SUSPECT)
        assert card.name == "Colonel Mustard"
        assert card.card_type == CardType.SUSPECT

    def test_from_suspect_factory_method(self):
        """Test creating ClueCard from suspect enum."""
        card = ClueCard.from_suspect(ValidSuspect.COLONEL_MUSTARD)
        assert card.name == "Colonel Mustard"
        assert card.card_type == CardType.SUSPECT

    def test_from_weapon_factory_method(self):
        """Test creating ClueCard from weapon enum."""
        card = ClueCard.from_weapon(ValidWeapon.CANDLESTICK)
        assert card.name == "Candlestick"
        assert card.card_type == CardType.WEAPON

    def test_from_room_factory_method(self):
        """Test creating ClueCard from room enum."""
        card = ClueCard.from_room(ValidRoom.LIBRARY)
        assert card.name == "Library"
        assert card.card_type == CardType.ROOM

    def test_to_dict_method(self):
        """Test converting ClueCard to dictionary."""
        card = ClueCard(name="Knife", card_type=CardType.WEAPON)
        result = card.to_dict()
        assert result == {"name": "Knife", "card_type": "Weapon"}

    def test_all_factory_methods_coverage(self):
        """Test creating cards for all enum values."""
        # Test all suspects
        for suspect in ValidSuspect:
            card = ClueCard.from_suspect(suspect)
            assert card.name == suspect.value
            assert card.card_type == CardType.SUSPECT

        # Test all weapons
        for weapon in ValidWeapon:
            card = ClueCard.from_weapon(weapon)
            assert card.name == weapon.value
            assert card.card_type == CardType.WEAPON

        # Test all rooms
        for room in ValidRoom:
            card = ClueCard.from_room(room)
            assert card.name == room.value
            assert card.card_type == CardType.ROOM


class TestClueSolution:
    """Test ClueSolution dataclass."""

    def test_clue_solution_creation(self):
        """Test creating a ClueSolution instance."""
        solution = ClueSolution(
            suspect=ValidSuspect.MISS_SCARLET,
            weapon=ValidWeapon.ROPE,
            room=ValidRoom.STUDY,
        )
        assert solution.suspect == ValidSuspect.MISS_SCARLET
        assert solution.weapon == ValidWeapon.ROPE
        assert solution.room == ValidRoom.STUDY

    def test_solution_to_dict(self):
        """Test converting ClueSolution to dictionary."""
        solution = ClueSolution(
            suspect=ValidSuspect.PROFESSOR_PLUM,
            weapon=ValidWeapon.LEAD_PIPE,
            room=ValidRoom.CONSERVATORY,
        )
        result = solution.to_dict()
        assert result == {
            "suspect": "Professor Plum",
            "weapon": "Lead Pipe",
            "room": "Conservatory",
        }

    def test_solution_with_different_combinations(self):
        """Test creating solutions with various combinations."""
        combinations = [
            (ValidSuspect.MR_GREEN, ValidWeapon.KNIFE, ValidRoom.KITCHEN),
            (ValidSuspect.MRS_PEACOCK, ValidWeapon.REVOLVER, ValidRoom.BALLROOM),
            (ValidSuspect.MRS_WHITE, ValidWeapon.WRENCH, ValidRoom.DINING_ROOM),
        ]

        for suspect, weapon, room in combinations:
            solution = ClueSolution(suspect=suspect, weapon=weapon, room=room)
            assert solution.suspect == suspect
            assert solution.weapon == weapon
            assert solution.room == room


class TestClueGuess:
    """Test ClueGuess dataclass."""

    def test_clue_guess_creation(self):
        """Test creating a ClueGuess instance."""
        guess = ClueGuess(
            suspect=ValidSuspect.COLONEL_MUSTARD,
            weapon=ValidWeapon.CANDLESTICK,
            room=ValidRoom.LIBRARY,
        )
        assert guess.suspect == ValidSuspect.COLONEL_MUSTARD
        assert guess.weapon == ValidWeapon.CANDLESTICK
        assert guess.room == ValidRoom.LIBRARY

    def test_guess_to_dict(self):
        """Test converting ClueGuess to dictionary."""
        guess = ClueGuess(
            suspect=ValidSuspect.MISS_SCARLET,
            weapon=ValidWeapon.KNIFE,
            room=ValidRoom.HALL,
        )
        result = guess.to_dict()
        assert result == {
            "suspect": "Miss Scarlet",
            "weapon": "Knife",
            "room": "Hall",
        }

    def test_guess_does_not_have_player_attribute(self):
        """Test that ClueGuess does not have a player attribute."""
        guess = ClueGuess(
            suspect=ValidSuspect.MR_GREEN,
            weapon=ValidWeapon.ROPE,
            room=ValidRoom.LOUNGE,
        )
        assert not hasattr(guess, "player")


class TestClueResponse:
    """Test ClueResponse dataclass."""

    def test_correct_response_creation(self):
        """Test creating a correct response."""
        response = ClueResponse(is_correct=True)
        assert response.is_correct is True
        assert response.responding_player is None
        assert response.refuting_card is None

    def test_refuting_response_creation(self):
        """Test creating a refuting response."""
        card = ClueCard(name="Knife", card_type=CardType.WEAPON)
        response = ClueResponse(
            is_correct=False,
            responding_player="Player 2",
            refuting_card=card,
        )
        assert response.is_correct is False
        assert response.responding_player == "Player 2"
        assert response.refuting_card == card

    def test_response_to_dict_without_card(self):
        """Test converting response to dict without refuting card."""
        response = ClueResponse(is_correct=False, responding_player="Player 1")
        result = response.to_dict()
        assert result == {
            "is_correct": False,
            "responding_player": "Player 1",
        }

    def test_response_to_dict_with_card(self):
        """Test converting response to dict with refuting card."""
        card = ClueCard(name="Library", card_type=CardType.ROOM)
        response = ClueResponse(
            is_correct=False,
            responding_player="Player 3",
            refuting_card=card,
        )
        result = response.to_dict()
        assert result == {
            "is_correct": False,
            "responding_player": "Player 3",
            "refuting_card": {"name": "Library", "card_type": "Room"},
        }


class TestClueHypothesis:
    """Test ClueHypothesis dataclass."""

    def test_hypothesis_creation_with_defaults(self):
        """Test creating hypothesis with default values."""
        hypothesis = ClueHypothesis()
        assert hypothesis.prime_suspect is None
        assert hypothesis.prime_weapon is None
        assert hypothesis.prime_room is None
        assert hypothesis.confidence == 0.0
        assert hypothesis.excluded_suspects == []
        assert hypothesis.excluded_weapons == []
        assert hypothesis.excluded_rooms == []
        assert hypothesis.reasoning == ""

    def test_hypothesis_creation_with_values(self):
        """Test creating hypothesis with specific values."""
        hypothesis = ClueHypothesis(
            prime_suspect=ValidSuspect.PROFESSOR_PLUM,
            prime_weapon=ValidWeapon.LEAD_PIPE,
            prime_room=ValidRoom.CONSERVATORY,
            confidence=0.85,
            excluded_suspects=[ValidSuspect.MISS_SCARLET, ValidSuspect.MR_GREEN],
            excluded_weapons=[ValidWeapon.KNIFE],
            excluded_rooms=[ValidRoom.KITCHEN, ValidRoom.HALL],
            reasoning="Based on the evidence...",
        )
        assert hypothesis.prime_suspect == ValidSuspect.PROFESSOR_PLUM
        assert hypothesis.prime_weapon == ValidWeapon.LEAD_PIPE
        assert hypothesis.prime_room == ValidRoom.CONSERVATORY
        assert hypothesis.confidence == 0.85
        assert len(hypothesis.excluded_suspects) == 2
        assert ValidSuspect.MISS_SCARLET in hypothesis.excluded_suspects

    def test_hypothesis_to_dict_empty(self):
        """Test converting empty hypothesis to dictionary."""
        hypothesis = ClueHypothesis()
        result = hypothesis.to_dict()
        assert result == {
            "prime_suspect": None,
            "prime_weapon": None,
            "prime_room": None,
            "confidence": 0.0,
            "excluded_suspects": [],
            "excluded_weapons": [],
            "excluded_rooms": [],
            "reasoning": "",
        }

    def test_hypothesis_to_dict_full(self):
        """Test converting full hypothesis to dictionary."""
        hypothesis = ClueHypothesis(
            prime_suspect=ValidSuspect.MRS_WHITE,
            prime_weapon=ValidWeapon.WRENCH,
            prime_room=ValidRoom.BILLIARD_ROOM,
            confidence=0.95,
            excluded_suspects=[ValidSuspect.COLONEL_MUSTARD],
            excluded_weapons=[ValidWeapon.ROPE, ValidWeapon.REVOLVER],
            excluded_rooms=[ValidRoom.STUDY],
            reasoning="Strong evidence suggests...",
        )
        result = hypothesis.to_dict()
        assert result == {
            "prime_suspect": "Mrs. White",
            "prime_weapon": "Wrench",
            "prime_room": "Billiard Room",
            "confidence": 0.95,
            "excluded_suspects": ["Colonel Mustard"],
            "excluded_weapons": ["Rope", "Revolver"],
            "excluded_rooms": ["Study"],
            "reasoning": "Strong evidence suggests...",
        }

    def test_hypothesis_mutable_default_lists_are_independent(self):
        """Test that default lists are independent between instances."""
        hypothesis1 = ClueHypothesis()
        hypothesis2 = ClueHypothesis()

        # Modify hypothesis1's lists
        hypothesis1.excluded_suspects.append(ValidSuspect.MR_GREEN)
        hypothesis1.excluded_weapons.append(ValidWeapon.KNIFE)
        hypothesis1.excluded_rooms.append(ValidRoom.LIBRARY)

        # Verify hypothesis2's lists are unaffected
        assert hypothesis2.excluded_suspects == []
        assert hypothesis2.excluded_weapons == []
        assert hypothesis2.excluded_rooms == []


class TestModelIntegration:
    """Test integration between different model classes."""

    def test_solution_and_guess_compatibility(self):
        """Test that solution and guess can be compared."""
        solution = ClueSolution(
            suspect=ValidSuspect.MISS_SCARLET,
            weapon=ValidWeapon.CANDLESTICK,
            room=ValidRoom.LIBRARY,
        )

        # Matching guess
        correct_guess = ClueGuess(
            suspect=ValidSuspect.MISS_SCARLET,
            weapon=ValidWeapon.CANDLESTICK,
            room=ValidRoom.LIBRARY,
        )

        # Non-matching guess
        wrong_guess = ClueGuess(
            suspect=ValidSuspect.COLONEL_MUSTARD,
            weapon=ValidWeapon.ROPE,
            room=ValidRoom.KITCHEN,
        )

        # Test comparison
        assert correct_guess.suspect == solution.suspect
        assert correct_guess.weapon == solution.weapon
        assert correct_guess.room == solution.room

        assert wrong_guess.suspect != solution.suspect
        assert wrong_guess.weapon != solution.weapon
        assert wrong_guess.room != solution.room

    def test_card_creation_from_all_enums(self):
        """Test creating cards from all enum types."""
        cards = []

        # Create suspect cards
        for suspect in ValidSuspect:
            cards.append(ClueCard.from_suspect(suspect))

        # Create weapon cards
        for weapon in ValidWeapon:
            cards.append(ClueCard.from_weapon(weapon))

        # Create room cards
        for room in ValidRoom:
            cards.append(ClueCard.from_room(room))

        # Verify total card count
        assert len(cards) == len(ValidSuspect) + len(ValidWeapon) + len(ValidRoom)
        assert len(cards) == 6 + 6 + 9  # 21 total cards

    def test_hypothesis_can_reference_solution_elements(self):
        """Test that hypothesis can reference solution elements."""
        solution = ClueSolution(
            suspect=ValidSuspect.PROFESSOR_PLUM,
            weapon=ValidWeapon.LEAD_PIPE,
            room=ValidRoom.CONSERVATORY,
        )

        hypothesis = ClueHypothesis(
            prime_suspect=solution.suspect,
            prime_weapon=solution.weapon,
            prime_room=solution.room,
            confidence=1.0,
            reasoning="Certain match",
        )

        assert hypothesis.prime_suspect == solution.suspect
        assert hypothesis.prime_weapon == solution.weapon
        assert hypothesis.prime_room == solution.room
