import datetime
import pickle
choice=1
date=""
format = '%Y/%m/%d'

try:
    with open('todoist_data.pkl', 'rb') as file:
        todoist_data = pickle.load(file)
except:
    todoist_data={}
print("Welcome to the To-Doist app!")
task=True
while choice!=0:
    print("""
    0.exit
    1.Add new task
    2.View Tasks
    3.Delete/Mark as done
    Enter your choice - 
    """)
    choice=int(input())
    if choice==1:
        date=input("Enter the date when this task is to be added in yyyy/mm/dd or write today -")
        if date=="today":
            date=datetime.date.today()
        else:
            date=datetime.datetime.strptime(date, format).date()
        print("""
        Enter the task you wanna add , type exit one done
        """)
        while True:
            task=input()
            if task=="exit":
                break
            if date in todoist_data:
                todoist_data[date].append(task)
                print("Task added!")
            else:
                todoist_data[date]=[]
                todoist_data[date].append(task)
                print("Task added!")
    elif choice==2:
        date=input("Enter the date in yyyy/mm/dd or write today -")
        if date=="today":
            date=datetime.date.today()
        else:
            date=datetime.datetime.strptime(date, format).date()
        if date in todoist_data:
            for i in range(len(todoist_data[date])):
                print(i+1,".",todoist_data[date][i])
            input("press any key")
        else:
            print("No tasks for ",date)
            input("press any key")

    elif choice ==3:
        date=input("Enter the date in yyyy/mm/dd or write today -")
        if date=="today":
            date=datetime.date.today()
        else:
            date=datetime.datetime.strptime(date, format).date()
        if date in todoist_data:
            for i in range(len(todoist_data[date])):
                print(i+1,".",todoist_data[date][i])
            d=1
            while todoist_data[date]:
                d=input("Enter the task no. which you wanna delete, type exit when done,")
                if d=="exit":
                    break
                d=int(d)
                del todoist_data[date][d-1]
                print("task deleted!")
                for i in range(len(todoist_data[date])):
                    print(i+1,".",todoist_data[date][i])
        else:
            print("No tasks for ",date)
            input("press any key")
with open('todoist_data.pkl', 'wb') as file:
    pickle.dump(todoist_data, file)