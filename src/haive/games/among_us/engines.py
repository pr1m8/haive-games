# among_us_engines.py

from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import OpenAILLMConfig
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from haive.games.among_us.prompts import (
    CREWMATE_PROMPT,
    IMPOSTOR_PROMPT,
    MEETING_PROMPT,
    VOTING_PROMPT,
)


class AmongUsEngines:
    """Engines for the Among Us game.

    This class creates and manages the LLM engines used for different player roles and
    game phases.

    """

    @classmethod
    def create_engines(
        cls, llm_config: dict[str, Any] | None = None
    ) -> dict[str, dict[str, AugLLMConfig]]:
        """Create the engines for the Among Us game.

        Args:
            llm_config: Optional configuration for the language model

        Returns:
            A dictionary of engines organized by role and game phase

        """
        # Default LLM config
        default_llm_config = {
            "model": "gpt-4o",
            "parameters": {"temperature": 0.8, "top_p": 0.9},
        }

        # Merge with provided LLM config if any
        llm_config = {**default_llm_config, **(llm_config or {})}

        # Create Azure LLM config
        azure_llm_config = OpenAILLMConfig(**llm_config)

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

    @classmethod
    def create_runnable_engines(
        cls, llm_config: dict[str, Any] | None = None
    ) -> dict[str, dict[str, Any]]:
        """Create runnable engines for the Among Us game.

        Args:
            llm_config: Optional configuration for the language model

        Returns:
            A dictionary of runnable engines organized by role and game phase

        """
        engines_config = cls.create_engines(llm_config)
        runnable_engines = {}

        for role, role_engines in engines_config.items():
            runnable_engines[role] = {}
            for phase, engine_config in role_engines.items():
                runnable_engines[role][phase] = engine_config.create_runnable()

        return runnable_engines
