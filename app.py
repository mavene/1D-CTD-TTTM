from helper_functions import read_clock, calculate_time, convert_time, story, progression
import sys

def progressive():

    read_prog = progression.Progress("Reading the Clock", 4, 6)
    convert_prog = progression.Progress("Converting Time", 6, 10)
    calc_prog = progression.Progress("Calculating Time", 6, 10)

    while not read_prog.check_proficiency():
        # Mode 1 : insert Aravind's part here
        read_clock.question(read_prog)

    while not convert_prog.check_proficiency():
        # Mode 2 : insert Vanessa's part here
        convert_time.question(convert_prog)

    while not calc_prog.check_proficiency():
        # Mode 3 : insert YongQing's part here
        calculate_time.question(calc_prog)    

    if read_prog.check_proficiency() and convert_prog.check_proficiency() and calc_prog.check_proficiency():
        print("\nYou have unlocked Story Mode!")
        story.start()

def practice():
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
            read_clock.read_the_time()
    elif level_choice in ["2", "Convert Time"]:
        for i in range(0, 10):
            pass
    elif level_choice in ["3", "Calculate Time"]:
        for i in range(0, 10):
            calculate_time.calculate_interval()

def quit():
    print("Goodbye!")
    sys.exit()

def welcome_screen():
    valid_modes = ["Progressive", "1", "Main", "Practice", "2", "Quit", "3"]

    # Welcome Screen    
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

    while mode_choice not in valid_modes:
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
        quit()

def main_app():
    welcome_screen()
    # progression.check_progress()
    
if __name__ == "__main__":
    main_app()