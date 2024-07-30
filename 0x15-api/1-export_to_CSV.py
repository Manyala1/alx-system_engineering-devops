#!/usr/bin/python3

"""
    Returns to-do list information for a given employee ID and export data in csv format
."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    
    user_id = sys.argv[1]
    user_resource = requests.get(url + "users/{}".format(user_id))
    user = user_response.json()
    username = user.get("username")
    params = {"userId": user_id}
    todos_response = requests.get(url + "todos", params=params)
    todos = todos_response.json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
            writer = csv.writer(csvfile. quoting=CSV.QUOTE_ALL)

            for todo in todos:
                writer.writerow([user_id, username, todo.get("completed"), todo.get("title")])
