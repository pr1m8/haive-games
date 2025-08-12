
:py:mod:`games.cards.standard.blackjack.config`
===============================================

.. py:module:: games.cards.standard.blackjack.config


Classes
-------

.. autoapisummary::

   games.cards.standard.blackjack.config.BetAmount
   games.cards.standard.blackjack.config.BlackjackAgentConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BetAmount:

   .. graphviz::
      :align: center

      digraph inheritance_BetAmount {
        node [shape=record];
        "BetAmount" [label="BetAmount"];
        "pydantic.BaseModel" -> "BetAmount";
      }

.. autopydantic_model:: games.cards.standard.blackjack.config.BetAmount
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BlackjackAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_BlackjackAgentConfig {
        node [shape=record];
        "BlackjackAgentConfig" [label="BlackjackAgentConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "BlackjackAgentConfig";
      }

.. autoclass:: games.cards.standard.blackjack.config.BlackjackAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.cards.standard.blackjack.config.build_blackjack_aug_llms
   games.cards.standard.blackjack.config.generate_betting_prompt
   games.cards.standard.blackjack.config.generate_player_action_prompt

.. py:function:: build_blackjack_aug_llms() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Build AugLLM configurations for the Blackjack game.


   .. autolink-examples:: build_blackjack_aug_llms
      :collapse:

.. py:function:: generate_betting_prompt() -> langchain_core.prompts.ChatPromptTemplate

.. py:function:: generate_player_action_prompt() -> langchain_core.prompts.ChatPromptTemplate



.. rubric:: Related Links

.. autolink-examples:: games.cards.standard.blackjack.config
   :collapse:
   
.. autolink-skip:: next
