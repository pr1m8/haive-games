games.battleship.state
======================

.. py:module:: games.battleship.state


Classes
-------

.. autoapisummary::

   games.battleship.state.BattleshipState
   games.battleship.state.PlayerState


Module Contents
---------------

.. py:class:: BattleshipState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive state model for managing complete Battleship game sessions.

   This class provides complete state management for Battleship games, supporting
   turn-based gameplay, phase transitions, strategic analysis, and secure state
   views. The state system maintains both public and private information while
   ensuring game rule enforcement and data integrity.

   The game state manages:
   - Complete player states with board and strategic data
   - Turn-based gameplay mechanics and phase transitions
   - Comprehensive move history and outcome tracking
   - Error handling and state validation
   - Public/private state views for AI decision-making
   - Game completion detection and winner determination

   .. attribute:: player1_state

      Complete state for the first player,
      including board configuration, ship placements, and strategic analysis.

      :type: PlayerState

   .. attribute:: player2_state

      Complete state for the second player,
      including board configuration, ship placements, and strategic analysis.

      :type: PlayerState

   .. attribute:: current_player

      Identifier of the player
      whose turn it currently is in the game.

      :type: Literal["player1", "player2"]

   .. attribute:: game_phase

      Current phase of the game (SETUP, PLAYING, ENDED),
      determining which actions are valid.

      :type: GamePhase

   .. attribute:: winner

      Identifier of the winning
      player, or None if the game is still in progress.

      :type: Optional[Literal["player1", "player2"]]

   .. attribute:: move_history

      Complete chronological record
      of all moves made in the game with their outcomes.

      :type: List[Tuple[str, MoveOutcome]]

   .. attribute:: error_message

      Error message from the last operation,
      or None if no error occurred.

      :type: Optional[str]

   .. rubric:: Examples

   Creating a new game state::\n

       state = BattleshipState()
       assert state.current_player == "player1"
       assert state.game_phase == GamePhase.SETUP
       assert state.winner is None

   Managing turn-based gameplay::\n

       # Start player 1's turn
       state.current_player = "player1"
       player1 = state.get_player_state("player1")

       # After player 1 moves, switch to player 2
       state.current_player = "player2"
       player2 = state.get_player_state("player2")

   Tracking game progress::\n

       # Check if setup is complete
       if state.is_setup_complete():
           state.game_phase = GamePhase.PLAYING

       # Check for game completion
       if state.is_game_over():
           # Determine winner based on remaining ships
           if state.player1_state.board.all_ships_sunk():
               state.winner = "player2"
           elif state.player2_state.board.all_ships_sunk():
               state.winner = "player1"

   Managing move history::\n

       # Add a move to history
       move_outcome = MoveOutcome(hit=True, sunk_ship=ShipType.DESTROYER)
       state.move_history.append(("player1", move_outcome))

       # Analyze recent moves
       recent_moves = state.move_history[-5:]  # Last 5 moves

   Getting secure state views::\n

       # Get public state for AI decision-making
       public_state = state.get_public_state_for_player("player1")
       # Contains only information player1 should know

       # Check opponent without revealing private info
       opponent = state.get_opponent("player1")

   Error handling::\n

       try:
           # Attempt game operation
           state.some_operation()
       except Exception as e:
           state.error_message = str(e)
           # Game can continue with error logged

   .. note::

      The state uses Pydantic annotations for LangGraph accumulation,
      enabling efficient state updates in distributed game systems.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BattleshipState
      :collapse:

   .. py:method:: get_opponent(player: str) -> str

      Determine the opponent of a specified player.

      Provides the identifier of the opposing player, essential for turn-based
      game mechanics and strategic analysis. This method ensures consistent
      opponent identification throughout the game.

      :param player: Player identifier ("player1" or "player2").
      :type player: str

      :returns: The opponent's identifier ("player2" for "player1", "player1" for "player2").
      :rtype: str

      .. rubric:: Examples

      Basic opponent identification::\n

          state = BattleshipState()
          opponent = state.get_opponent("player1")
          assert opponent == "player2"

      Turn-based game logic::\n

          current_player = state.current_player
          opponent = state.get_opponent(current_player)

          # Switch turns
          state.current_player = opponent

      Strategic analysis::\n

          player = "player1"
          opponent = state.get_opponent(player)
          opponent_state = state.get_player_state(opponent)

          # Analyze opponent's remaining ships
          opponent_ships = opponent_state.board.sunk_ships


      .. autolink-examples:: get_opponent
         :collapse:


   .. py:method:: get_player_state(player: str) -> PlayerState

      Retrieve a player's complete state by their identifier.

      Provides access to a player's complete state including board configuration,
      ship placements, strategic analysis, and game statistics. This method
      ensures type safety and validates player identifiers.

      :param player: Player identifier, must be either "player1" or "player2".
      :type player: str

      :returns:

                The complete state object for the specified player,
                    containing board, strategic analysis, and placement information.
      :rtype: PlayerState

      :raises ValueError: If the player identifier is not "player1" or "player2".

      .. rubric:: Examples

      Basic player state access::\n

          state = BattleshipState()
          player1 = state.get_player_state("player1")
          player1.has_placed_ships = True

      Accessing player board::\n

          player_state = state.get_player_state("player1")
          hits = len(player_state.board.successful_hits)
          misses = len(player_state.board.failed_attacks)

      Managing strategic analysis::\n

          player_state = state.get_player_state("player2")
          player_state.strategic_analysis.append("Focus on quadrant C")
          latest_analysis = player_state.strategic_analysis[-1]


      .. autolink-examples:: get_player_state
         :collapse:


   .. py:method:: get_public_state_for_player(player: str) -> dict[str, Any]

      Generate a secure public view of the game state for AI decision- making.

      Creates a carefully sanitized view of the game state that provides all
      information a player should legitimately know while hiding opponent secrets
      like ship positions. This method is essential for AI agents to make informed
      decisions without having access to private information.

      The public state includes:
      - Game phase and turn information
      - Player's own hits, misses, and sunk ships
      - Opponent's hits, misses, and sunk ships (but not ship positions)
      - Strategic analysis history for the requesting player
      - Complete move history for pattern analysis
      - Structured output compatibility for LLM processing

      :param player: Player identifier ("player1" or "player2") requesting the state.
      :type player: str

      :returns:

                Comprehensive public state dictionary containing:
                    - game_phase: Current game phase (setup/playing/ended)
                    - current_player: Whose turn it is
                    - is_your_turn: Boolean indicating if it's the requesting player's turn
                    - your_hits/your_misses: Player's attack results
                    - your_sunk_ships: Ships the player has sunk
                    - opponent_hits/opponent_misses: Opponent's attack results
                    - opponent_sunk_ships: Ships the opponent has sunk
                    - strategic_thoughts: Latest strategic analysis
                    - move_history: Complete chronological move record
                    - your_analysis: Full strategic analysis history
                    - row/col: Compatibility fields for structured output
      :rtype: Dict[str, Any]

      .. rubric:: Examples

      Getting state for AI decision-making::\n

          state = BattleshipState()
          public_state = state.get_public_state_for_player("player1")

          # Check if it's player's turn
          if public_state["is_your_turn"]:
              # Use public state to make move decision
              hits = public_state["your_hits"]
              misses = public_state["your_misses"]

      Analyzing strategic information::\n

          public_state = state.get_public_state_for_player("player2")
          strategic_thoughts = public_state["strategic_thoughts"]
          analysis_history = public_state["your_analysis"]

          # Use for strategic planning
          if "center quadrant" in strategic_thoughts:
              # Continue center-focused strategy
              pass

      Checking game progress::\n

          public_state = state.get_public_state_for_player("player1")

          player_sunk = len(public_state["your_sunk_ships"])
          opponent_sunk = len(public_state["opponent_sunk_ships"])

          print(f"You sunk: {player_sunk}, Opponent sunk: {opponent_sunk}")

      Move history analysis::\n

          public_state = state.get_public_state_for_player("player1")
          recent_moves = public_state["move_history"][-5:]  # Last 5 moves

          # Analyze patterns in recent gameplay
          for player_id, move_outcome in recent_moves:
              if move_outcome["hit"]:
                  print(f"{player_id} scored a hit!")

      .. note::

         This method ensures information security by never exposing opponent
         ship positions or other private game state. All information provided
         is what the player would legitimately know during actual gameplay.


      .. autolink-examples:: get_public_state_for_player
         :collapse:


   .. py:method:: is_game_over() -> bool

      Determine if the game has reached a terminal state.

      Checks multiple conditions to determine if the game is complete:
      1. Game phase is explicitly set to ENDED
      2. All ships of either player are sunk (victory condition)

      This method is critical for game loop termination and winner determination.

      :returns: True if the game is over, False if gameplay should continue.
      :rtype: bool

      .. rubric:: Examples

      Basic game completion check::\n

          state = BattleshipState()
          state.game_phase = GamePhase.ENDED
          assert state.is_game_over() == True

      Victory condition checking::\n

          if state.is_game_over():
              if state.player1_state.board.all_ships_sunk():
                  state.winner = "player2"
                  print("Player 2 wins!")
              elif state.player2_state.board.all_ships_sunk():
                  state.winner = "player1"
                  print("Player 1 wins!")

      Game loop integration::\n

          while not state.is_game_over():
              current_player = state.current_player
              # Process current player's turn
              process_turn(state, current_player)

          # Game completed, display results
          winner = state.winner
          print(f"Game over! Winner: {winner}")


      .. autolink-examples:: is_game_over
         :collapse:


   .. py:method:: is_setup_complete() -> bool

      Check if the ship placement phase is complete for both players.

      Determines whether both players have successfully placed all their ships
      and the game is ready to transition from the SETUP phase to the PLAYING
      phase. This method is essential for game phase management.

      :returns: True if both players have completed ship placement, False otherwise.
      :rtype: bool

      .. rubric:: Examples

      Checking setup completion::\n

          state = BattleshipState()
          state.player1_state.has_placed_ships = True
          state.player2_state.has_placed_ships = True

          if state.is_setup_complete():
              state.game_phase = GamePhase.PLAYING

      Game phase transition logic::\n

          if state.game_phase == GamePhase.SETUP and state.is_setup_complete():
              state.game_phase = GamePhase.PLAYING
              print("Game is ready to begin!")

      Validating game readiness::\n

          if not state.is_setup_complete():
              players_needed = []
              if not state.player1_state.has_placed_ships:
                  players_needed.append("player1")
              if not state.player2_state.has_placed_ships:
                  players_needed.append("player2")
              print(f"Waiting for ship placement: {players_needed}")


      .. autolink-examples:: is_setup_complete
         :collapse:


   .. py:attribute:: current_player
      :type:  Literal['player1', 'player2']
      :value: None



   .. py:attribute:: error_message
      :type:  str | None
      :value: None



   .. py:attribute:: game_phase
      :type:  haive.games.battleship.models.GamePhase
      :value: None



   .. py:property:: game_statistics
      :type: dict[str, int | float | str]


      Calculate comprehensive game statistics and metrics.

      :returns: Dictionary containing game statistics.
      :rtype: Dict[str, Union[int, float, str]]

      .. rubric:: Examples

      Analyzing game performance::\n

          stats = state.game_statistics
          print(f"Total moves: {stats['total_moves']}")
          print(f"Game duration: {stats['game_phase']}")

      .. autolink-examples:: game_statistics
         :collapse:


   .. py:attribute:: move_history
      :type:  list[tuple[str, haive.games.battleship.models.MoveOutcome]]
      :value: None



   .. py:attribute:: player1_state
      :type:  Annotated[PlayerState, accumulate]
      :value: None



   .. py:attribute:: player2_state
      :type:  Annotated[PlayerState, accumulate]
      :value: None



   .. py:attribute:: winner
      :type:  Literal['player1', 'player2'] | None
      :value: None



.. py:class:: PlayerState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive state model for individual player tracking and strategic analysis.

   This class maintains complete state information for a single player in the
   Battleship game, including their board configuration, ship placements, attack
   history, and strategic analysis data. The state supports both active gameplay
   and post-game analysis.

   The player state tracks:
   - Board state with ship positions and attack results
   - Strategic analysis history for decision-making
   - Ship placement records and validation
   - Performance metrics and game statistics
   - Error tracking and state validation

   .. attribute:: board

      The player's game board containing ship positions,
      attack history, successful hits, failed attacks, and sunk ships.

      :type: PlayerBoard

   .. attribute:: strategic_analysis

      Complete history of strategic analyses
      performed for this player, used for learning and adaptation.

      :type: List[str]

   .. attribute:: has_placed_ships

      Flag indicating whether the player has completed
      the ship placement phase of the game.

      :type: bool

   .. attribute:: ship_placements

      Complete record of all ship
      placement commands executed for this player.

      :type: List[ShipPlacement]

   .. rubric:: Examples

   Creating a new player state::\n

       player_state = PlayerState()
       assert not player_state.has_placed_ships
       assert len(player_state.strategic_analysis) == 0

   Managing ship placement::\n

       placement = ShipPlacement(
           ship_type=ShipType.DESTROYER,
           start_row=0, start_col=0,
           orientation=Orientation.HORIZONTAL
       )
       player_state.ship_placements.append(placement)
       player_state.has_placed_ships = True

   Adding strategic analysis::\n

       analysis = "Enemy likely has carrier in top-left quadrant"
       player_state.strategic_analysis.append(analysis)

       # Access latest analysis
       latest_analysis = player_state.strategic_analysis[-1]

   Checking board state::\n

       if player_state.board.all_ships_sunk():
           print("Player has lost the game")

       hits = len(player_state.board.successful_hits)
       misses = len(player_state.board.failed_attacks)
       accuracy = hits / (hits + misses) if (hits + misses) > 0 else 0

   .. note::

      Player state is designed to be serializable and thread-safe, supporting
      both local gameplay and distributed game systems.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlayerState
      :collapse:

   .. py:attribute:: board
      :type:  haive.games.battleship.models.PlayerBoard
      :value: None



   .. py:attribute:: has_placed_ships
      :type:  bool
      :value: None



   .. py:attribute:: ship_placements
      :type:  list[haive.games.battleship.models.ShipPlacement]
      :value: None



   .. py:attribute:: strategic_analysis
      :type:  list[str]
      :value: None



