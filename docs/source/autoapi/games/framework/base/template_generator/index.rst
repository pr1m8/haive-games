
:py:mod:`games.framework.base.template_generator`
=================================================

.. py:module:: games.framework.base.template_generator

Template generator for game agents (EXPERIMENTAL).

This experimental module provides a template generator for creating new game
implementations. It automates the creation of boilerplate code and ensures
consistency across different game implementations.

.. warning::

   This module is experimental and its API may change without notice.
   Use with caution in production environments.

.. rubric:: Example

>>> # Create templates for a new chess game
>>> generator = GameTemplateGenerator(
...     game_name="Chess",
...     player1_name="white",
...     player2_name="black",
...     enable_analysis=True
... )
>>> generator.generate_templates()

Typical usage:
    - Initialize the generator with game details
    - Generate all template files at once
    - Customize the generated code for your specific game


.. autolink-examples:: games.framework.base.template_generator
   :collapse:

Classes
-------

.. autoapisummary::

   games.framework.base.template_generator.GameTemplateGenerator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameTemplateGenerator:

   .. graphviz::
      :align: center

      digraph inheritance_GameTemplateGenerator {
        node [shape=record];
        "GameTemplateGenerator" [label="GameTemplateGenerator"];
      }

.. autoclass:: games.framework.base.template_generator.GameTemplateGenerator
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.framework.base.template_generator
   :collapse:
   
.. autolink-skip:: next
