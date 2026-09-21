class Maze:
    """Maze data placeholder."""

    def __init__(self, grid=None):
        self.grid = grid or []

    def width(self):
        return len(self.grid[0]) if self.grid else 0

    def height(self):
        return len(self.grid)
