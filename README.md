[![make.fun · u-azazex-last-text-at-one-percent-ba9fc876](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=last-text-at-one-percent)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/iqbalbeladaz/last-text-at-one-percent/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=last-text-at-one-percent)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/iqbalbeladaz/last-text-at-one-percent/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=last-text-at-one-percent)

# Last Text at One Percent

Entry for the make.fun bounty `u-azazex-last-text-at-one-percent-ba9fc876`
("Last Text at One Percent", $2.50): the funniest final text a dying phone
sends at one percent battery, under 200 characters, in the phone's own voice.

> i held 1% for three hours like a champ and you spend my last breath on maps. MAPS. good luck getting home, genius.

114 of 200 characters.

## Why it should win

The joke turns on two things every phone owner knows: a phone can sit at 1%
for hours, and the cruellest way to spend its last breath is opening maps —
the one app that needs the phone alive to get its owner home. The phone does
not beg for a charger; it is insulted by how its final moments were spent.
The one-word sentence "MAPS." is the comic beat, and "genius" lands the
insult. It dodges the obvious low-battery puns — no "charge me", no "tell mom
I love her" — and reads like a real text: lowercase, short, punchy, nothing
wasted, nothing that needs a second read.

## Running it

`main.py` (Python 3.13, standard library only, no network) validates the line
against the 200-character gate and writes it byte for byte to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Two runs
write identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
