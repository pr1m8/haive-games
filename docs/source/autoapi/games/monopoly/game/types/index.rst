games.monopoly.game.types
=========================

.. py:module:: games.monopoly.game.types


Classes
-------

.. autoapisummary::

   games.monopoly.game.types.ActionType
   games.monopoly.game.types.PropertyType
   games.monopoly.game.types.SpecialSquareType


Module Contents
---------------

.. py:class:: ActionType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of actions a player can take.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ActionType
      :collapse:

   .. py:attribute:: AUCTION
      :value: 'auction'



   .. py:attribute:: BUILD_HOUSE
      :value: 'build_house'



   .. py:attribute:: BUY
      :value: 'buy'



   .. py:attribute:: END_TURN
      :value: 'end_turn'



   .. py:attribute:: MORTGAGE
      :value: 'mortgage'



   .. py:attribute:: PAY_JAIL_FEE
      :value: 'pay_jail_fee'



   .. py:attribute:: ROLL
      :value: 'roll'



   .. py:attribute:: ROLL_FOR_JAIL
      :value: 'roll_for_jail'



   .. py:attribute:: SELL_HOUSE
      :value: 'sell_house'



   .. py:attribute:: TRADE
      :value: 'trade'



   .. py:attribute:: UNMORTGAGE
      :value: 'unmortgage'



   .. py:attribute:: USE_JAIL_CARD
      :value: 'use_jail_card'



.. py:class:: PropertyType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of properties on the board.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PropertyType
      :collapse:

   .. py:attribute:: PROPERTY
      :value: 'property'



   .. py:attribute:: RAILROAD
      :value: 'railroad'



   .. py:attribute:: SPECIAL
      :value: 'special'



   .. py:attribute:: UTILITY
      :value: 'utility'



.. py:class:: SpecialSquareType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of special squares on the board.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SpecialSquareType
      :collapse:

   .. py:attribute:: CHANCE
      :value: 'chance'



   .. py:attribute:: COMMUNITY_CHEST
      :value: 'community_chest'



   .. py:attribute:: FREE_PARKING
      :value: 'free_parking'



   .. py:attribute:: GO
      :value: 'go'



   .. py:attribute:: GO_TO_JAIL
      :value: 'go_to_jail'



   .. py:attribute:: INCOME_TAX
      :value: 'income_tax'



   .. py:attribute:: JAIL
      :value: 'jail'



   .. py:attribute:: LUXURY_TAX
      :value: 'luxury_tax'



