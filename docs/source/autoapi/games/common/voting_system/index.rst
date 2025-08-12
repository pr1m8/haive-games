
:py:mod:`games.common.voting_system`
====================================

.. py:module:: games.common.voting_system

Generalized AI Voting System for Game Winner Determination.

This module provides a reusable voting system that can evaluate game performance across
different game types using AI judges with specialized perspectives.


.. autolink-examples:: games.common.voting_system
   :collapse:

Classes
-------

.. autoapisummary::

   games.common.voting_system.AIGameJudge
   games.common.voting_system.ChessEvaluator
   games.common.voting_system.DebateEvaluator
   games.common.voting_system.GameEvaluator
   games.common.voting_system.GameVotingSystem
   games.common.voting_system.JudgePersonality
   games.common.voting_system.VoteChoice
   games.common.voting_system.VotingResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AIGameJudge:

   .. graphviz::
      :align: center

      digraph inheritance_AIGameJudge {
        node [shape=record];
        "AIGameJudge" [label="AIGameJudge"];
      }

.. autoclass:: games.common.voting_system.AIGameJudge
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChessEvaluator:

   .. graphviz::
      :align: center

      digraph inheritance_ChessEvaluator {
        node [shape=record];
        "ChessEvaluator" [label="ChessEvaluator"];
      }

.. autoclass:: games.common.voting_system.ChessEvaluator
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DebateEvaluator:

   .. graphviz::
      :align: center

      digraph inheritance_DebateEvaluator {
        node [shape=record];
        "DebateEvaluator" [label="DebateEvaluator"];
      }

.. autoclass:: games.common.voting_system.DebateEvaluator
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameEvaluator:

   .. graphviz::
      :align: center

      digraph inheritance_GameEvaluator {
        node [shape=record];
        "GameEvaluator" [label="GameEvaluator"];
        "Protocol" -> "GameEvaluator";
      }

.. autoclass:: games.common.voting_system.GameEvaluator
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameVotingSystem:

   .. graphviz::
      :align: center

      digraph inheritance_GameVotingSystem {
        node [shape=record];
        "GameVotingSystem" [label="GameVotingSystem"];
      }

.. autoclass:: games.common.voting_system.GameVotingSystem
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for JudgePersonality:

   .. graphviz::
      :align: center

      digraph inheritance_JudgePersonality {
        node [shape=record];
        "JudgePersonality" [label="JudgePersonality"];
        "str" -> "JudgePersonality";
        "enum.Enum" -> "JudgePersonality";
      }

.. autoclass:: games.common.voting_system.JudgePersonality
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **JudgePersonality** is an Enum defined in ``games.common.voting_system``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for VoteChoice:

   .. graphviz::
      :align: center

      digraph inheritance_VoteChoice {
        node [shape=record];
        "VoteChoice" [label="VoteChoice"];
        "pydantic.BaseModel" -> "VoteChoice";
      }

.. autopydantic_model:: games.common.voting_system.VoteChoice
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

   Inheritance diagram for VotingResult:

   .. graphviz::
      :align: center

      digraph inheritance_VotingResult {
        node [shape=record];
        "VotingResult" [label="VotingResult"];
        "pydantic.BaseModel" -> "VotingResult";
      }

.. autopydantic_model:: games.common.voting_system.VotingResult
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

   games.common.voting_system.create_voting_system

.. py:function:: create_voting_system(game_type: str = 'general', num_judges: int = 3) -> GameVotingSystem

   Create appropriate voting system for game type.

   :param game_type: Type of game ("general", "chess", "debate", "poker", "go")
   :param num_judges: Number of judges (default: 3 to avoid ties)


   .. autolink-examples:: create_voting_system
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.common.voting_system
   :collapse:
   
.. autolink-skip:: next
