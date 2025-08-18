games.framework.core.rule
=========================

.. py:module:: games.framework.core.rule

Module documentation for games.framework.core.rule


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 classes</span>   </div>


      
            
            

.. admonition:: Classes (2)
   :class: note

   .. autoapisummary::

      games.framework.core.rule.Rule
      games.framework.core.rule.RuleSet

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Rule(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Base class for game rules.

            Rules define what actions are valid in a game and how they affect the game state.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: apply(action: Any, game_state: Any) -> dict[str, Any]

               Apply the effects of this rule after an action is taken.

               :param action: The action being taken
               :param game_state: The current game state

               :returns: Dictionary of updates to apply to the game state



            .. py:method:: validate(action: Any, game_state: Any) -> bool
               :abstractmethod:


               Validate whether an action is allowed under this rule.

               :param action: The action to validate
               :param game_state: The current game state

               :returns: True if the action is valid, False otherwise



            .. py:attribute:: active
               :type:  bool
               :value: True



            .. py:attribute:: description
               :type:  str | None
               :value: None



            .. py:attribute:: name
               :type:  str



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: RuleSet(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A collection of rules that govern a game.

            RuleSet allows for modular rule composition and enforcement.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: add_rule(rule: Rule) -> None

               Add a rule to the ruleset.

               :param rule: The rule to add



            .. py:method:: apply_effects(action: Any, game_state: Any) -> dict[str, Any]

               Apply the effects of all rules after an action.

               :param action: The action that was taken
               :param game_state: The current game state

               :returns: Combined dictionary of all updates to apply



            .. py:method:: validate_action(action: Any, game_state: Any) -> bool

               Validate an action against all active rules.

               :param action: The action to validate
               :param game_state: The current game state

               :returns: True if the action is valid under all rules, False otherwise



            .. py:attribute:: name
               :type:  str


            .. py:attribute:: rules
               :type:  list[Rule]
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.framework.core.rule import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

