# `prompts.md` — Reasoning Notebook (AI & Prompts Track)

# Prompts Overview

 1. Role Prompt
 2. Constraints Prompt
 3. Critique → Refine Loop
 4. Python Prompt
 5. Tools / Models Disclosure

---

## 1) Role Prompt
**Goal:** Tell the model who it is and what to do.

**Prompt (final):**
 You are a front-end accessibility reviewer. Check this HTML mobile menu code
 for:

  1. click and keyboard toggle functionality,
  2. visible focus styles,
  3. correct ARIA attributes (aria-expanded, aria-controls).
  4. Provide a corrected version using only vanilla JS and CSS.

**Notes (1–2 lines):**

- Framing the model as an accessibility reviewer helped it focus on keyboard support and ARIA updates.
- Result included toggle fixes, aria-expanded updates, and restored focus outline.

---

## 2) Constraints Prompt
**Goal:** List hard limits (no new libs, keep file names, show diff only, etc.).

**Prompt (final):**

  Constraints:

   1. Do not add any external libraries.
   2. Only modify the provided HTML, JS, and CSS in this file.
   3. Show code with inline comments indicating fixes.
   4. Keep original file structure and names intact.

**Notes (1–2 lines):**

   - Ensured the output preserved file names and comment style.
   - Output included proper inline FIX markers.
  
---

## 3) Critique → Refine Loop
**Goal:** Ask the model to critique the initial fix, then refine and re-test.

**Critique prompt (final):**

    - Review the fixed HTML and JS code. Identify any remaining accessibility issues, missing keyboard support, or incorrect ARIA handling.
    - Provide detailed notes without changing the code yet.

**Refine prompt (final):**
  
   * Based on the critique, update the HTML and JS code to fix the issues:
 
    1. Ensure menu toggles correctly on click and keyboard (Enter/Space)
    2. Update aria-expanded dynamically
    3. Restore visible focus
    4. Include inline comments with // FIX where changes were made.

**Notes:**
    - Critique revealed missing keyboard toggle and ARIA updates.
    - Refined fix added key down handler and aria-expanded updates; inline FIX comments added. 

---

## 4) Python Prompt
**Goal:** Fix the buggy average calculator with proper validation.

**Prompt (final):**

    You are a Python tutor. Fix this average calculator:

     1. Skip header row, blank lines, and invalid values
     2. Treat 'NaN' as invalid
     3. Count only valid numbers
     4. Print average rounded to two decimals
     5. Keep file structure and comments, add # FIX where appropriate

**Notes:**
     - Prompt led to skipping invalid rows, handling 'NaN', and proper rounding.
     - Result matches hackathon acceptance criteria.

---
## Tools / Models Disclosure

     - GPT-4.1 via ChatGPT
     - VS Code (editing)
     - Python 3.13 (testing scripts)
     - Chrome DevTools (testing HTML/CSS)