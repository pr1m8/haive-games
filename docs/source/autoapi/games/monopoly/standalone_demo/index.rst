games.monopoly.standalone_demo
==============================

.. py:module:: games.monopoly.standalone_demo

.. autoapi-nested-parse::

   Standalone Monopoly demo with minimal dependencies.

   This script provides a self-contained demonstration of the Monopoly game
   without relying on external dependencies like langchain.

   Usage:
       python standalone_demo.py


   .. autolink-examples:: games.monopoly.standalone_demo
      :collapse:


Attributes
----------

.. autoapisummary::

   games.monopoly.standalone_demo.BOARD_PROPERTIES


Classes
-------

.. autoapisummary::

   games.monopoly.standalone_demo.Color
   games.monopoly.standalone_demo.DiceRoll
   games.monopoly.standalone_demo.GameEvent
   games.monopoly.standalone_demo.GameState
   games.monopoly.standalone_demo.Player
   games.monopoly.standalone_demo.Property
   games.monopoly.standalone_demo.PropertyColor
   games.monopoly.standalone_demo.PropertyType


Functions
---------

.. autoapisummary::

   games.monopoly.standalone_demo.calculate_rent
   games.monopoly.standalone_demo.create_board
   games.monopoly.standalone_demo.create_players
   games.monopoly.standalone_demo.get_property_at_position
   games.monopoly.standalone_demo.handle_property_landing
   games.monopoly.standalone_demo.move_player
   games.monopoly.standalone_demo.print_divider
   games.monopoly.standalone_demo.print_player_status
   games.monopoly.standalone_demo.print_property
   games.monopoly.standalone_demo.print_recent_events
   games.monopoly.standalone_demo.roll_dice
   games.monopoly.standalone_demo.run_demo


Module Contents
---------------

.. py:class:: Color

   .. py:attribute:: BLUE
      :value: '\x1b[94m'



   .. py:attribute:: BOLD
      :value: '\x1b[1m'



   .. py:attribute:: CYAN
      :value: '\x1b[96m'



   .. py:attribute:: GREEN
      :value: '\x1b[92m'



   .. py:attribute:: MAGENTA
      :value: '\x1b[95m'



   .. py:attribute:: RED
      :value: '\x1b[91m'



   .. py:attribute:: RESET
      :value: '\x1b[0m'



   .. py:attribute:: YELLOW
      :value: '\x1b[93m'



.. py:class:: DiceRoll

   .. py:attribute:: die1
      :type:  int


   .. py:attribute:: die2
      :type:  int


   .. py:property:: is_doubles
      :type: bool



   .. py:property:: total
      :type: int



.. py:class:: GameEvent

   .. py:attribute:: description
      :type:  str


   .. py:attribute:: details
      :type:  dict


   .. py:attribute:: event_type
      :type:  str


   .. py:attribute:: money_change
      :type:  int
      :value: 0



   .. py:attribute:: player
      :type:  str


   .. py:attribute:: property_involved
      :type:  str | None
      :value: None



.. py:class:: GameState

   .. py:method:: next_player() -> None


   .. py:property:: active_players
      :type: list[Player]



   .. py:property:: current_player
      :type: Player



   .. py:attribute:: current_player_index
      :type:  int
      :value: 0



   .. py:attribute:: game_events
      :type:  list[GameEvent]
      :value: []



   .. py:attribute:: last_roll
      :type:  DiceRoll | None
      :value: None



   .. py:attribute:: players
      :type:  list[Player]


   .. py:attribute:: properties
      :type:  dict[str, Property]


   .. py:attribute:: turn_number
      :type:  int
      :value: 1



.. py:class:: Player

   .. py:method:: can_afford(amount: int) -> bool


   .. py:attribute:: bankrupt
      :type:  bool
      :value: False



   .. py:attribute:: doubles_count
      :type:  int
      :value: 0



   .. py:attribute:: in_jail
      :type:  bool
      :value: False



   .. py:attribute:: jail_cards
      :type:  int
      :value: 0



   .. py:attribute:: jail_turns
      :type:  int
      :value: 0



   .. py:attribute:: money
      :type:  int
      :value: 1500



   .. py:attribute:: name
      :type:  str


   .. py:attribute:: position
      :type:  int
      :value: 0



   .. py:attribute:: properties
      :type:  list[str]
      :value: []



.. py:class:: Property

   .. py:attribute:: color
      :type:  PropertyColor


   .. py:attribute:: hotel
      :type:  bool
      :value: False



   .. py:attribute:: house_cost
      :type:  int
      :value: 0



   .. py:attribute:: houses
      :type:  int
      :value: 0



   .. py:attribute:: mortgage_value
      :type:  int
      :value: 0



   .. py:attribute:: mortgaged
      :type:  bool
      :value: False



   .. py:attribute:: name
      :type:  str


   .. py:attribute:: owner
      :type:  str | None
      :value: None



   .. py:attribute:: position
      :type:  int


   .. py:attribute:: price
      :type:  int


   .. py:attribute:: property_type
      :type:  PropertyType


   .. py:attribute:: rent
      :type:  list[int]


.. py:class:: PropertyColor

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   str(object='') -> str
   str(bytes_or_buffer[, encoding[, errors]]) -> str

   Create a new string object from the given object. If encoding or
   errors is specified, then the object must expose a data buffer
   that will be decoded using the given encoding and error handler.
   Otherwise, returns the result of object.__str__() (if defined)
   or repr(object).
   encoding defaults to sys.getdefaultencoding().
   errors defaults to 'strict'.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PropertyColor
      :collapse:

   .. py:attribute:: BROWN
      :value: 'brown'



   .. py:attribute:: DARK_BLUE
      :value: 'dark_blue'



   .. py:attribute:: GREEN
      :value: 'green'



   .. py:attribute:: LIGHT_BLUE
      :value: 'light_blue'



   .. py:attribute:: ORANGE
      :value: 'orange'



   .. py:attribute:: PINK
      :value: 'pink'



   .. py:attribute:: RAILROAD
      :value: 'railroad'



   .. py:attribute:: RED
      :value: 'red'



   .. py:attribute:: SPECIAL
      :value: 'special'



   .. py:attribute:: UTILITY
      :value: 'utility'



   .. py:attribute:: YELLOW
      :value: 'yellow'



.. py:class:: PropertyType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   str(object='') -> str
   str(bytes_or_buffer[, encoding[, errors]]) -> str

   Create a new string object from the given object. If encoding or
   errors is specified, then the object must expose a data buffer
   that will be decoded using the given encoding and error handler.
   Otherwise, returns the result of object.__str__() (if defined)
   or repr(object).
   encoding defaults to sys.getdefaultencoding().
   errors defaults to 'strict'.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PropertyType
      :collapse:

   .. py:attribute:: RAILROAD
      :value: 'railroad'



   .. py:attribute:: SPECIAL
      :value: 'special'



   .. py:attribute:: STREET
      :value: 'street'



   .. py:attribute:: UTILITY
      :value: 'utility'



.. py:function:: calculate_rent(property_obj: Property, state: GameState, dice_roll: int | None = None) -> int

   Calculate rent for a property.


   .. autolink-examples:: calculate_rent
      :collapse:

.. py:function:: create_board() -> dict[str, Property]

   Create the initial board with all properties.


   .. autolink-examples:: create_board
      :collapse:

.. py:function:: create_players(player_names: list[str]) -> list[Player]

   Create initial players.


   .. autolink-examples:: create_players
      :collapse:

.. py:function:: get_property_at_position(position: int) -> dict | None

   Get property information at a board position.


   .. autolink-examples:: get_property_at_position
      :collapse:

.. py:function:: handle_property_landing(state: GameState, position: int) -> list[GameEvent]

   Handle a player landing on a property.


   .. autolink-examples:: handle_property_landing
      :collapse:

.. py:function:: move_player(player: Player, dice_roll: DiceRoll) -> tuple[int, bool]

   Move a player based on dice roll.


   .. autolink-examples:: move_player
      :collapse:

.. py:function:: print_divider()

   Print a divider line.


   .. autolink-examples:: print_divider
      :collapse:

.. py:function:: print_player_status(state: GameState)

   Print current status of all players.


   .. autolink-examples:: print_player_status
      :collapse:

.. py:function:: print_property(property_obj: Property)

   Print property details.


   .. autolink-examples:: print_property
      :collapse:

.. py:function:: print_recent_events(events: list[GameEvent], count: int = 5)

   Print recent game events.


   .. autolink-examples:: print_recent_events
      :collapse:

.. py:function:: roll_dice() -> DiceRoll

   Roll two dice.


   .. autolink-examples:: roll_dice
      :collapse:

.. py:function:: run_demo(turns: int = 10)

   Run a simple Monopoly game demo.


   .. autolink-examples:: run_demo
      :collapse:

.. py:data:: BOARD_PROPERTIES

