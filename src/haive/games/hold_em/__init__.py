"""Texas Hold'em poker game implementation module.

This package provides a complete implementation of the Texas Hold'em poker game, including:
    - Game agent with LLM-powered players
    - State management with betting rounds
    - Hand evaluation and ranking
    - Player decision-making
    - Game visualization
    - Specialized LLM configurations

Example:
    >>> from haive.games.hold_em import HoldemGameAgent, HoldemGameAgentConfig
    >>>
    >>> # Create and configure a Hold'em game agent
    >>> config = HoldemGameAgentConfig(max_players=4, starting_chips=1000)
    >>> agent = HoldemGameAgent(config)
"""

from haive.games.hold_em.aug_llms import (
    get_betting_strategist,
    get_bluff_detector,
    get_complete_llm_suite,
    get_hand_analyzer,
    get_opponent_profiler,
    get_situation_analyzer,
    get_table_dynamics_analyzer,
)
from haive.games.hold_em.config import (
    HoldemGameSettings,
    create_cash_game_config,
    create_custom_holdem_config,
    create_default_holdem_config,
    create_heads_up_config,
    create_tournament_config,
)
from haive.games.hold_em.game_agent import HoldemGameAgent, HoldemGameAgentConfig
from haive.games.hold_em.models import (
    BettingDecision,
    GameSituationAnalysis,
    HandEvaluation,
    HandRank,
    OpponentModel,
    PlayerDecisionModel,
    PokerAction,
    PokerAnalysis,
    PokerCard,
    PokerHandHistory,
    TableDynamics,
)
from haive.games.hold_em.player_agent import HoldemPlayerAgent, HoldemPlayerAgentConfig
from haive.games.hold_em.state import (
    GamePhase,
    HoldemState,
    PlayerAction,
    PlayerDecision,
    PlayerState,
    PlayerStatus,
)
from haive.games.hold_em.state_manager import HoldemGameStateManager
from haive.games.hold_em.ui import HoldemRichUI

__all__ = [
    # Game agent and configuration
    "HoldemGameAgent",
    "HoldemGameAgentConfig",
    "HoldemPlayerAgent",
    "HoldemPlayerAgentConfig",
    # Configuration helpers
    "HoldemGameSettings",
    "create_default_holdem_config",
    "create_cash_game_config",
    "create_tournament_config",
    "create_heads_up_config",
    "create_custom_holdem_config",
    # State management
    "HoldemState",
    "PlayerState",
    "PlayerStatus",
    "GamePhase",
    "HoldemGameStateManager",
    # Actions and decisions
    "PlayerAction",
    "PlayerDecision",
    "PokerAction",
    # Models
    "HandRank",
    "PokerCard",
    "HandEvaluation",
    "PlayerDecisionModel",
    "PokerAnalysis",
    "GameSituationAnalysis",
    "BettingDecision",
    "OpponentModel",
    "PokerHandHistory",
    "TableDynamics",
    # Specialized LLM configurations
    "get_hand_analyzer",
    "get_opponent_profiler",
    "get_betting_strategist",
    "get_situation_analyzer",
    "get_bluff_detector",
    "get_table_dynamics_analyzer",
    "get_complete_llm_suite",
    # UI
    "HoldemRichUI",
]
