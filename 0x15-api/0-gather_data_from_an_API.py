#!/usr/bin/python3
"""Gather data from an API"""


from requests import get
from sys import argv


def gad():
    user = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    todos = "https://jsonplaceholder.typicode.com/todos/?userId=" + argv[1]

    r1 = get(user)
    r2 = get(todos)

    employee = r1.json()
    tasks = r2.json()
    done_tasks = [x for x in tasks if x.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(employee.get("name"),
                                                          len(done_tasks),
                                                          len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(argv) == 2:
        gad()
