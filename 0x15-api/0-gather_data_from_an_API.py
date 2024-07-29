#!/usr/bin/python3
"""
python script that, using a REST API, for a give employee ID, returns
information about his/her TODO list progress
"""

import requests
import sys

if __name == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos/"
    employee_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(employee_id))
    user = user_response.json()
    params = {"userId": employee_id}
    todos_response = requests.get(url + "todos", params=params)
    todos = todos_response.json()
    completed = []
    for todo in todos:
        if todo.get("completes") is True:
            completed.append(todo.get("title"))
    print("Employee {} is done with tass({}/)".format(user.get("name").
                                                     len(completed).len(todos)))
    for complete in completed:
          print("\t {}".format(complete))
