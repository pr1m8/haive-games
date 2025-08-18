games.utils.recursion_config
============================

.. py:module:: games.utils.recursion_config

Recursion configuration utilities for game agents.

This module provides utilities to properly configure recursion limits for game agents to
prevent recursion errors during gameplay.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Recursion configuration utilities for game agents.

   This module provides utilities to properly configure recursion limits for game agents to
   prevent recursion errors during gameplay.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.utils.recursion_config.RecursionConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: RecursionConfig

            Configuration helper for managing recursion limits in game agents.


            .. py:method:: configure_runnable(runnable_config: dict[str, Any] | None = None, game_name: str | None = None, game_type: str = 'standard', enable_analysis: bool = False, num_players: int = 2, thread_id: str | None = None) -> dict[str, Any]
               :classmethod:


               Configure or update a runnable config with appropriate recursion limit.

               :param runnable_config: Existing config to update (creates new if None)
               :param game_name: Specific game name
               :param game_type: Type of game
               :param enable_analysis: Whether analysis is enabled
               :param num_players: Number of players
               :param thread_id: Thread ID to use (generates if None)

               :returns: Updated runnable configuration

               .. rubric:: Examples

               >>> # Create new config for chess
               >>> config = RecursionConfig.configure_runnable(
               ...     game_name="chess",
               ...     enable_analysis=True
               ... )
               >>> print(config["configurable"]["recursion_limit"])  # 720

               >>> # Update existing config
               >>> existing = {"configurable": {"thread_id": "abc123"}}
               >>> updated = RecursionConfig.configure_runnable(
               ...     runnable_config=existing,
               ...     game_type="complex"
               ... )
               >>> print(updated["configurable"]["recursion_limit"])  # 800



            .. py:method:: get_recursion_limit(game_name: str | None = None, game_type: str = 'standard', enable_analysis: bool = False, num_players: int = 2, custom_limit: int | None = None) -> int
               :classmethod:


               Get the appropriate recursion limit for a game.

               :param game_name: Specific game name (e.g., "chess", "checkers")
               :param game_type: Type of game ("simple", "standard", "complex", "extreme")
               :param enable_analysis: Whether analysis is enabled (adds overhead)
               :param num_players: Number of players (more players = higher limit)
               :param custom_limit: Override with custom limit

               :returns: Recommended recursion limit

               .. rubric:: Examples

               >>> # Simple game
               >>> limit = RecursionConfig.get_recursion_limit(game_type="simple")
               >>> print(limit)  # 300

               >>> # Chess with analysis
               >>> limit = RecursionConfig.get_recursion_limit(
               ...     game_name="chess",
               ...     enable_analysis=True
               ... )
               >>> print(limit)  # 720 (600 + 20% for analysis)

               >>> # Multi-player game
               >>> limit = RecursionConfig.get_recursion_limit(
               ...     game_type="complex",
               ...     num_players=4
               ... )
               >>> print(limit)  # 960 (800 + 20% for extra players)



            .. py:method:: validate_recursion_limit(limit: int, game_name: str | None = None, game_type: str = 'standard') -> tuple[bool, str]
               :classmethod:


               Validate if a recursion limit is appropriate.

               :param limit: The recursion limit to validate
               :param game_name: Specific game name
               :param game_type: Type of game

               :returns: Tuple of (is_valid, message)

               .. rubric:: Examples

               >>> valid, msg = RecursionConfig.validate_recursion_limit(
               ...     100, game_type="complex"
               ... )
               >>> print(valid, msg)  # False, "Limit too low..."



            .. py:attribute:: DEFAULT_LIMITS


            .. py:attribute:: GAME_LIMITS





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.utils.recursion_config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

