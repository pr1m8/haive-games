games.monopoly.state
====================

.. py:module:: games.monopoly.state


Classes
-------

.. autoapisummary::

   games.monopoly.state.GameStatus
   games.monopoly.state.MonopolyState


Functions
---------

.. autoapisummary::

   games.monopoly.state.add_events
   games.monopoly.state.add_strings


Module Contents
---------------

.. py:class:: GameStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Enumeration of game status states.

   Defines the different states a Monopoly game can be in,
   affecting which actions are valid and how the game progresses.

   Values:
       WAITING: Game is waiting to start
       PLAYING: Game is actively in progress
       PAUSED: Game is temporarily paused
       FINISHED: Game has completed with a winner
       ABANDONED: Game was abandoned before completion


   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GameStatus
      :collapse:

   .. py:attribute:: ABANDONED
      :value: 'abandoned'



   .. py:attribute:: FINISHED
      :value: 'finished'



   .. py:attribute:: PAUSED
      :value: 'paused'



   .. py:attribute:: PLAYING
      :value: 'playing'



   .. py:attribute:: WAITING
      :value: 'waiting'



.. py:class:: MonopolyState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive state model for Monopoly gameplay with economic analysis and.
   strategic context.

   This class provides complete state management for Monopoly games, supporting
   both traditional gameplay mechanics and advanced economic simulation. The state
   system maintains game rules, property ownership, financial transactions, and
   strategic context for AI decision-making and tournament play.

   The state system supports:
   - Complete game state tracking with property ownership and development
   - Economic transaction logging with detailed financial analysis
   - Strategic analysis integration for AI decision-making capabilities
   - Multi-player state synchronization for distributed gameplay
   - Comprehensive validation and consistency checking
   - LangGraph integration with proper state reducers and command updates

   .. attribute:: players

      All players in the game with complete financial profiles.

      :type: List[Player]

   .. attribute:: properties

      All properties on the board with ownership details.

      :type: Dict[str, Property]

   .. attribute:: current_player_index

      Index of the player whose turn it currently is.

      :type: int

   .. attribute:: turn_number

      Current turn number for tracking game progression.

      :type: int

   .. attribute:: round_number

      Current round number (completed cycles through all players).

      :type: int

   .. attribute:: game_status

      Current status of the game (waiting, playing, finished, etc.).

      :type: GameStatus

   .. attribute:: last_roll

      Most recent dice roll with movement information.

      :type: Optional[DiceRoll]

   .. attribute:: doubles_rolled

      Whether doubles were rolled this turn (affects extra turns).

      :type: bool

   .. attribute:: doubles_count

      Number of consecutive doubles rolled (jail on 3).

      :type: int

   .. attribute:: chance_cards

      Shuffled deck of Chance cards.

      :type: List[str]

   .. attribute:: community_chest_cards

      Shuffled deck of Community Chest cards.

      :type: List[str]

   .. attribute:: game_events

      Complete history of all game events and transactions.

      :type: List[GameEvent]

   .. attribute:: winner

      Name of the winning player if game is complete.

      :type: Optional[str]

   .. attribute:: error_message

      Error message if any operation failed.

      :type: Optional[str]

   .. attribute:: messages

      Optional conversation messages for LLM compatibility.

      :type: Optional[List[BaseMessage]]

   .. attribute:: houses_remaining

      Number of houses available for purchase (scarcity rule).

      :type: int

   .. attribute:: hotels_remaining

      Number of hotels available for purchase (scarcity rule).

      :type: int

   .. attribute:: free_parking_money

      Money accumulated on Free Parking (house rule).

      :type: int

   .. attribute:: jail_get_out_free_cards

      Get Out of Jail Free cards held by players.

      :type: Dict[str, int]

   .. rubric:: Examples

   Creating a new game state::\n

       state = MonopolyState.initialize_game(
           player_names=["Alice", "Bob", "Charlie"],
           starting_money=1500
       )
       assert len(state.players) == 3
       assert state.current_player_index == 0
       assert state.turn_number == 1

   Managing property transactions::\n

       # Purchase property
       state = state.purchase_property("Alice", "Boardwalk", 400)
       alice = state.get_player_by_name("Alice")
       assert "Boardwalk" in alice.properties
       assert alice.money == 1100  # 1500 - 400

       # Build development
       state = state.build_houses("Alice", "Boardwalk", 2)
       boardwalk = state.get_property_by_name("Boardwalk")
       assert boardwalk.houses == 2

       # Calculate rent with development
       rent = state.get_rent_amount("Boardwalk", dice_roll=7)
       assert rent > 50  # Base rent plus houses

   Tracking game progression::\n

       # Move to next player
       initial_player = state.current_player.name
       state.next_player()
       assert state.current_player.name != initial_player

       # Add game events
       event = GameEvent(
           type=PlayerActionType.BUY_PROPERTY,
           player="Alice",
           details="Purchased Boardwalk for $400",
           turn_number=state.turn_number
       )
       state.add_event(event)
       assert len(state.game_events) == 1

       # Check game completion
       if state.is_game_over():
           winner = state.winner
           final_rankings = state.player_rankings

   Economic analysis and strategic context::\n

       # Financial metrics
       metrics = state.economic_metrics
       assert "total_money_in_game" in metrics
       assert "average_player_wealth" in metrics

       # Property distribution analysis
       distribution = state.property_distribution
       assert "monopolies" in distribution
       assert "undeveloped_properties" in distribution

       # Player rankings by net worth
       rankings = state.player_rankings
       assert len(rankings) == len(state.players)

       # Strategic position analysis
       for player in state.players:
           position = state.get_player_strategic_position(player.name)
           assert "net_worth" in position
           assert "monopolies_owned" in position
           assert "development_potential" in position

   Advanced state operations::\n

       # Validate state consistency
       issues = state.validate_state_consistency()
       assert len(issues) == 0  # No validation errors

       # Convert for distributed gameplay
       state_dict = state.to_dict()
       restored_state = MonopolyState.from_dict(state_dict)
       assert restored_state.turn_number == state.turn_number

       # Create secure public view for AI
       public_view = state.get_public_view_for_player("Alice")
       assert "current_player" in public_view
       assert "properties" in public_view
       # Opponent private information is hidden

   .. note::

      The state uses Pydantic for validation and supports both JSON serialization
      and integration with LangGraph for distributed tournament systems.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MonopolyState
      :collapse:

   .. py:method:: _calculate_strategic_score(player_name: str) -> float

      Calculate strategic score for a player.

      :param player_name: Name of the player.
      :type player_name: str

      :returns: Strategic score based on net worth, monopolies, and position.
      :rtype: float


      .. autolink-examples:: _calculate_strategic_score
         :collapse:


   .. py:method:: _get_player_monopolies(player_name: str) -> list[str]

      Get list of color groups where player has monopoly.

      :param player_name: Name of the player to check.
      :type player_name: str

      :returns: List of color groups where player owns all properties.
      :rtype: List[str]


      .. autolink-examples:: _get_player_monopolies
         :collapse:


   .. py:method:: add_event(event: haive.games.monopoly.models.GameEvent) -> None

      Add a single event to the game history.


      .. autolink-examples:: add_event
         :collapse:


   .. py:method:: add_events_and_update(events: list[haive.games.monopoly.models.GameEvent], **updates) -> dict[str, Any]

      Add events and other updates for Command usage.


      .. autolink-examples:: add_events_and_update
         :collapse:


   .. py:method:: from_dict(data: dict[str, Any]) -> MonopolyState
      :classmethod:


      Create state from dictionary with proper nested object handling.


      .. autolink-examples:: from_dict
         :collapse:


   .. py:method:: from_state_object(state: Union[MonopolyState, pydantic.BaseModel, dict[str, Any]]) -> MonopolyState
      :classmethod:


      Convert any state object to MonopolyState.

      This is the primary method for ensuring consistency across all state handling.



      .. autolink-examples:: from_state_object
         :collapse:


   .. py:method:: get_player_by_name(name: str) -> haive.games.monopoly.models.Player | None

      Get player by name.


      .. autolink-examples:: get_player_by_name
         :collapse:


   .. py:method:: get_player_strategic_position(player_name: str) -> dict[str, Any]

      Get comprehensive strategic position analysis for a player.

      :param player_name: Name of the player to analyze.
      :type player_name: str

      :returns: Strategic position analysis including strengths and weaknesses.
      :rtype: Dict[str, Any]


      .. autolink-examples:: get_player_strategic_position
         :collapse:


   .. py:method:: get_properties_owned_by_player(player_name: str) -> list[haive.games.monopoly.models.Property]

      Get all properties owned by a player.


      .. autolink-examples:: get_properties_owned_by_player
         :collapse:


   .. py:method:: get_property_by_name(name: str) -> haive.games.monopoly.models.Property | None

      Get property by name.


      .. autolink-examples:: get_property_by_name
         :collapse:


   .. py:method:: get_property_by_position(position: int) -> haive.games.monopoly.models.Property | None

      Get property at a specific board position.


      .. autolink-examples:: get_property_by_position
         :collapse:


   .. py:method:: get_public_view_for_player(player_name: str) -> dict[str, Any]

      Generate a secure public view of the game state for a specific player.

      This method creates a view that contains all information a player should
      legitimately know while hiding private information from other players.

      :param player_name: Name of the player requesting the view.
      :type player_name: str

      :returns: Public state information for the player.
      :rtype: Dict[str, Any]


      .. autolink-examples:: get_public_view_for_player
         :collapse:


   .. py:method:: get_recent_events(count: int = 10) -> list[haive.games.monopoly.models.GameEvent]

      Get the most recent game events.


      .. autolink-examples:: get_recent_events
         :collapse:


   .. py:method:: get_rent_amount(property_name: str, dice_roll: int = 0) -> int

      Calculate rent amount for a property.


      .. autolink-examples:: get_rent_amount
         :collapse:


   .. py:method:: next_player() -> None

      Move to the next player's turn with proper bounds checking.


      .. autolink-examples:: next_player
         :collapse:


   .. py:method:: player_owns_monopoly(player_name: str, color: str) -> bool

      Check if player owns all properties of a color group.


      .. autolink-examples:: player_owns_monopoly
         :collapse:


   .. py:method:: to_dict() -> dict[str, Any]

      Convert state to dictionary for serialization.


      .. autolink-examples:: to_dict
         :collapse:


   .. py:method:: update_player(player_index: int, player: haive.games.monopoly.models.Player) -> MonopolyState

      Update a player and return a new state instance with proper bounds.
      checking.


      .. autolink-examples:: update_player
         :collapse:


   .. py:method:: update_property(property_name: str, property_obj: haive.games.monopoly.models.Property) -> MonopolyState

      Update a property and return a new state instance.


      .. autolink-examples:: update_property
         :collapse:


   .. py:method:: validate_current_player_index(v: int, values) -> int
      :classmethod:


      Validate current player index is within bounds.

      :param v: Current player index to validate.
      :type v: int
      :param values: Other field values for validation context.

      :returns: Validated current player index.
      :rtype: int


      .. autolink-examples:: validate_current_player_index
         :collapse:


   .. py:method:: validate_doubles_count(v: int) -> int
      :classmethod:


      Validate doubles count doesn't exceed 3.

      :param v: Doubles count to validate.
      :type v: int

      :returns: Validated doubles count.
      :rtype: int


      .. autolink-examples:: validate_doubles_count
         :collapse:


   .. py:method:: validate_state_consistency() -> list[str]

      Validate the state for consistency and return any issues found.


      .. autolink-examples:: validate_state_consistency
         :collapse:


   .. py:property:: active_players
      :type: list[haive.games.monopoly.models.Player]


      Get list of active (non-bankrupt) players.

      :returns: All players who are still actively playing the game.
      :rtype: List[Player]

      .. autolink-examples:: active_players
         :collapse:


   .. py:property:: bankrupt_players
      :type: list[haive.games.monopoly.models.Player]


      Get list of bankrupt players.

      :returns: All players who have been eliminated from the game.
      :rtype: List[Player]

      .. autolink-examples:: bankrupt_players
         :collapse:


   .. py:attribute:: chance_cards
      :type:  list[str]
      :value: None



   .. py:attribute:: community_chest_cards
      :type:  list[str]
      :value: None



   .. py:property:: current_player
      :type: haive.games.monopoly.models.Player


      Get the current player with comprehensive bounds checking and validation.

      :returns: The player whose turn it currently is, with defensive fallbacks.
      :rtype: Player

      .. autolink-examples:: current_player
         :collapse:


   .. py:attribute:: current_player_index
      :type:  int
      :value: None



   .. py:attribute:: doubles_count
      :type:  int
      :value: None



   .. py:attribute:: doubles_rolled
      :type:  bool
      :value: None



   .. py:property:: economic_metrics
      :type: dict[str, int | float]


      Calculate comprehensive economic metrics for the game.

      :returns:

                Economic analysis including money supply,
                    wealth distribution, and market concentration.
      :rtype: Dict[str, Union[int, float]]

      .. autolink-examples:: economic_metrics
         :collapse:


   .. py:attribute:: error_message
      :type:  str | None
      :value: None



   .. py:attribute:: free_parking_money
      :type:  int
      :value: None



   .. py:attribute:: game_events
      :type:  Annotated[list[haive.games.monopoly.models.GameEvent], add_events]
      :value: None



   .. py:property:: game_statistics
      :type: dict[str, int | float | str]


      Generate comprehensive game statistics and metrics.

      :returns:

                Game statistics including duration,
                    activity levels, and strategic metrics.
      :rtype: Dict[str, Union[int, float, str]]

      .. autolink-examples:: game_statistics
         :collapse:


   .. py:attribute:: game_status
      :type:  GameStatus
      :value: None



   .. py:attribute:: hotels_remaining
      :type:  int
      :value: None



   .. py:attribute:: houses_remaining
      :type:  int
      :value: None



   .. py:property:: is_game_over
      :type: bool


      Check if the game has reached a terminal state.

      :returns: True if the game is over, False if gameplay should continue.
      :rtype: bool

      .. autolink-examples:: is_game_over
         :collapse:


   .. py:attribute:: jail_get_out_free_cards
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: last_roll
      :type:  haive.games.monopoly.models.DiceRoll | None
      :value: None



   .. py:attribute:: messages
      :type:  list[langchain_core.messages.BaseMessage] | None
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:property:: player_rankings
      :type: list[dict[str, Any]]


      Generate player rankings by net worth and strategic position.

      :returns: Players ranked by net worth with strategic metrics.
      :rtype: List[Dict[str, Any]]

      .. autolink-examples:: player_rankings
         :collapse:


   .. py:attribute:: players
      :type:  list[haive.games.monopoly.models.Player]
      :value: None



   .. py:attribute:: properties
      :type:  dict[str, haive.games.monopoly.models.Property]
      :value: None



   .. py:property:: property_distribution
      :type: dict[str, Any]


      Analyze property distribution and development across players.

      :returns:

                Property distribution analysis including monopolies,
                    development patterns, and strategic positions.
      :rtype: Dict[str, Any]

      .. autolink-examples:: property_distribution
         :collapse:


   .. py:attribute:: round_number
      :type:  int
      :value: None



   .. py:attribute:: turn_number
      :type:  int
      :value: None



   .. py:attribute:: winner
      :type:  str | None
      :value: None



.. py:function:: add_events(left: list[haive.games.monopoly.models.GameEvent], right: list[haive.games.monopoly.models.GameEvent]) -> list[haive.games.monopoly.models.GameEvent]

   Custom reducer for game events - always append new events.

   This reducer ensures that when state updates occur through LangGraph Commands,
   game events are properly accumulated rather than replaced.

   :param left: Existing events in the state.
   :type left: List[GameEvent]
   :param right: New events to add.
   :type right: List[GameEvent]

   :returns: Combined list of events.
   :rtype: List[GameEvent]


   .. autolink-examples:: add_events
      :collapse:

.. py:function:: add_strings(left: list[str], right: list[str]) -> list[str]

   Custom reducer for string lists.

   Generic reducer for accumulating string lists in LangGraph state updates.

   :param left: Existing strings in the state.
   :type left: List[str]
   :param right: New strings to add.
   :type right: List[str]

   :returns: Combined list of strings.
   :rtype: List[str]


   .. autolink-examples:: add_strings
      :collapse:

