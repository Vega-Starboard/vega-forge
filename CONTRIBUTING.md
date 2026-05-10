# Contributing

## Development Setup

```bash
python3 -m pip install --user -e .
python3 scripts/verify.py
```

## Pull Requests

- Keep changes focused.
- Update docs when behavior changes.
- Add or update examples when a template changes.
- Run `python3 scripts/verify.py` before opening a pull request.

## Boundaries

Do not add hidden network calls or model dependencies to the MVP path. Vega Forge should remain deterministic and local by default.
