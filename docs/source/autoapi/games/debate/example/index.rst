games.debate.example
====================

.. py:module:: games.debate.example

Module documentation for games.debate.example


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">3 functions</span> • <span class="module-stat">1 attributes</span>   </div>


      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.debate.example.result

            
            
            

.. admonition:: Functions (3)
   :class: info

   .. autoapisummary::

      games.debate.example.run_debate
      games.debate.example.run_policy_debate
      games.debate.example.run_trial_debate

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_debate(topic: str, description: str = '', max_rounds: int = 2, num_debaters: int = 2, num_judges: int = 3)

            Run a multi-agent debate on the specified topic.

            :param topic: Topic of the debate
            :param description: Optional description of the debate context
            :param max_rounds: Number of argument rounds
            :param num_debaters: Number of debaters
            :param num_judges: Number of judges



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_policy_debate(policy: str, context: str = '')

            Run a policy debate using the debate framework.

            :param policy: The policy to debate
            :param context: Context about the policy



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_trial_debate(case_title: str, case_facts: str, charges: str)

            Run a trial debate using the debate framework.

            :param case_title: Title of the case
            :param case_facts: Facts of the case
            :param charges: Charges against the defendant



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: result




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.debate.example import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

