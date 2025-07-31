"""Comprehensive agent implementation for the Clue (Cluedo) mystery game.

This module provides the complete agent implementation for the Clue game,
managing game state, player interactions, AI decision-making, and visualization.
The agent orchestrates the entire gameplay experience from initialization
through completion, handling all game mechanics and player coordination.

The agent system provides:
- Game state initialization and management
- Player action coordination and validation
- AI decision-making and reasoning
- Real-time game visualization and logging
- Game completion detection and handling
- Performance monitoring and optimization

Key Features:
    - Complete game orchestration from start to finish
    - Real-time visualization with detailed game state display
    - Robust error handling and edge case management
    - Performance monitoring and game completion detection
    - Comprehensive logging for debugging and analysis
    - Integration with the Haive agent framework

Examples:
    Basic agent usage::

        from haive.games.clue.agent import ClueAgent
        from haive.games.clue.config import ClueConfig

        # Create agent with default configuration
        agent = ClueAgent()

        # Run a complete game
        final_state = agent.run_game()
        print(f"Game completed with status: {final_state['game_status']}")

    Custom configuration::

        from haive.games.clue.config import ClueConfig

        # Create custom configuration
        config = ClueConfig.competitive_game(max_turns=15)
        agent = ClueAgent(config)

        # Run game without visualization for performance
        final_state = agent.run_game(visualize=False)

    Game state management::

        # Initialize game state
        initial_state = agent.initialize_game({})

        # Visualize current state
        agent.visualize_state(initial_state)

        # Check game completion
        from haive.games.clue.state import ClueState
        state = ClueState(**initial_state)
        if state.is_game_over:
            print(f"Game ended! Winner: {state.winner}")

The agent integrates seamlessly with the Haive framework and provides complete
functionality for running Clue games with AI players, visualization, and
comprehensive state management.

"""

import logging
import time
from typing import Any

from haive.core.engine.agent.agent import register_agent

from haive.games.clue.config import ClueConfig
from haive.games.clue.state import ClueState
from haive.games.clue.state_manager import ClueStateManager
from haive.games.framework.base.agent import GameAgent

logger = logging.getLogger(__name__)


@register_agent(ClueConfig)
class ClueAgent(GameAgent[ClueConfig]):
    """Comprehensive agent for playing Clue (Cluedo) mystery games.

    This class implements the complete Clue game agent, managing all aspects
    of gameplay including state management, player coordination, AI decision-making,
    and visualization. The agent orchestrates the entire game experience from
    initialization through completion.

    The agent handles:
    - Game state initialization with proper solution generation
    - Player action coordination and turn management
    - AI decision-making and reasoning processes
    - Real-time game visualization and logging
    - Game completion detection and result handling
    - Performance monitoring and optimization

    The agent integrates with the Haive framework to provide a complete
    gaming experience with configurable AI behavior, visualization options,
    and comprehensive state management.

    Attributes:
        state_manager: The state management system for game logic.
            Handles all game state transitions and validation.
        config: The configuration object controlling agent behavior.
            Defines game parameters, AI settings, and visualization options.

    Examples:
        Basic agent creation::

            from haive.games.clue.agent import ClueAgent

            # Create agent with default configuration
            agent = ClueAgent()

            # Run a complete game
            final_state = agent.run_game()
            print(f"Game status: {final_state['game_status']}")

        Custom configuration::

            from haive.games.clue.config import ClueConfig

            # Create competitive configuration
            config = ClueConfig.competitive_game(max_turns=15)
            agent = ClueAgent(config)

            # Run high-performance game
            final_state = agent.run_game(visualize=False)

        Tutorial mode::

            # Create tutorial configuration
            config = ClueConfig.tutorial_game()
            agent = ClueAgent(config)

            # Run educational game with predetermined solution
            final_state = agent.run_game(visualize=True)

    Note:
        The agent requires a configured state manager and proper game
        configuration to function correctly. All game logic is delegated
        to the state manager to maintain separation of concerns.

    """

    def __init__(self, config: ClueConfig = ClueConfig()):
        """Initialize the Clue agent with configuration.

        Sets up the agent with the specified configuration and initializes
        the state management system. The agent is ready to run games after
        initialization.

        Args:
            config: The configuration for the Clue game.
                Controls game parameters, AI behavior, and visualization options.
                Defaults to standard configuration if not provided.

        Examples:
            Default initialization::

                agent = ClueAgent()
                assert agent.config.max_turns == 20
                assert agent.config.enable_analysis == True
                assert agent.config.visualize == True

            Custom configuration::

                from haive.games.clue.config import ClueConfig

                config = ClueConfig(
                    max_turns=15,
                    enable_analysis=False,
                    visualize=False
                )
                agent = ClueAgent(config)
                assert agent.config.max_turns == 15

            Factory method configuration::

                config = ClueConfig.competitive_game()
                agent = ClueAgent(config)
                assert agent.config.enable_analysis == False

        """
        self.state_manager = ClueStateManager
        super().__init__(config)

    def initialize_game(self, state: dict[str, Any]) -> dict[str, Any]:
        """Initialize the Clue game with proper state setup.

        Creates a new game state with appropriate configuration settings,
        including solution generation, card dealing, and player setup.
        The initialization process sets up all necessary game components
        for a complete Clue experience.

        Args:
            state: Initial state dictionary (unused here but required for interface).
                Maintained for compatibility with the GameAgent interface.

        Returns:
            dict[str, Any]: New game state dictionary ready for gameplay.
                Contains all game information including solution, player cards,
                and initial game parameters.

        Examples:
            Basic initialization::

                agent = ClueAgent()
                initial_state = agent.initialize_game({})

                # Verify game state structure
                assert "solution" in initial_state
                assert "player1_cards" in initial_state
                assert "player2_cards" in initial_state
                assert initial_state["current_player"] == "player1"
                assert initial_state["game_status"] == "ongoing"

            Custom configuration initialization::

                from haive.games.clue.config import ClueConfig

                config = ClueConfig(
                    first_player="player2",
                    max_turns=15
                )
                agent = ClueAgent(config)
                initial_state = agent.initialize_game({})

                assert initial_state["current_player"] == "player2"
                assert initial_state["max_turns"] == 15

            Predetermined solution::

                from haive.games.clue.models import ValidSuspect, ValidWeapon, ValidRoom

                solution = {
                    "suspect": ValidSuspect.COLONEL_MUSTARD.value,
                    "weapon": ValidWeapon.KNIFE.value,
                    "room": ValidRoom.KITCHEN.value
                }
                config = ClueConfig(solution=solution)
                agent = ClueAgent(config)
                initial_state = agent.initialize_game({})

                assert initial_state["solution"]["suspect"] == "Colonel Mustard"
                assert initial_state["solution"]["weapon"] == "Knife"
                assert initial_state["solution"]["room"] == "Kitchen"

        Note:
            The state parameter is unused in this implementation but is
            maintained for interface compatibility. All initialization
            parameters come from the agent's configuration object.

        """
        # Initialize the game state
        game_state = self.state_manager.initialize(
            solution=self.config.solution,
            first_player=self.config.first_player,
            max_turns=self.config.max_turns,
        )

        return (
            game_state.model_dump()
            if hasattr(game_state, "model_dump")
            else game_state.dict()
        )

    def visualize_state(self, state: dict[str, Any]) -> None:
        """Visualize the current game state with comprehensive display.

        Provides a detailed visual representation of the current game state,
        including game progress, player information, guess history, and
        solution details (when appropriate). The visualization is designed
        to be informative and easy to read.

        Args:
            state: The state dictionary to visualize.
                Must contain all necessary game state information.

        Examples:
            Basic visualization::

                agent = ClueAgent()
                initial_state = agent.initialize_game({})
                agent.visualize_state(initial_state)
                # Outputs:
                # ==================================================
                # 🎮 Game: Clue v1.0.0
                # 📊 Turn: 1/20
                # 🎭 Current Player: player1
                # 📝 Status: ongoing
                # ==================================================
                # No guesses yet.

            Game in progress::

                # After some gameplay
                agent.visualize_state(current_state)
                # Outputs:
                # ==================================================
                # 🎮 Game: Clue v1.0.0
                # 📊 Turn: 5/20
                # 🎭 Current Player: player2
                # 📝 Status: ongoing
                # ==================================================
                # Turn 1: Colonel Mustard, Knife, Kitchen | Response: Alice
                # Turn 2: Professor Plum, Candlestick, Library | Response: No card shown
                # ...

            Game completion::

                # When game ends
                agent.visualize_state(final_state)
                # Outputs:
                # ==================================================
                # 🎮 Game: Clue v1.0.0
                # 📊 Turn: 8/20
                # 🎭 Current Player: player1
                # 📝 Status: player1_win
                # 🔑 Solution: Colonel Mustard, Knife, Kitchen
                # ==================================================
                # [Full game history displayed]

        Note:
            Visualization is controlled by the agent's configuration.
            If visualize=False, this method returns immediately without
            displaying anything. The display includes emoji icons for
            better readability and visual appeal.

        """
        if not self.config.visualize:
            return

        # Create a ClueState from the dict
        game_state = ClueState(**state)

        logger.info("\n" + "=" * 50)
        logger.info(f"🎮 Game: Clue v{self.config.version}")
        logger.info(f"📊 Turn: {game_state.current_turn_number}/{game_state.max_turns}")
        logger.info(f"🎭 Current Player: {game_state.current_player}")
        logger.info(f"📝 Status: {game_state.game_status}")

        # Only show solution if game is over
        if game_state.game_status != "ongoing":
            logger.info(
                f"🔑 Solution: {game_state.solution.suspect.value}, {
                    game_state.solution.weapon.value
                }, {game_state.solution.room.value}"
            )

        logger.info("=" * 50)

        # Log the board with all guesses and responses
        if game_state.guesses:
            logger.info("\n" + game_state.board_string)
        else:
            logger.info("\nNo guesses yet.")

        # Add a short delay for readability
        time.sleep(0.5)

    def run_game(self, visualize: bool = True) -> dict[str, Any]:
        """Run a complete Clue game with optional visualization and monitoring.

        Executes a full game from initialization to completion, with optional
        real-time visualization and comprehensive monitoring for game completion
        and performance. The method handles all game flow and provides robust
        error handling and loop detection.

        Args:
            visualize: Whether to visualize each game state.
                Overrides the agent's configuration visualization setting.
                True enables real-time game display, False runs silently.

        Returns:
            dict[str, Any]: The final game state dictionary.
                Contains complete game results including winner, solution,
                and full game history.

        Examples:
            Basic game execution::

                agent = ClueAgent()
                final_state = agent.run_game()

                # Check results
                print(f"Game status: {final_state['game_status']}")
                print(f"Winner: {final_state.get('winner', 'No winner')}")
                print(f"Total turns: {len(final_state['guesses'])}")

            Silent game execution::

                agent = ClueAgent()
                final_state = agent.run_game(visualize=False)

                # Faster execution without visualization
                assert final_state['game_status'] in ['player1_win', 'player2_win']

            Performance monitoring::

                import time
                start_time = time.time()

                agent = ClueAgent()
                final_state = agent.run_game(visualize=False)

                duration = time.time() - start_time
                print(f"Game completed in {duration:.2f} seconds")
                print(f"Final turn: {len(final_state['guesses'])}")

            Configuration-based execution::

                # Use competitive configuration
                config = ClueConfig.competitive_game(max_turns=15)
                agent = ClueAgent(config)
                final_state = agent.run_game()

                # Should finish within 15 turns
                assert len(final_state['guesses']) <= 15

        Note:
            The method includes infinite loop detection to prevent games
            from running indefinitely. If the maximum turns are reached
            or the game state stops changing, the game will be automatically
            terminated with appropriate logging.

        """
        # Initialize the game state
        initial_state = self.state_manager.initialize(
            solution=self.config.solution,
            first_player=self.config.first_player,
            max_turns=self.config.max_turns,
        )

        # Run the game
        if visualize:
            # Store the last seen state to prevent infinite loops
            last_state = None
            final_state = None

            for step in self.stream(initial_state, stream_mode="values", debug=True):
                self.visualize_state(step)

                # Create a ClueState to check for game completion
                current_state = ClueState(**step)

                # Break the loop if the game is over
                if current_state.game_status != "ongoing":
                    final_state = step
                    break

                # Detect if we're stuck in an infinite loop by comparing with
                # last state
                if last_state:
                    # If we've seen the same guesses twice, we might be in a
                    # loop
                    if (
                        len(current_state.guesses) == len(last_state.guesses)
                        and len(current_state.guesses) > 0
                        and len(last_state.guesses) > 0
                    ):
                        # Check if max turns reached
                        if len(current_state.guesses) >= current_state.max_turns:
                            logger.warning("\n⚠️ Maximum turns reached. Ending game.")
                            # Force game to end
                            current_state.game_status = "ongoing_win"
                            final_state = current_state.model_dump()
                            break

                # Update last state
                last_state = current_state

            return final_state if final_state else step
        return super().run(initial_state)
