"""Comprehensive tests for Clue game state.

This module tests the ClueState class and its initialization,
properties, and methods.
"""

from haive.games.clue.models import (
    ClueGuess,
    ClueResponse,
    ClueSolution,
    ValidRoom,
    ValidSuspect,
    ValidWeapon,
)
from haive.games.clue.state import ClueState


class TestClueStateInitialization:
    """Test ClueState initialization and factory methods."""

    def test_default_initialization(self):
        """Test initializing ClueState with default values."""
        solution = ClueSolution(
            suspect=ValidSuspect.MISS_SCARLET,
            weapon=ValidWeapon.ROPE,
            room=ValidRoom.STUDY,
        )
        state = ClueState(solution=solution)

        assert state.solution == solution
        assert state.guesses == []
        assert state.responses == []
        assert state.player1_cards == []
        assert state.player2_cards == []
        assert state.current_player == "player1"
        assert state.max_turns == 20
        assert state.game_status == "ongoing"
        assert state.winner is None
        assert state.player1_hypotheses == []
        assert state.player2_hypotheses == []

    def test_initialize_class_method_with_random_solution(self):
        """Test initialize method creates random solution."""
        state = ClueState.initialize()

        # Verify solution is properly set
        assert isinstance(state.solution, ClueSolution)
        assert isinstance(state.solution.suspect, ValidSuspect)
        assert isinstance(state.solution.weapon, ValidWeapon)
        assert isinstance(state.solution.room, ValidRoom)

        # Verify cards are dealt
        assert len(state.player1_cards) > 0
        assert len(state.player2_cards) > 0

        # Total cards should be 21 - 3 (solution cards)
        total_cards = len(state.player1_cards) + len(state.player2_cards)
        assert total_cards == 18  # 21 total - 3 solution cards

        # Verify solution cards are not in player hands
        solution_cards = [
            state.solution.suspect,
            state.solution.weapon,
            state.solution.room,
        ]
        all_player_cards = state.player1_cards + state.player2_cards
        for card in solution_cards:
            assert card not in all_player_cards

    def test_initialize_with_predefined_solution(self):
        """Test initialize with a specific solution."""
        predefined_solution = ClueSolution(
            suspect=ValidSuspect.COLONEL_MUSTARD,
            weapon=ValidWeapon.CANDLESTICK,
            room=ValidRoom.LIBRARY,
        )

        state = ClueState.initialize(solution=predefined_solution)

        assert state.solution == predefined_solution
        assert state.solution.suspect == ValidSuspect.COLONEL_MUSTARD
        assert state.solution.weapon == ValidWeapon.CANDLESTICK
        assert state.solution.room == ValidRoom.LIBRARY

    def test_initialize_with_custom_parameters(self):
        """Test initialize with custom parameters."""
        state = ClueState.initialize(
            first_player="player2",
            max_turns=30,
        )

        assert state.current_player == "player2"
        assert state.max_turns == 30

    def test_card_distribution_is_fair(self):
        """Test that cards are distributed fairly between players."""
        state = ClueState.initialize()

        # Players should have roughly equal number of cards
        diff = abs(len(state.player1_cards) - len(state.player2_cards))
        assert diff <= 1  # At most 1 card difference

    def test_all_cards_are_distributed(self):
        """Test that all non-solution cards are distributed."""
        state = ClueState.initialize()

        # Get all cards
        all_suspects = list(ValidSuspect)
        all_weapons = list(ValidWeapon)
        all_rooms = list(ValidRoom)

        # Remove solution cards
        all_suspects.remove(state.solution.suspect)
        all_weapons.remove(state.solution.weapon)
        all_rooms.remove(state.solution.room)

        # All remaining cards should be in player hands
        expected_cards = set(all_suspects + all_weapons + all_rooms)
        actual_cards = set(state.player1_cards + state.player2_cards)

        assert expected_cards == actual_cards


class TestClueStateProperties:
    """Test ClueState property methods."""

    def test_current_turn_number_property(self):
        """Test current_turn_number property calculation."""
        solution = ClueSolution(
            suspect=ValidSuspect.MISS_SCARLET,
            weapon=ValidWeapon.ROPE,
            room=ValidRoom.STUDY,
        )
        state = ClueState(solution=solution)

        # Initial turn
        assert state.current_turn_number == 1

        # Add some guesses
        guess1 = ClueGuess(
            suspect=ValidSuspect.MR_GREEN,
            weapon=ValidWeapon.KNIFE,
            room=ValidRoom.KITCHEN,
        )
        state.guesses.append(guess1)
        assert state.current_turn_number == 2

        guess2 = ClueGuess(
            suspect=ValidSuspect.MRS_WHITE,
            weapon=ValidWeapon.WRENCH,
            room=ValidRoom.HALL,
        )
        state.guesses.append(guess2)
        assert state.current_turn_number == 3

    def test_is_game_over_property(self):
        """Test is_game_over property."""
        solution = ClueSolution(
            suspect=ValidSuspect.PROFESSOR_PLUM,
            weapon=ValidWeapon.LEAD_PIPE,
            room=ValidRoom.CONSERVATORY,
        )
        state = ClueState(solution=solution)

        # Game starts as ongoing
        assert not state.is_game_over
        assert state.game_status == "ongoing"

        # Player 1 wins
        state.game_status = "player1_win"
        assert state.is_game_over

        # Player 2 wins
        state.game_status = "player2_win"
        assert state.is_game_over

    def test_board_string_property_empty(self):
        """Test board_string property with no guesses."""
        state = ClueState.initialize()
        assert state.board_string == "No guesses yet."

    def test_board_string_property_with_guesses(self):
        """Test board_string property with guesses and responses."""
        state = ClueState.initialize()

        # Add first guess and response
        guess1 = ClueGuess(
            suspect=ValidSuspect.COLONEL_MUSTARD,
            weapon=ValidWeapon.CANDLESTICK,
            room=ValidRoom.LIBRARY,
        )
        response1 = ClueResponse(is_correct=False, card_shown="Library")
        state.guesses.append(guess1)
        state.responses.append(response1)

        board = state.board_string
        assert "Turn 1:" in board
        assert "Colonel Mustard, Candlestick, Library" in board
        assert "Response: Library" in board

        # Add second guess with no card shown
        guess2 = ClueGuess(
            suspect=ValidSuspect.MISS_SCARLET,
            weapon=ValidWeapon.ROPE,
            room=ValidRoom.STUDY,
        )
        response2 = ClueResponse(is_correct=False, card_shown=None)
        state.guesses.append(guess2)
        state.responses.append(response2)

        board = state.board_string
        assert "Turn 2:" in board
        assert "Miss Scarlet, Rope, Study" in board
        assert "Response: No card shown" in board

    def test_board_string_with_mismatched_guesses_responses(self):
        """Test board_string handles mismatched guesses and responses."""
        state = ClueState.initialize()

        # Add more guesses than responses
        guess1 = ClueGuess(
            suspect=ValidSuspect.MR_GREEN,
            weapon=ValidWeapon.KNIFE,
            room=ValidRoom.KITCHEN,
        )
        guess2 = ClueGuess(
            suspect=ValidSuspect.MRS_PEACOCK,
            weapon=ValidWeapon.REVOLVER,
            room=ValidRoom.BALLROOM,
        )
        response1 = ClueResponse(is_correct=False, card_shown="Kitchen")

        state.guesses.extend([guess1, guess2])
        state.responses.append(response1)

        # Should handle gracefully with zip
        board = state.board_string
        assert "Turn 1:" in board
        assert "Turn 2:" not in board  # No response for second guess


class TestClueStateManipulation:
    """Test manipulating ClueState."""

    def test_adding_guesses_and_responses(self):
        """Test adding guesses and responses to state."""
        state = ClueState.initialize()

        # Add a guess
        guess = ClueGuess(
            suspect=ValidSuspect.PROFESSOR_PLUM,
            weapon=ValidWeapon.LEAD_PIPE,
            room=ValidRoom.CONSERVATORY,
        )
        state.guesses.append(guess)
        assert len(state.guesses) == 1
        assert state.guesses[0] == guess

        # Add a response
        response = ClueResponse(is_correct=False, card_shown="Lead Pipe")
        state.responses.append(response)
        assert len(state.responses) == 1
        assert state.responses[0] == response

    def test_switching_players(self):
        """Test switching between players."""
        state = ClueState.initialize()

        assert state.current_player == "player1"
        state.current_player = "player2"
        assert state.current_player == "player2"
        state.current_player = "player1"
        assert state.current_player == "player1"

    def test_game_end_conditions(self):
        """Test various game end conditions."""
        state = ClueState.initialize()

        # Test player 1 win
        state.game_status = "player1_win"
        state.winner = "player1"
        assert state.is_game_over
        assert state.winner == "player1"

        # Reset and test player 2 win
        state.game_status = "player2_win"
        state.winner = "player2"
        assert state.is_game_over
        assert state.winner == "player2"

    def test_max_turns_reached(self):
        """Test behavior when max turns is reached."""
        state = ClueState.initialize(max_turns=3)

        # Add guesses up to max turns
        for _i in range(3):
            guess = ClueGuess(
                suspect=ValidSuspect.MISS_SCARLET,
                weapon=ValidWeapon.ROPE,
                room=ValidRoom.STUDY,
            )
            state.guesses.append(guess)

        # Check that we've reached max turns
        assert len(state.guesses) == state.max_turns
        assert state.current_turn_number == 4  # Next turn would be 4

    def test_hypothesis_tracking(self):
        """Test tracking player hypotheses."""
        state = ClueState.initialize()

        # Add hypothesis for player 1
        hyp1 = {
            "suspect": "Colonel Mustard",
            "weapon": "Candlestick",
            "room": "Library",
            "confidence": 0.7,
        }
        state.player1_hypotheses.append(hyp1)
        assert len(state.player1_hypotheses) == 1
        assert state.player1_hypotheses[0] == hyp1

        # Add hypothesis for player 2
        hyp2 = {
            "suspect": "Miss Scarlet",
            "weapon": "Rope",
            "room": "Study",
            "confidence": 0.9,
        }
        state.player2_hypotheses.append(hyp2)
        assert len(state.player2_hypotheses) == 1
        assert state.player2_hypotheses[0] == hyp2


class TestClueStateValidation:
    """Test validation and edge cases for ClueState."""

    def test_state_with_all_enum_values(self):
        """Test state can handle all enum values."""
        # Test with each suspect
        for suspect in ValidSuspect:
            solution = ClueSolution(
                suspect=suspect,
                weapon=ValidWeapon.KNIFE,
                room=ValidRoom.KITCHEN,
            )
            state = ClueState(solution=solution)
            assert state.solution.suspect == suspect

        # Test with each weapon
        for weapon in ValidWeapon:
            solution = ClueSolution(
                suspect=ValidSuspect.MISS_SCARLET,
                weapon=weapon,
                room=ValidRoom.KITCHEN,
            )
            state = ClueState(solution=solution)
            assert state.solution.weapon == weapon

        # Test with each room
        for room in ValidRoom:
            solution = ClueSolution(
                suspect=ValidSuspect.MISS_SCARLET,
                weapon=ValidWeapon.KNIFE,
                room=room,
            )
            state = ClueState(solution=solution)
            assert state.solution.room == room

    def test_state_serialization(self):
        """Test that state can be serialized and deserialized."""
        state = ClueState.initialize()

        # Add some data
        guess = ClueGuess(
            suspect=ValidSuspect.MR_GREEN,
            weapon=ValidWeapon.WRENCH,
            room=ValidRoom.BILLIARD_ROOM,
        )
        state.guesses.append(guess)
        state.current_player = "player2"
        state.winner = "player1"
        state.game_status = "player1_win"

        # Serialize to dict
        state_dict = (
            state.model_dump() if hasattr(state, "model_dump") else state.dict()
        )

        # Deserialize back
        new_state = ClueState(**state_dict)

        # Verify fields match
        assert new_state.current_player == state.current_player
        assert new_state.winner == state.winner
        assert new_state.game_status == state.game_status
        assert len(new_state.guesses) == len(state.guesses)

    def test_independent_state_instances(self):
        """Test that state instances are independent."""
        state1 = ClueState.initialize()
        state2 = ClueState.initialize()

        # Modify state1
        guess = ClueGuess(
            suspect=ValidSuspect.COLONEL_MUSTARD,
            weapon=ValidWeapon.CANDLESTICK,
            room=ValidRoom.LIBRARY,
        )
        state1.guesses.append(guess)
        state1.current_player = "player2"

        # Verify state2 is unaffected
        assert len(state2.guesses) == 0
        assert state2.current_player == "player1"

    def test_state_with_empty_player_cards(self):
        """Test state can handle empty player card lists."""
        solution = ClueSolution(
            suspect=ValidSuspect.MISS_SCARLET,
            weapon=ValidWeapon.ROPE,
            room=ValidRoom.STUDY,
        )
        state = ClueState(
            solution=solution,
            player1_cards=[],
            player2_cards=[],
        )

        assert state.player1_cards == []
        assert state.player2_cards == []
        assert state.board_string == "No guesses yet."
