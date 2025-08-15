games.debate_v2.agent
=====================

.. py:module:: games.debate_v2.agent

.. autoapi-nested-parse::

   Gamified Debate Agent - Modern Implementation.

   This module implements a gamified debate using the modern conversation agent
   pattern from haive-agents, providing proper topic handling and state management
   without the deprecated DynamicGraph system.


   .. autolink-examples:: games.debate_v2.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   games.debate_v2.agent.logger


Classes
-------

.. autoapisummary::

   games.debate_v2.agent.GameDebateAgent


Module Contents
---------------

.. py:class:: GameDebateAgent

   Bases: :py:obj:`haive.agents.conversation.debate.agent.DebateConversation`


   Gamified debate agent with scoring and tournament features.

   This agent extends the conversation debate system with game-like features:
   - Scoring system for arguments and rebuttals
   - Tournament bracket support
   - Performance statistics tracking
   - Ranking and leaderboard capabilities



   .. autolink-examples:: GameDebateAgent
      :collapse:

   .. py:method:: __repr__() -> str

      String representation of the game debate agent.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: _calculate_argument_score(content: str, speaker: str, phase: str, state: haive.agents.conversation.debate.state.DebateState) -> dict[str, Any]

      Calculate and assign scores for arguments/rebuttals.


      .. autolink-examples:: _calculate_argument_score
         :collapse:


   .. py:method:: _create_initial_message() -> langchain_core.messages.BaseMessage

      Create the gamified debate introduction message.


      .. autolink-examples:: _create_initial_message
         :collapse:


   .. py:method:: _custom_initialization(state: haive.agents.conversation.debate.state.DebateState) -> dict[str, Any]

      Initialize game-specific state fields.


      .. autolink-examples:: _custom_initialization
         :collapse:


   .. py:method:: _has_evidence(content: str) -> bool

      Detect if content cites evidence or sources.


      .. autolink-examples:: _has_evidence
         :collapse:


   .. py:method:: _is_repetitive(content: str, speaker: str, state: haive.agents.conversation.debate.state.DebateState) -> bool

      Detect if content is repetitive of previous arguments.


      .. autolink-examples:: _is_repetitive
         :collapse:


   .. py:method:: _update_game_phase(state: haive.agents.conversation.debate.state.DebateState) -> dict[str, Any]

      Update game phase based on debate progress.


      .. autolink-examples:: _update_game_phase
         :collapse:


   .. py:method:: conclude_conversation(state: haive.agents.conversation.debate.state.DebateState) -> langgraph.types.Command

      Create gamified conclusion with scores and winner declaration.


      .. autolink-examples:: conclude_conversation
         :collapse:


   .. py:method:: create_tournament_match(topic: str, player_a: tuple[str, str], player_b: tuple[str, str], match_id: str, bracket_position: str = 'tournament', **kwargs) -> GameDebateAgent
      :classmethod:


      Create a tournament debate match.


      .. autolink-examples:: create_tournament_match
         :collapse:


   .. py:method:: process_response(state: haive.agents.conversation.debate.state.DebateState) -> langgraph.types.Command

      Process response with game scoring logic.


      .. autolink-examples:: process_response
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup the game debate agent with proper state schema.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: validate_game_setup() -> GameDebateAgent

      Validate game configuration.


      .. autolink-examples:: validate_game_setup
         :collapse:


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



.. py:data:: logger

