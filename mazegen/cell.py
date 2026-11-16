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
        self.walls = {
            Direction.NORTH: True,
            Direction.EAST: True,
            Direction.SOUTH: True,
            Direction.WEST: True
        }
        self.visited = False
        self.is_entry = is_entry
        self.is_exit = is_exit