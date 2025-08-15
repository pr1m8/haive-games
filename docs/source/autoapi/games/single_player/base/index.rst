games.single_player.base
========================

.. py:module:: games.single_player.base

.. autoapi-nested-parse::

   Single-player game framework for LLM-powered games.

   This module provides a core framework for building single-player games where
   an LLM can act as the player, the assistant, or the game engine. The framework
   is designed to be flexible, extensible, and independent of any multiplayer
   game concepts.

   .. rubric:: Example

   >>> from haive.agents.single_player import SinglePlayerGameAgent
   >>> class WordleAgent(SinglePlayerGameAgent):
   ...     def __init__(self, config):
   ...         super().__init__(config)
   ...         self.state_manager = WordleStateManager

   Typical usage:
       - Inherit from SinglePlayerGameState for game-specific state
       - Inherit from SinglePlayerStateManager for game logic
       - Inherit from SinglePlayerGameConfig for configuration
       - Inherit from SinglePlayerGameAgent for the agent implementation


   .. autolink-examples:: games.single_player.base
      :collapse:


Attributes
----------

.. autoapisummary::

   games.single_player.base.T


Classes
-------

.. autoapisummary::

   games.single_player.base.GameDifficulty
   games.single_player.base.GameMode
   games.single_player.base.GameSourceType
   games.single_player.base.PlayerType
   games.single_player.base.SinglePlayerGameAgent
   games.single_player.base.SinglePlayerGameConfig
   games.single_player.base.SinglePlayerGameState
   games.single_player.base.SinglePlayerStateManager


Module Contents
---------------

.. py:class:: GameDifficulty

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Difficulty level for a game.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GameDifficulty
      :collapse:

   .. py:attribute:: EASY
      :value: 'easy'



   .. py:attribute:: EXPERT
      :value: 'expert'



   .. py:attribute:: HARD
      :value: 'hard'



   .. py:attribute:: MEDIUM
      :value: 'medium'



.. py:class:: GameMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Mode of operation for the game.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GameMode
      :collapse:

   .. py:attribute:: ASSIST
      :value: 'assist'



   .. py:attribute:: AUTO
      :value: 'auto'



   .. py:attribute:: INTERACTIVE
      :value: 'interactive'



.. py:class:: GameSourceType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Source of the game content.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GameSourceType
      :collapse:

   .. py:attribute:: CUSTOM
      :value: 'custom'



   .. py:attribute:: EXTERNAL
      :value: 'external'



   .. py:attribute:: INTERNAL
      :value: 'internal'



.. py:class:: PlayerType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Type of player in a single-player game.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlayerType
      :collapse:

   .. py:attribute:: HUMAN
      :value: 'human'



   .. py:attribute:: HYBRID
      :value: 'hybrid'



   .. py:attribute:: LLM
      :value: 'llm'



.. py:class:: SinglePlayerGameAgent(config)

   Base agent for single-player games.

   This class provides the core functionality for single-player game agents,
   including state initialization, move handling, analysis, and visualization.

   .. attribute:: config

      Configuration for the game agent

   .. attribute:: state_manager

      Manager for game state transitions

   .. attribute:: engines

      Dictionary of LLM engines for move generation and analysis

   .. attribute:: graph

      State graph for game flow

   .. attribute:: app

      Compiled graph application

   Initialize the game agent.

   :param config: Configuration for the game agent


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SinglePlayerGameAgent
      :collapse:

   .. py:method:: _setup_output_paths()

      Set up paths for output files.


      .. autolink-examples:: _setup_output_paths
         :collapse:


   .. py:method:: analyze_position(state: T) -> langgraph.types.Command

      Analyze the current game state.

      :param state: Current game state

      :returns: Command with the updated game state including analysis


      .. autolink-examples:: analyze_position
         :collapse:


   .. py:method:: extract_move(response: Any) -> Any
      :abstractmethod:


      Extract move from engine response.

      :param response: Response from the engine

      :returns: Extracted move


      .. autolink-examples:: extract_move
         :collapse:


   .. py:method:: get_hint(state: T) -> langgraph.types.Command

      Get a hint for the current game state.

      :param state: Current game state

      :returns: Command with the updated game state including a hint


      .. autolink-examples:: get_hint
         :collapse:


   .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

      Initialize a new game.

      :param state: Initial state (usually empty)

      :returns: Command with the initialized game state


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: interactive_command(state: T, command: str) -> langgraph.types.Command

      Process an interactive command.

      :param state: Current game state
      :param command: Command string

      :returns: Command with the updated game state


      .. autolink-examples:: interactive_command
         :collapse:


   .. py:method:: make_player_move(state: T) -> langgraph.types.Command

      Make a move for the player.

      In auto mode, this uses the LLM to generate a move.
      In interactive mode, this just returns the state unchanged.

      :param state: Current game state

      :returns: Command with the updated game state


      .. autolink-examples:: make_player_move
         :collapse:


   .. py:method:: prepare_analysis_context(state: T) -> dict[str, Any]
      :abstractmethod:


      Prepare context for analysis.

      :param state: Current game state

      :returns: Context dictionary for the analysis engine


      .. autolink-examples:: prepare_analysis_context
         :collapse:


   .. py:method:: prepare_move_context(state: T) -> dict[str, Any]
      :abstractmethod:


      Prepare context for move generation.

      :param state: Current game state

      :returns: Context dictionary for the move engine


      .. autolink-examples:: prepare_move_context
         :collapse:


   .. py:method:: save_state_history() -> None

      Save the current agent state to a JSON file.


      .. autolink-examples:: save_state_history
         :collapse:


   .. py:method:: setup_workflow()

      Setup the workflow for the game.

      The workflow depends on the game mode:
      - Auto: Initialize -> Analyze -> Move -> Check -> Repeat
      - Interactive: Initialize -> Listen for commands
      - Assist: Initialize -> Analyze -> Listen for commands



      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: should_continue_game(state: T) -> bool

      Check if the game should continue.

      :param state: Current game state

      :returns: True if the game should continue, False otherwise


      .. autolink-examples:: should_continue_game
         :collapse:


   .. py:method:: visualize_state(state: dict[str, Any]) -> None
      :abstractmethod:


      Visualize the current game state.

      :param state: Current game state


      .. autolink-examples:: visualize_state
         :collapse:


   .. py:attribute:: app


   .. py:attribute:: config


   .. py:attribute:: engines


   .. py:attribute:: graph


   .. py:attribute:: memory


   .. py:attribute:: runnable_config


   .. py:attribute:: state_manager
      :value: None



.. py:class:: SinglePlayerGameConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for single-player games.

   This class defines the core configuration parameters that all single-player
   games need, including player type, game mode, and difficulty.

   .. attribute:: state_schema

      The state schema class for the game

   .. attribute:: player_type

      Type of player (human, LLM, hybrid)

   .. attribute:: game_mode

      Mode of operation (interactive, auto, assist)

   .. attribute:: difficulty

      Difficulty level of the game

   .. attribute:: max_hints

      Maximum number of hints allowed

   .. attribute:: auto_analyze

      Whether to automatically analyze after each move

   .. attribute:: engines

      Configurations for game LLMs

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SinglePlayerGameConfig
      :collapse:

   .. py:attribute:: auto_analyze
      :type:  bool
      :value: None



   .. py:attribute:: difficulty
      :type:  GameDifficulty
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: game_mode
      :type:  GameMode
      :value: None



   .. py:attribute:: game_source
      :type:  GameSourceType
      :value: None



   .. py:attribute:: max_hints
      :type:  int
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: output_dir
      :type:  str
      :value: None



   .. py:attribute:: player_type
      :type:  PlayerType
      :value: None



   .. py:attribute:: runtime_config
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: save_history
      :type:  bool
      :value: None



   .. py:attribute:: state_schema
      :type:  type[SinglePlayerGameState]
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: None



.. py:class:: SinglePlayerGameState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Base state for single-player games.

   This class defines the core state attributes that all single-player games
   need to track, including game status, move history, and analysis.

   .. attribute:: player_type

      Type of player (human, LLM, hybrid)

      :type: PlayerType

   .. attribute:: move_count

      Number of moves made

      :type: int

   .. attribute:: hint_count

      Number of hints used

      :type: int

   .. attribute:: difficulty

      Difficulty level of the game

      :type: GameDifficulty

   .. attribute:: game_status

      Status of the game (ongoing, victory, defeat)

      :type: str

   .. attribute:: move_history

      History of moves made

      :type: List[Dict]

   .. attribute:: analysis_history

      History of analyses made

      :type: List[Dict]

   .. attribute:: error_message

      Error message if any

      :type: Optional[str]

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SinglePlayerGameState
      :collapse:

   .. py:method:: increment_move_count() -> None

      Increment the move count.


      .. autolink-examples:: increment_move_count
         :collapse:


   .. py:method:: is_defeat() -> bool

      Check if the game was lost.


      .. autolink-examples:: is_defeat
         :collapse:


   .. py:method:: is_game_over() -> bool

      Check if the game is over.


      .. autolink-examples:: is_game_over
         :collapse:


   .. py:method:: is_victory() -> bool

      Check if the game was won.


      .. autolink-examples:: is_victory
         :collapse:


   .. py:method:: use_hint() -> None

      Use a hint.


      .. autolink-examples:: use_hint
         :collapse:


   .. py:attribute:: analysis_history
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: difficulty
      :type:  GameDifficulty
      :value: None



   .. py:attribute:: error_message
      :type:  str | None
      :value: None



   .. py:attribute:: game_status
      :type:  str
      :value: None



   .. py:attribute:: hint_count
      :type:  int
      :value: None



   .. py:attribute:: move_count
      :type:  int
      :value: None



   .. py:attribute:: move_history
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: player_type
      :type:  PlayerType
      :value: None



.. py:class:: SinglePlayerStateManager

   Bases: :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   Base state manager for single-player games.

   This class provides the interface for managing game state transitions
   and operations. Each game should extend this with game-specific logic
   by implementing the required methods.

   Type Parameters:
       T: The type of the game state, must be a Pydantic BaseModel.

   .. method:: initialize

      Initialize a new game state

   .. method:: apply_move

      Apply a move to the game state

   .. method:: generate_hint

      Generate a hint for the current game state

   .. method:: check_game_status

      Check and update the game status

   .. method:: interactive_input

      Process interactive input from the player
      
      


   .. autolink-examples:: SinglePlayerStateManager
      :collapse:

   .. py:method:: apply_move(state: T, move: Any) -> T
      :classmethod:

      :abstractmethod:


      Apply a move to the game state.

      :param state: Current game state
      :param move: Move to apply

      :returns: Updated game state


      .. autolink-examples:: apply_move
         :collapse:


   .. py:method:: check_game_status(state: T) -> T
      :classmethod:

      :abstractmethod:


      Check and update the game status.

      :param state: Current game state

      :returns: Updated game state with status checked


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: generate_hint(state: T) -> tuple[T, str]
      :classmethod:


      Generate a hint for the current game state.

      :param state: Current game state

      :returns: Tuple of (updated state, hint text)


      .. autolink-examples:: generate_hint
         :collapse:


   .. py:method:: get_legal_moves(state: T) -> list[Any]
      :classmethod:

      :abstractmethod:


      Get all legal moves for the current state.

      :param state: Current game state

      :returns: List of legal moves


      .. autolink-examples:: get_legal_moves
         :collapse:


   .. py:method:: initialize(difficulty: GameDifficulty = GameDifficulty.MEDIUM, player_type: PlayerType = PlayerType.LLM, **kwargs) -> T
      :classmethod:

      :abstractmethod:


      Initialize a new game state.

      :param difficulty: Difficulty level of the game
      :param player_type: Type of player
      :param \*\*kwargs: Additional game-specific initialization parameters

      :returns: A new game state


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: interactive_input(state: T, user_input: str) -> T
      :classmethod:


      Process interactive input from the player.

      This method handles general commands like 'hint', 'quit', etc.
      Game-specific commands should be handled by overriding this method.

      :param state: Current game state
      :param user_input: User input string

      :returns: Updated game state


      .. autolink-examples:: interactive_input
         :collapse:


.. py:data:: T

