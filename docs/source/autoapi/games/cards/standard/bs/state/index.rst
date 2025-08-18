games.cards.standard.bs.state
=============================

.. py:module:: games.cards.standard.bs.state

Module documentation for games.cards.standard.bs.state


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.cards.standard.bs.state.BullshitGameState

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: BullshitGameState(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents the overall state of a Bullshit game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: challenge_history
               :type:  list[dict[str, Any]]
               :value: None



            .. py:attribute:: current_claimed_value
               :type:  str | None
               :value: None



            .. py:attribute:: current_pile
               :type:  list[haive.games.cards.standard.bs.models.Card]
               :value: None



            .. py:attribute:: current_player_index
               :type:  int
               :value: None



            .. py:attribute:: game_status
               :type:  str
               :value: None



            .. py:attribute:: last_played_cards
               :type:  list[haive.games.cards.standard.bs.models.Card]
               :value: None



            .. py:attribute:: players
               :type:  list[haive.games.cards.standard.bs.models.PlayerState]
               :value: None



            .. py:attribute:: winner
               :type:  str | None
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.cards.standard.bs.state import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

