games.framework.core.position
=============================

.. py:module:: games.framework.core.position

Module documentation for games.framework.core.position


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.framework.core.position.Position

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Position(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Base class for all position types in games.

            A Position represents a location in a game, with different games using different
            coordinate systems.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: frozen
                  :value: True




            .. py:method:: __eq__(other: object) -> bool

               Equality check must be implemented by subclasses.

               The base implementation just checks if the IDs match.




            .. py:method:: __hash__() -> int

               Hash implementation must be consistent with __eq__.

               The base implementation uses the ID.




            .. py:method:: serialize() -> dict[str, Any]

               Convert the position to a serializable dictionary.



            .. py:attribute:: id
               :type:  str
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.framework.core.position import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

