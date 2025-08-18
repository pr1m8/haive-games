games.debate.state
==================

.. py:module:: games.debate.state

Module documentation for games.debate.state


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.debate.state.DebateState

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DebateState(/, **data: Any)

            Bases: :py:obj:`haive.games.framework.multi_player.state.MultiPlayerGameState`


            State model for debate-style interactions.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:property:: current_speaker
               :type: str


               Get the current speaker's ID.


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






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.debate.state import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

