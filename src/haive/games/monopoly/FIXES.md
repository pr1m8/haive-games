# Monopoly Game Fixes

This document outlines the fixes made to the Monopoly game module.

## Issues Fixed

1. **Missing Properties in the Board**:
   - The `create_board()` function in `utils.py` was only creating Property objects for non-SPECIAL property types
   - This caused "Property not found" errors when players landed on properties like "Vermont Avenue"
   - Fixed by creating Property objects for ALL property types, including special ones

2. **Player List Update Errors**:
   - The `move_player_node` function in `game_agent.py` was failing when the player list was empty
   - Added proper bounds checking and error handling to prevent IndexError exceptions
   - Safely updates the player state in the players list with proper validation

3. **Property Type Checking**:
   - Fixed attribute references in the simple demo (`property_type` vs `is_property`)
   - Made property type checking more robust using enum values

4. **Proper Error Recovery**:
   - Added recovery code in `handle_property_space` function to create missing properties on the fly
   - This allows the game to continue even if there are issues with the property initialization

## New Components

1. **Standalone Demo**:
   - Created a simplified, standalone demo that shows core functionality
   - Doesn't rely on external dependencies like langchain or langgraph
   - Demonstrates property purchases, rent payments, and player movement

2. **Simple Demo**:
   - Created a simple demo using the full Monopoly game code but without the UI complexity
   - Shows the core game mechanics working properly

## Key Changes

### 1. Fixed Property Creation in `utils.py`

```python
def create_board() -> dict[str, Property]:
    """Create the initial board with all properties."""
    properties = {}

    for position, prop_data in BOARD_PROPERTIES.items():
        # Create ALL properties, including special ones
        property_type = PropertyType(prop_data["type"])

        # For regular properties, include all details
        if property_type != PropertyType.SPECIAL:
            properties[prop_data["name"]] = Property(...)
        # For special properties, create minimal Property objects
        else:
            properties[prop_data["name"]] = Property(...)

    return properties
```

### 2. Fixed Player Updates in `game_agent.py`

```python
def move_player_node(self, state: MonopolyState) -> Command:
    # Create event update
    event_update = {"game_events": [event]}

    # Check if players list is valid before trying to update
    if monopoly_state.players and 0 <= monopoly_state.current_player_index < len(monopoly_state.players):
        # Update the player in the players list using safe update_player method
        updated_state = monopoly_state.update_player(monopoly_state.current_player_index, current_player)
        event_update["players"] = updated_state.players
    else:
        # Handle the empty players list case
        print("⚠️ Warning: Cannot update player - players list is empty or index out of bounds")
        # Initialize players list if needed
        if not monopoly_state.players:
            event_update["players"] = [current_player]

    return Command(update=event_update)
```

### 3. Added Recovery Code in `handle_property_space`

```python
def handle_property_space(self, state: MonopolyState, property_name: str) -> Command:
    # ...
    if not property_obj:
        # Handle the case where property isn't found - log error but don't crash
        print(f"⚠️ WARNING: Property not found: {property_name}")
        print(f"⚠️ Available properties: {list(state.properties.keys())}")

        # Try to get property info from utils.BOARD_PROPERTIES
        from haive.games.monopoly.utils import BOARD_PROPERTIES
        position = current_player.position
        position_data = BOARD_PROPERTIES.get(position)

        if position_data and position_data["name"] == property_name:
            print(f"🔄 Creating missing property: {property_name}")
            # Create the property on the fly based on board data
            property_obj = Property(...)

            # Add to the state and continue
            updated_properties = state.properties.copy()
            updated_properties[property_name] = property_obj

            # Return event that adds the property to state
            return Command(
                update={
                    "properties": updated_properties,
                    "game_events": [...]
                }
            )
```

## Testing

The fixes were tested using:

1. A standalone demo that shows the core functionality works correctly
2. A simple demo that uses the full Monopoly game code
3. Verified property creation, especially for "Vermont Avenue"
4. Tested player movement and property landing
5. Tested rent payments and ownership changes

All tests show that the game is now working correctly.
