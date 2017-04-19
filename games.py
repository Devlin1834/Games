# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 18:34:52 2017

@author: Devlin
"""

## Package Imports ##

import madlib as mad
import hangman as hang
import rps
import rand
import caps
import aliens
import yourname
import magic
import collatz

### Global Variable Deffinition ###

over = True

### Pick a Game ### 
 
while over is True:
    print("-" * 65)
    print("Lets play a game!")

    print("""We Have 
            0. Quit  
            1. Guess The number
            2. Hangman
            3. Rock - Paper - Scissors
            4. Madlibs
            5. Guess The State Capital
            6. Alien Attack
            7. Your Name
            8. Magic Eight Ball
            9. The Collatz Sequence
            """)

    game = int(input("Input the number of the game we're playing: "))
    print("-" * 65)
    
    if game == 1:
        rand.guess()
    elif game == 2:
        hang.hangman()
    elif game == 3:
        rps.rps()
    elif game == 4:
        mad.madlib()
    elif game == 5:
        caps.caps_game()
    elif game == 6:
        aliens.a_game.play()
    elif game == 7:
        yourname.yourname()
    elif game == 8:
        magic.magic()
    elif game == 9:
        collatz.collatz()
    elif game == 0:
        print("Bye!")
        over = False
    else:
        print("There isnt a game like that")