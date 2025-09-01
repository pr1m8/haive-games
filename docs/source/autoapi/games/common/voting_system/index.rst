games.common.voting_system
==========================

.. py:module:: games.common.voting_system

.. autoapi-nested-parse::

   Generalized AI Voting System for Game Winner Determination.

   This module provides a reusable voting system that can evaluate game performance across
   different game types using AI judges with specialized perspectives.



Attributes
----------

.. autoapisummary::

   games.common.voting_system.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/common/voting_system/AIGameJudge
   /autoapi/games/common/voting_system/ChessEvaluator
   /autoapi/games/common/voting_system/DebateEvaluator
   /autoapi/games/common/voting_system/GameEvaluator
   /autoapi/games/common/voting_system/GameVotingSystem
   /autoapi/games/common/voting_system/JudgePersonality
   /autoapi/games/common/voting_system/VoteChoice
   /autoapi/games/common/voting_system/VotingResult

.. autoapisummary::

   games.common.voting_system.AIGameJudge
   games.common.voting_system.ChessEvaluator
   games.common.voting_system.DebateEvaluator
   games.common.voting_system.GameEvaluator
   games.common.voting_system.GameVotingSystem
   games.common.voting_system.JudgePersonality
   games.common.voting_system.VoteChoice
   games.common.voting_system.VotingResult


Functions
---------

.. autoapisummary::

   games.common.voting_system.create_voting_system


Module Contents
---------------

.. py:function:: create_voting_system(game_type: str = 'general', num_judges: int = 3) -> GameVotingSystem

   Create appropriate voting system for game type.

   :param game_type: Type of game ("general", "chess", "debate", "poker", "go")
   :param num_judges: Number of judges (default: 3 to avoid ties)


.. py:data:: logger

