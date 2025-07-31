# src/haive/games/debate/models.py
"""Pydantic models for debate game components.

This module defines the core data models used in the debate game implementation,
including statements, participants, topics, votes, and debate phases. All models
use Pydantic for validation and serialization with comprehensive field documentation.

The models support various debate formats including parliamentary, Oxford-style,
and Lincoln-Douglas debates with proper type safety and validation.

Examples:
    Creating a debate statement::

        statement = Statement(
            content="I believe AI regulation is essential for safety",
            speaker_id="participant_1",
            statement_type="opening",
            timestamp="2024-01-08T15:30:00Z"
        )

    Setting up a debate topic::

        topic = Topic(
            title="AI Should Be Regulated by Government",
            description="Debate whether artificial intelligence development should be subject to government oversight",
            keywords=["artificial intelligence", "regulation", "government oversight"]
        )

    Creating a participant::

        participant = Participant(
            id="debater_1",
            name="Dr. Smith",
            role="debater",
            position="pro",
            expertise=["AI ethics", "technology policy"]
        )
"""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, field_validator


class Statement(BaseModel):
    """Represents a single statement in a debate or discussion.

    A statement is the fundamental unit of discourse in a debate, containing
    the speaker's argument, position, or response. Each statement includes
    metadata for tracking, analysis, and proper debate flow management.

    This model supports various statement types including opening statements,
    rebuttals, questions, and closing arguments. It also tracks references,
    sentiment analysis, and targeting for structured debate formats.

    Attributes:
        content (str): The actual text content of the statement.
        speaker_id (str): Unique identifier of the participant making the statement.
        target_id (Optional[str]): ID of targeted participant for directed statements.
        statement_type (str): Category of statement for debate flow management.
        references (List[str]): Citations, sources, or evidence supporting the statement.
        sentiment (Optional[float]): Sentiment analysis score if available.
        timestamp (str): ISO format timestamp when the statement was made.

    Examples:
        Creating an opening statement::

            opening = Statement(
                content="Government regulation of AI is necessary to prevent harmful outcomes",
                speaker_id="pro_debater_1",
                statement_type="opening",
                references=["AI Safety Research Paper 2024"],
                timestamp="2024-01-08T15:30:00Z"
            )

        Creating a rebuttal with targeting::

            rebuttal = Statement(
                content="The previous speaker's concerns about innovation are unfounded",
                speaker_id="con_debater_1",
                target_id="pro_debater_1",
                statement_type="rebuttal",
                timestamp="2024-01-08T15:35:00Z"
            )

        Creating a question::

            question = Statement(
                content="Can you provide specific examples of AI harm that regulation would prevent?",
                speaker_id="moderator",
                target_id="pro_debater_1",
                statement_type="question",
                timestamp="2024-01-08T15:40:00Z"
            )

    Note:
        Statement types should follow debate format conventions. Common types
        include: "opening", "rebuttal", "question", "answer", "closing",
        "point_of_information", "point_of_order".
    """

    content: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="The text content of the statement (1-5000 characters)",
        examples=[
            "I believe that artificial intelligence regulation is essential for public safety",
            "The opposition's argument fails to consider the economic implications",
            "Can you provide evidence to support that claim?",
        ],
    )

    speaker_id: str = Field(
        ...,
        min_length=1,
        description="Unique identifier of the participant making the statement",
        examples=["pro_debater_1", "con_debater_2", "moderator", "judge_1"],
    )

    target_id: str | None = Field(
        None,
        description="ID of targeted participant for directed statements or questions",
        examples=["pro_debater_1", "con_debater_2", None],
    )

    statement_type: str = Field(
        "general",
        description="Type/category of statement for debate flow management",
        examples=[
            "opening",
            "rebuttal",
            "question",
            "answer",
            "closing",
            "point_of_information",
            "point_of_order",
            "general",
        ],
    )

    references: list[str] = Field(
        default_factory=list,
        description="Citations, sources, or evidence supporting the statement",
        examples=[
            ["AI Safety Research 2024", "https://example.com/study"],
            ["Economic Impact Report"],
            [],
        ],
    )

    sentiment: float | None = Field(
        None,
        ge=-1.0,
        le=1.0,
        description="Sentiment analysis score from -1.0 (negative) to 1.0 (positive)",
        examples=[0.7, -0.3, 0.0, None],
    )

    timestamp: str = Field(
        ...,
        description="ISO format timestamp when the statement was made",
        examples=["2024-01-08T15:30:00Z", "2024-01-08T15:35:45.123Z"],
    )

    @field_validator("content")
    @classmethod
    def validate_content(cls, v: str) -> str:
        """Validate statement content is not empty and properly formatted.

        Args:
            v (str): Content to validate.

        Returns:
            str: Cleaned and validated content.

        Raises:
            ValueError: If content is empty or contains only whitespace.
        """
        content = v.strip()
        if not content:
            raise ValueError("Statement content cannot be empty")
        return content

    @field_validator("timestamp")
    @classmethod
    def validate_timestamp(cls, v: str) -> str:
        """Validate timestamp is in proper ISO format.

        Args:
            v (str): Timestamp string to validate.

        Returns:
            str: Validated timestamp string.

        Raises:
            ValueError: If timestamp format is invalid.
        """
        try:
            datetime.fromisoformat(v.replace("Z", "+00:00"))
        except ValueError:
            raise ValueError(
                "Timestamp must be in ISO format (e.g., '2024-01-08T15:30:00Z')"
            )
        return v


class Topic(BaseModel):
    """Represents a debate topic or resolution.

    A topic defines the subject matter for a debate, including the resolution
    to be argued, background context, and any constraints or guidelines for
    the discussion. Topics can range from simple yes/no propositions to
    complex policy discussions.

    This model supports various debate formats by allowing flexible topic
    definition with keywords for research and constraints for format-specific
    rules or limitations.

    Attributes:
        title (str): The main resolution or question being debated.
        description (str): Detailed background and context for the topic.
        keywords (List[str]): Key terms for research and fact-checking.
        constraints (Optional[Dict[str, str]]): Format-specific rules or limitations.

    Examples:
        Simple policy topic::

            topic = Topic(
                title="This House Believes That Social Media Does More Harm Than Good",
                description="Debate the overall impact of social media platforms on society, considering both benefits and drawbacks",
                keywords=["social media", "mental health", "democracy", "privacy"],
                constraints={"time_limit": "8 minutes per speaker", "format": "Oxford"}
            )

        Technical topic with research areas::

            topic = Topic(
                title="AI Development Should Prioritize Safety Over Speed",
                description="Consider whether artificial intelligence research should emphasize safety measures even if it slows development",
                keywords=["AI safety", "research ethics", "technological progress", "risk assessment"],
                constraints={
                    "evidence_required": "true",
                    "fact_checking": "enabled",
                    "research_time": "30 minutes"
                }
            )

        Philosophical topic::

            topic = Topic(
                title="Justice Ought to Take Precedence Over Security",
                description="A philosophical examination of the tension between individual rights and collective safety",
                keywords=["justice", "security", "individual rights", "social contract"],
                constraints={"format": "Lincoln-Douglas", "framework_required": "true"}
            )

    Note:
        Topic titles should be clear, debatable propositions. For formal debates,
        use standard resolution formats like "This House Believes..." or
        "Resolved: ..." depending on the debate format.
    """

    title: str = Field(
        ...,
        min_length=5,
        max_length=200,
        description="The main resolution, proposition, or question being debated",
        examples=[
            "This House Believes That AI Should Be Regulated by Government",
            "Resolved: Climate Action Should Prioritize Economic Growth",
            "Should Universal Basic Income Be Implemented?",
        ],
    )

    description: str = Field(
        ...,
        min_length=10,
        max_length=2000,
        description="Detailed background, context, and scope of the debate topic",
        examples=[
            "This debate examines whether government regulation of AI development is necessary to prevent harmful outcomes while considering innovation and economic impacts.",
            "Explore the balance between environmental protection and economic considerations in climate policy, examining trade-offs and potential solutions.",
        ],
    )

    keywords: list[str] = Field(
        default_factory=list,
        description="Key terms, concepts, and research areas related to the topic",
        examples=[
            [
                "artificial intelligence",
                "regulation",
                "government oversight",
                "innovation",
            ],
            ["climate change", "economic policy", "environmental protection"],
            ["social media", "mental health", "privacy", "democracy"],
        ],
    )

    constraints: dict[str, str] | None = Field(
        None,
        description="Format-specific rules, time limits, or debate constraints",
        examples=[
            {
                "time_limit": "8 minutes",
                "format": "parliamentary",
                "interruptions": "allowed",
            },
            {"evidence_required": "true", "fact_checking": "enabled"},
            {"format": "Lincoln-Douglas", "framework_required": "true"},
        ],
    )

    @field_validator("title")
    @classmethod
    def validate_title(cls, v: str) -> str:
        """Validate topic title is properly formatted.

        Args:
            v (str): Title to validate.

        Returns:
            str: Cleaned and validated title.

        Raises:
            ValueError: If title is too short or improperly formatted.
        """
        title = v.strip()
        if len(title) < 5:
            raise ValueError("Topic title must be at least 5 characters")
        return title

    @field_validator("keywords")
    @classmethod
    def validate_keywords(cls, v: list[str]) -> list[str]:
        """Validate and clean keyword list.

        Args:
            v (List[str]): Keywords to validate.

        Returns:
            List[str]: Cleaned list of non-empty keywords.
        """
        return [kw.strip().lower() for kw in v if kw.strip()]


class Participant(BaseModel):
    """Represents a participant in the debate.

    A participant can be a debater, judge, moderator, or audience member with
    specific roles, expertise, and characteristics that influence their
    contribution to the debate. This model supports AI-powered participants
    with configurable personalities and human participants with tracked metadata.

    Participants can have positions (pro/con/neutral), expertise areas that
    inform their arguments, and personality traits that influence their
    debating style and decision-making patterns.

    Attributes:
        id (str): Unique identifier for the participant.
        name (str): Display name shown in the debate interface.
        role (str): Function in the debate (debater, judge, moderator, audience).
        position (Optional[str]): Stance on the topic (pro, con, neutral).
        persona (Optional[Dict[str, str]]): Personality traits and characteristics.
        expertise (List[str]): Subject matter expertise areas.
        bias (Optional[float]): Inherent bias level for realistic modeling.

    Examples:
        Creating a pro debater::

            debater = Participant(
                id="pro_debater_1",
                name="Dr. Sarah Chen",
                role="debater",
                position="pro",
                persona={
                    "style": "analytical",
                    "approach": "evidence-based",
                    "temperament": "calm"
                },
                expertise=["artificial intelligence", "technology policy", "ethics"],
                bias=0.2
            )

        Creating a neutral moderator::

            moderator = Participant(
                id="moderator_1",
                name="Judge Williams",
                role="moderator",
                position="neutral",
                persona={
                    "style": "formal",
                    "approach": "procedural",
                    "fairness": "strict"
                },
                expertise=["debate procedures", "parliamentary law"]
            )

        Creating a specialized judge::

            judge = Participant(
                id="judge_1",
                name="Prof. Martinez",
                role="judge",
                position="neutral",
                expertise=["economics", "public policy", "data analysis"],
                bias=-0.1
            )

    Note:
        Bias values range from -1.0 (strongly biased toward con position)
        to +1.0 (strongly biased toward pro position), with 0.0 being
        perfectly neutral. Small bias values (±0.1 to ±0.3) create
        realistic human-like tendencies without compromising debate quality.
    """

    id: str = Field(
        ...,
        min_length=1,
        description="Unique identifier for the participant across all debates",
        examples=[
            "pro_debater_1",
            "con_debater_2",
            "moderator",
            "judge_1",
            "audience_member_5",
        ],
    )

    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Display name shown in the debate interface and transcripts",
        examples=[
            "Dr. Sarah Chen",
            "Judge Williams",
            "Prof. Martinez",
            "Alex Thompson",
        ],
    )

    role: str = Field(
        ...,
        description="Primary function in the debate structure and flow",
        examples=[
            "debater",
            "judge",
            "moderator",
            "audience",
            "timekeeper",
            "fact_checker",
        ],
    )

    position: str | None = Field(
        None,
        description="Stance on the debate topic (pro supports, con opposes, neutral abstains)",
        examples=["pro", "con", "neutral", None],
    )

    persona: dict[str, str] | None = Field(
        None,
        description="Personality traits, debating style, and behavioral characteristics",
        examples=[
            {
                "style": "analytical",
                "approach": "evidence-based",
                "temperament": "calm",
            },
            {
                "style": "passionate",
                "approach": "rhetorical",
                "temperament": "energetic",
            },
            {"style": "formal", "approach": "procedural", "fairness": "strict"},
        ],
    )

    expertise: list[str] = Field(
        default_factory=list,
        description="Subject matter areas where participant has knowledge or credentials",
        examples=[
            ["artificial intelligence", "technology policy", "ethics"],
            ["economics", "public policy", "statistics"],
            ["debate procedures", "parliamentary law", "rhetoric"],
        ],
    )

    bias: float | None = Field(
        None,
        ge=-1.0,
        le=1.0,
        description="Inherent bias level: -1.0 (strongly con) to +1.0 (strongly pro), 0.0 neutral",
        examples=[0.2, -0.1, 0.0, None],
    )

    @field_validator("role")
    @classmethod
    def validate_role(cls, v: str) -> str:
        """Validate participant role is recognized.

        Args:
            v (str): Role to validate.

        Returns:
            str: Validated role string.

        Raises:
            ValueError: If role is not supported.
        """
        valid_roles = {
            "debater",
            "judge",
            "moderator",
            "audience",
            "timekeeper",
            "fact_checker",
        }
        role = v.strip().lower()
        if role not in valid_roles:
            raise ValueError(f"Role must be one of: {', '.join(valid_roles)}")
        return role

    @field_validator("position")
    @classmethod
    def validate_position(cls, v: str | None) -> str | None:
        """Validate debate position if provided.

        Args:
            v (Optional[str]): Position to validate.

        Returns:
            Optional[str]: Validated position or None.

        Raises:
            ValueError: If position is not valid.
        """
        if v is None:
            return None

        valid_positions = {"pro", "con", "neutral"}
        position = v.strip().lower()
        if position not in valid_positions:
            raise ValueError(f"Position must be one of: {', '.join(valid_positions)}")
        return position


class Vote(BaseModel):
    """Represents a vote or evaluation from a participant.

    Votes are used for various purposes in debates including final judgments,
    audience polling, quality ratings, and procedural decisions. The flexible
    vote_value field supports different voting systems (binary, numeric, ranked).

    Votes can target specific participants (for best speaker awards), statements
    (for argument quality), or the overall debate topic (for winner determination).
    The reasoning field provides transparency and educational value.

    Attributes:
        voter_id (str): Unique identifier of the participant casting the vote.
        vote_value (Union[str, int, float]): The actual vote (yes/no, 1-10, ranking).
        target_id (Optional[str]): What/who is being voted on (participant, statement, topic).
        reason (Optional[str]): Explanation or justification for the vote.

    Examples:
        Binary topic vote::

            topic_vote = Vote(
                voter_id="judge_1",
                vote_value="pro",
                target_id="main_topic",
                reason="The pro side provided more compelling evidence and stronger logical arguments"
            )

        Numeric quality rating::

            quality_vote = Vote(
                voter_id="audience_member_3",
                vote_value=8.5,
                target_id="statement_15",
                reason="Excellent use of data and clear reasoning, but could have addressed counterarguments"
            )

        Best speaker vote::

            speaker_vote = Vote(
                voter_id="judge_2",
                vote_value="winner",
                target_id="pro_debater_1",
                reason="Outstanding rhetorical skills and effective rebuttal strategy"
            )

        Procedural vote::

            procedural_vote = Vote(
                voter_id="moderator",
                vote_value="approve",
                target_id="time_extension_request",
                reason="Complex topic warrants additional time for thorough discussion"
            )

    Note:
        Vote values should be consistent within each voting context. Use
        strings for categorical votes ("pro", "con", "abstain"), numbers
        for ratings (1-10 scales), and structured data for ranked choices.
    """

    voter_id: str = Field(
        ...,
        min_length=1,
        description="Unique identifier of the participant casting the vote",
        examples=["judge_1", "audience_member_3", "moderator", "pro_debater_1"],
    )

    vote_value: str | int | float = Field(
        ...,
        description="The actual vote value: binary (yes/no), categorical (pro/con), or numeric (1-10)",
        examples=["pro", "con", "abstain", "yes", "no", 1, 2, 5, 8, 10, 7.5, 8.2, 9.1],
    )

    target_id: str | None = Field(
        None,
        description="Identifier of what/who is being voted on (topic, participant, statement)",
        examples=[
            "main_topic",
            "pro_debater_1",
            "statement_15",
            "time_extension_request",
            None,
        ],
    )

    reason: str | None = Field(
        None,
        max_length=1000,
        description="Explanation, justification, or commentary supporting the vote decision",
        examples=[
            "Strong evidence and logical reasoning throughout the debate",
            "Excellent rhetorical skills but weak factual support",
            "The argument was compelling but failed to address key counterpoints",
            None,
        ],
    )

    @field_validator("vote_value")
    @classmethod
    def validate_vote_value(cls, v: str | int | float) -> str | int | float:
        """Validate vote value is reasonable.

        Args:
            v (Union[str, int, float]): Vote value to validate.

        Returns:
            Union[str, int, float]: Validated vote value.

        Raises:
            ValueError: If vote value is invalid.
        """
        if isinstance(v, str):
            return v.strip().lower()
        elif isinstance(v, (int, float)):
            if not -100 <= v <= 100:  # Reasonable numeric range
                raise ValueError("Numeric votes should be between -100 and 100")
            return v
        else:
            raise ValueError("Vote value must be string, int, or float")


class DebatePhase(str, Enum):
    """Enumeration of debate phases for structured discussion flow.

    These phases represent the standard progression of formal debates,
    providing structure and ensuring all participants have appropriate
    opportunities to present arguments, respond to opponents, and reach
    conclusions. Different debate formats may use subsets of these phases.

    The phases are designed to support various debate formats including
    parliamentary, Oxford-style, Lincoln-Douglas, and custom formats
    while maintaining logical flow and fairness.

    Attributes:
        SETUP: Initial preparation and rule establishment.
        OPENING_STATEMENTS: Initial position presentations.
        DISCUSSION: Open floor discussion and argument development.
        REBUTTAL: Direct responses to opposing arguments.
        QUESTIONS: Cross-examination and clarification phase.
        CLOSING_STATEMENTS: Final position summaries.
        VOTING: Decision-making and evaluation phase.
        JUDGMENT: Official results and analysis.
        CONCLUSION: Final wrap-up and documentation.

    Examples:
        Parliamentary debate flow::

            phases = [
                DebatePhase.SETUP,
                DebatePhase.OPENING_STATEMENTS,
                DebatePhase.REBUTTAL,
                DebatePhase.CLOSING_STATEMENTS,
                DebatePhase.JUDGMENT
            ]

        Oxford-style debate::

            phases = [
                DebatePhase.SETUP,
                DebatePhase.OPENING_STATEMENTS,
                DebatePhase.DISCUSSION,
                DebatePhase.QUESTIONS,
                DebatePhase.CLOSING_STATEMENTS,
                DebatePhase.VOTING,
                DebatePhase.CONCLUSION
            ]

        Lincoln-Douglas format::

            phases = [
                DebatePhase.SETUP,
                DebatePhase.OPENING_STATEMENTS,
                DebatePhase.QUESTIONS,  # Cross-examination
                DebatePhase.REBUTTAL,
                DebatePhase.CLOSING_STATEMENTS,
                DebatePhase.JUDGMENT
            ]

    Note:
        Phase transitions should be managed by the debate agent to ensure
        proper timing and participant readiness. Some phases may be repeated
        (e.g., multiple rebuttal rounds) or skipped based on debate format.
    """

    SETUP = "setup"  #: Initial preparation, rule establishment, and participant introduction
    OPENING_STATEMENTS = (
        "opening_statements"  #: Initial position presentations from each side
    )
    DISCUSSION = "discussion"  #: Open floor discussion and argument development
    REBUTTAL = (
        "rebuttal"  #: Direct responses and counter-arguments to opposing positions
    )
    QUESTIONS = "questions"  #: Cross-examination, clarification, and probing questions
    CLOSING_STATEMENTS = (
        "closing_statements"  #: Final position summaries and persuasive appeals
    )
    VOTING = "voting"  #: Decision-making phase where judges or audience cast votes
    JUDGMENT = "judgment"  #: Official results announcement and winner determination
    CONCLUSION = "conclusion"  #: Final wrap-up, analysis, and documentation

    @classmethod
    def get_parliamentary_flow(cls) -> list["DebatePhase"]:
        """Get standard parliamentary debate phase sequence.

        Returns:
            List[DebatePhase]: Ordered phases for parliamentary format.
        """
        return [
            cls.SETUP,
            cls.OPENING_STATEMENTS,
            cls.REBUTTAL,
            cls.CLOSING_STATEMENTS,
            cls.JUDGMENT,
        ]

    @classmethod
    def get_oxford_flow(cls) -> list["DebatePhase"]:
        """Get standard Oxford-style debate phase sequence.

        Returns:
            List[DebatePhase]: Ordered phases for Oxford format.
        """
        return [
            cls.SETUP,
            cls.OPENING_STATEMENTS,
            cls.DISCUSSION,
            cls.QUESTIONS,
            cls.CLOSING_STATEMENTS,
            cls.VOTING,
            cls.CONCLUSION,
        ]

    @classmethod
    def get_lincoln_douglas_flow(cls) -> list["DebatePhase"]:
        """Get standard Lincoln-Douglas debate phase sequence.

        Returns:
            List[DebatePhase]: Ordered phases for Lincoln-Douglas format.
        """
        return [
            cls.SETUP,
            cls.OPENING_STATEMENTS,
            cls.QUESTIONS,
            cls.REBUTTAL,
            cls.CLOSING_STATEMENTS,
            cls.JUDGMENT,
        ]


# Additional model for comprehensive debate analysis
class DebateAnalysis(BaseModel):
    """Comprehensive analysis of debate performance and quality.

    This model provides structured evaluation of debate participants,
    arguments, and overall debate quality. It supports both automated
    AI analysis and human judge evaluations with detailed scoring
    and qualitative feedback.

    Attributes:
        participant_scores (Dict[str, float]): Individual performance scores.
        argument_quality (float): Overall argument quality assessment.
        engagement_level (float): Participant engagement and interaction.
        factual_accuracy (float): Accuracy of claims and evidence.
        rhetorical_effectiveness (float): Persuasive power and delivery.
        winner (Optional[str]): Determined winner if applicable.
        key_arguments (List[str]): Most significant arguments presented.
        strengths (List[str]): Notable strengths in the debate.
        weaknesses (List[str]): Areas needing improvement.
        recommendations (List[str]): Suggestions for future debates.
    """

    participant_scores: dict[str, float] = Field(
        default_factory=dict,
        description="Individual performance scores by participant ID (0.0-10.0)",
        examples=[{"pro_debater_1": 8.5, "con_debater_1": 7.2, "moderator": 9.0}],
    )

    argument_quality: float = Field(
        0.0,
        ge=0.0,
        le=10.0,
        description="Overall quality of arguments presented (0.0-10.0)",
        examples=[7.5, 8.2, 6.8],
    )

    engagement_level: float = Field(
        0.0,
        ge=0.0,
        le=10.0,
        description="Level of participant engagement and interaction (0.0-10.0)",
        examples=[8.0, 7.3, 9.1],
    )

    factual_accuracy: float = Field(
        0.0,
        ge=0.0,
        le=10.0,
        description="Accuracy of factual claims and evidence presented (0.0-10.0)",
        examples=[6.5, 8.8, 7.0],
    )

    rhetorical_effectiveness: float = Field(
        0.0,
        ge=0.0,
        le=10.0,
        description="Persuasive power and rhetorical skill demonstrated (0.0-10.0)",
        examples=[7.8, 8.5, 6.2],
    )

    winner: str | None = Field(
        None,
        description="Determined winner of the debate (participant ID or side)",
        examples=["pro_debater_1", "con_side", "draw", None],
    )

    key_arguments: list[str] = Field(
        default_factory=list,
        description="Most significant or impactful arguments presented",
        examples=[
            [
                "Economic benefits outweigh regulatory costs",
                "Safety concerns require immediate action",
            ],
            [
                "Historical precedent supports this approach",
                "Alternative solutions are more effective",
            ],
        ],
    )

    strengths: list[str] = Field(
        default_factory=list,
        description="Notable strengths demonstrated in the debate",
        examples=[
            [
                "Excellent use of evidence",
                "Strong logical reasoning",
                "Effective rebuttals",
            ],
            [
                "Good engagement with opponents",
                "Clear communication",
                "Well-structured arguments",
            ],
        ],
    )

    weaknesses: list[str] = Field(
        default_factory=list,
        description="Areas needing improvement or weaknesses observed",
        examples=[
            ["Limited evidence diversity", "Weak response to counterarguments"],
            ["Time management issues", "Insufficient fact-checking"],
        ],
    )

    recommendations: list[str] = Field(
        default_factory=list,
        description="Suggestions for improvement in future debates",
        examples=[
            ["Prepare more diverse evidence sources", "Practice rebuttal techniques"],
            ["Improve time allocation", "Enhance fact-checking procedures"],
        ],
    )
