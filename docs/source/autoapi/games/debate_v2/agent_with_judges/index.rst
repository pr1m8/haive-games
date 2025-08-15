games.debate_v2.agent_with_judges
=================================

.. py:module:: games.debate_v2.agent_with_judges

.. autoapi-nested-parse::

   Enhanced Gamified Debate Agent with AI Judge Integration.

   This module extends the basic gamified debate with AI judge panels for sophisticated
   winner determination and performance evaluation.


   .. autolink-examples:: games.debate_v2.agent_with_judges
      :collapse:


Attributes
----------

.. autoapisummary::

   games.debate_v2.agent_with_judges.logger


Classes
-------

.. autoapisummary::

   games.debate_v2.agent_with_judges.JudgedGameDebateAgent


Module Contents
---------------

.. py:class:: JudgedGameDebateAgent

   Bases: :py:obj:`haive.games.debate_v2.agent.GameDebateAgent`


   Gamified debate agent with AI judge panel integration.

   This agent extends the basic GameDebateAgent with sophisticated AI judge evaluation
   for more nuanced winner determination and detailed performance feedback from
   multiple judge perspectives.



   .. autolink-examples:: JudgedGameDebateAgent
      :collapse:

   .. py:method:: __repr__() -> str

      String representation of the judged debate agent.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: _combine_scoring_methods(state: haive.agents.conversation.debate.state.DebateState, judgment: haive.games.debate_v2.judges.DebateJudgment) -> dict[str, float]

      Combine automatic scoring with AI judge scores.


      .. autolink-examples:: _combine_scoring_methods
         :collapse:


   .. py:method:: _create_debate_transcript(state: haive.agents.conversation.debate.state.DebateState) -> str

      Create a formatted transcript for judge evaluation.


      .. autolink-examples:: _create_debate_transcript
         :collapse:


   .. py:method:: _create_enhanced_conclusion(state: haive.agents.conversation.debate.state.DebateState, judgment: haive.games.debate_v2.judges.DebateJudgment) -> langchain_core.messages.SystemMessage

      Create enhanced conclusion message with judge evaluation.


      .. autolink-examples:: _create_enhanced_conclusion
         :collapse:


   .. py:method:: _create_judge_panel() -> haive.games.debate_v2.judges.DebateJudgingPanel

      Create appropriate judge panel based on configuration.


      .. autolink-examples:: _create_judge_panel
         :collapse:


   .. py:method:: _extract_judge_scores(judgment: haive.games.debate_v2.judges.DebateJudgment) -> dict[str, float]

      Extract average judge scores for each player.


      .. autolink-examples:: _extract_judge_scores
         :collapse:


   .. py:method:: _get_ai_judge_evaluation(state: haive.agents.conversation.debate.state.DebateState) -> haive.games.debate_v2.judges.DebateJudgment
      :async:


      Get evaluation from AI judge panel.


      .. autolink-examples:: _get_ai_judge_evaluation
         :collapse:


   .. py:method:: conclude_conversation(state: haive.agents.conversation.debate.state.DebateState) -> langgraph.types.Command
      :async:


      Enhanced conclusion with AI judge evaluation.


      .. autolink-examples:: conclude_conversation
         :collapse:


   .. py:method:: create_judged_tournament_match(topic: str, player_a: tuple[str, str], player_b: tuple[str, str], match_id: str, judge_panel_type: Literal['tournament', 'academic', 'public'] = 'tournament', num_judges: int = 3, bracket_position: str = 'tournament', **kwargs) -> JudgedGameDebateAgent
      :classmethod:


      Create a tournament debate match with AI judge evaluation.


      .. autolink-examples:: create_judged_tournament_match
         :collapse:


   .. py:method:: get_judge_panel_info() -> dict[str, Any]

      Get information about the current judge panel.


      .. autolink-examples:: get_judge_panel_info
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup the judged debate agent with judge panel.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: auto_scoring_weight
      :type:  float
      :value: None



   .. py:attribute:: combine_auto_and_judge_scoring
      :type:  bool
      :value: None



   .. py:attribute:: custom_judges
      :type:  haive.games.debate_v2.judges.DebateJudgingPanel | None
      :value: None



   .. py:attribute:: final_judgment
      :type:  haive.games.debate_v2.judges.DebateJudgment | None
      :value: None



   .. py:attribute:: judge_panel_type
      :type:  Literal['tournament', 'academic', 'public', 'custom']
      :value: None



   .. py:attribute:: judge_scoring_weight
      :type:  float
      :value: None



   .. py:attribute:: num_judges
      :type:  int
      :value: None



   .. py:attribute:: use_ai_judges
      :type:  bool
      :value: None



.. py:data:: logger

