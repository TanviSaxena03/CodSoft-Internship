import random
import string

def password(n):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    pswd = ""
    
    for i in range(n):
        pswd = pswd + random.choice(chars)
        
    return pswd   

num = eval(input("\nEnter length of Password: ")) 
print("\nGenerated Password:", password(num))