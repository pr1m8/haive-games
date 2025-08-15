games.framework.multi_player.agent
==================================

.. py:module:: games.framework.multi_player.agent

.. autoapi-nested-parse::

   Multi-player game agent implementation.

   This module provides the base agent class for multi-player games, supporting:
       - Variable number of players
       - Role-based player configurations
       - Phase-based game flow
       - Information hiding between players
       - Concurrent or sequential player actions

   .. rubric:: Example

   >>> from haive.agents.agent_games.framework.multi_player.agent import MultiPlayerGameAgent
   >>>
   >>> class ChessAgent(MultiPlayerGameAgent[ChessState]):
   ...     def __init__(self, config: ChessConfig):
   ...         super().__init__(config)
   ...         self.state_manager = ChessStateManager


   .. autolink-examples:: games.framework.multi_player.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   games.framework.multi_player.agent.T


Classes
-------

.. autoapisummary::

   games.framework.multi_player.agent.MultiPlayerGameAgent


Module Contents
---------------

.. py:class:: MultiPlayerGameAgent(config: haive.games.framework.multi_player.config.MultiPlayerGameConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.games.framework.multi_player.config.MultiPlayerGameConfig`\ ], :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   Base game agent for multi-player games.

   This class provides the foundation for implementing multi-player game agents
   with support for role-based configurations, phase-based gameplay, and
   information hiding between players.

   Type Parameters:
       T: The game state type, must be a Pydantic BaseModel.

   .. attribute:: config

      Agent configuration.

      :type: MultiPlayerGameConfig

   .. attribute:: engines

      LLM engines by role and function.

      :type: Dict[str, Dict[str, Any]]

   .. attribute:: state_manager

      State manager class.

      :type: Type[MultiPlayerGameStateManager]

   .. attribute:: graph

      Game workflow graph.

      :type: StateGraph

   .. rubric:: Example

   >>> class MafiaAgent(MultiPlayerGameAgent[MafiaState]):
   ...     def __init__(self, config: MafiaConfig):
   ...         super().__init__(config)
   ...         self.state_manager = MafiaStateManager
   ...
   ...     def prepare_move_context(self, state, player_id):
   ...         return {
   ...             "game_state": state.board_string,
   ...             "player_role": self.get_player_role(state, player_id)
   ...         }

   Initialize the multi-player game agent.

   :param config: Agent configuration including
                  state schema, LLM configurations, and game settings.
   :type config: MultiPlayerGameConfig


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MultiPlayerGameAgent
      :collapse:

   .. py:method:: _init_engines()

      Initialize the engines from the configuration.

      This method sets up LLM engines for each role and function, handling both AugLLM
      configurations and direct runnables.



      .. autolink-examples:: _init_engines
         :collapse:


   .. py:method:: determine_next_step_after_player_turn(state: haive.games.framework.multi_player.state.MultiPlayerGameState) -> str

      Determine what to do after a player's turn.

      This method handles complex game flow logic, including:
      - Checking game end conditions
      - Managing phase transitions
      - Handling night/day cycle transitions
      - Processing voting and action completions

      :param state: Current game state.
      :type state: MultiPlayerGameState

      :returns:

                Next step to take, one of:
                    - "end_game": Game is over
                    - "phase_transition": Move to next phase
                    - "next_player": Continue with next player
      :rtype: str

      .. rubric:: Example

      >>> state = MafiaGameState(game_phase="NIGHT", votes={"p1": "p2"})
      >>> # If all night actions complete
      >>> agent.determine_next_step_after_player_turn(state)
      'phase_transition'  # Move to day phase
      >>> # If more players need to act
      >>> agent.determine_next_step_after_player_turn(state)
      'next_player'  # Continue with next player


      .. autolink-examples:: determine_next_step_after_player_turn
         :collapse:


   .. py:method:: extract_move(response: Any, role: str) -> Any
      :abstractmethod:


      Extract move from engine response.

      :param response: Response from the engine.
      :type response: Any
      :param role: Role of the player.
      :type role: str

      :returns: Extracted move.
      :rtype: Any

      :raises NotImplementedError: Must be implemented by subclass.


      .. autolink-examples:: extract_move
         :collapse:


   .. py:method:: get_engine_for_player(role: str, function: str) -> Any | None

      Get the appropriate engine for a player based on role and function.

      :param role: Player's role.
      :type role: str
      :param function: Function to get engine for.
      :type function: str

      :returns: Engine for the role and function, or None if not found.
      :rtype: Optional[Any]


      .. autolink-examples:: get_engine_for_player
         :collapse:


   .. py:method:: get_player_role(state: haive.games.framework.multi_player.state.MultiPlayerGameState, player_id: str) -> str

      Get the role of a player, handling case sensitivity.

      This method attempts to find the player's role while handling different
      case variations of player IDs and special roles like 'narrator'.

      :param state: Current game state.
      :type state: MultiPlayerGameState
      :param player_id: ID of the player to look up.
      :type player_id: str

      :returns: Role of the player, defaulting to "VILLAGER" if not found.
      :rtype: str

      .. rubric:: Example

      >>> state = MafiaGameState(roles={"player1": "MAFIA", "narrator": "NARRATOR"})
      >>> agent.get_player_role(state, "Player1")  # Case-insensitive
      'MAFIA'
      >>> agent.get_player_role(state, "narrator")
      'NARRATOR'


      .. autolink-examples:: get_player_role
         :collapse:


   .. py:method:: handle_end_game(state: T) -> dict[str, Any]

      Handle the end of the game.

      :param state: Current game state.
      :type state: T

      :returns: Final game state.
      :rtype: Dict[str, Any]


      .. autolink-examples:: handle_end_game
         :collapse:


   .. py:method:: handle_narrator_turn(state: haive.games.framework.multi_player.state.MultiPlayerGameState) -> dict[str, Any]

      Handle the narrator's turn in the game.

      This method manages the narrator's actions, including:
      - Getting the appropriate narrator engine
      - Preparing narrator context
      - Processing narrator decisions
      - Applying narrator actions to the game state

      :param state: Current game state.
      :type state: MultiPlayerGameState

      :returns: Updated game state after narrator's action.
      :rtype: Dict[str, Any]

      .. rubric:: Example

      >>> state = MafiaGameState(phase="NIGHT")
      >>> # Narrator processes night actions
      >>> new_state = agent.handle_narrator_turn(state)
      >>> new_state["phase"]  # Narrator may have changed phase
      'DAY'

      .. rubric:: Notes

      - Handles case sensitivity issues with narrator role
      - Provides error handling for missing narrator engine
      - Converts state between dict and model forms as needed


      .. autolink-examples:: handle_narrator_turn
         :collapse:


   .. py:method:: handle_phase_transition(state: T) -> dict[str, Any]

      Handle transition between game phases.

      :param state: Current game state.
      :type state: T

      :returns: Updated game state in the new phase.
      :rtype: Dict[str, Any]


      .. autolink-examples:: handle_phase_transition
         :collapse:


   .. py:method:: handle_player_turn(state: T) -> dict[str, Any]

      Handle a player's turn.

      This method:
      1. Gets the current player and their role
      2. Retrieves the appropriate move engine
      3. Filters state information for the player
      4. Gets and applies the player's move
      5. Checks game status after the move

      :param state: Current game state.
      :type state: T

      :returns: Updated game state after the player's move.
      :rtype: Dict[str, Any]


      .. autolink-examples:: handle_player_turn
         :collapse:


   .. py:method:: handle_setup_phase(state: T) -> dict[str, Any]

      Handle the setup phase of the game.

      :param state: Current game state.
      :type state: T

      :returns: Updated game state after setup.
      :rtype: Dict[str, Any]


      .. autolink-examples:: handle_setup_phase
         :collapse:


   .. py:method:: initialize_game(state: pydantic.BaseModel) -> dict[str, Any]

      Initialize the game state.

      :param state: Initial state data or empty state.
      :type state: BaseModel

      :returns: Initialized game state.
      :rtype: Dict[str, Any]

      :raises ValueError: If state manager is not set.


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: prepare_move_context(state: T, player_id: str) -> dict[str, Any]
      :abstractmethod:


      Prepare context for move generation.

      :param state: Current game state.
      :type state: T
      :param player_id: ID of the player.
      :type player_id: str

      :returns: Context for move generation.
      :rtype: Dict[str, Any]

      :raises NotImplementedError: Must be implemented by subclass.


      .. autolink-examples:: prepare_move_context
         :collapse:


   .. py:method:: prepare_narrator_context(state: haive.games.framework.multi_player.state.MultiPlayerGameState) -> dict[str, Any]
      :abstractmethod:


      Prepare context for narrator's decision making.

      This method should be implemented by game-specific agents to provide
      the narrator with appropriate context for the current game state.

      :param state: Current game state.
      :type state: MultiPlayerGameState

      :returns: Context for narrator's decision making.
      :rtype: Dict[str, Any]

      :raises NotImplementedError: Must be implemented by subclass.

      .. rubric:: Example

      >>> def prepare_narrator_context(self, state):
      ...     return {
      ...         "phase": state.game_phase,
      ...         "alive_players": [p for p in state.players if p.is_alive],
      ...         "recent_actions": state.action_history[-5:]
      ...     }


      .. autolink-examples:: prepare_narrator_context
         :collapse:


   .. py:method:: setup_workflow()

      Setup the standard game workflow with phases.

      This method creates a workflow graph with the following structure:
          1. Game initialization
          2. Setup phase
          3. Player turns
          4. Phase transitions
          5. Game end

      The workflow supports conditional transitions based on game state
      and can be overridden for custom game flows.



      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: should_continue_after_phase_transition(state: T) -> bool

      Determine if we should continue after a phase transition.

      :param state: Current game state.
      :type state: T

      :returns: True if game should continue.
      :rtype: bool


      .. autolink-examples:: should_continue_after_phase_transition
         :collapse:


   .. py:method:: should_continue_to_main_phase(state: T) -> bool

      Determine if we should continue to the main phase.

      :param state: Current game state.
      :type state: T

      :returns: True if game should continue to main phase.
      :rtype: bool


      .. autolink-examples:: should_continue_to_main_phase
         :collapse:


   .. py:method:: should_transition_phase(state: T) -> bool

      Determine if we should transition to a new phase.

      :param state: Current game state.
      :type state: T

      :returns: True if phase transition should occur.
      :rtype: bool


      .. autolink-examples:: should_transition_phase
         :collapse:


   .. py:method:: visualize_state(state: dict[str, Any]) -> None
      :abstractmethod:


      Visualize the current game state.

      :param state: Current game state.
      :type state: Dict[str, Any]

      :raises NotImplementedError: Must be implemented by subclass.


      .. autolink-examples:: visualize_state
         :collapse:


.. py:data:: T

