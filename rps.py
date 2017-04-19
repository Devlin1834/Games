# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 23:49:28 2017

@author: Devlin
"""

# Rock - Paper - Scissors

import random as rn
    

    
def rps():
    global over
    over = False
    comp = rn.randrange(1,4)
    if comp == 1:
        play = "rock"
    elif comp == 2:
        play = "paper"
    else:
        play = "scissors"
    
    anything = {1: "Flamethrower",
            2: "Grenade Launcher",
            3: "+1 Mace",
            4: "Scissors",
            5: "Lightsaber",
            6: "Jetpack",
            7: "Pike",
            8: "4 Hour Old Churro",
            9: "Laser Watch",
            10: "Sharp Dressed Man",
            11: "Advanced Trigonometric Identity",
            12: "Phaser, set to kill",
            13: "Pet T-Rex",
            14: "Sister who never shuts up",
            15: "Elder wand"}
     
    print("""The computer thinks it can beat you in Rock Paper Scissors
Try your best to prove it wrong
      
    Rule 1: no caps please
    Rule 2: no crazy shit from elementary school
    Rule 3: be a graceful loser
      
HAVE FUN!!!
-----------------------------------------------------------------""")
    you = input("ROCK, PAPER, SCISSORS, SHOOT! : ")
    win = False
    win2 = False   
        
    if you == "rock":
        if play == "paper":
            print("This is some hardcore paper, man")
            print("Its the best paper")
            print("No one can beat this paper")
            print("This is the kind of paper that donald trump leaves randsome notes on")
            print("This paper just CRUSHED your puny rock")
            print("LOSER")
            over = True
            
        elif play == "scissors":
            print("Rock crushes scissors")
            print("How did you win?")
            win = True
            
        elif play == "rock":
            print("Its a lame-o tie")
            over = True
            
    elif you == "scissors":
        if play == "paper":
            print("Scissors cuts paper")
            print("You win")
            win = True
            
        elif play == "rock":
            print("Rock crushes scissors")
            print("WHAT A LOSER YOU TURNED OUT TO BE")
            over = True
            
        elif play == "scissors":
            print("Its a lame-o tie")
            over  = True
            
    elif you == "paper":
        if play == "rock":      
            print("Paper beats rock")
            print("Somehow")
            print("YOU WIN")
            win = True
            
        elif play == "scissors":
            print("Scissors cuts paper")
            print("YOU LOSE")
            over = True
            
        elif play == "paper":
            print("Its a lame-o tie")
            over = True
            
    elif you =="lizzard" or you == "spock":
        print("We can't be friends anymore")
        over = True
        
    else:
        print("I dunno what you did but you lose")    
        over = True
        
    if win is True:
        print("-" * 65)
        print("The 'puter wants a rematch")
        print("nothing can shield you now!!!")
        rematch = input("ROCK, PAPER, SCISSORS, SHOOT! : ")
    
        if rematch == "scissors":
            print("The computer's mighty rock crushes your puny scissors")
            print("You LOSE!")
            over = True
            
        elif rematch == "paper":
            print("WHY would you chose paper??")
            print("The computers mighty scissors cut your paper into confetti for its birdthday party")
            print("YOU LOSE")
            over = True
            
        elif rematch == "rock":
            print("Your pebble is wrapped up and suffocated in paper")
            print("THE COMPUTER LAUGHS AT YOUR HUMILIATING DEFEAT")
            over = True
            
        elif rematch == "shoot":
            print("YOU SHOT THE COMPUTER")
            print("Computers dont bleed, moron")
            over = True
            
        elif rematch == "shield":
            print("The computer keeps throwing things at you but you keep blocking them")
            print("Your mighty fourth grade logic makes short work of the illogical computer")
            print("Victory is yours")
            win2 = True
        elif rematch == "lizzard" or rematch == "spock":
            print("get out of my house")
            print("NOW")
            over = True
            
        else:
            print("I dunno what that was but you lost, asshole")
            over = True
    
    if win2 is True:
        print("-" * 65)
        print("The computer is impressed by your ability to make up rules")
        print("It challenges you to a battle of ROCK PAPER SCISSORS ANYTHING!!")
    
        kill = anything[rn.randrange(1,16)]
    
        save = input("ROCK, PAPER, SCISSORS, ANYTHING! : ")
    
        live = rn.randrange(1,3)
    
        if live == 1:
            print("""The computer brought its %s,
but your skillful use of %s saved your life.
I think that computer was trying to kill you!
              
Congratulations on winning 3 rounds of Rock Paper Scissors""" %(kill, save))
            over = True
            
        elif live == 2:
            print("""Despite your expert use of %s,
the computer used its %s, and you didnt stand a chance.
             
The computer dances over your mutilated corpse.""" %(save, kill))
            over = True


    