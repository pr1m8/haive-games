"""Texas Hold'em Agent module - Main agent interface.

This module provides the main agent interface for Texas Hold'em poker games,
wrapping the game agent and providing a simplified interface.
"""

from haive.games.hold_em.game_agent import HoldemGameAgent, HoldemGameAgentConfig
from haive.games.hold_em.player_agent import HoldemPlayerAgent, HoldemPlayerAgentConfig
from haive.games.hold_em.state import HoldemState

# Export the main classes for easy importing
__all__ = [
    "HoldemGameAgent",
    "HoldemGameAgentConfig",
    "HoldemPlayerAgent",
    "HoldemPlayerAgentConfig",
    "HoldemState",
]

# For compatibility, provide aliases
HoldEmAgent = HoldemGameAgent
HoldEmAgentConfig = HoldemGameAgentConfig
HoldEmPlayerAgent = HoldemPlayerAgent
HoldEmPlayerAgentConfig = HoldemPlayerAgentConfig
HoldEmState = HoldemState
