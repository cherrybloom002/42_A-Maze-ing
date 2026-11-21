from mazegen.cell import Cell, Direction

class MazeGenerator:
    def __init__(self, width: int, height: int, entry: Tuple[int, int], exit: Tuple[int, int]):
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.grid: list[list[Cell]] = []
        
        self._initialize_grid()

    def _initialize_grid(self) -> None:
        for y in range(self.height):
            row: list[Cell] = []
            for x in range(self.width):
                is_entry = (x, y) == self.entry
                is_exit = (x, y) == self.exit
                
                cell = Cell(x, y, is_entry=is_entry, is_exit=is_exit)
                row.append(cell)
            self.grid.append(row)

    def _get_valid_neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        neighbors: list[tuple[int, int]] = []
        directions: list[tuple[int, int]] = [
            (0, -1),  # North
            (1, 0),   # East
            (0, 1),   # South
            (-1, 0)   # West
        ]
        
        for dx, dy in directions:
            neighbor_x: int = x + dx 
            neighbor_y: int = y + dy
            if 0 <= neighbor_x < self.width and 0 <= neighbor_y < self.height:
                if not self.grid[neighbor_y][neighbor_x].visited:
                    neighbors.append((neighbor_x, neighbor_y))     
        return neighbors

    def generate(self, start_x: int = 0, start_y: int = 0) -> None:
        start_cell: Cell = self.grid[start_y][start_x]
        start_cell.visited = True
        stack: list[Cell] = [start_cell]

        while stack:
            current_cell: Cell = stack[-1]
            valid_neighbors: list[tuple[int, int]] = self._get_valid_neighbors(
                current_cell.x, current_cell.y
            )

        if valid_neighbors:
            chosen_coords: tuple[int, int] = random.choice(valid_neighbors)
            next_x: int = chosen_coords[0]
            next_y: int = chosen_coords[1]