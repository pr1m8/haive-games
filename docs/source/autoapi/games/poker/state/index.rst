games.poker.state
=================

.. py:module:: games.poker.state

.. autoapi-nested-parse::

   Texas Hold'em Poker game state management.

   This module implements the core state management for a Texas Hold'em poker game,
   including:
       - Game initialization and progression
       - Player action handling
       - Betting rounds and pot management
       - Hand evaluation and showdown logic
       - Side pot creation for all-in situations

   The state management is built on top of LangGraph for AI agent integration,
   using Pydantic models for type safety and validation.

   .. rubric:: Example

   >>> from poker.state import PokerState
   >>>
   >>> # Initialize a new game
   >>> state = PokerState()
   >>> state.initialize_game(["Alice", "Bob", "Charlie"], starting_chips=1000)
   >>> state.start_new_hand()


   .. autolink-examples:: games.poker.state
      :collapse:


Attributes
----------

.. autoapisummary::

   games.poker.state.logger


Classes
-------

.. autoapisummary::

   games.poker.state.PokerState


Module Contents
---------------

.. py:class:: PokerState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State manager for Texas Hold'em Poker game.

   Manages the complete state of a poker game, including player actions,
   game progression, betting rounds, and hand evaluation. Built on top of
   LangGraph for AI agent integration.

   .. attribute:: messages

      Message history for agent communication

      :type: List[BaseMessage]

   .. attribute:: current_step

      Current step in the game progression

      :type: int

   .. attribute:: max_steps

      Maximum allowed steps before forced game end

      :type: int

   .. attribute:: error

      Current error state, if any

      :type: Optional[str]

   .. attribute:: memory

      Persistent memory for game state

      :type: Dict[str, Any]

   .. attribute:: game

      Current game state

      :type: PokerGameState

   .. attribute:: waiting_for_player

      ID of player we're waiting for

      :type: Optional[str]

   .. attribute:: game_log

      Timestamped log of game events

      :type: List[str]

   .. attribute:: current_decision

      Last decision made

      :type: Optional[AgentDecision]

   .. rubric:: Example

   >>> state = PokerState()
   >>> state.initialize_game(["Alice", "Bob"], 1000)
   >>> state.start_new_hand()
   >>> obs = state.create_player_observation("player_0")

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PokerState
      :collapse:

   .. py:method:: _advance_to_next_player()

      Move to the next active player in the game.

      Internal helper method to advance the current player index to the
      next player who can act (active and not all-in). If no such player
      is found after a full circle, marks the round as complete.

      Side Effects:
          - Updates current_player_idx
          - May mark round as complete



      .. autolink-examples:: _advance_to_next_player
         :collapse:


   .. py:method:: _check_round_completion() -> bool

      Check if the current betting round is complete.

      Internal helper method to determine if the current betting round
      should end. A round is complete when:
          - Only one player remains active
          - All active players have bet the same amount
          - All players have acted after the last aggressor

      :returns: True if round is complete, False otherwise
      :rtype: bool

      Side Effects:
          - May mark round as complete



      .. autolink-examples:: _check_round_completion
         :collapse:


   .. py:method:: _create_side_pots_if_needed()

      Create side pots when players are all-in.

      Internal helper method to handle side pot creation when one or more
      players are all-in with different amounts. Ensures fair pot distribution
      when players can't match bets.

      Side Effects:
          - Creates new pots based on all-in amounts
          - Updates pot eligibility for each player
          - Redistributes chips between pots



      .. autolink-examples:: _create_side_pots_if_needed
         :collapse:


   .. py:method:: _evaluate_hand(cards: list[haive.games.poker.models.Card]) -> tuple[haive.games.poker.models.HandRank, list[int], str]

      Evaluate the best 5-card poker hand from given cards.

      Internal helper method to determine the best possible poker hand
      from a set of cards (hole cards + community cards). Handles all
      standard poker hand rankings and tiebreakers.

      :param cards: List of cards to evaluate (usually 7 cards)
      :type cards: List[Card]

      :returns:

                A tuple containing:
                    - HandRank: The type of hand (pair, flush, etc.)
                    - List[int]: High card values for tiebreaking
                    - str: Human-readable description of the hand
      :rtype: Tuple[HandRank, List[int], str]

      .. rubric:: Example

      >>> cards = [
      ...     Card(suit=Suit.HEARTS, value=CardValue.ACE),
      ...     Card(suit=Suit.HEARTS, value=CardValue.KING),
      ...     Card(suit=Suit.HEARTS, value=CardValue.QUEEN),
      ...     Card(suit=Suit.HEARTS, value=CardValue.JACK),
      ...     Card(suit=Suit.HEARTS, value=CardValue.TEN)
      ... ]
      >>> rank, high_cards, desc = _evaluate_hand(cards)
      >>> print(desc)  # Shows "Royal Flush"


      .. autolink-examples:: _evaluate_hand
         :collapse:


   .. py:method:: _handle_showdown()

      Handle the showdown phase of the game.

      Internal helper method to process the showdown when multiple players
      remain after all betting rounds. Includes:
          - Evaluating all active players' hands
          - Determining winners for each pot
          - Distributing chips appropriately
          - Handling split pots

      Side Effects:
          - Evaluates hands
          - Awards pots to winners
          - Updates game phase
          - Logs results



      .. autolink-examples:: _handle_showdown
         :collapse:


   .. py:method:: _handle_single_player_win()

      Handle case where only one player remains active.

      Internal helper method to process an early hand completion when all
      other players have folded. Awards all pots to the remaining player
      and ends the hand.

      Side Effects:
          - Awards pots to winner
          - Updates game phase
          - Logs result



      .. autolink-examples:: _handle_single_player_win
         :collapse:


   .. py:method:: _place_bet(player: haive.games.poker.models.Player, amount: int) -> int

      Place a bet for a player.

      Internal helper method to handle bet placement, including:
          - Updating player chips and bet amounts
          - Adding to pot
          - Checking for all-in
          - Creating side pots if needed

      :param player: Player placing the bet
      :type player: Player
      :param amount: Amount to bet
      :type amount: int

      :returns: Actual amount bet (may be less if player can't cover)
      :rtype: int

      Side Effects:
          - Updates player chips and bet amounts
          - May create side pots if player goes all-in



      .. autolink-examples:: _place_bet
         :collapse:


   .. py:method:: _player_has_acted_after_last_aggressor() -> bool

      Check if all players have acted after the last aggressive action.

      Internal helper method to determine if betting can end by checking if
      all players have had a chance to act after the last bet/raise.

      :returns: True if all players have acted, False otherwise
      :rtype: bool


      .. autolink-examples:: _player_has_acted_after_last_aggressor
         :collapse:


   .. py:method:: advance_game_phase()

      Move the game to the next phase if current phase is complete.

      Handles progression through game phases:
          1. Preflop -> Flop (deal 3 cards)
          2. Flop -> Turn (deal 1 card)
          3. Turn -> River (deal 1 card)
          4. River -> Showdown (evaluate hands)

      For each phase transition:
          - Resets betting amounts
          - Deals appropriate community cards
          - Sets first player to act
          - Updates game phase

      Side Effects:
          - Updates game phase
          - Deals community cards
          - Resets betting state
          - May end the hand



      .. autolink-examples:: advance_game_phase
         :collapse:


   .. py:method:: create_player_observation(player_id: str) -> haive.games.poker.models.PlayerObservation

      Create an observation object for a player.

      Generates a view of the game state from a specific player's perspective,
      hiding information they shouldn't have access to (e.g., other players'
      hole cards).

      :param player_id: ID of player to create observation for
      :type player_id: str

      :returns: Object containing all information visible to player
      :rtype: PlayerObservation

      :raises ValueError: If player_id is not found

      .. rubric:: Example

      >>> obs = state.create_player_observation("player_0")
      >>> print(obs.hand)  # Shows player's hole cards
      >>> print(obs.community_cards)  # Shows shared cards


      .. autolink-examples:: create_player_observation
         :collapse:


   .. py:method:: deal_community_cards(count: int = 3)

      Deal community cards to the board.

      Deals the specified number of cards from the deck to the community
      cards area. Used for flop (3 cards), turn (1 card), and river (1 card).
      Logs the dealt cards with appropriate phase name.

      :param count: Number of cards to deal. Defaults to 3 for flop.
      :type count: int, optional

      :raises Sets self.error if there aren't enough cards in the deck.:


      .. autolink-examples:: deal_community_cards
         :collapse:


   .. py:method:: deal_hands()

      Deal two cards to each active player.

      Deals hole cards to all active players with chips. Skips inactive or busted
      players. Logs an error if there aren't enough cards.



      .. autolink-examples:: deal_hands
         :collapse:


   .. py:method:: handle_player_action(player_id: str, decision: haive.games.poker.models.AgentDecision)

      Process a player's action in the game.

      Handles all possible player actions (fold, check, call, bet, raise, all-in),
      including validation, bet placement, and game state updates.

      :param player_id: ID of player taking action
      :type player_id: str
      :param decision: Player's chosen action and amount
      :type decision: AgentDecision

      Side Effects:
          - Updates player state (chips, active status)
          - Updates game state (pot, current bet, etc.)
          - Advances to next player
          - May complete betting round
          - May end hand if only one player remains

      :raises Sets self.error for invalid actions: - Player not found
          - Player not active
          - Invalid action for current state
          - Invalid bet/raise amount


      .. autolink-examples:: handle_player_action
         :collapse:


   .. py:method:: initialize_deck()

      Create and shuffle a new deck of cards.

      Creates a standard 52-card deck and performs a random shuffle. Updates the game
      state with the new deck.



      .. autolink-examples:: initialize_deck
         :collapse:


   .. py:method:: initialize_game(player_names: list[str], starting_chips: int = 1000)

      Initialize a new poker game with the given players.

      Creates a new game state with the specified players, assigning
      IDs, positions, and starting chip stacks.

      :param player_names: Names of players to add
      :type player_names: List[str]
      :param starting_chips: Initial chips per player. Defaults to 1000.
      :type starting_chips: int, optional

      .. rubric:: Example

      >>> state.initialize_game(["Alice", "Bob", "Charlie"], 2000)


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: log_event(message: str)

      Add a timestamped message to the game log.

      Records game events with timestamps for history tracking and debugging.
      Events are both added to the game_log list and sent to the logger.

      :param message: Event message to log
      :type message: str

      .. rubric:: Example

      >>> state.log_event("Alice raises to $100")
      [14:30:45] Alice raises to $100


      .. autolink-examples:: log_event
         :collapse:


   .. py:method:: post_blinds()

      Post small and big blinds.

      Forces the two players after the dealer to post the small and big
      blinds. Updates player chips, pot size, and current bet amount.
      Sets minimum raise to the big blind size.

      :raises Sets self.error if there aren't enough players or if blind:
      :raises positions can't be determined.:


      .. autolink-examples:: post_blinds
         :collapse:


   .. py:method:: start_new_hand()

      Start a new hand of poker.

      Resets all necessary state for a new hand:
          - Rotates dealer position
          - Resets player hands and bets
          - Clears community cards and pots
          - Initializes new deck and deals cards
          - Posts blinds
          - Sets first player to act (UTG)

      The game progresses through these phases:
          1. Setup (reset state)
          2. Deal hole cards
          3. Post blinds
          4. Start preflop betting



      .. autolink-examples:: start_new_hand
         :collapse:


   .. py:attribute:: current_decision
      :type:  haive.games.poker.models.AgentDecision | None
      :value: None



   .. py:attribute:: current_step
      :type:  int
      :value: 0



   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: game
      :type:  haive.games.poker.models.PokerGameState
      :value: None



   .. py:attribute:: game_log
      :type:  list[str]
      :value: None



   .. py:attribute:: max_steps
      :type:  int
      :value: 1000



   .. py:attribute:: memory
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: messages
      :type:  list[langchain_core.messages.BaseMessage]
      :value: None



   .. py:attribute:: waiting_for_player
      :type:  str | None
      :value: None



.. py:data:: logger

