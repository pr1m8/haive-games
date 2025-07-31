"""Generalized AI Voting System for Game Winner Determination.

This module provides a reusable voting system that can evaluate game
performance across different game types using AI judges with specialized
perspectives.
"""

import json
import logging
import random
import re
from enum import Enum
from typing import Any, Protocol

from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field

from haive.games.simple.agent import SimpleAgent

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class JudgePersonality(str, Enum):
    """Different AI judge personalities for game evaluation."""

    STRATEGIC = "strategic"  # Focuses on strategy and tactics
    ANALYTICAL = "analytical"  # Focuses on logic and analysis
    BALANCED = "balanced"  # Considers all factors equally
    AUDIENCE = "audience"  # Judges from spectator perspective


class VoteChoice(BaseModel):
    """A judge's vote choice with reasoning."""

    choice: str = Field(description="The judge's choice (player name, option, etc.)")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in the choice")
    reasoning: str = Field(description="Detailed reasoning for the choice")
    criteria_scores: dict[str, int] = Field(
        default_factory=dict, description="Scores on specific criteria"
    )


class VotingResult(BaseModel):
    """Complete voting results from multiple judges."""

    topic: str = Field(description="What was being voted on")
    options: list[str] = Field(description="Available choices")
    judge_votes: dict[str, VoteChoice] = Field(description="Each judge's vote")
    winner: str = Field(description="The winning choice")
    margin: float = Field(ge=0.0, le=1.0, description="Margin of victory")
    consensus: float = Field(ge=0.0, le=1.0, description="Level of agreement")
    summary: str = Field(description="Summary of the voting results")


class GameEvaluator(Protocol):
    """Protocol for game-specific evaluation logic."""

    def get_evaluation_criteria(self) -> list[str]:
        """Get the criteria this game should be judged on."""
        ...

    def format_game_data(self, game_data: Any) -> str:
        """Format game data for judge evaluation."""
        ...

    def get_evaluation_context(self) -> str:
        """Get context-specific information for judges."""
        ...


class AIGameJudge:
    """AI judge that can evaluate any game type."""

    def __init__(
        self,
        name: str,
        personality: JudgePersonality = JudgePersonality.BALANCED,
        expertise_area: str | None = None,
        focus_weight: float = 0.5,
    ):
        self.name = name
        self.personality = personality
        self.expertise_area = expertise_area
        self.focus_weight = focus_weight  # How strongly focused vs general

        # Create the AI agent for this judge
        self.agent = self._create_judge_agent()

    def _create_judge_agent(self) -> SimpleAgent:
        """Create the AI agent for this judge."""
        personalities = {
            JudgePersonality.STRATEGIC: {
                "focus": "strategic thinking, tactical decisions, and competitive advantage",
                "style": "analytical and strategy-focused",
                "bias": "toward smart plays and strategic depth",
            },
            JudgePersonality.ANALYTICAL: {
                "focus": "logical analysis, systematic thinking, and objective evaluation",
                "style": "methodical and evidence-based",
                "bias": "toward clear reasoning and logical consistency",
            },
            JudgePersonality.BALANCED: {
                "focus": "all aspects of performance equally",
                "style": "fair and comprehensive",
                "bias": "none - evaluates all criteria objectively",
            },
            JudgePersonality.AUDIENCE: {
                "focus": "entertainment value, accessibility, and spectator appeal",
                "style": "considers what would be engaging to watch",
                "bias": "toward exciting and understandable play",
            },
        }

        personality_info = personalities[self.personality]
        expertise_text = (
            f" with expertise in {self.expertise_area}" if self.expertise_area else ""
        )

        system_message = f"""🎯 GAME JUDGE: {self.name.upper()} 🎯

You are {self.name}, a professional game judge{expertise_text}.

JUDGE PROFILE:
• Personality: {self.personality.value.title()}
• Focus: {personality_info["focus"]}
• Style: {personality_info["style"]}
• Approach: {personality_info["bias"]}
• Focus Weight: {self.focus_weight:.1f}/1.0

JUDGING METHODOLOGY:
You evaluate game performance across multiple criteria and provide:
1. 🎯 Choice - Your selection of the winner/best option
2. 📊 Confidence - How confident you are (0.0-1.0)
3. 💭 Reasoning - Detailed explanation of your decision
4. 📈 Criteria Scores - Specific scores on relevant criteria

RESPONSE FORMAT:
Provide your evaluation as JSON:
{{
    "choice": "Winner/Option Name",
    "confidence": 0.X,
    "reasoning": "Detailed explanation...",
    "criteria_scores": {{
        "criterion1": X,
        "criterion2": X
    }}
}}

Be {personality_info["style"]} in your evaluation. Focus on {personality_info["focus"]}."""

        engine = AugLLMConfig(
            name=f"{self.name.lower()}_judge_engine",
            system_message=system_message,
            temperature=0.3,  # Consistent judging
            max_tokens=800,
        )

        return SimpleAgent(name=f"{self.name}_judge_agent", engine=engine)

    async def evaluate(
        self, topic: str, options: list[str], game_data: str, criteria: list[str]
    ) -> VoteChoice:
        """Evaluate the game and return a vote choice."""
        criteria_text = "\n".join([f"• {criterion}" for criterion in criteria])
        options_text = "\n".join([f"• {option}" for option in options])

        evaluation_prompt = f"""🎯 GAME EVALUATION REQUEST 🎯

EVALUATION TOPIC: {topic}

AVAILABLE OPTIONS:
{options_text}

JUDGING CRITERIA:
{criteria_text}

GAME DATA:
{game_data}

TASK: Evaluate the performance and select your choice based on your judging style.

Consider your {self.personality.value} perspective and provide your evaluation
in the specified JSON format."""

        try:
            response = await self.agent.arun(evaluation_prompt)

            # Parse JSON response

            json_match = re.search(r"\{.*\}", response, re.DOTALL)
            if json_match:
                vote_data = json.loads(json_match.group())

                return VoteChoice(
                    choice=vote_data["choice"],
                    confidence=vote_data["confidence"],
                    reasoning=vote_data["reasoning"],
                    criteria_scores=vote_data.get("criteria_scores", {}),
                )
            # Fallback if JSON parsing fails
            return self._create_fallback_vote(options[0], response)

        except Exception as e:
            logger.exception(f"Judge {self.name} evaluation failed: {e}")
            return self._create_fallback_vote(
                options[0] if options else "Unknown", f"Error: {e}"
            )

    def _create_fallback_vote(self, choice: str, response: str) -> VoteChoice:
        """Create a fallback vote if parsing fails."""
        return VoteChoice(
            choice=choice,
            confidence=0.3,
            reasoning=f"Fallback vote due to parsing error. Response: {response[:200]}...",
            criteria_scores={},
        )


class GameVotingSystem:
    """Generalized voting system for any game type."""

    def __init__(self, judges: list[AIGameJudge]):
        self.judges = judges

    @classmethod
    def create_standard_judges(cls, num_judges: int = 3) -> "GameVotingSystem":
        """Create standard judge panel with configurable size and randomized
        personalities.

        Args:
            num_judges: Number of judges to create (default: 3 to avoid ties)
                       Odd numbers recommended to prevent tie votes.
        """

        # Warn about even numbers that can cause ties
        if num_judges % 2 == 0:
            logger.warning(
                f"Even number of judges ({
                    num_judges
                }) can cause tie votes. Consider using {num_judges + 1} judges."
            )

        # Pool of possible judge names and traits
        judge_names = [
            "Judge_Alpha",
            "Judge_Beta",
            "Judge_Gamma",
            "Judge_Delta",
            "Judge_Epsilon",
            "Prof_Analysis",
            "Dr_Logic",
            "Expert_Fair",
            "Master_Review",
            "Scholar_Wise",
            "Critic_Sharp",
            "Eval_Pro",
            "Judge_Keen",
            "Assessor_Prime",
            "Review_Chief",
            "Judge_Omega",
            "Expert_Core",
            "Analyst_Prime",
            "Eval_Master",
            "Judge_Zeta",
        ]

        personalities = list(JudgePersonality)
        expertises = [
            "Strategic Analysis",
            "Game Theory",
            "Competitive Play",
            "Performance Analysis",
            "Fair Evaluation",
            "Critical Assessment",
            "Decision Analysis",
            "Objective Review",
            "Strategic Planning",
            "Competitive Strategy",
            "Performance Metrics",
            "Quality Assessment",
        ]

        # Generate enough unique combinations
        judges = []
        used_names = set()

        for _i in range(num_judges):
            # Select unique name
            available_names = [name for name in judge_names if name not in used_names]
            if not available_names:
                # Reset if we've used all names
                used_names.clear()
                available_names = judge_names

            selected_name = random.choice(available_names)
            used_names.add(selected_name)

            # Random personality and expertise (can repeat)
            selected_personality = random.choice(personalities)
            selected_expertise = random.choice(expertises)

            judge = AIGameJudge(
                selected_name,
                selected_personality,
                selected_expertise,
                round(random.uniform(0.4, 0.8), 1),
            )
            judges.append(judge)

        return cls(judges)

    @classmethod
    def create_game_specific_judges(
        cls, game_type: str, num_judges: int = 3
    ) -> "GameVotingSystem":
        """Create judges specialized for a specific game type.

        Args:
            game_type: Type of game to create judges for
            num_judges: Number of judges to create (default: 3)
        """

        if num_judges % 2 == 0:
            logger.warning(
                f"Even number of judges ({
                    num_judges
                }) can cause tie votes. Consider using {num_judges + 1} judges."
            )

        # Base judge profiles for each game type
        game_judge_pools = {
            "chess": [
                (
                    "Chess_Grandmaster",
                    JudgePersonality.STRATEGIC,
                    "Chess Grandmaster",
                    0.9,
                ),
                ("Chess_Tactician", JudgePersonality.STRATEGIC, "Chess Tactics", 0.8),
                ("Chess_Analyst", JudgePersonality.ANALYTICAL, "Chess Analysis", 0.7),
                ("Chess_Teacher", JudgePersonality.BALANCED, "Chess Education", 0.6),
                ("Chess_Fan", JudgePersonality.AUDIENCE, "Chess Entertainment", 0.4),
            ],
            "debate": [
                (
                    "Logic_Master",
                    JudgePersonality.ANALYTICAL,
                    "Logic and Evidence",
                    0.8,
                ),
                (
                    "Rhetoric_Expert",
                    JudgePersonality.STRATEGIC,
                    "Rhetorical Strategy",
                    0.7,
                ),
                ("Appeal_Judge", JudgePersonality.BALANCED, "Overall Appeal", 0.6),
                ("Public_Voice", JudgePersonality.AUDIENCE, "Public Persuasion", 0.5),
                (
                    "Critical_Thinker",
                    JudgePersonality.ANALYTICAL,
                    "Critical Analysis",
                    0.9,
                ),
            ],
            "poker": [
                (
                    "Poker_Champion",
                    JudgePersonality.STRATEGIC,
                    "Poker Championship",
                    0.9,
                ),
                (
                    "Poker_Analyst",
                    JudgePersonality.ANALYTICAL,
                    "Poker Mathematics",
                    0.8,
                ),
                ("Poker_Pro", JudgePersonality.STRATEGIC, "Professional Poker", 0.8),
                (
                    "Poker_Observer",
                    JudgePersonality.AUDIENCE,
                    "Poker Entertainment",
                    0.4,
                ),
                (
                    "Poker_Psychologist",
                    JudgePersonality.ANALYTICAL,
                    "Player Psychology",
                    0.7,
                ),
            ],
            "go": [
                ("Go_Master", JudgePersonality.STRATEGIC, "Go Mastery", 0.9),
                ("Go_Strategist", JudgePersonality.STRATEGIC, "Go Strategy", 0.8),
                ("Go_Aesthetic", JudgePersonality.BALANCED, "Go Beauty", 0.6),
                ("Go_Teacher", JudgePersonality.BALANCED, "Go Education", 0.7),
                ("Go_Enthusiast", JudgePersonality.AUDIENCE, "Go Appreciation", 0.5),
            ],
        }

        # Get judge pool for this game type, or fall back to general
        judge_pool = game_judge_pools.get(game_type)
        if not judge_pool:
            return cls.create_standard_judges(num_judges)

        # Select judges from the pool
        if num_judges > len(judge_pool):
            # If we need more judges than available, cycle through
            selected_judges = []
            for i in range(num_judges):
                pool_index = i % len(judge_pool)
                profile = judge_pool[pool_index]
                # Add variation to name if cycling
                name_suffix = (
                    f"_{i // len(judge_pool) + 1}" if i >= len(judge_pool) else ""
                )
                selected_judges.append(
                    (
                        profile[0] + name_suffix,
                        profile[1],
                        profile[2],
                        round(random.uniform(profile[3] - 0.1, profile[3] + 0.1), 1),
                    )
                )
        else:
            selected_judges = random.sample(judge_pool, num_judges)

        judges = [
            AIGameJudge(profile[0], profile[1], profile[2], profile[3])
            for profile in selected_judges
        ]

        return cls(judges)

    async def vote(
        self,
        topic: str,
        options: list[str],
        game_data: str,
        criteria: list[str],
        evaluator: GameEvaluator | None = None,
    ) -> VotingResult:
        """Conduct voting with all judges."""
        logger.info(f"🗳️ Conducting vote: '{topic}'")
        logger.info(f"📋 Options: {', '.join(options)}")
        logger.info(f"👨‍⚖️ Judges: {', '.join([j.name for j in self.judges])}")

        # Use evaluator if provided
        if evaluator:
            criteria = evaluator.get_evaluation_criteria()
            game_data = evaluator.format_game_data(game_data)
            context = evaluator.get_evaluation_context()
            game_data = f"{context}\n\n{game_data}"

        # Collect votes from all judges
        judge_votes = {}
        for judge in self.judges:
            logger.info(f"🔍 {judge.name} ({judge.personality.value}) evaluating...")

            vote = await judge.evaluate(topic, options, game_data, criteria)
            judge_votes[judge.name] = vote

        # Calculate results
        winner, margin, consensus = self._calculate_winner(judge_votes, options)
        summary = self._create_summary(
            topic, options, judge_votes, winner, margin, consensus
        )

        return VotingResult(
            topic=topic,
            options=options,
            judge_votes=judge_votes,
            winner=winner,
            margin=margin,
            consensus=consensus,
            summary=summary,
        )

    def _calculate_winner(
        self, judge_votes: dict[str, VoteChoice], options: list[str]
    ) -> tuple[str, float, float]:
        """Calculate winner, margin, and consensus from votes."""
        # Count votes for each option
        vote_counts = dict.fromkeys(options, 0)
        confidence_sums = dict.fromkeys(options, 0.0)

        for _judge_name, vote in judge_votes.items():
            if vote.choice in vote_counts:
                vote_counts[vote.choice] += 1
                confidence_sums[vote.choice] += vote.confidence

        # Determine winner (by vote count, then by confidence)
        winner = max(vote_counts.items(), key=lambda x: (x[1], confidence_sums[x[0]]))[
            0
        ]

        # Calculate margin (difference in votes / total possible)
        winner_votes = vote_counts[winner]
        total_votes = len(judge_votes)

        if total_votes > 1:
            second_place_votes = max(
                [count for option, count in vote_counts.items() if option != winner]
            )
            margin = (winner_votes - second_place_votes) / total_votes
        else:
            margin = 1.0

        # Calculate consensus (how confident judges were in winner)
        if winner_votes > 0:
            avg_confidence = confidence_sums[winner] / winner_votes
            consensus = avg_confidence
        else:
            consensus = 0.0

        return winner, margin, consensus

    def _create_summary(
        self,
        topic: str,
        options: list[str],
        judge_votes: dict[str, VoteChoice],
        winner: str,
        margin: float,
        consensus: float,
    ) -> str:
        """Create a summary of the voting results."""
        summary_parts = [
            "🗳️ **VOTING RESULTS** 🗳️",
            "",
            f"**Topic**: {topic}",
            f"**Options**: {', '.join(options)}",
            "",
            f"🏆 **WINNER**: {winner}",
            f"📊 **Margin**: {margin:.1%}",
            f"🤝 **Consensus**: {consensus:.1%}",
            "",
            "👨‍⚖️ **JUDGE VOTES**:",
        ]

        # Add individual judge votes
        for judge_name, vote in judge_votes.items():
            winner_mark = "👑" if vote.choice == winner else "  "
            summary_parts.append(
                f"  {winner_mark} {judge_name}: {vote.choice} (confidence: {
                    vote.confidence:.1%
                })"
            )

        # Add judge reasoning snippets
        summary_parts.extend(["", "💭 **KEY REASONING**:"])

        for judge_name, vote in judge_votes.items():
            reasoning_snippet = (
                vote.reasoning[:100] + "..."
                if len(vote.reasoning) > 100
                else vote.reasoning
            )
            summary_parts.append(f"  • {judge_name}: {reasoning_snippet}")

        return "\n".join(summary_parts)


# Game-specific evaluator implementations
class DebateEvaluator:
    """Evaluator for debate games."""

    def get_evaluation_criteria(self) -> list[str]:
        return [
            "logical_strength",
            "evidence_quality",
            "persuasiveness",
            "clarity",
            "consistency",
        ]

    def format_game_data(self, game_data: Any) -> str:
        if isinstance(game_data, str):
            return game_data
        # Format debate transcript, positions, etc.
        return str(game_data)

    def get_evaluation_context(self) -> str:
        return "This is a debate competition. Evaluate each participant's argumentative performance."


class ChessEvaluator:
    """Evaluator for chess games."""

    def get_evaluation_criteria(self) -> list[str]:
        return [
            "strategic_depth",
            "tactical_accuracy",
            "positional_understanding",
            "endgame_technique",
            "time_management",
        ]

    def format_game_data(self, game_data: Any) -> str:
        # Format chess moves, positions, analysis
        return str(game_data)

    def get_evaluation_context(self) -> str:
        return "This is a chess match. Evaluate each player's chess performance and skill level."


# Factory functions
def create_voting_system(
    game_type: str = "general", num_judges: int = 3
) -> GameVotingSystem:
    """Create appropriate voting system for game type.

    Args:
        game_type: Type of game ("general", "chess", "debate", "poker", "go")
        num_judges: Number of judges (default: 3 to avoid ties)
    """
    if game_type == "general":
        return GameVotingSystem.create_standard_judges(num_judges)
    return GameVotingSystem.create_game_specific_judges(game_type, num_judges)
