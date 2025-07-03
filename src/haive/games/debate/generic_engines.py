"""Generic Debate engine creation using the generic player agent system.

This module provides generic engine creation functions for Debate games,
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
from haive.games.debate.models import (
    Statement,
    Topic,
)


class DebatePlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Player identifiers for Debate game."""
    
    def __init__(self):
        super().__init__(
            player1="debater1",
            player2="debater2"
        )


class DebatePromptGenerator(GenericPromptGenerator[str, str]):
    """Prompt generator for Debate game."""
    
    def create_move_prompt(self, player: str) -> ChatPromptTemplate:
        """Create move prompt for Debate player."""
        return ChatPromptTemplate.from_messages([
            (
                "system",
                f"You are {player} in a Debate game. You are a debater in a structured debate. Your goal is to present compelling arguments and counter-arguments to win the debate.\n\n"
                "As a Debate player:\n"
                "- Present clear, logical arguments with supporting evidence"
                "- Listen carefully to opponent's points and identify weaknesses"
                "- Use rhetorical techniques to strengthen your position"
                "- Stay focused on the debate topic and avoid ad hominem attacks"
                "- Build upon previous arguments to create a cohesive case"\n\n"
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
        """Create analysis prompt for Debate game state."""
        return ChatPromptTemplate.from_messages([
            (
                "system",
                f"You are an expert Debate strategist analyzing the current game state for {player}.\n\n"
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


class DebateEngineFactory(GenericGameEngineFactory[str, str]):
    """Factory for creating Debate game engines."""
    
    def __init__(self):
        identifiers = DebatePlayerIdentifiers()
        prompt_generator = DebatePromptGenerator()
        super().__init__(identifiers, prompt_generator)
    
    def get_structured_output_model(self, role: str) -> type:
        """Get the structured output model for a specific role."""
        if "analyzer" in role:
            return Topic
        else:
            return Statement


# Factory instance
debate_factory = DebateEngineFactory()


def create_generic_debate_engines(
    player_configs: Dict[str, PlayerAgentConfig]
) -> Dict[str, AugLLMConfig]:
    """Create Debate engines from detailed player configurations.
    
    Args:
        player_configs: Dictionary mapping role names to player configurations
        
    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Debate engines
        
    Expected roles:
        - "debater1_player": Player 1 configuration
        - "debater2_player": Player 2 configuration
        - "debater1_analyzer": Player 1 analyzer configuration
        - "debater2_analyzer": Player 2 analyzer configuration
    """
    return debate_factory.create_engines(player_configs)


def create_generic_debate_engines_simple(
    debater1_model: str,
    debater2_model: str,
    temperature: float = 0.3
) -> Dict[str, AugLLMConfig]:
    """Create Debate engines with simple model specifications.
    
    Args:
        debater1_model: Model for debater1 and analyzer
        debater2_model: Model for debater2 and analyzer
        temperature: Generation temperature
        
    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Debate engines
    """
    return create_engines_from_simple_configs(
        debate_factory,
        debater1_model,
        debater2_model,
        temperature
    )


def create_generic_debate_config_from_example(
    example_name: str,
    temperature: float = 0.3
) -> Dict[str, AugLLMConfig]:
    """Create Debate engines from a predefined example configuration.
    
    Args:
        example_name: Name of the example configuration
        temperature: Generation temperature
        
    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Debate engines
        
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
    
    debater1_model, debater2_model = examples[example_name]
    return create_generic_debate_engines_simple(
        debater1_model, debater2_model, temperature
    )


# Convenience functions for common configurations

def create_advanced_debate_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create advanced Debate engines with high-powered models."""
    return create_generic_debate_config_from_example("advanced", **kwargs)


def create_budget_debate_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create budget-friendly Debate engines."""
    return create_generic_debate_config_from_example("budget", **kwargs)


def create_mixed_debate_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create mixed-provider Debate engines."""
    return create_generic_debate_config_from_example("mixed", **kwargs)
