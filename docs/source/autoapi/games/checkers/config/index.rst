games.checkers.config
=====================

.. py:module:: games.checkers.config


Classes
-------

.. autoapisummary::

   games.checkers.config.CheckersAgentConfig


Module Contents
---------------

.. py:class:: CheckersAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Advanced configuration system for Checkers agents with comprehensive rule.
   support.

   This class provides complete configuration management for Checkers gameplay,
   supporting multiple rule variants, strategic AI customization, and performance
   optimization. The configuration system enables flexible game setups from
   casual play to competitive tournaments and AI research applications.

   The configuration supports:
   - International rule variants (American, International, Russian, Brazilian)
   - Advanced AI strategy parameters with depth control
   - Performance optimization for different scenarios
   - Comprehensive validation and error handling
   - Factory methods for common configurations
   - Strategic analysis parameter tuning

   .. attribute:: board_size

      Size of the checkers board (8 for American, 10 for International).
      Determines the game complexity and strategy depth.

      :type: int

   .. attribute:: max_turns

      Maximum number of turns before declaring a draw.
      Prevents infinite games and ensures reasonable game duration.

      :type: int

   .. attribute:: allow_flying_kings

      Whether kings can move any distance along diagonals.
      True for International Draughts, False for American Checkers.

      :type: bool

   .. attribute:: mandatory_jumps

      Whether jumps are mandatory when available.
      Core rule that significantly affects strategy and gameplay.

      :type: bool

   .. attribute:: king_promotion_row

      Row where pieces promote to kings.
      Typically board_size-1 for the opponent's back rank.

      :type: int

   .. attribute:: strategic_depth

      Analysis depth for AI strategic planning.
      Higher values provide stronger play but slower decision-making.

      :type: int

   .. attribute:: time_per_move

      Maximum time allowed per move in seconds.
      Prevents excessive computation and ensures game flow.

      :type: float

   .. attribute:: enable_endgame_tables

      Whether to use endgame tablebase lookup.
      Provides perfect play in endgame positions when available.

      :type: bool

   .. attribute:: analysis_threads

      Number of threads for position analysis.
      Enables parallel processing for faster strategic evaluation.

      :type: int

   .. attribute:: memory_limit_mb

      Memory limit for position evaluation in MB.
      Prevents excessive memory usage during deep analysis.

      :type: int

   .. attribute:: state_schema

      State schema for the checkers game.
      Pydantic model defining the game state structure.

      :type: type[BaseModel]

   .. attribute:: engines

      LLM configurations for players and analyzers.
      Mapping of engine names to their configuration objects.

      :type: Dict[str, AugLLMConfig]

   .. attribute:: runnable_config

      Runtime configuration for the agent.
      LangGraph configuration including recursion limits and threading.

      :type: RunnableConfig

   .. rubric:: Examples

   Standard American Checkers configuration::\n

       config = CheckersAgentConfig.american_checkers()
       assert config.board_size == 8
       assert config.allow_flying_kings == False
       assert config.mandatory_jumps == True

   International Draughts configuration::\n

       config = CheckersAgentConfig.international_draughts()
       assert config.board_size == 10
       assert config.allow_flying_kings == True
       assert config.strategic_depth == 6

   Tournament-level competitive play::\n

       config = CheckersAgentConfig.tournament()
       assert config.strategic_depth == 8
       assert config.time_per_move == 30.0
       assert config.enable_endgame_tables == True

   Custom configuration with validation::\n

       config = CheckersAgentConfig(
           board_size=12,  # Custom board size
           max_turns=300,
           allow_flying_kings=True,
           strategic_depth=4,
           time_per_move=15.0
       )
       # Automatic validation ensures king_promotion_row = 11

   Training configuration for AI development::\n

       config = CheckersAgentConfig.training()
       assert config.strategic_depth == 3  # Faster for experimentation
       assert config.memory_limit_mb == 512  # Reasonable resource usage

   Performance-optimized configuration::\n

       config = CheckersAgentConfig.performance()
       assert config.analysis_threads == 4
       assert config.memory_limit_mb == 1024
       assert config.enable_endgame_tables == True

   .. note::

      All configurations use Pydantic for validation and support both JSON
      serialization and integration with distributed tournament systems.


   .. autolink-examples:: CheckersAgentConfig
      :collapse:

   .. py:method:: american_checkers() -> CheckersAgentConfig
      :classmethod:


      Create configuration for standard American Checkers.

      Standard American Checkers features:
      - 8x8 board with 64 squares
      - 12 pieces per player
      - Kings move one square diagonally
      - Mandatory jumps when available
      - Pieces promote on the back rank

      :returns: Configuration for American Checkers.
      :rtype: CheckersAgentConfig

      .. rubric:: Examples

      Creating American Checkers game::\n

          config = CheckersAgentConfig.american_checkers()
          agent = CheckersAgent(config)
          result = agent.run_game()

      Verifying American Checkers rules::\n

          config = CheckersAgentConfig.american_checkers()
          assert config.board_size == 8
          assert config.allow_flying_kings == False
          assert config.mandatory_jumps == True
          assert config.pieces_per_player == 12


      .. autolink-examples:: american_checkers
         :collapse:


   .. py:method:: default() -> CheckersAgentConfig
      :classmethod:


      Create a default configuration for checkers.

      Creates a configuration with standard American Checkers rules:
      - 8x8 board with 64 squares
      - 100 max turns for reasonable game length
      - Mandatory jumps following traditional rules
      - Standard kings (no flying kings)
      - Balanced strategic depth

      :returns: Default configuration for checkers.
      :rtype: CheckersAgentConfig

      .. rubric:: Examples

      Creating default game::\n

          config = CheckersAgentConfig.default()
          agent = CheckersAgent(config)
          result = agent.run_game()

      Verifying default settings::\n

          config = CheckersAgentConfig.default()
          assert config.board_size == 8
          assert config.mandatory_jumps == True
          assert config.strategic_depth == 4
          assert config.game_variant == "American Checkers"


      .. autolink-examples:: default
         :collapse:


   .. py:method:: international_draughts() -> CheckersAgentConfig
      :classmethod:


      Create configuration for International Draughts (10x10).

      International Draughts features:
      - 10x10 board with 100 squares
      - 20 pieces per player
      - Flying kings with unlimited diagonal movement
      - Mandatory jumps with maximum capture rule
      - More complex strategic gameplay

      :returns: Configuration for International Draughts.
      :rtype: CheckersAgentConfig

      .. rubric:: Examples

      Creating International Draughts game::\n

          config = CheckersAgentConfig.international_draughts()
          agent = CheckersAgent(config)
          result = agent.run_game()

      Verifying International rules::\n

          config = CheckersAgentConfig.international_draughts()
          assert config.board_size == 10
          assert config.allow_flying_kings == True
          assert config.pieces_per_player == 20
          assert config.strategic_depth == 6


      .. autolink-examples:: international_draughts
         :collapse:


   .. py:method:: performance() -> CheckersAgentConfig
      :classmethod:


      Create configuration optimized for maximum performance.

      Performance configuration features:
      - Maximum parallel processing
      - Extended memory allocation
      - Optimized analysis depth
      - Endgame tablebase support
      - Balanced for speed and strength

      :returns: Configuration optimized for maximum performance.
      :rtype: CheckersAgentConfig

      .. rubric:: Examples

      Setting up high-performance game::\n

          config = CheckersAgentConfig.performance()
          agent = CheckersAgent(config)
          # Optimized for speed and strength

      Performance characteristics::\n

          config = CheckersAgentConfig.performance()
          assert config.analysis_threads == 4
          assert config.memory_limit_mb == 1024
          assert config.enable_endgame_tables == True
          assert config.strategic_depth == 6


      .. autolink-examples:: performance
         :collapse:


   .. py:method:: tournament() -> CheckersAgentConfig
      :classmethod:


      Create configuration optimized for tournament play.

      Tournament configuration features:
      - Extended analysis depth for strong play
      - Endgame tablebase support
      - Optimized time controls
      - Enhanced memory allocation
      - Parallel processing support

      :returns: Configuration optimized for competitive tournament play.
      :rtype: CheckersAgentConfig

      .. rubric:: Examples

      Setting up tournament game::\n

          config = CheckersAgentConfig.tournament()
          agent = CheckersAgent(config)
          # Strong AI play suitable for competitions

      Tournament characteristics::\n

          config = CheckersAgentConfig.tournament()
          assert config.strategic_depth == 8
          assert config.enable_endgame_tables == True
          assert config.time_per_move == 30.0
          assert config.analysis_threads == 4


      .. autolink-examples:: tournament
         :collapse:


   .. py:method:: training() -> CheckersAgentConfig
      :classmethod:


      Create configuration optimized for AI training and experimentation.

      Training configuration features:
      - Balanced depth for learning
      - Reasonable resource usage
      - Faster move generation
      - Suitable for iterative improvement
      - Good for experimentation

      :returns: Configuration optimized for AI training and development.
      :rtype: CheckersAgentConfig

      .. rubric:: Examples

      Setting up training environment::\n

          config = CheckersAgentConfig.training()
          agent = CheckersAgent(config)
          # Balanced for learning and experimentation

      Training characteristics::\n

          config = CheckersAgentConfig.training()
          assert config.strategic_depth == 3
          assert config.time_per_move == 5.0
          assert config.memory_limit_mb == 256
          assert config.max_turns == 100


      .. autolink-examples:: training
         :collapse:


   .. py:method:: validate_king_promotion_row(v: int | None, values) -> int
      :classmethod:


      Validate and auto-calculate king promotion row.

      :param v: The specified king promotion row.
      :type v: Optional[int]
      :param values: Other field values for validation context.

      :returns: The validated king promotion row.
      :rtype: int

      :raises ValueError: If promotion row is invalid for the board size.


      .. autolink-examples:: validate_king_promotion_row
         :collapse:


   .. py:attribute:: allow_flying_kings
      :type:  bool
      :value: None



   .. py:attribute:: analysis_threads
      :type:  int
      :value: None



   .. py:attribute:: board_size
      :type:  int
      :value: None



   .. py:attribute:: enable_endgame_tables
      :type:  bool
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:property:: game_variant
      :type: str


      Determine the game variant based on configuration.

      :returns: Game variant name (American, International, Custom).
      :rtype: str

      .. autolink-examples:: game_variant
         :collapse:


   .. py:attribute:: king_promotion_row
      :type:  int | None
      :value: None



   .. py:attribute:: mandatory_jumps
      :type:  bool
      :value: None



   .. py:attribute:: max_turns
      :type:  int
      :value: None



   .. py:attribute:: memory_limit_mb
      :type:  int
      :value: None



   .. py:attribute:: model_config


   .. py:property:: performance_profile
      :type: dict[str, str | int | float]


      Generate performance profile based on configuration.

      :returns: Performance characteristics.
      :rtype: Dict[str, Union[str, int, float]]

      .. autolink-examples:: performance_profile
         :collapse:


   .. py:property:: pieces_per_player
      :type: int


      Calculate number of pieces per player at game start.

      :returns: Number of pieces each player starts with.
      :rtype: int

      .. autolink-examples:: pieces_per_player
         :collapse:


   .. py:property:: playable_squares
      :type: int


      Calculate number of playable (dark) squares on the board.

      :returns: Number of playable squares (half of total squares).
      :rtype: int

      .. autolink-examples:: playable_squares
         :collapse:


   .. py:attribute:: runnable_config
      :type:  langchain_core.runnables.RunnableConfig
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: strategic_depth
      :type:  int
      :value: None



   .. py:attribute:: time_per_move
      :type:  float
      :value: None



   .. py:property:: total_squares
      :type: int


      Calculate total number of squares on the board.

      :returns: Total number of squares (board_size * board_size).
      :rtype: int

      .. autolink-examples:: total_squares
         :collapse:


