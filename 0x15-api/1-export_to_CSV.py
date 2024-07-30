#!/usr/bin/python3

"""
    Returns to-do list information for a given employee ID and export data in csv format
."""
import csv
import requests
import sys

def fetch_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    username = user.get('username')

    todos = requests.get(f"{base_url}/todos", params={'userId': employee_id}).json()
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([employee_id, username, todo['completed'], todo['title']])

            print(f"Data for employee {username} (ID: {employee_id}) has been written to {filename}")
