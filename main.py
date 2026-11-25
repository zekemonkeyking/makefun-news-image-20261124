#!/usr/bin/env python3
"""Decode the bundled newspaper image and write it to /output/entry.png.

Reads entry.png.b64 (a single line of base64) from the repository root,
checks the PNG magic bytes, and writes the decoded image.
Standard library only; no network.
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path("/output/entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    text = (ROOT / "entry.png.b64").read_text().strip()
    data = base64.b64decode(text, validate=True)
    if not data.startswith(PNG_MAGIC):
        raise ValueError("decoded data is not a PNG image")
    if b"IEND" not in data[-16:]:
        raise ValueError("decoded PNG is truncated (no IEND chunk)")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(data)


if __name__ == "__main__":
    main()
