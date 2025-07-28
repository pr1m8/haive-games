"""State core module.

This module provides state functionality for the Haive framework.

Classes:
    DebateState: DebateState implementation.

Functions:
    current_speaker: Current Speaker functionality.
"""

# src/haive/games/debate/state.py
from pydantic import Field

from haive.games.debate.models import DebatePhase, Participant, Statement, Topic, Vote
from haive.games.framework.multi_player.state import MultiPlayerGameState


class DebateState(MultiPlayerGameState):
    """State model for debate-style interactions."""

    # Core elements
    topic: Topic = Field(..., description="The topic being debated")
    participants: dict[str, Participant] = Field(
        default_factory=dict, description="Debate participants"
    )
    statements: list[Statement] = Field(
        default_factory=list, description="History of statements"
    )
    current_speaker_idx: int = Field(0, description="Index of the current speaker")

    # Phase management
    debate_phase: str = Field(DebatePhase.SETUP, description="Current debate phase")
    phase_time_limit: int | None = Field(
        None, description="Time limit for current phase"
    )
    phase_statement_limit: int | None = Field(
        None, description="Maximum statements in phase"
    )

    # Voting and scoring
    votes: dict[str, list[Vote]] = Field(
        default_factory=dict, description="Votes from participants"
    )
    scores: dict[str, float] = Field(
        default_factory=dict, description="Current participant scores"
    )

    # Moderation controls
    interruptions_allowed: bool = Field(
        False, description="Whether interruptions are allowed"
    )
    moderator_id: str | None = Field(None, description="ID of the moderator if any")
    moderation_notes: list[str] = Field(
        default_factory=list, description="Moderation notes"
    )

    # Format-specific fields
    time_remaining: dict[str, int] = Field(
        default_factory=dict, description="Time remaining per participant"
    )
    turn_order: list[str] = Field(
        default_factory=list, description="Order of turns if not round-robin"
    )

    @property
    def current_speaker(self) -> str:
        """Get the current speaker's ID."""
        if 0 <= self.current_speaker_idx < len(self.turn_order):
            return self.turn_order[self.current_speaker_idx]
        return ""
