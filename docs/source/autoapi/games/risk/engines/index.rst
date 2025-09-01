games.risk.engines
==================

.. py:module:: games.risk.engines

.. autoapi-nested-parse::

   Risk game engines.

   This module defines engine configurations for the Risk game, including state management,
   analysis, and strategic planning.



Functions
---------

.. autoapisummary::

   games.risk.engines.risk_engines


Module Contents
---------------

.. py:function:: risk_engines(config: haive.games.risk.config.RiskConfig | None = None) -> dict[str, Any]

   Create a set of engines for the Risk game.

   :param config: Optional configuration for the Risk game.
                  If not provided, default configuration will be used.

   :returns: A dictionary of engine configurations for the Risk game.


