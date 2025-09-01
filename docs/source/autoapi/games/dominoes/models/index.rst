games.dominoes.models
=====================

.. py:module:: games.dominoes.models

.. autoapi-nested-parse::

   Comprehensive data models for the Dominoes tile game.

   This module defines the complete set of data structures for traditional Dominoes
   gameplay, providing models for tile representation, game moves, strategic
   analysis, and game state management. The implementation supports standard
   double-six dominoes with traditional matching rules.

   Dominoes is a classic tile-matching game involving:
   - 28 tiles in a double-six set (0-0 through 6-6)
   - Line-building with matching endpoints
   - Strategic tile placement and blocking
   - Point-based scoring systems

   Key Models:
       DominoTile: Individual domino tile with two values
       DominoMove: Player's tile placement action
       DominoLinePosition: Position tracking on the domino line
       DominoAnalysis: Strategic evaluation for AI decision-making

   .. rubric:: Examples

   Working with tiles::

       from haive.games.dominoes.models import DominoTile

       # Create standard tiles
       double_six = DominoTile(left=6, right=6)
       mixed_tile = DominoTile(left=3, right=5)

       # Check tile properties
       assert double_six.is_double() == True
       assert mixed_tile.sum() == 8
       print(double_six)  # "[6|6]"

   Making moves::

       from haive.games.dominoes.models import DominoMove

       move = DominoMove(
           tile=DominoTile(left=4, right=2),
           position="left",
           player="player1"
       )

   Strategic analysis::

       analysis = DominoAnalysis(
           available_moves=5,
           blocking_potential=3,
           point_value=12,
           strategy="Control high-value tiles"
       )

   The models provide comprehensive tile management and strategic gameplay
   support for AI-driven dominoes implementation.



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/dominoes/models/DominoMove
   /autoapi/games/dominoes/models/DominoTile
   /autoapi/games/dominoes/models/DominoesAnalysis
   /autoapi/games/dominoes/models/DominoesPlayerDecision

.. autoapisummary::

   games.dominoes.models.DominoMove
   games.dominoes.models.DominoTile
   games.dominoes.models.DominoesAnalysis
   games.dominoes.models.DominoesPlayerDecision


