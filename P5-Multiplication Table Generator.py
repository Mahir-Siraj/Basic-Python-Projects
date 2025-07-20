print("Welcome to the Multiplication Table Generator!")
print("This program will generate a multiplication table for a number you provide.")
print("Please enter an integer to get started.")
def user_input(prompt):
    while True:
        try:
            n = int(input(prompt)) # THIS CONVERT THE INPUT INTO INTEGER IF IT FAILS SO EXCEPT BLOCK WILL EXECUTE
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
        else:
            break
    return n

def Multiplication_Table(n):
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')

n=user_input("Enter a number for the multiplication table: ")
Multiplication_Table(n)

