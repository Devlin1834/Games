# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 22:33:28 2017

@author: Devlin
"""

## Magic Eight Ball

import random as rn

def magic():
    print("Ask the Magic Eight Ball ANY Question!")
    input("> ")    
    ans = rn.randint(1, 9)
    
    if ans == 1:
        print("It is certain")
    elif ans == 2:
        print("Decidedly so")
    elif ans == 3:
        print("Yupers")
    elif ans == 4:
        print("Reply Hazy, try again")
    elif ans == 5:
        print("Ask again later")
    elif ans == 6:
        print("Concentrate and ask again")
    elif ans == 7:
        print("My reply is no")
    elif ans == 8:
        print("Outlook not so good")
    elif ans == 9:
        print("Very doubtful")
        
