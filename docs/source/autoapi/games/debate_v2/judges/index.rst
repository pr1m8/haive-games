games.debate_v2.judges
======================

.. py:module:: games.debate_v2.judges

.. autoapi-nested-parse::

   AI Judge System for Gamified Debates.

   This module provides sophisticated AI judge agents that can evaluate debates using
   different criteria and scoring methodologies.



Attributes
----------

.. autoapisummary::

   games.debate_v2.judges.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/debate_v2/judges/AIDebateJudge
   /autoapi/games/debate_v2/judges/DebateJudgingPanel
   /autoapi/games/debate_v2/judges/DebateJudgment
   /autoapi/games/debate_v2/judges/JudgeScore
   /autoapi/games/debate_v2/judges/JudgeType
   /autoapi/games/debate_v2/judges/JudgingCriteria

.. autoapisummary::

   games.debate_v2.judges.AIDebateJudge
   games.debate_v2.judges.DebateJudgingPanel
   games.debate_v2.judges.DebateJudgment
   games.debate_v2.judges.JudgeScore
   games.debate_v2.judges.JudgeType
   games.debate_v2.judges.JudgingCriteria


Functions
---------

.. autoapisummary::

   games.debate_v2.judges.create_academic_judges
   games.debate_v2.judges.create_public_judges
   games.debate_v2.judges.create_tournament_judges


Module Contents
---------------

.. py:function:: create_academic_judges(num_judges: int = 3) -> DebateJudgingPanel

   Create academic judges focused on evidence and logic.

   :param num_judges: Number of judges (default: 3)


.. py:function:: create_public_judges(num_judges: int = 3) -> DebateJudgingPanel

   Create public judges focused on accessibility and appeal.

   :param num_judges: Number of judges (default: 3)


.. py:function:: create_tournament_judges(num_judges: int = 3) -> DebateJudgingPanel

   Create judges suitable for tournament play.

   :param num_judges: Number of judges (default: 3 to avoid ties)


.. py:data:: logger

