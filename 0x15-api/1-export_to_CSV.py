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

    employee_name = employee_url.json()['username']
    all_tasks = task_url.json()

    with open('{}.csv'.format(id), 'w') as file:
        for task in all_tasks:
            file.write('"{}","{}","{}","{}"\n'.format(id,
                       employee_name, task['completed'], task['title']))
