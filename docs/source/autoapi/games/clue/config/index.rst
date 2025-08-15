games.clue.config
=================

.. py:module:: games.clue.config

.. autoapi-nested-parse::

   Comprehensive configuration system for the Clue (Cluedo) mystery game agent.

   This module defines the configuration system for the Clue game agent, providing
   complete control over game mechanics, AI behavior, analysis settings, and
   visualization options. The configuration system supports both casual and
   competitive gameplay modes with extensive customization options.

   The configuration manages:
   - Game state schema and persistence
   - AI engine configurations and behavior
   - Analysis and reasoning settings
   - Visualization and UI options
   - Game flow and turn management
   - Solution generation and validation
   - Player interaction modes

   Key Features:
       - Flexible game parameter configuration
       - Multiple AI difficulty levels
       - Comprehensive analysis and logging
       - Customizable visualization options
       - Solution pre-configuration for testing
       - Turn limit and timeout management
       - Player order customization

   .. rubric:: Examples

   Basic configuration::

       from haive.games.clue.config import ClueConfig

       # Create default configuration
       config = ClueConfig()
       print(f"Game: {config.name} v{config.version}")
       print(f"Max turns: {config.max_turns}")
       print(f"Analysis enabled: {config.enable_analysis}")

   Custom configuration::

       from haive.games.clue.models import ClueSolution, ValidSuspect, ValidWeapon, ValidRoom

       # Create custom game configuration
       custom_solution = {
           "suspect": ValidSuspect.COLONEL_MUSTARD.value,
           "weapon": ValidWeapon.KNIFE.value,
           "room": ValidRoom.KITCHEN.value
       }

       config = ClueConfig(
           max_turns=15,
           first_player="player2",
           solution=custom_solution,
           enable_analysis=False,
           visualize=False
       )

   Configuration validation::

       config = ClueConfig()

       # Validate configuration
       assert config.max_turns > 0
       assert config.first_player in ["player1", "player2"]
       assert config.state_schema == ClueState
       assert isinstance(config.enable_analysis, bool)

   The configuration system integrates seamlessly with the game engine and provides
   all necessary parameters for consistent and customizable gameplay experiences.


   .. autolink-examples:: games.clue.config
      :collapse:


Attributes
----------

.. autoapisummary::

   games.clue.config.VERSION


Classes
-------

.. autoapisummary::

   games.clue.config.ClueConfig


Module Contents
---------------

.. py:class:: ClueConfig

   Bases: :py:obj:`haive.games.framework.base.config.GameConfig`


   Comprehensive configuration for the Clue game agent.

   This class defines all configuration parameters for the Clue game agent,
   providing complete control over game mechanics, AI behavior, analysis
   settings, and visualization options. The configuration supports both
   casual and competitive gameplay modes with extensive customization.

   The configuration manages game flow, player interactions, AI reasoning,
   solution generation, and performance optimization. It integrates with
   the game engine to provide consistent and customizable gameplay
   experiences.

   .. attribute:: name

      Unique identifier for the game type.
      Used for logging, metrics, and game selection.

   .. attribute:: version

      Version string for tracking implementation changes.
      Follows semantic versioning (major.minor.patch).

   .. attribute:: state_schema

      Pydantic model class for game state management.
      Defines the structure and validation for game data.

   .. attribute:: enable_analysis

      Whether to enable AI position analysis.
      Affects performance and decision-making quality.

   .. attribute:: visualize

      Whether to enable game visualization.
      Controls UI rendering and display updates.

   .. attribute:: max_turns

      Maximum number of turns before game timeout.
      Prevents infinite games and ensures completion.

   .. attribute:: first_player

      Which player starts the game.
      Must be either "player1" or "player2".

   .. attribute:: solution

      Predetermined solution for testing and tutorials.
      If None, a random solution will be generated.

   .. rubric:: Examples

   Default configuration::

       config = ClueConfig()
       assert config.name == "clue"
       assert config.max_turns == 20
       assert config.first_player == "player1"
       assert config.enable_analysis == True
       assert config.visualize == True
       assert config.solution is None

   Custom configuration::

       from haive.games.clue.models import ValidSuspect, ValidWeapon, ValidRoom

       # Create specific solution for testing
       test_solution = {
           "suspect": ValidSuspect.COLONEL_MUSTARD.value,
           "weapon": ValidWeapon.KNIFE.value,
           "room": ValidRoom.KITCHEN.value
       }

       config = ClueConfig(
           max_turns=15,
           first_player="player2",
           solution=test_solution,
           enable_analysis=False,
           visualize=False
       )

   Performance optimization::

       # High-performance configuration for batch processing
       config = ClueConfig(
           enable_analysis=False,  # Disable analysis for speed
           visualize=False,        # Disable visualization for speed
           max_turns=10           # Shorter games for faster completion
       )

   Tutorial configuration::

       # Educational configuration with predetermined solution
       tutorial_solution = {
           "suspect": ValidSuspect.MISS_SCARLET.value,
           "weapon": ValidWeapon.CANDLESTICK.value,
           "room": ValidRoom.LIBRARY.value
       }

       config = ClueConfig(
           solution=tutorial_solution,
           max_turns=30,          # More turns for learning
           enable_analysis=True,   # Show AI reasoning
           visualize=True         # Show game progression
       )

   .. note::

      The solution parameter accepts a dictionary with 'suspect', 'weapon',
      and 'room' keys. Values should be the string values from the
      corresponding enum classes, not the enum instances themselves.


   .. autolink-examples:: ClueConfig
      :collapse:

   .. py:method:: benchmark_game(max_turns: int = 10) -> ClueConfig
      :classmethod:


      Create configuration for performance benchmarking.

      Features:
      - Minimal turn limit for fast completion
      - Analysis disabled for performance
      - Visualization disabled for speed
      - Random solution generation

      :param max_turns: Maximum number of turns (default: 10).

      :returns: Benchmark game configuration.
      :rtype: ClueConfig

      .. rubric:: Examples

      Creating a benchmark game::

          config = ClueConfig.benchmark_game()
          assert config.max_turns == 10
          assert config.enable_analysis == False
          assert config.visualize == False
          assert config.solution is None

      Custom benchmark configuration::

          config = ClueConfig.benchmark_game(max_turns=5)
          assert config.max_turns == 5


      .. autolink-examples:: benchmark_game
         :collapse:


   .. py:method:: casual_game(max_turns: int = 25) -> ClueConfig
      :classmethod:


      Create configuration for casual gameplay.

      Features:
      - Extended turn limit for relaxed play
      - Analysis enabled for learning
      - Visualization enabled for engagement
      - Random solution generation

      :param max_turns: Maximum number of turns (default: 25).

      :returns: Casual game configuration.
      :rtype: ClueConfig

      .. rubric:: Examples

      Creating a casual game::

          config = ClueConfig.casual_game()
          assert config.max_turns == 25
          assert config.enable_analysis == True
          assert config.visualize == True
          assert config.solution is None

      Custom casual game::

          config = ClueConfig.casual_game(max_turns=30)
          assert config.max_turns == 30


      .. autolink-examples:: casual_game
         :collapse:


   .. py:method:: competitive_game(max_turns: int = 15) -> ClueConfig
      :classmethod:


      Create configuration for competitive gameplay.

      Features:
      - Reduced turn limit for faster games
      - Analysis disabled for challenge
      - Visualization optional for focus
      - Random solution generation

      :param max_turns: Maximum number of turns (default: 15).

      :returns: Competitive game configuration.
      :rtype: ClueConfig

      .. rubric:: Examples

      Creating a competitive game::

          config = ClueConfig.competitive_game()
          assert config.max_turns == 15
          assert config.enable_analysis == False
          assert config.visualize == False
          assert config.solution is None

      Tournament configuration::

          config = ClueConfig.competitive_game(max_turns=12)
          assert config.max_turns == 12


      .. autolink-examples:: competitive_game
         :collapse:


   .. py:method:: tutorial_game(solution_dict: dict | None = None) -> ClueConfig
      :classmethod:


      Create configuration for tutorial/educational gameplay.

      Features:
      - Extended turn limit for learning
      - Analysis enabled for understanding
      - Visualization enabled for instruction
      - Predetermined solution for consistency

      :param solution_dict: Specific solution dictionary. If None, uses Colonel Mustard example.

      :returns: Tutorial game configuration.
      :rtype: ClueConfig

      .. rubric:: Examples

      Creating a tutorial game::

          config = ClueConfig.tutorial_game()
          assert config.max_turns == 30
          assert config.enable_analysis == True
          assert config.visualize == True
          assert config.solution is not None

      Custom tutorial solution::

          from haive.games.clue.models import ValidSuspect, ValidWeapon, ValidRoom

          custom_solution = {
              "suspect": ValidSuspect.PROFESSOR_PLUM.value,
              "weapon": ValidWeapon.CANDLESTICK.value,
              "room": ValidRoom.LIBRARY.value
          }
          config = ClueConfig.tutorial_game(solution_dict=custom_solution)
          assert config.solution == custom_solution


      .. autolink-examples:: tutorial_game
         :collapse:


   .. py:attribute:: enable_analysis
      :type:  bool
      :value: None



   .. py:attribute:: first_player
      :type:  str
      :value: None



   .. py:attribute:: max_turns
      :type:  int
      :value: None



   .. py:attribute:: model_config


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: solution
      :type:  dict | None
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.games.clue.state.ClueState]
      :value: None



   .. py:attribute:: version
      :type:  str
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: None



.. py:data:: VERSION
   :value: '1.0.0'


