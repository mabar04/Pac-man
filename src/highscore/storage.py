import json
from pathlib import Path


class HighScoreStorage:
    """Stores high scores in a JSON file."""

    def __init__(self, path="highscores/highscores.json"):
        self.path = Path(path)

    def save(self, entries):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as handle:
            json.dump(entries, handle)

    def load(self):
        if not self.path.exists():
            return []
        with self.path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
