
:py:mod:`games.single_player.crossword_puzzle.base`
===================================================

.. py:module:: games.single_player.crossword_puzzle.base


Classes
-------

.. autoapisummary::

   games.single_player.crossword_puzzle.base.CrosswordCell
   games.single_player.crossword_puzzle.base.CrosswordClue
   games.single_player.crossword_puzzle.base.CrosswordGame
   games.single_player.crossword_puzzle.base.CrosswordMove
   games.single_player.crossword_puzzle.base.CrosswordTemplate
   games.single_player.crossword_puzzle.base.CrosswordWord
   games.single_player.crossword_puzzle.base.Direction


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CrosswordCell:

   .. graphviz::
      :align: center

      digraph inheritance_CrosswordCell {
        node [shape=record];
        "CrosswordCell" [label="CrosswordCell"];
        "game_framework_base.GridSpace[CrosswordLetter]" -> "CrosswordCell";
      }

.. autoclass:: games.single_player.crossword_puzzle.base.CrosswordCell
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CrosswordClue:

   .. graphviz::
      :align: center

      digraph inheritance_CrosswordClue {
        node [shape=record];
        "CrosswordClue" [label="CrosswordClue"];
        "pydantic.BaseModel" -> "CrosswordClue";
      }

.. autopydantic_model:: games.single_player.crossword_puzzle.base.CrosswordClue
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

   Inheritance diagram for CrosswordGame:

   .. graphviz::
      :align: center

      digraph inheritance_CrosswordGame {
        node [shape=record];
        "CrosswordGame" [label="CrosswordGame"];
        "game_framework_base.Game[game_framework_base.GridPosition, CrosswordLetter]" -> "CrosswordGame";
      }

.. autoclass:: games.single_player.crossword_puzzle.base.CrosswordGame
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CrosswordMove:

   .. graphviz::
      :align: center

      digraph inheritance_CrosswordMove {
        node [shape=record];
        "CrosswordMove" [label="CrosswordMove"];
        "pydantic.BaseModel" -> "CrosswordMove";
      }

.. autopydantic_model:: games.single_player.crossword_puzzle.base.CrosswordMove
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

   Inheritance diagram for CrosswordTemplate:

   .. graphviz::
      :align: center

      digraph inheritance_CrosswordTemplate {
        node [shape=record];
        "CrosswordTemplate" [label="CrosswordTemplate"];
        "pydantic.BaseModel" -> "CrosswordTemplate";
      }

.. autopydantic_model:: games.single_player.crossword_puzzle.base.CrosswordTemplate
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

   Inheritance diagram for CrosswordWord:

   .. graphviz::
      :align: center

      digraph inheritance_CrosswordWord {
        node [shape=record];
        "CrosswordWord" [label="CrosswordWord"];
        "pydantic.BaseModel" -> "CrosswordWord";
      }

.. autopydantic_model:: games.single_player.crossword_puzzle.base.CrosswordWord
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

   Inheritance diagram for Direction:

   .. graphviz::
      :align: center

      digraph inheritance_Direction {
        node [shape=record];
        "Direction" [label="Direction"];
        "str" -> "Direction";
        "enum.Enum" -> "Direction";
      }

.. autoclass:: games.single_player.crossword_puzzle.base.Direction
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **Direction** is an Enum defined in ``games.single_player.crossword_puzzle.base``.





.. rubric:: Related Links

.. autolink-examples:: games.single_player.crossword_puzzle.base
   :collapse:
   
.. autolink-skip:: next
