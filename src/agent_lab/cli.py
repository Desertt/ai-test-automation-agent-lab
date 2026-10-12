import argparse
import json


def create_plan(task: str) -> dict:
    task = task.strip()

    if not task:
        raise ValueError("Task cannot be empty")

    return {
        "task": task,
        "status": "planned",
        "mode": "deterministic",
        "approved": False,
        "execution": "not_started",
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="agent-lab",
        description="AI Test Automation Agent Lab",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("--task", required=True)

    args = parser.parse_args()

    if args.command == "run":
        try:
            result = create_plan(args.task)
        except ValueError as exc:
            parser.error(str(exc))

        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()