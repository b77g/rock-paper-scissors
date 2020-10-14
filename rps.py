from random import choice
from os import system, name

OPTIONS = {
    'rock': ('rock', 'r'),
    'paper': ('paper', 'p'),
    'scissors': ('scissors', 's')
    }
BEST_OF = None
game_active = True
player_points = 0
comp_points = 0

def parse(choice1, choice2):
    if choice1 in OPTIONS[choice2]:
        return 'DRAW'
    elif choice1 in OPTIONS['rock']:
        return 'WIN' if choice2 in OPTIONS['scissors'] else 'LOSS'
    elif choice1 in OPTIONS['paper']:
        return 'WIN' if choice2 in OPTIONS['rock'] else 'LOSS'
    elif choice1 in OPTIONS['scissors']:
        return 'WIN' if choice2 in OPTIONS['paper'] else 'LOSS'

def add_points(player_choice, comp_choice):
    global player_points, comp_points
    if parse(player_choice, comp_choice) == 'WIN':
        player_points += 1
    elif parse(player_choice, comp_choice) == 'LOSS':
        comp_points += 1

def get_winner():
    global game_active
    if player_points == BEST_OF:
        game_active = False
        return 'YOU WON'
    elif comp_points == BEST_OF:
        game_active = False
        return 'YOU LOST'
    elif player_points == BEST_OF / 2 + 0.5:
        if comp_points < player_points:
            game_active = False
            return 'YOU WON'
    elif comp_points == BEST_OF / 2 + 0.5:
        if player_points < comp_points:
            game_active = False
            return 'YOU LOST'

def clear():
    system('clear') if name == 'posix' else system('cls')

def set_up():
    clear()
    global BEST_OF
    while BEST_OF not in [1, 3, 5]:
        try:
            BEST_OF = int(input('best of (1/3/5): '))
        except:
            continue

    print('options: (r)ock, (p)aper, (s)cissors')
    input('hit ENTER to start ')
    clear()

def update(player_choice, comp_choice):
    result = parse(player_choice, comp_choice)
    add_points(player_choice, comp_choice)
    winner = get_winner()

    visualize(player_choice, comp_choice, result, winner)

def visualize(player_choice, comp_choice, result, winner):
    clear()
    print(f'| your choice: {player_choice}')
    print(f'| AI\'s choice: {comp_choice}')
    print(f'| {result} >>> {player_points}-{comp_points}')
    if winner != None:
        print(winner)

def main():
    set_up()

    while game_active:
        comp_choice = choice([k for k in OPTIONS])
        player_choice = input('- your choice: ').strip().lower()

        if player_choice in ('rock', 'r', 'paper', 'p', 'scissors', 's'):
            update(player_choice, comp_choice)
        elif player_choice == 'q':
            quit()

if __name__ == '__main__':
    main()
