games.monopoly.game.player
==========================

.. py:module:: games.monopoly.game.player

Module documentation for games.monopoly.game.player


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.monopoly.game.player.Player

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Player(name: str, index: int, starting_cash: int = 1500)

            Represents a player in the game.


            .. py:method:: lose_property(property_position: int) -> None

               Remove a property from this player's properties.



            .. py:method:: net_worth(board_properties: list[haive.games.monopoly.game.property.Property]) -> int

               Calculate the player's net worth including property values.

               :param board_properties: List of all properties on the board

               :returns: The player's total net worth



            .. py:method:: own_property(property_position: int) -> None

               Add a property to this player's properties.



            .. py:method:: pay(amount: int) -> bool

               Pay an amount from the player's cash.

               :param amount: Amount to pay

               :returns: True if the payment was successful, False if player can't afford it



            .. py:method:: receive(amount: int) -> None

               Receive an amount of cash.

               :param amount: Amount to receive



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






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.monopoly.game.player import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

