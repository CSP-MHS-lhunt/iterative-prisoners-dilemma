'''
Names: Griffin,Luke,Jack,Casey
Iterative Prisoner's Dillema Team Submission

In this file, you MUST define the following:

Variables:
  - team_name:            a string with your team's name
  - strategy_name:        a string with your team's strategy name
  - strategy_description: a string with your team's strategy name

Functions:
  - move(my_last_move, their_last_move):
    your team's implementation of your strategy (see move() docstring)
'''

team_name = 'TEAM 5'
strategy_name = '123 punish'
strategy_description = 'If the other team colludes we will collude but if they betray we will betray for three times and then go back to colluding if they are colluding again as well'
punish = 0
def move(my_last_move, their_last_move):
    '''
    Make my move based on the history with this player.

    my_last_move: a one letter String (c or b) that represents the last move you made
        against your opponent
    their_last_move: a one letter String (c or b) that represents the last move your
        opponent made against you
    Returns 'c' or 'b' for collude or betray.
    '''
    global punish
    if(their_last_move == 'b' or 0<punish <=3):
        punish= punish +1
        if(punish>3):
            punish == 0
        return 'b'
    else:
        return 'c'

if __name__ == '__main__':
    print(move('',''))
    print(move('c','c'))
    print(move('c','b'))
    print(move('b','b'))
    print(move('b','c'))
