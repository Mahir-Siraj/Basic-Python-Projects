print("Welcome to the Number Guessing Game!")
print("In this game, you will try to guess a number between 1 and 100.")
print("You will receive feedback on whether your guess is too high, too low, or correct.")

def user_input(prompt):
    while True:
        try:
            n = int(input(prompt))
        except ValueError:
            print('invalid input, please enter a number.')
        else:
            break
    return n
# def Number_Guessing_Game(guess):  # guess = 0
number_to_guess = 42  # This can be randomized for a real game
attempts = 0
Total_Chance = 3
while attempts < Total_Chance: 
    guess = user_input('Enter your guess (between 1 and 100): ')
    attempts += 1
    if guess < number_to_guess:
        print('Your guess is too low.')
    elif guess > number_to_guess:
        print('Your guess is too high.')
    else:
        print('Congratulations! You guessed the number correctly.')
        break
else:
    print(f'Sorry, you have used all your chances. The number was {number_to_guess}.')
    exit()


