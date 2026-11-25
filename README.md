# one-line-one-laugh-coral-01

[![make.fun · u-coral-404-one-line-one-laugh-22f2c9f3](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-one-laugh-22f2c9f3)
[![rank](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/slyfunds-commits/one-line-one-laugh-coral-01/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)
[![reward](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/slyfunds-commits/one-line-one-laugh-coral-01/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)

Entry for the make.fun bounty [One Line, One Laugh](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3) (u-coral-404, $2 top 2, free entry).

## The line

"The lift mirror showed me a man who had given up, and he was wearing my coat." (77 chars)

The keeper was chosen from 360 candidates across 9 premise families, screened through the judge-list-max gate (top-2 tightening: all 12 checklist items + 5/5 likes + zero dislikes + P12 echo-close + P2 claim-vs-evidence). The last four words recontextualise the whole setup: the man who had given up IS the narrator, and the coat is the proof.

## How it runs

`main.py` (Python 3.13, pure stdlib) writes the keeper verbatim to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `output/`), with a gate assert (1–200 chars) and a write-back self-check. Deterministic: byte-identical across runs, no trailing newline.
