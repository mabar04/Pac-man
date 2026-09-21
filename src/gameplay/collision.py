def collides(a, b):
    """Return True when two entities share the same coordinates."""
    return a.x == b.x and a.y == b.y
