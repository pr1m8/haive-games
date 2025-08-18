games.single_player.agent
=========================

.. py:module:: games.single_player.agent

Single-player game agent base class.

This module provides the SinglePlayerGameAgent base class for implementing single-player
game agents in the Haive framework.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Single-player game agent base class.

   This module provides the SinglePlayerGameAgent base class for implementing single-player
   game agents in the Haive framework.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.single_player.agent.SinglePlayerGameAgent

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: SinglePlayerGameAgent(config: T)

            Bases: :py:obj:`haive.games.base.agent.GameAgent`\ [\ :py:obj:`T`\ ]


            Base class for single-player game agents.

            This class extends GameAgent to provide specific functionality for
            single-player games where an LLM can act as the player, assistant,
            or game engine.

            Single-player games differ from multiplayer games in that they:
            - Don't require turn management between multiple players
            - Often involve puzzles, challenges, or solo adventures
            - May use the LLM as a game master or narrator

            .. rubric:: Example

            >>> from haive.games.single_player import SinglePlayerGameAgent
            >>> class WordleAgent(SinglePlayerGameAgent):
            ...     def __init__(self, config):
            ...         super().__init__(config)
            ...         self.state_manager = WordleStateManager

            .. attribute:: config

               Configuration for the single-player game

            .. attribute:: state_manager

               Manager for game state transitions

            Initialize the single-player game agent.

            :param config: Game-specific configuration


            .. py:method:: generate_game_response(state: dict) -> str
               :abstractmethod:


               Generate the game's response to the current state.

               :param state: Current game state

               :returns: Game's response or narration
               :rtype: str



            .. py:method:: handle_player_action(action: str) -> dict
               :abstractmethod:


               Handle a player action in the game.

               :param action: The player's action as a string

               :returns: Result of the action including any state changes
               :rtype: dict



            .. py:method:: setup_single_player_workflow() -> None

               Set up the workflow specific to single-player games.

               This method can be overridden by subclasses to customize the workflow for
               specific single-player game mechanics.







----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

