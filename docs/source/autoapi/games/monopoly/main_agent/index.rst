games.monopoly.main_agent
=========================

.. py:module:: games.monopoly.main_agent

.. autoapi-nested-parse::

   Fixed Main Monopoly agent that orchestrates the complete game.

   This module provides the corrected main agent implementation that:
       - Ensures BaseModel consistency throughout (no dict conversions)
       - Properly handles state schema compatibility
       - Fixes the validation error by maintaining BaseModel state


   .. autolink-examples:: games.monopoly.main_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   games.monopoly.main_agent.logger


Classes
-------

.. autoapisummary::

   games.monopoly.main_agent.MonopolyAgent


Module Contents
---------------

.. py:class:: MonopolyAgent(config: haive.games.monopoly.game_agent.MonopolyGameAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.games.monopoly.game_agent.MonopolyGameAgentConfig`\ ]


   Main Monopoly agent that orchestrates the complete game.

   This agent combines:
       - Game rule enforcement and turn management
       - Player decision delegation to subgraphs
       - Complete game state management
       - Game end detection and winner determination


   Initialize the monopoly agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MonopolyAgent
      :collapse:

   .. py:method:: _display_final_results(final_state: haive.games.monopoly.state.MonopolyState) -> None

      Display final game results.


      .. autolink-examples:: _display_final_results
         :collapse:


   .. py:method:: get_game_summary() -> dict[str, Any]

      Get a summary of the game configuration and status.


      .. autolink-examples:: get_game_summary
         :collapse:


   .. py:method:: save_game_history(filename: str | None = None) -> None

      Save game history to a file.


      .. autolink-examples:: save_game_history
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the complete monopoly workflow.

      This creates the main game workflow nodes and connects them properly.



      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: start_game() -> haive.games.monopoly.state.MonopolyState

      Start a new monopoly game.

      CRITICAL: Keep everything as BaseModel - no dict conversions!

      :returns: Final game state as MonopolyState BaseModel


      .. autolink-examples:: start_game
         :collapse:


   .. py:attribute:: initial_state


   .. py:attribute:: player_agent


.. py:data:: logger

