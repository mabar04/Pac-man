from src.maze.maze_loader import MazeLoader


def test_maze_loader_creates_maze_object():
    rows = [
        "######",
        "#....#",
        "#.#..#",
        "######",
    ]

    maze = MazeLoader().load(rows)
    assert maze.height() == 4
    assert maze.width() == 6
