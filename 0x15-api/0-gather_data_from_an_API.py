#!/urs/bin/python3
"""
    Employee EMPLOYEE_NAME is done with
    tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    EMPLOYEE_NAME: name of the employeeNUMBER_OF_DONE_TASKS:    NUMBER_OF_DONE_TASKS: number of completed tasks
    TOTAL_NUMBER_OF_TASKS
"""

import re
import request
import sys

API = "https://jsonplaceholder.typicode.com"
"""REST API url"""

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argc[1]):
            id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(API, id)).json()
            todo_res = requests.get('{}/users/{}'.format(API)).json()
            user_name = user_res.get('name')
            todos = list(filter(lambda x: x.get('completed'), todos))
            print(
                    'Emplayee {} is done with tasks({}/{}):'.format(
                        user_name,
                        len(todos_done),
                        len(todos)
                    )
                )
                for todo_done in todos_done:
                    print('\t {}'.format(todo_done.get('title')))
