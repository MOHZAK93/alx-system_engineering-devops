#!/usr/bin/python3
"""Gather data from API"""


import requests
import sys


def gad():
    """Gather data from an API"""

    user = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    todos = 'https://jsonplaceholder.typicode.com/todos/?userId=' + sys.argv[1]
    r1 = requests.get(user)
    r2 = requests.get(todos)

    emp = r1.json()
    name = emp.get('name')
    tasks = r2.json()
    done_tasks = [x for x in tasks if x.get('completed')]
    d_len = len(done_tasks)

    print(f"Employee {name} is done with tasks({d_len}/{len(tasks)})")

    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        gad()
