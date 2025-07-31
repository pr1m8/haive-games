# src/haive/games/debate/factory.py

from typing import Any

from haive.games.debate.agent import DebateAgent
from haive.games.debate.config import DebateAgentConfig


class DebateFactory:
    """Factory for creating specialized debate formats."""

    @staticmethod
    def create_presidential_debate(
        candidates: list[dict[str, Any]], moderator_name: str, topic: str
    ) -> DebateAgent:
        """Create a presidential debate format.

        Args:
            candidates: List of candidate details
            moderator_name: Name of debate moderator
            topic: Debate topic

        Returns:
            DebateAgent: Configured presidential debate agent
        """
        # Create config
        config = DebateAgentConfig.presidential()

        # Setup initial state
        [moderator_name] + [c.get("name") for c in candidates]

        # Create agent
        agent = DebateAgent(config)

        # Initialize with custom data
        {
            "title": topic,
            "description": f"Presidential debate on {topic}",
            "keywords": topic.split(),
        }

        # Setup personas
        personas = {}
        for candidate in candidates:
            name = candidate.get("name")
            personas[name] = {
                "id": name,
                "name": name,
                "role": "debater",
                "position": candidate.get("position", "neutral"),
                "persona": candidate.get("persona", {}),
                "expertise": candidate.get("expertise", []),
            }

        # Add moderator
        personas[moderator_name] = {
            "id": moderator_name,
            "name": moderator_name,
            "role": "moderator",
        }

        return agent

    @staticmethod
    def create_legal_trial(
        case_details: dict[str, Any], participants: dict[str, str]
    ) -> DebateAgent:
        """Create a legal trial format.

        Args:
            case_details: Details of the legal case
            participants: Dict mapping participant IDs to roles

        Returns:
            DebateAgent: Configured trial debate agent
        """
        # Create config
        config = DebateAgentConfig.trial()

        # Create agent
        agent = DebateAgent(config)

        # Create topic from case details
        {
            "title": case_details.get("title", "Legal Case"),
            "description": case_details.get("description", ""),
            "keywords": case_details.get("keywords", []),
        }

        # Setup initial state with roles

        return agent

    @staticmethod
    def create_panel_discussion(
        panel_topic: str, host_name: str, panelists: list[dict[str, Any]]
    ) -> DebateAgent:
        """Create a panel discussion format.

        Args:
            panel_topic: Topic of discussion
            host_name: Name of panel host/moderator
            panelists: List of panelist details

        Returns:
            DebateAgent: Configured panel discussion agent
        """
        # Create config
        config = DebateAgentConfig.panel_discussion()

        # Create agent
        agent = DebateAgent(config)

        # Create topic
        {
            "title": panel_topic,
            "description": f"Panel discussion on {panel_topic}",
            "keywords": panel_topic.split(),
        }

        # Setup participants
        participants = {}

        # Add host
        participants[host_name] = {
            "id": host_name,
            "name": host_name,
            "role": "moderator",
        }

        # Add panelists
        for panelist in panelists:
            name = panelist.get("name")
            participants[name] = {
                "id": name,
                "name": name,
                "role": "debater",
                "position": panelist.get("position", "neutral"),
                "expertise": panelist.get("expertise", []),
                "persona": panelist.get("persona", {}),
            }

        # Setup initial state

        return agent

    @staticmethod
    def create_prisoner_dilemma(
        prisoners: list[dict[str, Any]], scenario: str
    ) -> DebateAgent:
        """Create a prisoner's dilemma simulation.

        Args:
            prisoners: List of prisoner details
            scenario: Description of the dilemma scenario

        Returns:
            DebateAgent: Configured prisoner's dilemma agent
        """
        # Create custom config
        config = DebateAgentConfig(
            name="prisoner_dilemma",
            debate_format="dilemma",
            time_limit=300,
            max_statements=5,
            allow_interruptions=False,
            voting_enabled=True,
        )

        # Create agent
        agent = DebateAgent(config)

        # Create topic

        # Setup participants
        participants = {}
        for prisoner in prisoners:
            name = prisoner.get("name")
            participants[name] = {
                "id": name,
                "name": name,
                "role": "prisoner",
                "persona": prisoner.get("persona", {}),
            }

        # Add interrogator
        participants["Interrogator"] = {
            "id": "Interrogator",
            "name": "Interrogator",
            "role": "moderator",
        }

        # Setup initial state

        return agent
