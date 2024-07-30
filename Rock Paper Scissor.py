print('''
 _____                                                     _____ 
( ___ )---------------------------------------------------( ___ )
 |   |                                                     |   | 
 |   |  _____           _        _____                _    |   | 
 |   | /  __ \         | |      /  __ \              | |   |   | 
 |   | | /  \/ ___   __| | ___  | /  \/ __ _ _ __ ___| |_  |   | 
 |   | | |    / _ \ / _` |/ _ \ | |    / _` | '__/ _ \ __| |   | 
 |   | | \__/\ (_) | (_| |  __/ | \__/\ (_| | | |  __/ |_  |   | 
 |   |  \____/\___/ \__,_|\___|  \____/\__,_|_|  \___|\__| |   | 
 |___|                                                     |___| 
(_____)---------------------------------------------------(_____)
''')
#Project: Implement a Console-Based Rock, Paper, Scissors Game
#Objective: Create a simple text-based Rock, Paper, Scissors game that allows a user to play against the computer.

#Rules-->
'''
Rock wins against Scissor
Scissor wins against Paper
Paper wins against Rock
'''

import random
option=['rock','paper','scissor']

def play(option):
    usr_choice=input('Enter your choice (rock,paper,scissor): ').lower()
    if usr_choice in option:
        com_choice=random.choice(option)
        print('Computer choice: ',com_choice)
        if com_choice==usr_choice:
            print("It's a tie")
        elif (com_choice=='rock') and usr_choice=='paper':
            print('You win!')
        elif com_choice=='rock' and usr_choice=='scissor':
            print('You loss!')
        elif com_choice=='paper' and usr_choice=='scissor':
            print('You win!')
        elif com_choice=='paper' and usr_choice=='rock':
            print('You loss!')
        elif com_choice=='scissor' and usr_choice=='rock':
            print('You win!')
        elif com_choice=='scissor' and usr_choice=='paper':
            print('You loss!')
        
        more_play=input('Want to play more(y/n): ').lower()
        if more_play=='y':
            play(option)
    else:
        print('Invalid option. Choose again: ')
        play(option)
play(option)
    