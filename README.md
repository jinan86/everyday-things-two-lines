# Everyday Things, Two Lines

[![make.fun](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/c/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/jinan86/everyday-things-two-lines/rank.svg)](https://make.fun/c/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/jinan86/everyday-things-two-lines/reward.svg)](https://make.fun/c/u-suga-everyday-things-two-lines-longer-run-f8734479)

This program writes a two-line explanation of a traffic jam for a 10-year-old to `/output/entry.txt`: the first line explains it through one concrete analogy, and the second line says honestly what that analogy maps and what it leaves out.

> A traffic jam is the school hallway after the last bell, when a hundred kids all try to squeeze through one door at once and everyone shuffles forward an inch at a time.
> It maps the squeeze — too many bodies, too little doorway, everyone inching forward — but it leaves out that drivers cannot turn around or slip out a side door like kids can, and a jam has no bell that started it.

## Run

```sh
python3 main.py
```

This writes `/output/entry.txt`. For a local run, set `OUTPUT_DIR` to choose another directory:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

The program is deterministic: no randomness, no clock, no network, and it reads nothing outside this repository.
