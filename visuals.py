from os import system, name

from templates import TEMPLATE, TEMPLATE_SPACES, EMPTY, ROCK, PAPER, SCISSORS


def clear():
    system('clear') if name == 'posix' else system('cls')


def get_template(choice):
    '''match `choice` to a template in `templates.py`'''
    return {
        'rock': ROCK,
        'paper': PAPER,
        'scissors': SCISSORS
    }.get(choice, EMPTY)


def show(choices, result, player_points, ai_points, winner):
    '''format and print TEMPLATE string in `templates.py`'''
    clear()

    space_between_choice_names = ' ' * (
        (TEMPLATE_SPACES-2) - len(choices[0]+choices[1])
    )
    if result == 'WIN':
        result += ' '
    if not winner:
        winner = ' ' * 8
    template1 = get_template(choices[0])
    template2 = get_template(choices[1])

    print(TEMPLATE.format(
        template1[0:11],
        template1[12:23],
        template1[24:35],
        template1[36:47],
        template1[48:59],
        template1[60:71],
        template1[72:83],
        template1[84:95],
        template1[96:107],
        template1[108:119],
        template1[120:131],
        template1[132:143],

        template2[0:11],
        template2[12:23],
        template2[24:35],
        template2[36:47],
        template2[48:59],
        template2[60:71],
        template2[72:83],
        template2[84:95],
        template2[96:107],
        template2[108:119],
        template2[120:131],
        template2[132:143],

        choices[0],
        space_between_choice_names,
        choices[1],
        result,
        player_points,
        ai_points,
        winner
    ))
