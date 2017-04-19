# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:14:09 2017

@author: Devlin
"""

## Tic Tac Toe

import random as rn

global over

the_Board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(' ' + board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'])
    print('---+---+---')
    print(' ' + board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'])
    print('---+---+---')
    print(' ' + board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'])
    
printBoard(the_Board)

turn = 'X'
for i in range(9):
    printBoard(the_Board)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    the_Board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
        
## Full Game Found
# http://inventwithpython.com/chapter10.html