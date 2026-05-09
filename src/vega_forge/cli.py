from __future__ import annotations

import argparse
import json
from pathlib import Path

def load_spec(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    for key in ("name", "type", "description"):
        if key not in data:
            raise SystemExit(f"spec missing {key}")
    return data

def files_for(spec: dict) -> dict[str, str]:
    name = spec["name"]
    desc = spec["description"]
    common = {"README.md": f"# {name}\n\n{desc}\n", "LICENSE": "License placeholder.\n", ".gitignore": "__pycache__/\n.env\n"}
    if spec["type"] == "static-site":
        common.update({"index.html": f"<!doctype html><title>{name}</title><main><h1>{name}</h1><p>{desc}</p></main>\n", "styles.css": "body{font-family:sans-serif;max-width:760px;margin:4rem auto;line-height:1.6}\n"})
    elif spec["type"] == "python-cli":
        package = name.replace("-", "_")
        common.update({f"src/{package}/__main__.py": "print('hello from generated cli')\n", "scripts/verify.py": "print('verify placeholder')\n"})
    elif spec["type"] == "api-service":
        common.update({"app.py": "try:\n    from fastapi import FastAPI\nexcept ImportError:\n    FastAPI = None\n\napp = FastAPI() if FastAPI else None\n", ".env.example": "PORT=8000\n"})
    else:
        raise SystemExit(f"unsupported type: {spec['type']}")
    return common

def preview(spec: dict) -> str:
    return "\n".join(sorted(files_for(spec))) + "\n"

def generate(spec: dict, out: Path) -> None:
    for rel, content in files_for(spec).items():
        target = out / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

def main() -> int:
    parser = argparse.ArgumentParser(description="Generate deterministic project skeletons from JSON specs.")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("preview", "new"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--spec", type=Path, required=True)
        if name == "new":
            cmd.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    spec = load_spec(args.spec)
    if args.command == "preview":
        print(preview(spec), end="")
    else:
        generate(spec, args.out)
        print(f"generated {spec['name']} at {args.out}")
    return 0
