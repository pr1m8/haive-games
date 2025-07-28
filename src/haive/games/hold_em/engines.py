"""Texas Hold'em engines and prompts module - FIXED VERSION.

This module provides LLM configurations and prompts for Hold'em agents.
Fixed variable naming consistency issues.
"""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AnthropicLLMConfig, AzureLLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.hold_em.models import (
    BettingDecision,
    GameSituationAnalysis,
    OpponentModel,
    PokerAnalysis,
)

# ============================================================================
# PLAYER DECISION PROMPTS
# ============================================================================


def create_player_decision_prompt(player_style: str = "balanced") -> ChatPromptTemplate:
    """Create a decision-making prompt based on player style."""
    style_instructions = {
        "tight": "You are a TIGHT player. You play few hands but play them aggressively. "
        "Only enter pots with strong hands (top 15% of hands). Fold weak hands quickly.",
        "loose": "You are a LOOSE player. You play many hands and like to see flops. "
        "You're willing to play weaker hands and chase draws. Take more risks.",
        "aggressive": "You are an AGGRESSIVE player. You bet and raise frequently. "
        "You use aggression to win pots and put pressure on opponents. Bluff selectively.",
        "passive": "You are a PASSIVE player. You prefer to call rather than bet or raise. "
        "You let others lead the action and look for strong hands to win big pots.",
        "balanced": "You are a BALANCED player. You mix up your play style based on position, "
        "opponents, and game situation. Adapt your strategy dynamically.",
        "tricky": "You are a TRICKY player. You use deception, varying bet sizes, and "
        "unconventional plays to confuse opponents. Mix up your timing and sizing.",
    }

    style_instruction = style_instructions.get(
        player_style, style_instructions["balanced"]
    )

    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"You are playing Texas Hold'em poker. {style_instruction}\n\n"
                "DECISION RULES:\n"
                "- Consider your hole cards, community cards, position, and pot odds\n"
                "- Factor in opponent behavior and betting patterns\n"
                "- Choose from: fold, check, call, bet, raise, all_in\n"
                "- Provide bet/raise amounts when applicable\n"
                "- Give clear reasoning for your decision\n\n"
                "BETTING GUIDELINES:\n"
                "- Value bet when you have a strong hand\n"
                "- Bluff when you have fold equity\n"
                "- Consider pot odds when drawing\n"
                "- Adjust bet sizing based on board texture\n",
            ),
            (
                "human",
                "GAME SITUATION:\n"
                "Your hole cards: {hole_cards}\n"
                "Community cards: {community_cards}\n"
                "Game phase: {phase}\n"
                "Your position: {position}\n"
                "Your chips: {chips}\n"
                "Current bet to call: {current_bet}\n"
                "Pot size: {pot}\n"
                "Players in hand: {players_in_hand}\n\n"
                "ANALYSIS DATA:\n"
                "Situation analysis: {situation_analysis}\n"
                "Hand analysis: {hand_analysis}\n"
                "Opponent analysis: {opponent_analysis}\n\n"
                "AVAILABLE ACTIONS: {available_actions}\n"
                "Your playing style: {player_style}\n"
                "Risk tolerance: {risk_tolerance}\n\n"
                "Make your decision and explain your reasoning.",
            ),
        ]
    )


# ============================================================================
# ANALYSIS PROMPTS - FIXED VARIABLE NAMES
# ============================================================================

situation_analysis_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are analyzing the current poker game situation. Evaluate:\n"
            "- Stack sizes and their implications\n"
            "- Position advantages/disadvantages\n"
            "- Betting action and what it suggests\n"
            "- Stage of the hand and how it affects play\n"
            "- Pot odds and implied odds\n",
        ),
        (
            "human",
            "CURRENT SITUATION ANALYSIS:\n"
            "Your position: {player_position}\n"
            "Pot size: {pot_size}\n"
            "Current bet: {current_bet}\n"
            "Your chips: {player_chips}\n"
            "Players in hand: {players_in_hand}\n"
            "Game phase: {game_phase}\n"
            "Community cards: {community_cards}\n"
            "Recent actions: {recent_actions}\n"
            "Stack sizes: {stack_sizes}\n\n"
            "Analyze this poker situation comprehensively. Consider position dynamics, "
            "stack-to-pot ratios, betting patterns, and strategic implications.",
        ),
    ]
)

hand_analysis_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are analyzing poker hand strength. Evaluate:\n"
            "- Current hand strength (made hands, draws)\n"
            "- Potential to improve on future streets\n"
            "- Hand range vs likely opponent ranges\n"
            "- Nut potential and relative strength\n"
            "- Pot odds and equity calculations\n",
        ),
        (
            "human",
            "HAND STRENGTH ANALYSIS:\n"
            "Your hole cards: {hole_cards}\n"
            "Community cards: {community_cards}\n"
            "Game phase: {game_phase}\n"
            "Number of opponents: {num_opponents}\n"
            "Pot odds: {pot_odds}\n"
            "Current bet to call: {current_bet}\n"
            "Pot size: {pot_size}\n\n"
            "Analyze your hand strength comprehensively. Include equity calculations, "
            "draw potential, and relative strength against likely opponent ranges.",
        ),
    ]
)

opponent_analysis_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are analyzing opponent behavior in poker. Look for:\n"
            "- Betting patterns and sizing tells\n"
            "- Position-based tendencies\n"
            "- Aggression levels and frequency\n"
            "- Likely hand ranges based on actions\n"
            "- Exploitable tendencies\n",
        ),
        (
            "human",
            "OPPONENT BEHAVIOR ANALYSIS:\n"
            "Opponents in hand: {opponents}\n"
            "Betting pattern this hand: {betting_pattern}\n"
            "Game phase: {game_phase}\n"
            "Community cards: {community_cards}\n"
            "Position dynamics: {position_info}\n"
            "Stack sizes: {stack_sizes}\n\n"
            "Analyze opponent tendencies, likely hand ranges, and exploitable patterns. "
            "Consider their betting behavior and position-based play.",
        ),
    ]
)


# ============================================================================
# ENGINE BUILDERS - FIXED
# ============================================================================


def build_player_engines(
    player_name: str, player_style: str, heads_up: bool = False
) -> dict[str, AugLLMConfig]:
    """Build LLM engines for a player agent."""
    # Adjust model selection based on complexity needs
    if heads_up:
        # Use more powerful models for heads-up play
        decision_model = AnthropicLLMConfig(
            model="claude-3-5-sonnet-20240620", temperature=0.7
        )
        analysis_model = AzureLLMConfig(model="gpt-4o", temperature=0.6)
    else:
        # Standard models for multi-way play
        decision_model = AzureLLMConfig(model="gpt-4o", temperature=0.7)
        analysis_model = AzureLLMConfig(model="gpt-4o", temperature=0.6)

    return {
        "situation_analyzer": AugLLMConfig(
            name=f"{player_name}_situation_analyzer",
            llm_config=analysis_model,
            prompt_template=situation_analysis_prompt,
            structured_output_model=GameSituationAnalysis,
            description=f"Situation analyzer for {player_name}",
            structured_output_version="v1",
        ),
        "hand_analyzer": AugLLMConfig(
            name=f"{player_name}_hand_analyzer",
            llm_config=analysis_model,
            prompt_template=hand_analysis_prompt,
            structured_output_model=PokerAnalysis,
            force_tool_choice=True,
            description=f"Hand analyzer for {player_name}",
            structured_output_version="v1",
        ),
        "opponent_analyzer": AugLLMConfig(
            name=f"{player_name}_opponent_analyzer",
            llm_config=analysis_model,
            prompt_template=opponent_analysis_prompt,
            structured_output_model=OpponentModel,
            description=f"Opponent analyzer for {player_name}",
            structured_output_version="v1",
        ),
        "decision_maker": AugLLMConfig(
            name=f"{player_name}_decision_maker",
            llm_config=decision_model,
            prompt_template=create_player_decision_prompt(player_style),
            structured_output_model=BettingDecision,
            description=f"Decision maker for {player_name} ({player_style} style)",
            structured_output_version="v1",
        ),
    }


def build_holdem_game_engines() -> dict[str, AugLLMConfig]:
    """Build engines for the main game agent."""
    # Game management engines (if needed for complex decisions)
    base_model = AzureLLMConfig(model="gpt-4o-mini", temperature=0.3)

    return {
        "game_narrator": AugLLMConfig(
            name="holdem_game_narrator",
            llm_config=base_model,
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        "You narrate poker games, describing key moments and decisions.",
                    ),
                    ("human", "Describe this poker situation: {situation}"),
                ]
            ),
            description="Game narration and commentary",
        ),
        "hand_evaluator": AugLLMConfig(
            name="holdem_hand_evaluator",
            llm_config=base_model,
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        "You evaluate poker hands and determine winners at showdown.",
                    ),
                    ("human", "Evaluate these hands: {hands_to_evaluate}"),
                ]
            ),
            description="Hand evaluation for showdowns",
            structured_output_version="v1",
            structured_output_model=PokerAnalysis,
            force_tool_choice=True,
        ),
    }


# ============================================================================
# SPECIALIZED PROMPTS FOR DIFFERENT SITUATIONS
# ============================================================================

preflop_decision_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are making a PREFLOP decision in Texas Hold'em. Consider:\n"
            "- Hand strength relative to position\n"
            "- Stack sizes and effective stacks\n"
            "- Opponent tendencies and ranges\n"
            "- Table dynamics and image\n"
            "- ICM considerations (if tournament)\n",
        ),
        (
            "human",
            "PREFLOP DECISION CONTEXT:\n"
            "Hole cards: {hole_cards}\n"
            "Position: {position}\n"
            "Action before you: {action_before}\n"
            "Players behind: {players_behind}\n"
            "Your stack: {stack}\n"
            "Blinds: {blinds}\n"
            "Game phase: {game_phase}\n"
            "Players in hand: {players_in_hand}\n\n"
            "Make your preflop decision based on position, hand strength, and opponent action.",
        ),
    ]
)

postflop_decision_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are making a POSTFLOP decision in Texas Hold'em. Consider:\n"
            "- Board texture and how it hits ranges\n"
            "- Your hand strength and potential\n"
            "- Opponent's likely holdings\n"
            "- Pot odds and implied odds\n"
            "- Position and initiative\n",
        ),
        (
            "human",
            "POSTFLOP DECISION CONTEXT:\n"
            "Hole cards: {hole_cards}\n"
            "Community cards: {community_cards}\n"
            "Game phase: {game_phase}\n"
            "Position: {position}\n"
            "Pot size: {pot_size}\n"
            "Current bet: {current_bet}\n"
            "Effective stack: {effective_stack}\n"
            "Action this street: {action_this_street}\n"
            "Hand analysis: {hand_analysis}\n"
            "Players in hand: {players_in_hand}\n\n"
            "Make your postflop decision considering board texture, hand strength, and position.",
        ),
    ]
)

tournament_decision_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are playing in a TOURNAMENT. Consider ICM implications:\n"
            "- Survival vs chip accumulation\n"
            "- Stack sizes relative to blinds\n"
            "- Bubble factors and pay jumps\n"
            "- Risk vs reward in tournament context\n"
            "- Opponent stack sizes and desperation\n",
        ),
        (
            "human",
            "TOURNAMENT DECISION CONTEXT:\n"
            "Your stack: {stack}\n"
            "Average stack: {average_stack}\n"
            "Blinds: {blinds}\n"
            "Players remaining: {players_remaining}\n"
            "Prize structure: {prize_structure}\n"
            "Bubble distance: {bubble_distance}\n"
            "Game situation: {game_situation}\n"
            "Hole cards: {hole_cards}\n"
            "Community cards: {community_cards}\n"
            "Position: {position}\n\n"
            "Make your tournament decision considering ICM and survival factors.",
        ),
    ]
)


def create_style_specific_engines(player_style: str) -> dict[str, AugLLMConfig]:
    """Create engines optimized for specific playing styles."""
    if player_style == "aggressive":
        temp = 0.8  # Higher variance for aggressive play
        model = AnthropicLLMConfig(model="claude-3-5-sonnet-20240620", temperature=temp)
    elif player_style == "tight":
        temp = 0.4  # Lower variance for tight play
        model = AzureLLMConfig(model="gpt-4o", temperature=temp)
    elif player_style == "loose":
        temp = 0.9  # Higher variance for loose play
        model = AzureLLMConfig(model="gpt-4o", temperature=temp)
    else:
        temp = 0.7  # Balanced temperature
        model = AzureLLMConfig(model="gpt-4o", temperature=temp)

    return {
        "preflop_specialist": AugLLMConfig(
            name=f"{player_style}_preflop_specialist",
            llm_config=model,
            prompt_template=preflop_decision_prompt,
            structured_output_model=BettingDecision,
            force_tool_choice=True,
            structured_output_version="v1",
            description=f"Preflop specialist for {player_style} style",
        ),
        "postflop_specialist": AugLLMConfig(
            name=f"{player_style}_postflop_specialist",
            llm_config=model,
            prompt_template=postflop_decision_prompt,
            structured_output_model=BettingDecision,
            force_tool_choice=True,
            structured_output_version="v1",
            description=f"Postflop specialist for {player_style} style",
        ),
    }


# ============================================================================
# CONTEXT PREPARATION HELPERS
# ============================================================================


def prepare_situation_context(game_state, player) -> dict[str, str]:
    """Prepare context dictionary for situation analysis with correct variable
    names."""
    return {
        "player_position": player.position,
        "pot_size": str(game_state.pot_size),
        "current_bet": str(game_state.current_bet),
        "player_chips": str(player.chips),
        "players_in_hand": str(game_state.players_in_hand),
        "game_phase": game_state.phase,
        "community_cards": str(game_state.community_cards),
        "recent_actions": str(game_state.recent_actions),
        "stack_sizes": str(game_state.stack_sizes),
    }


def prepare_hand_context(game_state, player) -> dict[str, str]:
    """Prepare context dictionary for hand analysis."""
    return {
        "hole_cards": str(player.hole_cards),
        "community_cards": str(game_state.community_cards),
        "game_phase": game_state.phase,
        "num_opponents": str(len(game_state.players_in_hand) - 1),
        "pot_odds": str(game_state.calculate_pot_odds()),
        "current_bet": str(game_state.current_bet),
        "pot_size": str(game_state.pot_size),
    }


def prepare_opponent_context(game_state, opponents) -> dict[str, str]:
    """Prepare context dictionary for opponent analysis."""
    return {
        "opponents": str([opp.name for opp in opponents]),
        "betting_pattern": str(game_state.betting_pattern),
        "game_phase": game_state.phase,
        "community_cards": str(game_state.community_cards),
        "position_info": str(game_state.position_info),
        "stack_sizes": str(game_state.stack_sizes),
    }


def prepare_decision_context(game_state, player, analyses) -> dict[str, str]:
    """Prepare context dictionary for final decision making."""
    return {
        "hole_cards": str(player.hole_cards),
        "community_cards": str(game_state.community_cards),
        "phase": game_state.phase,
        "position": player.position,
        "chips": str(player.chips),
        "current_bet": str(game_state.current_bet),
        "pot": str(game_state.pot_size),
        "players_in_hand": str(game_state.players_in_hand),
        "situation_analysis": str(analyses.get("situation", "No analysis available")),
        "hand_analysis": str(analyses.get("hand", "No analysis available")),
        "opponent_analysis": str(analyses.get("opponent", "No analysis available")),
        "available_actions": str(game_state.available_actions),
        "player_style": player.style,
        "risk_tolerance": str(player.risk_tolerance),
    }
