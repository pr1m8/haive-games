games.core.agent.generic_player_agent
=====================================

.. py:module:: games.core.agent.generic_player_agent

.. autoapi-nested-parse::

   Generic player agent system using Python generics.

   This module provides a fully generic player agent system that works across all
   two-player games using Python's typing.Generic system. It abstracts the common
   pattern of player1/player2 + analyzer1/analyzer2 found across all games.

   The generic system supports:
   - Type-safe player identifiers (e.g., "white"/"black", "red"/"yellow", "X"/"O")
   - Generic role definitions that work for any game
   - Automatic engine generation from player configurations
   - Template-based prompt generation
   - Full integration with the LLM factory system



Attributes
----------

.. autoapisummary::

   games.core.agent.generic_player_agent.PlayerType
   games.core.agent.generic_player_agent.PlayerType2


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/core/agent/generic_player_agent/AmongUsPlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/BattleshipPlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/CheckersPlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/ChessPlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/CluePlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/Connect4PlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/DebatePlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/DominoesPlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/FoxAndGeesePlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/GamePlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/GenericGameEngineFactory
   /autoapi/games/core/agent/generic_player_agent/GenericGameRole
   /autoapi/games/core/agent/generic_player_agent/GenericPromptGenerator
   /autoapi/games/core/agent/generic_player_agent/GoPlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/HoldEmPlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/MafiaPlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/MancalaPlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/MastermindPlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/MonopolyPlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/NimPlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/PokerPlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/ReversiPlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/RiskPlayerIdentifiers
   /autoapi/games/core/agent/generic_player_agent/TicTacToePlayerIdentifiers

.. autoapisummary::

   games.core.agent.generic_player_agent.AmongUsPlayerIdentifiers
   games.core.agent.generic_player_agent.BattleshipPlayerIdentifiers
   games.core.agent.generic_player_agent.CheckersPlayerIdentifiers
   games.core.agent.generic_player_agent.ChessPlayerIdentifiers
   games.core.agent.generic_player_agent.CluePlayerIdentifiers
   games.core.agent.generic_player_agent.Connect4PlayerIdentifiers
   games.core.agent.generic_player_agent.DebatePlayerIdentifiers
   games.core.agent.generic_player_agent.DominoesPlayerIdentifiers
   games.core.agent.generic_player_agent.FoxAndGeesePlayerIdentifiers
   games.core.agent.generic_player_agent.GamePlayerIdentifiers
   games.core.agent.generic_player_agent.GenericGameEngineFactory
   games.core.agent.generic_player_agent.GenericGameRole
   games.core.agent.generic_player_agent.GenericPromptGenerator
   games.core.agent.generic_player_agent.GoPlayerIdentifiers
   games.core.agent.generic_player_agent.HoldEmPlayerIdentifiers
   games.core.agent.generic_player_agent.MafiaPlayerIdentifiers
   games.core.agent.generic_player_agent.MancalaPlayerIdentifiers
   games.core.agent.generic_player_agent.MastermindPlayerIdentifiers
   games.core.agent.generic_player_agent.MonopolyPlayerIdentifiers
   games.core.agent.generic_player_agent.NimPlayerIdentifiers
   games.core.agent.generic_player_agent.PokerPlayerIdentifiers
   games.core.agent.generic_player_agent.ReversiPlayerIdentifiers
   games.core.agent.generic_player_agent.RiskPlayerIdentifiers
   games.core.agent.generic_player_agent.TicTacToePlayerIdentifiers


Functions
---------

.. autoapisummary::

   games.core.agent.generic_player_agent.create_engines_from_simple_configs
   games.core.agent.generic_player_agent.create_generic_game_config
   games.core.agent.generic_player_agent.example_chess_usage
   games.core.agent.generic_player_agent.example_custom_game_usage


Module Contents
---------------

.. py:function:: create_engines_from_simple_configs(factory: GenericGameEngineFactory, player1_model: str | haive.core.models.llm.LLMConfig, player2_model: str | haive.core.models.llm.LLMConfig, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create engines from simple model configurations using a factory.

   :param factory: The game engine factory instance
   :param player1_model: Model for first player and analyzer
   :param player2_model: Model for second player and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of engines
   :rtype: Dict[str, AugLLMConfig]


.. py:function:: create_generic_game_config(game_name: str, players: GamePlayerIdentifiers, prompt_generator: GenericPromptGenerator, player1_model: str | haive.core.models.llm.LLMConfig = 'gpt-4o', player2_model: str | haive.core.models.llm.LLMConfig = 'claude-3-5-sonnet-20240620', **kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create a generic game configuration for any two-player game.

   :param game_name: Name of the game
   :param players: Player identifiers for the game
   :param prompt_generator: Prompt generator for the game
   :param player1_model: Model for first player
   :param player2_model: Model for second player
   :param \*\*kwargs: Additional configuration parameters

   :returns: Dictionary of engines
   :rtype: Dict[str, AugLLMConfig]

   .. rubric:: Examples

   >>> chess_players = ChessPlayerIdentifiers()
   >>> chess_prompt_gen = ChessPromptGenerator(chess_players)
   >>> engines = create_generic_game_config(
   ...     "chess", chess_players, chess_prompt_gen, "gpt-4", "claude-3-opus"
   ... )


.. py:function:: example_chess_usage()

   Example of how to use the generic system for chess.


.. py:function:: example_custom_game_usage()

   Example of creating a new game using the generic system.


.. py:data:: PlayerType

.. py:data:: PlayerType2

