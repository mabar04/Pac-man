from src.entities.player import Player


def test_player_tracks_direction():
    player = Player(2, 3, lives=4)
    player.set_direction(1, 0)
    assert player.x == 2
    assert player.y == 3
    assert player.lives == 4
    assert player.direction == (1, 0)
