# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 19:15:31 2017

@author: Devlin
"""

### State Capitals

import random as rn

def caps_game():
    
    caps = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Connecticut": "Hartford",
        "Delaware": "Dover",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta",
        "Hawaii": "Honolulu",
        "Idaho": "Boise",
        "Illinois": "Springfield",
        "Indiana": "Indianapolis",
        "Iowa": "Des Moines",
        "Kansas": "Topeaka",
        "Kentucky": "Frankfort",
        "Louisiana": "Baton Rouge",
        "Maine": "Augusta",
        "Maryland": "Annapolis",
        "Massachusetts": "Boston",
        "Michigan": "Lansing",
        "Minnesota": "Saint Paul",
        "Mississippi": "Jackson",
        "Missouri": "Jefferson",
        "Montana": "Helena",
        "Nebraska": "Lincoln",
        "Nevada": "Carson City",
        "New Hampshire": "Concord",
        "New Jersey": "Trenton",
        "New Mexico": "Santa Fe",
        "New York": "Albany",
        "North Carolina": "Raleigh",
        "North Dakota": "Bismark",
        "Ohio": "Columbus",
        "Oklahoma": "Oklahoma City",
        "Oregon": "Salem",
        "Pennsylvania": "Harrisburg",
        "Rhode Island": "Providence",
        "South Carolina": "Columbia",
        "South Dakota": "Pierre",
        "Tennessee": "Nashville",
        "Texas": "Austin",
        "Utah": "Salt Lake City",
        "Vermont": "Montpelier",
        "Virginia": "Richmond",
        "Washington": "Olympia",
        "West Viginia": "Charelston",
        "Wisconsin": "Madison",
        "Wyoming": "Cheyenne"}
    
    global over
    over = False
    print("Lets play a fun game!")
    print("I'm going to give you a state, and you tell me its capital")
    print("This game is case sensitive so use caps where appropriate")
    print("And HAVE FUN!")
    print("-" * 65)
    
    game_length = int(input("First tell me how many you want to guess: "))
    if game_length >50:
        game_length = 50
        print("I like your enthusiasm, but we only have 50 states at the moment")
    
    game_list = rn.sample(list(caps), game_length)

    played = 0
    
    correct = 0
    
    while played != game_length:
        print(game_list[played])
        print('Whats that capital?')
        your_cap = input("> ")
        if your_cap == caps[game_list[played]]:
            print("Good guess!")
            print("")
            played += 1
            correct += 1
        elif your_cap != caps[game_list[played]]:
            print("Nope, its actually:")
            print(caps[game_list[played]])
            print("")
            played += 1
        else:
            print("What happened? ABBORT")
            over = True
    
    if played == game_length:
        print("Congrats! You got %d out of %d correct!" %(correct, game_length))
        over = True
