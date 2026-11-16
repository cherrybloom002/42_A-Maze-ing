from enum import Enum

class Direction(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"


class Cell:
    def __init__(self, x: int, y: int, is_entry: bool = False, is_exit: bool = False):
        self.x = x
        self.y = y
        self.walls: dict[Direction, bool] = {
            Direction.NORTH: True,
            Direction.EAST: True,
            Direction.SOUTH: True,
            Direction.WEST: True
        }
        self.visited: bool = False
        self.is_entry = is_entry
        self.is_exit = is_exit

    def _remove_wall(self, current_cell: Cell, neighbor_cell: Cell) -> None:
        if neighbor_cell.x > current_cell.x: # Il vicino e' piu' a destra (Est)
            current_cell.walls[Direction.EAST] = False
            neighbor_cell.walls[Direction.WEST] = False
        elif neighbor_cell.x < current_cell.x: # Il vicino e' piu' a sinistra (Ovest)
            current_cell.walls[Direction.WEST] = False
            neighbor_cell.walls[Direction.EAST] = False
        elif neighbor_cell.y > current_cell.y: # Il vicino e' piu' in basso (Sud)
            current_cell.walls[Direction.SOUTH] = False
            neighbor_cell.walls[Direction.NORTH] = False
        elif neighbor_cell.y < current_cell.y: # Il vicino e' piu' in alt (Nord)
            current_cell.walls[Direction.NORTH] = False
            neighbor_cell.walls[Direction.SOUTH] = False