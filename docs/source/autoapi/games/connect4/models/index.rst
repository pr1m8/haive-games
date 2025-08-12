
:py:mod:`games.connect4.models`
===============================

.. py:module:: games.connect4.models

Connect4 game models module.

This module provides data models for the Connect4 game implementation, including:
    - Move validation and representation
    - Player decisions and analysis
    - Game state components
    - Structured output models for LLMs

.. rubric:: Example

>>> from haive.games.connect4.models import Connect4Move
>>>
>>> # Create and validate a move
>>> move = Connect4Move(
...     column=3,
...     explanation="Control the center column"
... )


.. autolink-examples:: games.connect4.models
   :collapse:

Classes
-------

.. autoapisummary::

   games.connect4.models.Connect4Analysis
   games.connect4.models.Connect4Move
   games.connect4.models.Connect4PlayerDecision


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Connect4Analysis:

   .. graphviz::
      :align: center

      digraph inheritance_Connect4Analysis {
        node [shape=record];
        "Connect4Analysis" [label="Connect4Analysis"];
        "pydantic.BaseModel" -> "Connect4Analysis";
      }

.. autopydantic_model:: games.connect4.models.Connect4Analysis
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

   Inheritance diagram for Connect4Move:

   .. graphviz::
      :align: center

      digraph inheritance_Connect4Move {
        node [shape=record];
        "Connect4Move" [label="Connect4Move"];
        "pydantic.BaseModel" -> "Connect4Move";
      }

.. autopydantic_model:: games.connect4.models.Connect4Move
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

   Inheritance diagram for Connect4PlayerDecision:

   .. graphviz::
      :align: center

      digraph inheritance_Connect4PlayerDecision {
        node [shape=record];
        "Connect4PlayerDecision" [label="Connect4PlayerDecision"];
        "pydantic.BaseModel" -> "Connect4PlayerDecision";
      }

.. autopydantic_model:: games.connect4.models.Connect4PlayerDecision
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





.. rubric:: Related Links

.. autolink-examples:: games.connect4.models
   :collapse:
   
.. autolink-skip:: next
