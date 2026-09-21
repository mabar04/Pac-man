class MazeAdapter:
    """Adapter for converting maze representations."""

    def adapt(self, grid):
        return [list(row) for row in grid]
