# src/haive/games/debate/config.py
from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field

from haive.games.debate.engines import build_debate_engines
from haive.games.debate.state import DebateState


class DebateAgentConfig(AgentConfig):
    """Configuration for debate agents."""

    debate_format: str = Field(default="standard", description="Format of the debate")
    time_limit: int | None = Field(
        default=None, description="Time limit in seconds per phase"
    )
    max_statements: int | None = Field(
        default=None, description="Max statements per participant"
    )
    allow_interruptions: bool = Field(
        default=False, description="Allow participants to interrupt"
    )
    voting_enabled: bool = Field(default=True, description="Enable voting at the end")

    # Role configurations
    moderator_role: str | None = Field(
        default=None, description="Specific role for moderator"
    )
    participant_roles: dict[str, str] = Field(
        default_factory=dict, description="Role assignments"
    )

    # State schema
    state_schema: type[BaseModel] = Field(
        default=DebateState, description="State schema for the debate"
    )

    # Engine configurations
    engines: dict[str, AugLLMConfig] = Field(
        default_factory=build_debate_engines, description="LLM engines for debate roles"
    )

    @classmethod
    def default(cls):
        """Create a default configuration for standard debate."""
        return cls(
            name="standard_debate",
            debate_format="standard",
            time_limit=120,
            max_statements=3,
            allow_interruptions=False,
            voting_enabled=True,
        )

    @classmethod
    def presidential(cls):
        """Create a configuration for presidential debate."""
        return cls(
            name="presidential_debate",
            debate_format="presidential",
            time_limit=120,
            max_statements=None,
            allow_interruptions=True,
            voting_enabled=False,
            moderator_role="moderator",
        )

    @classmethod
    def trial(cls):
        """Create a configuration for a trial format."""
        return cls(
            name="trial_debate",
            debate_format="trial",
            time_limit=300,
            max_statements=None,
            allow_interruptions=False,
            voting_enabled=True,
            participant_roles={
                "judge": "JUDGE",
                "prosecution": "PROSECUTOR",
                "defense": "DEFENSE",
                "jury": "JURY",
            },
        )

    @classmethod
    def panel_discussion(cls):
        """Create a configuration for a panel discussion."""
        return cls(
            name="panel_discussion",
            debate_format="panel",
            time_limit=180,
            max_statements=None,
            allow_interruptions=True,
            voting_enabled=False,
            moderator_role="moderator",
        )
