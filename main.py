import argparse
from task_manager import add_task


def main():
    """
    Entry point for the Task Tracker CLI application.
    Parses command-line arguments and invokes the appropriate task function.
    """
    parser = argparse.ArgumentParser(
        description="Task Tracker CLI"
    )  # Create the top-level parser
    subparsers = parser.add_subparsers(
        dest="command"
    )  # Create subparsers for each command

    # Parser for the 'add' command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Title of the task")
    add_parser.add_argument(
        "--description", default="", help="Optional description of the task"
    )
    add_parser.add_argument("--due", default="", help="Optional due date for the task")

    # Parse the arguments provided by the user
    args = parser.parse_args()

    # Dispatch the appropriate function based on the command
    if args.command == "add":
        add_task(args.title, args.description, args.due)


# Run the main function when the script is executed directly
if __name__ == "__main__":
    main()
