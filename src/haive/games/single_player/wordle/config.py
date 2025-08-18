from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.games.framework.base import GameConfig
from haive.games.single_player.wordle.models import WordConnectionsState


class WordConnectionsGuess(BaseModel):
    """A guess in Word Connections."""

    words: list[str] = Field(..., description="Exactly 4 words that form a category")
    category: str = Field(..., description="What connects these 4 words")
    reasoning: str = Field(..., description="Why these words go together")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence 0-1")


def create_game_prompt() -> ChatPromptTemplate:
    """Create the main game playing prompt."""
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are playing Word Connections, where you must find groups of 4 words that share something in common.

RULES:
- Find 4 groups of 4 words each
- Each word belongs to exactly ONE group
- Groups have different difficulty levels (yellow=easiest, purple=hardest)

COMMON CATEGORY TYPES:
1. Direct categories (e.g., "Types of birds")
2. Word associations (e.g., "Words that go before CAKE")
3. Pop culture (e.g., "Marvel superheroes")
4. Wordplay (e.g., "Homophones of animals")

STRATEGY:
- Start with the most obvious connections
- Beware of words that SEEM to go together but don't (red herrings)
- If stuck, try different groupings
- Learn from incorrect guesses - they eliminate possibilities

PREVIOUS GAME EXAMPLES:
- "FINE PRINT": ASTERISK, CATCH, CONDITION, STRINGS
- "CHARACTERS WITH GREEN SKIN": ELPHABA, GRINCH, HULK, SHREK
- "THINGS THAT OPEN LIKE A CLAM": CLAM, COMPACT, LAPTOP, WAFFLE IRON
- "MOTHER ___": EARTH, GOOSE, MAY I, SUPERIOR""",
            ),
            (
                "human",
                """Current game state:.
{display_grid}

Previous incorrect guesses:
{incorrect_guesses}

Analyze the remaining words and find a group of 4 that share a specific connection. Be precise about what connects them.""",
            ),
        ]
    )


class WordConnectionsAgentConfig(GameConfig):
    """Configuration for Word Connections agent."""

    state_schema: type = Field(default=WordConnectionsState)

    game_engine: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            name="connections_player",
            id="connections_player_engine",
            llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.7),
            prompt_template=create_game_prompt(),
            structured_output_model=WordConnectionsGuess,
        )
    )

    visualize: bool = Field(default=True)
    puzzle_set: str = Field(default="nyt_recent", description="Which puzzle set to use")
