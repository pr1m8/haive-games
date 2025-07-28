"""Recursion configuration utilities for game agents.

This module provides utilities to properly configure recursion limits
for game agents to prevent recursion errors during gameplay.
"""

from typing import Any, Dict, Optional


class RecursionConfig:
    """Configuration helper for managing recursion limits in game agents."""

    # Default recursion limits for different game types
    DEFAULT_LIMITS = {
        "simple": 300,  # Simple turn-based games (tic-tac-toe, etc.)
        "standard": 500,  # Standard games (chess, checkers)
        "complex": 800,  # Complex games with many analysis steps
        "extreme": 1200,  # Games with heavy analysis or many players
    }

    # Game-specific overrides
    GAME_LIMITS = {
        "chess": 600,  # Chess with analysis needs more
        "checkers": 500,  # Standard for checkers
        "connect4": 400,  # Simpler game
        "monopoly": 800,  # Complex multi-player
        "poker": 700,  # Multiple rounds and players
        "battleship": 500,  # Standard two-player
        "fox_and_geese": 500,  # Standard strategy
        "mancala": 400,  # Relatively simple
        "dominoes": 500,  # Standard gameplay
    }

    @classmethod
    def get_recursion_limit(
        cls,
        game_name: Optional[str] = None,
        game_type: str = "standard",
        enable_analysis: bool = False,
        num_players: int = 2,
        custom_limit: Optional[int] = None,
    ) -> int:
        """Get the appropriate recursion limit for a game.

        Args:
            game_name: Specific game name (e.g., "chess", "checkers")
            game_type: Type of game ("simple", "standard", "complex", "extreme")
            enable_analysis: Whether analysis is enabled (adds overhead)
            num_players: Number of players (more players = higher limit)
            custom_limit: Override with custom limit

        Returns:
            Recommended recursion limit

        Examples:
            >>> # Simple game
            >>> limit = RecursionConfig.get_recursion_limit(game_type="simple")
            >>> print(limit)  # 300

            >>> # Chess with analysis
            >>> limit = RecursionConfig.get_recursion_limit(
            ...     game_name="chess",
            ...     enable_analysis=True
            ... )
            >>> print(limit)  # 720 (600 + 20% for analysis)

            >>> # Multi-player game
            >>> limit = RecursionConfig.get_recursion_limit(
            ...     game_type="complex",
            ...     num_players=4
            ... )
            >>> print(limit)  # 960 (800 + 20% for extra players)
        """
        # Use custom limit if provided
        if custom_limit is not None:
            return max(custom_limit, 200)  # Minimum safety limit

        # Start with game-specific or type-based limit
        if game_name and game_name.lower() in cls.GAME_LIMITS:
            base_limit = cls.GAME_LIMITS[game_name.lower()]
        else:
            base_limit = cls.DEFAULT_LIMITS.get(game_type, 500)

        # Adjust for analysis
        if enable_analysis:
            base_limit = int(base_limit * 1.2)  # 20% increase

        # Adjust for multiple players
        if num_players > 2:
            # 10% increase per additional player
            player_factor = 1 + (0.1 * (num_players - 2))
            base_limit = int(base_limit * player_factor)

        # Ensure minimum safety limit
        return max(base_limit, 200)

    @classmethod
    def configure_runnable(
        cls,
        runnable_config: Optional[Dict[str, Any]] = None,
        game_name: Optional[str] = None,
        game_type: str = "standard",
        enable_analysis: bool = False,
        num_players: int = 2,
        thread_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Configure or update a runnable config with appropriate recursion
        limit.

        Args:
            runnable_config: Existing config to update (creates new if None)
            game_name: Specific game name
            game_type: Type of game
            enable_analysis: Whether analysis is enabled
            num_players: Number of players
            thread_id: Thread ID to use (generates if None)

        Returns:
            Updated runnable configuration

        Examples:
            >>> # Create new config for chess
            >>> config = RecursionConfig.configure_runnable(
            ...     game_name="chess",
            ...     enable_analysis=True
            ... )
            >>> print(config["configurable"]["recursion_limit"])  # 720

            >>> # Update existing config
            >>> existing = {"configurable": {"thread_id": "abc123"}}
            >>> updated = RecursionConfig.configure_runnable(
            ...     runnable_config=existing,
            ...     game_type="complex"
            ... )
            >>> print(updated["configurable"]["recursion_limit"])  # 800
        """
        # Start with existing config or create new
        if runnable_config is None:
            runnable_config = {"configurable": {}}
        elif "configurable" not in runnable_config:
            runnable_config["configurable"] = {}

        # Get appropriate recursion limit
        recursion_limit = cls.get_recursion_limit(
            game_name=game_name,
            game_type=game_type,
            enable_analysis=enable_analysis,
            num_players=num_players,
        )

        # Update configurable settings
        configurable = runnable_config["configurable"]

        # Set recursion limit (don't decrease if already higher)
        current_limit = configurable.get("recursion_limit", 0)
        configurable["recursion_limit"] = max(recursion_limit, current_limit)

        # Set thread_id if not present
        if "thread_id" not in configurable and thread_id:
            configurable["thread_id"] = thread_id
        elif "thread_id" not in configurable:
            import uuid

            configurable["thread_id"] = str(uuid.uuid4())

        # Add other common settings if not present
        if "engine_configs" not in configurable:
            configurable["engine_configs"] = {}

        return runnable_config

    @classmethod
    def validate_recursion_limit(
        cls,
        limit: int,
        game_name: Optional[str] = None,
        game_type: str = "standard",
    ) -> tuple[bool, str]:
        """Validate if a recursion limit is appropriate.

        Args:
            limit: The recursion limit to validate
            game_name: Specific game name
            game_type: Type of game

        Returns:
            Tuple of (is_valid, message)

        Examples:
            >>> valid, msg = RecursionConfig.validate_recursion_limit(
            ...     100, game_type="complex"
            ... )
            >>> print(valid, msg)  # False, "Limit too low..."
        """
        recommended = cls.get_recursion_limit(
            game_name=game_name,
            game_type=game_type,
        )

        if limit < 200:
            return False, f"Recursion limit {limit} is too low. Minimum is 200."

        if limit < recommended * 0.8:
            return False, (
                f"Recursion limit {limit} may be too low for {game_name or game_type}. "
                f"Recommended: {recommended}"
            )

        if limit > recommended * 2:
            return True, (
                f"Recursion limit {limit} is higher than needed. "
                f"Recommended: {recommended}"
            )

        return True, f"Recursion limit {limit} is appropriate."
