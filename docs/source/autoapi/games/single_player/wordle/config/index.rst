
:py:mod:`games.single_player.wordle.config`
===========================================

.. py:module:: games.single_player.wordle.config


Classes
-------

.. autoapisummary::

   games.single_player.wordle.config.WordConnectionsAgentConfig
   games.single_player.wordle.config.WordConnectionsGuess


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for WordConnectionsAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_WordConnectionsAgentConfig {
        node [shape=record];
        "WordConnectionsAgentConfig" [label="WordConnectionsAgentConfig"];
        "haive.games.framework.base.GameConfig" -> "WordConnectionsAgentConfig";
      }

.. autoclass:: games.single_player.wordle.config.WordConnectionsAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for WordConnectionsGuess:

   .. graphviz::
      :align: center

      digraph inheritance_WordConnectionsGuess {
        node [shape=record];
        "WordConnectionsGuess" [label="WordConnectionsGuess"];
        "pydantic.BaseModel" -> "WordConnectionsGuess";
      }

.. autopydantic_model:: games.single_player.wordle.config.WordConnectionsGuess
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



Functions
---------

.. autoapisummary::

   games.single_player.wordle.config.create_game_prompt

.. py:function:: create_game_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Create the main game playing prompt.


   .. autolink-examples:: create_game_prompt
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.single_player.wordle.config
   :collapse:
   
.. autolink-skip:: next
