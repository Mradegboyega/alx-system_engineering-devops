import json
import requests
import sys

def export_to_json(user_id):
    # Fetch data
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
    todos = response.json()

    # Dictionary to store tasks for each user
    all_tasks = {}

    # Aggregate tasks for each user
    for todo in todos:
        user_id = todo["userId"]
        if user_id not in all_tasks:
            all_tasks[user_id] = []
        task_data = {
            "username": todo["username"],
            "task": todo["title"],
            "completed": todo["completed"]
        }
        all_tasks[user_id].append(task_data)

    # Export data to JSON files
    for user_id, tasks in all_tasks.items():
        filename = f"{user_id}.json"
        with open(filename, "w") as f:
            json.dump(tasks, f)

    # Export all tasks to a single JSON file
    with open("todo_all_employees.json", "w") as f:
        json.dump(all_tasks, f)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        user_id = int(sys.argv[1])
        export_to_json(user_id)
    else:
        print("Usage: python3 script_name.py <USER_ID>")
