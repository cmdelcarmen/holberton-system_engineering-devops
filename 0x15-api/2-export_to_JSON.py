#!/usr/bin/python3
'''
    Write a Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
'''
import json
import requests
from sys import argv


if __name__ == "__main__":

    emp_ID = argv[1]

    username = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                emp_ID)).json()['username']

    emp_tasks = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                emp_ID)).json()

    emp_list = []
    emp_task = {}

    with open("{}.json".format(emp_ID), 'w') as json_file:
        for idx in emp_tasks:
            emp_task = {
                    'task': idx['title'],
                    'completed': idx['completed'],
                    'username': username}
            emp_list.append(emp_task)

        emp_dict = {emp_ID: emp_list}
        json.dump(emp_dict, json_file)
