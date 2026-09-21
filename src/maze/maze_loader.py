from src.maze.maze import Maze


class MazeLoader:
    """Loads maze definitions from a list of strings."""

    def load(self, rows):
        return Maze(rows)
