# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 20:25:28 2017

@author: Devlin
"""

import random as rn
    
def guess():
    global over 
    over = False
    print("Lets play a guessing game!")
    
    l = int(input("Choose a lower bound: "))
    u = int(input("And now choose an upper bound: "))
    
    a = rn.randrange(l, u)
    guesses_taken = 1
    
    print("a is a random number between %s and %s" %(l, u))
    
    a_guess = int(input("Take a guess: "))
    
    while a_guess != a:
        
        if a_guess > u or a_guess < l:
            print("Guess out of bounds!")
            a_guess = int(input("Guess again: "))
            guesses_taken += 1
        elif a_guess > a and a_guess <= u:
            print("You guessed too high")
            a_guess = int(input("Guess again: "))
            guesses_taken += 1
        else:
            print("Too Low")
            a_guess = int(input("Guess again: "))
            guesses_taken += 1
            
    if a_guess == a:
        print("JUST RIGHT")
        print("And in %d guesses too!" %guesses_taken)
        if guesses_taken == 1:
            print("Im sooooo proud of you!")
        over = True
