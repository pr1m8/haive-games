"""Example chess game runner."""

import uuid

import chess

from haive.games.chess.agent import ChessAgent
from haive.games.chess.config import ChessAgentConfig
from haive.games.chess.state import ChessState


def run_chess_game(thread_id: str = None):
    """Run a chess game."""

    # Create thread ID
    thread_id = thread_id or f"chess_{uuid.uuid4().hex[:8]}"
    print(f"🧵 Starting chess game with thread_id: {thread_id}")

    # Create configuration
    config = ChessAgentConfig(name="Chess Game", enable_analysis=True, max_moves=200)

    # Create agent
    agent = ChessAgent(config)

    # Create initial state
    initial_state = ChessState()

    # Compile the agent
    app = agent.app

    # Run the game
    try:
        # Stream the game
        for step in app.stream(
            initial_state.model_dump(),
            config={"configurable": {"thread_id": thread_id}},
            stream_mode="values",
        ):
            # Print current status
            if "game_status" in step:
                print(f"📊 Game status: {step['game_status']}")

            # Check for game end
            if step.get("game_result"):
                print(f"\n🏁 Game ended: {step['game_result']}")
                break

    except Exception as e:
        print(f"❌ Error during game: {e}")
        import traceback

        traceback.print_exc()

    print("\n✅ Game completed!")


if __name__ == "__main__":
    run_chess_game()
