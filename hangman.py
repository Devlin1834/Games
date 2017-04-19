# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:39:33 2017

@author: Devlin
"""

## Hangman

## Improvements to make:
    ### 1. define victory word
    ### 2. Fix Strike Counting System

import random as rn


def hangman():
    global over
    
    words = {1: "atmospheric", 
         2: "xlographic", 
         3: "keyboarding",
         4: "uncopyrightable",
         5: "geophysical",
         6: "troublemaking",
         7: "dumbwaiter",
         8: "haricots",
         9: "juxtaposed",
         10: "trapezoids",
         11: "centrifugals",
         12: "demonstrably",
         13: "playgrounds",
         14: "workmanship",
         15: "postcardlike",
         16: "exhaustingly",
         17: "artichoke",
         18: "hospitable",
         19: "nefariously",
         20: "shockingly"}

    over = False
    h = rn.randrange(1, len(words.keys())+1)
    pick = words[h]
    
    print("Lets play a game of hangman")
    print("You guess letters and when you fail, someone dies lol")
    print("You get to fail six times before I actually kill this guy")
    print("""           
                      O    <Please Don't let me die!
                     /|\\
                     / \\                                                 
                       """)
    print("Oh and the game is case-sensitive, so only use lower case letters")
    print("Lets get started")
    print("-" * 65)
    print("Your word is " + str(len(pick)) + " letters long")
    print("")
    print("_" * len(pick))

    blanks = list('_' * len(pick))

    letters = list(pick)

    k = 1

    h_guess = input("Make a guess: ")
    
    old_guesses = []

    while blanks.count('_') != 0 and k < 6:
            
        if len(h_guess) > 1:
            print("Thats not a legal guess")
            print("")
            h_guess = input("Guess again: ") 
        else:
            if h_guess in letters:
                pound = letters.index(h_guess)
                blanks[pound] = h_guess
                print("".join(blanks))
                old_guesses.append(h_guess)
                print("""
So far you've used: """)
                print(", ".join(old_guesses))
                print("")

                if blanks.count('_') == 0:
                    print(pick + "!")
                    print("You Win!")
                    over = True
                else:
                    h_guess = input("Guess again: ")

            else:
                print("WRONG!, thats one strike")
                k += 1
                print("%d strikes left" %(7-k))
                old_guesses.append(h_guess)
                print("""
So far you've used: """)
                print(", ".join(old_guesses))
                print("")
                h_guess = input("Guess again: ")

    if k == 6:
        print("He died")
        print("""
                       S
                       O
                      /U\\
                      /`\\
                      """)
        print("I know you want to see the word but I don't reward failure")
        print("GAME OVER")
        over = True
