---
name: write-tests
description: Use when the user asks to write unit tests, add pytest tests, or improve test coverage for a Python script. Handles one script at a time, mocks anything that writes to production, then runs pytest until green.
---

# Write pytest unit tests for one script

Work on exactly one script. If the user did not name one, ask which. Never
modify the script under test; if you find a bug, report it instead of fixing it.

## 1. Understand the script
- Read the whole script. List every function/class, its branches, and its
  failure modes.
- Look for an existing `tests/` folder, `conftest.py`, and `pyproject.toml` /
  `pytest.ini` next to the script or at the repo root. Match existing
  conventions and reuse existing fixtures.
- Identify every external touchpoint: databases, APIs/HTTP, Airflow, cloud
  services, filesystem, env vars, clock/randomness.

## 2. Production safety rules (most important)
Tests must never change anything in production.
- **Writes are always mocked.** Anything that inserts, updates, deletes,
  triggers, posts, uploads, sends, or commits (DB writes, POST/PUT/DELETE
  calls, triggering/clearing/pausing Airflow DAGs, Slack messages, file
  uploads) must be replaced with a mock. Assert it was called with the
  expected arguments instead of running it.
- **Read-only calls are allowed** (SELECT queries, GET requests, listing or
  reading DAG state) but prefer mocks when a fast, deterministic test is
  possible. Use a real read only when it is the only way to verify behavior,
  and never in a way that needs write permissions.
- If you cannot tell whether a call is read-only, treat it as a write and
  mock it.
- Never put real credentials, hosts, or tokens in tests. Patch connection
  helpers and env vars (`monkeypatch.setenv`) with fake values.
- Use `tmp_path` for any file output; never write into the repo or real paths.
- Before running pytest, scan the generated tests: if any path could reach a
  real write, stop and fix the mocking first.

## 3. Design the tests
- File: `tests/test_<script_name>.py` (create `tests/` if missing).
- One test per behavior, named `test_<function>_<scenario>`.
- Use `@pytest.mark.parametrize` for input variations.
- Cover: happy path, edge cases (empty, `None`, wrong type, boundaries), and
  error paths (`pytest.raises` with `match=`).
- Use `monkeypatch` or `unittest.mock.patch` (patch where the name is
  *used*, not where it is defined). Use `pytest` fixtures for shared setup.
- Keep tests independent and deterministic: freeze time, seed randomness.
- Type-hint test functions (`-> None`) and give non-trivial tests a one-line
  docstring.
- Do not test third-party libraries or trivial getters.

## 4. Run and iterate
- Run `pytest tests/test_<script_name>.py -q`. If `pytest-cov` is installed,
  add `--cov=<module> --cov-report=term-missing` and report uncovered lines.
- If a test fails, decide whether the test or the script is wrong. Fix the
  test; if the script is wrong, leave it and report the bug.
- Repeat until all tests pass. Never report success without a passing run.

## 5. Report
Keep it short:
- Tests file path and number of tests passing
- Coverage (if available) and which branches are not covered, and why
- Which external calls were mocked (especially every write)
- Any bugs or oddities found in the script
- Suggest running `review-code` on the new test file before committing
