games.tic_tac_toe.models
========================

.. py:module:: games.tic_tac_toe.models

Comprehensive data models for strategic Tic Tac Toe gameplay and positional analysis.

This module provides sophisticated data models for the classic game of Tic Tac Toe,
supporting both traditional gameplay and advanced strategic analysis. The models
enable structured data handling throughout the game implementation and provide
strong typing for LLM-based components and strategic decision-making systems.

The models support:
- Complete move representation with coordinate validation
- Strategic analysis with winning/blocking move detection
- Fork opportunity identification for advanced play
- Position evaluation from game theory perspective
- Multi-level strategic recommendations
- Perfect play analysis and minimax integration

.. rubric:: Examples

Basic move representation::

    move = TicTacToeMove(
        row=0,
        col=1,
        player="X"
    )
    print(str(move))  # Output: "X places at (0, 1)"

Strategic position analysis::

    analysis = TicTacToeAnalysis(
        winning_moves=[{"row": 0, "col": 2}],
        blocking_moves=[{"row": 1, "col": 1}],
        fork_opportunities=[],
        center_available=False,
        corner_available=True,
        position_evaluation="winning",
        recommended_move={"row": 0, "col": 2},
        strategy="Win immediately by completing top row"
    )

Fork creation analysis::

    analysis = TicTacToeAnalysis(
        winning_moves=[],
        blocking_moves=[],
        fork_opportunities=[{"row": 0, "col": 0}, {"row": 2, "col": 2}],
        center_available=False,
        corner_available=True,
        position_evaluation="unclear",
        recommended_move={"row": 0, "col": 0},
        strategy="Create fork with two winning threats"
    )

.. note::

   All models use Pydantic for validation and support both JSON serialization
   and integration with LLM-based strategic analysis systems for perfect play.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 classes</span>   </div>

.. autoapi-nested-parse::

   Comprehensive data models for strategic Tic Tac Toe gameplay and positional analysis.

   This module provides sophisticated data models for the classic game of Tic Tac Toe,
   supporting both traditional gameplay and advanced strategic analysis. The models
   enable structured data handling throughout the game implementation and provide
   strong typing for LLM-based components and strategic decision-making systems.

   The models support:
   - Complete move representation with coordinate validation
   - Strategic analysis with winning/blocking move detection
   - Fork opportunity identification for advanced play
   - Position evaluation from game theory perspective
   - Multi-level strategic recommendations
   - Perfect play analysis and minimax integration

   .. rubric:: Examples

   Basic move representation::

       move = TicTacToeMove(
           row=0,
           col=1,
           player="X"
       )
       print(str(move))  # Output: "X places at (0, 1)"

   Strategic position analysis::

       analysis = TicTacToeAnalysis(
           winning_moves=[{"row": 0, "col": 2}],
           blocking_moves=[{"row": 1, "col": 1}],
           fork_opportunities=[],
           center_available=False,
           corner_available=True,
           position_evaluation="winning",
           recommended_move={"row": 0, "col": 2},
           strategy="Win immediately by completing top row"
       )

   Fork creation analysis::

       analysis = TicTacToeAnalysis(
           winning_moves=[],
           blocking_moves=[],
           fork_opportunities=[{"row": 0, "col": 0}, {"row": 2, "col": 2}],
           center_available=False,
           corner_available=True,
           position_evaluation="unclear",
           recommended_move={"row": 0, "col": 0},
           strategy="Create fork with two winning threats"
       )

   .. note::

      All models use Pydantic for validation and support both JSON serialization
      and integration with LLM-based strategic analysis systems for perfect play.



      
            
            

.. admonition:: Classes (2)
   :class: note

   .. autoapisummary::

      games.tic_tac_toe.models.TicTacToeAnalysis
      games.tic_tac_toe.models.TicTacToeMove

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: TicTacToeAnalysis(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Advanced strategic analysis model for Tic Tac Toe positions with game theory.
            insights.

            This model provides comprehensive analysis of Tic Tac Toe positions using
            game theory principles, perfect play algorithms, and strategic heuristics.
            It supports both educational gameplay and competitive AI decision-making
            with detailed explanations of optimal strategies.

            The analysis includes:
            - Immediate win detection and threat assessment
            - Defensive move identification to prevent losses
            - Fork creation and prevention strategies
            - Positional advantage evaluation (center, corners, edges)
            - Game-theoretic position classification
            - Perfect play recommendations with explanations
            - Educational insights for learning optimal strategy

            .. attribute:: winning_moves

               Coordinates that win immediately.
               Each dict contains 'row' and 'col' keys for winning positions.

               :type: List[Dict[str, int]]

            .. attribute:: blocking_moves

               Moves that must be played to prevent loss.
               Critical defensive moves to block opponent's winning threats.

               :type: List[Dict[str, int]]

            .. attribute:: fork_opportunities

               Moves creating multiple threats.
               Advanced positions that force opponent into defensive play.

               :type: List[Dict[str, int]]

            .. attribute:: center_available

               Whether the center square (1,1) is unoccupied.
               Center control is crucial for optimal Tic Tac Toe strategy.

               :type: bool

            .. attribute:: corner_available

               Whether any corner square is unoccupied.
               Corners are second-best positions after center.

               :type: bool

            .. attribute:: position_evaluation

               Game-theoretic evaluation of position.
               Classifications: winning, losing, drawing, unclear.

               :type: Literal

            .. attribute:: recommended_move

               Best move by perfect play.
               Computed using minimax algorithm with full game tree search.

               :type: Optional[Dict[str, int]]

            .. attribute:: strategy

               Natural language explanation of optimal strategy.
               Educational description for understanding the position.

               :type: str

            .. attribute:: move_priority

               Priority ranking of recommended move.
               1=win, 2=block loss, 3=create fork, 4=block fork, 5=positional.

               :type: Optional[int]

            .. attribute:: optimal_outcome

               Expected result with perfect play.
               Predicts game outcome assuming both players play optimally.

               :type: Optional[Literal]

            .. rubric:: Examples

            Winning position analysis::

                analysis = TicTacToeAnalysis(
                    winning_moves=[{"row": 0, "col": 2}],
                    blocking_moves=[],
                    fork_opportunities=[],
                    center_available=False,
                    corner_available=False,
                    position_evaluation="winning",
                    recommended_move={"row": 0, "col": 2},
                    strategy="Win immediately by completing the top row",
                    move_priority=1,
                    optimal_outcome="win"
                )

            Defensive position requiring blocking::

                analysis = TicTacToeAnalysis(
                    winning_moves=[],
                    blocking_moves=[{"row": 1, "col": 1}],
                    fork_opportunities=[],
                    center_available=True,
                    corner_available=True,
                    position_evaluation="losing",
                    recommended_move={"row": 1, "col": 1},
                    strategy="Must block opponent's winning threat in center",
                    move_priority=2,
                    optimal_outcome="draw"
                )

            Fork creation opportunity::

                analysis = TicTacToeAnalysis(
                    winning_moves=[],
                    blocking_moves=[],
                    fork_opportunities=[{"row": 0, "col": 0}, {"row": 2, "col": 2}],
                    center_available=False,
                    corner_available=True,
                    position_evaluation="unclear",
                    recommended_move={"row": 0, "col": 0},
                    strategy="Create fork with two winning threats - opponent cannot block both",
                    move_priority=3,
                    optimal_outcome="win"
                )

            Opening position analysis::

                analysis = TicTacToeAnalysis(
                    winning_moves=[],
                    blocking_moves=[],
                    fork_opportunities=[],
                    center_available=True,
                    corner_available=True,
                    position_evaluation="unclear",
                    recommended_move={"row": 1, "col": 1},
                    strategy="Control center for maximum strategic flexibility",
                    move_priority=5,
                    optimal_outcome="draw"
                )

            .. note::

               This model provides the foundation for perfect Tic Tac Toe play.
               With optimal strategy, the game always ends in a draw.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: validate_move_coordinates(v: list[dict[str, int]]) -> list[dict[str, int]]
               :classmethod:


               Validate that all move coordinates are within bounds.

               :param v: List of move coordinates to validate.
               :type v: List[Dict[str, int]]

               :returns: Validated move coordinates.
               :rtype: List[Dict[str, int]]

               :raises ValueError: If coordinates are out of bounds.



            .. py:attribute:: blocking_moves
               :type:  list[dict[str, int]]
               :value: None



            .. py:attribute:: center_available
               :type:  bool
               :value: None



            .. py:attribute:: corner_available
               :type:  bool
               :value: None



            .. py:attribute:: fork_opportunities
               :type:  list[dict[str, int]]
               :value: None



            .. py:property:: has_immediate_threat
               :type: bool


               Check if there's an immediate win or loss threat.

               :returns: True if winning or blocking moves exist.
               :rtype: bool


            .. py:attribute:: model_config

               Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


            .. py:property:: move_count
               :type: dict[str, int]


               Count available moves by category.

               :returns: Counts of different move types.
               :rtype: Dict[str, int]


            .. py:attribute:: move_priority
               :type:  int | None
               :value: None



            .. py:attribute:: optimal_outcome
               :type:  Literal['win', 'draw', 'loss'] | None
               :value: None



            .. py:attribute:: position_evaluation
               :type:  Literal['winning', 'losing', 'drawing', 'unclear']
               :value: None



            .. py:attribute:: recommended_move
               :type:  dict[str, int] | None
               :value: None



            .. py:attribute:: strategy
               :type:  str
               :value: None



            .. py:property:: threat_level
               :type: str


               Assess the urgency level of the position.

               :returns: Threat level classification.
               :rtype: str


            .. py:attribute:: winning_moves
               :type:  list[dict[str, int]]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: TicTacToeMove(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Comprehensive representation of a Tic Tac Toe move with validation and game.
            context.

            This model provides complete representation of moves in Tic Tac Toe, supporting
            both basic gameplay and advanced strategic analysis. It includes coordinate
            validation, player identification, and integration with game state management
            for perfect play algorithms and educational systems.

            The model supports:
            - Coordinate validation for 3x3 grid constraints
            - Player symbol enforcement (X or O)
            - Move notation generation for game records
            - Integration with minimax and alpha-beta pruning
            - Educational move explanations
            - Tournament play recording standards

            .. attribute:: row

               Row index (0-2) where the player places their symbol.
               Uses 0-based indexing with 0=top, 1=middle, 2=bottom.

               :type: int

            .. attribute:: col

               Column index (0-2) where the player places their symbol.
               Uses 0-based indexing with 0=left, 1=center, 2=right.

               :type: int

            .. attribute:: player

               The symbol representing the player.
               'X' traditionally plays first, 'O' plays second.

               :type: Literal['X', 'O']

            .. rubric:: Examples

            Basic move creation::

                move = TicTacToeMove(row=1, col=1, player="X")
                print(str(move))  # Output: "X places at (1, 1)"
                # This represents X playing in the center square

            Corner move for strategic play::

                corner_move = TicTacToeMove(row=0, col=0, player="X")
                # Opening corner move - classic strategic opening

            Blocking move example::

                block = TicTacToeMove(row=2, col=2, player="O")
                # O blocks X's potential diagonal win

            Educational notation::

                move = TicTacToeMove(row=0, col=2, player="X")
                # Top-right corner: strategic for controlling diagonals

            .. note::

               Moves are validated to ensure coordinates are within the 3x3 grid.
               The string representation provides human-readable move descriptions.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               Generate human-readable string representation of the move.

               :returns: Formatted move description with position details.
               :rtype: str

               .. rubric:: Examples

               >>> move = TicTacToeMove(row=1, col=1, player="X")
               >>> print(str(move))
               X places at (1, 1) - center

               >>> move = TicTacToeMove(row=0, col=0, player="O")
               >>> print(str(move))
               O places at (0, 0) - top-left corner



            .. py:property:: board_position
               :type: str


               Get human-readable board position name.

               :returns: Position name like 'center', 'top-left corner', etc.
               :rtype: str


            .. py:attribute:: col
               :type:  int
               :value: None



            .. py:property:: is_center
               :type: bool


               Check if this move is the center position.

               :returns: True if the move is in the center (most valuable position).
               :rtype: bool


            .. py:property:: is_corner
               :type: bool


               Check if this move is a corner position.

               :returns: True if the move is in a corner (strategic positions).
               :rtype: bool


            .. py:property:: is_edge
               :type: bool


               Check if this move is an edge (non-corner, non-center) position.

               :returns: True if the move is on an edge (weakest positions).
               :rtype: bool


            .. py:attribute:: player
               :type:  Literal['X', 'O']
               :value: None



            .. py:attribute:: row
               :type:  int
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.tic_tac_toe.models import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

