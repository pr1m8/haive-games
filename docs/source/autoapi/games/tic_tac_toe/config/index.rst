games.tic_tac_toe.config
========================

.. py:module:: games.tic_tac_toe.config

.. autoapi-nested-parse::

   Comprehensive configuration system for strategic Tic Tac Toe gameplay.

   This module provides sophisticated configuration management for Tic Tac Toe agents,
   supporting various gameplay modes, AI difficulty levels, and analysis features.
   The configuration system enables flexible game setups from educational tutorials
   to competitive AI matches with perfect play algorithms.

   The configuration system supports:
   - Multiple AI engine configurations for different skill levels
   - Strategic analysis toggle for educational gameplay
   - Visualization options for interactive experiences
   - Player assignment and turn order customization
   - Integration with LLM-based decision engines
   - Tournament-ready configuration presets

   .. rubric:: Examples

   Basic game configuration:

   .. code-block:: python

       config = TicTacToeConfig(
           name="educational_game",
           enable_analysis=True,
           visualize=True
       )

   Tournament configuration::

       config = TicTacToeConfig(
           name="tournament_match",
           enable_analysis=False,
           visualize=False,
           first_player="X"
       )

   Custom player setup::

       config = TicTacToeConfig(
           player_X="player2",
           player_O="player1",
           first_player="O"
       )

   Using default configuration::

       config = TicTacToeConfig.default_config()
       # Ready for standard gameplay

   .. note::

      All configurations use Pydantic for validation and support both JSON
      serialization and integration with the game agent framework.



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/tic_tac_toe/config/TicTacToeConfig

.. autoapisummary::

   games.tic_tac_toe.config.TicTacToeConfig


