#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun entry.

Writes the GPS's own excuse, one line, to $ENTRY_OUTPUT_DIR/entry.txt.
"""
import os

LINE = "The map swore the lake had a bridge. It didn't. The wedding guests were delightful, though, and the cul-de-sac has great acoustics."


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
