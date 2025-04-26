# Scrum board >> File System memory using json and task contains json format

# task:{"id":87,"title":"sdsd","by":"","to":""}

from json import *

# Initialize board with structured task objects
def retrieve():
    try:
        with open("dlithe.json", "r") as file:
            return load(file)
    except (FileNotFoundError, JSONDecodeError):
        return {"todo": [], "progress": [], "done": []}  # Default structure

def write(board):
    with open("dlithe.json", "w") as file:
        dump(board, file, indent=4)

# View tasks in a specific bucket
def viewBucket(bucket):
    dlithe_board = retrieve()
    if bucket not in dlithe_board:
        print("Invalid bucket:", bucket)
    else:
        print(dlithe_board[bucket])

# Add a task as a JSON object
def addTask(bucket):
    dlithe_board = retrieve()
    if bucket not in dlithe_board:
        print("Invalid bucket:", bucket)
        return

    # Adding task while maintaining workflow order
    if bucket == 'todo':
        task_id = int(input("Enter task ID: "))
        task_name = input("Enter task name: ")
        task_by = input("Task assigned by: ")
        task_to = input("Task assigned to: ")
        task = {"id": task_id, "name": task_name, "by": task_by, "to": task_to}
        todo_tasks = [t['id'] for t in dlithe_board['todo']]
        if task['id'] not in todo_tasks:
            dlithe_board[bucket].append(task)
            print("Task added to", bucket)
        else:
            print("already in",bucket)
    elif bucket == 'progress':
        task_id = int(input("enter task id.. "))
        todo_tasks = [t['id'] for t in dlithe_board['todo']]
        if task_id in todo_tasks:
            task = {}
            for each in dlithe_board['todo']:
                if each['id']==task_id:
                    task = each
                    break
            dlithe_board['todo'] = [t for t in dlithe_board['todo'] if t['id'] != task_id]
            dlithe_board[bucket].append(task)
            print("Task moved to", bucket)
        else:
            print("Task ID not found in 'todo'")
    elif bucket == 'done':
        task_id = int(input("enter task id.. "))
        progress_tasks = [t['id'] for t in dlithe_board['progress']]
        task = {}
        for each in dlithe_board['progress']:
            if each['id']==task_id:
                task = each
                break
        if task_id in progress_tasks:
            dlithe_board['progress'] = [t for t in dlithe_board['progress'] if t['id'] != task_id]
            dlithe_board[bucket].append(task)
            print("Task moved to", bucket)
        else:
            print("Task ID not found in 'progress'")

    write(dlithe_board)

# Command Line Interface (CLI)
while True:
    print("\n1. Add task\n2. View Bucket\nAny other key to exit")
    choice = input("Enter your choice: ")
    if choice == "2":
        bucket = input("Enter bucket name (todo/progress/done): ")
        viewBucket(bucket)
    elif choice == "1":
        bucket = input("Enter bucket name (todo/progress/done): ")
        addTask(bucket)
    else:
        break