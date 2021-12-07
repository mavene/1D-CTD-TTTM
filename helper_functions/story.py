import os
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from app import welcome_screen
from helper_functions import read_time, convert_time, calculate_time, progression

dirname = os.path.dirname(__file__)
path = rf'{dirname}\\..\resources\storymode'

def display_graphic(qn):
    img = mpimg.imread(path+"\\"+qn+".png")
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def start(progress_tracker = None):
    story_prog = progression.Progress("Story Time", 5, 9)
    name = input("Hello there, we are here to teach time. What is your name? ")
    
    # Q1
    # Display image for Q1
    display_graphic("1")
    sleep(0.3)
    storygen_time1 = read_time.story_question("Morning", "24 hour", story_prog, 0, name)
    sleep(0.3)
    
    # Q2
    display_graphic("2")
    sleep(0.3)
    calculate_time.qn_generator(story_prog, True, 2, storygen_time1)
    sleep(0.3)

    # Q3
    display_graphic("3")
    sleep(0.3)
    convert_time.question(story_prog, True, 3)
    sleep(0.3)
    
    # Q4
    display_graphic("4")
    sleep(0.3)
    storygen_time2 = read_time.story_question("Noon", "24 hour", story_prog, 1)
    sleep(0.3)

    # Q5
    display_graphic("5")
    sleep(0.3)
    calculate_time.qn_generator(story_prog, True, 5, storygen_time2)
    sleep(0.3)

    # Q6
    display_graphic("6")
    sleep(0.3)
    storygen_time3 = read_time.story_question("Afternoon", "24 hour", story_prog, 2)
    sleep(0.3)

    # Q7
    display_graphic("7")
    sleep(0.3)
    calculate_time.qn_generator(story_prog, True, 7, storygen_time3)
    sleep(0.3)

    # Q8
    display_graphic("8")
    sleep(0.3)
    convert_time.question(story_prog, True, 5)
    sleep(0.3)
    
    # Q9
    display_graphic("9")
    sleep(0.3)
    convert_time.question(story_prog, True, 1)
    sleep(0.3)

    print(story_prog.progress_report())
    sleep(0.3)

    welcome_screen(True)