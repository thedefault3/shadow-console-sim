# shadow-console-sim

> ⚠️ **WARNING**: This repository is a **fake simulation / prank**.  
> Nothing here performs network scanning, exploits, or any malicious action. All tools are local simulators that print stylized output for entertainment and demonstration only.

## Overview

`shadow-console-sim` is a theatrical "black box" console simulator designed to look like an advanced security toolkit. It intentionally prints mysterious, noisy, and "hacker-like" output (ANSI colors, hex dumps, faux network logs) to spook and amuse your friends.

This project is purely for entertainment and educational demonstration — **do not** use it to impersonate real security tools or to attempt to deceive others into running harmful commands.

## Files

- `README.md` — this file.
- `fake_scanner.py` — a Python script that simulates a sophisticated host/port/AI scan (completely local and fake).
- `glitch.cpp` — a small C++ program that prints hex dumps, binary gibberish, and glitchy ASCII art.
- `stealth_log_generator.sh` — a Bash script that writes and tails a "weird" log file (local only).
- `evil_config.cfg` — decorative config file used by the simulation.

## Quick demo

Make the scripts executable and run them locally:

```bash
# make executable
chmod +x fake_scanner.py stealth_log_generator.sh
g++ -O2 -std=c++17 glitch.cpp -o glitch

# run
./glitch
./fake_scanner.py
./stealth_log_generator.sh
