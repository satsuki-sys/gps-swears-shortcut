#!/usr/bin/env python3
"""make.fun entry: The GPS Swears It Was a Shortcut.

Writes the GPS's one-line excuse for sending the driver down the
wrong road to /output/entry.txt (one line, plain text, <= 200 chars).
"""
import os
import sys

ENTRY = (
    "I didn't miss the turn, I upgraded it \u2014 the map swore the "
    "lake was a shortcut, the wedding waved us through, and the "
    "ducks have never seen a sedan before."
)


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > 200 or "\n" in text:
        print(f"entry invalid: {len(text)} chars", file=sys.stderr)
        return 1
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
