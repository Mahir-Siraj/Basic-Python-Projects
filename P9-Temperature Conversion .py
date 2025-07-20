# A INPUT FROM USER THAT THEY WANT TO CONVERT
print("Welcome to Temperature Conversion Program")
print("Available Conversions:")


# LIST OF TEMPERATURE CONVERSION 
Temperature_Convertion =(
    "1) Celsius to Fahrenheit\n"
    "2) Fahrenheit to Celsius\n"
    "3) Kelvin to Celsius\n"
    "4) Celsius to Kelvin\n"
    "5) Kelvin to Fahrenheit\n"
    "6) Fahrenheit to Kelvin"
)


print(Temperature_Convertion)


# TAKING INPUT OF USER OF WHICH TEMPERATURE THEY WANT TO CONVERT
n = input("Enter the number of conversions you want to perform From Following List : ").lower()


# DEFINING THE FUNCTION OF TEMPERATURE CONVERTION 
def Temperature_Conversion(n):
   
# HANDLES ERROR IF USER WRITE INVALID INPUT 
    while True:
        if n not in ['celsius to fahrenheit', 'fahrenheit to celsius', 'kelvin to celsius', 'celsius to kelvin', 'kelvin to fahrenheit', 'fahrenheit to kelvin']:
            print("Invalid conversion option. Please choose from the list.")
            n = input("Enter your choice again: ").lower()
        else:
            break
            
            
# CELSIUS TO FAHRENHEIT

  
    if(n == 'celsius to fahrenheit'):
        celsius = 'Enter temperature in celsius: '
        while True:
            try:
                celsius = float(input(celsius))

# try: begins a block where Python will attempt to run the code that may raise an exception.
# input(celsius) shows the prompt message stored in the celsius variable and waits for user input.
# The user's input is converted to a float using float().
# If the user enters a valid number like "25.3", it gets converted to 25.3.
# If they enter a non-numeric value like "hello", it raises a ValueError.


            except ValueError:
                print("Invalid ! Please Enter A Number .")

# If the conversion to float fails (because the user didn't enter a valid number), a ValueError is raised.
# The except block catches this error and prints "invalid" to let the user know their input was not valid.
# The loop then continues, prompting the user again.


            else:
                 break

# If no exception is raised (i.e., the input is a valid float), the else: block runs.
# break exits the loop, meaning we have a valid number and don’t need to ask again.

        fahrenheit = (celsius * 9/5) + 32
        print(f'{celsius}°C is equal to {fahrenheit}°F')
        

#  FAHRENHEIT TO CELSIUS      


    elif(n == 'fahrenheit to celsius'):
        fahrenheit = 'Enter temperature in Fahrenheit: '
        while True:
            try:
                fahrenheit = float(input(fahrenheit))
            except ValueError:
                 print("Invalid ! Please Enter A Number")
            else:
                  break
        celsius = (fahrenheit - 32) * 5/9
        print(f'{fahrenheit}°F is equal to {celsius}°C')


# KELVIN TO CELSIUS


    elif(n == 'kelvin to celsius'):
        kelvin = 'Enter temperature in Kelvin: '
        while True:
            try:
                kelvin = float(input(kelvin))
            except ValueError:
                print("Invalid ! Please Enter A Number")
            else:
                break
        celsius = kelvin - 273.15
        print(f'{kelvin}K is equal to {celsius}°C')
        

# CELSIUS TO KELVIN


    elif(n == 'celsius to kelvin'):
       celsius = 'Enter temperature in Celsius: '
       while True:
           try:
               celsius = float(input(celsius))
           except ValueError :
               print("Invalid ! Please Enter A Number")
           else:
                break
       kelvin = celsius + 273.15
       print(f'{celsius}°C is equal to {kelvin}K')
       
       
# KELVIN TO FAHRENHEIT


    elif(n == 'kelvin to fahrenheit'):
        kelvin  = ' Enter temperature in Kelvin: '
        while True :
            try:
                kelvin = float(input(kelvin))
            except ValueError:
                print("Invalid ! Please Enter A Number")
            else:
                 break
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        print(f'{kelvin}K is equal to {fahrenheit}°F')


# FAHRENHEIT TO KELVIN 


    elif(n == 'fahrenheit to kelvin'):
        fahrenheit = 'Enter temperature in Fahrenheit: '
        while True :
            try:
                fahrenheit = float(input(fahrenheit))
            except ValueError:
                print("Invalid ! Please Enter A Number")
            else:
                break
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        print(f'{fahrenheit}°F is equal to {kelvin}K')
 
 
 # CALLING THE FUNCTION
Temperature_Conversion(n)



