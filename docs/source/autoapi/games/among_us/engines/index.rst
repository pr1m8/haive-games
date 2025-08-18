games.among_us.engines
======================

.. py:module:: games.among_us.engines

Module documentation for games.among_us.engines


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.among_us.engines.AmongUsEngines

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: AmongUsEngines

            Engines for the Among Us game.

            This class creates and manages the LLM engines used for different player roles and
            game phases.



            .. py:method:: create_engines(llm_config: dict[str, Any] | None = None) -> dict[str, dict[str, haive.core.engine.aug_llm.AugLLMConfig]]
               :classmethod:


               Create the engines for the Among Us game.

               :param llm_config: Optional configuration for the language model

               :returns: A dictionary of engines organized by role and game phase



            .. py:method:: create_runnable_engines(llm_config: dict[str, Any] | None = None) -> dict[str, dict[str, Any]]
               :classmethod:


               Create runnable engines for the Among Us game.

               :param llm_config: Optional configuration for the language model

               :returns: A dictionary of runnable engines organized by role and game phase






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.among_us.engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

