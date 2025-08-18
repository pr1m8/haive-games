games.framework.base.agent
==========================

.. py:module:: games.framework.base.agent

Base game agent module.

This module provides the foundational GameAgent class that implements common workflow patterns
for game-specific agents. It handles game initialization, move generation, position analysis,
and game flow control.

.. rubric:: Example

>>> class ChessAgent(GameAgent[ChessConfig]):
...     def __init__(self, config: ChessConfig):
...         super().__init__(config)
...         self.state_manager = ChessStateManager

Typical usage:
    - Inherit from GameAgent to create game-specific agents
    - Override necessary methods like prepare_move_context and extract_move
    - Use the setup_workflow method to customize the game flow



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Base game agent module.

   This module provides the foundational GameAgent class that implements common workflow patterns
   for game-specific agents. It handles game initialization, move generation, position analysis,
   and game flow control.

   .. rubric:: Example

   >>> class ChessAgent(GameAgent[ChessConfig]):
   ...     def __init__(self, config: ChessConfig):
   ...         super().__init__(config)
   ...         self.state_manager = ChessStateManager

   Typical usage:
       - Inherit from GameAgent to create game-specific agents
       - Override necessary methods like prepare_move_context and extract_move
       - Use the setup_workflow method to customize the game flow



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.framework.base.agent.T

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.framework.base.agent.GameAgent

            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.framework.base.agent.run_game

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameAgent(config: haive.games.framework.base.config.GameConfig)

            Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.games.framework.base.config.GameConfig`\ ], :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


            Base game agent that implements common workflow patterns.

            This class provides a foundation for building game-specific agents by implementing
            common patterns for game initialization, move generation, position analysis, and
            game flow control. Game-specific agents should inherit from this class and
            override the necessary methods.

            .. attribute:: config

               Configuration for the game agent.

               :type: GameConfig

            .. attribute:: state_manager

               Manager for handling game state transitions.

            .. attribute:: engines

               Dictionary of LLM engines for different functions.

               :type: Dict[str, Any]

            .. attribute:: graph

               The workflow graph for the game.

            .. rubric:: Example

            >>> class ChessAgent(GameAgent[ChessConfig]):
            ...     def __init__(self, config: ChessConfig):
            ...         super().__init__(config)
            ...         self.state_manager = ChessStateManager
            ...
            ...     def prepare_move_context(self, state, player):
            ...         legal_moves = self.state_manager.get_legal_moves(state)
            ...         return {"legal_moves": legal_moves}

            Initialize the game agent.

            :param config: Configuration for the game agent.
                           Defaults to GameConfig().
            :type config: GameConfig, optional


            .. py:method:: analyze_player1(state: T) -> langgraph.types.Command
               :abstractmethod:


               Analyze position for player 1.

               This method should be implemented by subclasses to handle position
               analysis specifically for player 1.

               :param state: The current game state.
               :type state: T

               :returns: A command containing the updated game state with analysis.
               :rtype: Command

               :raises NotImplementedError: This method must be implemented by subclasses.

               .. rubric:: Example

               >>> def analyze_player1(self, state):
               ...     return self.analyze_position(state, "player1")



            .. py:method:: analyze_player2(state: T) -> langgraph.types.Command
               :abstractmethod:


               Analyze position for player 2.

               This method should be implemented by subclasses to handle position
               analysis specifically for player 2.

               :param state: The current game state.
               :type state: T

               :returns: A command containing the updated game state with analysis.
               :rtype: Command

               :raises NotImplementedError: This method must be implemented by subclasses.

               .. rubric:: Example

               >>> def analyze_player2(self, state):
               ...     return self.analyze_position(state, "player2")



            .. py:method:: analyze_position(state: T, player: str) -> langgraph.types.Command

               Analyze the position for the specified player.

               This method handles position analysis including:
               1. Getting the appropriate analyzer engine
               2. Preparing the analysis context
               3. Generating and storing the analysis

               :param state: The current game state.
               :type state: T
               :param player: The player for whom to analyze the position.
               :type player: str

               :returns: A command containing the updated game state with analysis.
               :rtype: Command

               .. rubric:: Example

               >>> def analyze_position(self, state, player):
               ...     analyzer = self.engines.get(f"{player}_analyzer")
               ...     analysis = analyzer.invoke({"position": state.board})
               ...     return Command(update={f"{player}_analysis": analysis})



            .. py:method:: extract_move(response: Any) -> Any
               :abstractmethod:


               Extract move from engine response.

               This method should be implemented by subclasses to parse the LLM's
               response and extract a valid move.

               :param response: The raw response from the LLM engine.
               :type response: Any

               :returns: A valid move object for the game.
               :rtype: Any

               :raises NotImplementedError: This method must be implemented by subclasses.

               .. rubric:: Example

               >>> def extract_move(self, response):
               ...     move_text = response.get("move")
               ...     return ChessMove.from_uci(move_text)



            .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

               Initialize a new game.

               :param state: The initial state dictionary.
               :type state: Dict[str, Any]

               :returns: A command containing the initialized game state.
               :rtype: Command

               .. rubric:: Example

               >>> def initialize_game(self, state):
               ...     game_state = self.state_manager.initialize()
               ...     return Command(update=game_state.dict())



            .. py:method:: make_move(state: T, player: str) -> langgraph.types.Command

               Make a move for the specified player.

               This method handles the complete move generation process including:
               1. Getting the appropriate engine for the player
               2. Preparing the move context
               3. Generating and validating the move
               4. Applying the move to the game state

               :param state: The current game state.
               :type state: T
               :param player: The player making the move.
               :type player: str

               :returns: A command containing the updated game state after the move.
               :rtype: Command

               .. rubric:: Example

               >>> def make_move(self, state, player):
               ...     engine = self.engines.get(f"{player}_player")
               ...     move_context = self.prepare_move_context(state, player)
               ...     response = engine.invoke(move_context)
               ...     move = self.extract_move(response)
               ...     new_state = self.state_manager.apply_move(state, move)
               ...     return Command(update=new_state.dict())



            .. py:method:: make_player1_move(state: T) -> langgraph.types.Command
               :abstractmethod:


               Make a move for player 1.

               This method should be implemented by subclasses to handle moves
               specifically for player 1.

               :param state: The current game state.
               :type state: T

               :returns: A command containing the updated game state after the move.
               :rtype: Command

               :raises NotImplementedError: This method must be implemented by subclasses.

               .. rubric:: Example

               >>> def make_player1_move(self, state):
               ...     return self.make_move(state, "player1")



            .. py:method:: make_player2_move(state: T) -> langgraph.types.Command
               :abstractmethod:


               Make a move for player 2.

               This method should be implemented by subclasses to handle moves
               specifically for player 2.

               :param state: The current game state.
               :type state: T

               :returns: A command containing the updated game state after the move.
               :rtype: Command

               :raises NotImplementedError: This method must be implemented by subclasses.

               .. rubric:: Example

               >>> def make_player2_move(self, state):
               ...     return self.make_move(state, "player2")



            .. py:method:: prepare_analysis_context(state: T, player: str) -> dict[str, Any]
               :abstractmethod:


               Prepare context for position analysis.

               This method should be implemented by subclasses to provide the necessary
               context for the LLM to analyze a position.

               :param state: The current game state.
               :type state: T
               :param player: The player for whom to prepare the analysis context.
               :type player: str

               :returns: The context dictionary for position analysis.
               :rtype: Dict[str, Any]

               :raises NotImplementedError: This method must be implemented by subclasses.

               .. rubric:: Example

               >>> def prepare_analysis_context(self, state, player):
               ...     return {
               ...         "board": state.board.to_fen(),
               ...         "material_count": state.get_material_count(player),
               ...         "previous_moves": state.move_history[-5:]
               ...     }



            .. py:method:: prepare_move_context(state: T, player: str) -> dict[str, Any]
               :abstractmethod:


               Prepare context for move generation.

               This method should be implemented by subclasses to provide the necessary
               context for the LLM to generate a move.

               :param state: The current game state.
               :type state: T
               :param player: The player for whom to prepare the context.
               :type player: str

               :returns: The context dictionary for move generation.
               :rtype: Dict[str, Any]

               :raises NotImplementedError: This method must be implemented by subclasses.

               .. rubric:: Example

               >>> def prepare_move_context(self, state, player):
               ...     legal_moves = self.state_manager.get_legal_moves(state)
               ...     return {
               ...         "board": state.board.to_fen(),
               ...         "legal_moves": legal_moves,
               ...         "player": player
               ...     }



            .. py:method:: setup_workflow()

               Setup the standard game workflow with configurable analysis.

               This method sets up the default game workflow including initialization,
               player moves, and optional position analysis. Override this method to
               implement custom game flows.

               The default workflow includes:
               1. Game initialization
               2. Alternating player moves
               3. Optional position analysis before each move
               4. Game continuation checks between moves

               .. rubric:: Example

               >>> def setup_workflow(self):
               ...     # Add custom nodes
               ...     self.graph.add_node("custom_analysis", self.analyze_position)
               ...     # Modify the workflow
               ...     self.graph.add_edge("initialize_game", "custom_analysis")



            .. py:method:: should_continue_game(state: T) -> bool

               Determine if the game should continue.

               :param state: The current game state.
               :type state: T

               :returns: True if the game should continue, False otherwise.
               :rtype: bool

               .. rubric:: Example

               >>> def should_continue_game(self, state):
               ...     return state.moves_remaining > 0 and not state.checkmate




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_game(agent: GameAgent, initial_state: dict[str, Any] | None = None)

            Run a complete game with the given agent.

            This function executes a game from start to finish using the provided agent.
            It handles game initialization, move execution, state visualization, and
            error reporting. The game can optionally start from a provided initial state.

            :param agent: The game agent to run the game with.
            :type agent: GameAgent
            :param initial_state: Initial game state.
                                  If not provided, a new game will be initialized. Defaults to None.
            :type initial_state: Optional[Dict[str, Any]], optional

            .. rubric:: Example

            >>> agent = ChessAgent(ChessConfig())
            >>> # Start a new game
            >>> run_game(agent)
            >>>
            >>> # Continue from a saved state
            >>> run_game(agent, saved_state)

            .. note::

               - The function will print game progress to the console
               - Game visualization depends on the agent's visualize_state method
               - Game history will be saved using the agent's save_state_history method



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: T




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.framework.base.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

