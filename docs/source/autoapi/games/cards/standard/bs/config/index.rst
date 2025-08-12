
:py:mod:`games.cards.standard.bs.config`
========================================

.. py:module:: games.cards.standard.bs.config


Classes
-------

.. autoapisummary::

   games.cards.standard.bs.config.BullshitAgentConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BullshitAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_BullshitAgentConfig {
        node [shape=record];
        "BullshitAgentConfig" [label="BullshitAgentConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "BullshitAgentConfig";
      }

.. autoclass:: games.cards.standard.bs.config.BullshitAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.cards.standard.bs.config.build_bullshit_aug_llms
   games.cards.standard.bs.config.generate_challenge_prompt
   games.cards.standard.bs.config.generate_claim_prompt

.. py:function:: build_bullshit_aug_llms() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Build AugLLM configurations for the Bullshit game.


   .. autolink-examples:: build_bullshit_aug_llms
      :collapse:

.. py:function:: generate_challenge_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Create a prompt for players to decide whether to challenge another player.


   .. autolink-examples:: generate_challenge_prompt
      :collapse:

.. py:function:: generate_claim_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Create a prompt for players to make a claim during their turn.


   .. autolink-examples:: generate_claim_prompt
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.cards.standard.bs.config
   :collapse:
   
.. autolink-skip:: next
