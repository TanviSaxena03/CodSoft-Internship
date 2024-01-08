task = []
done = []

def insert(i):
    task.append(i)
    print("Task has been Added successfully/n")
    
def delete(i):
    print("Task '"+i+"' is deleted\n" )
    task.remove(i)
    
def completed(i):
    print("Task '"+i+"' has been successfully completed\n")
    task.remove(i)
    done.append(i)
    
def show():
    n = 1
    print("\nTaskes yet to be completed: \n")
    for t in task:
        print(str(n)+": "+ t+"\n")
        n = n + 1
    n = 1
    if (done != []):
        print("\n Completed Tasks: \n")  
        for t in done:
            print(str(n)+": "+ t+"\n")  
            n = n + 1
    else:
        print("\nNo task completed yet\n")
        
ch = 0
while (ch != 5):
    print("1) Add a new Task\n")
    print("2) Delete a Task\n")
    print("3) Mark a Task as Completed\n")
    print("4) Display the To-Do List\n")
    print("5) Exit\n")
    
    ch = input ("Enter your choice: ")
    if (ch == '1'):
        a = input("\nEnter Task: ")
        insert(a)
        
    elif (ch == '2'):
        a = input("\nEnter Task: ")
        delete(a)
        
    elif (ch == '3'):
        a = input("\nEnter Task: ")
        completed(a)
        
    elif (ch == '4'):
        show()
        
    else:
        exit()
