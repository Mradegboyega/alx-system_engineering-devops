# Task Project README

This project includes solutions for a series of tasks implemented in Python. Each task involves working with JSON data related to employee tasks.

## Tasks Overview

### Task 0: Gather Data from an API
- **Filename:** `0-gather_data_from_an_API.py`
- **Description:** This script fetches data from a JSONPlaceholder API endpoint and prints information about a specified employee's TODO list.
- **Example Command:** `python3 0-gather_data_from_an_API.py 2`

### Task 1: Export to CSV
- **Filename:** `1-export_to_CSV.py`
- **Description:** This script extends Task 0 to export the data in CSV format.
- **Example Command:** `python3 1-export_to_CSV.py 2`

### Task 2: Export to JSON
- **Filename:** `2-export_to_JSON.py`
- **Description:** This script extends Task 0 to export the data in JSON format, specifically focusing on tasks owned by a particular employee.
- **Example Command:** `python3 2-export_to_JSON.py 2`

### Task 3: Dictionary of List of Dictionaries
- **Filename:** `3-dictionary_of_list_of_dictionaries.py`
- **Description:** This script extends Task 0 to export data in JSON format for all tasks from all employees.
- **Example Command:** `python3 3-dictionary_of_list_of_dictionaries.py`

## File Naming Convention
- For Task 0, the script is named `0-gather_data_from_an_API.py`.
- For Task 1, the script is named `1-export_to_CSV.py`.
- For Task 2, the script is named `2-export_to_JSON.py`.
- For Task 3, the script is named `3-dictionary_of_list_of_dictionaries.py`.

## JSON Output Files
- For Task 2, the output JSON file is named as `USER_ID.json`, where `USER_ID` corresponds to the user ID provided as input.
- For Task 3, the output JSON file is named as `todo_all_employees.json`.

## Running the Scripts
- Each script can be executed using the `python3` command followed by the script filename and optional arguments as required.

## Dependencies
- These scripts require Python 3 to be installed.
- No additional external libraries are needed beyond the standard Python library.
