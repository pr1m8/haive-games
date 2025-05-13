# game_framework/core/rule.py
from __future__ import annotations
from typing import Any, Callable, Dict, List, Optional
from pydantic import BaseModel, Field
from abc import abstractmethod

class Rule(BaseModel):
    """
    Base class for game rules.
    
    Rules define what actions are valid in a game and how they affect the game state.
    """
    name: str
    description: Optional[str] = None
    active: bool = True
    
    class Config:
        arbitrary_types_allowed = True
    
    @abstractmethod
    def validate(self, action: Any, game_state: Any) -> bool:
        """
        Validate whether an action is allowed under this rule.
        
        Args:
            action: The action to validate
            game_state: The current game state
            
        Returns:
            True if the action is valid, False otherwise
        """
        pass
    
    def apply(self, action: Any, game_state: Any) -> Dict[str, Any]:
        """
        Apply the effects of this rule after an action is taken.
        
        Args:
            action: The action being taken
            game_state: The current game state
            
        Returns:
            Dictionary of updates to apply to the game state
        """
        return {}

class RuleSet(BaseModel):
    """
    A collection of rules that govern a game.
    
    RuleSet allows for modular rule composition and enforcement.
    """
    name: str
    rules: List[Rule] = Field(default_factory=list)
    
    def add_rule(self, rule: Rule) -> None:
        """
        Add a rule to the ruleset.
        
        Args:
            rule: The rule to add
        """
        self.rules.append(rule)
    
    def validate_action(self, action: Any, game_state: Any) -> bool:
        """
        Validate an action against all active rules.
        
        Args:
            action: The action to validate
            game_state: The current game state
            
        Returns:
            True if the action is valid under all rules, False otherwise
        """
        return all(
            rule.validate(action, game_state)
            for rule in self.rules
            if rule.active
        )
    
    def apply_effects(self, action: Any, game_state: Any) -> Dict[str, Any]:
        """
        Apply the effects of all rules after an action.
        
        Args:
            action: The action that was taken
            game_state: The current game state
            
        Returns:
            Combined dictionary of all updates to apply
        """
        updates = {}
        for rule in self.rules:
            if rule.active:
                rule_updates = rule.apply(action, game_state)
                updates.update(rule_updates)
        return updates