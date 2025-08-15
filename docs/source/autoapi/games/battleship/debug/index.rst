games.battleship.debug
======================

.. py:module:: games.battleship.debug

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


   .. autolink-examples:: games.battleship.debug
      :collapse:


Attributes
----------

.. autoapisummary::

   games.battleship.debug.console


Functions
---------

.. autoapisummary::

   games.battleship.debug.test_battleship


Module Contents
---------------

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


   .. autolink-examples:: test_battleship
      :collapse:

.. py:data:: console

