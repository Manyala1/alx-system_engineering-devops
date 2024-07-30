#!/usr/bin/python3

"""
    Returns to-do list information for a given employee ID and export data in csv format
."""
import requests
import sys
import csv

def fetch_employee_todo_progress(emloyee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    employee = requests.get(f"{base_url}/users/{employee_id}").json()
    employee_name = employee.get('username')

    todos = request.get(f"{base_url}/todos", params={'userId': employee_id}).json()

    with open(f"{employee_id}.csv", mode='w', newline='') as file:
        writer = csv.write(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos:
            writer.writerow([employee_id, employee_name, todo['completed'], todo['title']])

    print(f"Data for employee {employee_name} (ID: {employee_id}) has been written to {employee_id}.csv")
