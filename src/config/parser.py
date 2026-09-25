import json
from pathlib import Path
from ..utils import ParsingError
from typing import Any, Dict


class ParserClass:
    """Loads JSON configuration files."""

    def __init__(self, file_path):

        self.file_path = Path(file_path)
        self.default_values = {
            "highscore_filename": "highscores.json",
            "level_array": [
                {"1": "(600, 700)"},
                {"2": "(200, 500)"},
                {"3": "(600, 700)"},
                {"4": "(600, 700)"},
                {"5": "(600, 700)"},
                {"6": "(600, 700)"}
            ],
            "lives": 3,
            "pacgum": 42,
            "points_per_pacgum": 10,
            "points_per_super_pacgum": 50,
            "points_per_ghost": 200,
            "seed": 42,
            "level_max_time": 90
        }

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
        self.values_validation(config, self.default_values)
        print(self.default_values)
        return self.default_values

    def values_validation(self, config: Dict[str, Any],
                          default: Dict[str, Any]) -> None:
        # base_level = 1
        # base_array = []
        for k, v in config.items():

            if k not in default.keys():
                continue

            if isinstance(v, str) and v.strip() == "":
                print(f"Missing value for '{k}' key")

            if isinstance(v, list) and v == []:
                print(f"Missing value for '{k}' key")

            # if k == "level_array":
            #     if not isinstance(v, list):
            #         print(f"{k} should be an array")
            #     for value in v:
            #         for key, v_tuple in value.items():
            #             try:
            #                 int_key = int(key)
            #                 if int_key != base_level:
            #                     print("The levels should start from 1 and go\
            #                         up by 1")
            #             except ValueError:
            #                 print(f"{key} should be an integer")
            #                 continue

            if (k == "lives" or k == "pacgum" or k == "points_per_pacgum"
                    or k == "points_per_super_pacgum"
                    or k == "points_per_ghost"):
                try:
                    int(v)
                    if (k == "points_per_super_pacgum" and
                            v <= self.default_values["points_per_pacgum"]):
                        print("Super gum points should be > than gum points")
                    else:
                        if v <= 0:
                            print(f"Value for {k} should be strict positive")
                        else:
                            self.default_values[k] = int(v)
                except ValueError:
                    print(f"Value of {k} should be an integer")

            if k == "level_max_time":
                try:
                    int(v)
                    if v <= 30:
                        print(f"Value for {k} should be >= 30 secondes")
                    else:
                        self.default_values[k] = v
                except ValueError:
                    print(f"Value for {k} should be an integer")
            if k == "seed":
                self.default_values[k] = v
