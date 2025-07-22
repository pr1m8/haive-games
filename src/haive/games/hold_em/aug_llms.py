"""Texas Hold'em specialized augmented LLM configurations.

This module provides specialized augmented LLM configurations for Texas Hold'em poker,
with customized prompts, output schemas, and model configurations for different
aspects of poker gameplay:
    - Hand evaluation and analysis
    - Opponent modeling and profiling
    - Betting strategy and decision-making
    - Position-based play adaptation
    - Pot odds and equity calculations

These specialized configurations build on the base engines in engines.py but provide
more targeted capabilities for specific poker reasoning tasks.

Example:
    >>> from haive.games.hold_em.aug_llms import get_hand_analyzer, get_bluff_detector
    >>> from haive.core.engine.aug_llm import AugLLMConfig
    >>>
    >>> # Get a specialized hand analyzer
    >>> hand_analyzer = get_hand_analyzer("advanced")
    >>> result = hand_analyzer.invoke({
    >>>     "hole_cards": ["Ah", "Kh"],
    >>>     "community_cards": ["Qh", "Jh", "2s", "7c", "9d"],
    >>> })
"""

from langchain_core.prompts import ChatPromptTemplate

from .engine.aug_llm import AugLLMConfig
from .hold_em.models import (
    BettingDecision,
    GameSituationAnalysis,
    OpponentModel,
    PokerAnalysis,
    TableDynamics,
)
from .models.llm.base import AnthropicLLMConfig, AzureLLMConfig

# ============================================================================
# SPECIALIZED HAND ANALYZERS
# ============================================================================


def get_hand_analyzer(level: str = "standard") -> AugLLMConfig:
    """Get a specialized hand analyzer configuration.

    This function returns an augmented LLM configuration specialized for analyzing
    poker hands with different levels of sophistication:
    - basic: Simple hand strength evaluation
    - standard: Balanced analysis considering draws and relative strength
    - advanced: Sophisticated analysis with equity calculations and range analysis

    Args:
        level: Complexity level of the analyzer ("basic", "standard", or "advanced")

    Returns:
        AugLLMConfig: Configured hand analyzer
    """
    # Select model based on complexity level
    if level == "basic":
        model = AzureLLMConfig(model="gpt-4o-mini", temperature=0.3)
        description = "Basic poker hand analyzer"
    elif level == "advanced":
        model = AnthropicLLMConfig(model="claude-3-5-sonnet-20240620", temperature=0.4)
        description = "Advanced poker hand analyzer with equity calculations"
    else:  # standard
        model = AzureLLMConfig(model="gpt-4o", temperature=0.4)
        description = "Standard poker hand analyzer"

    # Create prompt with level-specific instructions
    base_instructions = """
    You are a professional poker hand analyzer. Evaluate the given hole cards
    and community cards to determine hand strength, potential, and optimal strategy.
    """

    level_specific = {
        "basic": """
        Focus on the basic hand ranking and simple board texture analysis.
        Identify made hands and obvious draws without complex calculations.
        """,
        "standard": """
        Analyze hand strength, drawing potential, and how the hand performs against
        likely opponent ranges. Consider position and betting patterns in your evaluation.
        """,
        "advanced": """
        Perform detailed equity calculations against opponent ranges. Analyze complex
        drawing scenarios, blockers, and implied odds. Consider multi-street strategy
        and how the hand will play on future board runouts.
        """,
    }

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                base_instructions
                + level_specific.get(level, level_specific["standard"]),
            ),
            (
                "human",
                "Hole cards: {hole_cards}\n"
                "Community cards: {community_cards}\n"
                "Game phase: {game_phase}\n"
                "Position: {position}\n"
                "Pot odds: {pot_odds}\n"
                "Players in hand: {players_in_hand}\n\n"
                "Provide a detailed analysis of this poker hand.",
            ),
        ]
    )

    return AugLLMConfig(
        name=f"poker_hand_analyzer_{level}",
        llm_config=model,
        prompt_template=prompt,
        structured_output_model=PokerAnalysis,
        force_tool_choice=True,
        description=description,
        structured_output_version="v1",
    )


# ============================================================================
# SPECIALIZED OPPONENT MODELERS
# ============================================================================


def get_opponent_profiler(tracking_depth: str = "standard") -> AugLLMConfig:
    """Get a specialized opponent profiling configuration.

    This function returns an augmented LLM configuration specialized for building
    opponent models with different levels of detail:
    - basic: Simple tracking of betting patterns
    - standard: Balanced profiling of play style and tendencies
    - deep: Sophisticated profiling with psychological modeling

    Args:
        tracking_depth: Depth of opponent tracking ("basic", "standard", or "deep")

    Returns:
        AugLLMConfig: Configured opponent profiler
    """
    # Select model based on tracking depth
    if tracking_depth == "basic":
        model = AzureLLMConfig(model="gpt-4o-mini", temperature=0.4)
        description = "Basic opponent profiler"
    elif tracking_depth == "deep":
        model = AnthropicLLMConfig(model="claude-3-5-sonnet-20240620", temperature=0.5)
        description = "Deep opponent profiler with psychological modeling"
    else:  # standard
        model = AzureLLMConfig(model="gpt-4o", temperature=0.4)
        description = "Standard opponent profiler"

    # Create prompt with depth-specific instructions
    base_instructions = """
    You are a poker opponent profiler who specializes in analyzing player behavior
    and tendencies. Build models of opponents based on their actions and patterns.
    """

    depth_specific = {
        "basic": """
        Focus on basic betting patterns: how often they bet, raise, or fold in different positions.
        Track simple statistics on aggression and position play.
        """,
        "standard": """
        Analyze betting patterns, positional tendencies, and hand selection. Identify exploitable
        leaks in their strategy and track their adaptation to your play over time.
        """,
        "deep": """
        Perform detailed psychological profiling including tilt detection, confidence assessment,
        and emotional state tracking. Analyze meta-game adaptations, level thinking, and build
        complex models of their decision-making process. Track their perception of other players.
        """,
    }

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                base_instructions
                + depth_specific.get(tracking_depth, depth_specific["standard"]),
            ),
            (
                "human",
                "Player: {player_name}\n"
                "Actions this session: {player_actions}\n"
                "Position tendencies: {position_data}\n"
                "Betting patterns: {betting_patterns}\n"
                "Showdown history: {showdown_data}\n\n"
                "Build a profile of this poker opponent.",
            ),
        ]
    )

    return AugLLMConfig(
        name=f"opponent_profiler_{tracking_depth}",
        llm_config=model,
        prompt_template=prompt,
        structured_output_model=OpponentModel,
        force_tool_choice=True,
        description=description,
        structured_output_version="v1",
    )


# ============================================================================
# SPECIALIZED DECISION MAKERS
# ============================================================================


def get_betting_strategist(style: str = "gto") -> AugLLMConfig:
    """Get a specialized betting strategy configuration.

    This function returns an augmented LLM configuration specialized for making
    betting decisions with different strategic approaches:
    - gto: Game Theory Optimal balanced approach
    - exploitative: Adjusts to exploit opponent tendencies
    - aggressive: Higher variance, aggressive betting strategy
    - conservative: Lower variance, tighter betting strategy

    Args:
        style: Strategic style ("gto", "exploitative", "aggressive", or "conservative")

    Returns:
        AugLLMConfig: Configured betting strategist
    """
    # Select model and temperature based on style
    if style == "exploitative":
        model = AnthropicLLMConfig(model="claude-3-5-sonnet-20240620", temperature=0.6)
        description = "Exploitative betting strategist"
    elif style == "aggressive":
        model = AzureLLMConfig(model="gpt-4o", temperature=0.8)  # Higher variance
        description = "Aggressive betting strategist"
    elif style == "conservative":
        model = AzureLLMConfig(model="gpt-4o", temperature=0.3)  # Lower variance
        description = "Conservative betting strategist"
    else:  # gto
        model = AzureLLMConfig(model="gpt-4o", temperature=0.5)
        description = "GTO-based betting strategist"

    # Create prompt with style-specific instructions
    base_instructions = """
    You are a poker betting strategist responsible for making optimal betting decisions.
    Analyze the current situation and decide on the best betting action.
    """

    style_specific = {
        "gto": """
        Follow Game Theory Optimal principles to create a balanced, unexploitable strategy.
        Use appropriate bet sizing that balances your range and consider optimal frequencies
        for different actions. Don't be predictable or exploitable.
        """,
        "exploitative": """
        Focus on exploiting the specific tendencies of your opponents. Adapt your strategy
        to take advantage of their weaknesses and adjust as they adapt. Prioritize maximum
        expected value over balanced play when you have strong reads.
        """,
        "aggressive": """
        Adopt an aggressive betting strategy that puts pressure on opponents. Use more frequent
        bets and raises, and be willing to bluff more often. Take calculated risks to win bigger pots.
        """,
        "conservative": """
        Prioritize risk management and variance reduction. Play more selectively and focus on
        value betting with strong hands. Bluff less frequently and fold marginal holdings.
        """,
    }

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                base_instructions + style_specific.get(style, style_specific["gto"]),
            ),
            (
                "human",
                "Hole cards: {hole_cards}\n"
                "Community cards: {community_cards}\n"
                "Game phase: {phase}\n"
                "Position: {position}\n"
                "Current bet: {current_bet}\n"
                "Pot size: {pot}\n"
                "Your chips: {chips}\n"
                "Players in hand: {players_in_hand}\n"
                "Hand analysis: {hand_analysis}\n"
                "Opponent analysis: {opponent_analysis}\n"
                "Available actions: {available_actions}\n\n"
                "Make your betting decision with detailed reasoning.",
            ),
        ]
    )

    return AugLLMConfig(
        name=f"betting_strategist_{style}",
        llm_config=model,
        prompt_template=prompt,
        structured_output_model=BettingDecision,
        force_tool_choice=True,
        description=description,
        structured_output_version="v1",
    )


# ============================================================================
# SPECIALIZED SITUATION ANALYZERS
# ============================================================================


def get_situation_analyzer(focus: str = "general") -> AugLLMConfig:
    """Get a specialized situation analyzer configuration.

    This function returns an augmented LLM configuration specialized for analyzing
    poker game situations with different focus areas:
    - general: Balanced analysis of the overall situation
    - positional: Focus on positional dynamics and advantages
    - tournament: Specialized for tournament situations with ICM considerations
    - cash_game: Specialized for cash game dynamics

    Args:
        focus: Analysis focus ("general", "positional", "tournament", or "cash_game")

    Returns:
        AugLLMConfig: Configured situation analyzer
    """
    # Select model based on focus area
    if focus == "tournament":
        model = AnthropicLLMConfig(model="claude-3-5-sonnet-20240620", temperature=0.4)
        description = "Tournament situation analyzer with ICM considerations"
    else:  # general, positional, cash_game
        model = AzureLLMConfig(model="gpt-4o", temperature=0.4)
        description = f"{focus.capitalize()} poker situation analyzer"

    # Create prompt with focus-specific instructions
    base_instructions = """
    You are a poker situation analyzer who assesses the current game state and provides
    strategic insights based on position, stack sizes, and game dynamics.
    """

    focus_specific = {
        "general": """
        Analyze the overall poker situation considering pot odds, positions, stack depths,
        and table dynamics. Provide a balanced assessment of the current state.
        """,
        "positional": """
        Focus heavily on positional dynamics and advantages. Analyze how position affects
        optimal strategy, hand selection, and betting patterns. Consider stack-to-pot ratios
        and leverage based on position.
        """,
        "tournament": """
        Analyze the tournament situation with ICM (Independent Chip Model) considerations.
        Consider pay jumps, bubble factors, stack preservation, and chip accumulation phases.
        Factor in blind levels and tournament stage.
        """,
        "cash_game": """
        Focus on cash game dynamics including table selection, stack depth considerations,
        and long-term profitability. Analyze how to maximize value and minimize variance
        over an extended session.
        """,
    }

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                base_instructions
                + focus_specific.get(focus, focus_specific["general"]),
            ),
            (
                "human",
                "Player position: {player_position}\n"
                "Pot size: {pot_size}\n"
                "Current bet: {current_bet}\n"
                "Player chips: {player_chips}\n"
                "Players in hand: {players_in_hand}\n"
                "Game phase: {game_phase}\n"
                "Community cards: {community_cards}\n"
                "Recent actions: {recent_actions}\n"
                "Stack sizes: {stack_sizes}\n\n"
                "Provide a comprehensive analysis of this poker situation.",
            ),
        ]
    )

    return AugLLMConfig(
        name=f"situation_analyzer_{focus}",
        llm_config=model,
        prompt_template=prompt,
        structured_output_model=GameSituationAnalysis,
        force_tool_choice=True,
        description=description,
        structured_output_version="v1",
    )


# ============================================================================
# SPECIALIZED BLUFF DETECTION
# ============================================================================


def get_bluff_detector(sensitivity: str = "balanced") -> AugLLMConfig:
    """Get a specialized bluff detection configuration.

    This function returns an augmented LLM configuration specialized for detecting
    opponent bluffs with different sensitivity levels:
    - conservative: Lower false positive rate, only identifies clear bluffs
    - balanced: Moderate sensitivity to bluffing signals
    - aggressive: Higher sensitivity, may have more false positives

    Args:
        sensitivity: Bluff detection sensitivity ("conservative", "balanced", or "aggressive")

    Returns:
        AugLLMConfig: Configured bluff detector
    """
    # Select model and parameters based on sensitivity
    if sensitivity == "conservative":
        model = AzureLLMConfig(model="gpt-4o", temperature=0.3)
        description = "Conservative bluff detector"
    elif sensitivity == "aggressive":
        model = AnthropicLLMConfig(model="claude-3-5-sonnet-20240620", temperature=0.6)
        description = "Aggressive bluff detector"
    else:  # balanced
        model = AzureLLMConfig(model="gpt-4o", temperature=0.4)
        description = "Balanced bluff detector"

    # Create prompt with sensitivity-specific instructions
    base_instructions = """
    You are a poker bluff detector who analyzes betting patterns, timing, and bet sizing
    to determine if an opponent is likely bluffing.
    """

    sensitivity_specific = {
        "conservative": """
        Be conservative in your bluff detection. Only flag clear bluffs with strong evidence.
        Prioritize avoiding false positives, even if it means missing some bluffs.
        Require multiple strong indicators before concluding a player is bluffing.
        """,
        "balanced": """
        Take a balanced approach to bluff detection. Weigh betting patterns, timing tells,
        and board texture equally. Consider the player's history and tendencies when
        evaluating potential bluffs.
        """,
        "aggressive": """
        Be aggressive in your bluff detection. Flag potential bluffs even with limited evidence.
        It's better to catch all possible bluffs even if it means some false positives.
        Pay special attention to subtle timing tells and unusual bet sizing.
        """,
    }

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                base_instructions
                + sensitivity_specific.get(
                    sensitivity, sensitivity_specific["balanced"]
                ),
            ),
            (
                "human",
                "Player: {player_name}\n"
                "Betting pattern: {betting_pattern}\n"
                "Board texture: {board_texture}\n"
                "Player history: {player_history}\n"
                "Timing notes: {timing_notes}\n"
                "Bet sizing: {bet_sizing}\n\n"
                "Analyze whether this player is likely bluffing.",
            ),
        ]
    )

    # Custom output model for bluff detection
    class BluffDetectionResult(OpponentModel):
        bluff_probability: float
        confidence: float
        key_indicators: list[str]
        recommended_action: str

    return AugLLMConfig(
        name=f"bluff_detector_{sensitivity}",
        llm_config=model,
        prompt_template=prompt,
        structured_output_model=BluffDetectionResult,
        force_tool_choice=True,
        description=description,
        structured_output_version="v1",
    )


# ============================================================================
# SPECIALIZED TABLE DYNAMICS ANALYZER
# ============================================================================


def get_table_dynamics_analyzer() -> AugLLMConfig:
    """Get a specialized table dynamics analyzer configuration.

    This function returns an augmented LLM configuration specialized for analyzing
    overall poker table dynamics, player interactions, and meta-game considerations.

    Returns:
        AugLLMConfig: Configured table dynamics analyzer
    """
    model = AzureLLMConfig(model="gpt-4o", temperature=0.5)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
        You are a poker table dynamics analyzer who specializes in understanding the
        complex interactions between players at a poker table. Analyze player types,
        table image, chip distribution, and meta-game elements.

        Provide insights on:
        - Table aggression level
        - Power dynamics between players
        - Chip distribution implications
        - Meta-game considerations
        - Table image management
        - Exploitable dynamics
        """,
            ),
            (
                "human",
                "Table lineup: {player_list}\n"
                "Chip distribution: {chip_distribution}\n"
                "Recent hands summary: {recent_hands}\n"
                "Playing styles observed: {player_styles}\n"
                "Current dynamics: {current_dynamics}\n\n"
                "Provide a comprehensive analysis of the table dynamics.",
            ),
        ]
    )

    return AugLLMConfig(
        name="table_dynamics_analyzer",
        llm_config=model,
        prompt_template=prompt,
        structured_output_model=TableDynamics,
        force_tool_choice=True,
        description="Poker table dynamics analyzer",
        structured_output_version="v1",
    )


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================


def get_complete_llm_suite(player_style: str = "balanced") -> dict[str, AugLLMConfig]:
    """Get a complete suite of specialized LLMs for a poker player.

    This function creates a coordinated set of specialized LLM configurations
    that work well together based on a player's overall style.

    Args:
        player_style: Overall player style ("tight", "loose", "aggressive",
                      "passive", "balanced", or "tricky")

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of specialized LLM configurations
    """
    # Map player styles to specialized configurations
    style_map = {
        "tight": {
            "hand_analyzer": get_hand_analyzer("standard"),
            "opponent_profiler": get_opponent_profiler("standard"),
            "betting_strategist": get_betting_strategist("conservative"),
            "situation_analyzer": get_situation_analyzer("general"),
            "bluff_detector": get_bluff_detector("conservative"),
        },
        "loose": {
            "hand_analyzer": get_hand_analyzer("basic"),
            "opponent_profiler": get_opponent_profiler("basic"),
            "betting_strategist": get_betting_strategist("aggressive"),
            "situation_analyzer": get_situation_analyzer("general"),
            "bluff_detector": get_bluff_detector("aggressive"),
        },
        "aggressive": {
            "hand_analyzer": get_hand_analyzer("standard"),
            "opponent_profiler": get_opponent_profiler("standard"),
            "betting_strategist": get_betting_strategist("aggressive"),
            "situation_analyzer": get_situation_analyzer("positional"),
            "bluff_detector": get_bluff_detector("balanced"),
        },
        "passive": {
            "hand_analyzer": get_hand_analyzer("advanced"),
            "opponent_profiler": get_opponent_profiler("deep"),
            "betting_strategist": get_betting_strategist("conservative"),
            "situation_analyzer": get_situation_analyzer("general"),
            "bluff_detector": get_bluff_detector("conservative"),
        },
        "balanced": {
            "hand_analyzer": get_hand_analyzer("advanced"),
            "opponent_profiler": get_opponent_profiler("standard"),
            "betting_strategist": get_betting_strategist("gto"),
            "situation_analyzer": get_situation_analyzer("general"),
            "bluff_detector": get_bluff_detector("balanced"),
        },
        "tricky": {
            "hand_analyzer": get_hand_analyzer("advanced"),
            "opponent_profiler": get_opponent_profiler("deep"),
            "betting_strategist": get_betting_strategist("exploitative"),
            "situation_analyzer": get_situation_analyzer("positional"),
            "bluff_detector": get_bluff_detector("aggressive"),
        },
    }

    # Add table dynamics analyzer to all configurations
    suite = style_map.get(player_style, style_map["balanced"])
    suite["table_dynamics"] = get_table_dynamics_analyzer()

    # Rename engines to standard names expected by the player agent
    return {
        "situation_analyzer": suite["situation_analyzer"],
        "hand_analyzer": suite["hand_analyzer"],
        "opponent_analyzer": suite["opponent_profiler"],
        "decision_maker": suite["betting_strategist"],
        "bluff_detector": suite["bluff_detector"],
        "table_analyzer": suite["table_dynamics"],
    }
