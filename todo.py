# ------------------------------
# Simple To-Do App by Thomas Addisu
# Language: Python 3
# Features:
#   - Add, delete, view, and mark tasks as done
#   - Tasks are saved in text files for persistence
# ------------------------------

if __name__=="__main__":
        
    import json

    # write to a file

    # def save_tasks():
        # with open("todo.txt","wt") as file:
        #     for name,time in tasks.items():
        #         file.write(f"{name}|{time}\n")
        # with open("tododone.txt","wt") as file:
        #     for name,time in done_tasks.items():
        #         file.write(f"{name}|{time}\n")

    # write to json file

    def save_tasks():
        with open("todo.json","w") as file:
            json.dump(tasks,file)
        with open("tododone.json","w") as file:
            json.dump(done_tasks,file)


    tasks={}
    done_tasks={}

    # to load data from text file

    # try:
    #     with open("todo.txt","rt") as file:
    #         for line in file:
    #             task,time=line.strip().split("|")
    #             tasks[task]=time
    # except FileNotFoundError:
    #     pass
    # try:

    #     with open("tododone.txt","rt") as file:
    #         for line in file:
    #             task,time=line.strip().split("|")
    #             done_tasks[task]=time
    # except FileNotFoundError:
    #     pass

    #  a function load data from json file

    def json_load(path):
        try:
            with open(path,"r") as file:
                if not file:
                    return {}
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    tasks=json_load("todo.json")
    done_tasks=json_load("tododone.json")


    while True:
        print("\n📋 What do you want to do?")
        print(" 1️⃣  Add a task")
        print(" 2️⃣  Delete a task")
        print(" 3️⃣  View undone tasks")
        print(" 4️⃣  Mark a task as done")
        print(" Other number to exit")

        choice=input("enter:")
        
        cho=['1','2','3','4']  #use this strings to check the user choice not out from the list of choice
        if choice not in cho:
            break

        if choice=='1':
            task_name=input("enter task name:").lower()
            task_time=input("enter time:")
            tasks[task_name]=task_time
            print("✅ task added successfully!")
            save_tasks()        #save the task to be sure no file lose if program crash before the program end 
        elif choice=='2':
            task_name=input("enter the task name:").lower()
            remove_task=tasks.pop(task_name,None)
            if remove_task:
                print("✅ the task deleted")
            else:
                print("❌the task not found")
            save_tasks()
        elif choice=='3':
            print("task name    time")
            if tasks:
                for key,value in tasks.items():
                    print(f"{key}            {value}")
            else:
                print("NO undone task")
            save_tasks()
        else:
            task_name=input("enter the task name:").lower()
            if task_name in tasks.keys():
                done_tasks[task_name]=tasks[task_name]
                tasks.pop(task_name)
                print("Good you do well ✅")
            else:
                print("The task not found")
            save_tasks()

