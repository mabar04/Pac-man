from src.entities.player import Player
from src.entities.ghost import Ghost
from src.gameplay.collision import collides


def test_collision_detection_matches_position():
    player = Player(4, 4)
    ghost = Ghost(4, 4)
    assert collides(player, ghost) is True

    ghost = Ghost(4, 5)
    assert collides(player, ghost) is False
