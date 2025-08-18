games.hold_em.game_agent
========================

.. py:module:: games.hold_em.game_agent

Texas Hold'em Game Agent module - Main game coordinator and manager.

This module implements the core game management system for Texas Hold'em poker,
coordinating the game flow, player interactions, betting rounds, and showdowns.
It serves as the central orchestrator that manages the complete lifecycle of a
poker game from setup to completion.

Key features:
    - Complete poker game flow management with LangGraph
    - Betting round coordination and hand progression
    - Player action validation and processing
    - Pot management and chip tracking
    - Showdown evaluation and winner determination
    - Game state persistence and history tracking

The game agent creates and manages subgraph agents for each player, allowing them
to make independent decisions within the overall game context. It handles all
aspects of the game rules, ensuring proper sequencing of rounds and actions.

.. rubric:: Example

>>> from haive.games.hold_em.game_agent import HoldemGameAgent
>>> from haive.games.hold_em.config import create_default_holdem_config
>>>
>>> # Create a game configuration
>>> config = create_default_holdem_config(num_players=4)
>>>
>>> # Initialize the game agent
>>> agent = HoldemGameAgent(config)
>>>
>>> # Run the game
>>> result = agent.app.invoke({}, debug=True)

Implementation details:
    - Enhanced player ID handling and validation
    - Robust error checking and recovery
    - Comprehensive logging for debugging
    - Fixed player lookup and identification



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 classes</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Texas Hold'em Game Agent module - Main game coordinator and manager.

   This module implements the core game management system for Texas Hold'em poker,
   coordinating the game flow, player interactions, betting rounds, and showdowns.
   It serves as the central orchestrator that manages the complete lifecycle of a
   poker game from setup to completion.

   Key features:
       - Complete poker game flow management with LangGraph
       - Betting round coordination and hand progression
       - Player action validation and processing
       - Pot management and chip tracking
       - Showdown evaluation and winner determination
       - Game state persistence and history tracking

   The game agent creates and manages subgraph agents for each player, allowing them
   to make independent decisions within the overall game context. It handles all
   aspects of the game rules, ensuring proper sequencing of rounds and actions.

   .. rubric:: Example

   >>> from haive.games.hold_em.game_agent import HoldemGameAgent
   >>> from haive.games.hold_em.config import create_default_holdem_config
   >>>
   >>> # Create a game configuration
   >>> config = create_default_holdem_config(num_players=4)
   >>>
   >>> # Initialize the game agent
   >>> agent = HoldemGameAgent(config)
   >>>
   >>> # Run the game
   >>> result = agent.app.invoke({}, debug=True)

   Implementation details:
       - Enhanced player ID handling and validation
       - Robust error checking and recovery
       - Comprehensive logging for debugging
       - Fixed player lookup and identification



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.hold_em.game_agent.logger

            
            

.. admonition:: Classes (2)
   :class: note

   .. autoapisummary::

      games.hold_em.game_agent.HoldemGameAgent
      games.hold_em.game_agent.HoldemGameAgentConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HoldemGameAgent(config: HoldemGameAgentConfig)

            Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`HoldemGameAgentConfig`\ ]


            Main Texas Hold'em game agent that coordinates the complete poker game.

            This agent manages the entire lifecycle of a Texas Hold'em poker game,
            implementing all game rules, betting rounds, player actions, and hand evaluations.
            It creates and coordinates player subgraphs, manages the central game state,
            and ensures proper game flow from initial setup through the final showdown.

            The game progresses through the standard Texas Hold'em phases:
            1. Setup hand and post blinds
            2. Deal hole cards and run preflop betting
            3. Deal flop (3 community cards) and run flop betting
            4. Deal turn (4th community card) and run turn betting
            5. Deal river (5th community card) and run river betting
            6. Showdown evaluation and pot distribution
            7. Proceed to next hand or end game

            Between betting rounds, the agent routes the game flow based on the current
            state, handling special cases like all players folded or all-in situations.

            This version includes enhanced debugging capabilities, robust player ID handling,
            and comprehensive error recovery mechanisms.


            Initialize the agent with its configuration.

            :param config: Agent configuration
            :param verbose: Whether to enable verbose logging
            :param rich_logging: Whether to use rich UI for logging and debugging


            .. py:method:: _advance_or_complete_betting(state: haive.games.hold_em.state.HoldemState) -> langgraph.types.Command

               Advance to next player or complete betting round.



            .. py:method:: _advance_or_complete_betting_with_action(state: haive.games.hold_em.state.HoldemState, action_record: dict[str, Any]) -> langgraph.types.Command

               Advance betting after applying an action.



            .. py:method:: _apply_bet_raise(player: haive.games.hold_em.state.PlayerState, state: haive.games.hold_em.state.HoldemState, bet_amount: int)

               Apply a bet or raise action.



            .. py:method:: _apply_call(player: haive.games.hold_em.state.PlayerState, state: haive.games.hold_em.state.HoldemState, call_amount: int)

               Apply a call action.



            .. py:method:: _apply_player_action(state: haive.games.hold_em.state.HoldemState, player: haive.games.hold_em.state.PlayerState, decision: dict[str, Any]) -> langgraph.types.Command

               Apply a player's action to the game state and update chips and pot.

               This method processes a player's poker decision, updating the game state
               according to the chosen action (fold, check, call, bet, raise, or all-in).
               It modifies player chips, current bets, pot size, and player status as needed.

               The method also handles edge cases like:
               - Forcing call when player tries to check but there's a bet
               - Forcing fold when player can't meet the minimum call amount
               - Converting raise to all-in when player has insufficient chips
               - Treating unknown actions as fold for safety

               :param state: The current game state
               :type state: HoldemState
               :param player: The player making the action
               :type player: PlayerState
               :param decision: The decision from the player agent
               :type decision: Dict[str, Any]

               :returns: Game state update with the action applied and next player set
               :rtype: Command

               :raises RuntimeError: If action application fails due to errors



            .. py:method:: _create_deck() -> list[str]

               Create a standard 52-card deck.



            .. py:method:: _deal_community_cards(state: haive.games.hold_em.state.HoldemState, num_cards: int, phase: haive.games.hold_em.state.GamePhase, next_node: str) -> langgraph.types.Command

               Deal community cards to the board, with burn card.

               This helper method handles dealing community cards for the flop, turn, or river.
               It burns one card first (discards it face down), then deals the specified number
               of cards to the board. It also resets betting for the new round and determines
               the first player to act.

               :param state: The current game state
               :type state: HoldemState
               :param num_cards: Number of cards to deal (3 for flop, 1 for turn/river)
               :type num_cards: int
               :param phase: The new game phase to set
               :type phase: GamePhase
               :param next_node: The next node to transition to
               :type next_node: str

               :returns:

                         State update with new community cards, game phase, and
                                  reset betting information
               :rtype: Command

               :raises RuntimeError: If card dealing fails



            .. py:method:: _evaluate_hand_simple(hole_cards: list[str], community_cards: list[str]) -> float

               Simple hand evaluation method (placeholder for production evaluator).

               This is a simplified poker hand evaluator that assigns a score based
               primarily on high card values. In a production system, this would be
               replaced with a proper poker hand evaluator that correctly ranks hands
               according to standard poker rules.

               :param hole_cards: Player's private hole cards
               :type hole_cards: List[str]
               :param community_cards: Shared community cards
               :type community_cards: List[str]

               :returns: A score representing hand strength (higher is better)
               :rtype: float



            .. py:method:: _handle_betting_round(state: haive.games.hold_em.state.HoldemState, round_name: str) -> langgraph.types.Command

               Handle a betting round.



            .. py:method:: _save_debug_logs()

               Save debug logs to files.



            .. py:method:: _set_player_positions(state: haive.games.hold_em.state.HoldemState, dealer_pos: int)

               Set player positions for the hand.



            .. py:method:: award_pot(state: haive.games.hold_em.state.HoldemState) -> langgraph.types.Command[Literal['check_game_end']]

               Award the pot to the winner and record hand history.

               This node adds the pot to the winner's chip stack and records the completed
               hand in the game history. If no winner is explicitly determined (e.g., from
               showdown), it finds the last remaining player as the winner.

               The hand history is recorded with details about the hand number, winner,
               pot size, community cards, and betting actions for later analysis.

               :param state: The current game state
               :type state: HoldemState

               :returns:

                         State update with winner's updated chips and hand history,
                                  and incremented hand number
               :rtype: Command

               :raises RuntimeError: If pot awarding fails



            .. py:method:: check_game_end(state: haive.games.hold_em.state.HoldemState) -> langgraph.types.Command

               Check if the game should end.



            .. py:method:: deal_flop(state: haive.games.hold_em.state.HoldemState) -> langgraph.types.Command[Literal['flop_betting']]

               Deal the flop (3 community cards).



            .. py:method:: deal_hole_cards(state: haive.games.hold_em.state.HoldemState) -> langgraph.types.Command[Literal['preflop_betting']]

               Deal two hole cards to each active player in the game.

               This node deals two private cards to each active player from the deck,
               and determines the first player to act in the preflop betting round.
               For standard games, the first player to act is the one after the big blind.

               :param state: The current game state
               :type state: HoldemState

               :returns:

                         State update with updated deck, player hole cards, and
                                  the index of the first player to act
               :rtype: Command

               :raises RuntimeError: If there aren't enough cards or dealing fails



            .. py:method:: deal_river(state: haive.games.hold_em.state.HoldemState) -> langgraph.types.Command[Literal['river_betting']]

               Deal the river (5th community card).



            .. py:method:: deal_turn(state: haive.games.hold_em.state.HoldemState) -> langgraph.types.Command[Literal['turn_betting']]

               Deal the turn (4th community card).



            .. py:method:: flop_betting(state: haive.games.hold_em.state.HoldemState) -> langgraph.types.Command

               Handle flop betting round.



            .. py:method:: get_player_decision(state: haive.games.hold_em.state.HoldemState) -> langgraph.types.Command

               Get decision from current player using their subgraph agent.

               This is a critical node that invokes the current player's subgraph agent
               to get their poker decision (fold, check, call, bet, raise, or all-in).
               The method performs extensive validation of player IDs and provides detailed
               debugging information to track the decision process.

               The workflow:
               1. Identifies the current player and validates their player_id
               2. Prepares input for the player's subgraph agent
               3. Invokes the player agent with the game state and player ID
               4. Receives the decision and applies it to the game state

               Enhanced debug features include:
               - Comprehensive player ID validation and repair
               - Detailed logging of decision context and results
               - Error tracking with comprehensive context

               :param state: The current game state
               :type state: HoldemState

               :returns: State update based on the player's action
               :rtype: Command

               :raises RuntimeError: If player lookup fails or decision-making fails



            .. py:method:: log_agent_config(player_config: haive.games.hold_em.player_agent.HoldemPlayerAgentConfig)

               Log detailed player agent configuration for debugging purposes.

               This method creates a structured representation of a player agent's configuration
               and logs it for debugging. It includes information about the player's style,
               risk tolerance, engines, and engine details such as models and output formats.

               :param player_config: The player configuration to log
               :type player_config: HoldemPlayerAgentConfig

               :returns: The configuration is logged to the logger
               :rtype: None



            .. py:method:: post_blinds(state: haive.games.hold_em.state.HoldemState) -> langgraph.types.Command[Literal['deal_hole_cards']]

               Post small and big blinds to start the betting.

               This node identifies the small blind and big blind players based on
               their positions, collects the blind amounts from them, and adds these
               amounts to the pot. If a player doesn't have enough chips for their blind,
               they go all-in with their remaining chips.

               :param state: The current game state
               :type state: HoldemState

               :returns: State update with updated pot, player chips, and actions
               :rtype: Command

               :raises RuntimeError: If blind players cannot be found or posting fails



            .. py:method:: preflop_betting(state: haive.games.hold_em.state.HoldemState) -> langgraph.types.Command

               Handle preflop betting round.



            .. py:method:: river_betting(state: haive.games.hold_em.state.HoldemState) -> langgraph.types.Command

               Handle river betting round.



            .. py:method:: route_after_betting(state: haive.games.hold_em.state.HoldemState) -> str

               Route game flow after a betting round completes.

               This conditional routing method determines where the game should proceed
               after a betting round. The routing logic considers:

               1. If only one player remains (others folded) -> award_pot
               2. If betting is not complete -> player_decision (continue betting)
               3. If only one active player (rest all-in) -> showdown
               4. Otherwise, proceed to next game phase based on current phase:
                  - Preflop -> deal_flop
                  - Flop -> deal_turn
                  - Turn -> deal_river
                  - River -> showdown

               :param state: The current game state
               :type state: HoldemState

               :returns: The name of the next node to route to
               :rtype: str



            .. py:method:: route_game_continuation(state: haive.games.hold_em.state.HoldemState) -> str

               Route game continuation.



            .. py:method:: setup_hand(state: haive.games.hold_em.state.HoldemState) -> langgraph.types.Command[Literal['post_blinds']]

               Setup a new poker hand by initializing deck and player states.

               This node initializes a new hand by creating and shuffling a deck,
               resetting player states, advancing the dealer position, and setting up
               player positions around the table. It prepares all the necessary state
               for starting a new hand of poker.

               :param state: The current game state
               :type state: HoldemState

               :returns: State update with new deck, reset community cards, pot, etc.
               :rtype: Command

               :raises RuntimeError: If hand setup fails due to errors



            .. py:method:: setup_player_agents()

               Set up player subgraph agents with detailed logging.

               This method initializes a HoldemPlayerAgent instance for each player in the game
               based on the player configurations. It creates the independent decision-making
               subgraphs that will be invoked during betting rounds. The method includes
               comprehensive error handling and logging to ensure all agents are properly created.

               The player agents are stored in a dictionary keyed by player name for later
               retrieval during decision-making phases.

               :raises RuntimeError: If any required player agent cannot be created successfully



            .. py:method:: setup_workflow()

               Setup the main game workflow graph with all nodes and transitions.

               This method configures the complete LangGraph workflow for the poker game,
               defining all game phases, decision points, and conditional routing logic.
               It establishes the core game flow including:

               1. Game setup nodes: setup_hand, post_blinds, deal_hole_cards
               2. Betting round nodes: preflop_betting, flop_betting, turn_betting, river_betting
               3. Card dealing nodes: deal_flop, deal_turn, deal_river
               4. Game conclusion nodes: showdown, award_pot, check_game_end
               5. Player decision node: Invokes player subgraphs for decisions

               The graph includes conditional edges to route game flow based on the current
               state, such as proceeding to the next betting round or directly to showdown
               when appropriate. This creates a complete state machine for poker game flow.




            .. py:method:: showdown(state: haive.games.hold_em.state.HoldemState) -> langgraph.types.Command[Literal['award_pot']]

               Handle showdown - evaluate player hands and determine the winner.

               This node evaluates the hand of each player still in the game (not folded)
               and determines the winner based on hand strength. In case only one player
               remains, that player automatically wins. Otherwise, all qualifying hands
               are compared to find the strongest.

               The current implementation uses a simplified hand evaluation algorithm,
               which would be replaced by a more sophisticated poker hand evaluator
               in a production version.

               :param state: The current game state
               :type state: HoldemState

               :returns: State update with the winner's player ID
               :rtype: Command

               :raises RuntimeError: If showdown evaluation fails



            .. py:method:: turn_betting(state: haive.games.hold_em.state.HoldemState) -> langgraph.types.Command

               Handle turn betting round.



            .. py:attribute:: decision_log
               :value: []



            .. py:attribute:: error_log
               :value: []



            .. py:attribute:: invocation_log
               :value: []



            .. py:attribute:: player_agents



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HoldemGameAgentConfig

            Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


            Configuration for the main Hold'em game agent.

            This configuration class defines the parameters for a Texas Hold'em game, including
            the number of players, blinds, starting chips, game limits, and player agent
            configurations. It encapsulates all the settings needed to initialize and run a
            complete poker game.

            The configuration serves as the blueprint for creating a HoldemGameAgent instance
            with specific game rules and player characteristics. It can be created directly or
            through helper functions in the config module.



            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:attribute:: big_blind
               :type:  int
               :value: None



            .. py:attribute:: engines
               :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
               :value: None



            .. py:attribute:: max_hands
               :type:  int
               :value: None



            .. py:attribute:: max_players
               :type:  int
               :value: None



            .. py:attribute:: player_configs
               :type:  list[haive.games.hold_em.player_agent.HoldemPlayerAgentConfig]
               :value: None



            .. py:attribute:: small_blind
               :type:  int
               :value: None



            .. py:attribute:: starting_chips
               :type:  int
               :value: None



            .. py:attribute:: state_schema
               :type:  type
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.hold_em.game_agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

