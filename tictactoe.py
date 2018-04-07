#! /usr/bin/python3
#tictactoe game

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
 print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
 print('-+-+-')
 print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
 print('-+-+-')
 print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def isBoardComplete(board):
    a = (board['top-L'] == board['top-M'] == board['top-R']) and (board['top-L'] != ' ')
    b = (board['mid-L'] == board['mid-M'] == board['mid-R']) and (board['mid-L'] != ' ')
    c = (board['low-L'] == board['low-M'] == board['low-R']) and (board['low-L'] != ' ')
    d = (board['top-L'] == board['mid-L'] == board['low-L']) and (board['top-L'] != ' ')
    e = (board['top-M'] == board['mid-M'] == board['low-M']) and (board['top-M'] != ' ')
    f = (board['top-R'] == board['mid-R'] == board['low-R']) and (board['top-R'] != ' ')
    g = (board['top-L'] == board['mid-M'] == board['low-R']) and (board['top-L'] != ' ')
    h = (board['low-L'] == board['mid-M'] == board['top-R']) and (board['top-R'] != ' ')
    return any((a,b,c,d,e,f,g,h))

turn  = 'X'

for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if(isBoardComplete(theBoard)):
        printBoard(theBoard)
        print('Hey ' + turn + ': You won')
        break
    if turn == 'X':
        turn ='0'
    else:
        turn = 'X'
else:
    printBoard(theBoard)
    print('Game drew')
