import random
import string
num  = int(input('Enter The Lenght of Password : '))
def Condition():
    character = string.ascii_letters + string.digits + string.punctuation
    Password = ''.join(random.sample(character,num)) 
    print("Password:", Password)
Condition()

