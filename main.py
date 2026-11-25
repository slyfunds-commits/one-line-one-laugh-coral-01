#!/usr/bin/env python3
"""One Line, One Laugh (coral-404) — make.fun entry.

A lift mirror, a man who has given up, and a coat that gives the game
away. This program writes the single line to /output/entry.txt,
byte-exact, with no trailing newline.

The line works as one lock-screen moment: a plain observation that
turns in its last words. The mirror shows a stranger, and then the
coat proves the stranger is the narrator — the man who had given up
is the one telling it, and he has been standing there long enough to
notice his own coat. That small recontextualising turn is the whole
joke: no setup, no explanation, just the reveal.

Why it lands on a first read: the mirror is an everyday object, the
man is a stranger for exactly one clause, and the coat collapses the
distance in four words. The reader does the work of recognising
themselves in the mirror, which is why the line keeps its laugh
instead of explaining it away.
"""

import os

LINE = "The lift mirror showed me a man who had given up, and he was wearing my coat."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
