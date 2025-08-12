
:py:mod:`games.debate.example`
==============================

.. py:module:: games.debate.example



Functions
---------

.. autoapisummary::

   games.debate.example.run_debate
   games.debate.example.run_policy_debate
   games.debate.example.run_trial_debate

.. py:function:: run_debate(topic: str, description: str = '', max_rounds: int = 2, num_debaters: int = 2, num_judges: int = 3)

   Run a multi-agent debate on the specified topic.

   :param topic: Topic of the debate
   :param description: Optional description of the debate context
   :param max_rounds: Number of argument rounds
   :param num_debaters: Number of debaters
   :param num_judges: Number of judges


   .. autolink-examples:: run_debate
      :collapse:

.. py:function:: run_policy_debate(policy: str, context: str = '')

   Run a policy debate using the debate framework.

   :param policy: The policy to debate
   :param context: Context about the policy


   .. autolink-examples:: run_policy_debate
      :collapse:

.. py:function:: run_trial_debate(case_title: str, case_facts: str, charges: str)

   Run a trial debate using the debate framework.

   :param case_title: Title of the case
   :param case_facts: Facts of the case
   :param charges: Charges against the defendant


   .. autolink-examples:: run_trial_debate
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.debate.example
   :collapse:
   
.. autolink-skip:: next
