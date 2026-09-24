import json
from pathlib import Path
from ..utils import ParsingError
from typing import Any, Dict


class ParserClass:
    """Loads JSON configuration files."""

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def load(self):
        try:
            if not self.file_path.is_file():
                raise ParsingError("The path entered is not for a file")
            if not self.file_path.suffix == ".json":
                raise ParsingError("File is not an json")
            with self.file_path.open("r", encoding="utf-8") as handle:
                json_object = ""
                for line in handle.readlines():
                    line_array = line.split("#")
                    json_object = json_object + line_array[0]
                try:
                    last_json = json.loads(json_object)
                except json.decoder.JSONDecodeError:
                    raise ParsingError("invalid JSON syntax")
                return last_json
        except FileNotFoundError:
            raise ParsingError("File not found")
        except PermissionError:
            raise ParsingError("Permission not given error")
        except ParsingError as e:
            raise ParsingError(e)

    def validate(self, config: Dict[str, Any]) -> dict[str, Any]:
        default_values = {
            "highscore_filename": "highscores.json",
            "level_array": [0, 1, 2, 3, 4, 5],
            "width": 500,
            "height": 500,
            "lives": 3,
            "pacgum": 42,
            "points_per_pacgum": 10,
            "points_per_super_pacgum": 50,
            "points_per_ghost": 200,
            "seed": 42,
            "level_max_time": 90
        }
        self.values_validation(config, default_values)
        print(default_values)
        return default_values

    def values_validation(self, config: Dict[str, Any],
                          default: Dict[str, Any]) -> None:
        for k, v in config.items():
            if k not in default.keys():
                continue
            if isinstance(v, str) and v.strip() == "":
                print(f"Missing value for '{k}' key")
            if isinstance(v, list) and v == []:
                print(f"Missing value for '{k}' key")
            if k == "level_array":
                if not isinstance(v, []):
                    print(f"{k} should be an array")
                for index, value in enumerate():
                    try:
                        int(value)
                    except ValueError:
                        print(f"values inside {k} should be an int")
