import random

class Roll:
    def __init__(self, name, defeats, defeated_by):
        self.name = name
        self.defeats = defeats
        self.defeated_by = defeated_by

class Player:
    def __init__(self, name):
        self.name = name


def print_header():
    print('---------------------------------')
    print('    Rock Paper Scissors!')
    print('---------------------------------')

def build_rolls():
    rock = Roll('rock', 'scissors', 'paper')
    paper = Roll('paper', 'rock', 'scissors')
    scissors = Roll('scissors', 'paper', 'rock')
    return [rock, paper, scissors]

def get_player_name():
    name = (str(input('Enter your name: ')))
    return name

def player_select(rolls):
    selection = input('(R)ock, (P)aper, or (S)cissors? ')
    if selection.lower() == 'r':
        return rolls[0]
    if selection.lower() == 'p':
        return rolls[1]
    if selection.lower() == 's':
        return rolls[2]

def game_loop(player1, player2, rolls):
    count = 0
    p1_score = 0
    p2_score = 0
    while count < 3:
        p2_roll = random.choice(rolls)
        p1_roll = player_select(rolls)
        print(f'{player1.name} chooses {p1_roll.name} --- {player2.name} chooses {p2_roll.name}')
        if p1_roll.name == p2_roll.defeated_by:
            print(f'{player1.name} beats {player2.name} with {p1_roll.name}!')
            p1_score += 1
            count += 1
        elif p1_roll.name == p2_roll.defeats:
            print(f'{player2.name} beats {player1.name} with {p2_roll.name}!')
            p2_score += 1
            count += 1
        else:
            print('Tie! roll again...')
        print(f'The score is {p1_score} to {p2_score}')

    
def main():
    print_header()
    
    rolls = build_rolls()
    
    name = get_player_name()
    
    player1 = Player(name)
    player2 = Player('Computer')
    
    game_loop(player1, player2, rolls)


if __name__ == '__main__':
    main()