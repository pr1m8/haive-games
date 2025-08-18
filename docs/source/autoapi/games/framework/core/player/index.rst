games.framework.core.player
===========================

.. py:module:: games.framework.core.player

Module documentation for games.framework.core.player


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">5 classes</span> • <span class="module-stat">2 attributes</span>   </div>


      

.. admonition:: Attributes (2)
   :class: tip

   .. autoapisummary::

      games.framework.core.player.M
      games.framework.core.player.S

            
            

.. admonition:: Classes (5)
   :class: note

   .. autoapisummary::

      games.framework.core.player.AIPlayer
      games.framework.core.player.HumanPlayer
      games.framework.core.player.Player
      games.framework.core.player.RandomAIPlayer
      games.framework.core.player.RuleBasedAIPlayer

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: AIPlayer(/, **data: Any)

            Bases: :py:obj:`Player`, :py:obj:`Generic`\ [\ :py:obj:`S`\ , :py:obj:`M`\ ]


            Base class for AI/computer-controlled players.

            AI players automatically generate moves based on the game state.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: get_move(game_state: S, valid_moves: list[M]) -> M | None
               :abstractmethod:


               Get a move from this AI player.

               :param game_state: Current game state
               :param valid_moves: List of valid moves

               :returns: The chosen move, or None if no move chosen



            .. py:attribute:: difficulty
               :type:  str
               :value: 'medium'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HumanPlayer(/, **data: Any)

            Bases: :py:obj:`Player`


            A human player that requires external input for moves.

            Human players don't automatically generate moves; they receive them through UI
            interactions.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: get_move(game_state: S, valid_moves: list[M]) -> M | None

               Get a move from this player.

               For human players, this should be called after receiving
               input from the user interface.

               :param game_state: Current game state
               :param valid_moves: List of valid moves

               :returns: None (human players don't auto-generate moves)



            .. py:method:: select_move(move: M) -> M

               Select a move for this player.

               :param move: The selected move

               :returns: The selected move




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Player(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`abc.ABC`


            Base class for all player types in games.

            This is an abstract base class that defines the common interface for all player
            types (human, AI, etc.).


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: get_move(game_state: S, valid_moves: list[M]) -> M | None
               :abstractmethod:


               Get a move from this player.

               :param game_state: Current game state
               :param valid_moves: List of valid moves

               :returns: The chosen move, or None if no move chosen



            .. py:attribute:: id
               :type:  str
               :value: None



            .. py:attribute:: is_active
               :type:  bool
               :value: True



            .. py:attribute:: name
               :type:  str


            .. py:attribute:: properties
               :type:  dict[str, Any]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: RandomAIPlayer

            Bases: :py:obj:`AIPlayer`\ [\ :py:obj:`S`\ , :py:obj:`M`\ ]


            An AI player that selects random valid moves.

            This is the simplest form of AI player, useful for testing or for games where random
            play is appropriate.



            .. py:method:: get_move(game_state: S, valid_moves: list[M]) -> M | None

               Get a random valid move.

               :param game_state: Current game state
               :param valid_moves: List of valid moves

               :returns: A randomly selected valid move, or None if no valid moves




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: RuleBasedAIPlayer

            Bases: :py:obj:`AIPlayer`\ [\ :py:obj:`S`\ , :py:obj:`M`\ ]


            An AI player that follows predefined rules to select moves.

            Rule-based AIs use heuristics and decision trees to choose moves.



            .. py:method:: add_rule(condition: str, action: str, priority: int = 1) -> None

               Add a rule for the AI to follow.

               :param condition: When to apply this rule
               :param action: What to do when the condition is met
               :param priority: Rule priority (higher numbers take precedence)



            .. py:method:: get_move(game_state: S, valid_moves: list[M]) -> M | None

               Get a move using predefined rules.

               :param game_state: Current game state
               :param valid_moves: List of valid moves

               :returns: The chosen move, or None if no move chosen



            .. py:attribute:: rules
               :type:  list[dict[str, Any]]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: M


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: S




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.framework.core.player import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

