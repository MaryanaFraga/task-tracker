class Task:
    # Task's constructor
    def __init__(self, id, name, status, deadline):
        self.id = id
        self.name = name
        self.status = status
        self.deadline = deadline
    
    # Formatting the Task's object when used as a string
    def __str__(self):
        return f'{self.id} - {self.name} | {self.status} | {self.deadline}'


def menu():
    print("*** TASK MANAGER ***\n\n"
    "1 - CREATE NEW TASK\n"
    "2 - LIST TASKS\n"
    "3 - DELETE TAKS\n"
    "4 - EXIT\n")


def createNewTask():
    print("CREATING TASK: ")

    name = input("TYPE TASK'S NAME >>> ")
    deadline = input("TYPE TASKS DEADLINE (month/day) >>> ")
    print("\n")

    newTask = Task(len(task_array) + 1, name, 0, deadline)

    # If the new task was in fact created, it will be added by the end of the array
    if newTask:
        task_array.append(newTask)
        print("TASK ADDED SUCESSFULLY.\n")

    else:
        print("SOMETHING WENT WRONG.\n")

    print("ID - TASK | STATUS | DEADLINE\n")
    for task in task_array:
        print(task)


if __name__ == "__main__":
    task_array = []

    while(True):
        menu()
        option = input("TYPE YOUR OPTION (1-4) >>> ")
        print("\n")

        match option:
            case '1':
                createNewTask()
            case '2':
                print("LIST\n")
            case '3':
                print("DELETE\n")
            case '4':
                print("EXITING...\n")
                break
            case _:
                print("SORRY, NO OPTION MATCHED. TRY AGAIN.\n\n")