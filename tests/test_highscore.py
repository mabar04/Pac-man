from src.highscore.storage import HighScoreStorage


def test_highscore_storage_round_trip(tmp_path):
    path = tmp_path / "scores.json"
    storage = HighScoreStorage(path)
    payload = [{"player": "Alice", "score": 120}]

    storage.save(payload)
    assert storage.load() == payload
