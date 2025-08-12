
:py:mod:`games.api.general_api`
===============================

.. py:module:: games.api.general_api

General API system for all haive games.

from typing import Any This module provides a general-purpose API that automatically
discovers all available games and creates endpoints for each one, with OpenAPI
documentation and game selection capabilities.


.. autolink-examples:: games.api.general_api
   :collapse:

Classes
-------

.. autoapisummary::

   games.api.general_api.GameInfo
   games.api.general_api.GameSelectionRequest
   games.api.general_api.GeneralGameAPI


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameInfo:

   .. graphviz::
      :align: center

      digraph inheritance_GameInfo {
        node [shape=record];
        "GameInfo" [label="GameInfo"];
        "pydantic.BaseModel" -> "GameInfo";
      }

.. autopydantic_model:: games.api.general_api.GameInfo
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameSelectionRequest:

   .. graphviz::
      :align: center

      digraph inheritance_GameSelectionRequest {
        node [shape=record];
        "GameSelectionRequest" [label="GameSelectionRequest"];
        "pydantic.BaseModel" -> "GameSelectionRequest";
      }

.. autopydantic_model:: games.api.general_api.GameSelectionRequest
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GeneralGameAPI:

   .. graphviz::
      :align: center

      digraph inheritance_GeneralGameAPI {
        node [shape=record];
        "GeneralGameAPI" [label="GeneralGameAPI"];
      }

.. autoclass:: games.api.general_api.GeneralGameAPI
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.api.general_api.create_general_game_api

.. py:function:: create_general_game_api(app: fastapi.FastAPI | None = None, **kwargs) -> tuple[fastapi.FastAPI, GeneralGameAPI]

   Create a general game API that discovers all games.

   :param app: Optional FastAPI app (creates one if not provided)
   :param \*\*kwargs: Additional arguments for GeneralGameAPI

   :returns: Tuple of (FastAPI app, GeneralGameAPI instance)

   .. rubric:: Example

   >>> app, game_api = create_general_game_api()
   >>> # Now you have endpoints for all games!


   .. autolink-examples:: create_general_game_api
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.api.general_api
   :collapse:
   
.. autolink-skip:: next
