from src.entities.ghost import Ghost


def test_ghost_can_be_frightened():
    ghost = Ghost(5, 6, color="blue")
    ghost.frighten()
    assert ghost.scared is True

    ghost.recover()
    assert ghost.scared is False
    assert ghost.color == "blue"
