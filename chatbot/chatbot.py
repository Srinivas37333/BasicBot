import os,time
from datetime import datetime
import greetings.greetings as gt
import jokes.jokes as jk
import games.games as gm

class chatbot(object):
    """
    This class is used to integrate all the functionalities
    of chatbot.It implements the chatbot.This bot wishes the user.
    This bot can evaluate expressions,gives time,gives date,plays games 
    based on random numbers.This bot also stores your chat.If you want you 
    can view your entire chat at any point of time.It's name is Laxmi.It 
    always treats it's user name as "Lucky" initially.
    """
    def __init__(self):
        """
        This is the contructor.
        Here we initialize all variables.
        """
        self.name="Laxmi"
        self.user_name="Lucky"
        self.whole_chat=[]
        self.tasks=[ "1.Evaluating Epressions","2.Giving date time","3.Playing games",
        "4.Cracking jokes","5.Giving entire chat","6.Quit"]
        self.cnt=0
    def store(self,bot_msg,user_msg):
        """
        This function is used to store the user msg and bot msg
        """
        self.whole_chat.append((bot_msg,user_msg))
        self.cnt+=1

    def print_tasks(self):
        """
        It prints the tasks
        """
        print("_"*45,"_______Things which I can do______",sep='\n')
        print(*self.tasks,sep='\n')
        print("_"*45)

    def make_choice(self,prompt_msg=""):
        """
        It allows user to give an input number
        If he enters anything other than numbers then 
        it returns None.Otherwise it returns number given by user
        """
        try:
            bot_msg=f"{self.name} : {prompt_msg} Enter the number related to task you want me to perform"
            print(bot_msg)
            user_choice=input(f"{self.user_name} : ")
            user_msg=f"{self.user_name} : {user_choice}"
            self.store(bot_msg,user_msg)
            user_choice=int(user_choice)
        except:
            bot_msg=f"{self.name} : Your choice must be a number"
            print(bot_msg)
            self.store(bot_msg,"")
            return None
        else:
            return user_choice

    def evaluate_expression(self):
        """
        This method asks user to give an expression for evaluation.
        It evaluates the expression if it is correct,Otherwise it
        gies some error message
        """
        bot_msg=f"{self.name} : Enter the expression to be evaluated"
        print(bot_msg)
        exp=input(f"{self.user_name} : ")
        user_msg=f"{self.user_name} : {exp}"
        self.store(bot_msg,user_msg)
        try:
            ans=eval(exp)
        except:
            bot_msg=f"{self.name} : Enter a valid expression"
            print(bot_msg)
            self.store(bot_msg,"")
        else:
            bot_msg=f"{self.name} : {exp} = {ans}"
            print(bot_msg)
            self.store(bot_msg,"")

    def data_time_queries(self):
        """
        This fuction is used to answer some queries related to date and time
        """
        user_choice=self.make_choice("1.Today's date      2.Current time\n")
        date,time=str(datetime.now()).split()
        if(user_choice==None):
            pass
        elif(user_choice==1):
            bot_msg=f"{self.name} : {date}"
            print(bot_msg)
            self.store(bot_msg,"")
        elif(user_choice==2):
            bot_msg=f"{self.name} : {time}"
            print(bot_msg)
            self.store(bot_msg,"")
        else:
            bot_msg=f"{self.name} : Your input should be 1 or 2"
            print(bot_msg)
            self.store(bot_msg,"")

    def play_game(self):
        """
        This function is for playing games
        """
        while(1):
            user_choice=self.make_choice("Enter 1 for Rock Paper Scissor, 2 for Random number Guessing, 3 for quiz ,4 for quitting\n")
            if(user_choice==None):
                continue
            if(user_choice==1):
                bot_msg=f"{self.name} : Your have selected Rock paper Scissor game" 
                print(bot_msg)
                self.store(bot_msg,"You played Rock paper Scissor game")
                gm.rock_paper_scissor(self.name,self.user_name)
            elif(user_choice==2):
                bot_msg=f"{self.name} : Your have selected Random number Guessing game" 
                print(bot_msg)
                self.store(bot_msg,"You played random number guessing game")
                gm.number_guessing(self.name,self.user_name)
            elif(user_choice==3):
                bot_msg=f"{self.name} : Your have selected playing quiz" 
                print(bot_msg)
                self.store(bot_msg,"You played quiz")
                gm.quiz(self.name,self.user_name)
            elif(user_choice==4):
                print("I hope you had a great time playing these games. Come again to have fun :) ")
                break
            else:
                bot_msg=f"{self.name} : Please select a valid number..." 
                print(bot_msg)
                self.store(bot_msg,"")

    def crack_joke(self):
        """
        This function cracks a joke.
        """
        bot_msg=f"{self.name} : {jk.crack_joke()}"
        print(bot_msg)
        self.store(bot_msg,"")

    def give_whole_chat(self):
        """
        This function prints the entire chat upto
        the poin of calling this function
        """
        for i,j in self.whole_chat:
            print(i)
            if(j!=""):
                print(j)
        self.print_tasks()

    def chat(self):
        """
        This is main chat function
        """
        greeting=gt.greet(self.name)
        print(greeting)
        self.user_name=input()
        self.store(greeting,self.user_name)
        self.print_tasks()
        while(1):
            if(self.cnt>15):
                self.print_tasks()
                self.cnt=0
            user_choice=self.make_choice()
            if(user_choice==None):
                continue
            elif(user_choice==1):
                self.evaluate_expression()

            elif(user_choice==2):
                self.data_time_queries()

            elif(user_choice==3):
                self.play_game()

            elif(user_choice==4):
                self.crack_joke()

            elif(user_choice==5):
                self.give_whole_chat()
            
            elif(user_choice==6):
                closing=gt.closing_greets(self.user_name)
                self.store(closing,"") 
                print(closing)
                break

            else:
                bot_msg=f"{self.name} : Please enter a valid number. Input should lies in  [1-{len(self.tasks)}]" 
                print(bot_msg)
                self.store(bot_msg,"")
