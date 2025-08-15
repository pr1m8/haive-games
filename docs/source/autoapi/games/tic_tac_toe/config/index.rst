games.tic_tac_toe.config
========================

.. py:module:: games.tic_tac_toe.config

.. autoapi-nested-parse::

   Comprehensive configuration system for strategic Tic Tac Toe gameplay.

   This module provides sophisticated configuration management for Tic Tac Toe agents,
   supporting various gameplay modes, AI difficulty levels, and analysis features.
   The configuration system enables flexible game setups from educational tutorials
   to competitive AI matches with perfect play algorithms.

   The configuration system supports:
   - Multiple AI engine configurations for different skill levels
   - Strategic analysis toggle for educational gameplay
   - Visualization options for interactive experiences
   - Player assignment and turn order customization
   - Integration with LLM-based decision engines
   - Tournament-ready configuration presets

   .. rubric:: Examples

   Basic game configuration::

       config = TicTacToeConfig(
           name="educational_game",
           enable_analysis=True,
           visualize=True
       )

   Tournament configuration::

       config = TicTacToeConfig(
           name="tournament_match",
           enable_analysis=False,
           visualize=False,
           first_player="X"
       )

   Custom player setup::

       config = TicTacToeConfig(
           player_X="player2",
           player_O="player1",
           first_player="O"
       )

   Using default configuration::

       config = TicTacToeConfig.default_config()
       # Ready for standard gameplay

   .. note::

      All configurations use Pydantic for validation and support both JSON
      serialization and integration with the game agent framework.


   .. autolink-examples:: games.tic_tac_toe.config
      :collapse:


Classes
-------

.. autoapisummary::

   games.tic_tac_toe.config.TicTacToeConfig


Module Contents
---------------

.. py:class:: TicTacToeConfig

   Bases: :py:obj:`haive.games.framework.base.config.GameConfig`


   Advanced configuration system for Tic Tac Toe game agents.

   This class provides comprehensive configuration management for Tic Tac Toe
   gameplay, supporting multiple AI personalities, strategic analysis features,
   and flexible game setups. The configuration enables various gameplay modes
   from casual games to perfect-play AI competitions.

   The configuration supports:
   - AI engine selection for different skill levels
   - Strategic analysis for educational purposes
   - Board visualization for interactive gameplay
   - Flexible player assignment and turn order
   - Integration with LLM-based decision systems
   - Tournament and casual play modes

   .. attribute:: name

      Unique identifier for the game configuration.
      Used for logging and game session management.

      :type: str

   .. attribute:: state_schema

      State management class.
      Defines the game state structure and validation rules.

      :type: Type[TicTacToeState]

   .. attribute:: engines

      AI engine configurations.
      Maps engine roles to their LLM configurations.

      :type: Dict[str, AugLLMConfig]

   .. attribute:: enable_analysis

      Toggle for strategic analysis features.
      When True, provides detailed move explanations.

      :type: bool

   .. attribute:: visualize

      Toggle for board visualization.
      When True, displays board state after each move.

      :type: bool

   .. attribute:: first_player

      Starting player symbol.
      Determines which player makes the first move.

      :type: Literal['X', 'O']

   .. attribute:: player_X

      Player using X.
      Maps X symbol to player identifier.

      :type: Literal['player1', 'player2']

   .. attribute:: player_O

      Player using O.
      Maps O symbol to player identifier.

      :type: Literal['player1', 'player2']

   .. rubric:: Examples

   Educational game with analysis::

       config = TicTacToeConfig(
           name="learning_game",
           enable_analysis=True,
           visualize=True,
           first_player="X"
       )
       # Provides move explanations and board visualization

   Competitive AI match::

       config = TicTacToeConfig(
           name="ai_competition",
           enable_analysis=False,
           visualize=False,
           engines=advanced_engines
       )
       # Fast gameplay without analysis overhead

   Custom player assignment::

       config = TicTacToeConfig(
           player_X="player2",
           player_O="player1",
           first_player="O"
       )
       # Player 2 uses X, Player 1 uses O and goes first

   Tournament configuration::

       config = TicTacToeConfig(
           name="tournament_round_1",
           enable_analysis=False,
           visualize=True,
           engines=tournament_engines
       )
       # Optimized for competitive play with spectator view

   .. note::

      The configuration integrates with the game agent framework and
      supports runtime modification through the agent's lifecycle.


   .. autolink-examples:: TicTacToeConfig
      :collapse:

   .. py:method:: competitive_config() -> TicTacToeConfig
      :classmethod:


      Create configuration for competitive AI play.

      Features:
      - No analysis overhead
      - No visualization delays
      - Optimized for speed
      - Perfect for AI tournaments

      :returns: Competitive configuration.
      :rtype: TicTacToeConfig


      .. autolink-examples:: competitive_config
         :collapse:


   .. py:method:: default_config() -> TicTacToeConfig
      :classmethod:


      Create a default configuration for standard Tic Tac Toe gameplay.

      The default configuration is optimized for educational gameplay with
      both analysis and visualization enabled, suitable for learning and
      casual play.

      :returns: Default game configuration instance.
      :rtype: TicTacToeConfig

      .. rubric:: Examples

      Creating default game::

          config = TicTacToeConfig.default_config()
          assert config.enable_analysis == True
          assert config.visualize == True
          assert config.first_player == "X"

      Using with agent::

          config = TicTacToeConfig.default_config()
          agent = TicTacToeAgent(config)
          agent.run_game()


      .. autolink-examples:: default_config
         :collapse:


   .. py:method:: educational_config() -> TicTacToeConfig
      :classmethod:


      Create configuration optimized for learning.

      Features:
      - Full analysis of every position
      - Board visualization after each move
      - Detailed move explanations
      - Perfect for teaching optimal strategy

      :returns: Educational configuration.
      :rtype: TicTacToeConfig


      .. autolink-examples:: educational_config
         :collapse:


   .. py:method:: spectator_config() -> TicTacToeConfig
      :classmethod:


      Create configuration for watching games.

      Features:
      - Board visualization enabled
      - Analysis disabled for speed
      - Good balance for spectating
      - Suitable for demonstrations

      :returns: Spectator configuration.
      :rtype: TicTacToeConfig


      .. autolink-examples:: spectator_config
         :collapse:


   .. py:method:: validate_first_player(v: str) -> str
      :classmethod:


      Validate first player is either X or O.

      :param v: First player symbol to validate.
      :type v: str

      :returns: Validated first player symbol.
      :rtype: str

      :raises ValueError: If first player is not X or O.


      .. autolink-examples:: validate_first_player
         :collapse:


   .. py:attribute:: enable_analysis
      :type:  bool
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: first_player
      :type:  Literal['X', 'O']
      :value: None



   .. py:property:: game_mode
      :type: str


      Determine the game mode based on configuration.

      :returns: Game mode classification.
      :rtype: str

      .. autolink-examples:: game_mode
         :collapse:


   .. py:attribute:: model_config


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:property:: performance_profile
      :type: dict[str, Any]


      Generate performance profile based on settings.

      :returns: Performance characteristics.
      :rtype: Dict[str, Any]

      .. autolink-examples:: performance_profile
         :collapse:


   .. py:attribute:: player_O
      :type:  Literal['player1', 'player2']
      :value: None



   .. py:attribute:: player_X
      :type:  Literal['player1', 'player2']
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.games.tic_tac_toe.state.TicTacToeState]
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: None



