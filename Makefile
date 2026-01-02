.PHONY: help install test lint format clean example

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:  ## Install dependencies
	uv sync --group test --group dev

test:  ## Run tests
	uv run pytest

test-cov:  ## Run tests with coverage
	uv run pytest --cov=prompt_optimizer --cov-report=html

lint:  ## Run linting
	uv run flake8 prompt_optimizer tests
	uv run mypy prompt_optimizer

format:  ## Format code
	uv run black prompt_optimizer tests example.py

format-check:  ## Check code formatting
	uv run black --check prompt_optimizer tests example.py

clean:  ## Clean up build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

example:  ## Run the example script
	uv run python example.py

build:  ## Build the package
	uv build