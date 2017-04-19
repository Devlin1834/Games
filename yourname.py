# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 15:35:53 2017

@author: Devlin
"""

## Write your name


def yourname():
    global over
    over = False
    name  = ''
    tries = 0

    while name != 'your name':
        print("Write your name")
        name = input("> ")
        tries += 1
    print("Wow it took you %d tries" %tries)
    over = True