games.debate.state
==================

.. py:module:: games.debate.state


Classes
-------

.. autoapisummary::

   games.debate.state.DebateState


Module Contents
---------------

.. py:class:: DebateState

   Bases: :py:obj:`haive.games.framework.multi_player.state.MultiPlayerGameState`


   State model for debate-style interactions.


   .. autolink-examples:: DebateState
      :collapse:

   .. py:property:: current_speaker
      :type: str


      Get the current speaker's ID.

      .. autolink-examples:: current_speaker
         :collapse:


   .. py:attribute:: current_speaker_idx
      :type:  int
      :value: None



   .. py:attribute:: debate_phase
      :type:  str
      :value: None



   .. py:attribute:: interruptions_allowed
      :type:  bool
      :value: None



   .. py:attribute:: moderation_notes
      :type:  list[str]
      :value: None



   .. py:attribute:: moderator_id
      :type:  str | None
      :value: None



   .. py:attribute:: participants
      :type:  dict[str, haive.games.debate.models.Participant]
      :value: None



   .. py:attribute:: phase_statement_limit
      :type:  int | None
      :value: None



   .. py:attribute:: phase_time_limit
      :type:  int | None
      :value: None



   .. py:attribute:: scores
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: statements
      :type:  list[haive.games.debate.models.Statement]
      :value: None



   .. py:attribute:: time_remaining
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: topic
      :type:  haive.games.debate.models.Topic
      :value: None



   .. py:attribute:: turn_order
      :type:  list[str]
      :value: None



   .. py:attribute:: votes
      :type:  dict[str, list[haive.games.debate.models.Vote]]
      :value: None



