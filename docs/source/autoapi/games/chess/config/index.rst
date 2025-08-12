
:py:mod:`games.chess.config`
============================

.. py:module:: games.chess.config

Chess agent configuration module.

from typing import Any
This module provides configuration classes for chess agents, including:
    - Core game parameters
    - LLM engine settings
    - Analysis options
    - Visualization settings
    - State schema definition

The configuration system uses Pydantic for validation and default values,
making it easy to create and customize chess agent instances.


.. autolink-examples:: games.chess.config
   :collapse:

Classes
-------

.. autoapisummary::

   games.chess.config.ChessConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChessConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ChessConfig {
        node [shape=record];
        "ChessConfig" [label="ChessConfig"];
        "haive.games.core.config.BaseGameConfig" -> "ChessConfig";
      }

.. autoclass:: games.chess.config.ChessConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.chess.config
   :collapse:
   
.. autolink-skip:: next
