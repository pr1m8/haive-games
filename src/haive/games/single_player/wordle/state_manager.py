import random

from haive.games.framework.base import GameStateManager
from haive.games.single_player.wordle.models import (
    WordConnectionsMove,
    WordConnectionsState,
)


class WordConnectionsStateManager(GameStateManager[WordConnectionsState]):
    """Manager for Word Connections game state."""

    # Real NYT Connections puzzles from the data you provided
    NYT_PUZZLES = [
        {
            "date": "May 22, 2025",
            "number": 711,
            "categories": {
                "Fine print": ["ASTERISK", "CATCH", "CONDITION", "STRINGS"],
                "Characters with green skin": ["ELPHABA", "GRINCH", "HULK", "SHREK"],
                "Features of the National Mall in D.C.": [
                    "CAPITOL",
                    "MALL",
                    "OBELISK",
                    "POOL",
                ],
                "Famous riddle-givers": [
                    "BRIDGE TROLL",
                    "MAD HATTER",
                    "RIDDLER",
                    "SPHINX",
                ],
            },
            "difficulties": {
                "Fine print": "yellow",
                "Characters with green skin": "green",
                "Features of the National Mall in D.C.": "blue",
                "Famous riddle-givers": "purple",
            },
        },
        {
            "date": "May 21, 2025",
            "number": 710,
            "categories": {
                "Prohibit, as entry": ["BAR", "BLOCK", "DENY", "REFUSE"],
                "Folders on a Mac": ["DESKTOP", "MUSIC", "PICTURES", "TRASH"],
                "Medicine formats": ["CREAM", "PATCH", "SPRAY", "TABLET"],
                "Things that open like a clam": [
                    "CLAM",
                    "COMPACT",
                    "LAPTOP",
                    "WAFFLE IRON",
                ],
            },
            "difficulties": {
                "Prohibit, as entry": "yellow",
                "Folders on a Mac": "green",
                "Medicine formats": "blue",
                "Things that open like a clam": "purple",
            },
        },
        {
            "date": "May 20, 2025",
            "number": 709,
            "categories": {
                "Account book": ["LEDGER", "LOG", "RECORD", "REGISTER"],
                "Seen in a barn": ["BALE", "HORSE", "PITCHFORK", "TROUGH"],
                "Detectives of kid-lit": ["BROWN", "DREW", "HARDY", "HOLMES"],
                "Words before 'bed'": ["CANOPY", "DAY", "MURPHY", "WATER"],
            },
            "difficulties": {
                "Account book": "yellow",
                "Seen in a barn": "green",
                "Detectives of kid-lit": "blue",
                "Words before 'bed'": "purple",
            },
        },
        {
            "date": "May 18, 2025",
            "number": 707,
            "categories": {
                "Tasks for a student": ["ASSIGNMENT", "DRILL", "EXERCISE", "LESSON"],
                "Encouraging responses in a guessing game": [
                    "ALMOST",
                    "CLOSE",
                    "NOT QUITE",
                    "WARM",
                ],
                "Up for anything": ["EASY", "FLEXIBLE", "GAME", "OPEN"],
                "What 'A' might mean": ["AREA", "ATHLETIC", "EXCELLENT", "ONE"],
            },
            "difficulties": {
                "Tasks for a student": "yellow",
                "Encouraging responses in a guessing game": "green",
                "Up for anything": "blue",
                "What 'A' might mean": "purple",
            },
        },
        {
            "date": "May 11, 2025",
            "number": 700,
            "categories": {
                "Make happy": ["DELIGHT", "PLEASE", "SUIT", "TICKLE"],
                "Evade": ["DODGE", "DUCK", "SHAKE", "SKIRT"],
                "Common video game features": ["BOSS", "LEVEL", "HEALTH", "POWER-UP"],
                "Mother ___": ["EARTH", "GOOSE", "MAY I", "SUPERIOR"],
            },
            "difficulties": {
                "Make happy": "yellow",
                "Evade": "green",
                "Common video game features": "blue",
                "Mother ___": "purple",
            },
        },
    ]

    @classmethod
    def initialize(
        cls, puzzle_index: int | None = None, **kwargs
    ) -> WordConnectionsState:
        """Initialize a new Word Connections game.

        Args:
            puzzle_index: Optional index of puzzle to use (0 = most recent)
            **kwargs: Additional options

        Returns:
            Initialized game state
        """
        # Select puzzle
        if puzzle_index is not None and 0 <= puzzle_index < len(cls.NYT_PUZZLES):
            puzzle = cls.NYT_PUZZLES[puzzle_index]
        else:
            # Random puzzle
            puzzle = random.choice(cls.NYT_PUZZLES)

        # Create grid by shuffling all words
        all_words = []
        for words in puzzle["categories"].values():
            all_words.extend(words)
        random.shuffle(all_words)

        # Create initial state
        return WordConnectionsState(
            grid=all_words,
            categories=puzzle["categories"],
            difficulty_map=puzzle["difficulties"],
            found_categories={},
            incorrect_guesses=[],
            mistakes_remaining=4,
            game_status="playing",
        )

    @classmethod
    def apply_move(
        cls, state: WordConnectionsState, move: WordConnectionsMove
    ) -> WordConnectionsState:
        """Apply a move to the game state.

        Args:
            state: Current game state
            move: Move to apply

        Returns:
            Updated game state
        """
        # Create a copy of the state
        new_state = state.model_copy(deep=True)

        # Check if the game is still active
        if new_state.game_status != "playing":
            return new_state

        # Check if guess is correct
        guess_set = set(move.words)
        correct_category = None

        for category, words in new_state.categories.items():
            if set(words) == guess_set and category not in new_state.found_categories:
                correct_category = category
                break

        if correct_category:
            # Correct guess!
            new_state.found_categories[correct_category] = move.words

            # Check if won
            if len(new_state.found_categories) == 4:
                new_state.game_status = "won"
        else:
            # Incorrect guess
            new_state.incorrect_guesses.append(move.words)
            new_state.mistakes_remaining -= 1

            # Check if lost
            if new_state.mistakes_remaining == 0:
                new_state.game_status = "lost"

        return new_state

    @classmethod
    def check_game_status(cls, state: WordConnectionsState) -> WordConnectionsState:
        """Check and update game status.

        Args:
            state: Current game state

        Returns:
            Updated game state
        """
        # Already handled in apply_move
        return state

    @classmethod
    def get_hint(cls, state: WordConnectionsState) -> str:
        """Get a hint for the current state.

        Args:
            state: Current game state

        Returns:
            Hint string
        """
        # Find easiest unsolved category
        for difficulty in ["yellow", "green", "blue", "purple"]:
            for category, diff in state.difficulty_map.items():
                if diff == difficulty and category not in state.found_categories:
                    # Give a vague hint about this category
                    if difficulty == "yellow":
                        return "Look for the most straightforward connection among the remaining words."
                    if difficulty == "green":
                        return "Try finding a moderately obvious grouping."
                    if difficulty == "blue":
                        return "Consider less obvious connections or wordplay."
                    return "Think about obscure connections, puns, or very specific references."

        return "No hints available."
