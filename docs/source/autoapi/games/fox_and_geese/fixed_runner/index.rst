games.fox_and_geese.fixed_runner
================================

.. py:module:: games.fox_and_geese.fixed_runner

.. autoapi-nested-parse::

   Fixed runner for Fox and Geese game without LangGraph streaming issues.


   .. autolink-examples:: games.fox_and_geese.fixed_runner
      :collapse:


Attributes
----------

.. autoapisummary::

   games.fox_and_geese.fixed_runner.logger


Classes
-------

.. autoapisummary::

   games.fox_and_geese.fixed_runner.FixedFoxAndGeeseAgent


Functions
---------

.. autoapisummary::

   games.fox_and_geese.fixed_runner.main
   games.fox_and_geese.fixed_runner.parse_arguments


Module Contents
---------------

.. py:class:: FixedFoxAndGeeseAgent

   Bases: :py:obj:`haive.games.fox_and_geese.agent.FoxAndGeeseAgent`


   Fixed Fox and Geese agent that handles state directly.


   .. autolink-examples:: FixedFoxAndGeeseAgent
      :collapse:

   .. py:method:: run_fixed_game(delay: float = 1.0, max_moves: int = 100) -> haive.games.fox_and_geese.state.FoxAndGeeseState

      Run the Fox and Geese game step by step, managing state directly.

      This bypasses LangGraph's stream method, which can have issues with certain state types.

      :param delay: Time delay between moves for better visualization
      :param max_moves: Maximum number of moves before forcing a draw

      :returns: Final game state


      .. autolink-examples:: run_fixed_game
         :collapse:


.. py:function:: main()

   Run the Fox and Geese game with the fixed runner.


   .. autolink-examples:: main
      :collapse:

.. py:function:: parse_arguments()

   Parse command line arguments.


   .. autolink-examples:: parse_arguments
      :collapse:

.. py:data:: logger

