import random
import time
import os
def crack_joke():
    """
    This function is used to crack  joke.
    """
    jokes_file=open(os.getcwd()+"\\text_files\\jokes.txt",'r')
    jokes=jokes_file.readlines()
    jokes_file.close()
    random.seed(time.time())
    return random.choice(jokes)