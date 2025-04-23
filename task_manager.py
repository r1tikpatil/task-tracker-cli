from storage import (
    load_tasks,
    save_tasks,
)  # Import functions to load and save tasks from storage


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