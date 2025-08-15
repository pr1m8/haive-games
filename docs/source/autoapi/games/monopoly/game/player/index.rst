games.monopoly.game.player
==========================

.. py:module:: games.monopoly.game.player


Classes
-------

.. autoapisummary::

   games.monopoly.game.player.Player


Module Contents
---------------

.. py:class:: Player(name: str, index: int, starting_cash: int = 1500)

   Represents a player in the game.


   .. autolink-examples:: Player
      :collapse:

   .. py:method:: lose_property(property_position: int) -> None

      Remove a property from this player's properties.


      .. autolink-examples:: lose_property
         :collapse:


   .. py:method:: net_worth(board_properties: list[haive.games.monopoly.game.property.Property]) -> int

      Calculate the player's net worth including property values.

      :param board_properties: List of all properties on the board

      :returns: The player's total net worth


      .. autolink-examples:: net_worth
         :collapse:


   .. py:method:: own_property(property_position: int) -> None

      Add a property to this player's properties.


      .. autolink-examples:: own_property
         :collapse:


   .. py:method:: pay(amount: int) -> bool

      Pay an amount from the player's cash.

      :param amount: Amount to pay

      :returns: True if the payment was successful, False if player can't afford it


      .. autolink-examples:: pay
         :collapse:


   .. py:method:: receive(amount: int) -> None

      Receive an amount of cash.

      :param amount: Amount to receive


      .. autolink-examples:: receive
         :collapse:


   .. py:attribute:: bankruptcy_status
      :value: False



   .. py:attribute:: cash
      :value: 1500



   .. py:attribute:: in_jail
      :value: False



   .. py:attribute:: index


   .. py:attribute:: jail_cards
      :value: 0



   .. py:attribute:: jail_turns
      :value: 0



   .. py:attribute:: name


   .. py:attribute:: position
      :value: 0



   .. py:attribute:: properties
      :type:  list[int]
      :value: []



