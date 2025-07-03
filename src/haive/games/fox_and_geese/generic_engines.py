"""Generic FoxAndGeese engine creation using the generic player agent system.

This module provides generic engine creation functions for FoxAndGeese games,
allowing for configurable LLM models and game-specific player identifiers.
"""

from typing import Any, Dict, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.core.agent.generic_player_agent import (
    GamePlayerIdentifiers,
    GenericGameEngineFactory,
    GenericPromptGenerator,
    create_engines_from_simple_configs,
)
from haive.games.core.agent.player_agent import PlayerAgentConfig
from haive.games.fox_and_geese.models import (
    FoxAndGeeseAnalysis,
    FoxAndGeeseMove,
)


class FoxAndGeesePlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Player identifiers for FoxAndGeese game."""
    
    def __init__(self):
        super().__init__(
            player1="fox",
            player2="geese"
        )


class FoxAndGeesePromptGenerator(GenericPromptGenerator[str, str]):
    """Prompt generator for FoxAndGeese game."""
    
    def create_move_prompt(self, player: str) -> ChatPromptTemplate:
        """Create move prompt for FoxAndGeese player."""
        return ChatPromptTemplate.from_messages([
            (
                "system",
                f"You are {player} in a FoxAndGeese game. You are playing Fox and Geese. As the fox, capture geese; as geese, trap the fox.\n\n"
                "As a FoxAndGeese player:\n"
                "- Fox: Use mobility to separate and capture geese"
                "- Geese: Work together to surround and trap the fox"
                "- Control key board positions and movement paths"
                "- Plan several moves ahead"
                "- Use sacrificial tactics when beneficial"\n\n"
                "Key strategies:\n"
                "- Think several moves ahead\n"
                "- Adapt your strategy based on game state\n"
                "- Make calculated decisions\n"
                "- Learn from opponent's patterns\n"
                "- Stay focused on your win condition"
            ),
            (
                "human",
                "Current Game State:\n"
                "{game_state}\n\n"
                "Game History:\n"
                "{game_history}\n\n"
                "Available Actions:\n"
                "{available_actions}\n\n"
                "Make your next move. Analyze the position and choose your action carefully."
            ),
        ])
    
    def create_analyzer_prompt(self, player: str) -> ChatPromptTemplate:
        """Create analysis prompt for FoxAndGeese game state."""
        return ChatPromptTemplate.from_messages([
            (
                "system",
                f"You are an expert FoxAndGeese strategist analyzing the current game state for {player}.\n\n"
                "Analyze the game considering:\n"
                "- Current position and opportunities\n"
                "- Strategic advantages and disadvantages\n"
                "- Potential moves and their consequences\n"
                "- Opponent's possible strategies\n"
                "- Risk assessment and probability\n"
                "- Optimal decision-making"
            ),
            (
                "human",
                "Game State to Analyze:\n"
                "{game_state}\n\n"
                "Player Status:\n"
                "{player_status}\n\n"
                "Game History:\n"
                "{game_history}\n\n"
                "Current Situation:\n"
                "{current_situation}\n\n"
                "Provide a comprehensive analysis of the position, "
                "including strategic recommendations and tactical considerations."
            ),
        ])


class FoxAndGeeseEngineFactory(GenericGameEngineFactory[str, str]):
    """Factory for creating FoxAndGeese game engines."""
    
    def __init__(self):
        identifiers = FoxAndGeesePlayerIdentifiers()
        prompt_generator = FoxAndGeesePromptGenerator()
        super().__init__(identifiers, prompt_generator)
    
    def get_structured_output_model(self, role: str) -> type:
        """Get the structured output model for a specific role."""
        if "analyzer" in role:
            return FoxAndGeeseAnalysis
        else:
            return FoxAndGeeseMove


# Factory instance
fox_and_geese_factory = FoxAndGeeseEngineFactory()


def create_generic_fox_and_geese_engines(
    player_configs: Dict[str, PlayerAgentConfig]
) -> Dict[str, AugLLMConfig]:
    """Create FoxAndGeese engines from detailed player configurations.
    
    Args:
        player_configs: Dictionary mapping role names to player configurations
        
    Returns:
        Dict[str, AugLLMConfig]: Dictionary of FoxAndGeese engines
        
    Expected roles:
        - "fox_player": Player 1 configuration
        - "geese_player": Player 2 configuration
        - "fox_analyzer": Player 1 analyzer configuration
        - "geese_analyzer": Player 2 analyzer configuration
    """
    return fox_and_geese_factory.create_engines(player_configs)


def create_generic_fox_and_geese_engines_simple(
    fox_model: str,
    geese_model: str,
    temperature: float = 0.3
) -> Dict[str, AugLLMConfig]:
    """Create FoxAndGeese engines with simple model specifications.
    
    Args:
        fox_model: Model for fox and analyzer
        geese_model: Model for geese and analyzer
        temperature: Generation temperature
        
    Returns:
        Dict[str, AugLLMConfig]: Dictionary of FoxAndGeese engines
    """
    return create_engines_from_simple_configs(
        fox_and_geese_factory,
        fox_model,
        geese_model,
        temperature
    )


def create_generic_fox_and_geese_config_from_example(
    example_name: str,
    temperature: float = 0.3
) -> Dict[str, AugLLMConfig]:
    """Create FoxAndGeese engines from a predefined example configuration.
    
    Args:
        example_name: Name of the example configuration
        temperature: Generation temperature
        
    Returns:
        Dict[str, AugLLMConfig]: Dictionary of FoxAndGeese engines
        
    Available examples:
        - "gpt_vs_claude": GPT vs Claude
        - "gpt_only": GPT for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "advanced": High-powered models for strategic gameplay
    """
    examples = {
        "gpt_vs_claude": ("gpt-4o", "claude-3-5-sonnet-20240620"),
        "gpt_only": ("gpt-4o", "gpt-4o"),
        "claude_only": ("claude-3-5-sonnet-20240620", "claude-3-5-sonnet-20240620"),
        "budget": ("gpt-3.5-turbo", "claude-3-haiku"),
        "mixed": ("gpt-4o", "claude-3-opus"),
        "advanced": ("gpt-4o", "claude-3-opus"),
    }
    
    if example_name not in examples:
        available = ", ".join(examples.keys())
        raise ValueError(f"Unknown example '{example_name}'. Available: {available}")
    
    fox_model, geese_model = examples[example_name]
    return create_generic_fox_and_geese_engines_simple(
        fox_model, geese_model, temperature
    )


# Convenience functions for common configurations

def create_advanced_fox_and_geese_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create advanced FoxAndGeese engines with high-powered models."""
    return create_generic_fox_and_geese_config_from_example("advanced", **kwargs)


def create_budget_fox_and_geese_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create budget-friendly FoxAndGeese engines."""
    return create_generic_fox_and_geese_config_from_example("budget", **kwargs)


def create_mixed_fox_and_geese_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create mixed-provider FoxAndGeese engines."""
    return create_generic_fox_and_geese_config_from_example("mixed", **kwargs)
