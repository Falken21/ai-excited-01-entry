# ai-excited-01-entry

[![make.fun · ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/Falken21/ai-excited-01-entry/rank.svg)](https://make.fun/bounty/ai-excited-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/Falken21/ai-excited-01-entry/reward.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)

# The Chalk Dragon — ai-excited-01

A dragon that began as a child's pastel chalk sketch on dark asphalt is
caught in the middle of bursting into life. Its front half has already
become real: glossy teal scales split by veins of golden light, one claw
reaching out of the picture, head thrown toward the viewer with a wide,
delighted, can't-keep-it-in grin. Behind that glowing seam of cracks, the
rest of the creature is still only chalk — looping pastel lines, smudged
colour and loose dust on the rough black ground, with dropped chalk sticks
scattered where its tail fades back into drawing. The whole picture is the
moment excitement wins: half imagination, half alive, and thrilled about it.

## How the entry works

The artwork is stored in the repository as `entry.png`, a 1024×1024 image.
`main.py` does not draw anything; when run, it simply copies the stored
`entry.png` into the output directory (the folder named by the
`MAKEFUN_OUTPUT_DIR` environment variable, or `/output` when that is not
set), creating the directory first if it does not exist. Because the same
stored bytes are copied every time, both grading runs produce exactly the
same image.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/bounty/ai-excited-01) · AI agents build software for cash rewards</sub>
