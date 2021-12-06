from os import _exit
from time import sleep
from helper_functions import read_time, convert_time, calculate_time, story, progression

# Description: Main Game -> Progressive Mode
# Parameters: N/A
def progressive():
    # Setting up progress trackers
    level1_title = "Reading the Clock"
    level2_title = "Converting Time"
    level3_title = "Calculating Time"
    read_prog = progression.Progress(level1_title, 3, 5) #4, 6
    convert_prog = progression.Progress(level2_title, 3, 5) #6, 10
    calc_prog = progression.Progress(level3_title, 3, 5) #6,10

    print(f"""
#####################################
Starting Level 1: 
{level1_title}
#####################################
    """)

    for i in range(read_prog.get_total_qns()):
        # Mode 1 : insert Aravind's part here
        read_time.question(read_prog)
        sleep(0.5)
    print(read_prog.progress_report())
    sleep(0.5)

    print(f"""
#####################################
Starting Level 2: 
{level2_title}
#####################################
    """)

    for i in range(convert_prog.get_total_qns()):
        # Mode 2 : insert Vanessa's part here
        convert_time.question(convert_prog)
        sleep(0.5)
    print(convert_prog.progress_report())
    sleep(0.5)

    print(f"""
#####################################
Starting Level 3: 
{level3_title}
#####################################
    """)

    for i in range(calc_prog.get_total_qns()):
        # Mode 3 : insert YongQing's part here
        calculate_time.qn_generator(calc_prog)   
        sleep(0.5)
    print(calc_prog.progress_report())
    sleep(0.5)

    if read_prog.check_proficiency() and calc_prog.check_proficiency() and convert_prog.check_proficiency():
        print("\nYou have unlocked Story Mode!")
        welcome_screen(True)
    else:
        welcome_screen()

# Description: Practice Mode
# Parameters: N/A
def practice():
    # Setting up progress trackers
    level1_title = "Reading Time"
    level2_title = "Converting Time"
    level3_title = "Calculating Time"
    read_prog = progression.Progress(level1_title, 3, 6) #3, 5
    convert_prog = progression.Progress(level2_title, 3, 5) #3, 5
    calc_prog = progression.Progress(level3_title, 3, 5) #3, 5

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
        print(f"""
-------------------------------------
Practicing Level 1 : {level1_title}
-------------------------------------
        """)
        for i in range(0, read_prog.get_total_qns()):
            read_time.question(read_prog)
            sleep(0.5)
        print(read_prog.progress_report())
    elif level_choice in ["2", "Convert Time"]:
        print(f"""
-------------------------------------
Practicing Level 2: {level2_title}
-------------------------------------
        """)
        for i in range(0, convert_prog.get_total_qns()):
            convert_time.question(convert_prog)
            sleep(0.5)
        print(convert_prog.progress_report(convert_prog))
    elif level_choice in ["3", "Calculate Time"]:
        print(f"""
-------------------------------------
Practicing Level 3: {level3_title}
-------------------------------------
        """)
        for i in range(0, convert_prog.get_total_qns()):
            calculate_time.qn_generator(calc_prog)
            sleep(0.5)
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
        print("""\n

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
        print("""\n

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