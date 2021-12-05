# TODO: Score system using Progression class -> just tell correct answer and keep track of areas they can improve on and activate practice mode
# if score < 5, retry mini games?

from time import sleep
from helper_functions import progression

# TODO Complete and integrate into main app
# TODO Description
# Parameters: progress_tracker
def start(progress_tracker = None):
    story_prog = progression.Progress("Reading the Clock", 5, 9) #TODO: Proficiency by each level?

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