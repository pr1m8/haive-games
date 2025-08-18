games.debate_v2.judges
======================

.. py:module:: games.debate_v2.judges

AI Judge System for Gamified Debates.

This module provides sophisticated AI judge agents that can evaluate debates using
different criteria and scoring methodologies.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">6 classes</span> • <span class="module-stat">3 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   AI Judge System for Gamified Debates.

   This module provides sophisticated AI judge agents that can evaluate debates using
   different criteria and scoring methodologies.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.debate_v2.judges.logger

            
            

.. admonition:: Classes (6)
   :class: note

   .. autoapisummary::

      games.debate_v2.judges.AIDebateJudge
      games.debate_v2.judges.DebateJudgingPanel
      games.debate_v2.judges.DebateJudgment
      games.debate_v2.judges.JudgeScore
      games.debate_v2.judges.JudgeType
      games.debate_v2.judges.JudgingCriteria

            

.. admonition:: Functions (3)
   :class: info

   .. autoapisummary::

      games.debate_v2.judges.create_academic_judges
      games.debate_v2.judges.create_public_judges
      games.debate_v2.judges.create_tournament_judges

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: AIDebateJudge(name: str, judge_type: JudgeType = JudgeType.BALANCED, expertise_area: str | None = None, strictness_level: float = 0.5)

            AI judge that evaluates debate performances.


            .. py:method:: _create_fallback_score(player_name: str, response: str) -> JudgeScore

               Create a fallback score if parsing fails.



            .. py:method:: _create_judge_agent() -> haive.agents.simple.agent.SimpleAgent

               Create the AI agent for this judge.



            .. py:method:: judge_player_performance(player_name: str, player_position: str, debate_transcript: str, topic: str) -> JudgeScore
               :async:


               Judge a single player's performance in the debate.



            .. py:attribute:: agent


            .. py:attribute:: expertise_area
               :value: None



            .. py:attribute:: judge_type


            .. py:attribute:: name


            .. py:attribute:: strictness_level
               :value: 0.5




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DebateJudgingPanel(judges: list[AIDebateJudge])

            Panel of multiple AI judges for comprehensive debate evaluation.


            .. py:method:: _calculate_winner(all_scores: dict[str, list[JudgeScore]]) -> tuple[str, float, float]

               Calculate overall winner from all judge scores.



            .. py:method:: _create_judgment_summary(topic: str, players: list[str], all_scores: dict[str, list[JudgeScore]], winner: str, margin: float) -> str

               Create a comprehensive summary of the judging results.



            .. py:method:: create_expert_panel(expertise_area: str) -> DebateJudgingPanel
               :classmethod:


               Create a panel specialized in a particular area.



            .. py:method:: create_standard_panel(num_judges: int = 3) -> DebateJudgingPanel
               :classmethod:


               Create a standard panel with configurable number of randomized judges.

               :param num_judges: Number of judges to include (default: 3 to avoid ties)
                                  Must be odd number for proper tie-breaking.



            .. py:method:: judge_debate(topic: str, players: list[str], positions: dict[str, str], debate_transcript: str) -> DebateJudgment
               :async:


               Get comprehensive judgment from all judges.



            .. py:attribute:: judges



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DebateJudgment(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Complete judgment of a debate by multiple judges.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: consensus_level
               :type:  float
               :value: None



            .. py:attribute:: judge_scores
               :type:  dict[str, list[JudgeScore]]
               :value: None



            .. py:attribute:: judgment_summary
               :type:  str


            .. py:attribute:: margin_of_victory
               :type:  float
               :value: None



            .. py:attribute:: overall_winner
               :type:  str


            .. py:attribute:: players
               :type:  list[str]


            .. py:attribute:: topic
               :type:  str



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: JudgeScore(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Individual judge's scoring for a debate.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: confidence
               :type:  float
               :value: None



            .. py:attribute:: criteria_scores
               :type:  dict[JudgingCriteria, int]
               :value: None



            .. py:attribute:: judge_name
               :type:  str


            .. py:attribute:: judge_type
               :type:  JudgeType


            .. py:attribute:: reasoning
               :type:  str
               :value: None



            .. py:attribute:: total_score
               :type:  int
               :value: None



            .. py:attribute:: winner_vote
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: JudgeType

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Different types of AI judges with different personalities.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: ACADEMIC
               :value: 'academic'



            .. py:attribute:: AUDIENCE
               :value: 'audience'



            .. py:attribute:: BALANCED
               :value: 'balanced'



            .. py:attribute:: CRITICAL
               :value: 'critical'



            .. py:attribute:: RHETORICAL
               :value: 'rhetorical'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: JudgingCriteria

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Different criteria for judging debates.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: CLARITY
               :value: 'clarity'



            .. py:attribute:: CONSISTENCY
               :value: 'consistency'



            .. py:attribute:: EVIDENCE_QUALITY
               :value: 'evidence_quality'



            .. py:attribute:: LOGICAL_STRENGTH
               :value: 'logical_strength'



            .. py:attribute:: OVERALL_PERFORMANCE
               :value: 'overall_performance'



            .. py:attribute:: PERSUASIVENESS
               :value: 'persuasiveness'



            .. py:attribute:: REBUTTAL_QUALITY
               :value: 'rebuttal_quality'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_academic_judges(num_judges: int = 3) -> DebateJudgingPanel

            Create academic judges focused on evidence and logic.

            :param num_judges: Number of judges (default: 3)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_public_judges(num_judges: int = 3) -> DebateJudgingPanel

            Create public judges focused on accessibility and appeal.

            :param num_judges: Number of judges (default: 3)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_tournament_judges(num_judges: int = 3) -> DebateJudgingPanel

            Create judges suitable for tournament play.

            :param num_judges: Number of judges (default: 3 to avoid ties)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.debate_v2.judges import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

