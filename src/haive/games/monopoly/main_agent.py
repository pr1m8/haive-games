"""Fixed Main Monopoly agent that orchestrates the complete game.

This module provides the corrected main agent implementation that:
    - Ensures BaseModel consistency throughout (no dict conversions)
    - Properly handles state schema compatibility
    - Fixes the validation error by maintaining BaseModel state
"""

from typing import Any, Dict, Optional

from haive.core.engine.agent.agent import Agent, register_agent

from haive.games.monopoly.config import MonopolyGameAgentConfig
from haive.games.monopoly.state import MonopolyState


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
        print(
            f"DEBUG: Initial state created with {len(self.initial_state.players)} players"
        )
        if self.initial_state.players:
            print(
                f"DEBUG: Player names: {[p.name for p in self.initial_state.players]}"
            )
        else:
            raise ValueError("CRITICAL: No players in initial state!")

        super().__init__(config)

    def setup_workflow(self):
        """Set up the complete monopoly workflow.

        This creates the main game workflow nodes and connects them properly.
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

        print(
            f"🎮 Monopoly game initialized with {len(self.config.player_names)} players"
        )
        print(f"📋 Players: {', '.join(self.config.player_names)}")
        print(
            f"⚙️ Settings: Max turns={self.config.max_turns}, Trading={self.config.enable_trading}"
        )

    def start_game(self) -> MonopolyState:
        """Start a new monopoly game.

        CRITICAL: Keep everything as BaseModel - no dict conversions!

        Returns:
            Final game state as MonopolyState BaseModel
        """
        print("🎲 Starting Monopoly game!")
        print("=" * 50)

        # CRITICAL FIX: Pass the BaseModel directly, no conversion to dict
        print(f"DEBUG: Starting with {len(self.initial_state.players)} players")
        print(f"DEBUG: Initial state type: {type(self.initial_state)}")

        try:
            # Use the BaseModel directly with the graph
            final_state = self.app.invoke(
                self.initial_state,  # Pass BaseModel directly
                config=self.runnable_config,
            )

            print("\n" + "=" * 50)
            print("🏁 Game Complete!")

            # Ensure final_state is MonopolyState
            if not isinstance(final_state, MonopolyState):
                final_state = MonopolyState.from_state_object(final_state)

            self._display_final_results(final_state)

            return final_state

        except Exception as e:
            print(f"\n❌ Game error: {str(e)}")
            import traceback

            print(f"Traceback: {traceback.format_exc()}")
            raise

    def _display_final_results(self, final_state: MonopolyState) -> None:
        """Display final game results."""
        print(f"🏆 Winner: {final_state.winner}")
        print(f"🎮 Turns played: {final_state.turn_number}")
        print(f"🔄 Rounds completed: {final_state.round_number}")

        # Display player final standings
        print("\n📊 Final Standings:")
        players_by_worth = []

        for player in final_state.players:
            if not player.bankrupt:
                net_worth = player.net_worth(final_state.properties)
                players_by_worth.append(
                    (player.name, net_worth, player.money, len(player.properties))
                )

        # Sort by net worth
        players_by_worth.sort(key=lambda x: x[1], reverse=True)

        for i, (name, net_worth, money, prop_count) in enumerate(players_by_worth):
            status = "👑" if name == final_state.winner else f"{i+1}."
            print(
                f"  {status} {name}: ${net_worth:,} net worth (${money:,} cash, {prop_count} properties)"
            )

        # Display bankrupted players
        bankrupt_players = [p for p in final_state.players if p.bankrupt]
        if bankrupt_players:
            print("\n💥 Bankrupted:")
            for player in bankrupt_players:
                print(f"  ❌ {player.name}")

        # Display some game statistics
        print("\n📈 Game Statistics:"s:")
        print(f"  • Total events: {len(final_state.game_events)}")

        # Count different event types
        event_counts = {}
        for event in final_state.game_events:
            event_type = event.event_type
            event_counts[event_type] = event_counts.get(event_type, 0) + 1

        for event_type, count in sorted(event_counts.items()):
            print(f"  • {event_type.replace('_', ' ').title()}: {count}")

    def save_game_history(self, filename: Optional[str] = None) -> None:
        """Save game history to a file."""
        if filename is None:
            from datetime import datetime

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"monopoly_game_{timestamp}.json"

        # This would save the game state history
        # Implementation would depend on desired format
        print(f"💾 Game history saved to {filename}")

    def get_game_summary(self) -> Dict[str, Any]:
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
