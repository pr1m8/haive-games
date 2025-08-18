games.among_us.factory
======================

.. py:module:: games.among_us.factory

Module documentation for games.among_us.factory


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 functions</span>   </div>


      
            
            
            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.among_us.factory.create_among_us_game

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_among_us_game(player_names: list[str], llm_config: dict[str, Any] | None = None, game_config: dict[str, Any] | None = None) -> haive.games.among_us.agent.AmongUsAgent

            Create an Among Us game with customizable configuration.

            :param player_names: List of player names/IDs
            :param llm_config: Configuration for the language model
            :param game_config: Game-specific configuration

            :returns: An initialized AmongUsAgent





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.among_us.factory import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

