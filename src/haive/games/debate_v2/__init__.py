"""Module exports."""

from haive.games.debate_v2.agent import GameDebateAgent
from haive.games.debate_v2.agent import GameDebateAgent as DebateV2Agent
from haive.games.debate_v2.agent_with_judges import JudgedGameDebateAgent

# Create a dummy config for backward compatibility
DebateV2AgentConfig = type("DebateV2AgentConfig", (), {})

__all__ = [
    "DebateV2Agent",
    "DebateV2AgentConfig",
    "JudgedGameDebateAgent",
]
