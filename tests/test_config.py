from src.config.config_loader import ConfigLoader
from src.config.config_validator import ConfigValidator


def test_config_loader_reads_json():
    loader = ConfigLoader("config/config.json")
    config = loader.load()
    assert "window" in config
    assert "game" in config


def test_config_validator_accepts_mapping():
    validator = ConfigValidator()
    assert validator.validate({"window": {"width": 800}}) is True
