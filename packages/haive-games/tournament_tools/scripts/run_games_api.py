#!/usr/bin/env python3
"""Run the Haive Games API server.

This script provides a simple way to start the general games API
with all available games automatically discovered and configured.

Usage:
    python run_games_api.py [options]

Options:
    --port PORT         Port to run on (default: 8000)
    --host HOST         Host to bind to (default: 0.0.0.0)
    --reload           Enable auto-reload for development
    --exclude GAMES    Comma-separated list of games to exclude
"""

import argparse

import uvicorn

from haive.games.api import create_general_game_api


def main():
    """Main entry point for the games API server."""
    parser = argparse.ArgumentParser(
        description="Run the Haive Games API server",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to run the server on (default: 8000)",
    )

    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="Host to bind the server to (default: 0.0.0.0)",
    )

    parser.add_argument(
        "--reload", action="store_true", help="Enable auto-reload for development"
    )

    parser.add_argument(
        "--exclude",
        type=str,
        help="Comma-separated list of games to exclude (e.g., 'go,monopoly')",
    )

    args = parser.parse_args()

    # Parse excluded games
    exclude_games = None
    if args.exclude:
        exclude_games = [g.strip() for g in args.exclude.split(",")]

    # Create the API
    print("🎮 Starting Haive Games API Server")
    print("=" * 50)

    app, game_api = create_general_game_api(exclude_games=exclude_games)

    # Show discovered games
    print(f"\n📦 Discovered {len(game_api.discovered_games)} games:")
    for game_id, info in game_api.discovered_games.items():
        players = info.get("players", ["Player 1", "Player 2"])
        print(f"  • {info['name']} ({game_id}) - {' vs '.join(players)}")

    if exclude_games:
        print(f"\n❌ Excluded games: {', '.join(exclude_games)}")

    # Show endpoints
    print(f"\n🌐 API Endpoints:")
    print(f"  • List games: http://{args.host}:{args.port}/api/games/")
    print(f"  • Create game: http://{args.host}:{args.port}/api/games/create")
    print(f"  • Documentation: http://{args.host}:{args.port}/docs")
    print(f"  • Interactive docs: http://{args.host}:{args.port}/redoc")

    print("\n🚀 Starting server...")
    print(f"   Listening on http://{args.host}:{args.port}")
    print("   Press Ctrl+C to stop\n")

    # Run the server
    uvicorn.run(
        app, host=args.host, port=args.port, reload=args.reload, log_level="info"
    )


if __name__ == "__main__":
    main()
