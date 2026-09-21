class Entity:
    """Base class for game entities."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
