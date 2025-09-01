games.hold_em.engine_logging
============================

.. py:module:: games.hold_em.engine_logging

.. autoapi-nested-parse::

   Enhanced engine invocation with Rich logging and debugging.



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/hold_em/engine_logging/EngineInvocationLogger
   /autoapi/games/hold_em/engine_logging/LoggedAugLLMConfig

.. autoapisummary::

   games.hold_em.engine_logging.EngineInvocationLogger
   games.hold_em.engine_logging.LoggedAugLLMConfig


Functions
---------

.. autoapisummary::

   games.hold_em.engine_logging.enhance_game_engines
   games.hold_em.engine_logging.enhance_player_engines


Module Contents
---------------

.. py:function:: enhance_game_engines(engines: dict[str, haive.core.engine.aug_llm.AugLLMConfig], logger: EngineInvocationLogger | None = None) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Enhance game engines with logging.


.. py:function:: enhance_player_engines(engines: dict[str, haive.core.engine.aug_llm.AugLLMConfig], logger: EngineInvocationLogger | None = None) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Enhance player engines with logging.


