"""Example core module.

This module provides example functionality for the Haive framework.

Classes:
    WordConnectionsUI: WordConnectionsUI implementation.

Functions:
    display_grid: Display Grid functionality.
    display_solution: Display Solution functionality.
"""

#!/usr/bin/env python3
"""Example Word Connections game with interactive UI.

Uses the May 22, 2025 puzzle (#711).
"""

import asyncio

from haive.games.single_player.wordle.agent import WordConnectionsAgent
from haive.games.single_player.wordle.config import WordConnectionsAgentConfig
from haive.games.single_player.wordle.models import WordConnectionsState


class WordConnectionsUI:
    """Interactive UI for Word Connections game."""

    def __init__(self):
        self.config = WordConnectionsAgentConfig(visualize=True)
        self.agent = WordConnectionsAgent(self.config)
        self.state: WordConnectionsState | None = None

    def display_grid(self, state: WordConnectionsState):
        """Display the game grid in a nice format."""
        print("\n" + "=" * 60)
        print("🎮 WORD CONNECTIONS - Puzzle #711 (May 22, 2025)")
        print("=" * 60)

        remaining = state.remaining_words

        if not remaining:
            print("\n🎉 ALL CATEGORIES FOUND! 🎉\n")
        else:
            print("\nREMAINING WORDS:")
            print("-" * 60)

            # Display in 4x4 grid
            for i in range(0, len(remaining), 4):
                row = remaining[i : i + 4]
                # Pad if needed
                while len(row) < 4:
                    row.append("[SOLVED]")

                # Print row with nice spacing
                for word in row:
                    if word == "[SOLVED]":
                        print(f"{word:15}", end="")
                    else:
                        print(f"{word:15}", end="")
                print()  # New line after each row

        # Show found categories
        if state.found_categories:
            print("\n" + "-" * 60)
            print("FOUND CATEGORIES:")
            print("-" * 60)

            difficulty_order = ["yellow", "green", "blue", "purple"]
            emoji_map = {"yellow": "🟨", "green": "🟩", "blue": "🟦", "purple": "🟪"}

            # Sort by difficulty
            sorted_categories = sorted(
                state.found_categories.items(),
                key=lambda x: difficulty_order.index(
                    state.difficulty_map.get(x[0], "yellow")
                ),
            )

            for category, words in sorted_categories:
                difficulty = state.difficulty_map.get(category, "")
                emoji = emoji_map.get(difficulty, "")
                print(f"{emoji} {category.upper()}")
                print(f"   {', '.join(words)}")

        # Show mistakes
        print("\n" + "-" * 60)
        print(
            f"Mistakes Remaining: {'❌' * state.mistakes_remaining}{'⭕' * (4 - state.mistakes_remaining)}"
        )

        # Show incorrect guesses
        if state.incorrect_guesses:
            print("\nPrevious Incorrect Guesses:")
            for i, guess in enumerate(state.incorrect_guesses, 1):
                print(f"  {i}. {', '.join(guess)}")

    def display_solution(self, state: WordConnectionsState):
        """Display the full solution."""
        print("\n" + "=" * 60)
        print("COMPLETE SOLUTION:")
        print("=" * 60)

        difficulty_order = ["yellow", "green", "blue", "purple"]
        emoji_map = {"yellow": "🟨", "green": "🟩", "blue": "🟦", "purple": "🟪"}

        # Sort categories by difficulty
        sorted_cats = sorted(
            state.categories.items(),
            key=lambda x: difficulty_order.index(
                state.difficulty_map.get(x[0], "yellow")
            ),
        )

        for category, words in sorted_cats:
            difficulty = state.difficulty_map.get(category, "")
            emoji = emoji_map.get(difficulty, "")
            found = "✓" if category in state.found_categories else "✗"

            print(f"\n{emoji} {category.upper()} {found}")
            print(f"   {', '.join(words)}")

    async def play_game(self):
        """Play the game with AI assistance."""
        # Initialize with the May 22, 2025 puzzle
        self.state = self.agent.initialize_game(
            puzzle_data={
                "categories": {
                    "Fine print": ["ASTERISK", "CATCH", "CONDITION", "STRINGS"],
                    "Characters with green skin": [
                        "ELPHABA",
                        "GRINCH",
                        "HULK",
                        "SHREK",
                    ],
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
            }
        )

        print("\n" + "🎮" * 20)
        print("\n  WELCOME TO WORD CONNECTIONS!")
        print("\n  Find groups of 4 words that share something in common.")
        print("  You have 4 mistakes allowed.")
        print("\n" + "🎮" * 20)

        # Display initial state
        self.display_grid(self.state)

        # The agent's app property is the compiled graph
        # We invoke it directly
        result = await self.agent.graph.ainvoke(
            self.state.model_dump(), {"recursion_limit": 10}
        )

        # Display final results
        final_state = WordConnectionsState(**result)

        print("\n" + "=" * 60)
        if final_state.game_status == "won":
            print("🎉 CONGRATULATIONS! YOU SOLVED ALL CATEGORIES! 🎉")
        else:
            print("😔 GAME OVER - Better luck next time!")

        self.display_solution(final_state)

        print("\n" + "=" * 60)
        print(f"Final Score: {len(final_state.found_categories)}/4 categories found")
        print("=" * 60)


async def main():
    """Run the example game."""
    ui = WordConnectionsUI()
    await ui.play_game()


if __name__ == "__main__":
    # Run the async game
    asyncio.run(main())
