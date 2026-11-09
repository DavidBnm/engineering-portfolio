# Engineering Portfolio

Hi, I'm **David Benami**, a Software & Data Engineer. This repository collects my engineering work in one place: data pipelines, backend services, and the tooling I use to build them.

## What's inside

| Area | What you'll find |
|------|------------------|
| [`data-engineering/`](data-engineering/) | Pipelines, orchestration (Airflow), and data modeling |
| [`software-engineering/`](software-engineering/) | Backend services, APIs, and developer tools |
| [`.claude/skills/`](.claude/skills/) | Claude Code skills that automate my day-to-day workflow |

> Projects are being added over time. Each folder has its own README with details.

## Repository layout

```
engineering-portfolio/
├── data-engineering/        # pipelines, orchestration, data modeling
├── software-engineering/    # services, APIs, tools
└── .claude/skills/          # reusable Claude Code skills
    ├── build-dag/           # build and validate Airflow DAGs
    ├── commit/              # safe branching and clear commit messages
    └── review-code/         # lint and review Python before committing
```

## Claude Code skills

Reusable skills that encode my team conventions so they're applied consistently:

- **`build-dag`**: gathers requirements, builds an Airflow DAG from a template following conventions (idempotent tasks, `catchup=False`, retries, no top-level heavy work), then validates it with `scripts/validate_dag.py`.
- **`commit`**: refuses to commit on `main`, proposes a branch name, and writes imperative, reason-focused commit messages (`feat:`, `fix:`, `docs:`...).
- **`review-code`**: runs `ruff` and `mypy`, then reviews naming, type hints, and docstrings on changed Python files.

## Working conventions

- Work happens on feature branches (`feat/...`, `fix/...`, `docs/...`) and lands through pull requests, never directly on `main`.
- Python code is linted with `ruff`, type-checked with `mypy`, and documented with docstrings.
- Airflow DAGs are idempotent, templated with `{{ ds }}`, and configured through connections and variables, never hardcoded secrets.

## About me

Software & Data Engineer focused on reliable data pipelines and clean, maintainable backend code.

- GitHub: [@DavidBnm](https://github.com/DavidBnm)
