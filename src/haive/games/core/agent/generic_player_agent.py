"""Generic player agent system using Python generics.

This module provides a fully generic player agent system that works across all
two-player games using Python's typing.Generic system. It abstracts the common
pattern of player1/player2 + analyzer1/analyzer2 found across all games.

The generic system supports:
- Type-safe player identifiers (e.g., "white"/"black", "red"/"yellow", "X"/"O")
- Generic role definitions that work for any game
- Automatic engine generation from player configurations
- Template-based prompt generation
- Full integration with the LLM factory system
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, Optional, Tuple, Type, TypeVar, Union

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm import LLMConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.games.core.agent.player_agent import PlayerAgentConfig

# Generic type variables for player identifiers
PlayerType = TypeVar("PlayerType")  # e.g., "white", "red", "X"
PlayerType2 = TypeVar("PlayerType2")  # e.g., "black", "yellow", "O"


class GamePlayerIdentifiers(BaseModel, Generic[PlayerType, PlayerType2]):
    """Generic container for two-player game identifiers.

    This class defines the player identifiers for a two-player game using generics.
    It ensures type safety while allowing different naming conventions per game.

    Examples:
        >>> chess_players = GamePlayerIdentifiers(player1="white", player2="black")
        >>> checkers_players = GamePlayerIdentifiers(player1="red", player2="black")
        >>> ttt_players = GamePlayerIdentifiers(player1="X", player2="O")
        >>> connect4_players = GamePlayerIdentifiers(player1="red", player2="yellow")
    """

    player1: PlayerType = Field(description="Identifier for first player")
    player2: PlayerType2 = Field(description="Identifier for second player")

    class Config:
        arbitrary_types_allowed = True

    def get_players(self) -> Tuple[PlayerType, PlayerType2]:
        """Get both player identifiers as a tuple."""
        return (self.player1, self.player2)

    def get_opponent(
        self, player: Union[PlayerType, PlayerType2]
    ) -> Union[PlayerType, PlayerType2]:
        """Get the opponent of the given player."""
        if player == self.player1:
            return self.player2
        elif player == self.player2:
            return self.player1
        else:
            raise ValueError(f"Unknown player: {player}")


class GenericGameRole(BaseModel, Generic[PlayerType]):
    """Generic game role definition using player type generics.

    This class defines a role in a game (like "white_player" or
    "red_analyzer") using generic types for type safety and reusability
    across games.
    """

    role_name: str = Field(description="Name of the role (e.g., 'white_player')")
    player_identifier: PlayerType = Field(description="Player this role belongs to")
    role_type: str = Field(description="Type of role ('player' or 'analyzer')")
    prompt_template: Any = Field(description="Prompt template for this role")
    structured_output_model: Optional[Type] = Field(
        default=None, description="Expected output model"
    )
    temperature: Optional[float] = Field(
        default=None, description="Default temperature"
    )
    description: str = Field(default="", description="Description of this role")

    class Config:
        arbitrary_types_allowed = True


class GenericPromptGenerator(Generic[PlayerType, PlayerType2], ABC):
    """Abstract base class for generating game-specific prompts using generics.

    This class provides the interface for generating move and analysis
    prompts for any two-player game using generic player types.
    """

    def __init__(self, players: GamePlayerIdentifiers[PlayerType, PlayerType2]):
        self.players = players

    @abstractmethod
    def create_move_prompt(
        self, player: Union[PlayerType, PlayerType2]
    ) -> ChatPromptTemplate:
        """Create a move generation prompt for the specified player."""
        pass

    @abstractmethod
    def create_analysis_prompt(
        self, player: Union[PlayerType, PlayerType2]
    ) -> ChatPromptTemplate:
        """Create a position analysis prompt for the specified player."""
        pass

    @abstractmethod
    def get_move_output_model(self) -> Type:
        """Get the structured output model for moves."""
        pass

    @abstractmethod
    def get_analysis_output_model(self) -> Type:
        """Get the structured output model for analysis."""
        pass


class GenericGameEngineFactory(Generic[PlayerType, PlayerType2]):
    """Generic factory for creating game engines using player type generics.

    This factory creates AugLLMConfig engines for any two-player game
    using the generic player agent system and type-safe player
    identifiers.
    """

    def __init__(
        self,
        players: GamePlayerIdentifiers[PlayerType, PlayerType2],
        prompt_generator: GenericPromptGenerator[PlayerType, PlayerType2],
        default_temperature: float = 0.7,
        analyzer_temperature: float = 0.3,
    ):
        self.players = players
        self.prompt_generator = prompt_generator
        self.default_temperature = default_temperature
        self.analyzer_temperature = analyzer_temperature

    def create_role_definitions(
        self,
    ) -> Dict[str, GenericGameRole[Union[PlayerType, PlayerType2]]]:
        """Create generic role definitions for the game.

        Returns:
            Dict[str, GenericGameRole]: Dictionary of role definitions
        """
        move_model = self.prompt_generator.get_move_output_model()
        analysis_model = self.prompt_generator.get_analysis_output_model()

        roles = {}

        # Player roles
        for player in self.players.get_players():
            player_role_name = f"{player}_player"
            roles[player_role_name] = GenericGameRole(
                role_name=player_role_name,
                player_identifier=player,
                role_type="player",
                prompt_template=self.prompt_generator.create_move_prompt(player),
                structured_output_model=move_model,
                temperature=self.default_temperature,
                description=f"{player} player move generation",
            )

            # Analyzer roles
            analyzer_role_name = f"{player}_analyzer"
            roles[analyzer_role_name] = GenericGameRole(
                role_name=analyzer_role_name,
                player_identifier=player,
                role_type="analyzer",
                prompt_template=self.prompt_generator.create_analysis_prompt(player),
                structured_output_model=analysis_model,
                temperature=self.analyzer_temperature,
                description=f"{player} position analysis",
            )

        return roles

    def create_engines_from_player_configs(
        self, player_configs: Dict[str, PlayerAgentConfig]
    ) -> Dict[str, AugLLMConfig]:
        """Create engines from player configurations using generics.

        Args:
            player_configs: Dictionary of role name to player configuration

        Returns:
            Dict[str, AugLLMConfig]: Dictionary of configured engines

        Example:
            >>> configs = {
            ...     "white_player": PlayerAgentConfig(llm_config="gpt-4"),
            ...     "black_player": PlayerAgentConfig(llm_config="claude-3-opus"),
            ...     "white_analyzer": PlayerAgentConfig(llm_config="gpt-4"),
            ...     "black_analyzer": PlayerAgentConfig(llm_config="claude-3-opus"),
            ... }
            >>> engines = factory.create_engines_from_player_configs(configs)
        """
        role_definitions = self.create_role_definitions()
        engines = {}

        for role_name, role in role_definitions.items():
            if role_name in player_configs:
                agent_config = player_configs[role_name]
                engines[role_name] = self._create_engine_from_role(role, agent_config)
            else:
                raise ValueError(f"No player config provided for role: {role_name}")

        return engines

    def create_engines_from_simple_configs(
        self,
        player1_model: Union[str, LLMConfig],
        player2_model: Union[str, LLMConfig],
        **kwargs,
    ) -> Dict[str, AugLLMConfig]:
        """Create engines from simple model configurations.

        Args:
            player1_model: Model for first player and analyzer
            player2_model: Model for second player and analyzer
            **kwargs: Additional configuration parameters

        Returns:
            Dict[str, AugLLMConfig]: Dictionary of engines
        """
        player1, player2 = self.players.get_players()

        # Separate temperature handling to avoid conflicts
        player_temperature = kwargs.pop("temperature", self.default_temperature)
        analyzer_kwargs = {k: v for k, v in kwargs.items() if k != "temperature"}

        player_configs = {
            f"{player1}_player": PlayerAgentConfig(
                llm_config=player1_model,
                player_name=f"{player1} Player",
                temperature=player_temperature,
                **analyzer_kwargs,
            ),
            f"{player2}_player": PlayerAgentConfig(
                llm_config=player2_model,
                player_name=f"{player2} Player",
                temperature=player_temperature,
                **analyzer_kwargs,
            ),
            f"{player1}_analyzer": PlayerAgentConfig(
                llm_config=player1_model,
                player_name=f"{player1} Analyzer",
                temperature=self.analyzer_temperature,
                **analyzer_kwargs,
            ),
            f"{player2}_analyzer": PlayerAgentConfig(
                llm_config=player2_model,
                player_name=f"{player2} Analyzer",
                temperature=self.analyzer_temperature,
                **analyzer_kwargs,
            ),
        }

        return self.create_engines_from_player_configs(player_configs)

    def _create_engine_from_role(
        self, role: GenericGameRole, agent_config: PlayerAgentConfig
    ) -> AugLLMConfig:
        """Create an AugLLMConfig from a role and agent configuration."""
        llm_config = agent_config.create_llm_config()
        temperature = agent_config.temperature or role.temperature

        return AugLLMConfig(
            name=role.role_name,
            llm_config=llm_config,
            prompt_template=role.prompt_template,
            structured_output_model=role.structured_output_model,
            temperature=temperature,
            description=role.description,
            structured_output_version="v1",
        )


# Convenience classes for common game types


class ChessPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Chess-specific player identifiers."""

    player1: str = "white"
    player2: str = "black"


class CheckersPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Checkers-specific player identifiers."""

    player1: str = "red"
    player2: str = "black"


class TicTacToePlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Tic Tac Toe-specific player identifiers."""

    player1: str = "X"
    player2: str = "O"


class Connect4PlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Connect4-specific player identifiers."""

    player1: str = "red"
    player2: str = "yellow"


# Additional game identifiers for all other games


class AmongUsPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Among Us-specific player identifiers."""

    player1: str = "crewmate"
    player2: str = "impostor"


class BattleshipPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Battleship-specific player identifiers."""

    player1: str = "player1"
    player2: str = "player2"


class CluePlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Clue-specific player identifiers."""

    player1: str = "detective"
    player2: str = "suspect"


class DebatePlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Debate-specific player identifiers."""

    player1: str = "debater1"
    player2: str = "debater2"


class DominoesPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Dominoes-specific player identifiers."""

    player1: str = "player1"
    player2: str = "player2"


class FoxAndGeesePlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Fox and Geese-specific player identifiers."""

    player1: str = "fox"
    player2: str = "geese"


class GoPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Go-specific player identifiers."""

    player1: str = "black"
    player2: str = "white"


class HoldEmPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Hold'em-specific player identifiers."""

    player1: str = "player1"
    player2: str = "player2"


class MafiaPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Mafia-specific player identifiers."""

    player1: str = "mafia"
    player2: str = "town"


class MancalaPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Mancala-specific player identifiers."""

    player1: str = "player1"
    player2: str = "player2"


class MastermindPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Mastermind-specific player identifiers."""

    player1: str = "codemaker"
    player2: str = "codebreaker"


class MonopolyPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Monopoly-specific player identifiers."""

    player1: str = "player1"
    player2: str = "player2"


class NimPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Nim-specific player identifiers."""

    player1: str = "player1"
    player2: str = "player2"


class PokerPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Poker-specific player identifiers."""

    player1: str = "player1"
    player2: str = "player2"


class ReversiPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Reversi-specific player identifiers."""

    player1: str = "black"
    player2: str = "white"


class RiskPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Risk-specific player identifiers."""

    player1: str = "player1"
    player2: str = "player2"


# Convenience functions


def create_engines_from_simple_configs(
    factory: GenericGameEngineFactory,
    player1_model: Union[str, LLMConfig],
    player2_model: Union[str, LLMConfig],
    temperature: float = 0.3,
) -> Dict[str, AugLLMConfig]:
    """Create engines from simple model configurations using a factory.

    Args:
        factory: The game engine factory instance
        player1_model: Model for first player and analyzer
        player2_model: Model for second player and analyzer
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of engines
    """
    return factory.create_engines_from_simple_configs(
        player1_model, player2_model, temperature=temperature
    )


# Generic configuration creator


def create_generic_game_config(
    game_name: str,
    players: GamePlayerIdentifiers,
    prompt_generator: GenericPromptGenerator,
    player1_model: Union[str, LLMConfig] = "gpt-4o",
    player2_model: Union[str, LLMConfig] = "claude-3-5-sonnet-20240620",
    **kwargs,
) -> Dict[str, AugLLMConfig]:
    """Create a generic game configuration for any two-player game.

    Args:
        game_name: Name of the game
        players: Player identifiers for the game
        prompt_generator: Prompt generator for the game
        player1_model: Model for first player
        player2_model: Model for second player
        **kwargs: Additional configuration parameters

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of engines

    Example:
        >>> chess_players = ChessPlayerIdentifiers()
        >>> chess_prompt_gen = ChessPromptGenerator(chess_players)
        >>> engines = create_generic_game_config(
        ...     "chess", chess_players, chess_prompt_gen, "gpt-4", "claude-3-opus"
        ... )
    """
    factory = GenericGameEngineFactory(players, prompt_generator, **kwargs)
    return factory.create_engines_from_simple_configs(
        player1_model, player2_model, **kwargs
    )


# Example usage patterns for documentation


def example_chess_usage():
    """Example of how to use the generic system for chess."""
    from haive.games.chess.models import ChessPlayerDecision, SegmentedAnalysis

    class ChessPromptGenerator(GenericPromptGenerator[str, str]):
        def create_move_prompt(self, player: str) -> ChatPromptTemplate:
            return ChatPromptTemplate.from_messages(
                [
                    ("system", f"You are playing chess as {player.upper()}..."),
                    ("human", "Current position: {current_board_fen}..."),
                ]
            )

        def create_analysis_prompt(self, player: str) -> ChatPromptTemplate:
            return ChatPromptTemplate.from_messages(
                [
                    ("system", f"Analyze position for {player.upper()}..."),
                    ("human", "Position: {current_board_fen}..."),
                ]
            )

        def get_move_output_model(self) -> Type:
            return ChessPlayerDecision

        def get_analysis_output_model(self) -> Type:
            return SegmentedAnalysis

    # Usage
    chess_players = ChessPlayerIdentifiers()
    chess_prompt_gen = ChessPromptGenerator(chess_players)
    engines = create_generic_game_config(
        "chess", chess_players, chess_prompt_gen, "gpt-4", "claude-3-opus"
    )
    return engines


def example_custom_game_usage():
    """Example of creating a new game using the generic system."""
    # For a hypothetical "Stone-Paper-Scissors" game
    sps_players = GamePlayerIdentifiers(player1="stone", player2="paper")

    class SPSPromptGenerator(GenericPromptGenerator[str, str]):
        def create_move_prompt(self, player: str) -> ChatPromptTemplate:
            return ChatPromptTemplate.from_messages(
                [
                    ("system", f"You are player {player} in Stone-Paper-Scissors..."),
                    ("human", "Choose your move: {legal_moves}"),
                ]
            )

        def create_analysis_prompt(self, player: str) -> ChatPromptTemplate:
            return ChatPromptTemplate.from_messages(
                [
                    ("system", f"Analyze strategy for {player}..."),
                    ("human", "Game history: {move_history}"),
                ]
            )

        def get_move_output_model(self) -> Type:
            return dict  # Simplified for example

        def get_analysis_output_model(self) -> Type:
            return dict  # Simplified for example

    sps_prompt_gen = SPSPromptGenerator(sps_players)
    engines = create_generic_game_config(
        "sps", sps_players, sps_prompt_gen, "gpt-4", "claude-3-opus"
    )
    return engines
