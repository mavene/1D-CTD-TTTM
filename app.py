from os import read
from helper_functions import read_time, convert_time, calculate_time, progression, story
import sys

# Description: Main Game -> Progressive Mode
# Parameters: N/A
def progressive():
    # Setting up progress trackers
    read_prog = progression.Progress("Reading the Clock", 1, 1) #4, 6
    convert_prog = progression.Progress("Converting Time", 1, 1) #6, 10
    calc_prog = progression.Progress("Calculating Time", 1, 1) #6,10

    for i in range(read_prog.get_total_qns()):
        # Mode 1 : insert Aravind's part here
        read_time.question(read_prog)
    
    print(read_prog.progress_report())

    for i in range(convert_prog.get_total_qns()):
        # Mode 2 : insert Vanessa's part here
        convert_time.question(convert_prog)

    print(convert_prog.progress_report())

    for i in range(calc_prog.get_total_qns()):
        # Mode 3 : insert YongQing's part here
        calculate_time.question(calc_prog)   
    
    print(calc_prog.progress_report())

    # Troubleshooting -> run this to check output
    # print(read_prog.check_proficiency())
    # print(convert_prog.check_proficiency())
    # print(calc_prog.check_proficiency()) 

    if read_prog.check_proficiency() and calc_prog.check_proficiency() and convert_prog.check_proficiency():
        print("\nYou have unlocked Story Mode!")
        welcome_screen(True)
    else:
        welcome_screen()

# Description: Practice Mode
# Parameters: N/A
def practice():
    # Setting up progress trackers
    read_prog = progression.Progress("Reading the Clock", 1, 1) #4, 6
    convert_prog = progression.Progress("Converting Time", 1, 1) #6, 10
    calc_prog = progression.Progress("Calculating Time", 1, 1) #6,10

    level_choice = input ("""
    Choose a Level to Practise:
    -------------------------

    1 ) Read Time
    2 ) Convert Time
    3 ) Calculate Time

    \n""")

    while level_choice not in ["1", "Read Time", "2", "Convert Time", "3", "Calculate Time"]:
        level_choice = input ("""
    Choose Level to Practise:
    ------------------------

    1 ) Read Time
    2 ) Convert Time
    3 ) Calculate Time

    \n""")

    if level_choice in ["1", "Read Time"]:
        for i in range(0, 10):
            read_time.question()
        print(read_prog.progress_report())
    elif level_choice in ["2", "Convert Time"]:
        for i in range(0, 10):
            convert_time.question()
        print(convert_prog.progress_report())
    elif level_choice in ["3", "Calculate Time"]:
        for i in range(0, 10):
            calculate_time.question()
        print(calc_prog.progress_report())
        
    # Return to main menu
    welcome_screen()

# Description: Main Menu
# Parameters: unlock_story (bool)
def welcome_screen(unlock_story = False):
    valid_modes_nostory = ["Start Game", "1", "Main", "Practice", "2", "Quit", "3"]

    valid_modes_story = ["Start Game", "1", "Main", "Practice", "2", "Story", "3", "Quit", "4"]
    
    # Welcome Screen    
    if unlock_story:
        print("""

    ______  ______   __       __           ______  __   __    __   ______        ______  ______       __    __   ______    
   /\__  _\/\  ___\ /\ \     /\ \         /\__  _\/\ \ /\ "-./  \ /\  ___\      /\__  _\/\  __ \     /\ "-./  \ /\  ___\   
    \/_/\ \/\ \  __\ \ \ \____\ \ \____    \/_/\ \/\ \ \\ \ \-./\ \\ \  __\     \/_/\ \/\ \ \/\ \    \ \ \-./\ \\ \  __\   
       \ \_\ \ \_____\\ \_____\\ \_____\      \ \_\ \ \_\\ \_\ \ \_\\ \_____\      \ \_\ \ \_____\    \ \_\ \ \_\\ \_____\ 
        \/_/  \/_____/ \/_____/ \/_____/       \/_/  \/_/ \/_/  \/_/ \/_____/       \/_/  \/_____/     \/_/  \/_/ \/_____/ 
                                                                                                                       
    ------------------------------------------------------------------------------------------------------------------------

    1 ) Start Game
    2 ) Practice
    3 ) Story Mode
    4 ) Quit 

    \n""")

    else:
        print("""

    ______  ______   __       __           ______  __   __    __   ______        ______  ______       __    __   ______    
   /\__  _\/\  ___\ /\ \     /\ \         /\__  _\/\ \ /\ "-./  \ /\  ___\      /\__  _\/\  __ \     /\ "-./  \ /\  ___\   
    \/_/\ \/\ \  __\ \ \ \____\ \ \____    \/_/\ \/\ \ \\ \ \-./\ \\ \  __\     \/_/\ \/\ \ \/\ \    \ \ \-./\ \\ \  __\   
       \ \_\ \ \_____\\ \_____\\ \_____\      \ \_\ \ \_\\ \_\ \ \_\\ \_____\      \ \_\ \ \_____\    \ \_\ \ \_\\ \_____\ 
        \/_/  \/_____/ \/_____/ \/_____/       \/_/  \/_/ \/_/  \/_/ \/_____/       \/_/  \/_____/     \/_/  \/_/ \/_____/ 
                                                                                                                       
    ------------------------------------------------------------------------------------------------------------------------

    1 ) Start Game
    2 ) Practice
    3 ) Quit 

    \n""")

    mode_choice = input()
    
    if unlock_story:
        while mode_choice not in valid_modes_story:
            mode_choice = input ("""

            Choose a Mode:
            --------------

            1 ) Start Game
            2 ) Practice
            3 ) Story Mode
            4 ) Quit 

            \n""")

        if mode_choice == "1" or mode_choice == "Progressive" or mode_choice == "Main":
            progressive()
        elif mode_choice == "2" or mode_choice == "Practice":
            practice()
        elif mode_choice == "3" or mode_choice == "Story Mode":
            story.start()
        elif mode_choice == "4" or mode_choice == "Quit":
            print("Goodbye!")
            quit()

    else:
        while mode_choice not in valid_modes_nostory:
            mode_choice = input ("""

            Choose a Mode:
            --------------

            1 ) Start Game
            2 ) Practice
            3 ) Quit 

            \n""")

        if mode_choice == "1" or mode_choice == "Progressive" or mode_choice == "Main":
            progressive()
        elif mode_choice == "2" or mode_choice == "Practice":
            practice()
        elif mode_choice == "3" or mode_choice == "Quit":
            print("Goodbye!")
            quit()

if __name__ == "__main__":
    welcome_screen()