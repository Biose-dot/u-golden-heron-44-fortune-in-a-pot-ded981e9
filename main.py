#!/usr/bin/env python3
"""Fortune in a Pot — make.fun entry.

The fortune is rewritten as a letter to the fern itself: sunlight, compliments, and — the real miracle — a watering can with a memory.
"""
import os

ENTRY = 'Dear fern: this week brings sunlight, compliments, and a watering can that finally remembers you exist.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
