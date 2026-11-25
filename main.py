#!/usr/bin/env python3
"""One Line, One Laugh (coral-404) — entrypoint.

Writes the keeper line verbatim to /output/entry.txt.
Pure stdlib only (the grader runs python:3.13-slim, no site-packages).
"""

import os

KEEPER = "The lift mirror showed me a man who had given up, and he was wearing my coat."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 chars, not only
    # whitespace. The keeper is 81 chars; assert the band so a bad edit
    # fails loudly here instead of shipping an invalid entry.
    assert 1 <= len(KEEPER) <= 200, "keeper outside the 1-200 char gate"
    assert KEEPER.strip(), "keeper is only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)
    # Write-back self-check: what landed on disk must be the keeper, byte
    # for byte, with no trailing newline.
    with open(path, "rb") as f:
        assert f.read() == KEEPER.encode("utf-8"), "entry.txt mismatch"


if __name__ == "__main__":
    main()
