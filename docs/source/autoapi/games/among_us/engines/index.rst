games.among_us.engines
======================

.. py:module:: games.among_us.engines


Classes
-------

.. autoapisummary::

   games.among_us.engines.AmongUsEngines


Module Contents
---------------

.. py:class:: AmongUsEngines

   Engines for the Among Us game.

   This class creates and manages the LLM engines used for different player roles and
   game phases.



   .. autolink-examples:: AmongUsEngines
      :collapse:

   .. py:method:: create_engines(llm_config: dict[str, Any] | None = None) -> dict[str, dict[str, haive.core.engine.aug_llm.AugLLMConfig]]
      :classmethod:


      Create the engines for the Among Us game.

      :param llm_config: Optional configuration for the language model

      :returns: A dictionary of engines organized by role and game phase


      .. autolink-examples:: create_engines
         :collapse:


   .. py:method:: create_runnable_engines(llm_config: dict[str, Any] | None = None) -> dict[str, dict[str, Any]]
      :classmethod:


      Create runnable engines for the Among Us game.

      :param llm_config: Optional configuration for the language model

      :returns: A dictionary of runnable engines organized by role and game phase


      .. autolink-examples:: create_runnable_engines
         :collapse:


