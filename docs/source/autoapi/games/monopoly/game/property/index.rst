games.monopoly.game.property
============================

.. py:module:: games.monopoly.game.property


Classes
-------

.. autoapisummary::

   games.monopoly.game.property.Property


Module Contents
---------------

.. py:class:: Property(name: str, position: int, property_type: haive.games.monopoly.game.types.PropertyType, price: int = 0, color_group: str | None = None, rent_values: list[int] | None = None, mortgage_value: int | None = None, house_cost: int | None = None, special_type: haive.games.monopoly.game.types.SpecialSquareType | None = None)

   Represents a property on the board.


   .. autolink-examples:: Property
      :collapse:

   .. py:method:: get_rent(dice_roll: int | None = None) -> int

      Calculate the rent for this property.

      :param dice_roll: The dice roll (needed for utilities)

      :returns: The rent amount


      .. autolink-examples:: get_rent
         :collapse:


   .. py:attribute:: color_group
      :value: None



   .. py:attribute:: house_cost
      :value: 0



   .. py:attribute:: houses
      :type:  int
      :value: 0



   .. py:attribute:: is_mortgaged
      :type:  bool
      :value: False



   .. py:attribute:: mortgage_value
      :value: 0



   .. py:attribute:: name


   .. py:attribute:: owner
      :type:  int | None
      :value: None



   .. py:attribute:: position


   .. py:attribute:: price
      :value: 0



   .. py:attribute:: property_type


   .. py:attribute:: rent_values
      :value: [0]



   .. py:attribute:: special_type
      :value: None



