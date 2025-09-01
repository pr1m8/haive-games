games.api.setup
===============

.. py:module:: games.api.setup

.. autoapi-nested-parse::

   Game API setup utilities.

   This module provides utilities for setting up game APIs using the standardized GameAPI
   system from haive-dataflow.



Attributes
----------

.. autoapisummary::

   games.api.setup.app


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/api/setup/GameAPIConfig

.. autoapisummary::

   games.api.setup.GameAPIConfig


Functions
---------

.. autoapisummary::

   games.api.setup.create_chess_api
   games.api.setup.create_connect4_api
   games.api.setup.create_game_api
   games.api.setup.create_tic_tac_toe_api


Module Contents
---------------

.. py:function:: create_chess_api(app: fastapi.FastAPI, config_overrides: dict[str, Any] | None = None, **kwargs) -> haive.dataflow.api.game_api.GameAPI

   Create a Chess game API.

   :param app: FastAPI application
   :param config_overrides: Configuration overrides for chess
   :param \*\*kwargs: Additional API configuration

   :returns: Configured GameAPI for chess

   .. rubric:: Examples

   >>> app = FastAPI()
   >>> chess_api = create_chess_api(
   ...     app,
   ...     config_overrides={
   ...         "white_model": "gpt-4",
   ...         "black_model": "claude-3-opus",
   ...         "enable_analysis": True
   ...     }
   ... )


.. py:function:: create_connect4_api(app: fastapi.FastAPI, config_overrides: dict[str, Any] | None = None, **kwargs) -> haive.dataflow.api.game_api.GameAPI

   Create a Connect4 game API.

   :param app: FastAPI application
   :param config_overrides: Configuration overrides for Connect4
   :param \*\*kwargs: Additional API configuration

   :returns: Configured GameAPI for Connect4

   .. rubric:: Examples

   >>> app = FastAPI()
   >>> connect4_api = create_connect4_api(
   ...     app,
   ...     config_overrides={
   ...         "red_model": "gpt-3.5-turbo",
   ...         "yellow_model": "gpt-3.5-turbo",
   ...         "temperature": 0.5
   ...     }
   ... )


.. py:function:: create_game_api(app: fastapi.FastAPI, agent_class: type[haive.core.engine.agent.agent.Agent], api_config: GameAPIConfig | None = None, **kwargs) -> haive.dataflow.api.game_api.GameAPI

   Create a game API with the standardized system.

   :param app: FastAPI application instance
   :param agent_class: The game agent class
   :param api_config: API configuration
   :param \*\*kwargs: Additional arguments passed to GameAPI

   :returns: Configured GameAPI instance


.. py:function:: create_tic_tac_toe_api(app: fastapi.FastAPI, config_overrides: dict[str, Any] | None = None, **kwargs) -> haive.dataflow.api.game_api.GameAPI

   Create a Tic-Tac-Toe game API.

   :param app: FastAPI application
   :param config_overrides: Configuration overrides for Tic-Tac-Toe
   :param \*\*kwargs: Additional API configuration

   :returns: Configured GameAPI for Tic-Tac-Toe

   .. rubric:: Examples

   >>> app = FastAPI()
   >>> ttt_api = create_tic_tac_toe_api(
   ...     app,
   ...     config_overrides={
   ...         "x_model": "claude-3-haiku",
   ...         "o_model": "claude-3-haiku",
   ...         "example_config": "budget"
   ...     }
   ... )


.. py:data:: app

