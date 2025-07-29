"""Poker game module.

A complete implementation of Texas Hold'em poker using AI-powered players
that can analyze hands, make strategic betting decisions, and play competitive
multi-player poker games using large language models for decision making.

Key Components:
    PokerAgent: Main agent orchestrating LLM-powered poker gameplay
    PokerAgentConfig: Configuration for poker game parameters and engines
    PokerState: Game state management with betting rounds and community cards
    Card: Individual playing card representation with suit and value
    Hand: Player hand with cards and ranking evaluation
    Player: Player model with chips, actions, and betting history
    GamePhase: Enum for different poker game phases (preflop, flop, etc.)
    PlayerAction: Enum for poker actions (fold, call, raise, etc.)
    AgentDecision: Structured decision model for LLM poker decisions

Example:
    >>> from haive.games.poker import PokerAgent, PokerAgentConfig
    >>> config = PokerAgentConfig()
    >>> agent = PokerAgent(config)
    >>> result = agent.run_game()
"""

from haive.games.poker.agent import PokerAgent
from haive.games.poker.config import PokerAgentConfig
from haive.games.poker.models import (
    AgentDecision,
    Card,
    CardValue,
    GamePhase,
    GameResult,
    Hand,
    HandRank,
    Player,
    PlayerAction,
    Pot,
    Suit,
)
from haive.games.poker.state import PokerState

__all__ = [
    "AgentDecision",
    "Card",
    "CardValue",
    "GamePhase",
    "GameResult",
    "Hand",
    "HandRank",
    "Player",
    "PlayerAction",
    "PokerAgent",
    "PokerAgentConfig",
    "PokerState",
    "Pot",
    "Suit",
]
