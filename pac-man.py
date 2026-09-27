import sys
from src import ParsingError, ParserClass, MazeLoader, MazeAdapter
from maze_generator.mazegenerator import MazeGenerator


def main() -> None:
    if len(sys.argv) != 2:
        raise ParsingError("Parsing Error: Missing/Extra arguments")
    parser = ParserClass(sys.argv[1])
    parser.validate(parser.load())
    maze_loader = MazeLoader(5, 5, 20, MazeGenerator=MazeGenerator)
    maze = maze_loader.generate_maze()
    print(maze)
    MazeAdapter(maze).create_cells()


if __name__ == "__main__":
    # try:
    main()
    # except ParsingError as e:
    #     print(f"Parsing error: {e}")
    # except Exception as e:
    #     print(e)
