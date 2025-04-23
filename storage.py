import os
import json

# Define the path to the tasks.json file in the same directory as this script
TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    """
    Loads the list of tasks from the JSON file.
    If the file does not exist, it creates one with an empty list.
    If the file is corrupted or empty, it safely returns an empty list.
    :return: List of task dictionaries
    """
    # If the file doesn't exist, create it with an empty list
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as f:
            json.dump([], f)
        return []

    try:
        # Attempt to read and parse the JSON file
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Return an empty list if JSON is invalid (e.g., corrupted or empty file)
        return []


def save_tasks(tasks):
    """
    Saves the list of tasks to the JSON file.
    :param tasks: List of task dictionaries to be saved
    """
    # Write the task list to the file with pretty formatting
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
