# among_us_config.py

from typing import Any, Literal

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from pydantic import Field, computed_field, root_validator

from haive.games.among_us.prompts import (
    CREWMATE_PROMPT,
    IMPOSTOR_PROMPT,
    MEETING_PROMPT,
    VOTING_PROMPT,
)
from haive.games.among_us.state import AmongUsState
from haive.games.framework.base.config import GameConfig


class AmongUsAgentConfig(GameConfig):
    """Configuration for Among Us game agent."""

    # Base game agent fields inherited from GameAgentConfig
    name: str = Field(default="among_us_agent")
    state_schema: type = Field(default=AmongUsState)
    visualize: bool = Field(default=True)

    # Among Us specific configuration
    player_names: list[str] = Field(...)
    engines: dict[str, dict[str, AugLLMConfig]] | None = Field(default=None)
    llm_config: dict[str, Any] | None = Field(default=None)

    # Game settings
    map_name: str = Field(default="skeld")
    map_locations: list[str] | None = Field(default=None)
    num_impostors: int = Field(default=None)
    emergency_meetings_per_player: int = Field(default=1)
    discussion_time: int = Field(default=45)  # seconds
    voting_time: int = Field(default=30)  # seconds
    player_movement_speed: float = Field(default=1.0)
    kill_cooldown: int = Field(default=45)  # seconds
    task_bar_updates: Literal["always", "meetings", "never"] = Field(default="always")

    @root_validator(pre=True)
    def set_defaults(cls, values):
        """Set default values based on provided values."""
        # Set default number of impostors based on player count
        if values.get("num_impostors") is None and "player_names" in values:
            values["num_impostors"] = max(1, len(values["player_names"]) // 5)

        # Set default map locations based on map name
        if values.get("map_locations") is None:
            map_name = values.get("map_name", "skeld")
            if map_name.lower() == "skeld":
                values["map_locations"] = [
                    "cafeteria",
                    "admin",
                    "electrical",
                    "storage",
                    "medbay",
                    "navigation",
                    "shields",
                    "weapons",
                    "o2",
                    "security",
                ]
            elif map_name.lower() == "polus":
                values["map_locations"] = [
                    "dropship",
                    "office",
                    "laboratory",
                    "storage",
                    "communications",
                    "weapons",
                    "o2",
                    "electrical",
                    "security",
                    "specimen",
                ]
            elif map_name.lower() == "mira":
                values["map_locations"] = [
                    "launchpad",
                    "medbay",
                    "communications",
                    "locker",
                    "laboratory",
                    "office",
                    "admin",
                    "cafeteria",
                    "storage",
                    "reactor",
                ]

        # Set default engines if not provided
        if values.get("engines") is None:
            values["engines"] = cls._create_default_engines(values)

        return values

    @classmethod
    def _create_default_engines(cls, values):
        """Create default engines configuration."""
        # Default LLM config
        default_llm_config = {
            "model": "gpt-4o",
            "parameters": {"temperature": 0.8, "top_p": 0.9},
        }

        # Merge with provided LLM config if any
        llm_config = {**default_llm_config, **(values.get("llm_config") or {})}

        # Create Azure LLM config
        azure_llm_config = AzureLLMConfig(**llm_config)

        # Create prompt templates
        crewmate_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=CREWMATE_PROMPT),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        impostor_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=IMPOSTOR_PROMPT),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        meeting_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=MEETING_PROMPT),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        voting_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=VOTING_PROMPT),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        # Create AugLLM configs
        crewmate_config = AugLLMConfig(
            name="crewmate_player",
            llm_config=azure_llm_config,
            prompt_template=crewmate_template,
        )

        impostor_config = AugLLMConfig(
            name="impostor_player",
            llm_config=azure_llm_config,
            prompt_template=impostor_template,
        )

        meeting_config = AugLLMConfig(
            name="meeting_discussion",
            llm_config=azure_llm_config,
            prompt_template=meeting_template,
        )

        voting_config = AugLLMConfig(
            name="voting_decision",
            llm_config=azure_llm_config,
            prompt_template=voting_template,
        )

        # Return engines configuration
        return {
            "CREWMATE": {
                "player": crewmate_config,
                "meeting": meeting_config,
                "voting": voting_config,
            },
            "IMPOSTOR": {
                "player": impostor_config,
                "meeting": meeting_config,
                "voting": voting_config,
            },
        }

    @computed_field
    @property
    def game_balance(self) -> dict[str, Any]:
        """Calculate game balance metrics and recommendations.

        Returns:
            Dict[str, Any]: Balance analysis including ratios and recommendations.
        """
        player_count = len(self.player_names)
        impostor_ratio = self.num_impostors / player_count

        return {
            "player_count": player_count,
            "impostor_count": self.num_impostors,
            "impostor_ratio": impostor_ratio,
            "balance_rating": (
                "balanced"
                if 0.15 <= impostor_ratio <= 0.3
                else "impostor_favored" if impostor_ratio > 0.3 else "crewmate_favored"
            ),
            "recommended_discussion_time": min(60, max(30, player_count * 6)),
            "recommended_voting_time": min(45, max(15, player_count * 3)),
            "estimated_game_duration": f"{10 + player_count * 2}-{20 + player_count * 4} minutes",
        }

    @classmethod
    def casual_game(cls, player_count: int = 6) -> "AmongUsAgentConfig":
        """Create configuration for casual gameplay.

        Features:
        - Balanced timing for relaxed discussion
        - Standard movement speed
        - Moderate kill cooldown
        - Visualization enabled

        Args:
            player_count: Number of players (default: 6).

        Returns:
            AmongUsAgentConfig: Casual game configuration.
        """
        return cls(
            name="casual_game",
            player_names=[f"Player_{i}" for i in range(1, player_count + 1)],
            map_name="skeld",
            discussion_time=60,
            voting_time=30,
            kill_cooldown=45,
            visualize=True,
        )

    @classmethod
    def tournament_game(cls, player_count: int = 10) -> "AmongUsAgentConfig":
        """Create configuration for tournament play.

        Features:
        - Extended discussion time for strategy
        - Longer voting time for careful decisions
        - Reduced kill cooldown for action
        - Competitive balance

        Args:
            player_count: Number of players (default: 10).

        Returns:
            AmongUsAgentConfig: Tournament configuration.
        """
        return cls(
            name="tournament_game",
            player_names=[f"Competitor_{i}" for i in range(1, player_count + 1)],
            map_name="polus",
            discussion_time=90,
            voting_time=60,
            kill_cooldown=30,
            emergency_meetings_per_player=2,
            visualize=True,
        )

    @classmethod
    def educational_game(cls, player_count: int = 5) -> "AmongUsAgentConfig":
        """Create configuration for educational/demonstration purposes.

        Features:
        - Extended discussion for learning
        - Slower pace for observation
        - Higher movement speed for clarity
        - Always show task progress

        Args:
            player_count: Number of players (default: 5).

        Returns:
            AmongUsAgentConfig: Educational configuration.
        """
        return cls(
            name="educational_demo",
            player_names=[f"Student_{i}" for i in range(1, player_count + 1)],
            map_name="skeld",
            discussion_time=120,
            voting_time=45,
            kill_cooldown=60,
            player_movement_speed=1.5,
            task_bar_updates="always",
            visualize=True,
        )

    @classmethod
    def speed_game(cls, player_count: int = 8) -> "AmongUsAgentConfig":
        """Create configuration for fast-paced gameplay.

        Features:
        - Short discussion and voting times
        - Fast movement speed
        - Reduced kill cooldown
        - Quick decision making

        Args:
            player_count: Number of players (default: 8).

        Returns:
            AmongUsAgentConfig: Speed game configuration.
        """
        return cls(
            name="speed_game",
            player_names=[f"Speedster_{i}" for i in range(1, player_count + 1)],
            map_name="mira",
            discussion_time=30,
            voting_time=15,
            kill_cooldown=20,
            player_movement_speed=2.0,
            emergency_meetings_per_player=1,
            visualize=False,  # Reduced overhead for speed
        )

    model_config = {"arbitrary_types_allowed": True}
