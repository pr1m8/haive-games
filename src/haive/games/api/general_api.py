"""General API system for all haive games.

from typing import Any This module provides a general-purpose API that automatically
discovers all available games and creates endpoints for each one, with OpenAPI
documentation and game selection capabilities.

"""

import importlib
import logging
import uuid
from pathlib import Path
from typing import Any

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from haive.core.engine.agent.agent import Agent
from haive.dataflow.api.game_api import GameAPI
from pydantic import BaseModel, Field

from haive.games.core.config import BaseGameConfig

logger = logging.getLogger(__name__)


class GameInfo(BaseModel):
    """Information about an available game."""

    name: str = Field(description="Display name of the game")
    game_id: str = Field(description="Unique identifier for the game")
    description: str = Field(description="Description of the game")
    players: list[str] = Field(description="List of player roles")
    example_configs: list[str] = Field(description="Available example configurations")
    default_models: dict[str, str] = Field(description="Default models for each player")
    api_endpoints: dict[str, str] = Field(description="API endpoints for this game")


class GameSelectionRequest(BaseModel):
    """Request for creating a new game."""

    game_id: str = Field(description="ID of the game to create")
    config_mode: str = Field(
        default="simple",
        description="Configuration mode: simple, example, advanced, legacy",
    )
    player_models: dict[str, str] | None = Field(
        default=None, description="Models for each player (simple mode)"
    )
    example_config: str | None = Field(
        default=None, description="Example configuration name (example mode)"
    )
    player_configs: dict[str, Any] | None = Field(
        default=None, description="Advanced player configurations"
    )
    game_settings: dict[str, Any] | None = Field(
        default=None, description="Additional game settings"
    )


class GeneralGameAPI:
    """General API system that discovers and manages all games."""

    def __init__(
        self,
        app: FastAPI,
        games_package: str = "haive.games",
        route_prefix: str = "/api/games",
        ws_route_prefix: str = "/ws/games",
        exclude_games: list[str] | None = None,
    ):
        """Initialize the general game API.

        Args:
            app: FastAPI application
            games_package: Package to scan for games
            route_prefix: Prefix for REST routes
            ws_route_prefix: Prefix for WebSocket routes
            exclude_games: List of game names to exclude

        """
        self.app = app
        self.games_package = games_package
        self.route_prefix = route_prefix
        self.ws_route_prefix = ws_route_prefix
        self.exclude_games = exclude_games or ["go", "among_us"]  # Default exclusions

        self.discovered_games: dict[str, dict[str, Any]] = {}
        self.game_apis: dict[str, GameAPI] = {}

        # Discover and register games
        self._discover_games()
        self._register_routes()
        self._setup_openapi()

    def _discover_games(self):
        """Discover all available games in the package."""
        logger.info(f"Discovering games in {self.games_package}")

        # Get the package path
        try:
            games_module = importlib.import_module(self.games_package)
            games_path = Path(games_module.__file__).parent
        except Exception as e:
            logger.exception(f"Failed to import games package: {e}")
            return

        # Scan for game directories
        for game_dir in games_path.iterdir():
            if not game_dir.is_dir() or game_dir.name.startswith("_"):
                continue

            game_name = game_dir.name

            # Skip excluded games
            if game_name in self.exclude_games:
                logger.info(f"Skipping excluded game: {game_name}")
                continue

            # Try to import the game
            try:
                game_info = self._import_game(game_name)
                if game_info:
                    self.discovered_games[game_name] = game_info
                    logger.info(f"Discovered game: {game_name}")
            except Exception as e:
                logger.warning(f"Failed to import game {game_name}: {e}")

    def _import_game(self, game_name: str) -> dict[str, Any] | None:
        """Import a specific game and extract its information."""
        try:
            # Try to import agent module
            agent_module = importlib.import_module(
                f"{self.games_package}.{game_name}.agent"
            )

            # Find the agent class
            agent_class = None
            for attr_name in dir(agent_module):
                attr = getattr(agent_module, attr_name)
                if isinstance(attr, type) and issubclass(attr, Agent) and attr != Agent:
                    agent_class = attr
                    break

            if not agent_class:
                return None

            # Get config class
            config_class = agent_class.get_config_class()
            if not config_class:
                return None

            # Extract game information
            game_info = {
                "agent_class": agent_class,
                "config_class": config_class,
                "name": getattr(
                    config_class, "name", game_name.replace("_", " ").title()
                ),
                "game_id": game_name,
            }

            # Try to get additional info if config extends BaseGameConfig
            if issubclass(config_class, BaseGameConfig):
                # Create a temporary instance to get metadata
                try:
                    temp_config = config_class()
                    game_info["role_definitions"] = temp_config.get_role_definitions()
                    game_info["example_configs"] = list(
                        temp_config.get_example_configs().keys()
                    )
                    game_info["players"] = [
                        role.display_name
                        for role in game_info["role_definitions"].values()
                        if not role.is_analyzer
                    ]
                    game_info["default_models"] = {
                        role.display_name: role.default_model
                        for role in game_info["role_definitions"].values()
                        if not role.is_analyzer
                    }
                except Exception as e:
                    logger.warning(f"Failed to extract metadata for {game_name}: {e}")
                    game_info["players"] = ["Player 1", "Player 2"]
                    game_info["example_configs"] = []
                    game_info["default_models"] = {}

            return game_info

        except Exception as e:
            logger.exception(f"Error importing game {game_name}: {e}")
            return None

    def _register_routes(self):
        """Register API routes for all discovered games."""

        # Main games list endpoint
        @self.app.get(f"{self.route_prefix}/", response_model=list[GameInfo])
        async def list_games():
            """List all available games."""
            games = []
            for game_id, game_info in self.discovered_games.items():
                games.append(
                    GameInfo(
                        name=game_info["name"],
                        game_id=game_id,
                        description=f"Play {game_info['name']} with configurable AI opponents",
                        players=game_info.get("players", ["Player 1", "Player 2"]),
                        example_configs=game_info.get("example_configs", []),
                        default_models=game_info.get("default_models", {}),
                        api_endpoints={
                            "create": f"{self.route_prefix}/{game_id}/create",
                            "status": f"{self.route_prefix}/{game_id}/{{thread_id}}",
                            "move": f"{self.route_prefix}/{game_id}/{{thread_id}}/move",
                            "ai_move": f"{self.route_prefix}/{game_id}/{{thread_id}}/ai-move",
                            "websocket": f"{self.ws_route_prefix}/{game_id}/{{thread_id}}",
                        },
                    )
                )
            return games

        # Game selection endpoint
        @self.app.post(f"{self.route_prefix}/create")
        async def create_game(request: GameSelectionRequest):
            """Create a new game with the specified configuration."""
            game_id = request.game_id

            if game_id not in self.discovered_games:
                raise HTTPException(
                    status_code=404,
                    detail=f"Game '{game_id}' not found. Available games: {
                        list(self.discovered_games.keys())
                    }",
                )

            game_info = self.discovered_games[game_id]
            game_info["config_class"]

            # Build configuration based on mode
            config_kwargs = {}

            if request.config_mode == "legacy":
                config_kwargs["use_legacy_engines"] = True

            elif request.config_mode == "example":
                if not request.example_config:
                    raise HTTPException(
                        status_code=400,
                        detail="example_config required for example mode",
                    )
                config_kwargs["example_config"] = request.example_config

            elif request.config_mode == "advanced":
                if not request.player_configs:
                    raise HTTPException(
                        status_code=400,
                        detail="player_configs required for advanced mode",
                    )
                config_kwargs["player_configs"] = request.player_configs

            elif request.player_models:
                # Map generic player1/player2 to game-specific fields
                if game_id == "chess":
                    config_kwargs["white_model"] = request.player_models.get(
                        "player1", "gpt-4"
                    )
                    config_kwargs["black_model"] = request.player_models.get(
                        "player2", "claude-3-opus"
                    )
                elif game_id == "connect4":
                    config_kwargs["red_model"] = request.player_models.get(
                        "player1", "gpt-4"
                    )
                    config_kwargs["yellow_model"] = request.player_models.get(
                        "player2", "claude-3-opus"
                    )
                elif game_id == "tic_tac_toe":
                    config_kwargs["x_model"] = request.player_models.get(
                        "player1", "gpt-4"
                    )
                    config_kwargs["o_model"] = request.player_models.get(
                        "player2", "claude-3-opus"
                    )
                else:
                    config_kwargs["player1_model"] = request.player_models.get(
                        "player1", "gpt-4"
                    )
                    config_kwargs["player2_model"] = request.player_models.get(
                        "player2", "claude-3-opus"
                    )

            # Add any additional game settings
            if request.game_settings:
                config_kwargs.update(request.game_settings)

            # Create the game API if not already created
            if game_id not in self.game_apis:
                self._create_game_api(game_id, game_info)

            # Generate thread ID

            thread_id = str(uuid.uuid4())

            return {
                "game_id": game_id,
                "thread_id": thread_id,
                "config": config_kwargs,
                "endpoints": {
                    "status": f"{self.route_prefix}/{game_id}/{thread_id}",
                    "move": f"{self.route_prefix}/{game_id}/{thread_id}/move",
                    "ai_move": f"{self.route_prefix}/{game_id}/{thread_id}/ai-move",
                    "websocket": f"{self.ws_route_prefix}/{game_id}/{thread_id}",
                },
            }

        # Register individual game APIs
        for game_id, game_info in self.discovered_games.items():
            self._create_game_api(game_id, game_info)

    def _create_game_api(self, game_id: str, game_info: dict[str, Any]):
        """Create API for a specific game."""
        agent_class = game_info["agent_class"]
        config_class = game_info["config_class"]

        # Get state schema
        state_schema = getattr(config_class, "state_schema", None)
        if hasattr(state_schema, "default"):
            state_schema = state_schema.default

        if not state_schema:
            logger.warning(f"No state schema found for {game_id}")
            return

        # Create game-specific API
        game_api = GameAPI(
            app_name=game_info["name"],
            agent_class=agent_class,
            state_schema=state_schema,
            route_prefix=f"{self.route_prefix}/{game_id}",
            ws_route_prefix=f"{self.ws_route_prefix}/{game_id}",
        )

        self.game_apis[game_id] = game_api

    def _setup_openapi(self):
        """Setup custom OpenAPI documentation."""

        def custom_openapi() -> Any:
            if self.app.openapi_schema:
                return self.app.openapi_schema

            openapi_schema = get_openapi(
                title="Haive Games API",
                version="1.0.0",
                description="""
                # Haive Games API

                This API provides access to all available games in the Haive framework.

                ## Features
                - Automatic game discovery
                - Configurable AI opponents
                - Multiple configuration modes
                - Real-time gameplay via WebSocket
                - OpenAPI documentation

                ## Configuration Modes

                ### Simple Mode
                Specify models as strings for each player.

                ### Example Mode
                Use predefined configurations like "budget" or "gpt_vs_claude".

                ### Advanced Mode
                Full control with PlayerAgentConfig objects.

                ### Legacy Mode
                Use hardcoded engines for backward compatibility.

                ## Available Games
                """
                + "\n".join(
                    [
                        f"- **{info['name']}** ({game_id})"
                        for game_id, info in self.discovered_games.items()
                    ]
                ),
                routes=self.app.routes,
            )

            # Add game-specific information
            if "components" not in openapi_schema:
                openapi_schema["components"] = {}
            if "schemas" not in openapi_schema["components"]:
                openapi_schema["components"]["schemas"] = {}

            # Add game info schemas
            for game_id, game_info in self.discovered_games.items():
                schema_name = f"{game_id}_info"
                openapi_schema["components"]["schemas"][schema_name] = {
                    "title": f"{game_info['name']} Information",
                    "type": "object",
                    "properties": {
                        "players": {
                            "type": "array",
                            "items": {"type": "string"},
                            "example": game_info.get(
                                "players", ["Player 1", "Player 2"]
                            ),
                        },
                        "example_configs": {
                            "type": "array",
                            "items": {"type": "string"},
                            "example": game_info.get("example_configs", []),
                        },
                        "default_models": {
                            "type": "object",
                            "example": game_info.get("default_models", {}),
                        },
                    },
                }

            self.app.openapi_schema = openapi_schema
            return self.app.openapi_schema

        self.app.openapi = custom_openapi


def create_general_game_api(
    app: FastAPI | None = None, **kwargs
) -> tuple[FastAPI, GeneralGameAPI]:
    """Create a general game API that discovers all games.

    Args:
        app: Optional FastAPI app (creates one if not provided)
        **kwargs: Additional arguments for GeneralGameAPI

    Returns:
        Tuple of (FastAPI app, GeneralGameAPI instance)

    Example:
        >>> app, game_api = create_general_game_api()
        >>> # Now you have endpoints for all games!

    """
    if app is None:
        app = FastAPI(
            title="Haive Games API",
            description="Play AI-powered games with configurable opponents",
            version="1.0.0",
        )

    # Enable CORS

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Create the general API
    api = GeneralGameAPI(app, **kwargs)

    # Add root endpoint
    @app.get("/")
    async def root():
        return {
            "message": "Haive Games API",
            "documentation": "/docs",
            "games": f"{api.route_prefix}/",
            "create_game": f"{api.route_prefix}/create",
        }

    return app, api


# Example usage
if __name__ == "__main__":
    # Create the general API
    app, game_api = create_general_game_api()

    for _game_id, _info in game_api.discovered_games.items():
        pass

    uvicorn.run(app, host="0.0.0.0", port=8000)
