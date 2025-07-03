"""Test script for Word Connections game with custom words.

This script creates a custom Word Connections game with user-provided words
organized into thematic categories.
"""

from haive.games.single_player.wordle.agent import WordConnectionsAgent
from haive.games.single_player.wordle.config import WordConnectionsAgentConfig
from haive.games.single_player.wordle.state_manager import WordConnectionsStateManager


def create_custom_word_connections_game():
    """Create a Word Connections game with custom categories."""
    # Custom categories using the user's exact words (with typos corrected)
    # walker jet stroller jogger net hooks ranger monitor butler met bottle slack gay capri jean bib
    custom_categories = {
        "Baby/Child Items": ["WALKER", "STROLLER", "BOTTLE", "BIB"],
        "Clothing/Pants": [
            "JEAN",
            "CAPRI",
            "SLACK",
            "GAY",
        ],  # Gay can mean colorful/bright clothing
        "People/Occupations": [
            "RANGER",
            "BUTLER",
            "JOGGER",
            "MONITOR",
        ],  # Monitor as person who watches
        "Things That Connect": [
            "HOOKS",
            "NET",
            "JET",
            "MET",
        ],  # Hooks connect, Net connects, Jet stream, Met (meeting point)
    }

    # Temporarily add our custom categories to the ALL_CATEGORIES
    original_categories = WordConnectionsStateManager.ALL_CATEGORIES.copy()

    # Add our custom categories
    WordConnectionsStateManager.ALL_CATEGORIES.update(custom_categories)

    try:
        # Now use the state manager with our specific categories
        categories_list = list(custom_categories.keys())
        state = WordConnectionsStateManager.initialize(
            source="internal", categories=categories_list
        )

        return state

    finally:
        # Restore the original categories dictionary
        WordConnectionsStateManager.ALL_CATEGORIES = original_categories


def run_custom_word_connections_test():
    """Run the custom Word Connections game test."""
    print("🎮 Starting Custom Word Connections Game Test")
    print("=" * 60)
    print("Custom Categories:")

    # Create the custom game state using our fixed method
    try:
        game_state = create_custom_word_connections_game()

        # Display the categories (for testing purposes)
        for category, words in game_state.categories.items():
            difficulty = game_state.category_difficulty.get(category, "")
            color_emoji = {
                "yellow": "🟨",
                "green": "🟩",
                "blue": "🟦",
                "purple": "🟪",
            }.get(difficulty, "")
            print(f"{color_emoji} {category} ({difficulty}): {', '.join(words)}")

        print("=" * 60)

        # Create agent configuration
        config = WordConnectionsAgentConfig(
            enable_analysis=True, visualize=True, auto_submit=False, source="internal"
        )

        # Create the agent
        agent = WordConnectionsAgent(config)

        # Display the initial board
        print("\n" + game_state.board_string)

        print("\n🎯 Game Ready!")
        print("Words have been shuffled randomly on the board.")
        print("Try to find the 4 categories of 4 words each!")

        return game_state, agent

    except Exception as e:
        print(f"❌ Error creating game: {e}")
        import traceback

        traceback.print_exc()
        return None, None


def run_interactive_custom_game():
    """Run an interactive version of the custom game."""
    game_state, agent = run_custom_word_connections_test()

    # Check if game creation was successful
    if game_state is None or agent is None:
        print("❌ Failed to create game. Exiting.")
        return

    print("\n" + "=" * 60)
    print("🎮 Interactive Custom Word Connections Game")
    print("Commands:")
    print("- Enter numbers 0-15 to select/deselect cells")
    print("- Type 'submit' to submit your selection")
    print("- Type 'analyze' to get AI analysis")
    print("- Type 'auto' to let AI make a move")
    print("- Type 'hint' to see the categories")
    print("- Type 'quit' to exit")
    print("=" * 60)

    # Main game loop
    while game_state.game_status == "ongoing":
        print(f"\n📊 Status: {len(game_state.discovered_groups)}/4 categories found")
        print(f"🎯 Attempts remaining: {game_state.attempts_remaining}")
        print("\n" + game_state.board_string)

        # Get user input
        command = input("\nEnter command: ").strip().lower()

        if command == "quit":
            print("👋 Exiting game...")
            break
        if command == "hint":
            print("\n💡 Categories in this game:")
            for category, words in game_state.categories.items():
                difficulty = game_state.category_difficulty.get(category, "")
                color_emoji = {
                    "yellow": "🟨",
                    "green": "🟩",
                    "blue": "🟦",
                    "purple": "🟪",
                }.get(difficulty, "")
                print(f"{color_emoji} {category}: {', '.join(words)}")
        elif command == "submit":
            if len(game_state.selected_indices) == 4:
                selected_words = [
                    game_state.cells[i].word for i in game_state.selected_indices
                ]

                # Create a move
                from haive.games.single_player.wordle.models import WordConnectionsMove

                move = WordConnectionsMove(
                    words=selected_words, indices=game_state.selected_indices.copy()
                )

                # Apply the move
                game_state = WordConnectionsStateManager.apply_move(game_state, move)

                if move.result == "correct":
                    print("🎉 Correct! You found a category!")
                else:
                    print("❌ Incorrect grouping. Try again!")
            else:
                print("⚠️ Please select exactly 4 words before submitting.")
        elif command == "analyze":
            print("🔍 Analyzing current board state...")
            # Here you could add AI analysis if needed
            remaining = [cell.word for cell in game_state.cells if not cell.solved]
            print(f"Remaining words: {', '.join(remaining)}")
        else:
            # Try to parse as cell index
            try:
                cell_index = int(command)
                if 0 <= cell_index < 16:
                    game_state = WordConnectionsStateManager.select_cell(
                        game_state, cell_index
                    )
                else:
                    print("❌ Invalid cell index. Use 0-15.")
            except ValueError:
                print("❌ Invalid command. Try again.")

    # Game over
    if game_state.game_status == "victory":
        print("\n🎊 Congratulations! You solved all categories!")
    elif game_state.game_status == "defeat":
        print("\n💀 Game over! You ran out of attempts.")
        print("\nThe categories were:")
        for category, words in game_state.categories.items():
            if category not in game_state.discovered_groups:
                difficulty = game_state.category_difficulty.get(category, "")
                color_emoji = {
                    "yellow": "🟨",
                    "green": "🟩",
                    "blue": "🟦",
                    "purple": "🟪",
                }.get(difficulty, "")
                print(f"{color_emoji} {category}: {', '.join(words)}")

    print(f"\n📈 Final Score: {game_state.score}/4 categories found")


def test_custom_words_only():
    """Simple test just showing the word organization."""
    print("🧪 Testing Custom Word Organization")
    print("=" * 50)

    # Your original words (with typos corrected)
    original_words_raw = "walker jet stroller jogeeer anet hooks ranger monitoro and buitler met bottle slack gay capri jean bib"

    # Cleaned up words
    original_words = [
        "WALKER",
        "JET",
        "STROLLER",
        "JOGGER",
        "NET",
        "HOOKS",
        "RANGER",
        "MONITOR",
        "BUTLER",
        "MET",
        "BOTTLE",
        "SLACK",
        "GAY",
        "CAPRI",
        "JEAN",
        "BIB",
    ]

    print("Original words provided:")
    print(f'"{original_words_raw}"')
    print("\nCleaned up words:")
    print(", ".join(original_words))
    print(f"Total: {len(original_words)} words (perfect for 4x4 Word Connections!)")

    # Show how they've been categorized
    game_state = create_custom_word_connections_game()

    print("\n📂 Organized into categories:")
    for category, words in game_state.categories.items():
        difficulty = game_state.category_difficulty.get(category, "")
        color_emoji = {"yellow": "🟨", "green": "🟩", "blue": "🟦", "purple": "🟪"}.get(
            difficulty, ""
        )
        print(f"{color_emoji} {category} ({difficulty}): {', '.join(words)}")

    print(f"\n✅ Successfully organized {len(original_words)} words into 4 categories!")
    print("🎮 Ready to play as a single-player Word Connections game!")


def run_haive_single_player_game():
    """Run the custom game as a proper Haive single-player game."""
    print("🎮 Starting Haive Single-Player Word Connections")
    print("=" * 60)
    print("This uses your custom words in the full Haive game framework!")
    print("=" * 60)

    # Create agent configuration for single-player mode
    config = WordConnectionsAgentConfig(
        enable_analysis=True,
        visualize=True,
        auto_submit=False,  # Let user make decisions
        source="internal",
    )

    # Create the agent
    agent = WordConnectionsAgent(config)

    try:
        print("\n🚀 Initializing custom game...")

        # Create our custom game state
        initial_state = create_custom_word_connections_game()

        print("✅ Game initialized successfully!")
        print("\n" + initial_state.board_string)

        print("\n🎯 Your Challenge:")
        print("Find the 4 categories of 4 words each!")
        print("Categories are based on your original words:")
        print(
            "walker jet stroller jogger net hooks ranger monitor butler met bottle slack gay capri jean bib"
        )

        print("\n🎲 Game is ready to play!")
        print("You can now use the Haive framework to:")
        print("- Run AI analysis on the board")
        print("- Make moves through the agent")
        print("- Track game progress and history")

        return initial_state, agent

    except Exception as e:
        print(f"❌ Error initializing game: {e}")
        import traceback

        traceback.print_exc()
        return None, agent


def run_full_haive_game_stream():
    """Run the complete game using Haive's streaming interface."""
    print("🎮 Starting Full Haive Word Connections Game Stream")
    print("=" * 60)

    # Create agent with streaming enabled
    config = WordConnectionsAgentConfig(
        enable_analysis=True,
        visualize=True,
        auto_submit=True,  # Let AI play automatically
        source="internal",
    )

    agent = WordConnectionsAgent(config)

    try:
        print("🚀 Starting game stream with AI player...")

        # Create our custom game state
        game_state = create_custom_word_connections_game()

        print("📋 Initial Board:")
        print(game_state.board_string)

        print(
            "\n🤖 AI will now attempt to solve your custom Word Connections puzzle..."
        )
        print("=" * 60)

        # Convert the state to a dict for the workflow
        initial_state_dict = (
            game_state.dict()
            if hasattr(game_state, "dict")
            else game_state.model_dump()
        )

        # Stream through the game with AI making moves
        step_count = 0
        for step in agent.app.stream(
            initial_state_dict,  # Pass as dict instead of state object
            config=agent.runnable_config,
            debug=True,
            stream_mode="values",
        ):
            step_count += 1
            print(f"\n🔄 Step {step_count}:")

            # Visualize the current state
            if hasattr(agent, "visualize_state"):
                agent.visualize_state(step)
            else:
                print(step.get("board_string", "No board state available"))

            # Check for errors
            if step.get("error_message"):
                print(f"❌ Error: {step['error_message']}")

            # Check for game completion
            status = step.get("game_status", "ongoing")
            if status != "ongoing":
                print(f"\n🏁 Game finished with status: {status}")
                if status == "victory":
                    print("🎉 AI successfully solved your custom puzzle!")
                elif status == "defeat":
                    print("💀 AI ran out of attempts.")

                # Show final score
                score = step.get("score", 0)
                print(f"📊 Final Score: {score}/4 categories found")
                break

            # Prevent infinite loops
            if step_count > 20:
                print("⚠️ Stopping after 20 steps to prevent infinite loop")
                break

        print("\n✅ Game stream completed!")

    except Exception as e:
        print(f"❌ Error during game stream: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()

        if mode == "test":
            test_custom_words_only()
        elif mode == "interactive":
            run_interactive_custom_game()
        elif mode == "show":
            run_custom_word_connections_test()
        elif mode == "haive_single":
            run_haive_single_player_game()
        elif mode == "haive_stream":
            run_full_haive_game_stream()
        else:
            print("🎮 Custom Word Connections Game - Usage Options:")
            print("=" * 60)
            print("python test_custom_game.py [mode]")
            print()
            print("Available modes:")
            print("  test          - Just show word organization")
            print("  interactive   - Play manually (default)")
            print("  show          - Show setup and board")
            print("  haive_single  - Run as Haive single-player game")
            print("  haive_stream  - Let AI solve using Haive framework")
            print()
            print("Examples:")
            print("  python test_custom_game.py test")
            print("  python test_custom_game.py haive_stream")
            print("  python test_custom_game.py interactive")
    else:
        # Default: run interactive game
        print("🎮 Starting Interactive Mode (default)")
        print("Use 'python test_custom_game.py test' to see other options")
        print()
        run_interactive_custom_game()
