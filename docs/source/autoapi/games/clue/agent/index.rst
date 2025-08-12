
:py:mod:`games.clue.agent`
==========================

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


.. autolink-examples:: games.clue.agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.clue.agent.ClueAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ClueAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ClueAgent {
        node [shape=record];
        "ClueAgent" [label="ClueAgent"];
        "haive.games.framework.base.agent.GameAgent[haive.games.clue.config.ClueConfig]" -> "ClueAgent";
      }

.. autoclass:: games.clue.agent.ClueAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.clue.agent
   :collapse:
   
.. autolink-skip:: next
