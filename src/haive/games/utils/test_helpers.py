"""Test helpers for bypassing LLM factory issues during testing.

This module provides temporary workarounds for testing game
functionality while the LLM factory registry issues are being resolved.
"""

from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import (
    AnthropicLLMConfig,
    GeminiLLMConfig,
    GroqLLMConfig,
    LLMConfig,
    OpenAILLMConfig,
)

from haive.games.core.agent.player_agent import PlayerAgentConfig


def create_test_llm_config(model: str, **kwargs) -> LLMConfig:
    """Create an LLM config for testing, bypassing the factory.

    Args:
        model: Model name (e.g., "gpt-4o", "claude-3-opus")
        **kwargs: Additional config parameters

    Returns:
        LLMConfig: Appropriate config instance
    """
    # Simple model to provider mapping
    if "gpt" in model.lower():
        return OpenAILLMConfig(model=model, **kwargs)
    if "claude" in model.lower():
        return AnthropicLLMConfig(model=model, **kwargs)
    if "gemini" in model.lower():
        return GeminiLLMConfig(model=model, **kwargs)
    if "llama" in model.lower() or "mixtral" in model.lower():
        return GroqLLMConfig(model=model, **kwargs)
    # Default to OpenAI for unknown models
    return OpenAILLMConfig(model=model, **kwargs)


def create_test_player_agent_config(
    llm_config: str,
    player_name: str = "Test Player",
    temperature: float = 0.3,
    **kwargs,
) -> PlayerAgentConfig:
    """Create a PlayerAgentConfig for testing with direct LLM config.

    Args:
        llm_config: Model string
        player_name: Name for the player
        temperature: Generation temperature
        **kwargs: Additional parameters

    Returns:
        PlayerAgentConfig: Configured player agent
    """
    # Create the LLM config directly
    direct_llm_config = create_test_llm_config(llm_config, temperature=temperature)

    # Return PlayerAgentConfig with the direct config
    return PlayerAgentConfig(
        llm_config=direct_llm_config,
        player_name=player_name,
        temperature=temperature,
        **kwargs,
    )


def create_test_aug_llm_config(
    name: str,
    model: str,
    prompt_template: Any,
    structured_output_model: Any = None,
    temperature: float = 0.3,
    **kwargs,
) -> AugLLMConfig:
    """Create an AugLLMConfig for testing.

    Args:
        name: Engine name
        model: Model string
        prompt_template: Prompt template
        structured_output_model: Output model class
        temperature: Generation temperature
        **kwargs: Additional parameters

    Returns:
        AugLLMConfig: Configured augmented LLM
    """
    llm_config = create_test_llm_config(model, temperature=temperature)

    return AugLLMConfig(
        name=name,
        llm_config=llm_config,
        prompt_template=prompt_template,
        structured_output_model=structured_output_model,
        temperature=temperature,
        structured_output_version="v1",
        **kwargs,
    )


def create_test_engines_simple(
    player1_model: str,
    player2_model: str,
    player1_name: str = "player1",
    player2_name: str = "player2",
    temperature: float = 0.3,
) -> dict[str, AugLLMConfig]:
    """Create a simple set of test engines for any two-player game.

    Args:
        player1_model: Model for first player
        player2_model: Model for second player
        player1_name: Name/identifier for first player
        player2_name: Name/identifier for second player
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of test engines
    """
    from langchain_core.prompts import ChatPromptTemplate

    # Simple prompt template for testing
    test_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a game player. Make your move."),
            ("human", "Current state: {state}\nMake your move."),
        ]
    )

    engines = {
        f"{player1_name}_player": create_test_aug_llm_config(
            f"{player1_name}_player",
            player1_model,
            test_prompt,
            temperature=temperature,
        ),
        f"{player2_name}_player": create_test_aug_llm_config(
            f"{player2_name}_player",
            player2_model,
            test_prompt,
            temperature=temperature,
        ),
        f"{player1_name}_analyzer": create_test_aug_llm_config(
            f"{player1_name}_analyzer",
            player1_model,
            test_prompt,
            temperature=0.2,  # Lower temp for analysis
        ),
        f"{player2_name}_analyzer": create_test_aug_llm_config(
            f"{player2_name}_analyzer",
            player2_model,
            test_prompt,
            temperature=0.2,  # Lower temp for analysis
        ),
    }

    return engines


# Game-specific helper functions


def create_test_chess_engines(
    white_model: str = "gpt-4o", black_model: str = "claude-3-opus", **kwargs
) -> dict[str, AugLLMConfig]:
    """Create test engines for Chess."""
    return create_test_engines_simple(
        white_model, black_model, "white", "black", **kwargs
    )


def create_test_connect4_engines(
    red_model: str = "gpt-4o", yellow_model: str = "claude-3-opus", **kwargs
) -> dict[str, AugLLMConfig]:
    """Create test engines for Connect4."""
    return create_test_engines_simple(
        red_model, yellow_model, "red", "yellow", **kwargs
    )


def create_test_checkers_engines(
    red_model: str = "gpt-4o", black_model: str = "claude-3-opus", **kwargs
) -> dict[str, AugLLMConfig]:
    """Create test engines for Checkers."""
    return create_test_engines_simple(red_model, black_model, "red", "black", **kwargs)


def create_test_ttt_engines(
    x_model: str = "gpt-4o", o_model: str = "claude-3-opus", **kwargs
) -> dict[str, AugLLMConfig]:
    """Create test engines for Tic-Tac-Toe."""
    return create_test_engines_simple(x_model, o_model, "X", "O", **kwargs)


# Test validation helpers


def validate_engine_structure(engines: dict[str, AugLLMConfig], game_name: str) -> bool:
    """Validate that engines have the expected structure.

    Args:
        engines: Dictionary of engines to validate
        game_name: Name of the game for logging

    Returns:
        bool: True if structure is valid
    """
    if len(engines) != 4:
        return False

    # Check that all engines have required attributes
    for _name, engine in engines.items():
        if not hasattr(engine, "llm_config"):
            return False
        if not hasattr(engine, "prompt_template"):
            return False

    return True


def test_basic_game_structure(
    game_name: str, create_engines_func, expected_roles: list
) -> bool:
    """Test basic game structure.

    Args:
        game_name: Name of the game
        create_engines_func: Function to create engines
        expected_roles: List of expected role names

    Returns:
        bool: True if test passed
    """
    try:

        # Create engines
        engines = create_engines_func()

        # Validate structure
        if not validate_engine_structure(engines, game_name):
            return False

        # Check expected roles
        actual_roles = set(engines.keys())
        expected_roles_set = set(expected_roles)

        return actual_roles == expected_roles_set

    except Exception:
        return False


if __name__ == "__main__":
    # Test all games
    results = {}

    results["Chess"] = test_basic_game_structure(
        "Chess",
        create_test_chess_engines,
        ["white_player", "black_player", "white_analyzer", "black_analyzer"],
    )

    results["Connect4"] = test_basic_game_structure(
        "Connect4",
        create_test_connect4_engines,
        ["red_player", "yellow_player", "red_analyzer", "yellow_analyzer"],
    )

    results["Checkers"] = test_basic_game_structure(
        "Checkers",
        create_test_checkers_engines,
        ["red_player", "black_player", "red_analyzer", "black_analyzer"],
    )

    results["Tic-Tac-Toe"] = test_basic_game_structure(
        "Tic-Tac-Toe",
        create_test_ttt_engines,
        ["X_player", "O_player", "X_analyzer", "O_analyzer"],
    )

    # Summary

    passed = sum(results.values())
    total = len(results)

    for _game, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
