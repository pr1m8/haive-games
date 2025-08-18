games.dominoes.models
=====================

.. py:module:: games.dominoes.models

Comprehensive data models for the Dominoes tile game.

This module defines the complete set of data structures for traditional Dominoes
gameplay, providing models for tile representation, game moves, strategic
analysis, and game state management. The implementation supports standard
double-six dominoes with traditional matching rules.

Dominoes is a classic tile-matching game involving:
- 28 tiles in a double-six set (0-0 through 6-6)
- Line-building with matching endpoints
- Strategic tile placement and blocking
- Point-based scoring systems

Key Models:
    DominoTile: Individual domino tile with two values
    DominoMove: Player's tile placement action
    DominoLinePosition: Position tracking on the domino line
    DominoAnalysis: Strategic evaluation for AI decision-making

.. rubric:: Examples

Working with tiles::

    from haive.games.dominoes.models import DominoTile

    # Create standard tiles
    double_six = DominoTile(left=6, right=6)
    mixed_tile = DominoTile(left=3, right=5)

    # Check tile properties
    assert double_six.is_double() == True
    assert mixed_tile.sum() == 8
    print(double_six)  # "[6|6]"

Making moves::

    from haive.games.dominoes.models import DominoMove

    move = DominoMove(
        tile=DominoTile(left=4, right=2),
        position="left",
        player="player1"
    )

Strategic analysis::

    analysis = DominoAnalysis(
        available_moves=5,
        blocking_potential=3,
        point_value=12,
        strategy="Control high-value tiles"
    )

The models provide comprehensive tile management and strategic gameplay
support for AI-driven dominoes implementation.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">4 classes</span>   </div>

.. autoapi-nested-parse::

   Comprehensive data models for the Dominoes tile game.

   This module defines the complete set of data structures for traditional Dominoes
   gameplay, providing models for tile representation, game moves, strategic
   analysis, and game state management. The implementation supports standard
   double-six dominoes with traditional matching rules.

   Dominoes is a classic tile-matching game involving:
   - 28 tiles in a double-six set (0-0 through 6-6)
   - Line-building with matching endpoints
   - Strategic tile placement and blocking
   - Point-based scoring systems

   Key Models:
       DominoTile: Individual domino tile with two values
       DominoMove: Player's tile placement action
       DominoLinePosition: Position tracking on the domino line
       DominoAnalysis: Strategic evaluation for AI decision-making

   .. rubric:: Examples

   Working with tiles::

       from haive.games.dominoes.models import DominoTile

       # Create standard tiles
       double_six = DominoTile(left=6, right=6)
       mixed_tile = DominoTile(left=3, right=5)

       # Check tile properties
       assert double_six.is_double() == True
       assert mixed_tile.sum() == 8
       print(double_six)  # "[6|6]"

   Making moves::

       from haive.games.dominoes.models import DominoMove

       move = DominoMove(
           tile=DominoTile(left=4, right=2),
           position="left",
           player="player1"
       )

   Strategic analysis::

       analysis = DominoAnalysis(
           available_moves=5,
           blocking_potential=3,
           point_value=12,
           strategy="Control high-value tiles"
       )

   The models provide comprehensive tile management and strategic gameplay
   support for AI-driven dominoes implementation.



      
            
            

.. admonition:: Classes (4)
   :class: note

   .. autoapisummary::

      games.dominoes.models.DominoMove
      games.dominoes.models.DominoTile
      games.dominoes.models.DominoesAnalysis
      games.dominoes.models.DominoesPlayerDecision

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DominoMove(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A move in dominoes.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of the move.



            .. py:attribute:: location
               :type:  Literal['left', 'right']
               :value: None



            .. py:attribute:: tile
               :type:  DominoTile
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DominoTile(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A domino tile with two values.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __eq__(other) -> bool

               Check if two tiles are equal (ignoring order).



            .. py:method:: __str__() -> str

               String representation of the tile.



            .. py:method:: is_double() -> bool

               Check if this is a double (same value on both sides).



            .. py:method:: reversed() -> DominoTile

               Get a new tile with left and right values swapped.



            .. py:method:: sum() -> int

               Get the sum of both values.



            .. py:attribute:: left
               :type:  int
               :value: None



            .. py:attribute:: right
               :type:  int
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DominoesAnalysis(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Analysis of a dominoes position.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: blocking_potential
               :type:  str
               :value: None



            .. py:attribute:: hand_strength
               :type:  int
               :value: None



            .. py:attribute:: missing_values
               :type:  list[int]
               :value: None



            .. py:attribute:: open_ends
               :type:  list[str]
               :value: None



            .. py:attribute:: pip_count_assessment
               :type:  str
               :value: None



            .. py:attribute:: reasoning
               :type:  str
               :value: None



            .. py:attribute:: suggested_strategy
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DominoesPlayerDecision(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A player's decision in dominoes.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of the decision.



            .. py:attribute:: move
               :type:  DominoMove | None
               :value: None



            .. py:attribute:: pass_turn
               :type:  bool
               :value: None



            .. py:attribute:: reasoning
               :type:  str
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.dominoes.models import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

