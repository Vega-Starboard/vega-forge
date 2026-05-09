# Vega Forge

Vega Forge generates starter projects from structured JSON specs. The MVP is deterministic, local-only, and requires no model call.

## Usage

```bash
PYTHONPATH=src python3 -m vega_forge preview --spec examples/specs/static-site.json
PYTHONPATH=src python3 -m vega_forge new --spec examples/specs/python-cli.json --out build/demo-cli
```

## Templates

- `static-site`: HTML/CSS/JS starter
- `python-cli`: installable Python CLI starter
- `api-service`: FastAPI-style skeleton with optional dependency notes

## Status

MVP. Generates deterministic skeletons with README, LICENSE placeholder, `.gitignore`, runnable source, and basic verification files.
