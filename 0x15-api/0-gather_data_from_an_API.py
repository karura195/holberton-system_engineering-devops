#!/usr/bin/python3
'''
Consume API with Python
'''
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    # GET  METHOD
    user = requests.get('{}users?id={}'.format(url, user_id)).json()[0]
    request = requests.get('{}todos?userId={}'.format(url, user_id)).json()
    name = user.get('name')
    tasks = len(request)
    # Method : List Comprehension
    task_list = [todo.get("title") for todo in request
                 if todo.get('completed')]
    tasks_todo = len(task_list)
    string = "Employee {} is done with tasks({}/{}):"
    print(string.format(name, tasks_todo, tasks))
    [print("\t {}".format(i)) for i in task_list]
