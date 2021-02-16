from os import system, name

from templates import TEMPLATE, EMPTY, ROCK, PAPER, SCISSORS


def clear():
    system('clear') if name == 'posix' else system('cls')


def get_templates(choice1, choice2):
    '''match `choice1` and `choice2` to a template in `templates.py`'''
    TEMPLATES = {
        'rock': ROCK,
        'paper': PAPER,
        'scissors': SCISSORS
    }
    return TEMPLATES.get(choice1, EMPTY), TEMPLATES.get(choice2, EMPTY)


def show(choice1, choice2, result, points1, points2, winner):
    '''format and print TEMPLATE string in `templates.py`'''
    clear()
    if result == 'WIN':
        result += ' '
    if not winner:
        winner = ' ' * 8

    print(TEMPLATE.format(
        choice1[0:11],
        choice1[12:23],
        choice1[24:35],
        choice1[36:47],
        choice1[48:59],
        choice1[60:71],
        choice1[72:83],
        choice1[84:95],
        choice1[96:107],
        choice1[108:119],
        choice1[120:131],
        choice1[132:143],

        choice2[0:11],
        choice2[12:23],
        choice2[24:35],
        choice2[36:47],
        choice2[48:59],
        choice2[60:71],
        choice2[72:83],
        choice2[84:95],
        choice2[96:107],
        choice2[108:119],
        choice2[120:131],
        choice2[132:143],

        result,
        points1,
        points2,
        winner
    ))
