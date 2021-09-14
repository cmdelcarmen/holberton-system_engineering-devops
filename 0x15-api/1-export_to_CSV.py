#!/usr/bin/python3
'''
    Write a Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
'''
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

    with open("{}.csv".format(emp_ID), 'w') as cvs_file:
        for value in emp_tasks:
            cvs_file.write(
                    '"{}", "{}", "{}", "{}"\n'.format(
                        emp_ID, username, value['completed'], value['title']))
