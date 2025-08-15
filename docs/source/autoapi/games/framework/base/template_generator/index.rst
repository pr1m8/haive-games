games.framework.base.template_generator
=======================================

.. py:module:: games.framework.base.template_generator

.. autoapi-nested-parse::

   Template generator for game agents (EXPERIMENTAL).

   This experimental module provides a template generator for creating new game
   implementations. It automates the creation of boilerplate code and ensures
   consistency across different game implementations.

   .. warning::

      This module is experimental and its API may change without notice.
      Use with caution in production environments.

   .. rubric:: Example

   >>> # Create templates for a new chess game
   >>> generator = GameTemplateGenerator(
   ...     game_name="Chess",
   ...     player1_name="white",
   ...     player2_name="black",
   ...     enable_analysis=True
   ... )
   >>> generator.generate_templates()

   Typical usage:
       - Initialize the generator with game details
       - Generate all template files at once
       - Customize the generated code for your specific game


   .. autolink-examples:: games.framework.base.template_generator
      :collapse:


Classes
-------

.. autoapisummary::

   games.framework.base.template_generator.GameTemplateGenerator


Module Contents
---------------

.. py:class:: GameTemplateGenerator(game_name: str, player1_name: str = 'player1', player2_name: str = 'player2', enable_analysis: bool = True)

   Experimental template generator for new board game implementations.

   This class automates the creation of boilerplate code for implementing
   new board games within the framework. It generates a complete set of
   files with proper structure, documentation, and type hints.

   .. warning::

      This class is experimental and its API may change without notice.
      Generated code may need manual adjustments for specific games.

   .. attribute:: game_name

      The name of the game (used for class names).

      :type: str

   .. attribute:: player1_name

      Name for player 1.

      :type: str

   .. attribute:: player2_name

      Name for player 2.

      :type: str

   .. attribute:: enable_analysis

      Whether to include analysis in templates.

      :type: bool

   .. attribute:: game_slug

      Slugified version of the game name for file paths.

      :type: str

   .. attribute:: game_class_name

      CamelCase version of game name for class names.

      :type: str

   .. attribute:: base_dir

      Base directory for generated files.

      :type: str

   .. rubric:: Example

   >>> generator = GameTemplateGenerator("Tic Tac Toe")
   >>> generator.generate_templates()
   ✅ Generated template files for Tic Tac Toe in src/haive/agents/agent_games/tic_tac_toe

   Initialize the template generator.

   :param game_name: The name of the game (used for class names).
   :type game_name: str
   :param player1_name: Name for player 1. Defaults to "player1".
   :type player1_name: str, optional
   :param player2_name: Name for player 2. Defaults to "player2".
   :type player2_name: str, optional
   :param enable_analysis: Whether to include analysis in templates.
                           Defaults to True.
   :type enable_analysis: bool, optional

   .. rubric:: Example

   >>> generator = GameTemplateGenerator(
   ...     game_name="Chess",
   ...     player1_name="white",
   ...     player2_name="black"
   ... )


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GameTemplateGenerator
      :collapse:

   .. py:method:: _generate_agent_file() -> None

      Generate the agent.py file with the main agent class.

      This method creates a file containing the game agent class with:
      - Move generation and extraction
      - Position analysis (if enabled)
      - Game state visualization
      - Integration with the framework

      The generated code includes proper error handling and logging.



      .. autolink-examples:: _generate_agent_file
         :collapse:


   .. py:method:: _generate_config_file() -> None

      Generate the config.py file with agent configuration.

      This method creates a file containing:
      - LLM prompt templates for moves and analysis
      - AugLLM configurations for players and analyzers
      - Game-specific agent configuration class

      The generated code includes default configurations that can be customized.



      .. autolink-examples:: _generate_config_file
         :collapse:


   .. py:method:: _generate_example_file() -> None

      Generate an example.py file to demonstrate agent usage.

      This method creates a file containing:
      - Example game setup and configuration
      - Game execution with visualization
      - State history saving

      The generated code serves as a starting point for using the agent.



      .. autolink-examples:: _generate_example_file
         :collapse:


   .. py:method:: _generate_models_file() -> None

      Generate the models.py file with game-specific data models.

      This method creates a file containing Pydantic models for:
      - Game moves
      - Player decisions
      - Game state
      - Analysis (if enabled)

      The generated models include proper type hints, field descriptions,
      and validation rules.



      .. autolink-examples:: _generate_models_file
         :collapse:


   .. py:method:: _generate_state_manager_file() -> None

      Generate the state.py file with game state management logic.

      This method creates a file containing the state manager class with:
      - Game initialization logic
      - Move application logic
      - Legal move generation
      - Game status checking

      The generated code includes placeholders for game-specific logic.



      .. autolink-examples:: _generate_state_manager_file
         :collapse:


   .. py:method:: generate_templates(output_dir: str = None) -> None

      Generate all template files for the game.

      This method creates a complete set of files needed for a new game
      implementation, including models, state management, configuration,
      and example usage.

      :param output_dir: Optional directory to write files to.
                         If not provided, uses the standard package structure.
      :type output_dir: str, optional

      .. rubric:: Example

      >>> generator = GameTemplateGenerator("Chess")
      >>> # Generate in default location
      >>> generator.generate_templates()
      >>> # Generate in custom location
      >>> generator.generate_templates("my_games/chess")


      .. autolink-examples:: generate_templates
         :collapse:


   .. py:attribute:: base_dir
      :value: 'src/haive/agents/agent_games/Uninferable'



   .. py:attribute:: enable_analysis
      :value: True



   .. py:attribute:: game_class_name
      :value: ''



   .. py:attribute:: game_name


   .. py:attribute:: game_slug


   .. py:attribute:: player1_name
      :value: 'player1'



   .. py:attribute:: player2_name
      :value: 'player2'



