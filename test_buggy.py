#!/usr/bin/env python3
"""Tiny unit tests for buggy.py – AI & Prompts Track

Tests two simple scenarios:
1. Normal CSV with valid numbers.
2. CSV with blanks and invalid entries (including 'NaN').
"""

import io
import os
from buggy import average_from_csv

# Helper to create a temporary CSV file for testing
def write_temp_csv(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))

# Test 1: normal CSV
def test_normal_csv():
    # FIX: create a simple CSV with valid numbers
    lines = [
        "score",
        "80",
        "90",
        "70"
    ]
    filename = "test1.csv"
    write_temp_csv(filename, lines)
    avg = average_from_csv(filename)
    assert round(avg, 2) == 80.00, f"Expected 80.00, got {avg:.2f}"
    os.remove(filename)

# Test 2: CSV with blanks and bad values
def test_csv_with_bad_values():
    # FIX: include header, blank lines, 'NaN', and a bad string
    lines = [
        "score",
        "78",
        "",
        "oops",
        "84",
        "NaN",
        "73"
    ]
    filename = "test2.csv"
    write_temp_csv(filename, lines)
    avg = average_from_csv(filename)
    # valid numbers: 78, 84, 73 → avg = 235 / 3 = 78.3333
    assert round(avg, 2) == 78.33, f"Expected 78.33, got {avg:.2f}"
    os.remove(filename)

# Run tests
if __name__ == "__main__":
    test_normal_csv()
    print("Test 1 passed ✅")
    test_csv_with_bad_values()
    print("Test 2 passed ✅")