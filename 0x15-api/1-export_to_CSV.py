#!/usr/bin/python3
'''
    Write a Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
'''
import csv
import requests
from sys import argv


if __name__ == "__main__":

    # gettign employee name
    emp_ID = argv[1]
    response = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(emp_ID))
    emp = response.json()['name']

    # getting a list of tasks completed
    response = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                emp_ID))
    emp_tasks = response.json()

    with open("{}.csv".format(emp_ID), 'w') as cvs_file:
        for value in emp_tasks:
            cvs_file.write(
                    '"{}", "{}", "{}", "{}"\n'.format(
                        emp_ID, emp, value['completed'], value['title']))
