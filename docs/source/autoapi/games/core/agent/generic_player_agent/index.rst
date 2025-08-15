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


   .. autolink-examples:: games.core.agent.generic_player_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   games.core.agent.generic_player_agent.PlayerType
   games.core.agent.generic_player_agent.PlayerType2


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


Functions
---------

.. autoapisummary::

   games.core.agent.generic_player_agent.create_engines_from_simple_configs
   games.core.agent.generic_player_agent.create_generic_game_config
   games.core.agent.generic_player_agent.example_chess_usage
   games.core.agent.generic_player_agent.example_custom_game_usage


Module Contents
---------------

.. py:class:: AmongUsPlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Among Us-specific player identifiers.


   .. autolink-examples:: AmongUsPlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'crewmate'



   .. py:attribute:: player2
      :type:  str
      :value: 'impostor'



.. py:class:: BattleshipPlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Battleship-specific player identifiers.


   .. autolink-examples:: BattleshipPlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'player1'



   .. py:attribute:: player2
      :type:  str
      :value: 'player2'



.. py:class:: CheckersPlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Checkers-specific player identifiers.


   .. autolink-examples:: CheckersPlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'red'



   .. py:attribute:: player2
      :type:  str
      :value: 'black'



.. py:class:: ChessPlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Chess-specific player identifiers.


   .. autolink-examples:: ChessPlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'white'



   .. py:attribute:: player2
      :type:  str
      :value: 'black'



.. py:class:: CluePlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Clue-specific player identifiers.


   .. autolink-examples:: CluePlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'detective'



   .. py:attribute:: player2
      :type:  str
      :value: 'suspect'



.. py:class:: Connect4PlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Connect4-specific player identifiers.


   .. autolink-examples:: Connect4PlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'red'



   .. py:attribute:: player2
      :type:  str
      :value: 'yellow'



.. py:class:: DebatePlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Debate-specific player identifiers.


   .. autolink-examples:: DebatePlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'debater1'



   .. py:attribute:: player2
      :type:  str
      :value: 'debater2'



.. py:class:: DominoesPlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Dominoes-specific player identifiers.


   .. autolink-examples:: DominoesPlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'player1'



   .. py:attribute:: player2
      :type:  str
      :value: 'player2'



.. py:class:: FoxAndGeesePlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Fox and Geese-specific player identifiers.


   .. autolink-examples:: FoxAndGeesePlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'fox'



   .. py:attribute:: player2
      :type:  str
      :value: 'geese'



.. py:class:: GamePlayerIdentifiers(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`PlayerType`\ , :py:obj:`PlayerType2`\ ]


   Generic container for two-player game identifiers.

   This class defines the player identifiers for a two-player game using generics.
   It ensures type safety while allowing different naming conventions per game.

   .. rubric:: Examples

   >>> chess_players = GamePlayerIdentifiers(player1="white", player2="black")
   >>> checkers_players = GamePlayerIdentifiers(player1="red", player2="black")
   >>> ttt_players = GamePlayerIdentifiers(player1="X", player2="O")
   >>> connect4_players = GamePlayerIdentifiers(player1="red", player2="yellow")

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GamePlayerIdentifiers
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: get_opponent(player: PlayerType | PlayerType2) -> PlayerType | PlayerType2

      Get the opponent of the given player.


      .. autolink-examples:: get_opponent
         :collapse:


   .. py:method:: get_players() -> tuple[PlayerType, PlayerType2]

      Get both player identifiers as a tuple.


      .. autolink-examples:: get_players
         :collapse:


   .. py:attribute:: player1
      :type:  PlayerType
      :value: None



   .. py:attribute:: player2
      :type:  PlayerType2
      :value: None



.. py:class:: GenericGameEngineFactory(players: GamePlayerIdentifiers[PlayerType, PlayerType2], prompt_generator: GenericPromptGenerator[PlayerType, PlayerType2], default_temperature: float = 0.7, analyzer_temperature: float = 0.3)

   Bases: :py:obj:`Generic`\ [\ :py:obj:`PlayerType`\ , :py:obj:`PlayerType2`\ ]


   Generic factory for creating game engines using player type generics.

   This factory creates AugLLMConfig engines for any two-player game using the generic
   player agent system and type-safe player identifiers.



   .. autolink-examples:: GenericGameEngineFactory
      :collapse:

   .. py:method:: _create_engine_from_role(role: GenericGameRole, agent_config: haive.games.core.agent.player_agent.PlayerAgentConfig) -> haive.core.engine.aug_llm.AugLLMConfig

      Create an AugLLMConfig from a role and agent configuration.


      .. autolink-examples:: _create_engine_from_role
         :collapse:


   .. py:method:: create_engines_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

      Create engines from player configurations using generics.

      :param player_configs: Dictionary of role name to player configuration

      :returns: Dictionary of configured engines
      :rtype: Dict[str, AugLLMConfig]

      .. rubric:: Example

      >>> configs = {
      ...     "white_player": PlayerAgentConfig(llm_config="gpt-4"),
      ...     "black_player": PlayerAgentConfig(llm_config="claude-3-opus"),
      ...     "white_analyzer": PlayerAgentConfig(llm_config="gpt-4"),
      ...     "black_analyzer": PlayerAgentConfig(llm_config="claude-3-opus"),
      ... }
      >>> engines = factory.create_engines_from_player_configs(configs)


      .. autolink-examples:: create_engines_from_player_configs
         :collapse:


   .. py:method:: create_engines_from_simple_configs(player1_model: str | haive.core.models.llm.LLMConfig, player2_model: str | haive.core.models.llm.LLMConfig, **kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

      Create engines from simple model configurations.

      :param player1_model: Model for first player and analyzer
      :param player2_model: Model for second player and analyzer
      :param \*\*kwargs: Additional configuration parameters

      :returns: Dictionary of engines
      :rtype: Dict[str, AugLLMConfig]


      .. autolink-examples:: create_engines_from_simple_configs
         :collapse:


   .. py:method:: create_role_definitions() -> dict[str, GenericGameRole[PlayerType | PlayerType2]]

      Create generic role definitions for the game.

      :returns: Dictionary of role definitions
      :rtype: Dict[str, GenericGameRole]


      .. autolink-examples:: create_role_definitions
         :collapse:


   .. py:attribute:: analyzer_temperature
      :value: 0.3



   .. py:attribute:: default_temperature
      :value: 0.7



   .. py:attribute:: players


   .. py:attribute:: prompt_generator


.. py:class:: GenericGameRole(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`PlayerType`\ ]


   Generic game role definition using player type generics.

   This class defines a role in a game (like "white_player" or "red_analyzer") using
   generic types for type safety and reusability across games.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GenericGameRole
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: player_identifier
      :type:  PlayerType
      :value: None



   .. py:attribute:: prompt_template
      :type:  Any
      :value: None



   .. py:attribute:: role_name
      :type:  str
      :value: None



   .. py:attribute:: role_type
      :type:  str
      :value: None



   .. py:attribute:: structured_output_model
      :type:  type | None
      :value: None



   .. py:attribute:: temperature
      :type:  float | None
      :value: None



.. py:class:: GenericPromptGenerator(players: GamePlayerIdentifiers[PlayerType, PlayerType2])

   Bases: :py:obj:`Generic`\ [\ :py:obj:`PlayerType`\ , :py:obj:`PlayerType2`\ ], :py:obj:`abc.ABC`


   Abstract base class for generating game-specific prompts using generics.

   This class provides the interface for generating move and analysis prompts for any
   two-player game using generic player types.



   .. autolink-examples:: GenericPromptGenerator
      :collapse:

   .. py:method:: create_analysis_prompt(player: PlayerType | PlayerType2) -> langchain_core.prompts.ChatPromptTemplate
      :abstractmethod:


      Create a position analysis prompt for the specified player.


      .. autolink-examples:: create_analysis_prompt
         :collapse:


   .. py:method:: create_move_prompt(player: PlayerType | PlayerType2) -> langchain_core.prompts.ChatPromptTemplate
      :abstractmethod:


      Create a move generation prompt for the specified player.


      .. autolink-examples:: create_move_prompt
         :collapse:


   .. py:method:: get_analysis_output_model() -> type
      :abstractmethod:


      Get the structured output model for analysis.


      .. autolink-examples:: get_analysis_output_model
         :collapse:


   .. py:method:: get_move_output_model() -> type
      :abstractmethod:


      Get the structured output model for moves.


      .. autolink-examples:: get_move_output_model
         :collapse:


   .. py:attribute:: players


.. py:class:: GoPlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Go-specific player identifiers.


   .. autolink-examples:: GoPlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'black'



   .. py:attribute:: player2
      :type:  str
      :value: 'white'



.. py:class:: HoldEmPlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Hold'em-specific player identifiers.


   .. autolink-examples:: HoldEmPlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'player1'



   .. py:attribute:: player2
      :type:  str
      :value: 'player2'



.. py:class:: MafiaPlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Mafia-specific player identifiers.


   .. autolink-examples:: MafiaPlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'mafia'



   .. py:attribute:: player2
      :type:  str
      :value: 'town'



.. py:class:: MancalaPlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Mancala-specific player identifiers.


   .. autolink-examples:: MancalaPlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'player1'



   .. py:attribute:: player2
      :type:  str
      :value: 'player2'



.. py:class:: MastermindPlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Mastermind-specific player identifiers.


   .. autolink-examples:: MastermindPlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'codemaker'



   .. py:attribute:: player2
      :type:  str
      :value: 'codebreaker'



.. py:class:: MonopolyPlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Monopoly-specific player identifiers.


   .. autolink-examples:: MonopolyPlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'player1'



   .. py:attribute:: player2
      :type:  str
      :value: 'player2'



.. py:class:: NimPlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Nim-specific player identifiers.


   .. autolink-examples:: NimPlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'player1'



   .. py:attribute:: player2
      :type:  str
      :value: 'player2'



.. py:class:: PokerPlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Poker-specific player identifiers.


   .. autolink-examples:: PokerPlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'player1'



   .. py:attribute:: player2
      :type:  str
      :value: 'player2'



.. py:class:: ReversiPlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Reversi-specific player identifiers.


   .. autolink-examples:: ReversiPlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'black'



   .. py:attribute:: player2
      :type:  str
      :value: 'white'



.. py:class:: RiskPlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Risk-specific player identifiers.


   .. autolink-examples:: RiskPlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'player1'



   .. py:attribute:: player2
      :type:  str
      :value: 'player2'



.. py:class:: TicTacToePlayerIdentifiers

   Bases: :py:obj:`GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Tic Tac Toe-specific player identifiers.


   .. autolink-examples:: TicTacToePlayerIdentifiers
      :collapse:

   .. py:attribute:: player1
      :type:  str
      :value: 'X'



   .. py:attribute:: player2
      :type:  str
      :value: 'O'



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

.. py:data:: PlayerType

.. py:data:: PlayerType2

