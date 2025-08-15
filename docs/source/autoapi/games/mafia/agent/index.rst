games.mafia.agent
=================

.. py:module:: games.mafia.agent

.. autoapi-nested-parse::

   Mafia game agent implementation.

   This module provides the core agent implementation for the Mafia game,
   handling:
       - Game initialization and setup
       - Player turn management
       - Move generation and validation
       - Game state visualization
       - Role-specific behavior

   The agent uses LLMs to generate player decisions and narrator actions,
   creating an engaging and strategic game experience.

   .. rubric:: Example

   >>> from mafia.agent import MafiaAgent
   >>> from mafia.config import MafiaAgentConfig
   >>>
   >>> # Create and initialize agent
   >>> config = MafiaAgentConfig.default_config(player_count=7)
   >>> agent = MafiaAgent(config)
   >>>
   >>> # Run the game
   >>> for state in agent.app.stream(initial_state):
   ...     agent.visualize_state(state)


   .. autolink-examples:: games.mafia.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   games.mafia.agent.logger


Classes
-------

.. autoapisummary::

   games.mafia.agent.MafiaAgent


Module Contents
---------------

.. py:class:: MafiaAgent(config: haive.games.mafia.config.MafiaAgentConfig)

   Bases: :py:obj:`haive.games.framework.multi_player.agent.MultiPlayerGameAgent`\ [\ :py:obj:`haive.games.mafia.config.MafiaAgentConfig`\ ]


   Agent for playing Mafia.

   This class implements the core game logic for Mafia, managing player
   turns, move generation, and game progression.

   The agent handles:
       - Role assignment and management
       - Turn sequencing and validation
       - LLM-based decision making
       - Game state visualization
       - Win condition checking

   .. attribute:: state_manager

      Manager for game state

      :type: MafiaStateManager

   .. attribute:: role_enum_mapping

      Role to engine mapping

      :type: Dict[PlayerRole, str]

   .. attribute:: role_mapping

      Engine to role mapping

      :type: Dict[str, PlayerRole]

   .. rubric:: Example

   >>> config = MafiaAgentConfig.default_config(player_count=7)
   >>> agent = MafiaAgent(config)
   >>> initial_state = MafiaStateManager.initialize(
   ...     ["Player_1", "Player_2", "Narrator"]
   ... )
   >>> for state in agent.app.stream(initial_state):
   ...     agent.visualize_state(state)

   Initialize the Mafia agent.

   :param config: Configuration for the agent
   :type config: MafiaAgentConfig

   .. rubric:: Example

   >>> config = MafiaAgentConfig.default_config(player_count=7)
   >>> agent = MafiaAgent(config)


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MafiaAgent
      :collapse:

   .. py:method:: determine_next_step_after_player_turn(state: haive.games.mafia.state.MafiaGameState) -> str

      Determine what to do after a player's turn.

      This method decides the next game action based on:
          - Current game phase
          - Completed actions
          - Game end conditions
          - Maximum day limit

      :param state: Current game state
      :type state: MafiaGameState

      :returns: Next action ("end_game", "phase_transition", or "next_player")
      :rtype: str

      .. rubric:: Example

      >>> next_step = agent.determine_next_step_after_player_turn(state)
      >>> print(next_step)  # Shows what happens next


      .. autolink-examples:: determine_next_step_after_player_turn
         :collapse:


   .. py:method:: extract_move(response: str, player_id: str) -> haive.games.mafia.models.MafiaAction | haive.games.mafia.models.NarratorAction

      Extract move from engine response.

      This method processes the LLM response into a valid game action,
      handling:
          - Response validation
          - Action type conversion
          - Default action generation
          - Error handling

      :param response: Raw response from the LLM
      :param player_id: ID of the player making the move
      :type player_id: str

      :returns: Validated game action
      :rtype: Union[MafiaAction, NarratorAction]

      .. rubric:: Example

      >>> response = engine.invoke(context)
      >>> move = agent.extract_move(response, "Player_1")
      >>> print(move.action_type)  # Shows the action type


      .. autolink-examples:: extract_move
         :collapse:


   .. py:method:: get_engine_for_player(role: haive.games.mafia.models.PlayerRole | str, function: str) -> Any | None

      Get the appropriate engine for a player based on role and function.

      :param role: Player's role or role string
      :type role: Union[PlayerRole, str]
      :param function: Function type (e.g., "player")
      :type function: str

      :returns: Engine configuration if found, None otherwise
      :rtype: Optional[Any]

      .. rubric:: Example

      >>> engine = agent.get_engine_for_player(
      ...     PlayerRole.MAFIA, "player"
      ... )
      >>> print(engine.name)  # Shows "mafia_player"


      .. autolink-examples:: get_engine_for_player
         :collapse:


   .. py:method:: get_player_role(state: haive.games.mafia.state.MafiaGameState, player_id: str) -> haive.games.mafia.models.PlayerRole

      Get the role of a player.

      :param state: Current game state
      :type state: MafiaGameState
      :param player_id: ID of the player to check
      :type player_id: str

      :returns: The player's role
      :rtype: PlayerRole

      :raises Exception: If player not found in state

      .. rubric:: Example

      >>> role = agent.get_player_role(state, "Player_1")
      >>> print(role)  # Shows PlayerRole.VILLAGER


      .. autolink-examples:: get_player_role
         :collapse:


   .. py:method:: handle_narrator_turn(state: haive.games.mafia.state.MafiaGameState) -> dict[str, Any]

      Handle the narrator's turn.

      This method manages narrator actions, including:
          - Phase transitions
          - Night action resolution
          - Public announcements
          - Game state updates

      :param state: Current game state
      :type state: MafiaGameState

      :returns: Updated game state after narrator action
      :rtype: Dict[str, Any]

      .. rubric:: Example

      >>> new_state = agent.handle_narrator_turn(state)
      >>> print(new_state["public_announcements"][-1])


      .. autolink-examples:: handle_narrator_turn
         :collapse:


   .. py:method:: handle_player_turn(state: haive.games.mafia.state.MafiaGameState) -> dict[str, Any]

      Handle a player's turn with special Mafia logic.

      This method manages a player's turn, including:
          - Role-specific behavior
          - Move generation and validation
          - State updates
          - Error handling

      :param state: Current game state
      :type state: MafiaGameState

      :returns: Updated game state after the turn
      :rtype: Dict[str, Any]

      .. rubric:: Example

      >>> new_state = agent.handle_player_turn(state)
      >>> print(new_state["game_phase"])  # Shows current phase


      .. autolink-examples:: handle_player_turn
         :collapse:


   .. py:method:: prepare_move_context(state: haive.games.mafia.state.MafiaGameState, player_id: str) -> dict[str, Any]

      Prepare context for move generation.

      This method gathers all relevant information for a player's move,
      including:
          - Game state information
          - Player-specific knowledge
          - Legal moves
          - Recent history

      :param state: Current game state
      :type state: MafiaGameState
      :param player_id: ID of the player making the move
      :type player_id: str

      :returns: Context for move generation
      :rtype: Dict[str, Any]

      .. rubric:: Example

      >>> context = agent.prepare_move_context(state, "Player_1")
      >>> print(context["phase"])  # Shows current game phase


      .. autolink-examples:: prepare_move_context
         :collapse:


   .. py:method:: prepare_narrator_context(state: haive.games.mafia.state.MafiaGameState) -> dict[str, Any]

      Prepare context for narrator actions.

      This method gathers all information needed for narrator decisions,
      including:
          - Complete game state
          - Player summaries
          - Phase-specific information
          - Action histories

      :param state: Current game state
      :type state: MafiaGameState

      :returns: Context for narrator decisions
      :rtype: Dict[str, Any]

      .. rubric:: Example

      >>> context = agent.prepare_narrator_context(state)
      >>> print(context["phase"])  # Shows current game phase


      .. autolink-examples:: prepare_narrator_context
         :collapse:


   .. py:method:: state_to_dict(state: haive.games.mafia.state.MafiaGameState) -> dict[str, Any]

      Convert state to dictionary consistently.

      This method handles various state formats and ensures consistent
      dictionary conversion for the game graph.

      :param state: State to convert
      :type state: MafiaGameState

      :returns: Dictionary representation of the state
      :rtype: Dict[str, Any]

      .. rubric:: Example

      >>> state_dict = agent.state_to_dict(state)
      >>> print(state_dict["game_phase"])


      .. autolink-examples:: state_to_dict
         :collapse:


   .. py:method:: visualize_state(state_obj, debug: bool = False)

      Visualize the current game state.

      This method creates a human-readable display of:
          - Game phase and status
          - Player information
          - Recent announcements
          - Game statistics
          - Voting results (if applicable)

      :param state_obj: Game state (dict, MafiaGameState, or agent)
      :param debug: Show debug information. Defaults to False.
      :type debug: bool, optional

      .. rubric:: Example

      >>> agent.visualize_state(state, debug=True)


      .. autolink-examples:: visualize_state
         :collapse:


   .. py:attribute:: role_enum_mapping


   .. py:attribute:: role_mapping


   .. py:attribute:: state_manager


.. py:data:: logger

