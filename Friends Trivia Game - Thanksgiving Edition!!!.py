#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Friends Trivia Game Pyhton3 Code 

""""
@author: rosabel.bassil

"""

"""
DocString:
    
    A) Introduction:
    Welcome to the FRIENDS TRIVIA GAME - Save Thanksgiving Edition! In this 
    game you have the following 3 three rounds.
    
    Round 1: Guess the answer to unlock the right door. 
    Round 2:Name the Characters to save thanksgiving. 
    Round 3:Guess the season and WIN to receive your final prize 
           “The Thanksgiving Geller Cup”.
    Round 4:Randomly get a Friends Character to have Thanskgining dinner with.
    B) Known Bugs and/or Errors:
    None.

"""
#import exit to code to exit game
from sys import exit
#import random which will be used to randomly pick a number in round 4
import random

def game_start():
#declaring global variables    
    global contestant_name
    global new_contestant_name
#input prompt contestant name variable
    contestant_name= input(prompt= 'Enter your name to start the game: \n')
#print start game intro
    print(f"""
    \n Hello, {contestant_name} a friends fan or possibly a non-friends fan
    wanting to know more about the Friends series.
    Welcome to the Friends Trivia Game - Save Thanksgiving Edition!\n""")
    
    print(f"""\n 
    So, {contestant_name}, would you liked to be called Joey or Rachel 
    during the Game? 
    \n""")
    
    #input prompt new contestant name variable to be chosen from 2 names Joey and Rachel
    new_contestant_name= input(prompt= 'Enter your new game name from the above Friends character names\n')
    new_contestant_name = new_contestant_name.lower()
    
    #use if, else statement incase user doesn't type name correctly,they have to repeat the game
    if new_contestant_name == "joey"  or new_contestant_name== "rachel":
        print(f"""Amazing {new_contestant_name.capitalize()}, let's start the game!!!
    """)
        new_contestant_name = new_contestant_name.capitalize()
        round_1()

    else:  
        print(f""" Oh, I'm sorry {contestant_name}, you have to choose Joey or Rachel and spell it correctly.

    """)
        fail()

#define round 1

def round_1():

#input dynamic variable to continue
    
    input('\n\n<Press enter to continue>\n\n')
    
#print instructions
    print(f"""
In round 1 you have to guess the answer to unlock the right door to 
Monica's Secret Closet! 

Win this round to go to round to go to round 2 and cook the Turkey!
You have one chance {contestant_name}, oh I meant {new_contestant_name}.
Let's get started!!!
             
             """)
#input dynamic variable to start round 1 
    input('<Press enter to start Round 1>\n')

#number of tries allowed    
    tries = 2 


#use the while loop where the player has 2 tries only to choose both answers correctly. 
#the player can choose 2 answers before losing the whole round
#if, elif and else conditions are also used  to help display the correct, wrong and non-existing answer choices
#if, else are used to either fail the game if the player uses both tries or go to question 2 if player still has tries
#finally when the round is over and both questions are answered correctly the player can jump to round 2
#if the player doesnt guess question 2 correctly and has no more tries he/she has to repeat the game    
   
   
    while tries > 0:
        print("""
    Q1. Which two characters were friends in high school??

    (a) Phoebe & Monica
    (b) Ross & Joey
    (c) Monica & Rachel

        """)
        answer1 = (input(prompt = "choose between a, b or c:\n  ")).lower()
        
        if answer1 == 'a' or answer1 == 'b':
            tries -= 1
            print(f"""Incorrect. You lost one of your tries. {tries} left.""")
            
        elif answer1 == 'c':
            print("you got it correct!")
            break
        else:
            print("Incorrect Entry. Try again")
            tries -= 1
            
    if tries <= 0:
        print("You are out of lives.")
        fail()
    else:
        while tries > 0:
            print("""

Q2. Joey doesn’t share?

(a) Food
(b) Clothes
(c) Women

            """)
            answer1 = (input(prompt = "choose between a, b or c:\n  ")).lower()

            if answer1 == 'c' or answer1 == 'b':
                tries -= 1
                print(f"""Incorrect. You lost one of your tries. {tries} left.""")

            elif answer1 == 'a':
                print("you got it correct!")
                break
            else:
                print("Incorrect Entry. Try again")
                tries -= 1
        if  tries <= 0:
            print("""
Oops sorry! Seems like you unlocked the wrong door and accidentally walked in
on Rachel showering ! She is furious!!!""")
            fail()
            
        print("Congrats on completing round 1. You have unlocked the door to Monica’s Secret Closet.")
        round_2()
    

#round 2 is defined at first, dynamic variable are inputed and intructions are also printed 
#the player has to guess between two questions, and for each question answered correctly score is incremented by one
#to win and move to round 3 the player has to get a score of 1 out of 2 
#if,elif,else conditions are used here and as long as the  player's score is greater than "0" they win the round
#if players score is zero they fail and can repeat the game

def round_2():

    input('<Press enter to continue>\n')
   
    print(f""" 
    
Welcome to round 2 where you have to name the character that said the quote
Ross, Phoebe, Joey, Monica, Rachel, Chandler

""")
    score = 0
    
    print("""
We were on a break!
             1) Joey
             2) Ross
             3) Rachel
             4) Monica
    """)
    answer2 = (input(prompt = "Who said that?\n")).lower()
    incorrect_list = ["1","3","4","joey","rachel","monica"]

    if answer2 == "ross" or answer2 == "2":
        score += 1
        print(f"YAYYYYY You got it right. Current score: {score}")
    elif answer2 in incorrect_list:
        print(f"Unfortunately, it was not {answer2}")
    else:
        print("Incorrect entry.")
    
    print("""
OH!!  MY EYES!!! MY EYES!!!
             1) Joey
             2) Ross
             3) Rachel
             4) Phoebe
    """)
    answer2 = (input(prompt = "Who said that?\n")).lower()
    incorrect_list = ["1","3","2","joey","rachel","ross"]

    if answer2 == "phoebe" or answer2 == "4":
        score += 1
        print(f"YAYYYYY You got it right. Current score: {score}")
    elif answer2 in incorrect_list:
        print(f"Unfortunately, it was not {answer2}")
    else:
        print("Incorrect entry.")
        
    if score > 0:
        print(f"""
Yayy {new_contestant_name}! You got at least one correct answer and saved Thanksgiving. 
In order to receive the Geller Cup you will now have to complete Round 3!
        """)
        round_3()
    
    else:
        fail()
        

#round 3 is defined at first, dynamic variables are inputed and intructions are also printed  
#here the player has to guess the correct season 
#if the season is guessed correctly the player wins, else he/she can repeat the game
#a list of correct answers that might be typed in is given hereas well


def round_3():
    input('<Press enter to continue>\n')
    list_correct_answer = ["season 4", "season 4", "4", "season four"]
    
    print(f""" 
    
Congrats on cooking the turkey!It smells Amazing! All you have to do now 
{new_contestant_name} is to type in the correct season to win the Geller 
Cup!

""")

    print(f"""
"Ross gets married for the second time after Carol, but not to Rachel. 
While at the alter Ross mistakes his bride's name and calls Rachel’s name
instead."
    """) 
 
    season = input(prompt= 'Enter the season number in which these events occured:\n') 
    if season in list_correct_answer:
        print("Congrats! You have proved to be a FRIENDS FANATIC! You may now claim your Geller Cup.")
        round_4()
    else:
        print(f"""
        Sorry… You may not claim the Geller Cup this Thanksigiving. You can always try agin next 
        year
            """)
            
        fail()
        
#round 4 is defined at first, dynamic variables are inputed and intructions are also printed  
#the random variabe is used here where the player gets a random number from 1 to 6
#the random number represents the character the randomly selected Friends character the player gets to have Thansgiving dinner with

def round_4():
    print("""
You're not done yet! You're in for a treat. You get to have a Thanksgiving 
dinner with one of the Friends characters. Press enter to randomly get a Friends
character. 

    """)
    input("Press enter to continue...\n")
    answer4 = random.randint(1,6)
    
    if answer4 == 1:
        print("""
        You get to have a dinner with Joey! 
        Enjoy it! It was lovely playing with you!
        
        """)
    
    elif answer4 == 2:
        print("""
        You get to have a dinner with Monica! 
        Enjoy it! It was lovely playing with you!
        
        """)
    
    elif answer4 == 3:
        print("""
        You get to have a dinner with Ross! 
        Enjoy it! It was lovely playing with you!
        """)
    
    elif answer4 == 4:
        print("""
        You get to have a dinner with Rachel! 
        Enjoy it! It was lovely playing with you!
        
        """)
    
    elif answer4 == 5:
        print("""
        You get to have a dinner with Chandler! 
        Enjoy it! It was lovely playing with you!
        
        """)
    
    elif answer4 == 6:
        print("""
        You get to have a dinner with Phoebe! 
        Enjoy it! It was lovely playing with you!
        
        """)
   
    else:
        print("THERE IS SOMETHING WRONG!!!!!")
    
    
    
#fail function is defined
#print what comes up when player losess and they can either repeat the game or end it  
#define the replay variable as well which takes the player to the start of the game          
    

def fail():
    print(f"""

Ooops, {contestant_name}, looks like you've lost
the game!

             """)
    
    print(f" Would you like to play again? (Yes/No)")
    replay = input("> ")
    replay = replay.lower()
    
    if replay == 'yes':
        game_start()
        
    elif replay == 'no':
        print(f" Thanks for playing {contestant_name}!")
        exit(0)
    else:
        print("Something went wrong. Let's try again")
        fail()

game_start()


# In[ ]:




