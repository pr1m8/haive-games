games.cards.standard.bs.config
==============================

.. py:module:: games.cards.standard.bs.config


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/cards/standard/bs/config/BullshitAgentConfig

.. autoapisummary::

   games.cards.standard.bs.config.BullshitAgentConfig


Functions
---------

.. autoapisummary::

   games.cards.standard.bs.config.build_bullshit_aug_llms
   games.cards.standard.bs.config.generate_challenge_prompt
   games.cards.standard.bs.config.generate_claim_prompt


Module Contents
---------------

.. py:function:: build_bullshit_aug_llms() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Build AugLLM configurations for the Bullshit game.


.. py:function:: generate_challenge_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Create a prompt for players to decide whether to challenge another player.


.. py:function:: generate_claim_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Create a prompt for players to make a claim during their turn.


