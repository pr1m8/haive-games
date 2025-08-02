from abc import abstractmethod
from typing import Any, Generic
from pydantic import BaseModel, Field, model_validator
from haive.games.core.components.cards.base import TCard, TState

class ActionResult(BaseModel):
    """Result of executing a card action."""
    success: bool
    message: str = ''
    state_updates: dict[str, Any] = Field(default_factory=dict)

class CardAction(BaseModel, Generic[TCard, TState]):
    """Base model for card game actions."""
    action_type: str
    player_id: str

    class Config:
        arbitrary_types_allowed = True

    @model_validator(mode='after')
    def validate_action(self) -> 'CardAction':
        """Validate the action is properly formed."""
        return self

    def can_execute(self, state: TState) -> bool:
        """Check if this action can be executed in the current state."""
        return True

    @abstractmethod
    def execute(self, state: TState) -> ActionResult:
        """Execute this action on the game state."""

class DrawCardAction(CardAction[TCard, TState]):
    """Action to draw a card from the deck."""
    action_type: str = 'draw_card'
    count: int = 1

    @model_validator(mode='after')
    def validate_action(self) -> 'DrawCardAction':
        """Validate draw count."""
        if self.count < 1:
            raise ValueError('Must draw at least one card')
        return self

    def can_execute(self, state: TState) -> bool:
        """Check if player can draw."""
        return self.player_id in state.hands and state.deck.count() >= self.count and (self.player_id == state.current_player_id)

    def execute(self, state: TState) -> ActionResult:
        """Draw card(s) from deck to player's hand."""
        if not self.can_execute(state):
            return ActionResult(success=False, message='Cannot draw card: either not your turn or deck is empty')
        drawn_cards = state.deck.draw_many(self.count)
        for card in drawn_cards:
            state.hands[self.player_id].add_card(card)
        return ActionResult(success=True, message=f'Drew {len(drawn_cards)} card(s)', state_updates={'deck': state.deck, 'hands': {self.player_id: state.hands[self.player_id]}})

class PlayCardAction(CardAction[TCard, TState]):
    """Action to play a card from hand."""
    action_type: str = 'play_card'
    card_id: str
    target_id: str | None = None

    def can_execute(self, state: TState) -> bool:
        """Check if player can play the card."""
        if self.player_id != state.current_player_id:
            return False
        if self.player_id not in state.hands:
            return False
        hand = state.hands[self.player_id]
        return any((card.id == self.card_id for card in hand.cards))

    def execute(self, state: TState) -> ActionResult:
        """Play the card from hand."""
        if not self.can_execute(state):
            return ActionResult(success=False, message='Cannot play card: either not your turn or card not in hand')
        hand = state.hands[self.player_id]
        card = hand.play_card(self.card_id)
        if card:
            if hasattr(state, 'played_cards'):
                state.played_cards.append(card)
            elif hasattr(state, 'discard_pile'):
                state.discard_pile.append(card)
        return ActionResult(success=True, message=f'Played card {(card.name if card else 'unknown')}', state_updates={'hands': {self.player_id: hand}, 'played_cards': getattr(state, 'played_cards', []) if hasattr(state, 'played_cards') else None, 'discard_pile': getattr(state, 'discard_pile', []) if hasattr(state, 'discard_pile') else None})