#!/usr/bin/env python3
"""news-image-20261123: copy the bundled front page to the output dir.

Stdlib only: the grader runs Python 3.13 with no third-party packages.
The image is pre-rendered and shipped in this repository as entry.png;
this program only copies its bytes to $MAKEFUN_OUTPUT_DIR/entry.png
(default /output/entry.png). Deterministic: both runs write the same bytes.
"""
import os
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    data = src.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    if not 0 < len(data) <= 1048576:
        raise SystemExit("entry.png is empty or over the 1 MiB limit")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    dst.write_bytes(data)
    print(f"wrote {dst} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
