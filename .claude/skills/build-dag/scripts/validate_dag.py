"""Usage: python validate_dag.py <dag_file.py>. Exits non-zero on failure."""
import sys

from airflow.models import DagBag

path = sys.argv[1]
bag = DagBag(dag_folder=path, include_examples=False)

if bag.import_errors:
    for f, err in bag.import_errors.items():
        print(f"IMPORT ERROR in {f}:\n{err}")
    sys.exit(1)
if not bag.dags:
    print("No DAG found in file")
    sys.exit(1)

for dag_id, dag in bag.dags.items():
    problems = []
    if dag.catchup:
        problems.append("catchup is True")
    if not dag.default_args.get("retries"):
        problems.append("no retries in default_args")
    if not dag.tags:
        problems.append("no tags")
    print(f"{dag_id}: {len(dag.tasks)} tasks", "OK" if not problems else f"WARN {problems}")
