"""Unified LLM configuration factory for games.

This module provides a simplified factory for creating LLM configurations
for game agents, leveraging the new haive.core.models.llm factory system.
"""

from typing import Any, Dict, Optional, Tuple

from haive.core.models.llm import LLMConfig


# Note: These functions don't exist in the current core module
# We'll implement simplified versions for games until core API is available
def get_model_info(model: str) -> Dict[str, Any]:
    """Placeholder for model info - not yet implemented in core."""
    return {"model": model, "status": "placeholder"}


def list_available_models() -> list:
    """Placeholder for listing models - not yet implemented in core."""
    return []


class GameLLMFactory:
    """Factory for creating game-specific LLM configurations.

    This factory simplifies the process of creating LLM configurations for games
    by providing game-optimized defaults and leveraging the core LLM factory.
    """

    # Game-optimized temperature defaults
    GAME_TEMPERATURES: Dict[str, float] = {
        "strategic": 0.7,  # For strategic thinking (chess, checkers)
        "creative": 0.8,  # For creative play (storytelling games)
        "precise": 0.5,  # For rule-following (card games)
        "competitive": 0.6,  # For competitive analysis
        "default": 0.7,  # General default
    }

    # Game-specific model recommendations
    GAME_RECOMMENDATIONS: Dict[str, Dict[str, str]] = {
        "chess": {
            "default": "gpt-4",
            "fast": "gpt-3.5-turbo",
            "strong": "claude-3-opus",
        },
        "creative": {
            "default": "claude-3-sonnet",
            "fast": "gpt-3.5-turbo",
            "strong": "gpt-4",
        },
        "strategic": {
            "default": "gpt-4",
            "fast": "claude-3-haiku",
            "strong": "claude-3-opus",
        },
    }

    @classmethod
    def create_llm_config(
        cls,
        model: str,
        temperature: Optional[float] = None,
        game_type: str = "default",
        **kwargs
    ) -> LLMConfig:
        """Create an LLM configuration for a game.

        This method wraps the core create_llm_config with game-specific defaults.

        Args:
            model: Model string (e.g., "gpt-4", "claude-3-opus", "anthropic:claude-3-sonnet")
            temperature: Temperature setting (uses game_type default if None)
            game_type: Type of game ("strategic", "creative", "precise", "competitive")
            **kwargs: Additional parameters

        Returns:
            LLMConfig: Configured LLM instance

        Examples:
            >>> # Simple usage
            >>> config = GameLLMFactory.create_llm_config("gpt-4")

            >>> # Game-specific temperature
            >>> config = GameLLMFactory.create_llm_config(
            ...     "claude-3-opus",
            ...     game_type="strategic"
            ... )

            >>> # Custom parameters
            >>> config = GameLLMFactory.create_llm_config(
            ...     "gpt-4",
            ...     temperature=0.5,
            ...     max_tokens=1000
            ... )
        """
        # Determine temperature based on game type
        if temperature is None:
            temperature = cls.GAME_TEMPERATURES.get(
                game_type, cls.GAME_TEMPERATURES["default"]
            )

        # Use core factory with game defaults
        # Note: create_llm returns an LLM instance, not LLMConfig
        # For now, create a basic LLMConfig - this needs to be updated when proper factory is available
        from haive.core.models.llm.base import OpenAILLMConfig

        # Simple provider detection - enhance this as needed
        if "claude" in model.lower():
            from haive.core.models.llm.base import AnthropicLLMConfig

            return AnthropicLLMConfig(model=model, temperature=temperature, **kwargs)
        else:
            return OpenAILLMConfig(model=model, temperature=temperature, **kwargs)

    @classmethod
    def create_game_llm_pair(
        cls,
        player1_model: str = "gpt-4",
        player2_model: str = "gpt-4",
        game_type: str = "strategic",
        temperature: Optional[float] = None,
    ) -> Tuple[LLMConfig, LLMConfig]:
        """Create a pair of LLM configs for two-player games.

        Args:
            player1_model: Model string for player 1
            player2_model: Model string for player 2
            game_type: Type of game for temperature defaults
            temperature: Override temperature for both players

        Returns:
            Tuple of (player1_config, player2_config)

        Examples:
            >>> # Same model
            >>> p1, p2 = GameLLMFactory.create_game_llm_pair("gpt-4")

            >>> # Different models
            >>> p1, p2 = GameLLMFactory.create_game_llm_pair(
            ...     "claude-3-opus",
            ...     "gpt-4"
            ... )

            >>> # With providers
            >>> p1, p2 = GameLLMFactory.create_game_llm_pair(
            ...     "anthropic:claude-3-opus",
            ...     "openai:gpt-4"
            ... )
        """
        player1_config = cls.create_llm_config(
            player1_model,
            temperature=temperature,
            game_type=game_type,
        )

        player2_config = cls.create_llm_config(
            player2_model,
            temperature=temperature,
            game_type=game_type,
        )

        return player1_config, player2_config

    @classmethod
    def get_recommended_model(cls, game_type: str, performance: str = "default") -> str:
        """Get recommended model for a game type.

        Args:
            game_type: Type of game ("chess", "creative", "strategic")
            performance: Performance tier ("fast", "default", "strong")

        Returns:
            Recommended model string

        Examples:
            >>> # Get default chess model
            >>> model = GameLLMFactory.get_recommended_model("chess")
            >>> print(model)  # "gpt-4"

            >>> # Get fast creative model
            >>> model = GameLLMFactory.get_recommended_model("creative", "fast")
            >>> print(model)  # "gpt-3.5-turbo"
        """
        recommendations = cls.GAME_RECOMMENDATIONS.get(
            game_type, cls.GAME_RECOMMENDATIONS["strategic"]
        )
        return recommendations.get(performance, recommendations["default"])

    @classmethod
    def list_game_models(cls, game_type: Optional[str] = None) -> Dict[str, Any]:
        """List available models for games.

        Args:
            game_type: Optional game type to get recommendations for

        Returns:
            Dictionary with model information

        Examples:
            >>> models = GameLLMFactory.list_game_models("chess")
            >>> print(models["recommendations"])
        """
        # Get all available models from core
        all_models = list_available_models()

        result = {
            "total_models": len(all_models),
            "providers": list(set(m.provider for m in all_models)),
        }

        if game_type and game_type in cls.GAME_RECOMMENDATIONS:
            result["recommendations"] = cls.GAME_RECOMMENDATIONS[game_type]
            result["temperature"] = cls.GAME_TEMPERATURES.get(
                game_type, cls.GAME_TEMPERATURES["default"]
            )

        return result
