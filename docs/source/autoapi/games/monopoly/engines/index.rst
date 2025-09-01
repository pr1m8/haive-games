games.monopoly.engines
======================

.. py:module:: games.monopoly.engines

.. autoapi-nested-parse::

   Monopoly engines and prompts module.

   This module provides LLM configurations and prompts for monopoly player decisions,
   including:
       - Property purchase decisions
       - Jail action decisions
       - Building decisions
       - Trade negotiations



Attributes
----------

.. autoapisummary::

   games.monopoly.engines.building_decision_prompt
   games.monopoly.engines.jail_decision_prompt
   games.monopoly.engines.property_decision_prompt
   games.monopoly.engines.trade_decision_prompt


Functions
---------

.. autoapisummary::

   games.monopoly.engines.build_monopoly_player_aug_llms


Module Contents
---------------

.. py:function:: build_monopoly_player_aug_llms() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Build LLM configs for monopoly player decisions.


.. py:data:: building_decision_prompt

.. py:data:: jail_decision_prompt

.. py:data:: property_decision_prompt

.. py:data:: trade_decision_prompt

