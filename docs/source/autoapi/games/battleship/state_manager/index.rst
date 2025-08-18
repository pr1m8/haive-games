games.battleship.state_manager
==============================

.. py:module:: games.battleship.state_manager

Battleship game state management module.

This module provides state transition logic for the Battleship game, including:
    - Game initialization
    - Ship placement validation
    - Move execution and validation
    - Strategic analysis tracking
    - Game state updates



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Battleship game state management module.

   This module provides state transition logic for the Battleship game, including:
       - Game initialization
       - Ship placement validation
       - Move execution and validation
       - Strategic analysis tracking
       - Game state updates



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.battleship.state_manager.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.battleship.state_manager.BattleshipStateManager

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: BattleshipStateManager

            Manager for Battleship game state transitions.

            This class provides methods for:
                - Initializing a new game
                - Placing ships
                - Making moves
                - Checking game status
                - Tracking strategic analysis

            The state manager ensures immutability by returning new state objects
            rather than modifying existing ones, making state transitions predictable
            and traceable.

            .. rubric:: Examples

            >>> manager = BattleshipStateManager()
            >>> state = manager.initialize()
            >>> state.game_phase
            GamePhase.SETUP


            .. py:method:: add_analysis(state: haive.games.battleship.state.BattleshipState, player: str, analysis: str) -> haive.games.battleship.state.BattleshipState
               :staticmethod:


               Add strategic analysis for a player.

               Records a strategic analysis provided by the LLM for the specified
               player, maintaining a limited history of the most recent analyses.

               :param state: Current game state
               :param player: Player for whom to add analysis
               :param analysis: Analysis text from LLM

               :returns: Updated game state with added analysis
               :rtype: BattleshipState

               .. rubric:: Examples

               >>> manager = BattleshipStateManager()
               >>> state = manager.initialize()
               >>> analysis = "Focus attacks on the center of the board."
               >>> new_state = manager.add_analysis(state, "player1", analysis)
               >>> new_state.player1_state.strategic_analysis[-1]
               'Focus attacks on the center of the board.'



            .. py:method:: initialize() -> haive.games.battleship.state.BattleshipState
               :staticmethod:


               Initialize a new Battleship game state.

               Creates a fresh game state with default settings, setting up empty
               player states, initial game phase, and empty move history.

               :returns: Fresh game state with default settings
               :rtype: BattleshipState

               .. rubric:: Examples

               >>> manager = BattleshipStateManager()
               >>> state = manager.initialize()
               >>> state.current_player
               'player1'
               >>> state.game_phase
               GamePhase.SETUP



            .. py:method:: make_move(state: haive.games.battleship.state.BattleshipState, player: str, move: haive.games.battleship.models.MoveCommand) -> haive.games.battleship.state.BattleshipState
               :staticmethod:


               Make a move for a player.

               Processes an attack command from the specified player, updates the game
               state with the move outcome (hit, miss, or sunk), and checks for
               game-ending conditions.

               :param state: Current game state
               :param player: Player making the move ("player1" or "player2")
               :param move: Attack command with target coordinates

               :returns: Updated game state with move outcome
               :rtype: BattleshipState

               .. rubric:: Examples

               >>> manager = BattleshipStateManager()
               >>> state = BattleshipState(game_phase=GamePhase.PLAYING)
               >>> move = MoveCommand(row=3, col=4)
               >>> new_state = manager.make_move(state, "player1", move)
               >>> # Check if move was recorded in history
               >>> len(new_state.move_history) > 0
               True



            .. py:method:: place_ships(state: haive.games.battleship.state.BattleshipState, player: str, placements: list[haive.games.battleship.models.ShipPlacement]) -> haive.games.battleship.state.BattleshipState
               :staticmethod:


               Place ships for a player.

               Processes a list of ship placements for the specified player,
               validating each placement against game rules (e.g., no overlapping
               ships, valid ship types, correct placement) and updating the game
               state accordingly.

               :param state: Current game state
               :param player: Player making the placements ("player1" or "player2")
               :param placements: List of ship placements

               :returns: Updated game state with placed ships or error message
               :rtype: BattleshipState

               .. rubric:: Examples

               >>> manager = BattleshipStateManager()
               >>> state = manager.initialize()
               >>> placements = [
               ...     ShipPlacement(ship_type=ShipType.CARRIER, coordinates=[
               ...         Coordinates(row=0, col=0), Coordinates(row=0, col=1),
               ...         Coordinates(row=0, col=2), Coordinates(row=0, col=3),
               ...         Coordinates(row=0, col=4)
               ...     ]),
               ...     # Additional placements for other ships...
               ... ]
               >>> new_state = manager.place_ships(state, "player1", placements)
               >>> new_state.player1_state.has_placed_ships
               True




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.battleship.state_manager import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

