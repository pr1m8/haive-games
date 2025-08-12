
:py:mod:`games.mafia.mock_runner`
=================================

.. py:module:: games.mafia.mock_runner

Mock runner for the Mafia game.

This module provides a simplified version of the Mafia game runner that
uses mock responses instead of actual LLMs, allowing for faster testing
and demonstration without requiring API keys or internet access.

.. rubric:: Example

```bash
python mock_runner.py --players 5 --days 1 --debug
```


.. autolink-examples:: games.mafia.mock_runner
   :collapse:

Classes
-------

.. autoapisummary::

   games.mafia.mock_runner.MockEngine


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MockEngine:

   .. graphviz::
      :align: center

      digraph inheritance_MockEngine {
        node [shape=record];
        "MockEngine" [label="MockEngine"];
      }

.. autoclass:: games.mafia.mock_runner.MockEngine
   :members:
   :undoc-members:
   :show-inheritance:


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

.. py:function:: generate_detective_response(context: dict[str, Any]) -> haive.games.mafia.models.MafiaPlayerDecision

   Generate a mock response for a detective player.


   .. autolink-examples:: generate_detective_response
      :collapse:

.. py:function:: generate_doctor_response(context: dict[str, Any]) -> haive.games.mafia.models.MafiaPlayerDecision

   Generate a mock response for a doctor player.


   .. autolink-examples:: generate_doctor_response
      :collapse:

.. py:function:: generate_mafia_response(context: dict[str, Any]) -> haive.games.mafia.models.MafiaPlayerDecision

   Generate a mock response for a mafia player.


   .. autolink-examples:: generate_mafia_response
      :collapse:

.. py:function:: generate_narrator_response(context: dict[str, Any]) -> haive.games.mafia.models.NarratorDecision

   Generate a mock response for the narrator.


   .. autolink-examples:: generate_narrator_response
      :collapse:

.. py:function:: generate_villager_response(context: dict[str, Any]) -> haive.games.mafia.models.MafiaPlayerDecision

   Generate a mock response for a villager player.


   .. autolink-examples:: generate_villager_response
      :collapse:

.. py:function:: main()

   Main entry point for command-line execution.


   .. autolink-examples:: main
      :collapse:

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


   .. autolink-examples:: run_mafia_game_mock
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.mafia.mock_runner
   :collapse:
   
.. autolink-skip:: next
