class Pellets:
    """Placeholder for pellet collection logic."""

    def __init__(self, total=0):
        self.total = total

    def consume(self, amount=1):
        self.total = max(0, self.total - amount)
        return self.total
