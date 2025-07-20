# CALCULATOR PROGRAM WITH EXCEPTION HANDLING

print('Welcome to the Calculator Program')

# EXCEPTION HANDLING FOR CHOICE BETWEEN CALCULATOR AND FACTORIAL

method = ['1) Calculator' ,'Factorial']
p = input('\nDo You want Calculator or Find Factorial ? [Calculator/Factorial] : ').lower()
while True:
    if p not in ['calculator' , 'factorial']:
        print(f'\nInvalid ! Please Enter A Method From Following Option {method} \n')
        p = input('Choose From This Two Option Calculator or Find Factorial ? [Calculator/Factorial] : ').lower()
    else:
        break


# IF USER CHOOSE CALCULATOR SO IT TAKES INPUT FOR CALCULATOR 
if p == 'calculator':
    print('\nYou have chosen Calculator')


# ERROR HANDLING FOR FIRST INPUT
    while True:
        try:
            a = int(input("\nEnter an First Number : "))
        except ValueError:
            print('\nInvalid ! Please Enter A Number.')
        else:
            print(f'\nYour First Operand = {a}')
            break
        

# ERROR HANDLING FOR SECOND INPUT
    while True:
        try:
            b = int(input('\nEnter Your Second Number : '))
        except ValueError:
            print('\nInvalid ! Please Enter A Number.')
        else:
            print(f'\nYour Second Operand = {b}')
            break

# ERROR HANDLING FOR THIRD INPUT        
    c = input('\nEnter Your Sign [(+) , (-) , (*) , (/) , (%) , (^) ] : ')
    while True:
        if c not in  ['+' , '-' , '*' , '/' , '%' , '^']:
            print('\nInvalid ! Please Enter A Sign From Given List  ')
            c = input('\nEnter Your Sign [(+) , (-) , (*) , (/) , (%) , (^) ] : ')
        else:
            print(f'\nYour Operator Is {c}')
            break

# DEFINING A FUNCTION WHICH USED TO CALCULATE 

    def calculator(a, b, c):

    # FOR ADDITION
        if(c=='+'):
            print(f'\nYour Answer Is = {a+b}')

    # FOR SUBTRACTION
        elif(c=='-'):
            print(f'\nYour Answer Is = {a-b}')
    
    # FOR MULTIPLICATION
        elif(c=='*'):
            print(f'\nYour Answer Is + {a*b}')

    # FOR DIVISION
        elif(c=='/'):
            while(b==0):
                try:
                    if(b==0):
                        print(f'\nYour Answer Is = {a/b}')
                except ZeroDivisionError:
                    print('\nEnter a Suitable Number (demonitor never zero)')
                    b=int(input(f'\nAgain Enter The Number : '))
                    if(b!=0):
                        print(f'Your Answer Is = {a/b}')
    
    # FOR POWER

        elif(c=='^'):
            print(f'\nYour Answer Is = {a**b}')

    # FOR MODULUS
        elif(c=='%'):
            while(b==0):
                try:
                    if(b==0):
                        print(f'\nYour Answer Is = {a/b}')
                except ZeroDivisionError:
                    print(f'\nInvalid ! The Divisor Never Will Be Zero ')
                    b = int(input(f'\nAgain Enter The Proper Divisor = '))
                    if(b!=0):
                        print(f'\nYour Answer Is = {a%b}')

    # CALLING THE FUNCTION SO THAT FUNCTION CAN WORK

    calculator(a,b,c)

# IF USER CHOOSE FACTORIAL 
elif p == 'factorial':
    print('\nYou have chosen Factorial')

# IF USER CHOOSE FACTORIAL SO IT TAKES THE INPUT FROM USER
# INPUT VALIDATION LOOP
while True:
    try:
        n = int(input('\nEnter a Number for Factorial: '))
        if n < 0:
            print('\nInvalid! Factorial is not defined for negative numbers.')
            continue
    except ValueError:
        print('\nInvalid! Please enter a valid integer.')
    else:
        break

# MAIN FUNCTION FOR FACTORIAL
if n == 0 or n == 1:
    print(f'\nYour Answer For Factorial of {n} = 1')
else:
    fact = 1
    for i in range(2, n + 1):  # start from 2 since multiplying by 1 is redundant
        fact *= i
    print(f'\nYour Answer For Factorial of {n} = {fact}')

