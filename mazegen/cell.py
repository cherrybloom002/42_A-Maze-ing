from enum import Enum


class Direction(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"


class Cell:
    def __init__(
            self,
            x: int,
            y: int,
            is_entry: bool = False,
            is_exit: bool = False
    ):
        self.x = x
        self.y = y
        self.walls: dict[Direction, bool] = {
            Direction.NORTH: True,
            Direction.EAST: True,
            Direction.SOUTH: True,
            Direction.WEST: True
        }
        self.visited: bool = False
        self.is_entry: bool = is_entry
        self.is_exit: bool = is_exit

    def remove_wall(self, neighbor_cell: "Cell") -> None:
        if neighbor_cell.x > self.x: # Il vicino e' piu' a destra (Est)
            self.walls[Direction.EAST] = False
            neighbor_cell.walls[Direction.WEST] = False
        elif neighbor_cell.x < self.x: # Il vicino e' piu' a sinistra (Ovest)
            self.walls[Direction.WEST] = False
            neighbor_cell.walls[Direction.EAST] = False
        elif neighbor_cell.y > self.y: # Il vicino e' piu' in basso (Sud)
            self.walls[Direction.SOUTH] = False
            neighbor_cell.walls[Direction.NORTH] = False
        elif neighbor_cell.y < self.y: # Il vicino e' piu' in alt (Nord)
            self.walls[Direction.NORTH] = False
            neighbor_cell.walls[Direction.SOUTH] = False

    def to_hex(self) -> str:
        value: int = 0
        if self.walls[Direction.NORTH]:
            value += 1
        if self.walls[Direction.EAST]:
            value += 2
        if self.walls[Direction.SOUTH]:
            value += 4
        if self.walls[Direction.WEST]:
            value += 8
        return f"{value:X}"
