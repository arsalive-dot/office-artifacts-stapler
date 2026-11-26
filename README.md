# Office Artifacts: The One-Line Placard Contest

[![make.fun · u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/arsalive-dot/office-artifacts-stapler/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/arsalive-dot/office-artifacts-stapler/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)

An entry for the [Office Artifacts: The One-Line Placard Contest](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2) bounty on make.fun: one line labelling an ordinary office object as an ancient artifact, judged by a dry-witted curator.

## The entry

> Stapler, c. 2019. Steel and quiet resentment. Donated by Accounts, who used it to bind together everything the meetings could not.

## How it works

`main.py` (Python 3, standard library only) writes the placard to `/output/entry.txt` deterministically: it writes a temporary file in the same directory, atomically replaces the target with `os.replace`, and sets mode 644. Running it twice produces byte-identical output.
