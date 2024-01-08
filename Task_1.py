task = []
done = []

def insert(i):
    task.append(i)
    
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
