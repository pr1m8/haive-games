games.risk.state_manager
========================

.. py:module:: games.risk.state_manager

State manager for the Risk game.

This module defines the RiskStateManager class that manages game state transitions, rule
enforcement, and game progression.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   State manager for the Risk game.

   This module defines the RiskStateManager class that manages game state transitions, rule
   enforcement, and game progression.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.risk.state_manager.RiskStateManager

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: RiskStateManager(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Manages state transitions and rule enforcement for the Risk game.

            This class is responsible for applying moves to the game state,
            enforcing game rules, and managing game progression through different phases.

            .. attribute:: state

               The current game state.

            .. attribute:: config

               Configuration settings for the game.

            .. attribute:: move_history

               History of all moves made in the game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: _advance_to_next_player() -> None

               Advance to the next active player.



            .. py:method:: _apply_attack(move: haive.games.risk.models.RiskMove) -> None

               Apply an attack move to the game state.

               :param move: The attack move to apply.



            .. py:method:: _apply_fortify(move: haive.games.risk.models.RiskMove) -> None

               Apply a fortify move to the game state.

               :param move: The fortify move to apply.



            .. py:method:: _apply_place_armies(move: haive.games.risk.models.RiskMove) -> None

               Apply a place armies move to the game state.

               :param move: The place armies move to apply.



            .. py:method:: _apply_trade_cards(move: haive.games.risk.models.RiskMove) -> None

               Apply a trade cards move to the game state.

               :param move: The trade cards move to apply.



            .. py:method:: _calculate_reinforcements() -> None

               Calculate reinforcements for the current player.



            .. py:method:: _check_game_over() -> None

               Check if the game is over.



            .. py:method:: _end_turn() -> None

               End the current player's turn and prepare for the next player.



            .. py:method:: _validate_attack(move: haive.games.risk.models.RiskMove) -> None

               Validate an attack move.

               :param move: The move to validate.

               :raises ValueError: If the move is invalid.



            .. py:method:: _validate_fortify(move: haive.games.risk.models.RiskMove) -> None

               Validate a fortify move.

               :param move: The move to validate.

               :raises ValueError: If the move is invalid.



            .. py:method:: _validate_move(move: haive.games.risk.models.RiskMove) -> None

               Validate that a move is legal according to the game rules.

               :param move: The move to validate.

               :raises ValueError: If the move is invalid.



            .. py:method:: _validate_place_armies(move: haive.games.risk.models.RiskMove) -> None

               Validate a place armies move.

               :param move: The move to validate.

               :raises ValueError: If the move is invalid.



            .. py:method:: _validate_trade_cards(move: haive.games.risk.models.RiskMove) -> None

               Validate a trade cards move.

               :param move: The move to validate.

               :raises ValueError: If the move is invalid.



            .. py:method:: apply_move(move: haive.games.risk.models.RiskMove) -> haive.games.risk.state.RiskState

               Apply a move to the current game state.

               :param move: The move to apply.

               :returns: The updated game state after applying the move.

               :raises ValueError: If the move is invalid or violates game rules.



            .. py:method:: initialize(player_names: list[str], config: haive.games.risk.config.RiskConfig | None = None) -> RiskStateManager
               :classmethod:


               Initialize a new Risk game state manager.

               :param player_names: List of player names.
               :param config: Optional configuration for the game.
                              If not provided, classic Risk rules will be used.

               :returns: A new RiskStateManager with initialized state.

               :raises ValueError: If the number of players is invalid.



            .. py:attribute:: config
               :type:  haive.games.risk.config.RiskConfig
               :value: None



            .. py:attribute:: move_history
               :type:  list[haive.games.risk.models.RiskMove]
               :value: None



            .. py:attribute:: state
               :type:  haive.games.risk.state.RiskState





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.risk.state_manager import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

