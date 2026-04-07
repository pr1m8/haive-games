"""LangGraph Platform graph entry points for haive-games.

This module exposes all game agent graphs as callable factories for
LangGraph Platform (langgraph.json). Each function returns a compiled
LangGraph StateGraph served via ``langgraph dev`` or LangGraph Cloud.

All 22 games listed here can be instantiated with default configuration.
"""

import logging

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _game(agent_cls, config_cls, **config_kwargs):
    """Create a game agent with analysis/visualization disabled."""
    defaults = {"enable_analysis": False, "visualize": False}
    defaults.update(config_kwargs)
    try:
        config = config_cls(**defaults)
    except Exception:
        # Some configs don't accept all kwargs
        config = config_cls()
    return agent_cls(config).app


# ---------------------------------------------------------------------------
# Standard Two-Player Board Games
# ---------------------------------------------------------------------------

def tic_tac_toe():
    """Tic-Tac-Toe: AI vs AI on a 3x3 grid."""
    from haive.games.tic_tac_toe.agent import TicTacToeAgent
    from haive.games.tic_tac_toe.config import TicTacToeConfig
    return _game(TicTacToeAgent, TicTacToeConfig)


def chess():
    """Chess: AI vs AI standard chess."""
    from haive.games.chess.agent import ChessAgent
    from haive.games.chess.config import ChessConfig
    return _game(ChessAgent, ChessConfig)


def connect4():
    """Connect4: AI vs AI four-in-a-row."""
    from haive.games.connect4.agent import Connect4Agent
    from haive.games.connect4.config import Connect4AgentConfig
    return _game(Connect4Agent, Connect4AgentConfig)


def checkers():
    """Checkers: AI vs AI draughts."""
    from haive.games.checkers.agent import CheckersAgent
    from haive.games.checkers.config import CheckersAgentConfig
    return _game(CheckersAgent, CheckersAgentConfig)


def nim():
    """Nim: AI vs AI mathematical strategy game."""
    from haive.games.nim.agent import NimAgent
    from haive.games.nim.config import NimConfig
    return _game(NimAgent, NimConfig)


def battleship():
    """Battleship: AI vs AI naval strategy."""
    from haive.games.battleship.agent import BattleshipAgent
    from haive.games.battleship.config import BattleshipAgentConfig
    return _game(BattleshipAgent, BattleshipAgentConfig)


def go():
    """Go: AI vs AI on a Go board."""
    from haive.games.go.agent import GoAgent
    from haive.games.go.config import GoAgentConfig
    return _game(GoAgent, GoAgentConfig)


def reversi():
    """Reversi/Othello: AI vs AI disc-flipping strategy."""
    from haive.games.reversi.agent import ReversiAgent
    from haive.games.reversi.config import ReversiConfig
    return _game(ReversiAgent, ReversiConfig)


def mancala():
    """Mancala: AI vs AI seed-sowing board game."""
    from haive.games.mancala.agent import MancalaAgent
    from haive.games.mancala.config import MancalaConfig
    return _game(MancalaAgent, MancalaConfig)


def mastermind():
    """Mastermind: AI code-breaking logic game."""
    from haive.games.mastermind.agent import MastermindAgent
    from haive.games.mastermind.config import MastermindConfig
    return _game(MastermindAgent, MastermindConfig)


def dominoes():
    """Dominoes: AI vs AI tile-matching game."""
    from haive.games.dominoes.agent import DominoesAgent
    from haive.games.dominoes.config import DominoesAgentConfig
    return _game(DominoesAgent, DominoesAgentConfig)


def fox_and_geese():
    """Fox and Geese: AI vs AI asymmetric hunt game."""
    from haive.games.fox_and_geese.agent import FoxAndGeeseAgent
    from haive.games.fox_and_geese.config import FoxAndGeeseConfig
    return _game(FoxAndGeeseAgent, FoxAndGeeseConfig)


# ---------------------------------------------------------------------------
# Multi-Player Games
# ---------------------------------------------------------------------------

def among_us():
    """Among Us: Multi-agent social deduction game."""
    from haive.games.among_us.agent import AmongUsAgent
    from haive.games.among_us.config import AmongUsAgentConfig
    return _game(AmongUsAgent, AmongUsAgentConfig,
                 player_names=["Alice", "Bob", "Charlie", "Dave"])


def debate():
    """Debate: Multi-agent structured debate."""
    from haive.games.debate.agent import DebateAgent
    from haive.games.debate.config import DebateAgentConfig
    return _game(DebateAgent, DebateAgentConfig)


def mafia():
    """Mafia: Multi-agent social deduction game."""
    from haive.games.mafia.agent import MafiaAgent
    from haive.games.mafia.config import MafiaAgentConfig
    return _game(MafiaAgent, MafiaAgentConfig)


def clue():
    """Clue/Cluedo: Multi-agent mystery deduction."""
    from haive.games.clue.agent import ClueAgent
    from haive.games.clue.config import ClueConfig
    return _game(ClueAgent, ClueConfig)


def risk():
    """Risk: Multi-agent world domination strategy.

    Note: Risk uses a standalone Pydantic model, not a LangGraph agent.
    Requires custom instantiation.
    """
    from haive.games.risk.agent import RiskAgent
    a = RiskAgent(name="risk")
    # Risk doesn't use LangGraph compilation - return its internal graph
    if hasattr(a, "app") and a.app:
        return a.app
    raise NotImplementedError("Risk agent does not produce a LangGraph graph")


def monopoly():
    """Monopoly: Multi-agent economic board game."""
    from haive.games.monopoly.game_agent import MonopolyGameAgent
    from haive.games.monopoly.config import MonopolyGameAgentConfig
    config = MonopolyGameAgentConfig(name="monopoly")
    agent = MonopolyGameAgent(config)
    return agent.app


# ---------------------------------------------------------------------------
# Card Games
# ---------------------------------------------------------------------------

def poker():
    """Poker: Multi-agent card game.

    Note: Poker requires engine configurations for each player.
    """
    from haive.games.poker.agent import PokerAgent
    from haive.games.poker.config import PokerAgentConfig
    config = PokerAgentConfig()
    agent = PokerAgent(config)
    return agent.app


def holdem():
    """Texas Hold'em: Multi-agent poker variant."""
    from haive.games.hold_em.game_agent import HoldemGameAgent
    from haive.games.hold_em.config import HoldemGameAgentConfig
    return _game(HoldemGameAgent, HoldemGameAgentConfig)


def blackjack():
    """Blackjack: Card game against the dealer."""
    from haive.games.cards.standard.blackjack.agent import BlackjackAgent
    from haive.games.cards.standard.blackjack.config import BlackjackAgentConfig
    return _game(BlackjackAgent, BlackjackAgentConfig)


# ---------------------------------------------------------------------------
# Single-Player Games
# ---------------------------------------------------------------------------

def wordle():
    """Word Connections: Single-player word puzzle."""
    from haive.games.single_player.wordle.agent import WordConnectionsAgent
    from haive.games.single_player.wordle.config import WordConnectionsAgentConfig
    return _game(WordConnectionsAgent, WordConnectionsAgentConfig)


def flow_free():
    """Flow Free: Single-player path-connection puzzle."""
    from haive.games.single_player.flow_free.agent import FlowFreeAgent
    from haive.games.single_player.flow_free.config import FlowFreeConfig
    return _game(FlowFreeAgent, FlowFreeConfig)
