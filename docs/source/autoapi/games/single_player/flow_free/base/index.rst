games.single_player.flow_free.base
==================================

.. py:module:: games.single_player.flow_free.base


Attributes
----------

.. autoapisummary::

   games.single_player.flow_free.base.ConnectionType


Classes
-------

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


Module Contents
---------------

.. py:class:: EndpointType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Type of endpoint.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EndpointType
      :collapse:

   .. py:attribute:: END
      :value: 'end'



   .. py:attribute:: START
      :value: 'start'



.. py:class:: FlowBoard

   Bases: :py:obj:`game_framework_base.GridBoard`\ [\ :py:obj:`FlowGridSpace`\ [\ :py:obj:`FlowPiece`\ ]\ , :py:obj:`game_framework_base.GridPosition`\ , :py:obj:`FlowPiece`\ ]


   A Flow Free game board.


   .. autolink-examples:: FlowBoard
      :collapse:

   .. py:method:: _check_flow_completion(flow_id: str) -> bool

      Check if a flow is complete (connects the two endpoints).


      .. autolink-examples:: _check_flow_completion
         :collapse:


   .. py:method:: _update_pipe_connections(position: game_framework_base.GridPosition) -> None

      Update the connections between pipes and endpoints.


      .. autolink-examples:: _update_pipe_connections
         :collapse:


   .. py:method:: add_flow(color: str, start_pos: game_framework_base.GridPosition, end_pos: game_framework_base.GridPosition) -> str

      Add a new flow (pair of endpoints) to the board.


      .. autolink-examples:: add_flow
         :collapse:


   .. py:method:: add_pipe_segment(flow_id: str, position: game_framework_base.GridPosition, direction: PipeDirection) -> bool

      Add a pipe segment to a flow.


      .. autolink-examples:: add_pipe_segment
         :collapse:


   .. py:method:: get_adjacent_positions(position: game_framework_base.GridPosition) -> list[game_framework_base.GridPosition]

      Get all valid adjacent positions.


      .. autolink-examples:: get_adjacent_positions
         :collapse:


   .. py:method:: initialize_grid() -> None

      Initialize an empty grid.


      .. autolink-examples:: initialize_grid
         :collapse:


   .. py:attribute:: flows
      :type:  dict[str, dict[str, any]]
      :value: None



   .. py:property:: is_solved
      :type: bool


      Check if the puzzle is solved.

      .. autolink-examples:: is_solved
         :collapse:


.. py:class:: FlowEndpoint

   Bases: :py:obj:`FlowPiece`


   An endpoint (colored dot) in Flow Free.


   .. autolink-examples:: FlowEndpoint
      :collapse:

   .. py:method:: can_move_to(position: game_framework_base.GridPosition, board: game_framework_base.Board) -> bool

      Endpoints can't be moved in Flow Free.


      .. autolink-examples:: can_move_to
         :collapse:


   .. py:attribute:: connection_type
      :type:  Literal[ConnectionType]
      :value: 'endpoint'



   .. py:attribute:: endpoint_type
      :type:  EndpointType


.. py:class:: FlowFreeGame

   Bases: :py:obj:`game_framework_base.Game`\ [\ :py:obj:`game_framework_base.GridPosition`\ , :py:obj:`FlowPiece`\ ]


   Flow Free game controller.


   .. autolink-examples:: FlowFreeGame
      :collapse:

   .. py:method:: _determine_pipe_direction(position: game_framework_base.GridPosition) -> PipeDirection

      Determine the direction of a pipe based on adjacent segments.


      .. autolink-examples:: _determine_pipe_direction
         :collapse:


   .. py:method:: add_flow(color: str, start_pos: game_framework_base.GridPosition, end_pos: game_framework_base.GridPosition) -> str

      Add a new flow to the game.


      .. autolink-examples:: add_flow
         :collapse:


   .. py:method:: is_valid_move(move: FlowFreeMove) -> bool

      Check if a move is valid.


      .. autolink-examples:: is_valid_move
         :collapse:


   .. py:method:: make_move(move: FlowFreeMove) -> bool

      Make a move in the game.


      .. autolink-examples:: make_move
         :collapse:


   .. py:method:: reset() -> None

      Reset the game.


      .. autolink-examples:: reset
         :collapse:


   .. py:method:: select_flow(flow_id: str) -> bool

      Select a flow to work with.


      .. autolink-examples:: select_flow
         :collapse:


   .. py:method:: start_game() -> None

      Start the game.


      .. autolink-examples:: start_game
         :collapse:


   .. py:attribute:: board
      :type:  FlowBoard


   .. py:attribute:: current_flow_id
      :type:  str | None
      :value: None



.. py:class:: FlowFreeLevel(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A pre-defined Flow Free level.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FlowFreeLevel
      :collapse:

   .. py:method:: create_game() -> FlowFreeGame

      Create a game from this level.


      .. autolink-examples:: create_game
         :collapse:


   .. py:attribute:: cols
      :type:  int


   .. py:attribute:: flows
      :type:  list[tuple[str, tuple[int, int], tuple[int, int]]]


   .. py:attribute:: rows
      :type:  int


.. py:class:: FlowFreeMove(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A move in Flow Free.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FlowFreeMove
      :collapse:

   .. py:attribute:: flow_id
      :type:  str


   .. py:attribute:: position
      :type:  game_framework_base.GridPosition


.. py:class:: FlowGridSpace

   Bases: :py:obj:`game_framework_base.GridSpace`\ [\ :py:obj:`FlowPiece`\ ]


   A space on a Flow Free board.


   .. autolink-examples:: FlowGridSpace
      :collapse:

   .. py:property:: color
      :type: str | None


      Get the color of the piece in this space.

      .. autolink-examples:: color
         :collapse:


   .. py:property:: has_endpoint
      :type: bool


      Check if this space contains an endpoint.

      .. autolink-examples:: has_endpoint
         :collapse:


   .. py:property:: has_pipe
      :type: bool


      Check if this space contains a pipe.

      .. autolink-examples:: has_pipe
         :collapse:


.. py:class:: FlowPiece

   Bases: :py:obj:`game_framework_base.GamePiece`\ [\ :py:obj:`game_framework_base.GridPosition`\ ]


   Base class for Flow Free pieces (endpoints and pipes).


   .. autolink-examples:: FlowPiece
      :collapse:

   .. py:method:: validate_color(v: str) -> str
      :classmethod:


      Validate color format.


      .. autolink-examples:: validate_color
         :collapse:


   .. py:attribute:: color
      :type:  str


   .. py:attribute:: connection_type
      :type:  ConnectionType


   .. py:attribute:: flow_id
      :type:  str


.. py:class:: FlowPipe

   Bases: :py:obj:`FlowPiece`


   A pipe segment in Flow Free.


   .. autolink-examples:: FlowPipe
      :collapse:

   .. py:method:: can_move_to(position: game_framework_base.GridPosition, board: FlowBoard) -> bool

      Check if this pipe segment can be placed at the specified position.


      .. autolink-examples:: can_move_to
         :collapse:


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

      .. autolink-examples:: is_corner
         :collapse:


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



.. py:data:: ConnectionType

