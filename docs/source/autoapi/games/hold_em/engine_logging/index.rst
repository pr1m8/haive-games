
:py:mod:`games.hold_em.engine_logging`
======================================

.. py:module:: games.hold_em.engine_logging

Enhanced engine invocation with Rich logging and debugging.


.. autolink-examples:: games.hold_em.engine_logging
   :collapse:

Classes
-------

.. autoapisummary::

   games.hold_em.engine_logging.EngineInvocationLogger
   games.hold_em.engine_logging.LoggedAugLLMConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EngineInvocationLogger:

   .. graphviz::
      :align: center

      digraph inheritance_EngineInvocationLogger {
        node [shape=record];
        "EngineInvocationLogger" [label="EngineInvocationLogger"];
      }

.. autoclass:: games.hold_em.engine_logging.EngineInvocationLogger
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LoggedAugLLMConfig:

   .. graphviz::
      :align: center

      digraph inheritance_LoggedAugLLMConfig {
        node [shape=record];
        "LoggedAugLLMConfig" [label="LoggedAugLLMConfig"];
        "haive.core.engine.aug_llm.AugLLMConfig" -> "LoggedAugLLMConfig";
      }

.. autoclass:: games.hold_em.engine_logging.LoggedAugLLMConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.hold_em.engine_logging.enhance_game_engines
   games.hold_em.engine_logging.enhance_player_engines

.. py:function:: enhance_game_engines(engines: dict[str, haive.core.engine.aug_llm.AugLLMConfig], logger: EngineInvocationLogger | None = None) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Enhance game engines with logging.


   .. autolink-examples:: enhance_game_engines
      :collapse:

.. py:function:: enhance_player_engines(engines: dict[str, haive.core.engine.aug_llm.AugLLMConfig], logger: EngineInvocationLogger | None = None) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Enhance player engines with logging.


   .. autolink-examples:: enhance_player_engines
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.hold_em.engine_logging
   :collapse:
   
.. autolink-skip:: next
