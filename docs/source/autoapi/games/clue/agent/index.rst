games.clue.agent
================

.. py:module:: games.clue.agent

Comprehensive agent implementation for the Clue (Cluedo) mystery game.

This module provides the complete agent implementation for the Clue game,
managing game state, player interactions, AI decision-making, and visualization.
The agent orchestrates the entire gameplay experience from initialization
through completion, handling all game mechanics and player coordination.

The agent system provides:
- Game state initialization and management
- Player action coordination and validation
- AI decision-making and reasoning
- Real-time game visualization and logging
- Game completion detection and handling
- Performance monitoring and optimization

Key Features:
    - Complete game orchestration from start to finish
    - Real-time visualization with detailed game state display
    - Robust error handling and edge case management
    - Performance monitoring and game completion detection
    - Comprehensive logging for debugging and analysis
    - Integration with the Haive agent framework

.. rubric:: Examples

Basic agent usage::

    from haive.games.clue.agent import ClueAgent
    from haive.games.clue.config import ClueConfig

    # Create agent with default configuration
    agent = ClueAgent()

    # Run a complete game
    final_state = agent.run_game()
    print(f"Game completed with status: {final_state['game_status']}")

Custom configuration::

    from haive.games.clue.config import ClueConfig

    # Create custom configuration
    config = ClueConfig.competitive_game(max_turns=15)
    agent = ClueAgent(config)

    # Run game without visualization for performance
    final_state = agent.run_game(visualize=False)

Game state management::

    # Initialize game state
    initial_state = agent.initialize_game({})

    # Visualize current state
    agent.visualize_state(initial_state)

    # Check game completion
    from haive.games.clue.state import ClueState
    state = ClueState(**initial_state)
    if state.is_game_over:
        print(f"Game ended! Winner: {state.winner}")

The agent integrates seamlessly with the Haive framework and provides complete
functionality for running Clue games with AI players, visualization, and
comprehensive state management.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Comprehensive agent implementation for the Clue (Cluedo) mystery game.

   This module provides the complete agent implementation for the Clue game,
   managing game state, player interactions, AI decision-making, and visualization.
   The agent orchestrates the entire gameplay experience from initialization
   through completion, handling all game mechanics and player coordination.

   The agent system provides:
   - Game state initialization and management
   - Player action coordination and validation
   - AI decision-making and reasoning
   - Real-time game visualization and logging
   - Game completion detection and handling
   - Performance monitoring and optimization

   Key Features:
       - Complete game orchestration from start to finish
       - Real-time visualization with detailed game state display
       - Robust error handling and edge case management
       - Performance monitoring and game completion detection
       - Comprehensive logging for debugging and analysis
       - Integration with the Haive agent framework

   .. rubric:: Examples

   Basic agent usage::

       from haive.games.clue.agent import ClueAgent
       from haive.games.clue.config import ClueConfig

       # Create agent with default configuration
       agent = ClueAgent()

       # Run a complete game
       final_state = agent.run_game()
       print(f"Game completed with status: {final_state['game_status']}")

   Custom configuration::

       from haive.games.clue.config import ClueConfig

       # Create custom configuration
       config = ClueConfig.competitive_game(max_turns=15)
       agent = ClueAgent(config)

       # Run game without visualization for performance
       final_state = agent.run_game(visualize=False)

   Game state management::

       # Initialize game state
       initial_state = agent.initialize_game({})

       # Visualize current state
       agent.visualize_state(initial_state)

       # Check game completion
       from haive.games.clue.state import ClueState
       state = ClueState(**initial_state)
       if state.is_game_over:
           print(f"Game ended! Winner: {state.winner}")

   The agent integrates seamlessly with the Haive framework and provides complete
   functionality for running Clue games with AI players, visualization, and
   comprehensive state management.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.clue.agent.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.clue.agent.ClueAgent

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ClueAgent(config: haive.games.clue.config.ClueConfig = ClueConfig())

            Bases: :py:obj:`haive.games.framework.base.agent.GameAgent`\ [\ :py:obj:`haive.games.clue.config.ClueConfig`\ ]


            Comprehensive agent for playing Clue (Cluedo) mystery games.

            This class implements the complete Clue game agent, managing all aspects
            of gameplay including state management, player coordination, AI decision-making,
            and visualization. The agent orchestrates the entire game experience from
            initialization through completion.

            The agent handles:
            - Game state initialization with proper solution generation
            - Player action coordination and turn management
            - AI decision-making and reasoning processes
            - Real-time game visualization and logging
            - Game completion detection and result handling
            - Performance monitoring and optimization

            The agent integrates with the Haive framework to provide a complete
            gaming experience with configurable AI behavior, visualization options,
            and comprehensive state management.

            .. attribute:: state_manager

               The state management system for game logic.
               Handles all game state transitions and validation.

            .. attribute:: config

               The configuration object controlling agent behavior.
               Defines game parameters, AI settings, and visualization options.

            .. rubric:: Examples

            Basic agent creation::

                from haive.games.clue.agent import ClueAgent

                # Create agent with default configuration
                agent = ClueAgent()

                # Run a complete game
                final_state = agent.run_game()
                print(f"Game status: {final_state['game_status']}")

            Custom configuration::

                from haive.games.clue.config import ClueConfig

                # Create competitive configuration
                config = ClueConfig.competitive_game(max_turns=15)
                agent = ClueAgent(config)

                # Run high-performance game
                final_state = agent.run_game(visualize=False)

            Tutorial mode::

                # Create tutorial configuration
                config = ClueConfig.tutorial_game()
                agent = ClueAgent(config)

                # Run educational game with predetermined solution
                final_state = agent.run_game(visualize=True)

            .. note::

               The agent requires a configured state manager and proper game
               configuration to function correctly. All game logic is delegated
               to the state manager to maintain separation of concerns.

            Initialize the Clue agent with configuration.

            Sets up the agent with the specified configuration and initializes
            the state management system. The agent is ready to run games after
            initialization.

            :param config: The configuration for the Clue game.
                           Controls game parameters, AI behavior, and visualization options.
                           Defaults to standard configuration if not provided.

            .. rubric:: Examples

            Default initialization::

                agent = ClueAgent()
                assert agent.config.max_turns == 20
                assert agent.config.enable_analysis == True
                assert agent.config.visualize == True

            Custom configuration::

                from haive.games.clue.config import ClueConfig

                config = ClueConfig(
                    max_turns=15,
                    enable_analysis=False,
                    visualize=False
                )
                agent = ClueAgent(config)
                assert agent.config.max_turns == 15

            Factory method configuration::

                config = ClueConfig.competitive_game()
                agent = ClueAgent(config)
                assert agent.config.enable_analysis == False


            .. py:method:: initialize_game(state: dict[str, Any]) -> dict[str, Any]

               Initialize the Clue game with proper state setup.

               Creates a new game state with appropriate configuration settings,
               including solution generation, card dealing, and player setup.
               The initialization process sets up all necessary game components
               for a complete Clue experience.

               :param state: Initial state dictionary (unused here but required for interface).
                             Maintained for compatibility with the GameAgent interface.

               :returns:

                         New game state dictionary ready for gameplay.
                             Contains all game information including solution, player cards,
                             and initial game parameters.
               :rtype: dict[str, Any]

               .. rubric:: Examples

               Basic initialization::

                   agent = ClueAgent()
                   initial_state = agent.initialize_game({})

                   # Verify game state structure
                   assert "solution" in initial_state
                   assert "player1_cards" in initial_state
                   assert "player2_cards" in initial_state
                   assert initial_state["current_player"] == "player1"
                   assert initial_state["game_status"] == "ongoing"

               Custom configuration initialization::

                   from haive.games.clue.config import ClueConfig

                   config = ClueConfig(
                       first_player="player2",
                       max_turns=15
                   )
                   agent = ClueAgent(config)
                   initial_state = agent.initialize_game({})

                   assert initial_state["current_player"] == "player2"
                   assert initial_state["max_turns"] == 15

               Predetermined solution::

                   from haive.games.clue.models import ValidSuspect, ValidWeapon, ValidRoom

                   solution = {
                       "suspect": ValidSuspect.COLONEL_MUSTARD.value,
                       "weapon": ValidWeapon.KNIFE.value,
                       "room": ValidRoom.KITCHEN.value
                   }
                   config = ClueConfig(solution=solution)
                   agent = ClueAgent(config)
                   initial_state = agent.initialize_game({})

                   assert initial_state["solution"]["suspect"] == "Colonel Mustard"
                   assert initial_state["solution"]["weapon"] == "Knife"
                   assert initial_state["solution"]["room"] == "Kitchen"

               .. note::

                  The state parameter is unused in this implementation but is
                  maintained for interface compatibility. All initialization
                  parameters come from the agent's configuration object.



            .. py:method:: run_game(visualize: bool = True) -> dict[str, Any]

               Run a complete Clue game with optional visualization and monitoring.

               Executes a full game from initialization to completion, with optional
               real-time visualization and comprehensive monitoring for game completion
               and performance. The method handles all game flow and provides robust
               error handling and loop detection.

               :param visualize: Whether to visualize each game state.
                                 Overrides the agent's configuration visualization setting.
                                 True enables real-time game display, False runs silently.

               :returns:

                         The final game state dictionary.
                             Contains complete game results including winner, solution,
                             and full game history.
               :rtype: dict[str, Any]

               .. rubric:: Examples

               Basic game execution::

                   agent = ClueAgent()
                   final_state = agent.run_game()

                   # Check results
                   print(f"Game status: {final_state['game_status']}")
                   print(f"Winner: {final_state.get('winner', 'No winner')}")
                   print(f"Total turns: {len(final_state['guesses'])}")

               Silent game execution::

                   agent = ClueAgent()
                   final_state = agent.run_game(visualize=False)

                   # Faster execution without visualization
                   assert final_state['game_status'] in ['player1_win', 'player2_win']

               Performance monitoring::

                   import time
                   start_time = time.time()

                   agent = ClueAgent()
                   final_state = agent.run_game(visualize=False)

                   duration = time.time() - start_time
                   print(f"Game completed in {duration:.2f} seconds")
                   print(f"Final turn: {len(final_state['guesses'])}")

               Configuration-based execution::

                   # Use competitive configuration
                   config = ClueConfig.competitive_game(max_turns=15)
                   agent = ClueAgent(config)
                   final_state = agent.run_game()

                   # Should finish within 15 turns
                   assert len(final_state['guesses']) <= 15

               .. note::

                  The method includes infinite loop detection to prevent games
                  from running indefinitely. If the maximum turns are reached
                  or the game state stops changing, the game will be automatically
                  terminated with appropriate logging.



            .. py:method:: visualize_state(state: dict[str, Any]) -> None

               Visualize the current game state with comprehensive display.

               Provides a detailed visual representation of the current game state,
               including game progress, player information, guess history, and
               solution details (when appropriate). The visualization is designed
               to be informative and easy to read.

               :param state: The state dictionary to visualize.
                             Must contain all necessary game state information.

               .. rubric:: Examples

               Basic visualization::

                   agent = ClueAgent()
                   initial_state = agent.initialize_game({})
                   agent.visualize_state(initial_state)
                   # Outputs:
                   # ==================================================
                   # 🎮 Game: Clue v1.0.0
                   # 📊 Turn: 1/20
                   # 🎭 Current Player: player1
                   # 📝 Status: ongoing
                   # ==================================================
                   # No guesses yet.

               Game in progress::

                   # After some gameplay
                   agent.visualize_state(current_state)
                   # Outputs:
                   # ==================================================
                   # 🎮 Game: Clue v1.0.0
                   # 📊 Turn: 5/20
                   # 🎭 Current Player: player2
                   # 📝 Status: ongoing
                   # ==================================================
                   # Turn 1: Colonel Mustard, Knife, Kitchen | Response: Alice
                   # Turn 2: Professor Plum, Candlestick, Library | Response: No card shown
                   # ...

               Game completion::

                   # When game ends
                   agent.visualize_state(final_state)
                   # Outputs:
                   # ==================================================
                   # 🎮 Game: Clue v1.0.0
                   # 📊 Turn: 8/20
                   # 🎭 Current Player: player1
                   # 📝 Status: player1_win
                   # 🔑 Solution: Colonel Mustard, Knife, Kitchen
                   # ==================================================
                   # [Full game history displayed]

               .. note::

                  Visualization is controlled by the agent's configuration.
                  If visualize=False, this method returns immediately without
                  displaying anything. The display includes emoji icons for
                  better readability and visual appeal.



            .. py:attribute:: state_manager



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.clue.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

