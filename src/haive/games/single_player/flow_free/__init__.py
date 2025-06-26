"""Flow Free game module.

This package provides components for simulating and interacting with Flow Free,
a puzzle game where you need to connect matching colored dots with pipes without
intersections or gaps.
"""

from haive.games.single_player.flow_free.agent import FlowFreeAgent
from haive.games.single_player.flow_free.config import FlowFreeConfig
from haive.games.single_player.flow_free.engines import flow_free_engines
from haive.games.single_player.flow_free.models import FlowFreeAnalysis, FlowFreeMove
from haive.games.single_player.flow_free.state import FlowFreeState
from haive.games.single_player.flow_free.state_manager import FlowFreeStateManager

__all__ = [
    "FlowFreeAgent",
    "FlowFreeAnalysis",
    "FlowFreeConfig",
    "FlowFreeMove",
    "FlowFreeState",
    "FlowFreeStateManager",
    "flow_free_engines",
]
