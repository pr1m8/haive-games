from haive.games.monopoly.game.types import PropertyType, SpecialSquareType


class Property:
    """Represents a property on the board."""

    def __init__(
        self,
        name: str,
        position: int,
        property_type: PropertyType,
        price: int = 0,
        color_group: str | None = None,
        rent_values: list[int] | None = None,
        mortgage_value: int | None = None,
        house_cost: int | None = None,
        special_type: SpecialSquareType | None = None,
    ):
        """  Init  .

Args:
    name: [TODO: Add description]
    position: [TODO: Add description]
    property_type: [TODO: Add description]
    price: [TODO: Add description]
    color_group: [TODO: Add description]
    rent_values: [TODO: Add description]
    mortgage_value: [TODO: Add description]
    house_cost: [TODO: Add description]
    special_type: [TODO: Add description]
"""
        self.name = name
        self.position = position
        self.property_type = property_type
        self.price = price
        self.color_group = color_group
        self.rent_values = rent_values or [0]
        self.mortgage_value = mortgage_value or (price // 2 if price else 0)
        self.house_cost = house_cost or 0
        self.special_type = special_type

        # State variables
        self.owner: int | None = None  # Player index who owns this property
        self.houses: int = 0  # Number of houses (5 = hotel)
        self.is_mortgaged: bool = False

    def get_rent(self, dice_roll: int | None = None) -> int:
        """Calculate the rent for this property.

        Args:
            dice_roll: The dice roll (needed for utilities)

        Returns:
            The rent amount

        """
        if self.is_mortgaged or self.owner is None:
            return 0

        if self.property_type == PropertyType.PROPERTY:
            # Regular property rent based on houses
            house_level = min(self.houses, len(self.rent_values) - 1)
            return self.rent_values[house_level]

        if self.property_type == PropertyType.RAILROAD:
            # Railroad rent based on how many railroads the owner has
            return self.rent_values[0]  # Will be updated by the game engine

        if self.property_type == PropertyType.UTILITY:
            # Utility rent based on dice roll and how many utilities the owner
            # has
            # Will be updated by the game engine
            multiplier = self.rent_values[0]
            return (
                dice_roll or 7
            ) * multiplier  # Default to 7 if no dice roll provided

        return 0
