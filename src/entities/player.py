from src.entities.entity import Entity


class Player(Entity):
    """Player-controlled character."""

    def __init__(self, x=0, y=0, lives=3):
        super().__init__(x, y)
        self.lives = lives
        self.direction = (0, 0)

    def set_direction(self, dx, dy):
        self.direction = (dx, dy)
