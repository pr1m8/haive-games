games.api.general_api
=====================

.. py:module:: games.api.general_api

.. autoapi-nested-parse::

   General API system for all haive games.

   from typing import Any This module provides a general-purpose API that automatically
   discovers all available games and creates endpoints for each one, with OpenAPI
   documentation and game selection capabilities.



Attributes
----------

.. autoapisummary::

   games.api.general_api.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/api/general_api/GameInfo
   /autoapi/games/api/general_api/GameSelectionRequest
   /autoapi/games/api/general_api/GeneralGameAPI

.. autoapisummary::

   games.api.general_api.GameInfo
   games.api.general_api.GameSelectionRequest
   games.api.general_api.GeneralGameAPI


Functions
---------

.. autoapisummary::

   games.api.general_api.create_general_game_api


Module Contents
---------------

.. py:function:: create_general_game_api(app: fastapi.FastAPI | None = None, **kwargs) -> tuple[fastapi.FastAPI, GeneralGameAPI]

   Create a general game API that discovers all games.

   :param app: Optional FastAPI app (creates one if not provided)
   :param \*\*kwargs: Additional arguments for GeneralGameAPI

   :returns: Tuple of (FastAPI app, GeneralGameAPI instance)

   .. rubric:: Examples

   >>> app, game_api = create_general_game_api()
   >>> # Now you have endpoints for all games!


.. py:data:: logger

