"""BS (Bullshit) card game module."""

from haive.games.cards.standard.bs.agent import BullshitAgent
from haive.games.cards.standard.bs.config import BullshitAgentConfig
from haive.games.cards.standard.bs.models import (
    Card,
    ChallengeAction,
    PlayerClaimAction,
    PlayerState,
)
from haive.games.cards.standard.bs.state import BullshitGameState
from haive.games.cards.standard.bs.state_manager import BullshitStateManager

__all__ = [
    "BullshitAgent",
    "BullshitAgentConfig",
    "BullshitGameState",
    "BullshitStateManager",
    "Card",
    "ChallengeAction",
    "PlayerClaimAction",
    "PlayerState",
]

# Alias for compatibility
BSStateManager = BullshitStateManager
