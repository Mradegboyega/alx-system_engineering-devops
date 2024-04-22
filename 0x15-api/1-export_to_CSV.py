#!/usr/bin/python3
"""
Script to gather data from an API and export data in CSV format.
"""

import csv
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

    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for task in todos:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': str(task["completed"]),
                'TASK_TITLE': task["title"]
            })

    print("Data exported to", csv_filename)
