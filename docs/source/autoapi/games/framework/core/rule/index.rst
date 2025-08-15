games.framework.core.rule
=========================

.. py:module:: games.framework.core.rule


Classes
-------

.. autoapisummary::

   games.framework.core.rule.Rule
   games.framework.core.rule.RuleSet


Module Contents
---------------

.. py:class:: Rule(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Base class for game rules.

   Rules define what actions are valid in a game and how they affect the game state.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Rule
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: apply(action: Any, game_state: Any) -> dict[str, Any]

      Apply the effects of this rule after an action is taken.

      :param action: The action being taken
      :param game_state: The current game state

      :returns: Dictionary of updates to apply to the game state


      .. autolink-examples:: apply
         :collapse:


   .. py:method:: validate(action: Any, game_state: Any) -> bool
      :abstractmethod:


      Validate whether an action is allowed under this rule.

      :param action: The action to validate
      :param game_state: The current game state

      :returns: True if the action is valid, False otherwise


      .. autolink-examples:: validate
         :collapse:


   .. py:attribute:: active
      :type:  bool
      :value: True



   .. py:attribute:: description
      :type:  str | None
      :value: None



   .. py:attribute:: name
      :type:  str


.. py:class:: RuleSet(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A collection of rules that govern a game.

   RuleSet allows for modular rule composition and enforcement.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RuleSet
      :collapse:

   .. py:method:: add_rule(rule: Rule) -> None

      Add a rule to the ruleset.

      :param rule: The rule to add


      .. autolink-examples:: add_rule
         :collapse:


   .. py:method:: apply_effects(action: Any, game_state: Any) -> dict[str, Any]

      Apply the effects of all rules after an action.

      :param action: The action that was taken
      :param game_state: The current game state

      :returns: Combined dictionary of all updates to apply


      .. autolink-examples:: apply_effects
         :collapse:


   .. py:method:: validate_action(action: Any, game_state: Any) -> bool

      Validate an action against all active rules.

      :param action: The action to validate
      :param game_state: The current game state

      :returns: True if the action is valid under all rules, False otherwise


      .. autolink-examples:: validate_action
         :collapse:


   .. py:attribute:: name
      :type:  str


   .. py:attribute:: rules
      :type:  list[Rule]
      :value: None



