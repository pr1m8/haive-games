games.clue.state_manager
========================

.. py:module:: games.clue.state_manager

State manager for the Clue game.

This module defines the state management for the Clue game, providing methods for game
logic and state transitions.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   State manager for the Clue game.

   This module defines the state management for the Clue game, providing methods for game
   logic and state transitions.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.clue.state_manager.ClueStateManager

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ClueStateManager

            Bases: :py:obj:`haive.games.framework.base.state_manager.GameStateManager`\ [\ :py:obj:`haive.games.clue.state.ClueState`\ ]


            Manager for Clue game state.


            .. py:method:: add_analysis(state: haive.games.clue.state.ClueState, player: str, hypothesis: dict[str, Any]) -> haive.games.clue.state.ClueState
               :classmethod:


               Add a hypothesis to the state.

               :param state: Current game state
               :param player: Player performing the analysis
               :param hypothesis: Hypothesis details

               :returns: Updated state with added hypothesis



            .. py:method:: apply_move(state: haive.games.clue.state.ClueState, move: haive.games.clue.models.ClueGuess) -> haive.games.clue.state.ClueState
               :classmethod:


               Apply a guess to the current state.

               :param state: Current game state
               :param move: The guess to apply

               :returns: Updated game state



            .. py:method:: check_game_status(state: haive.games.clue.state.ClueState) -> haive.games.clue.state.ClueState
               :classmethod:


               Check and potentially update game status.

               :param state: Current game state

               :returns: Updated game state



            .. py:method:: get_legal_moves(state: haive.games.clue.state.ClueState) -> list[haive.games.clue.models.ClueGuess]
               :classmethod:


               Get all legal moves for the current state.

               :param state: The current game state

               :returns: List of possible legal guesses



            .. py:method:: get_possible_solutions(state: haive.games.clue.state.ClueState) -> set[tuple[str, str, str]]
               :classmethod:


               Get possible solutions based on the current game state.

               :param state: Current game state

               :returns: Set of possible solutions as (suspect, weapon, room) tuples



            .. py:method:: get_winner(state: haive.games.clue.state.ClueState) -> str | None
               :classmethod:


               Get the winner of the game.

               :param state: Current game state

               :returns: Winner of the game, or None if ongoing



            .. py:method:: initialize(**kwargs) -> haive.games.clue.state.ClueState
               :classmethod:


               Initialize a new Clue game.

               :param \*\*kwargs: Keyword arguments for game initialization

               :returns: A new Clue game state
               :rtype: ClueState






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.clue.state_manager import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

