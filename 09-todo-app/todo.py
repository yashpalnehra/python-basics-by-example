import argparse
import sys
from datetime import date
from pathlib import Path

import storage

DEFAULT_FILE = Path.home() / ".todo.json"


def add_task(data, text):
    task = {
        "id": data["next_id"],
        "text": text,
        "done": False,
        "added": str(date.today()),
    }
    data["tasks"].append(task)
    data["next_id"] += 1
    return task


def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise LookupError(f"no task with id {task_id}")


def mark_done(tasks, task_id):
    find_task(tasks, task_id)["done"] = True


def remove_task(tasks, task_id):
    tasks.remove(find_task(tasks, task_id))


def format_task(task):
    mark = "x" if task["done"] else " "
    return f"[{mark}] {task['id']:>3}  {task['text']}"


def build_parser():
    parser = argparse.ArgumentParser(description="a to-do list kept in a JSON file")
    parser.add_argument("--file", default=DEFAULT_FILE, help="where to keep the list")
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="add a task")
    add.add_argument("text", nargs="+")

    show = commands.add_parser("list", help="show tasks")
    show.add_argument("--all", action="store_true", help="include finished tasks")

    for name in ("done", "remove"):
        sub = commands.add_parser(name, help=f"{name} a task by id")
        sub.add_argument("id", type=int)
    return parser


def run(argv):
    args = build_parser().parse_args(argv)
    data = storage.load(args.file)
    tasks = data["tasks"]

    if args.command == "add":
        task = add_task(data, " ".join(args.text))
        print(f"added {task['id']}: {task['text']}")
    elif args.command == "list":
        shown = [t for t in tasks if args.all or not t["done"]]
        if not shown:
            print("nothing to do")
        for task in shown:
            print(format_task(task))
        return
    elif args.command == "done":
        mark_done(tasks, args.id)
        print(f"done {args.id}")
    elif args.command == "remove":
        remove_task(tasks, args.id)
        print(f"removed {args.id}")

    storage.save(args.file, data)


def main():
    try:
        run(sys.argv[1:])
    except (LookupError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
