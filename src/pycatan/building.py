from typing import Set
from .player import Player
from .building_type import BuildingType
from .coords import Coords


class Building:
    """A building on the Catan board

    Attributes:
            owner (Player): The player who owns this building
            building_type (BuildingType): The type of building this is

    Args:
            owner (Player): The player who owns this building
            building_type (BuildingType): The type of building this is
    """

    def __init__(self, owner: Player, building_type: BuildingType):
        self.owner = owner
        self.building_type = building_type


class CornerBuilding(Building):
    """A building that is built on a corner.
    I.e. a settlement or a city

    Attributes:
            owner (Player): The player who owns this building
            building_type (BuildingType): The type of building this is
            coords (Coords): The coords the building is at

    Args:
            owner (Player): The player who owns this building
            building_type (BuildingType): The type of building this is
            coords (Coords): The coords the building is at
    """

    def __init__(self, owner: Player, building_type: BuildingType, coords: Coords):
        super().__init__(owner, building_type)
        self.coords = coords


class EdgeBuilding(Building):
    """A building that is built on an edge
    I.e. a road

    Attributes:
            owner (Player): The player who owns this building
            building_type (BuildingType): The type of building this is
            edge_coords (Set[Coords]): The coordinates of the two corners the building is connecting

    Args:
            owner (Player): The player who owns this building
            building_type (BuildingType): The type of building this is
            edge_coords (Set[Coords]): The coordinates of the two corners the building is connecting
    """

    def __init__(
        self, owner: Player, building_type: BuildingType, edge_coords: Set[Coords]
    ):
        super().__init__(owner, building_type)
        self.edge_coords = edge_coords
