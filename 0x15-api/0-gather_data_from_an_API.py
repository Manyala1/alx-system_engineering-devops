#!/usr/bin/python3
"""
python script that, using a REST API, for a give employee ID, returns
information about his/her TODO list progress
"""

import requests
import sys

def fetch_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    employee = requests.get(f"{base_url}/users/{employee_id}").json()
    employee_name = employee.get('name')

    # Fetch employee's todo list
    todos = requests.get(f"{base_url}/todos", params={'userId': employee_id}).json()

    # Calculate the number of done tasks and the total number of tasks
    done_tasks = [todo for todo in todos if todo['completed']]
    number_of_done_tasks = len(done_tasks)
    total_tasks = len(todos)

    # Display the TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    fetch_employee_todo_progress(employee_id)
