
:py:mod:`games.debate_v2.judges`
================================

.. py:module:: games.debate_v2.judges

AI Judge System for Gamified Debates.

This module provides sophisticated AI judge agents that can evaluate debates using
different criteria and scoring methodologies.


.. autolink-examples:: games.debate_v2.judges
   :collapse:

Classes
-------

.. autoapisummary::

   games.debate_v2.judges.AIDebateJudge
   games.debate_v2.judges.DebateJudgingPanel
   games.debate_v2.judges.DebateJudgment
   games.debate_v2.judges.JudgeScore
   games.debate_v2.judges.JudgeType
   games.debate_v2.judges.JudgingCriteria


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AIDebateJudge:

   .. graphviz::
      :align: center

      digraph inheritance_AIDebateJudge {
        node [shape=record];
        "AIDebateJudge" [label="AIDebateJudge"];
      }

.. autoclass:: games.debate_v2.judges.AIDebateJudge
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DebateJudgingPanel:

   .. graphviz::
      :align: center

      digraph inheritance_DebateJudgingPanel {
        node [shape=record];
        "DebateJudgingPanel" [label="DebateJudgingPanel"];
      }

.. autoclass:: games.debate_v2.judges.DebateJudgingPanel
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DebateJudgment:

   .. graphviz::
      :align: center

      digraph inheritance_DebateJudgment {
        node [shape=record];
        "DebateJudgment" [label="DebateJudgment"];
        "pydantic.BaseModel" -> "DebateJudgment";
      }

.. autopydantic_model:: games.debate_v2.judges.DebateJudgment
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

   Inheritance diagram for JudgeScore:

   .. graphviz::
      :align: center

      digraph inheritance_JudgeScore {
        node [shape=record];
        "JudgeScore" [label="JudgeScore"];
        "pydantic.BaseModel" -> "JudgeScore";
      }

.. autopydantic_model:: games.debate_v2.judges.JudgeScore
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

   Inheritance diagram for JudgeType:

   .. graphviz::
      :align: center

      digraph inheritance_JudgeType {
        node [shape=record];
        "JudgeType" [label="JudgeType"];
        "str" -> "JudgeType";
        "enum.Enum" -> "JudgeType";
      }

.. autoclass:: games.debate_v2.judges.JudgeType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **JudgeType** is an Enum defined in ``games.debate_v2.judges``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for JudgingCriteria:

   .. graphviz::
      :align: center

      digraph inheritance_JudgingCriteria {
        node [shape=record];
        "JudgingCriteria" [label="JudgingCriteria"];
        "str" -> "JudgingCriteria";
        "enum.Enum" -> "JudgingCriteria";
      }

.. autoclass:: games.debate_v2.judges.JudgingCriteria
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **JudgingCriteria** is an Enum defined in ``games.debate_v2.judges``.



Functions
---------

.. autoapisummary::

   games.debate_v2.judges.create_academic_judges
   games.debate_v2.judges.create_public_judges
   games.debate_v2.judges.create_tournament_judges

.. py:function:: create_academic_judges(num_judges: int = 3) -> DebateJudgingPanel

   Create academic judges focused on evidence and logic.

   :param num_judges: Number of judges (default: 3)


   .. autolink-examples:: create_academic_judges
      :collapse:

.. py:function:: create_public_judges(num_judges: int = 3) -> DebateJudgingPanel

   Create public judges focused on accessibility and appeal.

   :param num_judges: Number of judges (default: 3)


   .. autolink-examples:: create_public_judges
      :collapse:

.. py:function:: create_tournament_judges(num_judges: int = 3) -> DebateJudgingPanel

   Create judges suitable for tournament play.

   :param num_judges: Number of judges (default: 3 to avoid ties)


   .. autolink-examples:: create_tournament_judges
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.debate_v2.judges
   :collapse:
   
.. autolink-skip:: next
