from __future__ import annotations

import uuid
from collections.abc import Callable, Iterable, Mapping, Sequence
from datetime import timedelta
from enum import Enum
from functools import cached_property
from typing import (
    Any,
    ClassVar,
    Dict,
    FrozenSet,
    Generic,
    List,
    Literal,
    Optional,
    Protocol,
    Set,
    Tuple,
    TypeVar,
    Union,
    cast,
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    computed_field,
    field_serializer,
    field_validator,
    model_validator,
)

# Type variables for generic relationships
A = TypeVar("A")  # Answer type
Q = TypeVar("Q", bound="Question")  # Question type
S = TypeVar("S", bound="Section")  # Section type

# ======================================================
# PROTOCOLS - Interfaces for components
# ======================================================


class AnswerableProtocol(Protocol, Generic[A]):
    """Protocol defining the required interface for answerable items."""

    id: str
    is_answered: bool

    def check_answer(self, provided_answer: A) -> bool: ...
    def clear_answer(self) -> None: ...
    def get_points(self) -> float: ...


class ScoringProtocol(Protocol):
    """Protocol for components that can be scored."""

    max_points: float

    def calculate_score(self) -> float: ...
    def get_completion_percentage(self) -> float: ...


# ======================================================
# QUESTION TYPES - Different types of test questions
# ======================================================


class QuestionType(str, Enum):
    """Types of questions available in tests."""

    MULTIPLE_CHOICE = "multiple_choice"
    TRUE_FALSE = "true_false"
    FREE_TEXT = "free_text"
    FILL_IN_BLANK = "fill_in_blank"
    MATCHING = "matching"
    NUMERIC = "numeric"
    ESSAY = "essay"
    CODE = "code"


class DifficultyLevel(str, Enum):
    """Difficulty levels for questions."""

    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    VERY_HARD = "very_hard"


class Question(BaseModel, Generic[A]):
    """Base class for all question types."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    text: str
    type: QuestionType
    points: float = 1.0
    time_limit: timedelta | None = None
    difficulty: DifficultyLevel = DifficultyLevel.MEDIUM
    tags: set[str] = Field(default_factory=set)
    explanation: str | None = None
    answer: A | None = None
    correct_answer: A

    model_config = ConfigDict(arbitrary_types_allowed=True, frozen=False)

    @computed_field
    @property
    def is_answered(self) -> bool:
        """Check if the question has been answered."""
        return self.answer is not None

    @field_validator("points")
    @classmethod
    def validate_points(cls, v: float) -> float:
        """Ensure points are positive."""
        if v < 0:
            raise ValueError("Points must be non-negative")
        return v

    @field_validator("time_limit")
    @classmethod
    def validate_time_limit(cls, v: timedelta | None) -> timedelta | None:
        """Ensure time limit is positive if set."""
        if v is not None and v.total_seconds() <= 0:
            raise ValueError("Time limit must be positive")
        return v

    def check_answer(self, provided_answer: A | None = None) -> bool:
        """Check if the provided answer is correct."""
        answer_to_check = (
            provided_answer if provided_answer is not None else self.answer
        )
        if answer_to_check is None:
            return False
        return self._is_correct(answer_to_check)

    def _is_correct(self, answer: A) -> bool:
        """Internal method to check correctness, overridden by subclasses."""
        return answer == self.correct_answer

    def clear_answer(self) -> None:
        """Clear the current answer."""
        self.answer = None

    def get_points(self) -> float:
        """Get the points earned for this question."""
        if not self.is_answered:
            return 0.0
        return self.points if self.check_answer() else 0.0


class MultipleChoiceQuestion(Question[str]):
    """A multiple choice question with one correct answer."""

    type: Literal[QuestionType.MULTIPLE_CHOICE] = QuestionType.MULTIPLE_CHOICE
    choices: list[str]
    correct_answer: str

    @model_validator(mode="after")
    def validate_choices(self) -> MultipleChoiceQuestion:
        """Validate that the correct answer is in the choices."""
        if self.correct_answer not in self.choices:
            raise ValueError("Correct answer must be one of the choices")
        return self

    @field_validator("answer")
    @classmethod
    def validate_answer(cls, v: str | None, info: Any) -> str | None:
        """Validate that the answer is in the choices."""
        if (
            v is not None
            and hasattr(info.data, "choices")
            and v not in info.data.choices
        ):
            raise ValueError("Answer must be one of the choices")
        return v


class TrueFalseQuestion(Question[bool]):
    """A true/false question."""

    type: Literal[QuestionType.TRUE_FALSE] = QuestionType.TRUE_FALSE
    correct_answer: bool


class FreeTextQuestion(Question[str]):
    """A free text question with text comparison."""

    type: Literal[QuestionType.FREE_TEXT] = QuestionType.FREE_TEXT
    correct_answer: str
    case_sensitive: bool = False

    def _is_correct(self, answer: str) -> bool:
        """Check if the answer matches the correct answer."""
        if self.case_sensitive:
            return answer == self.correct_answer
        return answer.lower() == self.correct_answer.lower()


class NumericQuestion(Question[float]):
    """A question with a numeric answer."""

    type: Literal[QuestionType.NUMERIC] = QuestionType.NUMERIC
    correct_answer: float
    tolerance: float = 0.0  # For floating-point comparison

    def _is_correct(self, answer: float) -> bool:
        """Check if the answer is within tolerance of the correct answer."""
        return abs(answer - self.correct_answer) <= self.tolerance


class MatchingQuestion(Question[dict[str, str]]):
    """A matching question where items must be paired correctly."""

    type: Literal[QuestionType.MATCHING] = QuestionType.MATCHING
    items: dict[str, str]  # key -> value pairs to match
    correct_answer: dict[str, str]

    @model_validator(mode="after")
    def validate_matching(self) -> MatchingQuestion:
        """Validate that the correct answer contains all items to match."""
        if set(self.correct_answer.keys()) != set(self.items.keys()):
            raise ValueError("Correct answer must contain all keys from items")
        return self

    def _is_correct(self, answer: dict[str, str]) -> bool:
        """Check if all matches are correct."""
        if set(answer.keys()) != set(self.correct_answer.keys()):
            return False
        return all(answer[k] == self.correct_answer[k] for k in answer)


class FillInBlankQuestion(Question[list[str]]):
    """A fill-in-the-blank question with multiple blanks."""

    type: Literal[QuestionType.FILL_IN_BLANK] = QuestionType.FILL_IN_BLANK
    correct_answer: list[str]
    blank_count: int
    case_sensitive: bool = False

    @model_validator(mode="after")
    def validate_blanks(self) -> FillInBlankQuestion:
        """Validate that the correct answer has the right number of blanks."""
        if len(self.correct_answer) != self.blank_count:
            raise ValueError("Number of answers must match number of blanks")
        return self

    def _is_correct(self, answer: list[str]) -> bool:
        """Check if all blanks are filled correctly."""
        if len(answer) != len(self.correct_answer):
            return False

        for i, ans in enumerate(answer):
            correct = self.correct_answer[i]
            if self.case_sensitive:
                if ans != correct:
                    return False
            elif ans.lower() != correct.lower():
                return False
        return True


# ======================================================
# SECTION - Grouping of related questions
# ======================================================


class Section(BaseModel, Generic[Q]):
    """A section of a test containing related questions."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    instructions: str | None = None
    questions: Sequence[Q] = Field(default_factory=list)
    time_limit: timedelta | None = None
    context: str | None = None  # Reading passage, code snippet, etc.

    @computed_field
    @property
    def question_count(self) -> int:
        """Get the number of questions in this section."""
        return len(self.questions)

    @computed_field
    @property
    def max_points(self) -> float:
        """Get the maximum possible points for this section."""
        return sum(q.points for q in self.questions)

    @computed_field
    @property
    def total_time(self) -> timedelta | None:
        """Get the total time limit for this section."""
        if self.time_limit is not None:
            return self.time_limit

        # If no section time limit, sum question time limits
        question_times = [
            q.time_limit for q in self.questions if q.time_limit is not None
        ]
        if not question_times:
            return None  # No time limits specified

        return sum(question_times, timedelta())

    def calculate_score(self) -> float:
        """Calculate the score for this section."""
        return sum(q.get_points() for q in self.questions)

    def get_completion_percentage(self) -> float:
        """Get the percentage of questions answered."""
        if not self.questions:
            return 0.0
        answered = sum(1 for q in self.questions if q.is_answered)
        return (answered / self.question_count) * 100

    def get_questions_by_type(self, question_type: QuestionType) -> list[Q]:
        """Get all questions of a specific type."""
        return [q for q in self.questions if q.type == question_type]

    def add_question(self, question: Q) -> None:
        """Add a question to this section."""
        if isinstance(self.questions, list):
            self.questions.append(question)
        else:
            # Convert to list if it's a different sequence type
            self.questions = list(self.questions) + [question]


# ======================================================
# TEST - Complete test with sections and settings
# ======================================================


class TestMode(str, Enum):
    """Test operation modes."""

    PRACTICE = "practice"
    GRADED = "graded"
    TIMED = "timed"
    ADAPTIVE = "adaptive"


class Test(BaseModel, Generic[S]):
    """A complete test composed of sections."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str | None = None
    sections: Sequence[S]
    time_limit: timedelta | None = None
    passing_score: float | None = None
    mode: TestMode = TestMode.GRADED
    randomize_questions: bool = False
    randomize_sections: bool = False
    show_answers: bool = False
    allow_navigation: bool = True

    @computed_field
    @property
    def question_count(self) -> int:
        """Get the total number of questions across all sections."""
        return sum(section.question_count for section in self.sections)

    @computed_field
    @property
    def max_points(self) -> float:
        """Get the maximum possible points for the entire test."""
        return sum(section.max_points for section in self.sections)

    @computed_field
    @property
    def total_time(self) -> timedelta | None:
        """Get the total time limit for the test."""
        if self.time_limit is not None:
            return self.time_limit

        # If no test time limit, sum section time limits
        section_times = [
            s.total_time for s in self.sections if s.total_time is not None
        ]
        if not section_times:
            return None  # No time limits specified

        return sum(section_times, timedelta())

    @computed_field
    @property
    def is_completed(self) -> bool:
        """Check if all questions have been answered."""
        return all(
            q.is_answered for section in self.sections for q in section.questions
        )

    def calculate_score(self) -> float:
        """Calculate the score for the entire test."""
        return sum(section.calculate_score() for section in self.sections)

    def get_completion_percentage(self) -> float:
        """Get the percentage of questions answered."""
        total_questions = self.question_count
        if total_questions == 0:
            return 0.0

        answered = sum(
            1 for section in self.sections for q in section.questions if q.is_answered
        )
        return (answered / total_questions) * 100

    def is_passing(self) -> bool:
        """Check if the current score meets the passing threshold."""
        if self.passing_score is None:
            return True  # No passing threshold set

        return self.calculate_score() >= self.passing_score

    def get_remaining_time(self, elapsed: timedelta) -> timedelta | None:
        """Calculate remaining time based on elapsed time."""
        if self.total_time is None:
            return None  # No time limit

        remaining = self.total_time - elapsed
        return max(remaining, timedelta())  # Don't return negative time

    def grade(self) -> dict[str, Any]:
        """Grade the test and return detailed results."""
        score = self.calculate_score()
        percentage = (score / self.max_points * 100) if self.max_points > 0 else 0

        return {
            "score": score,
            "max_points": self.max_points,
            "percentage": percentage,
            "passing_score": self.passing_score,
            "passed": self.is_passing(),
            "completion": self.get_completion_percentage(),
            "section_scores": [
                {
                    "section_id": section.id,
                    "title": section.title,
                    "score": section.calculate_score(),
                    "max_points": section.max_points,
                }
                for section in self.sections
            ],
        }


# ======================================================
# TEST SESSION - Tracking a test-taking instance
# ======================================================


class TestSessionStatus(str, Enum):
    """Status of a test session."""

    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    PAUSED = "paused"
    COMPLETED = "completed"
    TIMED_OUT = "timed_out"


class TestSession(BaseModel):
    """A session for taking a test, tracking state and progress."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    test_id: str
    user_id: str | None = None
    status: TestSessionStatus = TestSessionStatus.NOT_STARTED
    start_time: str | None = None
    end_time: str | None = None
    current_section_index: int = 0
    current_question_index: int = 0
    elapsed_time: timedelta = Field(default_factory=lambda: timedelta())
    answers: dict[str, Any] = Field(default_factory=dict)  # question_id -> answer

    def record_answer(self, question_id: str, answer: Any) -> None:
        """Record an answer for a question."""
        self.answers[question_id] = answer

    def navigate_to(self, section_index: int, question_index: int) -> bool:
        """Navigate to a specific question."""
        # Would validate indices against actual test structure
        self.current_section_index = section_index
        self.current_question_index = question_index
        return True

    def start(self) -> None:
        """Start the test session."""
        import datetime

        self.status = TestSessionStatus.IN_PROGRESS
        self.start_time = datetime.datetime.now().isoformat()

    def complete(self) -> None:
        """Complete the test session."""
        import datetime

        self.status = TestSessionStatus.COMPLETED
        self.end_time = datetime.datetime.now().isoformat()

    def timeout(self) -> None:
        """Mark the session as timed out."""
        import datetime

        self.status = TestSessionStatus.TIMED_OUT
        self.end_time = datetime.datetime.now().isoformat()
