"""Game API setup utilities.

This module provides utilities for setting up game APIs using the
standardized GameAPI system from haive-dataflow.
"""

from typing import Any

from fastapi import FastAPI
from haive.core.engine.agent.agent import Agent
from haive.dataflow.api.game_api import GameAPI
from pydantic import BaseModel, Field


class GameAPIConfig(BaseModel):
    """Configuration for game API setup."""

    app_name: str = Field(description="Name of the game application")
    route_prefix: str = Field(default="/api/games", description="REST API route prefix")
    ws_route_prefix: str = Field(
        default="/ws/games", description="WebSocket route prefix"
    )
    enable_cors: bool = Field(default=True, description="Enable CORS middleware")
    cors_origins: list[str] = Field(default=["*"], description="Allowed CORS origins")
    default_config_overrides: dict[str, Any] | None = Field(
        default=None, description="Default configuration overrides for game instances"
    )


def create_game_api(
    app: FastAPI,
    agent_class: type[Agent],
    api_config: GameAPIConfig | None = None,
    **kwargs,
) -> GameAPI:
    """Create a game API with the standardized system.

    Args:
        app: FastAPI application instance
        agent_class: The game agent class
        api_config: API configuration
        **kwargs: Additional arguments passed to GameAPI

    Returns:
        Configured GameAPI instance
    """
    if api_config is None:
        api_config = GameAPIConfig(app_name="Game")

    # Get the config class from the agent
    config_class = agent_class.get_config_class()

    # Get state schema from config
    state_schema = config_class.model_fields.get("state_schema", {}).get("default")
    if not state_schema:
        raise ValueError(f"Config class {config_class} must define state_schema")

    # Create the API
    game_api = GameAPI(
        app_name=api_config.app_name,
        agent_class=agent_class,
        state_schema=state_schema,
        route_prefix=api_config.route_prefix,
        ws_route_prefix=api_config.ws_route_prefix,
        **kwargs,
    )

    # Enable CORS if requested
    if api_config.enable_cors:
        from fastapi.middleware.cors import CORSMiddleware

        app.add_middleware(
            CORSMiddleware,
            allow_origins=api_config.cors_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    return game_api


# Convenience functions for specific games


def create_chess_api(
    app: FastAPI, config_overrides: dict[str, Any] | None = None, **kwargs
) -> GameAPI:
    """Create a Chess game API.

    Args:
        app: FastAPI application
        config_overrides: Configuration overrides for chess
        **kwargs: Additional API configuration

    Returns:
        Configured GameAPI for chess

    Example:
        >>> app = FastAPI()
        >>> chess_api = create_chess_api(
        ...     app,
        ...     config_overrides={
        ...         "white_model": "gpt-4",
        ...         "black_model": "claude-3-opus",
        ...         "enable_analysis": True
        ...     }
        ... )
    """
    # from haive.games.chess.agent import ChessAgent  # TODO: ChessAgent not implemented

    api_config = GameAPIConfig(
        app_name="Chess",
        route_prefix="/api/chess",
        ws_route_prefix="/ws/chess",
        default_config_overrides=config_overrides,
    )

    return create_game_api(app, ChessAgent, api_config=api_config, **kwargs)


def create_connect4_api(
    app: FastAPI, config_overrides: dict[str, Any] | None = None, **kwargs
) -> GameAPI:
    """Create a Connect4 game API.

    Args:
        app: FastAPI application
        config_overrides: Configuration overrides for Connect4
        **kwargs: Additional API configuration

    Returns:
        Configured GameAPI for Connect4

    Example:
        >>> app = FastAPI()
        >>> connect4_api = create_connect4_api(
        ...     app,
        ...     config_overrides={
        ...         "red_model": "gpt-3.5-turbo",
        ...         "yellow_model": "gpt-3.5-turbo",
        ...         "temperature": 0.5
        ...     }
        ... )
    """
    from haive.games.connect4.agent import Connect4Agent

    api_config = GameAPIConfig(
        app_name="Connect4",
        route_prefix="/api/connect4",
        ws_route_prefix="/ws/connect4",
        default_config_overrides=config_overrides,
    )

    return create_game_api(app, Connect4Agent, api_config=api_config, **kwargs)


def create_tic_tac_toe_api(
    app: FastAPI, config_overrides: dict[str, Any] | None = None, **kwargs
) -> GameAPI:
    """Create a Tic-Tac-Toe game API.

    Args:
        app: FastAPI application
        config_overrides: Configuration overrides for Tic-Tac-Toe
        **kwargs: Additional API configuration

    Returns:
        Configured GameAPI for Tic-Tac-Toe

    Example:
        >>> app = FastAPI()
        >>> ttt_api = create_tic_tac_toe_api(
        ...     app,
        ...     config_overrides={
        ...         "x_model": "claude-3-haiku",
        ...         "o_model": "claude-3-haiku",
        ...         "example_config": "budget"
        ...     }
        ... )
    """
    from haive.games.tic_tac_toe.agent import TicTacToeAgent

    api_config = GameAPIConfig(
        app_name="TicTacToe",
        route_prefix="/api/tictactoe",
        ws_route_prefix="/ws/tictactoe",
        default_config_overrides=config_overrides,
    )

    return create_game_api(app, TicTacToeAgent, api_config=api_config, **kwargs)


# Example usage script
if __name__ == "__main__":
    import uvicorn

    # Create FastAPI app
    app = FastAPI(title="Haive Games API")

    # Add multiple games to the same app
    chess_api = create_chess_api(
        app,
        config_overrides={"example_config": "gpt_vs_claude", "enable_analysis": True},
    )

    connect4_api = create_connect4_api(
        app,
        config_overrides={
            "red_model": "gpt-3.5-turbo",
            "yellow_model": "claude-3-haiku",
        },
    )

    ttt_api = create_tic_tac_toe_api(app, config_overrides={"example_config": "budget"})

    @app.get("/")
    async def root():
        return {
            "message": "Haive Games API",
            "games": {
                "chess": "/api/chess",
                "connect4": "/api/connect4",
                "tictactoe": "/api/tictactoe",
            },
            "websockets": {
                "chess": "/ws/chess/{thread_id}",
                "connect4": "/ws/connect4/{thread_id}",
                "tictactoe": "/ws/tictactoe/{thread_id}",
            },
        }

    # Run the server
    uvicorn.run(app, host="0.0.0.0", port=8000)
