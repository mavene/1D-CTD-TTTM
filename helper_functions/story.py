#TODO:

# Modularise their code and only retrieve the correct question to suit the story
# read_clock()

# Score system -> just tell correct answer and keep track of areas they can improve on and activate practice mode

#--------------------------------------------------------------------------
#Story mode
#add some score system if score < 5, retry mini games?
from time import sleep
import calculate_time, convert_time, read_clock, progression

def start():
    story_prog = progression.Progress("story")

    name = input("Hello there, we are here to teach time. What is your name? ")

    sleep(1)

    print("Using what you have learnt in the previous mini-games, we will now go through a day in your life!")

    sleep(1)

    print("""Good morning {}! You just woke up and looked at the clock. 
            What time is it now?""".format(name))

    #Aravind's function

    print("""You have 40 minutes to get ready before your school bus arrives
             What time will your bus reach?""")
    #YQ's function

    print("""Your first class today is science! Your teacher lets you
             watch a 100 minutes movie about plants. How many hours and minutes is that?""")
    #Vanessa's function

    print("""The movie starts to get boring and you are hungry. What time is it now?""")
    #Aravind's function

    print("""Lunch is at 12pm. How long more do you need to wait?""")
    #YQ's function