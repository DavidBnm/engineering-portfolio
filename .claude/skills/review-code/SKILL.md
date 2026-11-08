---
name: review-code
description: Use before committing or pushing, or when the user asks to check, lint, or review Python code quality. Runs automated checks, then reviews naming, type hints, and docstrings.
---

# Review code before commit

Review only the changed Python files (`git diff --name-only` plus staged and
untracked `.py` files) unless the user names other files.

## 1. Run automated checks
Run whichever of these are available (check `pyproject.toml` or
`.pre-commit-config.yaml`; skip a tool that is not installed and say so):
- `ruff check <files>` (imports, style, unused code, annotations, docstrings)
- `ruff format --check <files>`
- `mypy <files>`

Report failures. Do not fix them yet if the user only asked for a review.

## 2. Judgment review (what tools cannot catch)
For each changed file check:
- **Names:** variables, functions, and classes are descriptive. Flag `data2`,
  `tmp`, `x`, `df1`, misleading names, and names that don't match what the
  value actually is.
- **Type hints:** every function has typed arguments and a return type
  (`-> int`, `-> None`, etc.) and the types are accurate, not just `Any`.
- **Docstrings:** public functions and classes have one. It should say what
  is returned and why the function exists, not just repeat its name. Args and
  Returns sections where the function is not trivial.
- **Leftovers:** unused imports, dead or commented-out code, debug `print`s,
  hardcoded secrets or paths, TODOs that should be resolved.
- **Functions:** one clear job each; flag very long functions or deep nesting.

## 3. Report
Group findings by file with line numbers, most important first:

    path/file.py:42  naming   `d` -> suggest `daily_totals`
    path/file.py:57  types    missing return type on `load_rows`

End with a one-line verdict: ready to commit, or what must be fixed first.

## 4. Fix
Ask whether to apply the fixes. Apply only what the user approves, then re-run
step 1 to confirm the checks pass.
