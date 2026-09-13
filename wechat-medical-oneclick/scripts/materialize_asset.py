#!/usr/bin/env python3
"""Restore the retained reference image after a text-only GitHub install."""

from __future__ import annotations

import base64
from pathlib import Path


def main() -> None:
    assets = Path(__file__).resolve().parent.parent / "assets"
    source = assets / "female-clinician-reference.jpg.b64"
    target = assets / "female-clinician-reference.jpg"
    if target.is_file() and target.stat().st_size > 0:
        print(f"OK existing={target}")
        return
    target.write_bytes(base64.b64decode(source.read_text(encoding="ascii")))
    if target.stat().st_size < 10_000:
        raise RuntimeError("还原后的参考图异常")
    print(f"OK created={target}")


if __name__ == "__main__":
    main()
