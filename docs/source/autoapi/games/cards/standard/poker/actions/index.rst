games.cards.standard.poker.actions
==================================

.. py:module:: games.cards.standard.poker.actions


Classes
-------

.. autoapisummary::

   games.cards.standard.poker.actions.AllInAction
   games.cards.standard.poker.actions.BetAction
   games.cards.standard.poker.actions.CallAction
   games.cards.standard.poker.actions.CheckAction
   games.cards.standard.poker.actions.FoldAction
   games.cards.standard.poker.actions.PokerAction
   games.cards.standard.poker.actions.PokerActionType
   games.cards.standard.poker.actions.RaiseAction


Module Contents
---------------

.. py:class:: AllInAction

   Bases: :py:obj:`PokerAction`


   Action to go all-in.


   .. autolink-examples:: AllInAction
      :collapse:

   .. py:method:: execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> haive.games.cards.card.components.actions.ActionResult

      Execute all-in action.


      .. autolink-examples:: execute
         :collapse:


   .. py:attribute:: poker_action_type
      :type:  PokerActionType


.. py:class:: BetAction

   Bases: :py:obj:`PokerAction`


   Action to place a new bet.


   .. autolink-examples:: BetAction
      :collapse:

   .. py:method:: can_execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> bool

      Check if player can bet.


      .. autolink-examples:: can_execute
         :collapse:


   .. py:method:: execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> haive.games.cards.card.components.actions.ActionResult

      Execute bet action.


      .. autolink-examples:: execute
         :collapse:


   .. py:method:: validate_bet() -> BetAction

      Validate bet amount.


      .. autolink-examples:: validate_bet
         :collapse:


   .. py:attribute:: amount
      :type:  int


   .. py:attribute:: poker_action_type
      :type:  PokerActionType


.. py:class:: CallAction

   Bases: :py:obj:`PokerAction`


   Action to call a bet.


   .. autolink-examples:: CallAction
      :collapse:

   .. py:method:: can_execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> bool

      Check if player can call.


      .. autolink-examples:: can_execute
         :collapse:


   .. py:method:: execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> haive.games.cards.card.components.actions.ActionResult

      Execute call action.


      .. autolink-examples:: execute
         :collapse:


   .. py:attribute:: poker_action_type
      :type:  PokerActionType


.. py:class:: CheckAction

   Bases: :py:obj:`PokerAction`


   Action to check (pass without betting).


   .. autolink-examples:: CheckAction
      :collapse:

   .. py:method:: can_execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> bool

      Check if player can check.


      .. autolink-examples:: can_execute
         :collapse:


   .. py:method:: execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> haive.games.cards.card.components.actions.ActionResult

      Execute check action.


      .. autolink-examples:: execute
         :collapse:


   .. py:attribute:: poker_action_type
      :type:  PokerActionType


.. py:class:: FoldAction

   Bases: :py:obj:`PokerAction`


   Action to fold (forfeit hand).


   .. autolink-examples:: FoldAction
      :collapse:

   .. py:method:: execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> haive.games.cards.card.components.actions.ActionResult

      Execute fold action.


      .. autolink-examples:: execute
         :collapse:


   .. py:attribute:: poker_action_type
      :type:  PokerActionType


.. py:class:: PokerAction

   Bases: :py:obj:`haive.games.cards.card.components.actions.CardAction`\ [\ :py:obj:`haive.games.cards.card.components.standard.StandardCard`\ , :py:obj:`haive.games.cards.standard.poker.state.PokerGameState`\ ]


   Base class for poker actions.


   .. autolink-examples:: PokerAction
      :collapse:

   .. py:method:: can_execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> bool

      Check if this action can be executed.


      .. autolink-examples:: can_execute
         :collapse:


   .. py:attribute:: action_type
      :type:  str
      :value: 'poker_action'



   .. py:attribute:: poker_action_type
      :type:  PokerActionType


.. py:class:: PokerActionType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of poker actions.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PokerActionType
      :collapse:

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



.. py:class:: RaiseAction

   Bases: :py:obj:`PokerAction`


   Action to raise an existing bet.


   .. autolink-examples:: RaiseAction
      :collapse:

   .. py:method:: can_execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> bool

      Check if player can raise.


      .. autolink-examples:: can_execute
         :collapse:


   .. py:method:: execute(state: haive.games.cards.standard.poker.state.PokerGameState) -> haive.games.cards.card.components.actions.ActionResult

      Execute raise action.


      .. autolink-examples:: execute
         :collapse:


   .. py:method:: validate_raise() -> RaiseAction

      Validate raise amount.


      .. autolink-examples:: validate_raise
         :collapse:


   .. py:attribute:: amount
      :type:  int


   .. py:attribute:: poker_action_type
      :type:  PokerActionType


