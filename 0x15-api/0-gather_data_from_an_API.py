#!/usr/bin/python3
"""
    using REST API for employee ID
    Returning information about the TODO list progress.
"""

import requests

def get_employee_todo_progress(employee_id):
    # Make a GET request to the API
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todos = response.json()

    # Get the employee name
    employee_name = todos[0]['name'].split()[0]

    # Count the number of completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]
    number_of_done_tasks = len(completed_tasks)

    # Total number of tasks
    total_number_of_tasks = len(todos)

    # Display the progress
    print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):")

    # Display the completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")

# Prompt the user for an employee ID
employee_id = int(input("Enter the employee ID: "))

# Call the function to get the employee TODO list progress
get_employee_todo_progress(employee_id)   
