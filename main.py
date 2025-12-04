
---

# Code files

Save the following three files exactly as shown.

## 1) `fake_scanner.py` (Python — harmless, purely prints simulated output)

```python
#!/usr/bin/env python3
# fake_scanner.py — harmless, fake "scanner" output for theatrical effect.
# No real networking is performed.

import time, random, sys

ESC = "\x1b["
RESET = ESC + "0m"
BOLD = ESC + "1m"
RED = ESC + "31m"
GREEN = ESC + "32m"
YELLOW = ESC + "33m"
CYAN = ESC + "36m"
MAG = ESC + "35m"

hosts = [
    "host-azimuth.local",
    "core-gateway-11",
    "srv-ops-77",
    "vault-node-01",
    "ml-infer-03",
    "blackbox-edge"
]

modules = [
    "fingerprint/ai_fingerprint.v2",
    "kernel_probe.priv",
    "net-sim/latency-mapper",
    "quantum-timestamp",
    "entropy-harvester",
    "persistence-check"
]

banners = [
    "[ OK ]", "[ WARN ]", "[FAIL]", "[ > ]", "[ ... ]"
]

def slowprint(s, delay=0.01):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def progress_bar(duration=2.0):
    steps = 40
    for i in range(steps+1):
        pct = int(i/steps*100)
        bar = ("#"*i).ljust(steps, "-")
        sys.stdout.write(f"\r{CYAN}[{bar}]{RESET} {pct}%")
        sys.stdout.flush()
        time.sleep(duration/steps)
    print()

def fake_scan():
    slowprint(MAG + BOLD + "initiating shadow-console-sim v3.7" + RESET, 0.002)
    time.sleep(0.2)
    slowprint(YELLOW + "loading modules:" + RESET, 0.004)
    for m in modules:
        slowprint(f"  {GREEN}{m}{RESET} {random.choice(banners)}", 0.002)
        time.sleep(0.08)
    print()
    slowprint(RED + "target queue:" + RESET)
    for h in hosts:
        slowprint(f"  -> {h}  ({random.randint(2,320)}ms latency)  ", 0.004)
    print()
    slowprint(CYAN + "begin pseudo-probing..." + RESET)
    for h in hosts:
        sys.stdout.write(f"\n{BOLD}{h}{RESET} : ")
        sys.stdout.flush()
        progress_bar(1.2 + random.random()*1.4)
        # fake results:
        state = random.choices(["secure","compromised","weird-behavior","unknown"], [0.6,0.1,0.1,0.2])[0]
        tag = {
            "secure": GREEN + "[SECURE]" + RESET,
            "compromised": RED + "[COMPROMISED]" + RESET,
            "weird-behavior": YELLOW + "[ANOMALY]" + RESET,
            "unknown": CYAN + "[UNKNOWN]" + RESET
        }[state]
        slowprint(f"  status: {tag}  modules matched: {random.randint(0,9)}")
        time.sleep(0.3)
    print()
    slowprint(MAG + "analysis complete. generating artifact..." + RESET)
    time.sleep(0.6)
    for i in range(3):
        sys.stdout.write(". "); sys.stdout.flush(); time.sleep(0.4)
    print("\n")
    # fake artifact
    artifact = "".join(random.choice("0123456789abcdef") for _ in range(64))
    slowprint(GREEN + "artifact: " + RESET + artifact)
    print()
    slowprint(BOLD + "note: this is a simulation. no network I/O performed." + RESET)

if __name__ == "__main__":
    try:
        fake_scan()
    except KeyboardInterrupt:
        print("\n" + YELLOW + "interrupted (simulation stopped)" + RESET)
