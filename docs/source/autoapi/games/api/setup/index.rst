games.api.setup
===============

.. py:module:: games.api.setup

Game API setup utilities.

This module provides utilities for setting up game APIs using the standardized GameAPI
system from haive-dataflow.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">4 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Game API setup utilities.

   This module provides utilities for setting up game APIs using the standardized GameAPI
   system from haive-dataflow.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.api.setup.app

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.api.setup.GameAPIConfig

            

.. admonition:: Functions (4)
   :class: info

   .. autoapisummary::

      games.api.setup.create_chess_api
      games.api.setup.create_connect4_api
      games.api.setup.create_game_api
      games.api.setup.create_tic_tac_toe_api

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameAPIConfig(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Configuration for game API setup.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_game_api(app: fastapi.FastAPI, agent_class: type[haive.core.engine.agent.agent.Agent], api_config: GameAPIConfig | None = None, **kwargs) -> haive.dataflow.api.game_api.GameAPI

            Create a game API with the standardized system.

            :param app: FastAPI application instance
            :param agent_class: The game agent class
            :param api_config: API configuration
            :param \*\*kwargs: Additional arguments passed to GameAPI

            :returns: Configured GameAPI instance



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: app




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.api.setup import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

