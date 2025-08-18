games.common.voting_system
==========================

.. py:module:: games.common.voting_system

Generalized AI Voting System for Game Winner Determination.

This module provides a reusable voting system that can evaluate game performance across
different game types using AI judges with specialized perspectives.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">8 classes</span> • <span class="module-stat">1 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Generalized AI Voting System for Game Winner Determination.

   This module provides a reusable voting system that can evaluate game performance across
   different game types using AI judges with specialized perspectives.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.common.voting_system.logger

            
            

.. admonition:: Classes (8)
   :class: note

   .. autoapisummary::

      games.common.voting_system.AIGameJudge
      games.common.voting_system.ChessEvaluator
      games.common.voting_system.DebateEvaluator
      games.common.voting_system.GameEvaluator
      games.common.voting_system.GameVotingSystem
      games.common.voting_system.JudgePersonality
      games.common.voting_system.VoteChoice
      games.common.voting_system.VotingResult

            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.common.voting_system.create_voting_system

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: AIGameJudge(name: str, personality: JudgePersonality = JudgePersonality.BALANCED, expertise_area: str | None = None, focus_weight: float = 0.5)

            AI judge that can evaluate any game type.


            .. py:method:: _create_fallback_vote(choice: str, response: str) -> VoteChoice

               Create a fallback vote if parsing fails.



            .. py:method:: _create_judge_agent() -> haive.games.simple.agent.SimpleAgent

               Create the AI agent for this judge.



            .. py:method:: evaluate(topic: str, options: list[str], game_data: str, criteria: list[str]) -> VoteChoice
               :async:


               Evaluate the game and return a vote choice.



            .. py:attribute:: agent


            .. py:attribute:: expertise_area
               :value: None



            .. py:attribute:: focus_weight
               :value: 0.5



            .. py:attribute:: name


            .. py:attribute:: personality



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ChessEvaluator

            Evaluator for chess games.


            .. py:method:: format_game_data(game_data: Any) -> str


            .. py:method:: get_evaluation_context() -> str


            .. py:method:: get_evaluation_criteria() -> list[str]



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DebateEvaluator

            Evaluator for debate games.


            .. py:method:: format_game_data(game_data: Any) -> str


            .. py:method:: get_evaluation_context() -> str


            .. py:method:: get_evaluation_criteria() -> list[str]



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameEvaluator

            Bases: :py:obj:`Protocol`


            Protocol for game-specific evaluation logic.


            .. py:method:: format_game_data(game_data: Any) -> str

               Format game data for judge evaluation.



            .. py:method:: get_evaluation_context() -> str

               Get context-specific information for judges.



            .. py:method:: get_evaluation_criteria() -> list[str]

               Get the criteria this game should be judged on.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameVotingSystem(judges: list[AIGameJudge])

            Generalized voting system for any game type.


            .. py:method:: _calculate_winner(judge_votes: dict[str, VoteChoice], options: list[str]) -> tuple[str, float, float]

               Calculate winner, margin, and consensus from votes.



            .. py:method:: _create_summary(topic: str, options: list[str], judge_votes: dict[str, VoteChoice], winner: str, margin: float, consensus: float) -> str

               Create a summary of the voting results.



            .. py:method:: create_game_specific_judges(game_type: str, num_judges: int = 3) -> GameVotingSystem
               :classmethod:


               Create judges specialized for a specific game type.

               :param game_type: Type of game to create judges for
               :param num_judges: Number of judges to create (default: 3)



            .. py:method:: create_standard_judges(num_judges: int = 3) -> GameVotingSystem
               :classmethod:


               Create standard judge panel with configurable size and randomized.
               personalities.

               :param num_judges: Number of judges to create (default: 3 to avoid ties)
                                  Odd numbers recommended to prevent tie votes.



            .. py:method:: vote(topic: str, options: list[str], game_data: str, criteria: list[str], evaluator: GameEvaluator | None = None) -> VotingResult
               :async:


               Conduct voting with all judges.



            .. py:attribute:: judges



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: JudgePersonality

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Different AI judge personalities for game evaluation.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: ANALYTICAL
               :value: 'analytical'



            .. py:attribute:: AUDIENCE
               :value: 'audience'



            .. py:attribute:: BALANCED
               :value: 'balanced'



            .. py:attribute:: STRATEGIC
               :value: 'strategic'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: VoteChoice(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A judge's vote choice with reasoning.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: choice
               :type:  str
               :value: None



            .. py:attribute:: confidence
               :type:  float
               :value: None



            .. py:attribute:: criteria_scores
               :type:  dict[str, int]
               :value: None



            .. py:attribute:: reasoning
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: VotingResult(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Complete voting results from multiple judges.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: consensus
               :type:  float
               :value: None



            .. py:attribute:: judge_votes
               :type:  dict[str, VoteChoice]
               :value: None



            .. py:attribute:: margin
               :type:  float
               :value: None



            .. py:attribute:: options
               :type:  list[str]
               :value: None



            .. py:attribute:: summary
               :type:  str
               :value: None



            .. py:attribute:: topic
               :type:  str
               :value: None



            .. py:attribute:: winner
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_voting_system(game_type: str = 'general', num_judges: int = 3) -> GameVotingSystem

            Create appropriate voting system for game type.

            :param game_type: Type of game ("general", "chess", "debate", "poker", "go")
            :param num_judges: Number of judges (default: 3 to avoid ties)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.common.voting_system import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

