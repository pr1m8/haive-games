"""Example implementation and runner for the Mafia game.

This module provides a complete example of how to set up and run a Mafia game,
including:
    - Game configuration and initialization
    - Player setup with role assignment
    - Game execution with visualization
    - Debug logging and error handling
    - Command-line interface for game parameters

Example:
    To run a game from the command line:
    ```bash
    python example.py --players 7 --days 3 --debug
    ```

    To run programmatically:
    ```python
    from mafia.example import run_mafia_game
    run_mafia_game(player_count=7, max_days=3, debug=True)
    ```
"""

import logging
import time
import traceback
import uuid

from haive.games.mafia.agent import MafiaAgent
from haive.games.mafia.config import MafiaAgentConfig, aug_llm_configs
from haive.games.mafia.models import GamePhase
from haive.games.mafia.state import MafiaGameState
from haive.games.mafia.state_manager import MafiaStateManager

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_mafia_game(
    player_count: int = 5, max_days: int = 3, debug: bool = True
) -> None:
    """Run a complete Mafia game simulation with visualization.

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
        Exception: If game setup or execution fails.
    """
    print("\n🎭 Setting up Mafia Game")
    print("=" * 60)
    print(f"Number of players: {player_count}")
    print(f"Maximum days: {max_days}")
    print(f"Debug mode: {'Enabled' if debug else 'Disabled'}")
    print("=" * 60)

    agent: MafiaAgent | None = None

    try:
        # Print available configs for debugging
        if debug:
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
        initial_state = MafiaStateManager.initialize(player_names)

        if debug:
            print("\n🎲 Game Role Assignment:")
            for player_id, role in initial_state.roles.items():
                print(f"  {player_id}: {role.value}")

        # Run the game
        print("\n🎭 Starting Mafia Game")
        print("=" * 60)
        print(f"Players: {', '.join(player_names[:-1])} + Narrator")
        print("=" * 60)

        # Track day count to prevent infinite games
        current_day = 0

        # Create a simple thread ID for the session
        thread_id = str(uuid.uuid4())

        # Convert initial state to dict for streaming
        initial_state_dict = initial_state.model_dump()

        # Stream the game execution
        try:
            # Use invoke instead of stream to bypass the streaming error
            try:
                print("\n🎲 Running game using direct invoke instead of stream")
                final_state = agent.app.invoke(
                    initial_state_dict,
                    config={"configurable": {"thread_id": thread_id}},
                )

                # Visualize the final state
                if isinstance(final_state, dict):
                    agent.visualize_state(final_state)

                # Skip the streaming section
                print(
                    "\n⚠️ Game run in non-streaming mode due to LangGraph compatibility issue"
                )
                return
            except Exception as invoke_error:
                print(
                    f"\n❌ Direct invoke failed, falling back to stream: {invoke_error}"
                )

            # The stream method can return None values which need to be handled
            steps = agent.app.stream(
                initial_state_dict,
                config={"configurable": {"thread_id": thread_id}},
                debug=debug,
                stream_mode="values",
            )

            # Safely handle potentially None iterator
            if steps is None:
                print("\n❌ Stream returned None instead of an iterator")
                steps = []

            for step in steps:
                try:
                    # Skip empty steps
                    if not step:
                        continue

                    # Ensure step is a dictionary
                    if not isinstance(step, dict):
                        logger.warning(f"Unexpected step type: {type(step)}")
                        continue

                    # Convert dict to MafiaGameState for visualization
                    try:
                        if isinstance(step, dict) and "players" in step:
                            # Create a MafiaGameState from the dict for visualization
                            state_for_viz = MafiaGameState.model_validate(step)
                            agent.visualize_state(state_for_viz)
                        else:
                            # If we can't create a proper state, print raw step
                            print(f"\n📋 Raw step data: {step}")
                    except Exception as viz_error:
                        logger.debug(f"Visualization error: {viz_error}")
                        # Continue even if visualization fails

                    # Check for game over using dict access
                    game_status = step.get("game_status", "ongoing")
                    game_phase = step.get("game_phase")

                    if (
                        game_status != "ongoing"
                        or game_phase == GamePhase.GAME_OVER.value
                    ):
                        print(f"\n🏆 Game Status: {game_status.upper()}")
                        winner = step.get("winner")
                        if winner:
                            print(f"🎖️ Winner: {winner.upper()}")
                        break

                    # Check for errors
                    error_message = step.get("error_message")
                    if error_message:
                        print(f"\n❌ Error: {error_message}")
                        break

                    # Check day limit to prevent endless games
                    day_number = step.get("day_number", 0)
                    if day_number > current_day:
                        current_day = day_number
                        if current_day > max_days:
                            print(
                                f"\n⏰ Maximum days ({max_days}) reached. Ending game."
                            )
                            break

                    # Add a slight delay for better readability
                    time.sleep(0.3)

                except KeyboardInterrupt:
                    print("\n⚠️ Game interrupted by user")
                    break
                except Exception as step_error:
                    logger.error(f"Error processing step: {step_error}")
                    if debug:
                        traceback.print_exc()
                    # Continue to next step even if this one fails
                    continue

        except Exception as stream_error:
            print(f"\n❌ STREAMING ERROR: {stream_error}")
            if debug:
                traceback.print_exc()

    except Exception as setup_error:
        print(f"\n❌ SETUP ERROR: {setup_error}")
        if debug:
            traceback.print_exc()

    finally:
        # Try to save game history if agent exists
        if agent is not None:
            try:
                print("\n📊 Saving game history")
                agent.save_state_history()
                print("✅ Game history saved successfully")
            except Exception as save_error:
                print(f"⚠️ Could not save game history: {save_error}")
                if debug:
                    traceback.print_exc()

    print("\n✅ Game Complete!")


def main():
    """Main entry point for command-line execution."""
    import argparse

    parser = argparse.ArgumentParser(description="Run a Mafia game simulation")
    parser.add_argument(
        "--players",
        type=int,
        default=7,
        help="Number of players (including narrator, minimum 4)",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=3,
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
    run_mafia_game(player_count=args.players, max_days=args.days, debug=args.debug)


if __name__ == "__main__":
    main()
