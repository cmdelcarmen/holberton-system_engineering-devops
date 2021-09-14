#!/usr/bin/python3
'''
    Using what you did in the task #0,
    extend your Python script to export data in the JSON format.
'''
import json
import requests

if __name__ == "__main__":
    emp_dict = {}

    for emp in requests.get(
                        'https://jsonplaceholder.typicode.com/users').json():
        emp_id = emp.get('id')
        tasks = requests.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                    emp_id)).json()
        task_list = []
        for field in tasks:
            task = {'task': field['title'],
                    'completed': field['completed'],
                    'username': emp.get('username')
                    }
            task_list.append(task)
        emp_dict[emp_id] = task_list

        with open('todo_all_employees.json', 'w') as export:
            json.dump(emp_dict, export)
