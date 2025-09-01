games.cards.standard.blackjack.config
=====================================

.. py:module:: games.cards.standard.blackjack.config


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/cards/standard/blackjack/config/BetAmount
   /autoapi/games/cards/standard/blackjack/config/BlackjackAgentConfig

.. autoapisummary::

   games.cards.standard.blackjack.config.BetAmount
   games.cards.standard.blackjack.config.BlackjackAgentConfig


Functions
---------

.. autoapisummary::

   games.cards.standard.blackjack.config.build_blackjack_aug_llms
   games.cards.standard.blackjack.config.generate_betting_prompt
   games.cards.standard.blackjack.config.generate_player_action_prompt


Module Contents
---------------

.. py:function:: build_blackjack_aug_llms() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Build AugLLM configurations for the Blackjack game.


.. py:function:: generate_betting_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate Betting Prompt.

   :returns: Add return description]
   :rtype: [TODO


.. py:function:: generate_player_action_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate Player Action Prompt.

   :returns: Add return description]
   :rtype: [TODO


