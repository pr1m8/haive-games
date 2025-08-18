games.single_player.flow_free.state
===================================

.. py:module:: games.single_player.flow_free.state

State model for Flow Free game.

This module defines the game state for Flow Free, tracking the board, flows, and game
progress.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">4 classes</span>   </div>

.. autoapi-nested-parse::

   State model for Flow Free game.

   This module defines the game state for Flow Free, tracking the board, flows, and game
   progress.



      
            
            

.. admonition:: Classes (4)
   :class: note

   .. autoapisummary::

      games.single_player.flow_free.state.Cell
      games.single_player.flow_free.state.Flow
      games.single_player.flow_free.state.FlowEndpoint
      games.single_player.flow_free.state.FlowFreeState

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Cell(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A cell on the Flow Free board.

            .. attribute:: position

               Position of the cell.

            .. attribute:: flow_id

               ID of the flow occupying this cell, if any.

            .. attribute:: is_endpoint

               Whether this cell contains an endpoint.

            .. attribute:: pipe_direction

               Direction of the pipe in this cell, if any.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: flow_id
               :type:  str | None
               :value: None



            .. py:attribute:: is_endpoint
               :type:  bool
               :value: False



            .. py:attribute:: pipe_direction
               :type:  haive.games.single_player.flow_free.models.PipeDirection | None
               :value: None



            .. py:attribute:: position
               :type:  haive.games.single_player.flow_free.models.Position



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Flow(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A flow in Flow Free, consisting of two endpoints and a path of pipes.

            .. attribute:: id

               Unique identifier for the flow.

            .. attribute:: color

               Color of the flow.

            .. attribute:: start

               Starting endpoint.

            .. attribute:: end

               Ending endpoint.

            .. attribute:: path

               List of positions forming the path between endpoints.

            .. attribute:: completed

               Whether the flow is complete (endpoints connected).

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: color
               :type:  str


            .. py:attribute:: completed
               :type:  bool
               :value: False



            .. py:attribute:: end
               :type:  FlowEndpoint


            .. py:attribute:: id
               :type:  str
               :value: None



            .. py:attribute:: path
               :type:  list[haive.games.single_player.flow_free.models.Position]
               :value: None



            .. py:attribute:: start
               :type:  FlowEndpoint



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FlowEndpoint(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            An endpoint (colored dot) in Flow Free.

            .. attribute:: position

               Position of the endpoint on the board.

            .. attribute:: is_start

               Whether this is the start endpoint (otherwise it's the end).

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: is_start
               :type:  bool
               :value: True



            .. py:attribute:: position
               :type:  haive.games.single_player.flow_free.models.Position



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FlowFreeState(/, **data: Any)

            Bases: :py:obj:`haive.games.single_player.base.SinglePlayerGameState`


            State for the Flow Free game.

            .. attribute:: rows

               Number of rows in the grid.

            .. attribute:: cols

               Number of columns in the grid.

            .. attribute:: grid

               2D grid of cells.

            .. attribute:: flows

               Dictionary of flows by ID.

            .. attribute:: current_flow_id

               ID of the currently selected flow.

            .. attribute:: puzzle_id

               Identifier for the current puzzle.

            .. attribute:: hints_used

               Number of hints used.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: get_adjacent_positions(position: haive.games.single_player.flow_free.models.Position) -> list[haive.games.single_player.flow_free.models.Position]

               Get all valid adjacent positions.

               :param position: Position to get adjacent positions for.

               :returns: List of adjacent positions.



            .. py:method:: get_cell(position: haive.games.single_player.flow_free.models.Position) -> Cell | None

               Get the cell at the specified position.

               :param position: Position to get the cell for.

               :returns: The cell at the position, or None if out of bounds.



            .. py:method:: is_cell_empty(position: haive.games.single_player.flow_free.models.Position) -> bool

               Check if a cell is empty.

               :param position: Position to check.

               :returns: True if the cell is empty, False otherwise.



            .. py:method:: is_cell_endpoint(position: haive.games.single_player.flow_free.models.Position) -> bool

               Check if a cell contains an endpoint.

               :param position: Position to check.

               :returns: True if the cell contains an endpoint, False otherwise.



            .. py:method:: to_display_string() -> str

               Generate a string representation of the board for display.

               :returns: A formatted string representation of the board.



            .. py:property:: board_fill_percentage
               :type: float


               Calculate the percentage of the board that is filled.


            .. py:attribute:: cols
               :type:  int
               :value: None



            .. py:property:: completion_percentage
               :type: float


               Calculate the percentage of flows completed.


            .. py:attribute:: current_flow_id
               :type:  str | None
               :value: None



            .. py:property:: filled_cells
               :type: int


               Calculate the number of filled cells on the board.


            .. py:attribute:: flows
               :type:  dict[str, Flow]
               :value: None



            .. py:attribute:: grid
               :type:  list[list[Cell]]
               :value: None



            .. py:property:: is_solved
               :type: bool


               Check if the puzzle is solved.

               The puzzle is solved when all flows are completed and all cells are filled.


            .. py:attribute:: puzzle_id
               :type:  str
               :value: None



            .. py:attribute:: rows
               :type:  int
               :value: None



            .. py:property:: total_cells
               :type: int


               Calculate the total number of cells on the board.





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.flow_free.state import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

