---
name: build-dag
description: Use when the user asks to create or modify an Airflow DAG. Gathers requirements, builds the DAG following team conventions, and validates it.
---

# Build a DAG

## 1. Clarify before writing
Ask only what is not already stated:
- Schedule and start date, catchup yes/no
- Data source and destination
- Retries, expected runtime, who is alerted on failure
- Dependencies on other DAGs or datasets

## 2. Design first
Propose the task list and dependency graph in plain text
(extract >> transform >> load) and get confirmation before coding.

## 3. Build, following these conventions
- Start from `dag_template.py` in this skill folder
- `dag_id` is snake_case and matches the filename
- `catchup=False` unless the user asks for backfills
- `default_args`: retries=2, retry_delay=5 min, on_failure_callback set
- Tasks must be idempotent (safe to re-run for the same date)
- No heavy work at module top level (no queries or API calls at import)
- Use Airflow connections/variables for config, never hardcoded secrets
- Use `{{ ds }}` templating instead of `datetime.now()`
- Small, single-purpose tasks with clear names
- Add a DAG docstring and tags

## 4. Validate
Run `python .claude/skills/build-dag/scripts/validate_dag.py <dag_file>`.
Fix any failure and re-run until it passes.

## 5. Report
Summarize schedule, tasks, and anything the user must set up manually
(connections, variables).
