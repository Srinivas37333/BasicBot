"""
In this file we mainly focused on different types to 
wish the user at the begining of conversation.
Also we would like our bot to wish the user based on current time.
"""
from datetime import datetime
import random
from time import time

def give_part_of_day():
    """
    It gives current part  of day.
    """
    time=str(datetime.now()).split()[-1]
    h=[int(j) for j in time.split(':')[:-1]][0]
    part_of_day=""
    if(h<12):
        part_of_day="Morning"
    elif(h<16):
        part_of_day="After Noon"
    else:
        part_of_day="Evening"
    return part_of_day,h

def give_starting_wish():
    '''It returns a wish based on current time'''
    part_of_day=give_part_of_day()[0]
    wishes=[f"Good {part_of_day}!\n",f"Hello! Very Good {part_of_day} Buddy!!!\n",]
    random.seed(time())
    return random.choice(wishes)

def greet(bot_name):
    """With this function.. Our bot wishes and introduces itself to user 
       It also asks the user name
    """
    greets=[f"My name is {bot_name},Let's have some fun together\nWhat's your name?",f"I am {bot_name},Let's have some good time.....\n Your good name please"]
    random.seed(time())
    return give_starting_wish()+random.choice(greets)

def closing_greets(user_name):
    """
    It wishes the user while leaving the chat.
    """
    greets=[f"Bye! {user_name}, I wish you had a good time\n",f"See you {user_name}, I hope you enjoyed a lot\n"]
    part_of_day,h=give_part_of_day()
    random.seed(time())
    if(part_of_day=="Morning" or part_of_day=="AfterNoon"):
        return random.choice(greets)+"I wish a great day ahead for you :)\n"
    elif(h<19):
        return random.choice(greets)+"I wish you've enjoyed your day....\nI wish a fabulous evening for you :)\n"
    else:
        return random.choice(greets)+"I wish you had a great day...\nGood night sweet dreams yaar :)\n"
