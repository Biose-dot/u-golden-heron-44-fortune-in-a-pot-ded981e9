#!/usr/bin/env python3
"""Fortune in a Pot — make.fun entry.

A fortune for the little fern on the windowsill: watered, praised, and — for once — not mistaken for a salad.
"""
import os

ENTRY = 'Great news, little fern: this week you will be watered, praised, and — for once — not mistaken for a salad.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
