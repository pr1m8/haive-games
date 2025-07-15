"""AI Judge System for Gamified Debates.

This module provides sophisticated AI judge agents that can evaluate debates
using different criteria and scoring methodologies.
"""

import logging
from enum import Enum
from typing import Any, Dict, List, Literal, Optional

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class JudgingCriteria(str, Enum):
    """Different criteria for judging debates."""

    LOGICAL_STRENGTH = "logical_strength"
    EVIDENCE_QUALITY = "evidence_quality"
    PERSUASIVENESS = "persuasiveness"
    CLARITY = "clarity"
    CONSISTENCY = "consistency"
    REBUTTAL_QUALITY = "rebuttal_quality"
    OVERALL_PERFORMANCE = "overall_performance"


class JudgeType(str, Enum):
    """Different types of AI judges with different personalities."""

    ACADEMIC = "academic"  # Focuses on logic and evidence
    RHETORICAL = "rhetorical"  # Focuses on persuasion and style
    BALANCED = "balanced"  # Considers all factors equally
    CRITICAL = "critical"  # Very strict, hard to impress
    AUDIENCE = "audience"  # Judges from public perspective


class JudgeScore(BaseModel):
    """Individual judge's scoring for a debate."""

    judge_name: str
    judge_type: JudgeType
    criteria_scores: Dict[JudgingCriteria, int] = Field(
        description="Scores per criteria (1-10)"
    )
    total_score: int = Field(description="Total score for this player")
    reasoning: str = Field(description="Judge's reasoning for the scores")
    winner_vote: str = Field(description="Who this judge thinks won")
    confidence: float = Field(
        ge=0.0, le=1.0, description="Judge's confidence in decision"
    )


class DebateJudgment(BaseModel):
    """Complete judgment of a debate by multiple judges."""

    topic: str
    players: List[str]
    judge_scores: Dict[str, List[JudgeScore]] = Field(
        description="Judge scores for each player"
    )
    overall_winner: str
    margin_of_victory: float = Field(description="How decisive the victory was")
    consensus_level: float = Field(ge=0.0, le=1.0, description="How much judges agreed")
    judgment_summary: str


class AIDebateJudge:
    """AI judge that evaluates debate performances."""

    def __init__(
        self,
        name: str,
        judge_type: JudgeType = JudgeType.BALANCED,
        expertise_area: Optional[str] = None,
        strictness_level: float = 0.5,
    ):
        self.name = name
        self.judge_type = judge_type
        self.expertise_area = expertise_area
        self.strictness_level = strictness_level

        # Create specialized judge agent
        self.agent = self._create_judge_agent()

    def _create_judge_agent(self) -> SimpleAgent:
        """Create the AI agent for this judge."""

        # Base personality traits
        personalities = {
            JudgeType.ACADEMIC: {
                "focus": "logical reasoning, evidence quality, and factual accuracy",
                "style": "analytical and precise",
                "bias": "toward well-researched, logically sound arguments",
            },
            JudgeType.RHETORICAL: {
                "focus": "persuasive power, speaking style, and emotional impact",
                "style": "appreciates eloquence and charisma",
                "bias": "toward compelling delivery and audience appeal",
            },
            JudgeType.BALANCED: {
                "focus": "all aspects of debate performance equally",
                "style": "fair and comprehensive",
                "bias": "none - evaluates all criteria objectively",
            },
            JudgeType.CRITICAL: {
                "focus": "finding flaws and weaknesses in arguments",
                "style": "strict and demanding high standards",
                "bias": "toward perfect execution and flawless logic",
            },
            JudgeType.AUDIENCE: {
                "focus": "what would appeal to a general public audience",
                "style": "considers accessibility and relatability",
                "bias": "toward arguments that regular people would find convincing",
            },
        }

        personality = personalities[self.judge_type]
        expertise_text = (
            f" with expertise in {self.expertise_area}" if self.expertise_area else ""
        )

        system_message = f"""🏛️ DEBATE JUDGE: {self.name.upper()} 🏛️

You are {self.name}, a professional debate judge{expertise_text}.

JUDGE PROFILE:
• Type: {self.judge_type.value.title()} Judge
• Focus: {personality['focus']}
• Style: {personality['style']}
• Approach: {personality['bias']}
• Strictness: {self.strictness_level:.1f}/1.0

JUDGING METHODOLOGY:
You evaluate debates using these criteria (score 1-10 each):
1. 🧠 Logical Strength - How sound are the arguments?
2. 📊 Evidence Quality - How well-researched and credible?  
3. 🎯 Persuasiveness - How convincing to the target audience?
4. 💭 Clarity - How clear and well-organized?
5. 🔄 Consistency - How consistent throughout the debate?
6. ⚔️ Rebuttal Quality - How well did they counter opponents?

SCORING GUIDELINES:
• 1-3: Poor/Weak performance
• 4-6: Average/Adequate performance  
• 7-8: Good/Strong performance
• 9-10: Excellent/Outstanding performance

RESPONSE FORMAT:
Provide scores as JSON with this structure:
{{
    "criteria_scores": {{
        "logical_strength": X,
        "evidence_quality": X,
        "persuasiveness": X,
        "clarity": X,
        "consistency": X,
        "rebuttal_quality": X
    }},
    "total_score": X,
    "reasoning": "Detailed explanation of scoring...",
    "winner_vote": "Player Name",
    "confidence": 0.X
}}

Be {personality['style']} in your evaluation. Consider your {self.judge_type.value} perspective."""

        engine = AugLLMConfig(
            name=f"{self.name.lower()}_judge_engine",
            system_message=system_message,
            temperature=0.3,  # Consistent judging
            max_tokens=1000,
        )

        return SimpleAgent(name=f"{self.name}_judge_agent", engine=engine)

    async def judge_player_performance(
        self, player_name: str, player_position: str, debate_transcript: str, topic: str
    ) -> JudgeScore:
        """Judge a single player's performance in the debate."""

        judgment_prompt = f"""🏛️ JUDGE EVALUATION REQUEST 🏛️

DEBATE DETAILS:
• Topic: "{topic}"
• Player: {player_name}
• Position: {player_position}

FULL DEBATE TRANSCRIPT:
{debate_transcript}

TASK: Evaluate {player_name}'s performance based on your judging criteria.

Focus specifically on {player_name}'s contributions. Consider:
• How well did they argue their position?
• Quality of their evidence and examples
• Effectiveness of their rebuttals
• Clarity and organization of their points
• Consistency with their stated position
• Overall persuasive impact

Provide your evaluation in the specified JSON format."""

        try:
            response = await self.agent.arun(judgment_prompt)

            # Parse JSON response (would need proper JSON parsing in production)
            import json
            import re

            # Extract JSON from response
            json_match = re.search(r"\{.*\}", response, re.DOTALL)
            if json_match:
                score_data = json.loads(json_match.group())

                return JudgeScore(
                    judge_name=self.name,
                    judge_type=self.judge_type,
                    criteria_scores={
                        JudgingCriteria(k): v
                        for k, v in score_data["criteria_scores"].items()
                    },
                    total_score=score_data["total_score"],
                    reasoning=score_data["reasoning"],
                    winner_vote=score_data["winner_vote"],
                    confidence=score_data["confidence"],
                )
            else:
                # Fallback if JSON parsing fails
                return self._create_fallback_score(player_name, response)

        except Exception as e:
            logger.error(f"Judge {self.name} failed to evaluate {player_name}: {e}")
            return self._create_fallback_score(player_name, f"Error: {e}")

    def _create_fallback_score(self, player_name: str, response: str) -> JudgeScore:
        """Create a fallback score if parsing fails."""
        return JudgeScore(
            judge_name=self.name,
            judge_type=self.judge_type,
            criteria_scores={
                JudgingCriteria.LOGICAL_STRENGTH: 6,
                JudgingCriteria.EVIDENCE_QUALITY: 6,
                JudgingCriteria.PERSUASIVENESS: 6,
                JudgingCriteria.CLARITY: 6,
                JudgingCriteria.CONSISTENCY: 6,
                JudgingCriteria.REBUTTAL_QUALITY: 6,
            },
            total_score=36,
            reasoning=f"Fallback scoring due to parsing error. Judge response: {response[:200]}...",
            winner_vote=player_name,
            confidence=0.3,
        )


class DebateJudgingPanel:
    """Panel of multiple AI judges for comprehensive debate evaluation."""

    def __init__(self, judges: List[AIDebateJudge]):
        self.judges = judges

    @classmethod
    def create_standard_panel(cls, num_judges: int = 3) -> "DebateJudgingPanel":
        """Create a standard panel with configurable number of randomized judges.

        Args:
            num_judges: Number of judges to include (default: 3 to avoid ties)
                       Must be odd number for proper tie-breaking.
        """
        import random

        # Ensure odd number for tie-breaking
        if num_judges % 2 == 0:
            logger.warning(
                f"Even number of judges ({num_judges}) can cause ties. Consider using {num_judges + 1} judges."
            )

        # Pool of judge profiles for debates
        judge_profiles = [
            ("Prof_Logic", JudgeType.ACADEMIC, "Philosophy and Logic"),
            ("Dr_Evidence", JudgeType.ACADEMIC, "Research and Statistics"),
            ("Judge_Fair", JudgeType.BALANCED, "General Debate"),
            ("Ms_Persuasion", JudgeType.RHETORICAL, "Public Speaking"),
            ("Critic_Sharp", JudgeType.CRITICAL, "Argument Analysis"),
            ("Voice_Public", JudgeType.AUDIENCE, "Public Appeal"),
            ("Prof_Rhetoric", JudgeType.RHETORICAL, "Classical Rhetoric"),
            ("Dr_Analysis", JudgeType.ACADEMIC, "Systematic Analysis"),
            ("Judge_Strict", JudgeType.CRITICAL, "High Standards"),
            ("Eval_Balanced", JudgeType.BALANCED, "Fair Evaluation"),
            ("Expert_Logic", JudgeType.ACADEMIC, "Logical Reasoning"),
            ("Voice_Crowd", JudgeType.AUDIENCE, "Popular Appeal"),
        ]

        # Ensure we have enough profiles for the requested number
        if num_judges > len(judge_profiles):
            # If we need more judges than profiles, we'll reuse with different strictness
            logger.info(
                f"Requested {num_judges} judges but only have {len(judge_profiles)} profiles. Will reuse profiles with different configurations."
            )
            selected_profiles = []
            available_profiles = judge_profiles.copy()

            for i in range(num_judges):
                if not available_profiles:
                    available_profiles = judge_profiles.copy()
                profile = random.choice(available_profiles)
                available_profiles.remove(profile)
                selected_profiles.append(profile)
        else:
            # Randomly select the requested number of different judge profiles
            selected_profiles = random.sample(judge_profiles, num_judges)

        judges = [
            AIDebateJudge(
                name=profile[0],
                judge_type=profile[1],
                expertise_area=profile[2],
                strictness_level=round(random.uniform(0.4, 0.8), 1),
            )
            for profile in selected_profiles
        ]

        return cls(judges)

    @classmethod
    def create_expert_panel(cls, expertise_area: str) -> "DebateJudgingPanel":
        """Create a panel specialized in a particular area."""
        judges = [
            AIDebateJudge("Expert_1", JudgeType.ACADEMIC, expertise_area, 0.8),
            AIDebateJudge("Expert_2", JudgeType.CRITICAL, expertise_area, 0.9),
            AIDebateJudge("Practitioner", JudgeType.RHETORICAL, expertise_area, 0.6),
            AIDebateJudge("Generalist", JudgeType.BALANCED, "Cross-disciplinary", 0.5),
        ]
        return cls(judges)

    async def judge_debate(
        self,
        topic: str,
        players: List[str],
        positions: Dict[str, str],
        debate_transcript: str,
    ) -> DebateJudgment:
        """Get comprehensive judgment from all judges."""

        logger.info(f"🏛️ Judging panel evaluating debate: '{topic}'")
        logger.info(f"👥 Players: {', '.join(players)}")
        logger.info(f"⚖️ Judges: {', '.join([j.name for j in self.judges])}")

        # Get scores from all judges for all players
        all_scores: Dict[str, List[JudgeScore]] = {player: [] for player in players}

        for judge in self.judges:
            logger.info(
                f"🔍 Judge {judge.name} ({judge.judge_type.value}) evaluating..."
            )

            for player in players:
                score = await judge.judge_player_performance(
                    player_name=player,
                    player_position=positions[player],
                    debate_transcript=debate_transcript,
                    topic=topic,
                )
                all_scores[player].append(score)

        # Calculate overall results
        winner, margin, consensus = self._calculate_winner(all_scores)
        summary = self._create_judgment_summary(
            topic, players, all_scores, winner, margin
        )

        return DebateJudgment(
            topic=topic,
            players=players,
            judge_scores=all_scores,
            overall_winner=winner,
            margin_of_victory=margin,
            consensus_level=consensus,
            judgment_summary=summary,
        )

    def _calculate_winner(
        self, all_scores: Dict[str, List[JudgeScore]]
    ) -> tuple[str, float, float]:
        """Calculate overall winner from all judge scores."""

        # Calculate average scores per player
        player_averages = {}
        player_votes = {}

        for player, scores in all_scores.items():
            total_score = sum(score.total_score for score in scores)
            player_averages[player] = total_score / len(scores)

            # Count winner votes
            votes = sum(1 for score in scores if score.winner_vote == player)
            player_votes[player] = votes

        # Determine winner (by votes first, then by average score)
        winner_by_votes = max(player_votes.items(), key=lambda x: x[1])
        winner_by_score = max(player_averages.items(), key=lambda x: x[1])

        # Use votes as primary, score as tiebreaker
        if winner_by_votes[1] > len(self.judges) / 2:
            winner = winner_by_votes[0]
        else:
            winner = winner_by_score[0]

        # Calculate margin of victory
        scores = list(player_averages.values())
        scores.sort(reverse=True)
        margin = (scores[0] - scores[1]) / scores[0] if len(scores) > 1 else 1.0

        # Calculate consensus (how much judges agreed)
        total_possible_votes = len(self.judges)
        winning_votes = player_votes[winner]
        consensus = winning_votes / total_possible_votes

        return winner, margin, consensus

    def _create_judgment_summary(
        self,
        topic: str,
        players: List[str],
        all_scores: Dict[str, List[JudgeScore]],
        winner: str,
        margin: float,
    ) -> str:
        """Create a comprehensive summary of the judging results."""

        summary_parts = [
            f"🏛️ **JUDICIAL PANEL DECISION** 🏛️",
            f"",
            f"**Debate Topic**: {topic}",
            f"**Participants**: {', '.join(players)}",
            f"**Judges**: {', '.join([j.name for j in self.judges])}",
            f"",
            f"🏆 **WINNER**: {winner}",
            f"📊 **Margin of Victory**: {margin:.1%}",
            f"",
            "⚖️ **JUDGE BREAKDOWN**:",
        ]

        # Add individual judge perspectives
        for judge in self.judges:
            judge_votes = []
            for player in players:
                player_scores = all_scores[player]
                judge_score = next(
                    s for s in player_scores if s.judge_name == judge.name
                )
                if judge_score.winner_vote == player:
                    judge_votes.append(f"👑 {player}")
                else:
                    judge_votes.append(f"   {player}")

            summary_parts.append(
                f"  • {judge.name} ({judge.judge_type.value}): {', '.join(judge_votes)}"
            )

        # Add score summary
        summary_parts.extend(["", "📈 **AVERAGE SCORES**:"])

        for player in players:
            scores = all_scores[player]
            avg_score = sum(s.total_score for s in scores) / len(scores)
            votes = sum(1 for s in scores if s.winner_vote == player)
            summary_parts.append(
                f"  • {player}: {avg_score:.1f}/60 points ({votes}/{len(self.judges)} votes)"
            )

        return "\n".join(summary_parts)


# Factory functions for easy judge creation
def create_tournament_judges(num_judges: int = 3) -> DebateJudgingPanel:
    """Create judges suitable for tournament play.

    Args:
        num_judges: Number of judges (default: 3 to avoid ties)
    """
    return DebateJudgingPanel.create_standard_panel(num_judges)


def create_academic_judges(num_judges: int = 3) -> DebateJudgingPanel:
    """Create academic judges focused on evidence and logic.

    Args:
        num_judges: Number of judges (default: 3)
    """
    import random

    if num_judges % 2 == 0:
        logger.warning(
            f"Even number of judges ({num_judges}) can cause ties. Consider using {num_judges + 1} judges."
        )

    academic_profiles = [
        ("Prof_Logic", JudgeType.ACADEMIC, "Philosophy and Logic"),
        ("Dr_Research", JudgeType.ACADEMIC, "Research Methodology"),
        ("Dean_Critical", JudgeType.CRITICAL, "Academic Standards"),
        ("Scholar_Evidence", JudgeType.ACADEMIC, "Evidence Analysis"),
        ("Prof_Theory", JudgeType.ACADEMIC, "Theoretical Framework"),
        ("Dr_Methodology", JudgeType.ACADEMIC, "Scientific Method"),
    ]

    # Select judges with higher strictness for academic panel
    if num_judges > len(academic_profiles):
        selected_profiles = []
        available = academic_profiles.copy()
        for i in range(num_judges):
            if not available:
                available = academic_profiles.copy()
            profile = random.choice(available)
            available.remove(profile)
            selected_profiles.append(profile)
    else:
        selected_profiles = random.sample(academic_profiles, num_judges)

    judges = [
        AIDebateJudge(
            name=profile[0],
            judge_type=profile[1],
            expertise_area=profile[2],
            strictness_level=round(
                random.uniform(0.7, 0.9), 1
            ),  # Higher strictness for academic
        )
        for profile in selected_profiles
    ]

    return DebateJudgingPanel(judges)


def create_public_judges(num_judges: int = 3) -> DebateJudgingPanel:
    """Create public judges focused on accessibility and appeal.

    Args:
        num_judges: Number of judges (default: 3)
    """
    import random

    if num_judges % 2 == 0:
        logger.warning(
            f"Even number of judges ({num_judges}) can cause ties. Consider using {num_judges + 1} judges."
        )

    public_profiles = [
        ("Voice_Public", JudgeType.AUDIENCE, "Public Opinion"),
        ("Citizen_Rep", JudgeType.AUDIENCE, "Citizen Perspective"),
        ("Media_Voice", JudgeType.RHETORICAL, "Media Communication"),
        ("Common_Sense", JudgeType.BALANCED, "Practical Thinking"),
        ("Appeal_Judge", JudgeType.RHETORICAL, "Popular Appeal"),
        ("Fair_Moderator", JudgeType.BALANCED, "Public Debate"),
    ]

    if num_judges > len(public_profiles):
        selected_profiles = []
        available = public_profiles.copy()
        for i in range(num_judges):
            if not available:
                available = public_profiles.copy()
            profile = random.choice(available)
            available.remove(profile)
            selected_profiles.append(profile)
    else:
        selected_profiles = random.sample(public_profiles, num_judges)

    judges = [
        AIDebateJudge(
            name=profile[0],
            judge_type=profile[1],
            expertise_area=profile[2],
            strictness_level=round(
                random.uniform(0.3, 0.6), 1
            ),  # Lower strictness for public appeal
        )
        for profile in selected_profiles
    ]

    return DebateJudgingPanel(judges)
