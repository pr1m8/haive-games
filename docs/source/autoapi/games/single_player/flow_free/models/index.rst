games.single_player.flow_free.models
====================================

.. py:module:: games.single_player.flow_free.models

.. autoapi-nested-parse::

   Models for Flow Free gameplay and analysis.

   This module defines the core data models for the Flow Free puzzle game, including move
   representation and strategic analysis.


   .. autolink-examples:: games.single_player.flow_free.models
      :collapse:


Classes
-------

.. autoapisummary::

   games.single_player.flow_free.models.FlowColor
   games.single_player.flow_free.models.FlowFreeAnalysis
   games.single_player.flow_free.models.FlowFreeMove
   games.single_player.flow_free.models.PipeDirection
   games.single_player.flow_free.models.Position


Module Contents
---------------

.. py:class:: FlowColor

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Color options for Flow Free pipes.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FlowColor
      :collapse:

   .. py:attribute:: BLUE
      :value: 'blue'



   .. py:attribute:: BROWN
      :value: 'brown'



   .. py:attribute:: CYAN
      :value: 'cyan'



   .. py:attribute:: GRAY
      :value: 'gray'



   .. py:attribute:: GREEN
      :value: 'green'



   .. py:attribute:: ORANGE
      :value: 'orange'



   .. py:attribute:: PINK
      :value: 'pink'



   .. py:attribute:: PURPLE
      :value: 'purple'



   .. py:attribute:: RED
      :value: 'red'



   .. py:attribute:: YELLOW
      :value: 'yellow'



.. py:class:: FlowFreeAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Strategic analysis of a Flow Free board position.

   .. attribute:: completed_flows

      List of flow IDs that have been completed.

   .. attribute:: incomplete_flows

      List of flow IDs that need completion.

   .. attribute:: critical_flows

      Flows that are most constrained and should be prioritized.

   .. attribute:: blocked_flows

      Flows that might be blocked or have limited space.

   .. attribute:: recommended_move

      The suggested next move based on analysis.

   .. attribute:: reasoning

      Detailed explanation of the analysis.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FlowFreeAnalysis
      :collapse:

   .. py:attribute:: blocked_flows
      :type:  list[str]
      :value: None



   .. py:attribute:: completed_flows
      :type:  list[str]
      :value: None



   .. py:property:: completion_percentage
      :type: float


      Calculate the percentage of flows completed.

      .. autolink-examples:: completion_percentage
         :collapse:


   .. py:attribute:: critical_flows
      :type:  list[str]
      :value: None



   .. py:attribute:: hint
      :type:  str | None
      :value: None



   .. py:attribute:: incomplete_flows
      :type:  list[str]
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: recommended_move
      :type:  FlowFreeMove | None
      :value: None



.. py:class:: FlowFreeMove(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a single move in Flow Free.

   .. attribute:: flow_id

      Identifier for the flow being extended.

   .. attribute:: position

      Position to place the next pipe segment.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FlowFreeMove
      :collapse:

   .. py:method:: __str__() -> str

      String representation of the move.


      .. autolink-examples:: __str__
         :collapse:


   .. py:attribute:: flow_id
      :type:  str
      :value: None



   .. py:attribute:: position
      :type:  Position
      :value: None



.. py:class:: PipeDirection

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Direction of a pipe segment.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PipeDirection
      :collapse:

   .. py:attribute:: DOWN
      :value: 'down'



   .. py:attribute:: LEFT
      :value: 'left'



   .. py:attribute:: NONE
      :value: 'none'



   .. py:attribute:: RIGHT
      :value: 'right'



   .. py:attribute:: UP
      :value: 'up'



.. py:class:: Position(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A position on the Flow Free board.

   .. attribute:: row

      Row index (0-based).

   .. attribute:: col

      Column index (0-based).

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Position
      :collapse:

   .. py:method:: __str__() -> str

      String representation of the position.


      .. autolink-examples:: __str__
         :collapse:


   .. py:attribute:: col
      :type:  int
      :value: None



   .. py:attribute:: row
      :type:  int
      :value: None



