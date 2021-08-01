from .resource import Resource
from .building import CornerBuilding
from .hex import Hex


class RollYieldSource:
    """The source of some resources a player got after rolling the dice

    Attributes:
            resouce: The resouce earned,
            amount: The amount of the resource earned
            building: The building that earned the resources
            hex: The hex that the resources came from
    """

    def __init__(
        self, resource: Resource, amount: int, building: CornerBuilding, hex: Hex
    ):
        self.building = building
        self.hex = hex


class RollYield:
    """A utility class to represent what each player gets from a roll of the dice
    Contains information about where the resources came from as well

    Attributes:
            total_yield (Dict[Resource, int]): The total yield from this dice roll
            all_yields (Set[RollYieldSource]): The sources where the resources came from
    """

    def __init__(self):
        self.total_yield = {r: 0 for r in Resource}
        self.all_yields = set()

    def add_yield(
        self, resource: Resource, amount: int, source: RollYieldSource
    ) -> None:
        self.total_yield[resource] += amount
        self.all_yields.add(RollYieldSource)