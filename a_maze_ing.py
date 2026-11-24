import parser
from mazegen import Cell, Direction, MazeGenerator
from mazegen.cell import _remove_wall


WEIGHT: dict[Direction, int] = {
    Direction.NORTH: 1,
    Direction.EAST: 2,
    Direction.SOUTH: 4,
    Direction.WEST: 8
}


def cell_to_number(cell: Cell) -> int:
    """Return the wall bitmask of a cell (0 to 15)

    Args:
        cell: the cell to encode.

    Returns:
        The sum of the weights of every closed wall.
    """
    total = 0

    for direction, is_closed in cell.walls.items():
        if is_closed:
            total += WEIGHT[direction]
    return total


def row_to_string(row: list[Cell]) -> str:
    """Test the row encoding."""
    text = ""

    for cell in row:
        number = cell_to_number(cell)
        char = format(number, "x")
        text += char
    return text


def grid_to_hex(grid: list[list[Cell]]) -> list[str]:
    """Convert each row into a string"""
    lines: list[str] = []
    for row in grid:
        lines.append(row_to_string(row))
    return lines


def save_output(filename: str, lines: list[str]) -> None:
    """Write output lines on file"""
    try:
        with open(filename, "w") as f:
            for line in lines:
                f.write(line + "\n")
    except OSError as e:
        print(f"Error: cannot write {filename}: ")


def build_output_lines(
    grid: list[list[Cell]],
    entry: tuple[int, int],
    exit_point: tuple[int, int],
    path: str,
) -> list[str]:
    lines = grid_to_hex(grid)
    lines.append("")
    entry_x, entry_y = entry
    lines.append(f"{entry_x}, {entry_y}")
    exit_x, exit_y = exit_point
    lines.append(f"{exit_x}, {exit_y}")
    lines.append(path)
    return lines


def main() -> None:
    cfg = parser.couples
    gen = MazeGenerator(
        cfg["WIDTH"], cfg["HEIGHT"], cfg["ENTRY"], cfg["EXIT"]
    )
    _remove_wall(gen.grid[0][0], gen.grid[0][1])   # opens east of (0,0)
    _remove_wall(gen.grid[0][1], gen.grid[1][1])   # opens south of (1,0)
    lines = build_output_lines(gen.grid, cfg["ENTRY"], cfg["EXIT"], "")
    save_output(cfg["OUTPUT_FILE"], lines)


if __name__ == "__main__":
    main()
