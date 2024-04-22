#!/usr/bin/python3
"""
Script to gather data from an API and display TODO list progress for a given employee ID.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    response = requests.get(url)
    todos = response.json()

    if not todos:
        print("No data found for employee ID {}".format(employee_id))
        sys.exit(0)

    employee_name = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id)).json()["name"]
    completed_tasks = [task for task in todos if task["completed"]]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task["title"]))
