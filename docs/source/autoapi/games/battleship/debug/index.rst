games.battleship.debug
======================

.. py:module:: games.battleship.debug

Debug script for testing Battleship game.

This module provides a debugging interface for the Battleship game,
with detailed logging and visualization of game state at each step.
It's designed for:
    - Diagnosing game logic issues
    - Visualizing internal state transitions
    - Testing new features and configurations
    - Analyzing LLM decision making

Run this script directly to start a debug session:
    python -m haive.games.battleship.debug



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Debug script for testing Battleship game.

   This module provides a debugging interface for the Battleship game,
   with detailed logging and visualization of game state at each step.
   It's designed for:
       - Diagnosing game logic issues
       - Visualizing internal state transitions
       - Testing new features and configurations
       - Analyzing LLM decision making

   Run this script directly to start a debug session:
       python -m haive.games.battleship.debug



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.battleship.debug.console

            
            
            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.battleship.debug.test_battleship

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: test_battleship()

            Run a test game of Battleship with detailed logging.

            Creates and runs a Battleship game in debug mode, displaying detailed
            information about each step of the game, including:
                - Game phase and player turns
                - Ship placements during setup
                - Move history and results
                - Strategic analysis from LLMs
                - Error messages and game status

            This function is useful for:
                - Diagnosing issues with game logic
                - Validating LLM outputs and decisions
                - Testing state transitions and error handling
                - Visualizing the internal game state

            :returns: None

            :raises Exception: Catches and logs any exceptions that occur during gameplay



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: console




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.battleship.debug import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

