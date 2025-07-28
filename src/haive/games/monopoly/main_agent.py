"""Fixed Main Monopoly agent that orchestrates the complete game.

This module provides the corrected main agent implementation that:
    - Ensures BaseModel consistency throughout (no dict conversions)
    - Properly handles state schema compatibility
    - Fixes the validation error by maintaining BaseModel state
"""

# Standard library imports
import logging
from typing import Any

# Local imports
from haive.core.engine.agent.agent import Agent, register_agent

from haive.games.monopoly.config import MonopolyGameAgentConfig
from haive.games.monopoly.state import MonopolyState

logger = logging.getLogger(__name__)


@register_agent(MonopolyGameAgentConfig)
class MonopolyAgent(Agent[MonopolyGameAgentConfig]):
    """Main Monopoly agent that orchestrates the complete game.

    This agent combines:
        - Game rule enforcement and turn management
        - Player decision delegation to subgraphs
        - Complete game state management
        - Game end detection and winner determination
    """

    def __init__(self, config: MonopolyGameAgentConfig):
        """Initialize the monopoly agent."""
        # Set up player agent engines first
        config.setup_player_agent_engines()

        # Create the player decision agent
        self.player_agent = config.create_player_agent()

        # Create initial state
        self.initial_state = config.create_initial_state()

        # CRITICAL: Validate initial state
        logger.debug(
            f"Initial state created with {len(self.initial_state.players)} players"
        )
        if self.initial_state.players:
            logger.debug(
                f"Player names: {[p.name for p in self.initial_state.players]}"
            )
        else:
            raise ValueError("CRITICAL: No players in initial state!")

        super().__init__(config)

    def setup_workflow(self) -> None:
        """Set up the complete monopoly workflow.

        This creates the main game workflow nodes and connects them
        properly.
        """
        # Import the game agent here to avoid circular dependency
        from haive.games.monopoly.game_agent import (
            MonopolyGameAgent,
            MonopolyGameAgentConfig,
        )

        # Create game agent config with the player agent reference
        game_config = MonopolyGameAgentConfig(
            name="monopoly_game_orchestrator",
            player_names=self.config.player_names,
            max_turns=self.config.max_turns,
            enable_trading=self.config.enable_trading,
            player_agent=self.player_agent,  # Pass the created player agent
        )

        # Create the game orchestration agent
        self.game_agent = MonopolyGameAgent(game_config)

        # Use the game agent's workflow as our main workflow
        self.graph = self.game_agent.graph

    def start_game(self) -> MonopolyState:
        """Start a new monopoly game.

        CRITICAL: Keep everything as BaseModel - no dict conversions!

        Returns:
            Final game state as MonopolyState BaseModel
        """
        # CRITICAL FIX: Pass the BaseModel directly, no conversion to dict

        try:
            # Use the BaseModel directly with the graph
            final_state = self.app.invoke(
                self.initial_state,  # Pass BaseModel directly
                config=self.runnable_config,
            )

            # Ensure final_state is MonopolyState
            if not isinstance(final_state, MonopolyState):
                final_state = MonopolyState.from_state_object(final_state)

            self._display_final_results(final_state)

            return final_state

        except Exception:

            raise

    def _display_final_results(self, final_state: MonopolyState) -> None:
        """Display final game results."""
        # Display player final standings
        players_by_worth = []

        for player in final_state.players:
            if not player.bankrupt:
                net_worth = player.net_worth(final_state.properties)
                players_by_worth.append(
                    (player.name, net_worth, player.money, len(player.properties))
                )

        # Sort by net worth
        players_by_worth.sort(key=lambda x: x[1], reverse=True)

        for i, (name, net_worth, _money, _prop_count) in enumerate(players_by_worth):
            "👑" if name == final_state.winner else f"{i+1}."

        # Display bankrupted players
        bankrupt_players = [p for p in final_state.players if p.bankrupt]
        if bankrupt_players:
            for player in bankrupt_players:
                pass

        # Display some game statistics

        # Count different event types
        event_counts = {}
        for event in final_state.game_events:
            event_type = event.event_type
            event_counts[event_type] = event_counts.get(event_type, 0) + 1

        for event_type, _count in sorted(event_counts.items()):
            pass

    def save_game_history(self, filename: str | None = None) -> None:
        """Save game history to a file."""
        if filename is None:
            from datetime import datetime

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"monopoly_game_{timestamp}.json"

        # This would save the game state history
        # Implementation would depend on desired format

    def get_game_summary(self) -> dict[str, Any]:
        """Get a summary of the game configuration and status."""
        return {
            "players": self.config.player_names,
            "max_turns": self.config.max_turns,
            "settings": {
                "trading_enabled": self.config.enable_trading,
                "building_enabled": self.config.enable_building,
                "auctions_enabled": self.config.enable_auctions,
            },
            "initial_state_type": type(self.initial_state).__name__,
            "initial_players_count": len(self.initial_state.players),
        }
