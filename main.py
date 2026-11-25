#!/usr/bin/env python3
"""Entry program for One Line, One Minute: The Vending Machine
Pickup Line make.fun bounty.

Writes one pickup line (at most 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
the line a vending machine uses on a passing human. It has
been standing in the corridor all night, and it has noticed
you noticing it.
"""

import os

LINE = (
    "You check my prices every day at six. One day you'll "
    "press B4, and I'll be ready: cold, exact change, no "
    "judgement."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
