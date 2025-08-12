
:py:mod:`games.tic_tac_toe.agent`
=================================

.. py:module:: games.tic_tac_toe.agent

Comprehensive agent implementation for strategic Tic Tac Toe gameplay.

This module provides the core agent class for managing Tic Tac Toe games with
LLM-driven decision-making, strategic analysis, and flexible gameplay modes.
The agent coordinates all aspects of the game including initialization, move
generation, position analysis, and game flow management.

The agent supports:
- LLM-based move generation with perfect play capability
- Strategic position analysis for educational insights
- Flexible game flow with conditional analysis
- Board visualization for interactive gameplay
- Error handling and state validation
- Integration with LangGraph for distributed execution
- Multiple AI personalities through engine configuration

.. rubric:: Examples

Basic game execution::

    config = TicTacToeConfig.default_config()
    agent = TicTacToeAgent(config)
    final_state = agent.run_game()

Tournament play without visualization::

    config = TicTacToeConfig.competitive_config()
    agent = TicTacToeAgent(config)
    result = agent.run_game(visualize=False)

Educational game with analysis::

    config = TicTacToeConfig.educational_config()
    agent = TicTacToeAgent(config)
    agent.run_game(visualize=True, debug=True)

Custom engine configuration::

    config = TicTacToeConfig(
        engines=custom_engines,
        enable_analysis=True
    )
    agent = TicTacToeAgent(config)

.. note::

   The agent uses LangGraph for workflow management and supports
   concurrent execution with proper state reducers.


.. autolink-examples:: games.tic_tac_toe.agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.tic_tac_toe.agent.TicTacToeAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TicTacToeAgent:

   .. graphviz::
      :align: center

      digraph inheritance_TicTacToeAgent {
        node [shape=record];
        "TicTacToeAgent" [label="TicTacToeAgent"];
        "haive.games.framework.base.agent.GameAgent[haive.games.tic_tac_toe.config.TicTacToeConfig]" -> "TicTacToeAgent";
      }

.. autoclass:: games.tic_tac_toe.agent.TicTacToeAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.tic_tac_toe.agent
   :collapse:
   
.. autolink-skip:: next
