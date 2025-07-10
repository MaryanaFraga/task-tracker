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
    

if __name__ == "__main__":
    while(True):
        menu()
        option = input("TYPE YOUR OPTION (1-4) >>> ")
        print("\n")

        match option:
            case '1':
                print("CREATE\n")
            case '2':
                print("LIST\n")
            case '3':
                print("DELETE\n")
            case '4':
                break
            case _:
                print("SORRY, NO OPTION MATCHED. TRY AGAIN.\n\n")