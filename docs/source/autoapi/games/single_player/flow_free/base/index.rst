games.single_player.flow_free.base
==================================

.. py:module:: games.single_player.flow_free.base

Module documentation for games.single_player.flow_free.base


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">10 classes</span> • <span class="module-stat">1 attributes</span>   </div>


      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.single_player.flow_free.base.ConnectionType

            
            

.. admonition:: Classes (10)
   :class: note

   .. autoapisummary::

      games.single_player.flow_free.base.EndpointType
      games.single_player.flow_free.base.FlowBoard
      games.single_player.flow_free.base.FlowEndpoint
      games.single_player.flow_free.base.FlowFreeGame
      games.single_player.flow_free.base.FlowFreeLevel
      games.single_player.flow_free.base.FlowFreeMove
      games.single_player.flow_free.base.FlowGridSpace
      games.single_player.flow_free.base.FlowPiece
      games.single_player.flow_free.base.FlowPipe
      games.single_player.flow_free.base.PipeDirection

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: EndpointType

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Type of endpoint.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: END
               :value: 'end'



            .. py:attribute:: START
               :value: 'start'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FlowBoard

            Bases: :py:obj:`game_framework_base.GridBoard`\ [\ :py:obj:`FlowGridSpace`\ [\ :py:obj:`FlowPiece`\ ]\ , :py:obj:`game_framework_base.GridPosition`\ , :py:obj:`FlowPiece`\ ]


            A Flow Free game board.


            .. py:method:: _check_flow_completion(flow_id: str) -> bool

               Check if a flow is complete (connects the two endpoints).



            .. py:method:: _update_pipe_connections(position: game_framework_base.GridPosition) -> None

               Update the connections between pipes and endpoints.



            .. py:method:: add_flow(color: str, start_pos: game_framework_base.GridPosition, end_pos: game_framework_base.GridPosition) -> str

               Add a new flow (pair of endpoints) to the board.



            .. py:method:: add_pipe_segment(flow_id: str, position: game_framework_base.GridPosition, direction: PipeDirection) -> bool

               Add a pipe segment to a flow.



            .. py:method:: get_adjacent_positions(position: game_framework_base.GridPosition) -> list[game_framework_base.GridPosition]

               Get all valid adjacent positions.



            .. py:method:: initialize_grid() -> None

               Initialize an empty grid.



            .. py:attribute:: flows
               :type:  dict[str, dict[str, any]]
               :value: None



            .. py:property:: is_solved
               :type: bool


               Check if the puzzle is solved.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FlowEndpoint

            Bases: :py:obj:`FlowPiece`


            An endpoint (colored dot) in Flow Free.


            .. py:method:: can_move_to(position: game_framework_base.GridPosition, board: game_framework_base.Board) -> bool

               Endpoints can't be moved in Flow Free.



            .. py:attribute:: connection_type
               :type:  Literal[ConnectionType]
               :value: 'endpoint'



            .. py:attribute:: endpoint_type
               :type:  EndpointType



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FlowFreeGame

            Bases: :py:obj:`game_framework_base.Game`\ [\ :py:obj:`game_framework_base.GridPosition`\ , :py:obj:`FlowPiece`\ ]


            Flow Free game controller.


            .. py:method:: _determine_pipe_direction(position: game_framework_base.GridPosition) -> PipeDirection

               Determine the direction of a pipe based on adjacent segments.



            .. py:method:: add_flow(color: str, start_pos: game_framework_base.GridPosition, end_pos: game_framework_base.GridPosition) -> str

               Add a new flow to the game.



            .. py:method:: is_valid_move(move: FlowFreeMove) -> bool

               Check if a move is valid.



            .. py:method:: make_move(move: FlowFreeMove) -> bool

               Make a move in the game.



            .. py:method:: reset() -> None

               Reset the game.



            .. py:method:: select_flow(flow_id: str) -> bool

               Select a flow to work with.



            .. py:method:: start_game() -> None

               Start the game.



            .. py:attribute:: board
               :type:  FlowBoard


            .. py:attribute:: current_flow_id
               :type:  str | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FlowFreeLevel(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A pre-defined Flow Free level.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: create_game() -> FlowFreeGame

               Create a game from this level.



            .. py:attribute:: cols
               :type:  int


            .. py:attribute:: flows
               :type:  list[tuple[str, tuple[int, int], tuple[int, int]]]


            .. py:attribute:: rows
               :type:  int



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FlowFreeMove(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A move in Flow Free.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: flow_id
               :type:  str


            .. py:attribute:: position
               :type:  game_framework_base.GridPosition



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FlowGridSpace

            Bases: :py:obj:`game_framework_base.GridSpace`\ [\ :py:obj:`FlowPiece`\ ]


            A space on a Flow Free board.


            .. py:property:: color
               :type: str | None


               Get the color of the piece in this space.


            .. py:property:: has_endpoint
               :type: bool


               Check if this space contains an endpoint.


            .. py:property:: has_pipe
               :type: bool


               Check if this space contains a pipe.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FlowPiece

            Bases: :py:obj:`game_framework_base.GamePiece`\ [\ :py:obj:`game_framework_base.GridPosition`\ ]


            Base class for Flow Free pieces (endpoints and pipes).


            .. py:method:: validate_color(v: str) -> str
               :classmethod:


               Validate color format.



            .. py:attribute:: color
               :type:  str


            .. py:attribute:: connection_type
               :type:  ConnectionType


            .. py:attribute:: flow_id
               :type:  str



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FlowPipe

            Bases: :py:obj:`FlowPiece`


            A pipe segment in Flow Free.


            .. py:method:: can_move_to(position: game_framework_base.GridPosition, board: FlowBoard) -> bool

               Check if this pipe segment can be placed at the specified position.



            .. py:attribute:: connected_directions
               :type:  set[PipeDirection]
               :value: None



            .. py:attribute:: connection_type
               :type:  Literal[ConnectionType]
               :value: 'pipe'



            .. py:attribute:: direction
               :type:  PipeDirection


            .. py:property:: is_corner
               :type: bool


               Check if this pipe forms a corner.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PipeDirection

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Direction of a pipe segment.

            Initialize self.  See help(type(self)) for accurate signature.


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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: ConnectionType




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.flow_free.base import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

