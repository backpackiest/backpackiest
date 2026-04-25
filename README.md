# backpackiest

Python development environment.

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Setup

### With uv (recommended)

```bash
uv sync --all-extras --dev
```

This creates `.venv/` and installs runtime + dev dependencies.

### With pip

```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Common commands

```bash
# Run the app
uv run python -m backpackiest.main

# Run tests
uv run pytest

# Lint
uv run ruff check .

# Format
uv run ruff format .

# Type check
uv run mypy
```

## Project layout

```
.
├── src/backpackiest/    # package source
├── tests/               # pytest tests
├── pyproject.toml       # project + tool config
└── .github/workflows/   # CI
```
