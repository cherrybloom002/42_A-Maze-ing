from mazegen import MazeGenerator
import sys


def main() -> None:
    width: int = 5
    height: int = 5
    entry: tuple[int, int] = (0, 0)
    exit_coords: tuple[int, int] = (width - 1, height - 1)

    maze: MazeGenerator = MazeGenerator(width, height, entry, exit_coords)
    maze.generate(start_x=0, start_y=0)

    hex_rows: list[str] = maze.export_hex_grid()
    for row in hex_rows:
        print(row)

    path: str = maze.solve(
        entry_x=entry[0],
        entry_y=entry[1],
        exit_x=exit_coords[0],
        exit_y=exit_coords[1],
    )
    print(f"\n{entry[0]}, {entry[1]} entrance")
    print(f"{exit_coords[0]}, {exit_coords[1]} exit")
    print(f"{path}")


if __name__ == "__main__":
    main()
