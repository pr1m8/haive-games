games.mafia.mock_runner
=======================

.. py:module:: games.mafia.mock_runner

.. autoapi-nested-parse::

   Mock runner for the Mafia game.

   This module provides a simplified version of the Mafia game runner that
   uses mock responses instead of actual LLMs, allowing for faster testing
   and demonstration without requiring API keys or internet access.

   .. rubric:: Examples

   ```bash
   python mock_runner.py --players 5 --days 1 --debug
   ```



Attributes
----------

.. autoapisummary::

   games.mafia.mock_runner.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/mafia/mock_runner/MockEngine

.. autoapisummary::

   games.mafia.mock_runner.MockEngine


Functions
---------

.. autoapisummary::

   games.mafia.mock_runner.generate_detective_response
   games.mafia.mock_runner.generate_doctor_response
   games.mafia.mock_runner.generate_mafia_response
   games.mafia.mock_runner.generate_narrator_response
   games.mafia.mock_runner.generate_villager_response
   games.mafia.mock_runner.main
   games.mafia.mock_runner.run_mafia_game_mock


Module Contents
---------------

.. py:function:: generate_detective_response(context: dict[str, Any]) -> haive.games.mafia.models.MafiaPlayerDecision

   Generate a mock response for a detective player.


.. py:function:: generate_doctor_response(context: dict[str, Any]) -> haive.games.mafia.models.MafiaPlayerDecision

   Generate a mock response for a doctor player.


.. py:function:: generate_mafia_response(context: dict[str, Any]) -> haive.games.mafia.models.MafiaPlayerDecision

   Generate a mock response for a mafia player.


.. py:function:: generate_narrator_response(context: dict[str, Any]) -> haive.games.mafia.models.NarratorDecision

   Generate a mock response for the narrator.


.. py:function:: generate_villager_response(context: dict[str, Any]) -> haive.games.mafia.models.MafiaPlayerDecision

   Generate a mock response for a villager player.


.. py:function:: main()

   Main entry point for command-line execution.


.. py:function:: run_mafia_game_mock(player_count: int = 5, max_days: int = 1, debug: bool = True) -> None

   Run a mock Mafia game simulation with synthetic responses.

   This function sets up and executes a full Mafia game, handling:
       - Player creation and role assignment
       - Game state initialization
       - Turn-based gameplay execution using mock responses
       - State visualization
       - Game end conditions

   :param player_count: Total number of players including narrator.
                        Must be at least 4 (3 players + narrator). Defaults to 5.
   :param max_days: Maximum number of in-game days before forcing
                    game end. Defaults to 1.
   :param debug: Enable debug mode for detailed logging.
                 Defaults to True.

   :raises ValueError: If player_count is less than 4.


.. py:data:: logger

