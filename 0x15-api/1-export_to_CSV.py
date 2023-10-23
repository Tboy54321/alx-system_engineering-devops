#!/usr/bin/python3
"""API that todo lists of employees"""
import requests
import sys


if __name__ == '__main__':
    id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/users'

    employee_url_link = base_url + '/' + id
    task_url_link = employee_url_link + '/todos'

    employee_url = requests.get(employee_url_link)
    task_url = requests.get(task_url_link)

    employee_name = employee_url.json()['name']
    all_tasks = task_url.json()

    done_task = 0
    tasks = []

    for task in all_tasks:
        if task.get('completed'):
            tasks.append(task)
            done_task += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done_task, len(all_tasks)))
    for task in tasks:
        print("\t {}".format(task['title']))
