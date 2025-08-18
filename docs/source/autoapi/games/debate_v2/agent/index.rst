games.debate_v2.agent
=====================

.. py:module:: games.debate_v2.agent

Gamified Debate Agent - Modern Implementation.

This module implements a gamified debate using the modern conversation agent
pattern from haive-agents, providing proper topic handling and state management
without the deprecated DynamicGraph system.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Gamified Debate Agent - Modern Implementation.

   This module implements a gamified debate using the modern conversation agent
   pattern from haive-agents, providing proper topic handling and state management
   without the deprecated DynamicGraph system.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.debate_v2.agent.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.debate_v2.agent.GameDebateAgent

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameDebateAgent

            Bases: :py:obj:`haive.agents.conversation.debate.agent.DebateConversation`


            Gamified debate agent with scoring and tournament features.

            This agent extends the conversation debate system with game-like features:
            - Scoring system for arguments and rebuttals
            - Tournament bracket support
            - Performance statistics tracking
            - Ranking and leaderboard capabilities



            .. py:method:: __repr__() -> str

               String representation of the game debate agent.



            .. py:method:: _calculate_argument_score(content: str, speaker: str, phase: str, state: haive.agents.conversation.debate.state.DebateState) -> dict[str, Any]

               Calculate and assign scores for arguments/rebuttals.



            .. py:method:: _create_initial_message() -> langchain_core.messages.BaseMessage

               Create the gamified debate introduction message.



            .. py:method:: _custom_initialization(state: haive.agents.conversation.debate.state.DebateState) -> dict[str, Any]

               Initialize game-specific state fields.



            .. py:method:: _has_evidence(content: str) -> bool

               Detect if content cites evidence or sources.



            .. py:method:: _is_repetitive(content: str, speaker: str, state: haive.agents.conversation.debate.state.DebateState) -> bool

               Detect if content is repetitive of previous arguments.



            .. py:method:: _update_game_phase(state: haive.agents.conversation.debate.state.DebateState) -> dict[str, Any]

               Update game phase based on debate progress.



            .. py:method:: conclude_conversation(state: haive.agents.conversation.debate.state.DebateState) -> langgraph.types.Command

               Create gamified conclusion with scores and winner declaration.



            .. py:method:: create_tournament_match(topic: str, player_a: tuple[str, str], player_b: tuple[str, str], match_id: str, bracket_position: str = 'tournament', **kwargs) -> GameDebateAgent
               :classmethod:


               Create a tournament debate match.



            .. py:method:: process_response(state: haive.agents.conversation.debate.state.DebateState) -> langgraph.types.Command

               Process response with game scoring logic.



            .. py:method:: setup_agent() -> None

               Setup the game debate agent with proper state schema.



            .. py:method:: validate_game_setup() -> GameDebateAgent

               Validate game configuration.



            .. py:attribute:: bonus_for_evidence
               :type:  int
               :value: None



            .. py:attribute:: bracket_position
               :type:  str | None
               :value: None



            .. py:attribute:: match_id
               :type:  str | None
               :value: None



            .. py:attribute:: mode
               :type:  Literal['game_debate']
               :value: None



            .. py:attribute:: penalty_for_repetition
               :type:  int
               :value: None



            .. py:attribute:: points_per_argument
               :type:  int
               :value: None



            .. py:attribute:: points_per_rebuttal
               :type:  int
               :value: None



            .. py:attribute:: save_replay
               :type:  bool
               :value: None



            .. py:attribute:: scoring_enabled
               :type:  bool
               :value: None



            .. py:attribute:: state_schema
               :type:  type[pydantic.BaseModel]
               :value: None



            .. py:attribute:: tournament_mode
               :type:  bool
               :value: None



            .. py:attribute:: track_performance
               :type:  bool
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.debate_v2.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

