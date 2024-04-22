#!/usr/bin/python3
"""
Script to gather data from an API and export data in JSON format.
"""

import json
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

    json_filename = "{}.json".format(employee_id)
    with open(json_filename, 'w') as jsonfile:
        json.dump({employee_id: [{"task": task["title"], "completed": task["completed"], "username": employee_name} for task in todos]}, jsonfile)

    print("Data exported to", json_filename)
