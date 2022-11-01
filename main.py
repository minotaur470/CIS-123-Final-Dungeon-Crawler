#CIS123 Final Project - Dominic Quist

#This project is a demonstration of basic principles learned throughout the
#course. It will be a basic game consisting of basic ASCII UI elements and 
#a rudimentary storyline. 

#import modules
import character
from titlescreen import title_screen_newgame, title_screen_loadgame
from msvcrt import getch
import os

os.system('cls') #clear screen

#initialize variables
titlescreen_chr = 'x'
gamestate = 0
health = 0
attack = 0
defense = 0



#Draw title screen
title_screen_newgame(titlescreen_chr)

#title screen manipulation
while 1==1:
    key = ord(getch())
    if key == 27: #esc
        gamestate = -1
        break
    elif key == 13: #enter
        if gamestate == 0: #newgame
            gamestate = 10
            os.system('cls')
            break
        elif gamestate == 1: #loadgame
            gamestate = 11
            os.system('cls')
            break
    elif key == 224: 
        key = ord(getch())
        if key == 80: #down
            if gamestate == 0:
                gamestate = 1
                os.system('cls') 
                title_screen_loadgame(titlescreen_chr)
            elif gamestate == 1:
                gamestate = 0
                os.system('cls')
                title_screen_newgame(titlescreen_chr)
        if key == 72: #up
            if gamestate == 1:
                gamestate = 0
                os.system('cls')
                title_screen_newgame(titlescreen_chr)
            elif gamestate == 0:
                gamestate = 1
                os.system('cls') 
                title_screen_loadgame(titlescreen_chr)
            
if gamestate == 10: #newgame
    username = input('What is to be the name of our hero?')
    user = character.character(username)
    print(f'Your name is {user.name}? What a heroic name.')
    current_user = open(f'users\{user.name}.txt','a')
    current_user.write(f'{user.name}\n{str(user.health)}\n{str(user.attack)}\n{str(user.defense)}\n')
    current_user.close()
    
if gamestate == 11: #loadgame
    username = input("What is our returning hero's name?")
    try:
        current_user = open(f'users\{username}.txt','r')
        print(f'Your name is {username}? What a heroic name.')
        username, health, attack, defense = character.pull_values(current_user)
        user = character.character(username,health,attack,defense)
        current_user.close()
    except:
        print("That user doesn't exist. I'll create a new user with that name.")
        user = character.character(username)
        current_user = open(f'users\{user.name}.txt','a')
        current_user.write(f'{user.name}\n{str(user.health)}\n{str(user.attack)}\n{str(user.defense)}\n')
        current_user.close()
        
gamestate = 20

#start game

        