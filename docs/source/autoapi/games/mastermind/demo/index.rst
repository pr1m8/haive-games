
:py:mod:`games.mastermind.demo`
===============================

.. py:module:: games.mastermind.demo

Standalone demo for the Mastermind game with Rich UI.

This script demonstrates the Mastermind game without requiring the full Haive framework.


.. autolink-examples:: games.mastermind.demo
   :collapse:

Classes
-------

.. autoapisummary::

   games.mastermind.demo.ColorCode
   games.mastermind.demo.Feedback
   games.mastermind.demo.MastermindState
   games.mastermind.demo.MastermindUI


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ColorCode:

   .. graphviz::
      :align: center

      digraph inheritance_ColorCode {
        node [shape=record];
        "ColorCode" [label="ColorCode"];
        "pydantic.BaseModel" -> "ColorCode";
      }

.. autopydantic_model:: games.mastermind.demo.ColorCode
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

   Inheritance diagram for Feedback:

   .. graphviz::
      :align: center

      digraph inheritance_Feedback {
        node [shape=record];
        "Feedback" [label="Feedback"];
        "pydantic.BaseModel" -> "Feedback";
      }

.. autopydantic_model:: games.mastermind.demo.Feedback
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

   Inheritance diagram for MastermindState:

   .. graphviz::
      :align: center

      digraph inheritance_MastermindState {
        node [shape=record];
        "MastermindState" [label="MastermindState"];
        "pydantic.BaseModel" -> "MastermindState";
      }

.. autopydantic_model:: games.mastermind.demo.MastermindState
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

   Inheritance diagram for MastermindUI:

   .. graphviz::
      :align: center

      digraph inheritance_MastermindUI {
        node [shape=record];
        "MastermindUI" [label="MastermindUI"];
      }

.. autoclass:: games.mastermind.demo.MastermindUI
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.mastermind.demo.calculate_feedback
   games.mastermind.demo.main

.. py:function:: calculate_feedback(secret_code: list[str], guess: list[str]) -> dict[str, int]

   Calculate feedback for a guess.


   .. autolink-examples:: calculate_feedback
      :collapse:

.. py:function:: main()

   Run the Mastermind game.


   .. autolink-examples:: main
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.mastermind.demo
   :collapse:
   
.. autolink-skip:: next
