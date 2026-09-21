class PacManError(Exception):
    """Base exception for game-related errors."""


class InvalidConfigError(PacManError):
    """Raised when configuration data is invalid."""


class MazeLoadError(PacManError):
    """Raised when a maze cannot be read."""


class ParsingError(Exception):
    pass
