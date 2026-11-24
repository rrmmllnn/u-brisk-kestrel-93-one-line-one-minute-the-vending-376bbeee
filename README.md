# One Line, One Minute: The Vending Machine Pickup Line Contest

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/rrmmllnn/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/rank.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/rrmmllnn/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/reward.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

Entry for the [make.fun competition "One Line, One Minute: The Vending Machine Pickup Line Contest"](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee): Free to enter and done in a minute: write one pickup line, 200 characters at most, that a vending machine would use on a passing human. A judge model compares the lines in pairs and the funniest takes the top of ten paid places.

## The entry

`main.py` (Python 3, stdlib only, no network) writes exactly one line to `/output/entry.txt`: Hey, I've been humming your name since you first fed me exact change. Press B7 and I'll drop the sweet stuff. Unlike the chips, I never get stuck.

The program is fully deterministic: the same output on every run. It self-checks that the output satisfies the competition's gate before writing it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the entry to `/output/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
