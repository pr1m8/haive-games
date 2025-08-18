games.api.general_api
=====================

.. py:module:: games.api.general_api

General API system for all haive games.

from typing import Any This module provides a general-purpose API that automatically
discovers all available games and creates endpoints for each one, with OpenAPI
documentation and game selection capabilities.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">3 classes</span> • <span class="module-stat">1 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   General API system for all haive games.

   from typing import Any This module provides a general-purpose API that automatically
   discovers all available games and creates endpoints for each one, with OpenAPI
   documentation and game selection capabilities.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.api.general_api.logger

            
            

.. admonition:: Classes (3)
   :class: note

   .. autoapisummary::

      games.api.general_api.GameInfo
      games.api.general_api.GameSelectionRequest
      games.api.general_api.GeneralGameAPI

            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.api.general_api.create_general_game_api

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameInfo(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Information about an available game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: api_endpoints
               :type:  dict[str, str]
               :value: None



            .. py:attribute:: default_models
               :type:  dict[str, str]
               :value: None



            .. py:attribute:: description
               :type:  str
               :value: None



            .. py:attribute:: example_configs
               :type:  list[str]
               :value: None



            .. py:attribute:: game_id
               :type:  str
               :value: None



            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: players
               :type:  list[str]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameSelectionRequest(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Request for creating a new game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: config_mode
               :type:  str
               :value: None



            .. py:attribute:: example_config
               :type:  str | None
               :value: None



            .. py:attribute:: game_id
               :type:  str
               :value: None



            .. py:attribute:: game_settings
               :type:  dict[str, Any] | None
               :value: None



            .. py:attribute:: player_configs
               :type:  dict[str, Any] | None
               :value: None



            .. py:attribute:: player_models
               :type:  dict[str, str] | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GeneralGameAPI(app: fastapi.FastAPI, games_package: str = 'haive.games', route_prefix: str = '/api/games', ws_route_prefix: str = '/ws/games', exclude_games: list[str] | None = None)

            General API system that discovers and manages all games.

            Initialize the general game API.

            :param app: FastAPI application
            :param games_package: Package to scan for games
            :param route_prefix: Prefix for REST routes
            :param ws_route_prefix: Prefix for WebSocket routes
            :param exclude_games: List of game names to exclude


            .. py:method:: _create_game_api(game_id: str, game_info: dict[str, Any])

               Create API for a specific game.



            .. py:method:: _discover_games()

               Discover all available games in the package.



            .. py:method:: _import_game(game_name: str) -> dict[str, Any] | None

               Import a specific game and extract its information.



            .. py:method:: _register_routes()

               Register API routes for all discovered games.



            .. py:method:: _setup_openapi()

               Setup custom OpenAPI documentation.



            .. py:attribute:: app


            .. py:attribute:: discovered_games
               :type:  dict[str, dict[str, Any]]


            .. py:attribute:: exclude_games
               :value: ['go', 'among_us']



            .. py:attribute:: game_apis
               :type:  dict[str, haive.dataflow.api.game_api.GameAPI]


            .. py:attribute:: games_package
               :value: 'haive.games'



            .. py:attribute:: route_prefix
               :value: '/api/games'



            .. py:attribute:: ws_route_prefix
               :value: '/ws/games'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_general_game_api(app: fastapi.FastAPI | None = None, **kwargs) -> tuple[fastapi.FastAPI, GeneralGameAPI]

            Create a general game API that discovers all games.

            :param app: Optional FastAPI app (creates one if not provided)
            :param \*\*kwargs: Additional arguments for GeneralGameAPI

            :returns: Tuple of (FastAPI app, GeneralGameAPI instance)

            .. rubric:: Example

            >>> app, game_api = create_general_game_api()
            >>> # Now you have endpoints for all games!



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.api.general_api import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

