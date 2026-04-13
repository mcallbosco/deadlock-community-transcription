#!/usr/bin/env python3
"""Validate community localization folders against the metadata schema."""

import json
import sys
from pathlib import Path

from jsonschema import Draft7Validator

ROOT = Path(__file__).resolve().parent.parent
LOCALIZATIONS = ROOT / "localizations"
SCHEMA_PATH = ROOT / "schema" / "metadata.schema.json"


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft7Validator(schema)
    errors: list[str] = []

    if not LOCALIZATIONS.exists():
        print(f"No localizations/ directory found at {LOCALIZATIONS}")
        return 0

    for entry in sorted(LOCALIZATIONS.iterdir()):
        if not entry.is_dir() or entry.name.startswith("_"):
            continue

        metadata_path = entry / "metadata.json"
        if not metadata_path.exists():
            errors.append(f"{entry.name}/: missing metadata.json")
            continue

        try:
            data = json.loads(metadata_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{entry.name}/metadata.json: invalid JSON — {exc}")
            continue

        for err in validator.iter_errors(data):
            path = "/".join(str(p) for p in err.absolute_path) or "<root>"
            errors.append(f"{entry.name}/metadata.json [{path}]: {err.message}")

        language = data.get("language")
        if isinstance(language, str) and language != entry.name:
            errors.append(
                f"{entry.name}/metadata.json: 'language' field ({language!r}) "
                f"must match folder name ({entry.name!r})"
            )

        other_files = [
            p for p in entry.iterdir() if p.is_file() and p.name != "metadata.json"
        ]
        if not other_files:
            errors.append(
                f"{entry.name}/: no VDF localization file found "
                "(expected the original game VDF file alongside metadata.json)"
            )

    if errors:
        print("Validation failed:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("All localizations valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
