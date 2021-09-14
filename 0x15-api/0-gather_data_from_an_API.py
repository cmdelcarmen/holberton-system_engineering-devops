#!/usr/bin/python3
'''
    Write a Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
'''

import requests
from sys import argv


if __name__ == "__main__":

    emp_ID = argv[1]
    response = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(emp_ID))
    emp = response.json()['name']

    response = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                emp_ID))
    emp_tasks = response.json()

    emp_completed = 0
    task_list = []

    for value in emp_tasks:
        if value['completed']:
            emp_completed += 1
            task_list.append(value['title'])

    print("Employee {} is done with tasks({}/{}):".format(
        emp, emp_completed, len(emp_tasks)))

    for index in range(0, len(task_list)):
        print('\t {}'.format(task_list[index]))
