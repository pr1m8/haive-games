"""Configuration classes for debate agent setup and customization.

This module provides comprehensive configuration options for debate agents,
including format-specific presets, role assignments, timing controls, and
engine configurations. The configuration system supports various debate
formats from formal parliamentary debates to trial simulations.

The configuration classes use Pydantic for validation and provide factory
methods for common debate formats including standard debates, presidential
debates, trial formats, and panel discussions.

Examples:
    Creating a standard debate configuration::

        config = DebateAgentConfig.default()
        agent = DebateAgent(config)

    Creating a custom trial simulation::

        config = DebateAgentConfig.trial()
        config.time_limit = 600  # 10 minutes per phase
        config.participant_roles["witness_1"] = "witness"
        agent = DebateAgent(config)

    Creating a presidential debate format::

        config = DebateAgentConfig.presidential()
        config.allow_interruptions = True
        config.moderator_role = "moderator"
        agent = DebateAgent(config)

    Creating a custom configuration::

        config = DebateAgentConfig(
            name="custom_debate",
            debate_format="oxford",
            time_limit=300,
            max_statements=5,
            allow_interruptions=False,
            voting_enabled=True,
            participant_roles={
                "pro_1": "pro", "pro_2": "pro",
                "con_1": "con", "con_2": "con",
                "moderator": "moderator"
            }
        )

Note:
    All configuration classes inherit from AgentConfig and include automatic
    engine setup through the build_debate_engines factory function.
    Custom engine configurations can be provided to override defaults.
"""

from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field, field_validator

from haive.games.debate.engines import build_debate_engines
from haive.games.debate.state import DebateState


class DebateAgentConfig(AgentConfig):
    """Comprehensive configuration for debate agents with format-specific
    settings.

    This configuration class provides extensive customization options for debate
    agents, supporting various debate formats, role assignments, timing controls,
    and engine configurations. It includes validation for debate-specific parameters
    and provides factory methods for common debate formats.

    The configuration system supports:
    - Multiple debate formats (standard, parliamentary, oxford, trial, presidential)
    - Flexible role assignment system for participants
    - Timing controls and statement limits
    - Interruption and voting settings
    - Custom engine configurations for different participant roles

    Attributes:
        debate_format (str): Format type determining debate structure and rules.
            Supported formats: "standard", "parliamentary", "oxford", "trial",
            "presidential", "panel", "lincoln_douglas".
        time_limit (Optional[int]): Maximum time in seconds per debate phase.
            None means no time limit. Typical values: 60-600 seconds.
        max_statements (Optional[int]): Maximum statements per participant per phase.
            None means unlimited statements. Typical values: 1-5 statements.
        allow_interruptions (bool): Whether participants can interrupt each other
            during their statements. Common in presidential and panel formats.
        voting_enabled (bool): Whether to include a voting phase at debate end.
            Typically enabled for competitive debates, disabled for discussions.
        moderator_role (Optional[str]): Specific role identifier for the moderator.
            None means no dedicated moderator. Common value: "moderator".
        participant_roles (Dict[str, str]): Mapping of participant IDs to their roles.
            Keys are participant identifiers, values are role names like "pro",
            "con", "judge", "moderator", "prosecutor", "defense", "witness".
        state_schema (Type[BaseModel]): Pydantic model class for debate state.
            Defaults to DebateState but can be customized for specific formats.
        engines (Dict[str, AugLLMConfig]): Engine configurations for different roles.
            Automatically built by build_debate_engines but can be customized.

    Examples:
        Basic debate configuration::

            config = DebateAgentConfig(
                name="climate_debate",
                debate_format="oxford",
                time_limit=300,
                max_statements=3,
                participant_roles={
                    "scientist": "pro",
                    "economist": "con",
                    "moderator": "moderator"
                }
            )

        Trial simulation configuration::

            config = DebateAgentConfig(
                name="murder_trial",
                debate_format="trial",
                time_limit=600,
                allow_interruptions=False,
                participant_roles={
                    "prosecutor": "prosecutor",
                    "defense_attorney": "defense",
                    "judge": "judge",
                    "witness_1": "witness",
                    "witness_2": "witness"
                }
            )

        Parliamentary debate configuration::

            config = DebateAgentConfig(
                name="parliament_session",
                debate_format="parliamentary",
                time_limit=180,
                allow_interruptions=True,
                voting_enabled=True,
                participant_roles={
                    "pm": "government",
                    "deputy_pm": "government",
                    "leader_opposition": "opposition",
                    "deputy_opposition": "opposition",
                    "speaker": "moderator"
                }
            )

    Note:
        The configuration automatically sets up appropriate engines for each role
        using the build_debate_engines factory. Custom engines can be provided
        to override defaults for specific use cases or to add specialized capabilities.
    """

    debate_format: str = Field(
        default="standard",
        description="Format type determining debate structure and rules",
        examples=[
            "standard",
            "parliamentary",
            "oxford",
            "trial",
            "presidential",
            "panel",
            "lincoln_douglas",
        ],
    )

    time_limit: int | None = Field(
        default=None,
        ge=30,
        le=3600,
        description="Maximum time in seconds per debate phase (30-3600 seconds, None for no limit)",
        examples=[60, 120, 300, 600, None],
    )

    max_statements: int | None = Field(
        default=None,
        ge=1,
        le=20,
        description="Maximum statements per participant per phase (1-20, None for unlimited)",
        examples=[1, 3, 5, 10, None],
    )

    allow_interruptions: bool = Field(
        default=False,
        description="Whether participants can interrupt each other during statements",
        examples=[True, False],
    )

    voting_enabled: bool = Field(
        default=True,
        description="Whether to include a voting/judgment phase at debate conclusion",
        examples=[True, False],
    )

    # Role configurations
    moderator_role: str | None = Field(
        default=None,
        description="Specific role identifier for the debate moderator (None for no moderator)",
        examples=["moderator", "judge", "chair", "speaker", None],
    )

    participant_roles: dict[str, str] = Field(
        default_factory=dict,
        description="Mapping of participant IDs to their debate roles",
        examples=[
            {"debater_1": "pro", "debater_2": "con", "moderator": "moderator"},
            {"prosecutor": "prosecutor", "defense": "defense", "judge": "judge"},
            {"panelist_1": "expert", "panelist_2": "expert", "host": "moderator"},
        ],
    )

    # State schema
    state_schema: type[BaseModel] = Field(
        default=DebateState,
        description="Pydantic model class for managing debate state and transitions",
    )

    # Engine configurations
    engines: dict[str, AugLLMConfig] = Field(
        default_factory=build_debate_engines,
        description="LLM engine configurations for different participant roles",
    )

    @field_validator("debate_format")
    @classmethod
    def validate_debate_format(cls, v: str) -> str:
        """Validate debate format is supported.

        Args:
            v (str): Debate format to validate.

        Returns:
            str: Validated format string.

        Raises:
            ValueError: If format is not supported.
        """
        supported_formats = {
            "standard",
            "parliamentary",
            "oxford",
            "trial",
            "presidential",
            "panel",
            "lincoln_douglas",
        }
        format_lower = v.lower().strip()
        if format_lower not in supported_formats:
            raise ValueError(
                f"Debate format must be one of: {', '.join(supported_formats)}"
            )
        return format_lower

    @field_validator("participant_roles")
    @classmethod
    def validate_participant_roles(cls, v: dict[str, str]) -> dict[str, str]:
        """Validate participant role assignments.

        Args:
            v (Dict[str, str]): Role assignments to validate.

        Returns:
            Dict[str, str]: Validated role assignments.

        Raises:
            ValueError: If role assignments are invalid.
        """
        valid_roles = {
            "pro",
            "con",
            "neutral",
            "moderator",
            "judge",
            "jury",
            "prosecutor",
            "defense",
            "witness",
            "expert",
            "panelist",
            "government",
            "opposition",
            "chair",
            "speaker",
            "timekeeper",
        }

        for participant_id, role in v.items():
            if not isinstance(participant_id, str) or not participant_id.strip():
                raise ValueError("Participant IDs must be non-empty strings")

            role_lower = role.lower().strip()
            if role_lower not in valid_roles:
                raise ValueError(
                    f"Role '{role}' not recognized. Valid roles: {
                        ', '.join(valid_roles)
                    }"
                )

        return {pid: role.lower().strip() for pid, role in v.items()}

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
                "judge": "judge",
                "prosecution": "prosecutor",
                "defense": "defense",
                "jury": "jury",
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
