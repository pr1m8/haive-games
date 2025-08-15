games.cards.standard.poker.state
================================

.. py:module:: games.cards.standard.poker.state


Classes
-------

.. autoapisummary::

   games.cards.standard.poker.state.PokerBettingRound
   games.cards.standard.poker.state.PokerGameState
   games.cards.standard.poker.state.PokerPhase
   games.cards.standard.poker.state.PokerVariant


Module Contents
---------------

.. py:class:: PokerBettingRound

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Betting rounds in poker.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PokerBettingRound
      :collapse:

   .. py:attribute:: FLOP
      :value: 'flop'



   .. py:attribute:: PRE_FLOP
      :value: 'pre_flop'



   .. py:attribute:: RIVER
      :value: 'river'



   .. py:attribute:: TURN
      :value: 'turn'



.. py:class:: PokerGameState

   Bases: :py:obj:`haive.games.cards.card.components.state.CardGameState`\ [\ :py:obj:`haive.games.cards.card.components.standard.StandardCard`\ , :py:obj:`haive.games.cards.card.components.actions.CardAction`\ ], :py:obj:`haive.games.cards.card.components.betting.WagerableGameState`


   State for poker games.


   .. autolink-examples:: PokerGameState
      :collapse:

   .. py:method:: _distribute_winnings() -> None

      Distribute pot to winners based on hand rankings.


      .. autolink-examples:: _distribute_winnings
         :collapse:


   .. py:method:: _evaluate_hands() -> None

      Evaluate all active hands to determine winner(s).


      .. autolink-examples:: _evaluate_hands
         :collapse:


   .. py:method:: _get_position_order() -> list[int]

      Get the order of positions for the current betting round.


      .. autolink-examples:: _get_position_order
         :collapse:


   .. py:method:: _post_blinds() -> None

      Post small and big blinds.


      .. autolink-examples:: _post_blinds
         :collapse:


   .. py:method:: _setup_positions() -> None

      Set up dealer and blind positions.


      .. autolink-examples:: _setup_positions
         :collapse:


   .. py:method:: advance_phase() -> None

      Advance to the next phase of the poker game.


      .. autolink-examples:: advance_phase
         :collapse:


   .. py:method:: deal_community_cards(count: int = 1) -> list[haive.games.cards.card.components.standard.StandardCard]

      Deal community cards.


      .. autolink-examples:: deal_community_cards
         :collapse:


   .. py:method:: deal_hole_cards() -> None

      Deal hole cards to all players.


      .. autolink-examples:: deal_hole_cards
         :collapse:


   .. py:method:: get_player_view(player_id: str) -> dict[str, Any]

      Get the game state from a specific player's perspective.


      .. autolink-examples:: get_player_view
         :collapse:


   .. py:method:: setup_active_players() -> PokerGameState

      Ensure active_players is populated.


      .. autolink-examples:: setup_active_players
         :collapse:


   .. py:method:: start_game() -> None

      Start the poker game.


      .. autolink-examples:: start_game
         :collapse:


   .. py:attribute:: active_players
      :type:  list[str]
      :value: None



   .. py:attribute:: all_in_players
      :type:  list[str]
      :value: None



   .. py:attribute:: betting_round
      :type:  PokerBettingRound | None
      :value: None



   .. py:attribute:: big_blind
      :type:  int
      :value: 2



   .. py:attribute:: big_blind_position
      :type:  int | None
      :value: None



   .. py:attribute:: community_cards
      :type:  list[haive.games.cards.card.components.standard.StandardCard]
      :value: None



   .. py:attribute:: current_bet
      :type:  int
      :value: 0



   .. py:attribute:: dealer_position
      :type:  int
      :value: 0



   .. py:attribute:: folded_players
      :type:  list[str]
      :value: None



   .. py:attribute:: hand_rankings
      :type:  dict[str, haive.games.cards.standard.poker.scoring.PokerHandRank]
      :value: None



   .. py:attribute:: last_raiser
      :type:  str | None
      :value: None



   .. py:attribute:: phase
      :type:  PokerPhase


   .. py:attribute:: small_blind
      :type:  int
      :value: 1



   .. py:attribute:: small_blind_position
      :type:  int | None
      :value: None



   .. py:attribute:: variant
      :type:  PokerVariant


.. py:class:: PokerPhase

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Phases in a poker game.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PokerPhase
      :collapse:

   .. py:attribute:: DEAL
      :value: 'deal'



   .. py:attribute:: FLOP
      :value: 'flop'



   .. py:attribute:: PRE_FLOP
      :value: 'pre_flop'



   .. py:attribute:: RIVER
      :value: 'river'



   .. py:attribute:: SHOWDOWN
      :value: 'showdown'



   .. py:attribute:: TURN
      :value: 'turn'



.. py:class:: PokerVariant

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of poker games.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PokerVariant
      :collapse:

   .. py:attribute:: FIVE_CARD_DRAW
      :value: 'five_card_draw'



   .. py:attribute:: OMAHA
      :value: 'omaha'



   .. py:attribute:: SEVEN_CARD_STUD
      :value: 'seven_card_stud'



   .. py:attribute:: TEXAS_HOLDEM
      :value: 'texas_holdem'



