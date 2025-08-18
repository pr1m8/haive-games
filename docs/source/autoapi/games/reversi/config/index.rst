games.reversi.config
====================

.. py:module:: games.reversi.config

Configuration model for the Reversi (Othello) game agent.

Defines game metadata, initial settings, and engine bindings used to drive the game loop
and decision-making by language models.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Configuration model for the Reversi (Othello) game agent.

   Defines game metadata, initial settings, and engine bindings used to drive the game loop
   and decision-making by language models.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.reversi.config.ReversiConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ReversiConfig

            Bases: :py:obj:`haive.games.framework.base.config.GameConfig`


            Configuration for the Reversi/Othello game agent.

            .. attribute:: name

               Name of the game.

               :type: str

            .. attribute:: state_schema

               The state model used for gameplay.

               :type: Type[ReversiState]

            .. attribute:: engines

               Mapping of engine names to LLM configurations.

               :type: Dict[str, AugLLMConfig]

            .. attribute:: enable_analysis

               Whether to run post-move analysis.

               :type: bool

            .. attribute:: visualize

               Whether to render the board visually in the console.

               :type: bool

            .. attribute:: first_player

               Symbol of the player who starts (Black or White).

               :type: Literal['B', 'W']

            .. attribute:: player_B

               Who controls the Black pieces.

               :type: Literal['player1', 'player2']

            .. attribute:: player_W

               Who controls the White pieces.

               :type: Literal['player1', 'player2']


            .. py:method:: default_config()
               :classmethod:


               Create a default configuration for Reversi.

               :returns: An instance with standard engine bindings and player layout.
               :rtype: ReversiConfig



            .. py:attribute:: enable_analysis
               :type:  bool
               :value: None



            .. py:attribute:: engines
               :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
               :value: None



            .. py:attribute:: first_player
               :type:  Literal['B', 'W']
               :value: None



            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: player_B
               :type:  Literal['player1', 'player2']
               :value: None



            .. py:attribute:: player_W
               :type:  Literal['player1', 'player2']
               :value: None



            .. py:attribute:: state_schema
               :type:  type[haive.games.reversi.state.ReversiState]
               :value: None



            .. py:attribute:: visualize
               :type:  bool
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.reversi.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

