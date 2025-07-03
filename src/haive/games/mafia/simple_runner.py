"""Simple runner for the Mafia game that avoids LangGraph issues.

This module provides a simplified version of the Mafia game runner that
avoids the streaming issues in LangGraph by:
    - Using direct state manipulation instead of graph streaming
    - Following the game logic manually through phases
    - Providing the same visualization and game experience

Example:
    ```bash
    python simple_runner.py --players 7 --days 3 --debug
    ```
"""

import argparse
import logging
import time
import uuid

from haive.games.mafia.agent import MafiaAgent
from haive.games.mafia.config import MafiaAgentConfig
from haive.games.mafia.models import (
    GamePhase,
    PlayerRole,
)
from haive.games.mafia.state_manager import MafiaStateManager

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_mafia_game_simple(
    player_count: int = 5, max_days: int = 1, debug: bool = True
) -> None:
    """Run a simplified Mafia game simulation with direct state management.

    This function sets up and executes a full Mafia game, handling:
        - Player creation and role assignment
        - Game state initialization
        - Turn-based gameplay execution
        - State visualization
        - Game end conditions

    Args:
        player_count: Total number of players including narrator.
            Must be at least 4 (3 players + narrator). Defaults to 5.
        max_days: Maximum number of in-game days before forcing
            game end. Defaults to 3.
        debug: Enable debug mode for detailed logging.
            Defaults to True.

    Raises:
        ValueError: If player_count is less than 4.
    """
    print("\n🎭 Setting up Mafia Game")
    print("=" * 60)
    print(f"Number of players: {player_count}")
    print(f"Maximum days: {max_days}")
    print(f"Debug mode: {'Enabled' if debug else 'Disabled'}")
    print("=" * 60)

    try:
        # Print available configs for debugging
        if debug:
            from haive.games.mafia.engines import aug_llm_configs

            print("\n🔧 Available Engine Configs:")
            for role, engines in aug_llm_configs.items():
                print(f"  {role}: {list(engines.keys())}")

        # Create agent config
        config = MafiaAgentConfig.default_config(
            player_count=player_count, max_days=max_days
        )

        # Set debug mode
        config.debug = debug

        # Create the agent
        print("\n🎮 Creating Mafia agent")
        agent = MafiaAgent(config)

        # Generate player names
        player_names = [f"Player_{i+1}" for i in range(player_count - 1)]
        player_names.append("Narrator")  # Add narrator as the last player

        # Dump engine keys for debugging
        if debug:
            print("\n🔧 Available Engines in Agent:")
            for key, value in agent.engines.items():
                print(
                    f"  {key}: {list(value.keys()) if isinstance(value, dict) else 'None'}"
                )

            print("\n🔑 Role to Engine Mapping:")
            for role, engine_key in agent.role_enum_mapping.items():
                print(f"  {role}: {engine_key}")

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

        # Main game loop
        while game_state.game_status == "ongoing" and current_day <= max_days:
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

            # Check if player is alive (skip if dead, except narrator)
            if (
                player_id in game_state.player_states
                and not game_state.player_states[player_id].is_alive
                and game_state.roles.get(player_id) != GamePhase.NARRATOR
            ):
                # Advance to next player
                next_idx = (current_idx + 1) % len(game_state.players)
                game_state.current_player_idx = next_idx
                continue

            # Get player's role
            player_role = agent.get_player_role(game_state, player_id)

            # Handle narrator turn differently
            if player_role == "narrator" or player_id.lower() == "narrator":
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

                # If narrator's turn and all night actions are complete, transition to day
                if all_night_actions_complete and player_id.lower() == "narrator":
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
                    and player_id.lower() == "narrator"
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
                import traceback

                traceback.print_exc()

    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        if debug:
            import traceback

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
    run_mafia_game_simple(
        player_count=args.players, max_days=args.days, debug=args.debug
    )


if __name__ == "__main__":
    main()
