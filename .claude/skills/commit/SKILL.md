---
name: commit
description: Use when the user asks to commit, push, or save changes to git. Makes sure we are not on main and writes a good commit message.
---

# Commit changes

## 1. Check the branch first
Run `git branch --show-current`.
- If it is `main` (or `master`), STOP. Do not commit. Propose a branch name
  (`feat/short-description`, `fix/...`, `docs/...`) based on the changes, and
  ask the user to confirm before creating it with `git switch -c <name>`.
- If it is already a feature branch, say which one and continue.

## 2. Review what will be committed
Run `git status` and `git diff`. Summarize the changes in a line or two.
- Never stage `.env`, secrets, or anything in `.claude/` except `.claude/skills/`.
- If unrelated changes are mixed together, suggest splitting them into
  separate commits.

## 3. Write the commit message
Format:

    type: short summary in imperative mood

    Optional body: what changed and WHY (not how).

- Types: feat, fix, docs, refactor, test, chore
- Summary under 72 characters, no trailing period
- Imperative mood: "Add retry logic", not "Added" or "Adds"
- Describe the reason for the change, not just the files touched
- Show the message to the user before committing

## 4. Commit, then ask before pushing
Commit, then show `git log -1 --stat`. Ask before pushing. Push with
`git push -u origin <branch>` and never push directly to main.
