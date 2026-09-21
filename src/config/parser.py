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

    def validate(self, config: Dict[str, Any]) -> bool:
        if not isinstance(config, dict):
            raise ParsingError("Configuration must be a dictionary.")
        return True
