# Scrum board >> File System memory using json

from json import load,dump

# dlithe_board = {
#     "todo":[],
#     "progress":[],
#     "done":[]
# }

def retrieve():
    with open("dlithe.json","r") as file:
        return load(file)
def write(board):
    with open("dlithe.json","w") as file:
        dump(board,file,indent=4)

# view tasks in user given bucket
def viewBucket(bucket):
    dlithe_board = retrieve()
    if not bucket in dlithe_board: print("Invalid",bucket)
    else:
        print(dlithe_board[bucket])
# map the task into bucket
def addTask(bucket,task):
    dlithe_board = retrieve()
    if not bucket in dlithe_board: print("Invalid",bucket)
    else:
        if bucket == 'todo':
            if task not in dlithe_board[bucket]:
                dlithe_board[bucket].append(task)
                print(task,"added in",bucket)
            else:
                print(task,"already in",bucket)
        elif bucket == 'progress':
            if task in dlithe_board['todo']:
                dlithe_board['todo'].remove(task)
                dlithe_board[bucket].append(task)
                print(task,"added in",bucket)
            else:
                print(task,"already in",bucket,"/",task,"not in todo")
        elif bucket == 'done':
            if task in dlithe_board['progress']:
                dlithe_board['progress'].remove(task)
                dlithe_board[bucket].append(task)
                print(task,"added in",bucket)
            else:
                print(task,"already in",bucket,"/",task,"not in progress")
    write(dlithe_board)

# command line interface/ CLI
while True:
    print("1. Add task\n2.View Bucket\nAny to exit")
    choice = int(input("enter the choice "))
    if choice == 2: 
        bucket = input("tell us bucket name(todo/progress/done) ")
        viewBucket(bucket)
    elif choice == 1:
        bucket = input("tell us bucket name(todo/progress/done) ")
        task = input("tell us task to add "+bucket)
        addTask(bucket,task)
    else: break