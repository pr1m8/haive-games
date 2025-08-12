
:py:mod:`games.tic_tac_toe.config`
==================================

.. py:module:: games.tic_tac_toe.config

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

Basic game configuration::

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


.. autolink-examples:: games.tic_tac_toe.config
   :collapse:

Classes
-------

.. autoapisummary::

   games.tic_tac_toe.config.TicTacToeConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TicTacToeConfig:

   .. graphviz::
      :align: center

      digraph inheritance_TicTacToeConfig {
        node [shape=record];
        "TicTacToeConfig" [label="TicTacToeConfig"];
        "haive.games.framework.base.config.GameConfig" -> "TicTacToeConfig";
      }

.. autoclass:: games.tic_tac_toe.config.TicTacToeConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.tic_tac_toe.config
   :collapse:
   
.. autolink-skip:: next
