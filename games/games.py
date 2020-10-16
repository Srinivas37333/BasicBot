import random,time
import os
random.seed(time.time())
def rock_paper_scissor(bot_name,user_name):
    """
    This function implemented rock paper scissor game
    """
    options={1:"Rock",2:"Paper",3:"Scissor"}
    winning_moves=[(1,3),(2,1),(3,2)]
    print(f"{bot_name} : Enter 1 for Rock, 2 for Paper, 3 for Scissor  Enter Your choice")
    try:
        user_choice=int(input(f"{user_name} : "))
        bot_choice=random.choice([1,2,3])
    except:
        print(f"{bot_name} : Please enter a number")
    else:
        if(user_choice not in options.keys()):
            print(f"{bot_name} : Please select a number from 1,2,3")
        elif(user_choice==bot_choice):
            print(f"{bot_name} : Ah it's a Draw!!")
        elif((user_choice,bot_choice) in winning_moves):
            print(f"{bot_name} : Hurray!! You won the match...")
        else:
            print(f"{bot_name} : Yahoo!! I won the match")

def number_guessing(bot_name,user_name):
    """
    This function implements number guessing game.

    """
    print(f"{bot_name} : Guess a number from 1 - 100")
    try:
        user_guess=int(input(f"{user_name} : "))
    except:
        print(f"{bot_name} : Please enter a number")
    else:
        bot_guess=int(random.random()*100+1)
        if(user_guess==bot_guess):
            print(f"{bot_name} : Hurrah!!! You guessed it correctly... OMG")
        else:
            print(f"{bot_name} : oh :( I've selected {bot_guess} Better luck next time")

def quiz(bot_name,user_name):
    """
    This method is used to implement a quiz
    """
    print(f"{bot_name} : In this game I will ask you 3 questions Based on your answers I will give your score")
    q_n_a_file=open(os.getcwd()+"\\text_files\\questions_answers.txt",'r')
    q_n_a=q_n_a_file.readlines()
    q_n_a_file.close()
    quiz_qa=random.sample(q_n_a,3)
    score=0
    correct_answers=[]
    for i in range(3):
        q,a=quiz_qa[i].split("--")
        a=a.strip()
        print(f"{bot_name} : {q}")
        user_ans=input(f"{user_name} : ").strip()
        if(user_ans==a):
            score+=1
        correct_answers.append(a)
    print(f"{bot_name} : Your score is {score} Correct answers are : {correct_answers}")