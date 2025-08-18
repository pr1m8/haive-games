games.mafia.mock_runner
=======================

.. py:module:: games.mafia.mock_runner

Mock runner for the Mafia game.

This module provides a simplified version of the Mafia game runner that
uses mock responses instead of actual LLMs, allowing for faster testing
and demonstration without requiring API keys or internet access.

.. rubric:: Example

```bash
python mock_runner.py --players 5 --days 1 --debug
```



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">7 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Mock runner for the Mafia game.

   This module provides a simplified version of the Mafia game runner that
   uses mock responses instead of actual LLMs, allowing for faster testing
   and demonstration without requiring API keys or internet access.

   .. rubric:: Example

   ```bash
   python mock_runner.py --players 5 --days 1 --debug
   ```



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.mafia.mock_runner.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.mafia.mock_runner.MockEngine

            

.. admonition:: Functions (7)
   :class: info

   .. autoapisummary::

      games.mafia.mock_runner.generate_detective_response
      games.mafia.mock_runner.generate_doctor_response
      games.mafia.mock_runner.generate_mafia_response
      games.mafia.mock_runner.generate_narrator_response
      games.mafia.mock_runner.generate_villager_response
      games.mafia.mock_runner.main
      games.mafia.mock_runner.run_mafia_game_mock

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MockEngine(role)

            A mock engine that returns predefined responses.


            .. py:method:: invoke(context)

               Generate a mock response based on the role.



            .. py:attribute:: role



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_detective_response(context: dict[str, Any]) -> haive.games.mafia.models.MafiaPlayerDecision

            Generate a mock response for a detective player.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_doctor_response(context: dict[str, Any]) -> haive.games.mafia.models.MafiaPlayerDecision

            Generate a mock response for a doctor player.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_mafia_response(context: dict[str, Any]) -> haive.games.mafia.models.MafiaPlayerDecision

            Generate a mock response for a mafia player.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_narrator_response(context: dict[str, Any]) -> haive.games.mafia.models.NarratorDecision

            Generate a mock response for the narrator.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_villager_response(context: dict[str, Any]) -> haive.games.mafia.models.MafiaPlayerDecision

            Generate a mock response for a villager player.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main()

            Main entry point for command-line execution.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.mafia.mock_runner import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

