# Vibe-Coding-Round-2
# Bug-Fix & Accessibility – AI & Prompts Track

**Author:** Mayuresh Mandalik  
**Department:** Computer Engineering, 2nd Year  
**Track:** AI & Prompts (Vibe Coding Round 2)

---

## Project Overview

This project demonstrates **bug fixes and accessibility improvements** for a small web and Python task. It includes:

1. **Mobile Menu Fix (`buggy.html`)**
   - Mobile menu toggles correctly on small screens (≤640px)
   - Keyboard support: Enter/Space toggles menu
   - Focus outline is visible
   - ARIA attributes updated dynamically
   - Inline `// FIX` comments indicate changes

2. **Average Calculator Fix (`buggy.py`)**
   - Reads `marks.csv` and computes the correct average
   - Skips header, blank lines, and invalid rows (`oops`, `NaN`)
   - Rounds output to two decimals
   - Inline `# FIX` comments indicate changes

3. **Prompt Engineering Documentation (`prompts.md`)**
   - Role, Constraints, Critique→Refine, and Python prompts documented
   - Notes explain what changed and why
   - Tools/Models used: GPT-4.1, VS Code, Chrome DevTools, Python 3.13

4. **Unit Tests (`test_buggy.py`)**
   - Contains two small tests for `buggy.py` average function
   - Verifies correct handling of valid and invalid rows
   - Confirms output rounds to two decimals
   - Helps ensure the Python fix works reliably

---

## Usage

### HTML Mobile Menu
1. Open `buggy.html` in a browser.
2. Resize browser or use mobile view.
3. Click the menu button or use Enter/Space to toggle.

### Python Average Calculator
1. Ensure `marks.csv` is in the same folder as `buggy.py`.
2. Run:

```bash
python buggy.py
```
* Output prints the average rounded to two decimals, e.g.: 82.60

```bash
python test_buggy.py
```
* Expected output:

  Test 1 passed ✅<br>
  Test 2 passed ✅

### Outputs :

1. HTML menu: Opens/closes on click & keyboard, focus visible, ARIA updated.
2. Python average: Correct average calculated ignoring invalid rows (oops, NaN), rounded to two decimals.
3. Unit tests: Both tests pass, validating the Python fix.
