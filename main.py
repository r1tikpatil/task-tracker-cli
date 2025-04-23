import argparse
from task_manager import add_task, list_tasks, complete_task, delete_task


def main():
    """
    Entry point for the Task Tracker CLI application.
    Parses command-line arguments and invokes the appropriate task function.
    """
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Parser for the 'add' command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Title of the task")
    add_parser.add_argument(
        "--description", default="", help="Optional description of the task"
    )
    add_parser.add_argument("--due", default="", help="Optional due date for the task")

    # Parser for the 'list' command
    subparsers.add_parser("list", help="List all tasks")

    # Parser for the 'complete' command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument(
        "id", type=int, help="ID of the task to mark as completed"
    )

    # Parser for the 'delete' command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="ID of the task to delete")

    # Parse the arguments provided by the user
    args = parser.parse_args()

    # Dispatch the appropriate function based on the command
    if args.command == "add":
        add_task(args.title, args.description, args.due)
    elif args.command == "list":
        list_tasks()
    elif args.command == "complete":
        complete_task(args.id)
    elif args.command == "delete":
        delete_task(args.id)
    else:
        parser.print_help()


# Run the main function when the script is executed directly
if __name__ == "__main__":
    main()
