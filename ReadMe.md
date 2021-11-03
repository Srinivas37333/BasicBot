# BasicBot

Team Members: 18pa1a0511  18pa1a0547

## Goal
The main goal is to build a console based chatbot.This can perform certain number of tasks. This takes a number related to the task that user wants this bot to perform,this performs the task related to that particular number.The main intension of doing this  bot is to learn how to structure different files while building a chatbot and to gain some intution in making more useful chatbots. Although this chatbot is not robust it can make some conversations happen.

## What this chatbot can do?
* It greets the user.
* It can evaluate the expressions entered by the user.
* It can give the date and time to the user at any point of chatting.
* It can also play some games with user.The games which it can play with the user are:
  1. Rock Paper Scissor
  2. Random number guessing
  3. Quiz
* It stores the entire conversation happened between it and user. It can give the entire chat at any point of time.

## Block diagram of chatbot
![Block Diagram](https://github.com/Lakshman511/BasicBot/blob/master/blockDiagram.jpg)

## Coding
After completing the designing of chatbot.
* I've wrote code to 3 modules.Then integrated them in single class called chatbot.Finally main.py file calls chat() of chatbot object.By running this main.py file our chatbot will start chatting with us.
* [This](https://github.com/Lakshman511/BasicBot/blob/master/greetings/greetings.py) is the python file where I've implemented greetings functionality of my bot.
* [This](https://github.com/Lakshman511/BasicBot/blob/master/games/games.py) is the file where I've implemented the gaming functionality of my bot. This file contains code to the games which this bot can play.
* [This](https://github.com/Lakshman511/BasicBot/blob/master/jokes/jokes.py) is the file where I've wrote code for getting a joke from jokes file which is located [here](https://github.com/Lakshman511/BasicBot/blob/master/text_files/jokes.txt).
* [Chatbot](https://github.com/Lakshman511/BasicBot/blob/master/chatbot/chatbot.py) file contains a class called chatbot which integrated all the functionalities of chatbot.This class contains a function called chat on calling this function we can chat with it. Here I've imported all three modules and used all necessary functions in chatbot class.
* [This](https://github.com/Lakshman511/BasicBot/blob/master/main.py) is the link to my main.py file.In this file I've just created an object to chatbot class and called chat function of this chatbot.

## Some additional points
* I've named my chatbot as Laxmi.
* In this small project I've used very few python libraries.They are randomtime,datetime,os.
* You can understand whole code very easily.

## This is the chat of Our bot
![](https://github.com/Lakshman511/BasicBot/blob/master/chat_img.jpg)


* [This is the youtube video](https://youtu.be/PELp-rFbdwQ) Where you can see my interaction with this chatbot.

## References and tools
* Since it is basic version I haven't refered any where for coding.But idea of this bot is taken from one of the lectures of our professor.
* Coming to the tools I've used for making this repository...
* First of all I would like to thank the git.Previously I used to upload all the files of any project manually.But this time I've used git to do that.One of the advantages of git I've found is it uploaded my project in the same structure as it is in my system.Earlier I used to struggle a lot to create different folders and to upload files in it.
* Thanks to the guy in [this](https://youtu.be/xwlQimbwJJE) video for explaining git in very simple and clean way.
* I've used [this](https://creately.com) tool to draw the above block diagram.

## Conclusion
With the experience that I've gained by doing this project I would like to make a chatbot which helps a student for his academic development with the help of my team mates. The functionalities of chatbot that we've planned so far are:
1. It should suggest best textbooks for students.
2. It should suggest best courses on different platforms like udemy,coursera,edx etc.,
3. It should conduct quizzes to the student.
#### Thank You
