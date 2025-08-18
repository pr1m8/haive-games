games.cards.standard.poker.actions
==================================

.. py:module:: games.cards.standard.poker.actions

Module documentation for games.cards.standard.poker.actions


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">8 classes</span>   </div>


      
            
            

.. admonition:: Classes (8)
   :class: note

   .. autoapisummary::

      games.cards.standard.poker.actions.AllInAction
      games.cards.standard.poker.actions.BetAction
      games.cards.standard.poker.actions.CallAction
      games.cards.standard.poker.actions.CheckAction
      games.cards.standard.poker.actions.FoldAction
      games.cards.standard.poker.actions.PokerAction
      games.cards.standard.poker.actions.PokerActionType
      games.cards.standard.poker.actions.RaiseAction

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: AllInAction

            Bases: :py:obj:`PokerAction`


            Action to go all-in.


            .. py:method:: execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> haive.games.cards.card.components.actions.ActionResult

               Execute all-in action.



            .. py:attribute:: poker_action_type
               :type:  PokerActionType



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: BetAction

            Bases: :py:obj:`PokerAction`


            Action to place a new bet.


            .. py:method:: can_execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> bool

               Check if player can bet.



            .. py:method:: execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> haive.games.cards.card.components.actions.ActionResult

               Execute bet action.



            .. py:method:: validate_bet() -> BetAction

               Validate bet amount.



            .. py:attribute:: amount
               :type:  int


            .. py:attribute:: poker_action_type
               :type:  PokerActionType



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CallAction

            Bases: :py:obj:`PokerAction`


            Action to call a bet.


            .. py:method:: can_execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> bool

               Check if player can call.



            .. py:method:: execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> haive.games.cards.card.components.actions.ActionResult

               Execute call action.



            .. py:attribute:: poker_action_type
               :type:  PokerActionType



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CheckAction

            Bases: :py:obj:`PokerAction`


            Action to check (pass without betting).


            .. py:method:: can_execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> bool

               Check if player can check.



            .. py:method:: execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> haive.games.cards.card.components.actions.ActionResult

               Execute check action.



            .. py:attribute:: poker_action_type
               :type:  PokerActionType



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FoldAction

            Bases: :py:obj:`PokerAction`


            Action to fold (forfeit hand).


            .. py:method:: execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> haive.games.cards.card.components.actions.ActionResult

               Execute fold action.



            .. py:attribute:: poker_action_type
               :type:  PokerActionType



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PokerAction

            Bases: :py:obj:`haive.games.cards.card.components.actions.CardAction`\ [\ :py:obj:`haive.games.cards.card.components.standard.StandardCard`\ , :py:obj:`haive.games.cards.standard.poker.state.PokerGameState`\ ]


            Base class for poker actions.


            .. py:method:: can_execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> bool

               Check if this action can be executed.



            .. py:attribute:: action_type
               :type:  str
               :value: 'poker_action'



            .. py:attribute:: poker_action_type
               :type:  PokerActionType



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PokerActionType

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Types of poker actions.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: ALL_IN
               :value: 'all_in'



            .. py:attribute:: BET
               :value: 'bet'



            .. py:attribute:: CALL
               :value: 'call'



            .. py:attribute:: CHECK
               :value: 'check'



            .. py:attribute:: FOLD
               :value: 'fold'



            .. py:attribute:: RAISE
               :value: 'raise'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: RaiseAction

            Bases: :py:obj:`PokerAction`


            Action to raise an existing bet.


            .. py:method:: can_execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> bool

               Check if player can raise.



            .. py:method:: execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> haive.games.cards.card.components.actions.ActionResult

               Execute raise action.



            .. py:method:: validate_raise() -> RaiseAction

               Validate raise amount.



            .. py:attribute:: amount
               :type:  int


            .. py:attribute:: poker_action_type
               :type:  PokerActionType





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.cards.standard.poker.actions import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

