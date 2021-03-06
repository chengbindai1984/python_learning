# from __future__ import print_function

# Define and the board

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '
            }

# Dispay the board


def printBoard(board):

    print (board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print ('-+-+-')
    print (board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print ('-+-+-')
    print (board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# interaction with user input

turn = 'X'

for r in range(9):
    printBoard(theBoard)
    print ('Turn for'+  turn  +'. Move on which space ?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'o'
    else:
        turn = 'X'

printBoard(theBoard)
