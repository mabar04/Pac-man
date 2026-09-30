import sys
from src import ParsingError, ParserClass, MazeLoader, MazeAdapter
from maze_generator.mazegenerator import MazeGenerator
from src.ui.window import Window


def main() -> None:
    if len(sys.argv) != 2:
        raise ParsingError("Parsing Error: Missing/Extra arguments")
    parser = ParserClass(sys.argv[1])
    parser.validate(parser.load())
    maze_loader = MazeLoader(30, 30, 20, MazeGenerator=MazeGenerator)
    maze_loader.generate_maze()
    maze_adapter = MazeAdapter(maze_loader)
    maze_adapter.create_cells()
    window = Window()
    window.window_render(maze_adapter.cells, maze_adapter.get_all_walkable())


if __name__ == "__main__":
    # try:
    main()
    # except ParsingError as e:
    #     print(f"Parsing error: {e}")
    # except Exception as e:
    #     print(e)
