"""Single-player game agent base class.

This module provides the SinglePlayerGameAgent base class for implementing single-player
game agents in the Haive framework.

"""

from typing import TypeVar

from haive.games.base.agent import GameAgent
from haive.games.framework.base.config import GameConfig

T = TypeVar("T", bound=GameConfig)


class SinglePlayerGameAgent(GameAgent[T]):
    """Base class for single-player game agents.

    This class extends GameAgent to provide specific functionality for
    single-player games where an LLM can act as the player, assistant,
    or game engine.

    Single-player games differ from multiplayer games in that they:
    - Don't require turn management between multiple players
    - Often involve puzzles, challenges, or solo adventures
    - May use the LLM as a game master or narrator

    Example:
        >>> from haive.games.single_player import SinglePlayerGameAgent
        >>> class WordleAgent(SinglePlayerGameAgent):
        ...     def __init__(self, config):
        ...         super().__init__(config)
        ...         self.state_manager = WordleStateManager

    Attributes:
        config: Configuration for the single-player game
        state_manager: Manager for game state transitions

    """

    def __init__(self, config: T):
        """Initialize the single-player game agent.

        Args:
            config: Game-specific configuration

        """
        super().__init__(config)

    def setup_single_player_workflow(self) -> None:
        """Set up the workflow specific to single-player games.

        This method can be overridden by subclasses to customize the workflow for
        specific single-player game mechanics.

        """
        # Default implementation uses the base game workflow
        self.setup_workflow()

    def handle_player_action(self, action: str) -> dict:
        """Handle a player action in the game.

        Args:
            action: The player's action as a string

        Returns:
            dict: Result of the action including any state changes

        """
        raise NotImplementedError("Subclasses must implement handle_player_action")

    def generate_game_response(self, state: dict) -> str:
        """Generate the game's response to the current state.

        Args:
            state: Current game state

        Returns:
            str: Game's response or narration

        """
        raise NotImplementedError("Subclasses must implement generate_game_response")


__all__ = ["SinglePlayerGameAgent"]
