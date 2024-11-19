from datetime import datetime


def add_task(tasks, task):
    """
    Adds a new task to the task list.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task (dict): The task to be added.

    Returns:
    list of dict: Updated list of tasks.
    """
    # adding the new task, by appending it to the tasks list
    tasks.append(task)
    return tasks

def remove_task(tasks, task_id):
    """
    Removes a task by its ID.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be removed.

    Returns:
    list of dict: Updated list of tasks.
    """
    # removing the task, first checking if the given id is in any of the dicts, then if it is, we proceed to delete it
    for task in tasks:
        if task_id in task.values():
            tasks.remove(task)
    return tasks

def update_task(tasks, task_id, updated_task):
    """
    Updates an existing task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    updated_task (dict): The updated task details.

    Returns:
    list of dict: Updated list of tasks.
    """

    # loops through a task in tasks, checks if id is found
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            tasks[i] = {**task, **updated_task}
            return tasks
    return tasks

def get_task(tasks, task_id):
    """
    Retrieves a task by its ID.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be retrieved.

    Returns:
    dict: The task with the specified ID, or None if not found.
    """
    description = ''
    priority = ''
    deadline = ''
    # iterates until it finds a corresponding id in task, then prints the task in the following format
    for task in tasks:
        if task['id'] == task_id:
            description = task['description']
            priority = task['priority']
            deadline = task['deadline']
            status = task['completed']
            return (f'Description: {description}\n'
                    f'Priority: {priority}\n'
                    f'Deadline: {deadline}\n'
                    f'Status:{status}')
    return None



def set_task_priority(tasks, task_id, priority):
    """
    Sets the priority of a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    priority (str): The new priority level.

    Returns:
    list of dict: Updated list of tasks.
    """
    # iterates until it finds a corresponding id in task, changes the priority, then prints the task in the following format
    for task in tasks:
        if task['id'] == task_id:
            task['priority'] = priority
            return tasks
    return tasks




def set_task_deadline(tasks, task_id, deadline):
    """
    Sets the deadline for a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    deadline (str): The new deadline.

    Returns:
    list of dict: Updated list of tasks.
    """
    # iterates until it finds a corresponding id in task, changes the deadline, then prints the task in the following format
    for task in tasks:
        if task['id'] == task_id:
            task['deadline'] = deadline
            return tasks
    return tasks


def mark_task_as_completed(tasks, task_id):
    """
    Marks a task as completed.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be marked as completed.

    Returns:
    list of dict: Updated list of tasks.
    """
    # iterates until it finds a corresponding id in a task, then sets it as completed and returns it
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            return tasks
    return tasks



def set_task_description(tasks, task_id, description):
    """
    Sets the description for a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    description (str): The new description.

    Returns:
    list of dict: Updated list of tasks.
    """
    # iterates until it finds a corresponding id in task, changes the description, then prints the task in the following format
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            return tasks
    return tasks


def search_tasks_by_keyword(tasks, keyword):
    """
    Searches tasks by a keyword in the description.

    Parameters:
    tasks (list of dict): The current list of tasks.
    keyword (str): The keyword to search for.

    Returns:
    list of dict: Tasks that contain the keyword in their description.
    """
    #iterates until it finds a keyword in a task, then returns the ones that have it
    task_with_keyword = []
    for task in tasks:
        if keyword in task['description']:
            task_with_keyword.append(task)
    if task_with_keyword:
        return task_with_keyword
    return None

def filter_tasks_by_priority(tasks, priority):
    """
    Filters tasks by priority.

    Parameters:
    tasks (list of dict): The current list of tasks.
    priority (str): The priority level to filter by.

    Returns:
    list of dict: Tasks with the specified priority.
    """
    # iterates until the priority matches the given one, returns all with the same priority
    task_with_priority = []
    for task in tasks:
        if priority == task['priority']:
            task_with_priority.append(task)
    if task_with_priority:
        return task_with_priority
    return None
def filter_tasks_by_status(tasks, status):
    """
    Filters tasks by their completion status.

    Parameters:
    tasks (list of dict): The current list of tasks.
    status (bool): The completion status to filter by.

    Returns:
    list of dict: Tasks with the specified completion status.
    """
    # iterates,until the given status matches a task's status
    task_with_status = []
    for task in tasks:
        if status == task['completed']:
            task_with_status.append(task)
    if task_with_status:
        return task_with_status
    return None

def filter_tasks_by_deadline(tasks, deadline):
    """
    Filters tasks by their deadline.

    Parameters:
    tasks (list of dict): The current list of tasks.
    deadline (str): The deadline to filter by.

    Returns:
    list of dict: Tasks with the specified deadline.
    """
    # iterates,until the given deadline matches a task's deadline
    task_with_deadline = []
    for task in tasks:
        if deadline == task['deadline']:
            task_with_deadline.append(task)
    if task_with_deadline:
        return task_with_deadline
    return None
def count_tasks(tasks):
    """
    Returns the total number of tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The total number of tasks.
    """
    return len(tasks)


def count_completed_tasks(tasks):
    """
    Returns the number of completed tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The number of completed tasks.
    """
    num_of_completed_tasks = 0
    for task in tasks:
        if task['completed']:
            num_of_completed_tasks += 1
    return num_of_completed_tasks


def count_pending_tasks(tasks):
    """
    Returns the number of pending tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The number of pending tasks.
    """
    num_of_uncompleted_tasks = 0
    for task in tasks:
        if not task['completed']:
            num_of_uncompleted_tasks += 1
    return num_of_uncompleted_tasks


def generate_task_summary(tasks):
    """
    Generates a summary report of all tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    dict: A summary report containing total, completed, and pending tasks.
    """
    completed_tasks = 0
    pending_tasks = 0
    for task in tasks:
        if task['completed']:
            completed_tasks += 1
        pending_tasks += 1
    return f" total tasks - {len(tasks)}, completed tasks - {completed_tasks}, pending tasks - {pending_tasks}"

def save_tasks_to_file(tasks, file_path):
    """
    Saves the task list to a file.

    Parameters:
    tasks (list of dict): The current list of tasks.
    file_path (str): The path to the file where tasks will be saved.

    Returns:
    None
    """
    file = open(file_path,"w")
    file.write(tasks)
    file.close()

def load_tasks_from_file(file_path):
    """
    Loads the task list from a file.

    Parameters:
    file_path (str): The path to the file where tasks are saved.

    Returns:
    list of dict: The loaded list of tasks.
    """
    my_file = open(file_path, "rt")
    contents = my_file.read()
    my_file.close()
    print(contents)


def sort_tasks_by_deadline(tasks):
    """
    Sorts tasks by their deadline.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    list of dict: The sorted list of tasks.
    """
    for task in tasks:
        task['deadline'] = datetime.strptime(task['deadline'], "%Y-%m-%d")
    return sorted(tasks, key=lambda task: task['deadline'])

def sort_tasks_by_priority(tasks):
    """
    Sorts tasks by their priority.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    list of dict: The sorted list of tasks.
    """
    return sorted(tasks, key=lambda task: task['priority'])

def print_menu():
    """
    Prints the user menu.
    """
    menu = """
    Task Manager Menu:
    1. Add Task
    2. Remove Task
    3. Update Task
    4. Get Task
    5. Set Task Priority
    6. Set Task Deadline
    7. Mark Task as Completed
    8. Set Task Description
    9. Search Tasks by Keyword
    10. Filter Tasks by Priority
    11. Filter Tasks by Status
    12. Filter Tasks by Deadline
    13. Count Tasks
    14. Count Completed Tasks
    15. Count Pending Tasks
    16. Generate Task Summary
    17. Save Tasks to File
    18. Load Tasks from File
    19. Sort Tasks by Deadline
    20. Sort Tasks by Priority
    21. Exit
    """
    print(menu)


def main():
    tasks = []
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            task = {
                'id': int(input("Enter task ID: ")),
                'description': input("Enter task description: "),
                'priority': input("Enter task priority (low, medium, high): "),
                'deadline': input("Enter task deadline (YYYY-MM-DD): "),
                'completed': False
            }
            tasks = add_task(tasks, task)
            print("Task added successfully.")
        elif choice == '2':
            task_id = int(input("Enter task ID to remove: "))
            tasks = remove_task(tasks, task_id)
            print("Task removed successfully.")
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            updated_task = {
                'description': input("Enter new task description: "),
                'priority': input("Enter new task priority (low, medium, high): "),
                'deadline': input("Enter new task deadline (YYYY-MM-DD): ")
            }
            tasks = update_task(tasks, task_id, updated_task)
            print("Task updated successfully.")
        elif choice == '4':
            task_id = int(input("Enter task ID to get: "))
            task = get_task(tasks, task_id)
            print("Task details:", task)
        elif choice == '5':
            task_id = int(input("Enter task ID to set priority: "))
            priority = input("Enter new priority (low, medium, high): ")
            tasks = set_task_priority(tasks, task_id, priority)
            print("Task priority set successfully.")
        elif choice == '6':
            task_id = int(input("Enter task ID to set deadline: "))
            deadline = input("Enter new deadline (YYYY-MM-DD): ")
            tasks = set_task_deadline(tasks, task_id, deadline)
            print("Task deadline set successfully.")
        elif choice == '7':
            task_id = int(input("Enter task ID to mark as completed: "))
            tasks = mark_task_as_completed(tasks, task_id)
            print("Task marked as completed.")
        elif choice == '8':
            task_id = int(input("Enter task ID to set description: "))
            description = input("Enter new description: ")
            tasks = set_task_description(tasks, task_id, description)
            print("Task description set successfully.")
        elif choice == '9':
            keyword = input("Enter keyword to search: ")
            found_tasks = search_tasks_by_keyword(tasks, keyword)
            print("Tasks found:", found_tasks)
        elif choice == '10':
            priority = input("Enter priority to filter by (low, medium, high): ")
            filtered_tasks = filter_tasks_by_priority(tasks, priority)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '11':
            status = input("Enter status to filter by (completed/pending): ").lower() == 'completed'
            filtered_tasks = filter_tasks_by_status(tasks, status)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '12':
            deadline = input("Enter deadline to filter by (YYYY-MM-DD): ")
            filtered_tasks = filter_tasks_by_deadline(tasks, deadline)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '13':
            total_tasks = count_tasks(tasks)
            print("Total number of tasks:", total_tasks)
        elif choice == '14':
            completed_tasks = count_completed_tasks(tasks)
            print("Number of completed tasks:", completed_tasks)
        elif choice == '15':
            pending_tasks = count_pending_tasks(tasks)
            print("Number of pending tasks:", pending_tasks)
        elif choice == '16':
            summary = generate_task_summary(tasks)
            print("Task Summary:", summary)
        elif choice == '17':
            file_path = input("Enter file path to save tasks: ")
            save_tasks_to_file(tasks, file_path)
            print("Tasks saved to file.")
        elif choice == '18':
            file_path = input("Enter file path to load tasks from: ")
            tasks = load_tasks_from_file(file_path)
            print("Tasks loaded from file.")
        elif choice == '19':
            tasks = sort_tasks_by_deadline(tasks)
            print("Tasks sorted by deadline.", tasks)
        elif choice == '20':
            tasks = sort_tasks_by_priority(tasks)
            print("Tasks sorted by priority.", tasks)
        elif choice == '21':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()