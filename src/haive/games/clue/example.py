"""Clue example module.

This module provides an example of running a Clue game with the rich UI visualization.

It demonstrates how to:
    - Configure and initialize the Clue game
    - Set up the game state
    - Visualize the game with the rich UI
    - Process game turns with guesses and responses
    - Handle game over conditions

The module uses a standard CLI interface with argument parsing
to allow customization of game behavior.

Example:
    Run this script directly to start a Clue game:
        python -m haive.games.clue.example

    Command-line options:
        --debug: Enable debug mode with detailed logging
        --turns: Set maximum number of turns (default: 10)
        --delay: Set delay between moves in seconds (default: 1.0)
"""

import argparse
import logging
import random
import time
import traceback

from .clue.models import (
    CardType,
    ClueCard,
    ClueGuess,
    ClueHypothesis,
    ClueResponse,
    ClueSolution,
    ValidRoom,
    ValidSuspect,
    ValidWeapon,
)
from .clue.state import ClueState
from .clue.state_manager import ClueStateManager
from .clue.ui import ClueUI

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_clue_game(debug: bool = False, max_turns: int = 10, delay: float = 1.0):
    """Run a Clue game with rich UI visualization.

    This function sets up and runs a Clue game with test moves (for demonstration)
    with rich terminal visualization. It handles a simplified game flow with
    a few predetermined moves for UI testing.

    Args:
        debug (bool): Enable debug mode with detailed logging
        max_turns (int): Maximum number of turns before the game ends
        delay (float): Delay between moves in seconds for better readability

    Returns:
        None

    Example:
        >>> run_clue_game(debug=True, max_turns=5, delay=0.5)
        # Runs a test game with debug logging, 5 max turns, and 0.5s delay
    """
    # Create the UI
    ui = ClueUI()

    try:
        # For testing, we'll create a state manually instead of using the
        # ClueStateManager.initialize which expects a different format

        # Create a basic board setup
        [suspect.value for suspect in ValidSuspect]
        [weapon.value for weapon in ValidWeapon]
        [room.value for room in ValidRoom]

        # Define a predetermined solution for testing
        solution = ClueSolution(
            suspect=ValidSuspect.COLONEL_MUSTARD,
            weapon=ValidWeapon.KNIFE,
            room=ValidRoom.KITCHEN,
        )

        # Create a list of remaining cards (excluding solution)
        remaining_suspects = [
            s.value for s in ValidSuspect if s != ValidSuspect.COLONEL_MUSTARD
        ]
        remaining_weapons = [w.value for w in ValidWeapon if w != ValidWeapon.KNIFE]
        remaining_rooms = [r.value for r in ValidRoom if r != ValidRoom.KITCHEN]

        # Combine all remaining cards
        all_remaining_cards = remaining_suspects + remaining_weapons + remaining_rooms

        # Shuffle and split between players
        random.shuffle(all_remaining_cards)
        midpoint = len(all_remaining_cards) // 2
        player1_cards = all_remaining_cards[:midpoint]
        player2_cards = all_remaining_cards[midpoint:]

        # Create the state
        state = ClueState(
            solution=solution,
            guesses=[],
            responses=[],
            player1_cards=player1_cards,
            player2_cards=player2_cards,
            current_player="player1",
            max_turns=max_turns,
            game_status="ongoing",
            player1_hypotheses=[],
            player2_hypotheses=[],
        )

        # Display initial state
        ui.display_state(state)
        time.sleep(delay)

        # Define some mock hypotheses
        player1_hypothesis = ClueHypothesis(
            prime_suspect=ValidSuspect.PROFESSOR_PLUM,
            prime_weapon=ValidWeapon.KNIFE,
            prime_room=ValidRoom.LIBRARY,
            confidence=0.4,
            excluded_suspects=[ValidSuspect.MRS_WHITE, ValidSuspect.MR_GREEN],
            excluded_weapons=[ValidWeapon.ROPE],
            excluded_rooms=[ValidRoom.BALLROOM, ValidRoom.CONSERVATORY],
            reasoning="Based on the cards in my hand and guesses so far.",
        )

        player2_hypothesis = ClueHypothesis(
            prime_suspect=ValidSuspect.COLONEL_MUSTARD,
            prime_weapon=ValidWeapon.WRENCH,
            prime_room=ValidRoom.KITCHEN,
            confidence=0.35,
            excluded_suspects=[ValidSuspect.MISS_SCARLET],
            excluded_weapons=[ValidWeapon.CANDLESTICK, ValidWeapon.REVOLVER],
            excluded_rooms=[ValidRoom.STUDY, ValidRoom.HALL],
            reasoning="Process of elimination from previous guesses.",
        )

        # Add the hypotheses to the state
        state = ClueStateManager.add_analysis(
            state, "player1", player1_hypothesis.to_dict()
        )
        state = ClueStateManager.add_analysis(
            state, "player2", player2_hypothesis.to_dict()
        )

        # Display updated state with hypotheses
        ui.display_state(state)
        time.sleep(delay)

        # Predefined guesses for testing
        test_guesses = [
            # Player 1's guesses
            (
                ClueGuess(
                    suspect=ValidSuspect.PROFESSOR_PLUM,
                    weapon=ValidWeapon.ROPE,
                    room=ValidRoom.LIBRARY,
                ),
                "player1",
            ),
            # Player 2's guesses
            (
                ClueGuess(
                    suspect=ValidSuspect.MISS_SCARLET,
                    weapon=ValidWeapon.CANDLESTICK,
                    room=ValidRoom.BALLROOM,
                ),
                "player2",
            ),
            # Player 1's guesses
            (
                ClueGuess(
                    suspect=ValidSuspect.COLONEL_MUSTARD,
                    weapon=ValidWeapon.WRENCH,
                    room=ValidRoom.KITCHEN,
                ),
                "player1",
            ),
            # Player 2's guesses
            (
                ClueGuess(
                    suspect=ValidSuspect.COLONEL_MUSTARD,
                    weapon=ValidWeapon.KNIFE,
                    room=ValidRoom.STUDY,
                ),
                "player2",
            ),
            # Player 1's winning guess
            (
                ClueGuess(
                    suspect=ValidSuspect.COLONEL_MUSTARD,
                    weapon=ValidWeapon.KNIFE,
                    room=ValidRoom.KITCHEN,
                ),
                "player1",
            ),
        ]

        # Process each guess
        for guess, player in test_guesses:
            # Make sure it's the right player's turn
            if state.current_player != player:
                # Skip this guess if it's not this player's turn
                continue

            # Show thinking animation
            ui.show_thinking(player, "Analyzing clues...")
            time.sleep(delay * 0.5)

            # Show the guess
            ui.show_guess(guess, player)

            # Check if the guess matches the solution
            if (
                guess.suspect == solution.suspect
                and guess.weapon == solution.weapon
                and guess.room == solution.room
            ):
                # Winning move
                response = ClueResponse(is_correct=True)
                ui.show_response(response, player)

                # Update state
                state.guesses.append(guess)
                state.responses.append(response)
                state.game_status = f"{player}_win"
                state.winner = player

                # Display final state
                ui.display_state(state)
                ui.show_game_over(state)
                break
            # Find any refuting cards
            other_player = "player2" if player == "player1" else "player1"
            other_player_cards = (
                state.player2_cards if player == "player1" else state.player1_cards
            )

            refuting_cards = []

            # Check if other player has any matching cards
            if guess.suspect.value in other_player_cards:
                refuting_cards.append(
                    ClueCard(name=guess.suspect.value, card_type=CardType.SUSPECT)
                )
            if guess.weapon.value in other_player_cards:
                refuting_cards.append(
                    ClueCard(name=guess.weapon.value, card_type=CardType.WEAPON)
                )
            if guess.room.value in other_player_cards:
                refuting_cards.append(
                    ClueCard(name=guess.room.value, card_type=CardType.ROOM)
                )

            if refuting_cards:
                # Other player refutes with a random card
                refuting_card = random.choice(refuting_cards)
                response = ClueResponse(
                    is_correct=False,
                    responding_player=other_player,
                    refuting_card=refuting_card,
                )
            else:
                # No one can refute
                response = ClueResponse(
                    is_correct=False,
                    responding_player=None,
                    refuting_card=None,
                )

            # Show the response
            ui.show_response(response, player)

            # Update state
            state.guesses.append(guess)
            state.responses.append(response)
            state.current_player = "player2" if player == "player1" else "player1"

            # Display updated state
            ui.display_state(state)
            time.sleep(delay)

            # Add new hypotheses
            if player == "player1":
                # Update hypothesis based on new information
                player1_hypothesis.confidence += 0.1
                player1_hypothesis.reasoning += " Updated with new information."
                state = ClueStateManager.add_analysis(
                    state, "player1", player1_hypothesis.to_dict()
                )
            else:
                # Update hypothesis based on new information
                player2_hypothesis.confidence += 0.15
                player2_hypothesis.reasoning += " Getting closer to the solution."
                state = ClueStateManager.add_analysis(
                    state, "player2", player2_hypothesis.to_dict()
                )

            # Check if max turns reached
            if len(state.guesses) >= max_turns:
                # Game over - no winner
                state.game_status = "draw"
                ui.display_state(state)
                ui.show_game_over(state)
                break

    except Exception as e:
        logger.error(f"Error during game: {e}")
        traceback.print_exc()

    logger.info("Game complete!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a Clue game with rich UI")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("--turns", type=int, default=10, help="Maximum number of turns")
    parser.add_argument(
        "--delay", type=float, default=1.0, help="Delay between moves (seconds)"
    )

    args = parser.parse_args()

    # Set logging level based on debug flag
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    # Run the game
    run_clue_game(debug=args.debug, max_turns=args.turns, delay=args.delay)
