games.monopoly.game.property
============================

.. py:module:: games.monopoly.game.property

Module documentation for games.monopoly.game.property


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.monopoly.game.property.Property

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Property(name: str, position: int, property_type: haive.games.monopoly.game.types.PropertyType, price: int = 0, color_group: str | None = None, rent_values: list[int] | None = None, mortgage_value: int | None = None, house_cost: int | None = None, special_type: haive.games.monopoly.game.types.SpecialSquareType | None = None)

            Represents a property on the board.


            .. py:method:: get_rent(dice_roll: int | None = None) -> int

               Calculate the rent for this property.

               :param dice_roll: The dice roll (needed for utilities)

               :returns: The rent amount



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






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.monopoly.game.property import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

