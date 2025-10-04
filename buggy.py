#!/usr/bin/env python3
"""Buggy average calculator for AI & Prompts Track

Base task (what to fix):
- Read numbers from marks.csv and compute the average with two decimals.
- Ignore the header row and any blank lines.
- Handle bad values gracefully (skip them without crashing).
- Print only the final average to stdout, rounded to two decimals.

Current issues (intentionally introduced):
- Counts every line in the denominator (including header & blanks).
- Tries to convert every line to float, then still divides by total line count.
- No rounding to two decimals.
- Hard-codes the filename but that's fine for the task.
"""

import sys

def average_from_csv(path: str) -> float:
    with open(path, 'r') as f:
        rows = [line.strip() for line in f.readlines()]

    total = 0.0
    count = 0  # FIX: track only valid numeric rows
    for idx, r in enumerate(rows):
        # FIX: skip header (assume first row is header)
        if idx == 0:
            continue
        # FIX: skip blank lines
        if not r:
            continue
        # FIX: skip values that are literally 'NaN'
        if r.strip().lower() == "nan":
            continue
        try:
            total += float(r)
            count += 1  # FIX: count only valid numbers
        except Exception:
            # just ignore parse failure
            continue

    # WRONG: divide by total number of rows, including header/blank/invalid
    # FIX: divide only by count of valid numbers
    return total / count if count > 0 else 0.0


if __name__ == '__main__':
    # Intentionally hard-coded per instructions
    avg = average_from_csv('marks.csv')
    # FIX: round to two decimals
    print(f"{avg:.2f}")