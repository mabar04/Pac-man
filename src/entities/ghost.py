from src.entities.entity import Entity


class Ghost(Entity):
    """Ghost entity placeholder."""

    def __init__(self, x=0, y=0, color="red"):
        super().__init__(x, y)
        self.color = color
        self.scared = False

    def frighten(self):
        self.scared = True

    def recover(self):
        self.scared = False
