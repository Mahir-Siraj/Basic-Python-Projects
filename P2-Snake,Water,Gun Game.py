import random 
list=['snake','water','gun']
game_choice=random.choice(list)
User_input=input('Enter Your Choice : (Snake , Water , Gun) = ' ).lower()
def game(game_choice,User_input):
    while(game_choice==User_input):
        print('It is a draw')
        User_input=input('Again Enter Your Choice : (Snake , Water , Gun) = ' ).lower()
        
    if((game_choice=='snake') and (User_input=='water')):
        print('You Lose because Snake  can drink the water . ')
    elif((game_choice=='water') and (User_input=='snake')):
        print('You Win bcz Snake can drink the water .')
    elif((game_choice=='water')and (User_input=='gun')):
        print('You Lose because Water can drown the gun . ')
    elif((game_choice=='gun')and (User_input=='water')):
        print('You Win Because Water can drown the gun .')
    elif((game_choice=='gun')and (User_input=='snake')):
        print('You Lose Because gun can shoot the snake . ')
    elif((game_choice=='snake')and(User_input=='gun')):
        print('You Win Because gun can shoot the snake .')

game(game_choice,User_input)

# ANOTHER WAY


def game():
    while True:
        choices = ['snake', 'water', 'gun']
        game_choice = random.choice(choices)
        user_input = input('Enter Your Choice: (Snake, Water, Gun) = ').lower()

        if game_choice == user_input:
            print("It's a draw!\n")
            continue

        if game_choice == 'snake' and user_input == 'water':
            print("You Lose because Snake drinks the Water.\n")
        elif game_choice == 'water' and user_input == 'snake':
            print("You Win! Snake drinks the Water.\n")
        elif game_choice == 'water' and user_input == 'gun':
            print("You Lose! Water drowns the Gun.\n")
        elif game_choice == 'gun' and user_input == 'water':
            print("You Win! Water drowns the Gun.\n")
        elif game_choice == 'gun' and user_input == 'snake':
            print("You Lose! Gun shoots the Snake.\n")
        elif game_choice == 'snake' and user_input == 'gun':
            print("You Win! Gun shoots the Snake.\n")
        break  # stop after one full round

game()
    