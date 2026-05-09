# Vega Forge

[![Release](https://img.shields.io/github/v/release/Vega-Starboard/vega-forge?label=release)](https://github.com/Vega-Starboard/vega-forge/releases/tag/v0.1.0)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

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

MVP. `v0.1.0` is released. Generates deterministic skeletons with README, LICENSE placeholder, `.gitignore`, runnable source, and basic verification files.
