#!/usr/bin/python3
'''
Consume API with Python
'''
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    employee = requests.get('{}users?id={}'.format(url, employee_id)).json()[0]
    request = requests.get('{}todos?userId={}'.format(url, employee_id)).json()
    name = employee.get('name')
    tasks = len(request)
    task_list = [todo.get("title") for todo in request
                 if todo.get('completed')]
    tasks_todo = len(task_list)
    msg = "Employee {} is done with tasks({}/{}):"
    print(msg.format(name, tasks_todo, tasks))
    [print("\t {}".format(i)) for i in task_list]

