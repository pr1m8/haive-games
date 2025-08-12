
:py:mod:`games.core.agent.generic_player_agent`
===============================================

.. py:module:: games.core.agent.generic_player_agent

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


.. autolink-examples:: games.core.agent.generic_player_agent
   :collapse:

Classes
-------

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AmongUsPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_AmongUsPlayerIdentifiers {
        node [shape=record];
        "AmongUsPlayerIdentifiers" [label="AmongUsPlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "AmongUsPlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.AmongUsPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BattleshipPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_BattleshipPlayerIdentifiers {
        node [shape=record];
        "BattleshipPlayerIdentifiers" [label="BattleshipPlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "BattleshipPlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.BattleshipPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CheckersPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_CheckersPlayerIdentifiers {
        node [shape=record];
        "CheckersPlayerIdentifiers" [label="CheckersPlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "CheckersPlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.CheckersPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChessPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_ChessPlayerIdentifiers {
        node [shape=record];
        "ChessPlayerIdentifiers" [label="ChessPlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "ChessPlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.ChessPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CluePlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_CluePlayerIdentifiers {
        node [shape=record];
        "CluePlayerIdentifiers" [label="CluePlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "CluePlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.CluePlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Connect4PlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_Connect4PlayerIdentifiers {
        node [shape=record];
        "Connect4PlayerIdentifiers" [label="Connect4PlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "Connect4PlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.Connect4PlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DebatePlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_DebatePlayerIdentifiers {
        node [shape=record];
        "DebatePlayerIdentifiers" [label="DebatePlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "DebatePlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.DebatePlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DominoesPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_DominoesPlayerIdentifiers {
        node [shape=record];
        "DominoesPlayerIdentifiers" [label="DominoesPlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "DominoesPlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.DominoesPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FoxAndGeesePlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_FoxAndGeesePlayerIdentifiers {
        node [shape=record];
        "FoxAndGeesePlayerIdentifiers" [label="FoxAndGeesePlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "FoxAndGeesePlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.FoxAndGeesePlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GamePlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_GamePlayerIdentifiers {
        node [shape=record];
        "GamePlayerIdentifiers" [label="GamePlayerIdentifiers"];
        "pydantic.BaseModel" -> "GamePlayerIdentifiers";
        "Generic[PlayerType, PlayerType2]" -> "GamePlayerIdentifiers";
      }

.. autopydantic_model:: games.core.agent.generic_player_agent.GamePlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GenericGameEngineFactory:

   .. graphviz::
      :align: center

      digraph inheritance_GenericGameEngineFactory {
        node [shape=record];
        "GenericGameEngineFactory" [label="GenericGameEngineFactory"];
        "Generic[PlayerType, PlayerType2]" -> "GenericGameEngineFactory";
      }

.. autoclass:: games.core.agent.generic_player_agent.GenericGameEngineFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GenericGameRole:

   .. graphviz::
      :align: center

      digraph inheritance_GenericGameRole {
        node [shape=record];
        "GenericGameRole" [label="GenericGameRole"];
        "pydantic.BaseModel" -> "GenericGameRole";
        "Generic[PlayerType]" -> "GenericGameRole";
      }

.. autopydantic_model:: games.core.agent.generic_player_agent.GenericGameRole
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GenericPromptGenerator:

   .. graphviz::
      :align: center

      digraph inheritance_GenericPromptGenerator {
        node [shape=record];
        "GenericPromptGenerator" [label="GenericPromptGenerator"];
        "Generic[PlayerType, PlayerType2]" -> "GenericPromptGenerator";
        "abc.ABC" -> "GenericPromptGenerator";
      }

.. autoclass:: games.core.agent.generic_player_agent.GenericPromptGenerator
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GoPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_GoPlayerIdentifiers {
        node [shape=record];
        "GoPlayerIdentifiers" [label="GoPlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "GoPlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.GoPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HoldEmPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_HoldEmPlayerIdentifiers {
        node [shape=record];
        "HoldEmPlayerIdentifiers" [label="HoldEmPlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "HoldEmPlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.HoldEmPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MafiaPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_MafiaPlayerIdentifiers {
        node [shape=record];
        "MafiaPlayerIdentifiers" [label="MafiaPlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "MafiaPlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.MafiaPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MancalaPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_MancalaPlayerIdentifiers {
        node [shape=record];
        "MancalaPlayerIdentifiers" [label="MancalaPlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "MancalaPlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.MancalaPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MastermindPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_MastermindPlayerIdentifiers {
        node [shape=record];
        "MastermindPlayerIdentifiers" [label="MastermindPlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "MastermindPlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.MastermindPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MonopolyPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_MonopolyPlayerIdentifiers {
        node [shape=record];
        "MonopolyPlayerIdentifiers" [label="MonopolyPlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "MonopolyPlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.MonopolyPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for NimPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_NimPlayerIdentifiers {
        node [shape=record];
        "NimPlayerIdentifiers" [label="NimPlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "NimPlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.NimPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PokerPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_PokerPlayerIdentifiers {
        node [shape=record];
        "PokerPlayerIdentifiers" [label="PokerPlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "PokerPlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.PokerPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReversiPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_ReversiPlayerIdentifiers {
        node [shape=record];
        "ReversiPlayerIdentifiers" [label="ReversiPlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "ReversiPlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.ReversiPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RiskPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_RiskPlayerIdentifiers {
        node [shape=record];
        "RiskPlayerIdentifiers" [label="RiskPlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "RiskPlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.RiskPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TicTacToePlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_TicTacToePlayerIdentifiers {
        node [shape=record];
        "TicTacToePlayerIdentifiers" [label="TicTacToePlayerIdentifiers"];
        "GamePlayerIdentifiers[str, str]" -> "TicTacToePlayerIdentifiers";
      }

.. autoclass:: games.core.agent.generic_player_agent.TicTacToePlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.core.agent.generic_player_agent.create_engines_from_simple_configs
   games.core.agent.generic_player_agent.create_generic_game_config
   games.core.agent.generic_player_agent.example_chess_usage
   games.core.agent.generic_player_agent.example_custom_game_usage

.. py:function:: create_engines_from_simple_configs(factory: GenericGameEngineFactory, player1_model: str | haive.core.models.llm.LLMConfig, player2_model: str | haive.core.models.llm.LLMConfig, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create engines from simple model configurations using a factory.

   :param factory: The game engine factory instance
   :param player1_model: Model for first player and analyzer
   :param player2_model: Model for second player and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_engines_from_simple_configs
      :collapse:

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

   .. rubric:: Example

   >>> chess_players = ChessPlayerIdentifiers()
   >>> chess_prompt_gen = ChessPromptGenerator(chess_players)
   >>> engines = create_generic_game_config(
   ...     "chess", chess_players, chess_prompt_gen, "gpt-4", "claude-3-opus"
   ... )


   .. autolink-examples:: create_generic_game_config
      :collapse:

.. py:function:: example_chess_usage()

   Example of how to use the generic system for chess.


   .. autolink-examples:: example_chess_usage
      :collapse:

.. py:function:: example_custom_game_usage()

   Example of creating a new game using the generic system.


   .. autolink-examples:: example_custom_game_usage
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.core.agent.generic_player_agent
   :collapse:
   
.. autolink-skip:: next
