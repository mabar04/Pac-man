PYTHON ?= python3
APP = pac-man.py
CONFIG = config/config.json

.PHONY: run test lint clean

run:
	$(PYTHON) $(APP) $(CONFIG)

test:
	pytest -q

lint:
	python -m compileall src tests

clean:
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
