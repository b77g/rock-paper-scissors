from random import choice
from visuals import get_templates, show, clear

game_active = True
best_of = None
player_points = 0
ai_points = 0
WIN_CASES = (
    ('rock', 'scissors'),
    ('paper', 'rock'),
    ('scissors', 'paper')
)
VALID_CHOICES = set(
    [j for i in WIN_CASES for j in i]
    + [j[0] for i in WIN_CASES for j in i]
)

def match(choice):
    '''match `choice` to a valid word in `WIN_CASES`'''
    CHOICE_WORDS = (x for x in VALID_CHOICES if len(x) > 1)
    for valid_choice in CHOICE_WORDS:
        if choice == valid_choice or choice[0] == valid_choice[0]:
            return valid_choice

def parse(player_choice, ai_choice):
    if player_choice == ai_choice:
        return 'DRAW'
    return 'WIN' if (player_choice, ai_choice) in WIN_CASES else 'LOSS'

def add_points(player_choice, ai_choice):
    global player_points, ai_points
    if parse(player_choice, ai_choice) == 'WIN':
        player_points += 1
    elif parse(player_choice, ai_choice) == 'LOSS':
        ai_points += 1

def get_winner():
    global game_active
    majority = best_of / 2 + 0.5
    if player_points == majority or ai_points == majority:
        game_active = False
        return 'YOU WON!' if player_points > ai_points else 'YOU LOST'

def setup():
    clear()
    print(
        'options: '
        + ', '.join(f'({x[0]}){x[1:]}' for x in VALID_CHOICES if len(x) > 1)
    )
    global best_of
    while best_of not in (1, 3, 5):
        try:
            best_of = int(input('best-of (1/3/5): '))
        except:
            continue
    clear()

def update(player_choice, ai_choice):
    player_choice = match(player_choice)
    ai_choice = match(ai_choice)
    result = parse(player_choice, ai_choice)
    add_points(player_choice, ai_choice)
    templates = get_templates(player_choice, ai_choice, VALID_CHOICES)
    show(*templates, result, player_points, ai_points, get_winner())

def main():
    setup()
    while game_active:
        player_choice = input('> your choice: ').strip().lower()
        ai_choice = choice(tuple(VALID_CHOICES))
        if player_choice in VALID_CHOICES:
            update(player_choice, ai_choice)
        elif player_choice in ('quit', 'exit'):
            quit()

if __name__ == '__main__':
    main()
