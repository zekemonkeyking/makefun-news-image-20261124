#!/usr/bin/env python3
"""Decode the bundled newspaper image and write it to /output/entry.png.

Reads entry.png.b64 (a single line of base64) from the same directory
as this file, decodes it, checks the PNG magic bytes, and writes the
image to /output/entry.png. Standard library only, no network.
"""
import base64
import os

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    b64_path = os.path.join(here, "entry.png.b64")
    with open(b64_path, "r", encoding="ascii") as fh:
        data = base64.b64decode(fh.read().strip())
    if not data.startswith(PNG_MAGIC):
        raise ValueError("decoded data is not a PNG image")
    if b"IEND" not in data[-16:]:
        raise ValueError("decoded data is not a complete PNG image")
    if len(data) > 1048576:
        raise ValueError("decoded image is over the 1 MiB limit")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.png", "wb") as fh:
        fh.write(data)


if __name__ == "__main__":
    main()
