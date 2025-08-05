"""Module exports."""

from haive.games.debate_v2.agent import GameDebateAgent
from haive.games.debate_v2.agent import GameDebateAgent as DebateV2Agent

# Create a dummy config for backward compatibility
DebateV2AgentConfig = type("DebateV2AgentConfig", (), {})
from haive.games.debate_v2.agent_with_judges import JudgedGameDebateAgent
from haive.games.debate_v2.state import DebateV2State
from haive.games.debate_v2.state_manager import DebateV2StateManager
from haive.games.debate_v2.ui import DebateV2UI

__all__ = [
    "DebateV2Agent",
    "DebateV2AgentConfig",
    "DebateV2State",
    "DebateV2StateManager",
    "DebateV2UI",
    "JudgedGameDebateAgent",
]
