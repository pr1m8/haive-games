games.hold_em.engine_logging
============================

.. py:module:: games.hold_em.engine_logging

Enhanced engine invocation with Rich logging and debugging.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 classes</span> • <span class="module-stat">2 functions</span>   </div>

.. autoapi-nested-parse::

   Enhanced engine invocation with Rich logging and debugging.



      
            
            

.. admonition:: Classes (2)
   :class: note

   .. autoapisummary::

      games.hold_em.engine_logging.EngineInvocationLogger
      games.hold_em.engine_logging.LoggedAugLLMConfig

            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.hold_em.engine_logging.enhance_game_engines
      games.hold_em.engine_logging.enhance_player_engines

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: EngineInvocationLogger(console: rich.console.Console | None = None, debug_mode: bool = True)

            Rich logging for engine invocations with debugging capabilities.


            .. py:method:: _format_data_preview(data: Any) -> rich.text.Text

               Format data for Rich display.



            .. py:method:: _preview_data(data: Any) -> str

               Create a preview string for data.



            .. py:method:: create_enhanced_invoke(engine: haive.core.engine.aug_llm.AugLLMConfig) -> collections.abc.Callable

               Create an enhanced invoke method with logging.



            .. py:method:: enhance_engine(engine: haive.core.engine.aug_llm.AugLLMConfig) -> haive.core.engine.aug_llm.AugLLMConfig

               Enhance an engine with logging capabilities.



            .. py:method:: enhance_engines_dict(engines: dict[str, haive.core.engine.aug_llm.AugLLMConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

               Enhance all engines in a dictionary.



            .. py:method:: invocation_context(engine_name: str, input_data: Any)

               Context manager for engine invocations.



            .. py:method:: log_invocation_end(invocation_info: dict[str, Any], result: Any, error: Exception | None = None)

               Log the end of an engine invocation.



            .. py:method:: log_invocation_start(engine_name: str, input_data: Any) -> dict[str, Any]

               Log the start of an engine invocation.



            .. py:method:: print_invocation_tree()

               Print a tree view of all invocations.



            .. py:method:: print_timing_summary()

               Print a summary of engine timing statistics.



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



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: LoggedAugLLMConfig(*args, logger: EngineInvocationLogger | None = None, **kwargs)

            Bases: :py:obj:`haive.core.engine.aug_llm.AugLLMConfig`


            AugLLMConfig with enhanced logging capabilities.


            .. py:method:: create_runnable(runnable_config=None)

               Create runnable with logging enhancement.



            .. py:attribute:: logger



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: enhance_game_engines(engines: dict[str, haive.core.engine.aug_llm.AugLLMConfig], logger: EngineInvocationLogger | None = None) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Enhance game engines with logging.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: enhance_player_engines(engines: dict[str, haive.core.engine.aug_llm.AugLLMConfig], logger: EngineInvocationLogger | None = None) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Enhance player engines with logging.





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.hold_em.engine_logging import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

