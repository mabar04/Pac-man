from src.gameplay.scoring import score_pellet


def test_score_pellet_increases_total():
    assert score_pellet(30, 10) == 40
    assert score_pellet(30) == 40
