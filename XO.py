def display_board(board):
    print(board[1])+ '|' +print(board[2])+ '|' +print(board[3])
    print('---------')
    print(board[4])+ '|' +print(board[5])+ '|' +print(board[6])
    print('---------')
    print(board[7])+ '|' +print(board[8])+ '|' +print(board[9])

def player_input():

    marker =' '
    while marker != 'X' and marker != 'O':
        marker = input('player1: Choose letter X or O  ').upper()

        if marker == 'X':
            return ('X','O')
        else:
            return('O','X')

def place_marker(board,position,marker):
    board[position] = marker

def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or 
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))

import random

def first_player():
    flip = random.randint(0,1)

    if flip == 0 :
        return 'player 1'
    else:
        return 'player 2'
    
def space_check(board,position):
    return board[position] == ' '

def check_full_board(board):
    for i in range (1,10):
        if space_check(board,i):
            return False
    return True

def player_choise():
    position = 0

    while position not in range (1,10):
        return int(input('Choose between 1-9: '))
    
def replay():
    return input('Do you want to play again?  ')

print('Welcom to the game!')

while True:

    theboard = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = first_player()
    print(turn +' will begin')

    play_game =input('Are you ready?:y or n ').lower
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        
        if turn == 'player1':            

            display_board(theboard)
            position = player_choise(theboard)
            place_marker(theboard,position,player1_marker)

        if win_check(theboard,player1_marker):
            display_board(theboard)
            print('Congratulation player 1 has won the game! ')
            game_on = False

        else:
            if check_full_board(theboard):
                display_board(theboard)
                print('The game is draw')
                game_on = False

            else: 
                turn = 'player 2'

    else:
        display_board(theboard)
        position = player_choise(theboard,position)
        place_marker(theboard,player2_marker,position)

        if win_check(theboard):
            display_board(theboard)
            print('Congratulation player 2 has won the game!')
            game_on = False

        else:
            if check_full_board(theboard):
                display_board(theboard)
                print('The game is draw')
                game_on = False

            else:
                turn = 'player 1'

    if not replay:
        break