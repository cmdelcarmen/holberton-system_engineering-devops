#!/usr/bin/python3
'''
    Using what you did in the task #0,
    extend your Python script to export data in the JSON format.
'''
import json
import requests
from sys import argv


if __name__ == "__main__":

    users = requests.get(
            'https://jsonplaceholder.typicode.com/users').json()

    emp_profile = {}
    emp_list = []

    for user in users:

        emp_ID = user['id']
        user_prof = requests.get(
                        'https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(emp_ID)).json()
        emp_name = user['name']

        for idx in user_prof:
            emp_profile = {
                        'task': idx['title'],
                        'completed': idx['completed'],
                        'username': emp_name}
            emp_list.append(emp_profile)
            emp_dict = {emp_ID: emp_list}

        with open("todo_all_employees.json", 'w') as json_file:
            json.dump(emp_dict, json_file)
