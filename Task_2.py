def add(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)

def mul(a, b):
    return (a * b)

def div(a, b):
    if (b != 0):
        return (a / b)
    return ("Cannot be divided by 0")

ch = 0
while (ch != 5):
    print("1) Add two numbers\n")
    print("2) Subtract two numbers \n")
    print("3) Multiply two numbers\n")
    print("4) Divide two numbers\n")
    print("5) Exit\n")
    
    ch = input ("Enter your choice: ")
    
    if (ch == '5'):
        exit()
        
    x = eval (input ("\nEnter 1st Number: "))
    y = eval (input ("\nEnter 2nd Number: "))
    
    if (ch == '1'):
        print(x," + ",y," = ",add(x,y))
        
    elif (ch == '2'):
        print(x," - ",y," = ",sub(x,y))
        
    elif (ch == '3'):
        print(x," * ",y," = ",mul(x,y))
        
    elif (ch == '4'):
        print(x," / ",y," = ",div(x,y))
        
    else:
        print("\nInvalid choice\n")