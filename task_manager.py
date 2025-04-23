from storage import (
    load_tasks,
    save_tasks,
)
from rich import print
from rich.table import Table


def add_task(title, description="", due_date=""):
    """
    Adds a new task to the task list.
    :param title: Title of the task
    :param description: (Optional) Description of the task
    :param due_date: (Optional) Due date of the task
    """
    tasks = load_tasks()  # Load existing tasks
    # Generate a unique ID by finding the max existing ID and adding 1
    task_id = max([task["id"] for task in tasks], default=0) + 1
    # Define the new task dictionary
    new_task = {
        "id": task_id,
        "title": title,
        "description": description,
        "status": "Pending",  # Default status
        "due_date": due_date,
    }
    tasks.append(new_task)  # Add the new task to the list
    save_tasks(tasks)  # Save updated task list
    print(f"Task '{title}' added with ID {task_id}.")


def list_tasks():
    """
    Loads and displays tasks from the JSON file in a styled table format using Rich.
    Sorts tasks by due date and highlights their status with colors.
    """
    tasks = load_tasks()

    # If there are no tasks, inform the user and exit the function
    if not tasks:
        print("[bold red]No tasks found.[/bold red]")
        return

    # Initialize a styled Rich table with column headers
    table = Table(title="📋 Task List", show_lines=True)
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Title", style="bold")
    table.add_column("Description", style="")
    table.add_column("Status", style="magenta")
    table.add_column("Due Date", style="yellow")

    # Populate the table by sorting tasks by due date (empty due dates go last)
    for task in sorted(tasks, key=lambda x: x.get("due_date", "")):
        table.add_row(
            str(task["id"]),
            task["title"],
            task["description"],
            f"[green]{task['status']}[/green]"
            if task["status"] == "Completed"
            else f"[red]{task['status']}[/red]",
            task.get("due_date", "N/A"),
        )

    # Print the styled table to the terminal
    print(table)
