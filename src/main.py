import json

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

     # Method to turn Task's objects into dictionaries
    def to_dict(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "status" : self.status,
            "deadline" : self.deadline
        }

    # This function doesn't belong to any instance, but to the class, that's why @classmethod
    # That's also why it doesn't call self as a parameter
    # It turns the dictionary into a Task object
    # AT LEAST THAT'S WHAT I UNDESTOOD UNTILL NOW
    @classmethod
    def from_dict(Animal, data):
        return Animal(**data)

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


def listTasksMenu():
    listTasks()

    # This is a menu for future features
    print("1 - FILTER    2 - UPDATE     3 - GO BACK")
    option = input("TYPE YOUR OPTION (1-3) >>> ")
    print("\n")

    match option:
            case '1':
                print("FILTER TASKS")
            case '2':
                print("UPDATE A TASK")
            case '3':
                return
            case _:
                print("SORRY, NO OPTION MATCHED.\n\n")


def listTasks():
    print("ID - TASK | STATUS | DEADLINE\n")
    for task in task_array:
        print(task)


def deleteTaskMenu():
    listTasks()
    id = int(input("TYPE TASK ID >>> "))
    for task in task_array:
        if id == task.id:
            task_array.remove(task)
            print(f"TASK N({id}) WAS REMOVED.")

def help():
    print("\n\n"
    ">>> add <task-in-quotes>\n"
    ">>> update <task-id> <new-task-in-quotes>\n"
    ">>> delete <task-id>\n"
    ">>> list\n"
    ">>> mark-in-progress <task-id>\n"
    ">>> mark-done <task-id>\n"
    ">>> list done\n"
    ">>> list to-do\n"
    ">>> list in-progress\n")


if __name__ == "__main__":
    try:
        with open("task-tracker/src/tasks.json", mode = "r") as open_file:
            tasks_data_dict = json.load(open_file)
                
    except:
        tasks_data_dict = []

    task_array = []

    for d in tasks_data_dict:
        t = Task.from_dict(d)
        task_array.append(t)

    while(True):
        menu()
        option = input("TYPE YOUR OPTION (1-4) >>> ")
        print("\n")

        match option:
            case '1':
                createNewTask()
            case '2':
                listTasksMenu()
            case '3':
                deleteTaskMenu()
            case '4':
                print("EXITING...\n")
                break
            case _:
                print("SORRY, NO OPTION MATCHED. TRY AGAIN.\n\n")

    tasks_data_dict = []

    for t in task_array:
        d = Task.to_dict(t)
        tasks_data_dict.append(d)

    with open("task-tracker/src/tasks.json", mode = "w") as open_file:
        json.dump(tasks_data_dict, open_file, indent=4)