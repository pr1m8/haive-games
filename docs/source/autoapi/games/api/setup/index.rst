games.api.setup
===============

.. py:module:: games.api.setup

.. autoapi-nested-parse::

   Game API setup utilities.

   This module provides utilities for setting up game APIs using the standardized GameAPI
   system from haive-dataflow.


   .. autolink-examples:: games.api.setup
      :collapse:


Attributes
----------

.. autoapisummary::

   games.api.setup.app


Classes
-------

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

.. py:class:: GameAPIConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for game API setup.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GameAPIConfig
      :collapse:

   .. py:attribute:: app_name
      :type:  str
      :value: None



   .. py:attribute:: cors_origins
      :type:  list[str]
      :value: None



   .. py:attribute:: default_config_overrides
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: enable_cors
      :type:  bool
      :value: None



   .. py:attribute:: route_prefix
      :type:  str
      :value: None



   .. py:attribute:: ws_route_prefix
      :type:  str
      :value: None



.. py:function:: create_chess_api(app: fastapi.FastAPI, config_overrides: dict[str, Any] | None = None, **kwargs) -> haive.dataflow.api.game_api.GameAPI

   Create a Chess game API.

   :param app: FastAPI application
   :param config_overrides: Configuration overrides for chess
   :param \*\*kwargs: Additional API configuration

   :returns: Configured GameAPI for chess

   .. rubric:: Example

   >>> app = FastAPI()
   >>> chess_api = create_chess_api(
   ...     app,
   ...     config_overrides={
   ...         "white_model": "gpt-4",
   ...         "black_model": "claude-3-opus",
   ...         "enable_analysis": True
   ...     }
   ... )


   .. autolink-examples:: create_chess_api
      :collapse:

.. py:function:: create_connect4_api(app: fastapi.FastAPI, config_overrides: dict[str, Any] | None = None, **kwargs) -> haive.dataflow.api.game_api.GameAPI

   Create a Connect4 game API.

   :param app: FastAPI application
   :param config_overrides: Configuration overrides for Connect4
   :param \*\*kwargs: Additional API configuration

   :returns: Configured GameAPI for Connect4

   .. rubric:: Example

   >>> app = FastAPI()
   >>> connect4_api = create_connect4_api(
   ...     app,
   ...     config_overrides={
   ...         "red_model": "gpt-3.5-turbo",
   ...         "yellow_model": "gpt-3.5-turbo",
   ...         "temperature": 0.5
   ...     }
   ... )


   .. autolink-examples:: create_connect4_api
      :collapse:

.. py:function:: create_game_api(app: fastapi.FastAPI, agent_class: type[haive.core.engine.agent.agent.Agent], api_config: GameAPIConfig | None = None, **kwargs) -> haive.dataflow.api.game_api.GameAPI

   Create a game API with the standardized system.

   :param app: FastAPI application instance
   :param agent_class: The game agent class
   :param api_config: API configuration
   :param \*\*kwargs: Additional arguments passed to GameAPI

   :returns: Configured GameAPI instance


   .. autolink-examples:: create_game_api
      :collapse:

.. py:function:: create_tic_tac_toe_api(app: fastapi.FastAPI, config_overrides: dict[str, Any] | None = None, **kwargs) -> haive.dataflow.api.game_api.GameAPI

   Create a Tic-Tac-Toe game API.

   :param app: FastAPI application
   :param config_overrides: Configuration overrides for Tic-Tac-Toe
   :param \*\*kwargs: Additional API configuration

   :returns: Configured GameAPI for Tic-Tac-Toe

   .. rubric:: Example

   >>> app = FastAPI()
   >>> ttt_api = create_tic_tac_toe_api(
   ...     app,
   ...     config_overrides={
   ...         "x_model": "claude-3-haiku",
   ...         "o_model": "claude-3-haiku",
   ...         "example_config": "budget"
   ...     }
   ... )


   .. autolink-examples:: create_tic_tac_toe_api
      :collapse:

.. py:data:: app

