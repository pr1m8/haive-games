"""Mock runner for the Mafia game.

This module provides a simplified version of the Mafia game runner that
uses mock responses instead of actual LLMs, allowing for faster testing
and demonstration without requiring API keys or internet access.

Example:
    ```bash
    python mock_runner.py --players 5 --days 1 --debug
    ```

"""

import argparse
import logging
import random
import time
import traceback
import uuid
from typing import Any

from haive.games.mafia.agent import MafiaAgent
from haive.games.mafia.config import MafiaAgentConfig
from haive.games.mafia.models import (
    ActionType,
    GamePhase,
    MafiaAction,
    MafiaPlayerDecision,
    NarratorAction,
    NarratorDecision,
    PlayerRole,
)
from haive.games.mafia.state_manager import MafiaStateManager

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Mock response generators
def generate_villager_response(context: dict[str, Any]) -> MafiaPlayerDecision:
    """Generate a mock response for a villager player."""
    phase = context.get("phase", "")
    player_id = context.get("player_id", "")
    alive_players = context.get("alive_players", [])

    # Filter out self from target options
    possible_targets = [
        p for p in alive_players if p != player_id and p.lower() != "narrator"
    ]

    if phase == GamePhase.DAY_DISCUSSION.value:
        # During discussion, just speak
        return MafiaPlayerDecision(
            action=MafiaAction(
                player_id=player_id,
                action_type=ActionType.SPEAK,
                message="I suspect one of you is the mafia...",
                phase=GamePhase.DAY_DISCUSSION,
                round_number=context.get("round_number", 1),
            ),
            reasoning="Just making conversation",
        )

    if phase == GamePhase.DAY_VOTING.value:
        # During voting, choose someone to vote for
        if possible_targets:
            target = random.choice(possible_targets)
            return MafiaPlayerDecision(
                action=MafiaAction(
                    player_id=player_id,
                    action_type=ActionType.VOTE,
                    target_id=target,
                    phase=GamePhase.DAY_VOTING,
                    round_number=context.get("round_number", 1),
                ),
                reasoning=f"I'm suspicious of {target}",
            )

    # Default fallback
    return MafiaPlayerDecision(
        action=MafiaAction(
            player_id=player_id,
            action_type=ActionType.SPEAK,
            message="I have nothing to say.",
            phase=GamePhase(phase) if phase else GamePhase.DAY_DISCUSSION,
            round_number=context.get("round_number", 1),
        ),
        reasoning="No specific actions needed",
    )


def generate_mafia_response(context: dict[str, Any]) -> MafiaPlayerDecision:
    """Generate a mock response for a mafia player."""
    phase = context.get("phase", "")
    player_id = context.get("player_id", "")
    alive_players = context.get("alive_players", [])

    # Filter out self and other mafia from target options
    private_info = context.get("private_info", [])
    other_mafia = []
    for info in private_info:
        if "fellow mafia" in info:
            other_mafia = [name.strip() for name in info.split(":")[-1].split(",")]

    possible_targets = [
        p
        for p in alive_players
        if p != player_id and p.lower() != "narrator" and p not in other_mafia
    ]

    if phase == GamePhase.NIGHT.value:
        # At night, kill someone
        if possible_targets:
            target = random.choice(possible_targets)
            return MafiaPlayerDecision(
                action=MafiaAction(
                    player_id=player_id,
                    action_type=ActionType.KILL,
                    target_id=target,
                    phase=GamePhase.NIGHT,
                    round_number=context.get("round_number", 1),
                ),
                reasoning=f"Targeting {target} for elimination",
            )

    elif phase == GamePhase.DAY_DISCUSSION.value:
        # During discussion, act innocent
        return MafiaPlayerDecision(
            action=MafiaAction(
                player_id=player_id,
                action_type=ActionType.SPEAK,
                message="I think we need to be careful about our accusations.",
                phase=GamePhase.DAY_DISCUSSION,
                round_number=context.get("round_number", 1),
            ),
            reasoning="Maintaining cover",
        )

    elif phase == GamePhase.DAY_VOTING.value:
        # During voting, choose someone to vote for (not self or other mafia)
        if possible_targets:
            target = random.choice(possible_targets)
            return MafiaPlayerDecision(
                action=MafiaAction(
                    player_id=player_id,
                    action_type=ActionType.VOTE,
                    target_id=target,
                    phase=GamePhase.DAY_VOTING,
                    round_number=context.get("round_number", 1),
                ),
                reasoning=f"Deflecting suspicion by voting for {target}",
            )

    # Default fallback
    return MafiaPlayerDecision(
        action=MafiaAction(
            player_id=player_id,
            action_type=ActionType.SPEAK,
            message="I'm not sure what to do here.",
            phase=GamePhase(phase) if phase else GamePhase.DAY_DISCUSSION,
            round_number=context.get("round_number", 1),
        ),
        reasoning="No specific actions needed",
    )


def generate_detective_response(context: dict[str, Any]) -> MafiaPlayerDecision:
    """Generate a mock response for a detective player."""
    phase = context.get("phase", "")
    player_id = context.get("player_id", "")
    alive_players = context.get("alive_players", [])

    # Filter out self from target options
    possible_targets = [
        p for p in alive_players if p != player_id and p.lower() != "narrator"
    ]

    if phase == GamePhase.NIGHT.value:
        # At night, investigate someone
        if possible_targets:
            target = random.choice(possible_targets)
            return MafiaPlayerDecision(
                action=MafiaAction(
                    player_id=player_id,
                    action_type=ActionType.INVESTIGATE,
                    target_id=target,
                    phase=GamePhase.NIGHT,
                    round_number=context.get("round_number", 1),
                ),
                reasoning=f"Investigating {target} to determine if they are mafia",
            )

    # For other phases, act like a villager
    return generate_villager_response(context)


def generate_doctor_response(context: dict[str, Any]) -> MafiaPlayerDecision:
    """Generate a mock response for a doctor player."""
    phase = context.get("phase", "")
    player_id = context.get("player_id", "")
    alive_players = context.get("alive_players", [])

    # Include self in possible targets (doctor can save self)
    possible_targets = [p for p in alive_players if p.lower() != "narrator"]

    if phase == GamePhase.NIGHT.value:
        # At night, save someone
        if possible_targets:
            target = random.choice(possible_targets)
            return MafiaPlayerDecision(
                action=MafiaAction(
                    player_id=player_id,
                    action_type=ActionType.SAVE,
                    target_id=target,
                    phase=GamePhase.NIGHT,
                    round_number=context.get("round_number", 1),
                ),
                reasoning=f"Protecting {target} from potential harm tonight",
            )

    # For other phases, act like a villager
    return generate_villager_response(context)


def generate_narrator_response(context: dict[str, Any]) -> NarratorDecision:
    """Generate a mock response for the narrator."""
    phase = context.get("phase", "")
    day_number = context.get("day_number", 0)
    round_number = context.get("round_number", 0)

    # Phase transition logic
    if phase == GamePhase.NIGHT.value:
        # Check if all night actions complete
        phase_info = context.get("phase_info", {})
        expected_actions = phase_info.get("expected_actions", 0)
        completed_actions = phase_info.get("completed_actions", 0)

        if completed_actions >= expected_actions:
            # Transition to day
            return NarratorDecision(
                action=NarratorAction(
                    announcement=f"The sun rises on day {day_number}. The village awakens.",
                    phase_transition=True,
                    round_number=round_number,
                ),
                reasoning="All night actions are complete, moving to day phase",
            )

    elif phase == GamePhase.DAY_DISCUSSION.value:
        # Check if discussion complete
        return NarratorDecision(
            action=NarratorAction(
                announcement="The discussion period has ended. It is time to vote.",
                phase_transition=True,
                round_number=round_number,
            ),
            reasoning="Discussion phase complete, moving to voting",
        )

    elif phase == GamePhase.DAY_VOTING.value:
        # Check if voting complete
        phase_info = context.get("phase_info", {})
        expected_votes = phase_info.get("expected_votes", 0)
        completed_votes = phase_info.get("completed_votes", 0)

        if completed_votes >= expected_votes:
            # Count votes
            vote_counts = phase_info.get("vote_counts", {})
            most_votes = 0
            executed = None

            for player, count in vote_counts.items():
                if count > most_votes:
                    most_votes = count
                    executed = player

            # Transition to night
            return NarratorDecision(
                action=NarratorAction(
                    announcement=(
                        f"The votes are in. {executed} has been executed by the village."
                        if executed
                        else "No one received any votes. The village decides not to execute anyone."
                    ),
                    phase_transition=True,
                    round_number=round_number,
                ),
                reasoning="Voting complete, transitioning to night phase",
            )

    # Default: No phase transition, just narrate
    return NarratorDecision(
        action=NarratorAction(
            announcement="The narrator observes silently.",
            phase_transition=False,
            round_number=round_number,
        ),
        reasoning="Waiting for players to complete their actions",
    )


# Mock engine class
class MockEngine:
    """A mock engine that returns predefined responses."""

    def __init__(self, role):
        self.role = role

    def invoke(self, context):
        """Generate a mock response based on the role."""
        try:
            if self.role.lower() == "villager":
                return generate_villager_response(context)
            if self.role.lower() == "mafia":
                return generate_mafia_response(context)
            if self.role.lower() == "detective":
                return generate_detective_response(context)
            if self.role.lower() == "doctor":
                return generate_doctor_response(context)
            if self.role.lower() == "narrator":
                return generate_narrator_response(context)
            # Default to villager
            return generate_villager_response(context)
        except Exception as e:
            logger.error(f"Error in mock engine for {self.role}: {e}")
            # Return a simple default response
            return MafiaPlayerDecision(
                action=MafiaAction(
                    player_id=context.get("player_id", "Unknown"),
                    action_type=ActionType.SPEAK,
                    message="I pass my turn.",
                    phase=GamePhase(context.get("phase", "day_discussion")),
                    round_number=context.get("round_number", 1),
                ),
                reasoning="Error occurred, using fallback",
            )


def run_mafia_game_mock(
    player_count: int = 5, max_days: int = 1, debug: bool = True
) -> None:
    """Run a mock Mafia game simulation with synthetic responses.

    This function sets up and executes a full Mafia game, handling:
        - Player creation and role assignment
        - Game state initialization
        - Turn-based gameplay execution using mock responses
        - State visualization
        - Game end conditions

    Args:
        player_count: Total number of players including narrator.
            Must be at least 4 (3 players + narrator). Defaults to 5.
        max_days: Maximum number of in-game days before forcing
            game end. Defaults to 1.
        debug: Enable debug mode for detailed logging.
            Defaults to True.

    Raises:
        ValueError: If player_count is less than 4.

    """
    print("\n🎭 Setting up Mafia Game (MOCK VERSION)")
    print("=" * 60)
    print(f"Number of players: {player_count}")
    print(f"Maximum days: {max_days}")
    print(f"Debug mode: {'Enabled' if debug else 'Disabled'}")
    print("=" * 60)

    try:
        # Create agent config
        config = MafiaAgentConfig.default_config(
            player_count=player_count, max_days=max_days
        )
        config.debug = debug

        # Create the agent
        print("\n🎮 Creating Mafia agent")
        agent = MafiaAgent(config)

        # Replace engines with mock engines
        for role in agent.engines:
            agent.engines[role]["player"] = MockEngine(role)

        print("\n✓ Replaced LLM engines with mock engines")

        # Generate player names
        player_names = [f"Player_{i + 1}" for i in range(player_count - 1)]
        player_names.append("Narrator")  # Add narrator as the last player

        # Initialize game state
        print("\n🎲 Initializing game state")
        game_state = MafiaStateManager.initialize(player_names)

        if debug:
            print("\n🎲 Game Role Assignment:")
            for player_id, role in game_state.roles.items():
                print(f"  {player_id}: {role.value}")

        # Run the game
        print("\n🎭 Starting Mafia Game")
        print("=" * 60)
        print(f"Players: {', '.join(player_names[:-1])} + Narrator")
        print("=" * 60)

        # Track day count to prevent infinite games
        current_day = 0

        # Thread ID for consistency
        str(uuid.uuid4())

        # Execution counter to prevent infinite loops
        execution_counter = 0
        max_executions = 100  # Limit total state transitions

        # Main game loop
        while (
            game_state.game_status == "ongoing"
            and current_day <= max_days
            and execution_counter < max_executions
        ):
            execution_counter += 1

            # Visualize current state
            agent.visualize_state(game_state, debug=debug)

            # Add a very slight delay for better readability
            time.sleep(0.1)

            # Process the current phase
            if game_state.game_phase == GamePhase.SETUP:
                # Move from setup to night phase
                game_state = MafiaStateManager.advance_phase(game_state)
                continue

            # Get the current player
            current_idx = game_state.current_player_idx
            player_id = game_state.players[current_idx]

            # Debug output
            if debug:
                print(player_id)

            # Check if player is alive (skip if dead, except narrator)
            if (
                player_id in game_state.player_states
                and not game_state.player_states[player_id].is_alive
                and game_state.roles.get(player_id) != PlayerRole.NARRATOR
            ):
                # Advance to next player
                next_idx = (current_idx + 1) % len(game_state.players)
                game_state.current_player_idx = next_idx
                continue

            # Get player's role
            player_role = agent.get_player_role(game_state, player_id)

            # Handle narrator turn differently
            if player_role == PlayerRole.NARRATOR or player_id.lower() == "narrator":
                # Prepare context for the narrator
                context = agent.prepare_narrator_context(game_state)

                # Get narrator engine
                narrator_engine = None
                for key in agent.engines:
                    if key.lower() == "narrator" and "player" in agent.engines[key]:
                        narrator_engine = agent.engines[key]["player"]
                        break

                if narrator_engine:
                    try:
                        # Get decision from narrator
                        response = narrator_engine.invoke(context)

                        # Extract action
                        action = agent.extract_move(response, player_id)

                        # Apply action
                        game_state = MafiaStateManager.apply_move(
                            game_state, player_id, action
                        )

                        # Check if we need to transition phases
                        if (
                            hasattr(action, "phase_transition")
                            and action.phase_transition
                        ):
                            game_state = MafiaStateManager.advance_phase(game_state)
                    except Exception as e:
                        logger.error(f"Error in narrator turn: {e}")
                else:
                    logger.error("No narrator engine found")
            else:
                # Handle regular player turn
                move_engine = agent.get_engine_for_player(player_role, "player")

                if move_engine:
                    try:
                        # Prepare context for the move
                        context = agent.prepare_move_context(game_state, player_id)

                        # Get player's decision
                        response = move_engine.invoke(context)

                        # Extract move
                        move = agent.extract_move(response, player_id)

                        # Apply move
                        game_state = MafiaStateManager.apply_move(
                            game_state, player_id, move
                        )
                    except Exception as e:
                        logger.error(f"Error in player {player_id}'s turn: {e}")
                else:
                    logger.error(f"No move engine found for player {player_id}")

            # Advance to next player
            next_idx = (current_idx + 1) % len(game_state.players)
            game_state.current_player_idx = next_idx

            # Check if we need to transition phases
            if game_state.game_phase == GamePhase.NIGHT:
                # Check if all special role night actions are complete
                all_night_actions_complete = True
                for pid, role in game_state.roles.items():
                    if (
                        role
                        in [PlayerRole.MAFIA, PlayerRole.DOCTOR, PlayerRole.DETECTIVE]
                        and pid in game_state.player_states
                        and game_state.player_states[pid].is_alive
                    ):
                        # Check if this player has acted this round
                        has_acted = False
                        for action in reversed(game_state.action_history):
                            action_player = (
                                action.get("player_id")
                                if isinstance(action, dict)
                                else getattr(action, "player_id", None)
                            )
                            action_phase = (
                                action.get("phase")
                                if isinstance(action, dict)
                                else getattr(action, "phase", None)
                            )
                            action_round = (
                                action.get("round_number")
                                if isinstance(action, dict)
                                else getattr(action, "round_number", None)
                            )

                            if isinstance(action_phase, GamePhase):
                                action_phase = action_phase.value

                            if (
                                action_player == pid
                                and action_phase == GamePhase.NIGHT.value
                                and action_round == game_state.round_number
                            ):
                                has_acted = True
                                break

                        if not has_acted:
                            all_night_actions_complete = False
                            break

                # If narrator's turn and all night actions are complete,
                # transition to day
                if all_night_actions_complete and player_role == PlayerRole.NARRATOR:
                    game_state = MafiaStateManager.advance_phase(game_state)

            elif game_state.game_phase == GamePhase.DAY_VOTING:
                # Count alive players
                alive_players = [
                    pid
                    for pid, p_state in game_state.player_states.items()
                    if p_state.is_alive
                    and game_state.roles.get(pid) != PlayerRole.NARRATOR
                ]

                # If all votes are in and narrator's turn, transition to night
                if (
                    len(game_state.votes) >= len(alive_players)
                    and player_role == PlayerRole.NARRATOR
                ):
                    game_state = MafiaStateManager.advance_phase(game_state)

            # Check game status
            game_state = MafiaStateManager.check_game_status(game_state)

            # Update day count when day changes
            current_day = max(current_day, game_state.day_number)

            # Check if we've reached max days
            if current_day > max_days:
                print(f"\n⏰ Maximum days ({max_days}) reached. Ending game.")
                game_state.game_status = "ended"
                game_state.game_phase = GamePhase.GAME_OVER
                break

        # Check if we hit the execution limit
        if execution_counter >= max_executions:
            print(
                f"\n⚠️ Reached maximum execution limit ({max_executions}). Ending game."
            )
            game_state.game_status = "ended"
            game_state.game_phase = GamePhase.GAME_OVER

        # Final visualization
        agent.visualize_state(game_state, debug=debug)

        # Save game history
        try:
            print("\n📊 Saving game history")
            agent.save_state_history()
            print("✅ Game history saved successfully")
        except Exception as save_error:
            print(f"⚠️ Could not save game history: {save_error}")
            if debug:
                traceback.print_exc()

    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        if debug:
            traceback.print_exc()

    print("\n✅ Game Complete!")


def main():
    """Main entry point for command-line execution."""
    parser = argparse.ArgumentParser(description="Run a simple Mafia game simulation")
    parser.add_argument(
        "--players",
        type=int,
        default=5,
        help="Number of players (including narrator, minimum 4)",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=1,
        help="Maximum number of days before forcing game end",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")

    args = parser.parse_args()

    # Set logging level based on debug flag
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    # Validate arguments
    if args.players < 4:
        parser.error("Minimum 4 players required (3 players + narrator)")

    # Run the game
    run_mafia_game_mock(player_count=args.players, max_days=args.days, debug=args.debug)


if __name__ == "__main__":
    main()
