import json
import os
import datetime

tasks =[]

#json file
if not os.path.exists("tasksfile.json"):
    with open("tasksfile.json", "w") as f:
        json.dump(tasks, f)


def all_tasks():
    with open("tasksfile.json","r") as f:
        try :
            tasks = json.load(f)
        except json.JSONDecodeError:
            tasks = []

    print("all tasks : ")
    if tasks == []:
        print("you dont have any task")
    else:
        print(tasks)


def tasks_done():
    with open("tasksfile.json","r") as f:
        try :
            tasks = json.load(f)
        except json.JSONDecodeError:
            tasks = []

    print("List all tasks that are done : ")
    done_list = []
    for item in tasks:
        if item["status"]== "done":
            done_list.append(item)
    if done_list == []:
        print("You have no tasks marked as done")
    else:
        print(done_list)


def task_not_done():
    with open("tasksfile.json","r") as f:
        try :
            tasks = json.load(f)
        except json.JSONDecodeError:
            tasks = []

    print("List all tasks that are not done : ")
    not_done_list = []
    for item in tasks:
        if item["status"] != "done":
            not_done_list.append(item)
    if not_done_list == []:
        print("all task are done")
    else:
        print(not_done_list)



def task_progress():
    with open("tasksfile.json","r") as f:
        try :
            tasks = json.load(f)
        except json.JSONDecodeError:
            tasks = []

    print("List all tasks that are progress : ")
    progress_list = []
    for item in tasks:
        if item["status"] == "progress":
            progress_list.append(item)
    if progress_list == []:
        print("not any progress")
    else:
        print(progress_list)
        

def add_task():
    with open("tasksfile.json", "r") as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            tasks = []

    new_task = {
    "id": len(tasks) + 1,
    "description": input("add your task: "),
    "status": "todo",
    "createdAt": str(datetime.datetime.now()),
    "updatedAt": str(datetime.datetime.now())
    }
    print(f"your new task added : {new_task}")
    tasks.append(new_task)

    with open("tasksfile.json", "w") as f:
        json.dump(tasks, f, indent=4)
    

def remove_task():
    with open("tasksfile.json","r") as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            tasks = []
    
    print("Which task would you like to delete?")
    print(tasks)
    id = int(input("Please enter the ID of the task you wish to delete : "))
    task_found = False
    for i, task in enumerate(tasks):
        if task["id"] == id:
            tasks.pop(i)
            task_found = True
            print("Task removed.")
            break

    if not task_found:
        print("Task with that ID not found.")

    with open("tasksfile.json","w") as f:
        json.dump(tasks, f, indent=4)
    print("removed your task")



def update_task():
    with open("tasksfile.json", "r") as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            tasks = []

    print("Which task would you like to update?")
    print(tasks)
    id = int(input("Please enter the ID of the task you wish to update : "))
    task_found = False

    for task in tasks:
        if task["id"] == id:
            print(f"Current task: {task}")
            new_desc = input("Update description (leave blank to keep current): ")
            if new_desc.strip() != "":
                task["description"] = new_desc

            new_status = input("Update status (type 'done' or 'progress'): ").strip().lower()
            if new_status in ["done", "progress"]:
                task["status"] = new_status
            else:
                print("Invalid status. Must be 'done' or 'progress'. Keeping old status.")

            task["updatedAt"] = str(datetime.datetime.now())
            task_found = True
            print(f"Task updated: {task}")
            break

    if not task_found:
        print("Task with that ID not found.")

    with open("tasksfile.json", "w") as f:
        json.dump(tasks, f, indent=4)
    print("Saved updated task.")



#menu
def menu():
    while True:
        print("My ToDo list :) ")
        print("1.List all tasks")
        print("2.List all tasks that are done")
        print("3.List all tasks that are not done")
        print("4.List all tasks that are in progress")
        print("5.Add task")
        print("6.Remove task")
        print("7.Update task")
        print("8.Exit")

        choise = input("enter your num : ")
        if choise == "1":
            all_tasks()
        elif choise == "2":
            tasks_done()
        elif choise == "3":
            task_not_done()
        elif choise == "4":
            task_progress()
        elif choise == "5":
            add_task()
        elif choise == "6":
            remove_task()
        elif choise == "7":
            update_task()        
        elif choise == "8":
            break
        else:
            print("enter num between (1-8)")

menu()