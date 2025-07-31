"""Enhanced Gamified Debate Agent with AI Judge Integration.

This module extends the basic gamified debate with AI judge panels for sophisticated
winner determination and performance evaluation.

"""

import logging
from typing import Any, Literal

from haive.agents.conversation.debate.state import DebateState
from langchain_core.messages import SystemMessage
from langgraph.types import Command
from pydantic import Field

from haive.games.debate_v2.agent import GameDebateAgent
from haive.games.debate_v2.judges import (
    DebateJudgingPanel,
    DebateJudgment,
    create_academic_judges,
    create_public_judges,
    create_tournament_judges,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class JudgedGameDebateAgent(GameDebateAgent):
    """Gamified debate agent with AI judge panel integration.

    This agent extends the basic GameDebateAgent with sophisticated AI judge evaluation
    for more nuanced winner determination and detailed performance feedback from
    multiple judge perspectives.

    """

    # Judge system configuration
    use_ai_judges: bool = Field(
        default=True,
        description="Whether to use AI judge panel for winner determination",
    )

    judge_panel_type: Literal["tournament", "academic", "public", "custom"] = Field(
        default="tournament", description="Type of judge panel to use"
    )

    num_judges: int = Field(
        default=3,
        ge=1,
        le=15,
        description="Number of judges in the panel (odd numbers recommended to avoid ties)",
    )

    custom_judges: DebateJudgingPanel | None = Field(
        default=None, description="Custom judge panel if using custom type"
    )

    # Scoring combination
    combine_auto_and_judge_scoring: bool = Field(
        default=True,
        description="Whether to combine automatic scoring with judge evaluation",
    )

    auto_scoring_weight: float = Field(
        default=0.3, ge=0.0, le=1.0, description="Weight of automatic scoring (0.0-1.0)"
    )

    judge_scoring_weight: float = Field(
        default=0.7, ge=0.0, le=1.0, description="Weight of judge scoring (0.0-1.0)"
    )

    # Judgment storage
    final_judgment: DebateJudgment | None = Field(
        default=None, description="Final judgment from AI judge panel"
    )

    def setup_agent(self) -> None:
        """Setup the judged debate agent with judge panel."""
        super().setup_agent()

        # Initialize judge panel
        if self.use_ai_judges and not self.custom_judges:
            self.custom_judges = self._create_judge_panel()

        logger.debug(
            f"JudgedGameDebateAgent setup with judge panel: {self.judge_panel_type}"
        )

    def _create_judge_panel(self) -> DebateJudgingPanel:
        """Create appropriate judge panel based on configuration."""
        # Warn about even numbers
        if self.num_judges % 2 == 0:
            logger.warning(
                f"Even number of judges ({
                    self.num_judges
                }) can cause tie votes. Consider using {self.num_judges + 1} judges."
            )

        if self.judge_panel_type == "tournament":
            return create_tournament_judges(self.num_judges)
        elif self.judge_panel_type == "academic":
            return create_academic_judges(self.num_judges)
        elif self.judge_panel_type == "public":
            return create_public_judges(self.num_judges)
        else:  # custom
            if self.custom_judges:
                return self.custom_judges
            else:
                logger.warning(
                    "Custom judge panel requested but not provided, using tournament panel"
                )
                return create_tournament_judges(self.num_judges)

    async def conclude_conversation(self, state: DebateState) -> Command:
        """Enhanced conclusion with AI judge evaluation."""
        logger.info("🏛️ Starting AI judge evaluation for debate conclusion...")

        # Get base conclusion (with automatic scoring)
        base_conclusion = super().conclude_conversation(state)
        base_updates = (
            base_conclusion.update if hasattr(base_conclusion, "update") else {}
        )

        # Perform AI judge evaluation if enabled
        if self.use_ai_judges and self.custom_judges:
            try:
                judgment = await self._get_ai_judge_evaluation(state)
                self.final_judgment = judgment

                # Combine scoring if enabled
                if self.combine_auto_and_judge_scoring:
                    combined_scores = self._combine_scoring_methods(state, judgment)
                    base_updates["player_scores"] = combined_scores
                    base_updates["final_judgment"] = judgment
                else:
                    # Use judge scoring only
                    judge_scores = self._extract_judge_scores(judgment)
                    base_updates["player_scores"] = judge_scores
                    base_updates["final_judgment"] = judgment

                # Create enhanced conclusion message
                enhanced_conclusion = self._create_enhanced_conclusion(state, judgment)
                base_updates["messages"] = [enhanced_conclusion]

            except Exception as e:
                logger.error(f"AI judge evaluation failed: {e}")
                # Fall back to automatic scoring
                logger.info("Falling back to automatic scoring only")

        # Update with enhanced results
        enhanced_updates = {
            **base_updates,
            "conversation_ended": True,
            "current_phase": "judged_complete",
            "game_phase": "judged_complete",
        }

        return Command(update=enhanced_updates)

    async def _get_ai_judge_evaluation(self, state: DebateState) -> DebateJudgment:
        """Get evaluation from AI judge panel."""
        # Extract debate information
        players = list((self.debate_positions or {}).keys())
        positions = self.debate_positions or {}

        # Create debate transcript
        transcript = self._create_debate_transcript(state)

        # Get judgment from panel
        judgment = await self.custom_judges.judge_debate(
            topic=self.topic or "Unknown Topic",
            players=players,
            positions=positions,
            debate_transcript=transcript,
        )

        logger.info(f"🏆 AI Judges declare winner: {judgment.overall_winner}")
        logger.info(f"📊 Margin of victory: {judgment.margin_of_victory:.1%}")
        logger.info(f"🤝 Judge consensus: {judgment.consensus_level:.1%}")

        return judgment

    def _create_debate_transcript(self, state: DebateState) -> str:
        """Create a formatted transcript for judge evaluation."""
        transcript_parts = [
            f"🎯 DEBATE TOPIC: {self.topic}",
            f"👥 PARTICIPANTS: {', '.join((self.debate_positions or {}).keys())}",
            "",
            "📜 FULL DEBATE TRANSCRIPT:",
            "=" * 50,
        ]

        # Add all messages with speaker identification
        for i, message in enumerate(state.messages):
            if hasattr(message, "name") and message.name:
                speaker = message.name
            elif message.type == "human":
                speaker = "Moderator"
            elif message.type == "system":
                speaker = "System"
            else:
                speaker = f"Speaker_{i}"

            content = str(message.content)
            if len(content) > 50:  # Only add substantial content
                transcript_parts.extend([f"\n[{speaker.upper()}]:", content, ""])

        return "\n".join(transcript_parts)

    def _combine_scoring_methods(
        self, state: DebateState, judgment: DebateJudgment
    ) -> dict[str, float]:
        """Combine automatic scoring with AI judge scores."""
        auto_scores = getattr(state, "player_scores", {})
        judge_scores = self._extract_judge_scores(judgment)

        combined_scores = {}
        all_players = set(auto_scores.keys()) | set(judge_scores.keys())

        for player in all_players:
            auto_score = auto_scores.get(player, 0)
            judge_score = judge_scores.get(player, 0)

            # Normalize scores to same scale (0-100)
            auto_normalized = min(
                100, auto_score * 2
            )  # Assuming auto scores are typically 0-50
            judge_normalized = judge_score * 100 / 60  # Judge scores are 0-60

            # Weighted combination
            combined = (
                auto_normalized * self.auto_scoring_weight
                + judge_normalized * self.judge_scoring_weight
            )

            combined_scores[player] = round(combined, 1)

        return combined_scores

    def _extract_judge_scores(self, judgment: DebateJudgment) -> dict[str, float]:
        """Extract average judge scores for each player."""
        player_scores = {}

        for player, scores in judgment.judge_scores.items():
            if scores:
                avg_score = sum(score.total_score for score in scores) / len(scores)
                player_scores[player] = avg_score

        return player_scores

    def _create_enhanced_conclusion(
        self, state: DebateState, judgment: DebateJudgment
    ) -> SystemMessage:
        """Create enhanced conclusion message with judge evaluation."""

        # Get final scores (either combined or judge-only)
        final_scores = getattr(state, "player_scores", {})

        summary_parts = [
            "🏛️ **JUDGED DEBATE TOURNAMENT - FINAL DECISION** 🏛️",
            "",
            f"📋 **Topic**: {self.topic}",
            f"👥 **Participants**: {', '.join(judgment.players)}",
            f"⚖️ **Judge Panel**: {self.judge_panel_type.title()} ({len(self.custom_judges.judges) if self.custom_judges else self.num_judges} judges)",
            "",
            f"🏆 **OFFICIAL WINNER**: {judgment.overall_winner}",
            f"📊 **Margin of Victory**: {judgment.margin_of_victory:.1%}",
            f"🤝 **Judge Consensus**: {judgment.consensus_level:.1%}",
            "",
            "🏅 **FINAL SCORES**:",
        ]

        # Add final scores
        sorted_scores = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)
        for rank, (player, score) in enumerate(sorted_scores, 1):
            position = (self.debate_positions or {}).get(player, "Unknown")
            medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉"

            if self.combine_auto_and_judge_scoring:
                score_type = "Combined"
            else:
                score_type = "Judge Panel"

            summary_parts.append(
                f"  {medal} {player} ({position}): {score} points ({score_type})"
            )

        # Add judge panel summary
        summary_parts.extend(
            ["", "🏛️ **JUDGE PANEL EVALUATION**:", judgment.judgment_summary, ""]
        )

        # Add individual judge insights
        if len(judgment.judge_scores) > 0:
            summary_parts.extend(["👨‍⚖️ **INDIVIDUAL JUDGE INSIGHTS**:"])

            # Get a sample of judge reasoning
            # Show reasoning for first 2 players
            for player in judgment.players[:2]:
                player_scores = judgment.judge_scores.get(player, [])
                if player_scores:
                    best_reasoning = max(player_scores, key=lambda x: x.confidence)
                    summary_parts.append(
                        f"• **{player}** (Judge {best_reasoning.judge_name}): "
                        f"{best_reasoning.reasoning[:200]}..."
                    )

        # Tournament information
        if self.tournament_mode:
            summary_parts.extend(
                [
                    "",
                    "🏆 **TOURNAMENT ADVANCEMENT**:",
                    f"  • Match ID: {self.match_id or 'Unknown'}",
                    f"  • Bracket: {self.bracket_position or 'Unknown'}",
                    f"  • Advancing Player: {judgment.overall_winner}",
                    f"  • Victory Type: {
                        'Decisive' if judgment.margin_of_victory > 0.3 else 'Close'
                    }",
                ]
            )

        return SystemMessage(content="\n".join(summary_parts))

    @classmethod
    def create_judged_tournament_match(
        cls,
        topic: str,
        player_a: tuple[str, str],  # (name, position)
        player_b: tuple[str, str],  # (name, position)
        match_id: str,
        judge_panel_type: Literal["tournament", "academic", "public"] = "tournament",
        num_judges: int = 3,
        bracket_position: str = "tournament",
        **kwargs,
    ) -> "JudgedGameDebateAgent":
        """Create a tournament debate match with AI judge evaluation."""

        # Use the base factory method and enhance with judge configuration
        base_kwargs = {
            **kwargs,
            "use_ai_judges": True,
            "judge_panel_type": judge_panel_type,
            "num_judges": num_judges,
            "combine_auto_and_judge_scoring": True,
            "auto_scoring_weight": 0.3,
            "judge_scoring_weight": 0.7,
        }

        # Create base tournament match
        agent = cls.create_tournament_match(
            topic=topic,
            player_a=player_a,
            player_b=player_b,
            match_id=match_id,
            bracket_position=bracket_position,
            **base_kwargs,
        )

        # Override class type
        agent.__class__ = cls

        return agent

    def get_judge_panel_info(self) -> dict[str, Any]:
        """Get information about the current judge panel."""
        if not self.custom_judges:
            return {"status": "No judge panel configured"}

        return {
            "panel_type": self.judge_panel_type,
            "judge_count": len(self.custom_judges.judges),
            "judges": [
                {
                    "name": judge.name,
                    "type": judge.judge_type.value,
                    "expertise": judge.expertise_area,
                    "strictness": judge.strictness_level,
                }
                for judge in self.custom_judges.judges
            ],
            "scoring_method": (
                "Combined" if self.combine_auto_and_judge_scoring else "Judge-only"
            ),
            "weights": (
                {
                    "automatic": self.auto_scoring_weight,
                    "judges": self.judge_scoring_weight,
                }
                if self.combine_auto_and_judge_scoring
                else {"judges": 1.0}
            ),
        }

    def __repr__(self) -> str:
        """String representation of the judged debate agent."""
        mode_str = "Judged Tournament" if self.tournament_mode else "Judged Game"
        judge_info = (
            f"({self.judge_panel_type} panel)"
            if self.use_ai_judges
            else "(auto-scoring)"
        )
        positions = ", ".join(
            [
                f"{name}={pos[:15]}..."
                for name, pos in (self.debate_positions or {}).items()
            ]
        )
        return (
            f"{mode_str}DebateAgent{judge_info}(topic='{self.topic}', "
            f"positions=[{positions}], scoring={self.scoring_enabled})"
        )
