# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 10:16:15 2017

@author: Devlin
"""

### Mad Libs ###


## Improvements to make:
    ### 1. Write 5 libs

import random as rn

def madlib():
    global over
    over = False
    choose_lib = rn.randrange(1, 4)  
    print("""Let's play some madlibs. Just fill in the prompts with what they ask for
and be rewarded with humor beyond belief!""")
    print("-" * 65)
    def lib1():
        pers = input("A Person: ")
        act = input("An Anction Verb, ending in -ing: ")
        loc = input("A Location: ")
        adj1 = input("An Adjective: ")
        thing1 = input("An Animal or Thing: ")
        verb = input("A Verb, present tense: ")
        verb2 = input("Another Verb, present tense: ")
        thing2 = input("Another Thing, singular: ")
        mf = input("Men or Women: ")
        name = input("Your Name: ")
        print("-" * 65)
        print("""You and %s are %s in %s when you come accross a %s %s!
%s doesn't know what to do but you know that in order to %s a %s %s,
you must %s a %s. Over the objections of %s, you successfuly %s. Beautiful %s
rush to you in your victory. Fireworks go off and you are given the key to %s.
LONG LIVE %s!!!""" %(pers, act, loc, adj1, thing1, pers, verb, adj1, thing1, verb2, thing2, pers, verb2, mf, loc, name))
    
    def lib2():
        hero = str(input("A Superhero: "))
        vill = str(input("A Villain: "))
        pers = str(input("A Person: "))
        loc = str(input("A Location: "))
        ad = str(input("An Adjective: "))
        ad2 = str(input("Another Adjective: "))
        ad3 = str(input("And Another Adjective: "))
        thing = str(input("A Thing, plural: "))
        act = str(input("An Action, not ending in -ing: "))
        act2 = str(input("An Action, ending in -ing: "))
        act3 = str(input("Another Action, ending in -ing: "))
        fact = str(input("A Fighting Action: "))
        print("-" * 65)
        print("""You and %s are exploring the dangerous %s %s, a place where the %s %s is said to live.
While %s is looking at some rather %s %s, you decide to %s by yourself. 
SUDDENLY, %s appears before you and starts %s. You run and scream while %s is still busy %s.
Before %s can catch up to you, %s flies in from out of nowhere! %s takes one look at %s and delivers a %s
that makes all of %s shake like jello, and knocks you to your feet. When you stand, %s is gone and %s is 
standing over you, laughing and holding a cape. Turns out %s was %s THE WHOLE TIME!""" 
% (pers, ad, loc, ad2, vill, pers, ad3, thing, act, vill, act2, pers, act3, vill, hero, hero, vill, fact, loc, hero, pers, pers, hero))
        
    def lib3():
        pers1 = input("A Person: ")
        pers2 = input("A Second Person: ")
        time = input("A Period of Time: ")
        loc1 = input("A Location: ")
        loc2 = input("A Second Location: ")
        loc3 = input("A Third Location: ")
        ad1 = input("An Adjective: ")
        ad2 = input("Another Adjective: ")
        thing1 = input("A Thing, plural: ")
        thing2 = input("Another Thing: ")
        act1 = input("An Action: ")
        
        
        # (pers1, pers2, time, pers2, loc1, pers1, loc2, loc3, ad1, thing1, pers1, ad2, thing2, pers2, act1)
        print("-" * 65)
        print("""%s and %s have been best friends since %s but today that friendship would be tested. When %s wanted to go to %s, %s wanted to visit %s. 
They eventually decided to go to %s in order to see all the %s %s. Despite this compromise, %s kept getting crankier and crankier until finally they yelled '%s, you %s %s!'.
%s started %s with rage. Then they both died. Moral of the story is Devlin isnt very creative and we should give him points for trying"""
% (pers1, pers2, time, pers2, loc1, pers1, loc2, loc3, ad1, thing1, pers1, ad2, thing2, pers2, act1))
    
    if choose_lib == 1:
        lib1()
        over = True
    elif choose_lib == 2:
        lib2()
        over = True
    elif choose_lib == 3:
        lib3()
        over = True
    else:
        print("Run again")


