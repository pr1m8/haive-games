games.hold_em.engine_logging
============================

.. py:module:: games.hold_em.engine_logging

.. autoapi-nested-parse::

   Enhanced engine invocation with Rich logging and debugging.


   .. autolink-examples:: games.hold_em.engine_logging
      :collapse:


Classes
-------

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

.. py:class:: EngineInvocationLogger(console: rich.console.Console | None = None, debug_mode: bool = True)

   Rich logging for engine invocations with debugging capabilities.


   .. autolink-examples:: EngineInvocationLogger
      :collapse:

   .. py:method:: _format_data_preview(data: Any) -> rich.text.Text

      Format data for Rich display.


      .. autolink-examples:: _format_data_preview
         :collapse:


   .. py:method:: _preview_data(data: Any) -> str

      Create a preview string for data.


      .. autolink-examples:: _preview_data
         :collapse:


   .. py:method:: create_enhanced_invoke(engine: haive.core.engine.aug_llm.AugLLMConfig) -> collections.abc.Callable

      Create an enhanced invoke method with logging.


      .. autolink-examples:: create_enhanced_invoke
         :collapse:


   .. py:method:: enhance_engine(engine: haive.core.engine.aug_llm.AugLLMConfig) -> haive.core.engine.aug_llm.AugLLMConfig

      Enhance an engine with logging capabilities.


      .. autolink-examples:: enhance_engine
         :collapse:


   .. py:method:: enhance_engines_dict(engines: dict[str, haive.core.engine.aug_llm.AugLLMConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

      Enhance all engines in a dictionary.


      .. autolink-examples:: enhance_engines_dict
         :collapse:


   .. py:method:: invocation_context(engine_name: str, input_data: Any)

      Context manager for engine invocations.


      .. autolink-examples:: invocation_context
         :collapse:


   .. py:method:: log_invocation_end(invocation_info: dict[str, Any], result: Any, error: Exception | None = None)

      Log the end of an engine invocation.


      .. autolink-examples:: log_invocation_end
         :collapse:


   .. py:method:: log_invocation_start(engine_name: str, input_data: Any) -> dict[str, Any]

      Log the start of an engine invocation.


      .. autolink-examples:: log_invocation_start
         :collapse:


   .. py:method:: print_invocation_tree()

      Print a tree view of all invocations.


      .. autolink-examples:: print_invocation_tree
         :collapse:


   .. py:method:: print_timing_summary()

      Print a summary of engine timing statistics.


      .. autolink-examples:: print_timing_summary
         :collapse:


   .. py:attribute:: console


   .. py:attribute:: current_depth
      :value: 0



   .. py:attribute:: debug_mode
      :value: True



   .. py:attribute:: invocation_history
      :type:  list[dict[str, Any]]
      :value: []



   .. py:attribute:: timing_stats
      :type:  dict[str, list[float]]


.. py:class:: LoggedAugLLMConfig(*args, logger: EngineInvocationLogger | None = None, **kwargs)

   Bases: :py:obj:`haive.core.engine.aug_llm.AugLLMConfig`


   AugLLMConfig with enhanced logging capabilities.


   .. autolink-examples:: LoggedAugLLMConfig
      :collapse:

   .. py:method:: create_runnable(runnable_config=None)

      Create runnable with logging enhancement.


      .. autolink-examples:: create_runnable
         :collapse:


   .. py:attribute:: logger


.. py:function:: enhance_game_engines(engines: dict[str, haive.core.engine.aug_llm.AugLLMConfig], logger: EngineInvocationLogger | None = None) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Enhance game engines with logging.


   .. autolink-examples:: enhance_game_engines
      :collapse:

.. py:function:: enhance_player_engines(engines: dict[str, haive.core.engine.aug_llm.AugLLMConfig], logger: EngineInvocationLogger | None = None) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Enhance player engines with logging.


   .. autolink-examples:: enhance_player_engines
      :collapse:

