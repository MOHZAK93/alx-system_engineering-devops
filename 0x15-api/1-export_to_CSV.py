#!/usr/bin/python3
"""Export to CSV"""


from sys import argv
from requests import get


if __name__ == '__main__':
    USER_ID = argv[1]
    URL = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
    RESPONSE = get(URL)
    USERNAME = RESPONSE.json().get('username')

    URL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(USER_ID)
    RESPONSE = get(URL)
    TASKS = RESPONSE.json()
    with open('{}.csv'.format(USER_ID), 'w') as file:
        for task in TASKS:
            file.write('"{}","{}","{}","{}"\n'
                       .format(USER_ID, USERNAME, task.get('completed'),
                               task.get('title')))
