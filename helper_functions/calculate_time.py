import random

# TODO Description: Corrects time?
# Parameters: start_minutes (str)
def analyze_time_input(u_input = ""):
    if u_input == None:
        return ""
    u_input = u_input.strip().split(":")
    for index_i, i in enumerate(u_input):
            if u_input[index_i] == "":
                u_input[index_i] == "0"
            try:
                type(int(u_input[index_i])) != int
            except:
                u_input = ""
                break
    return u_input

# TODO Description: Corrects time?
# Parameters: start_minutes (str), start_hours (str), minutes (str), hours (str)
def time_correction(start_minutes, start_hours, minutes, hours):
    mins = int(minutes) + int(start_minutes)
    hrs = int(hours) + int(start_hours)
    days = 0
    while mins >= 60:
        hrs += 1
        mins -= 60
    while hrs >= 24:
        hrs -= 24
        days += 1
    if len(str(mins)) == 1:
        mins = "0" + str(mins)
    if len(str(hrs)) == 1:
        hrs = "0" + str(hrs)
    return str(mins), str(hrs), str(days)

# TODO Description: Checks time error?
# Parameters: minutes (str), hours (str), start_hour (str), start_minutes (str)
def time_error(minutes, hours, start_hour, start_minutes):
    if minutes == "":
        minutes += "0"
    if hours == "":
        hours += "0"

    try:
        type(int(minutes)) == int and type(int(hours)) == int
    except:
        return "incorrect duration value(s)"
    
    try:
        type(int(start_hour)) == int and type(int(start_minutes)) == int
    except:
        return "Incorrect starting value(s)"
    
    return None

# TODO Description: Checks day error?
# Parameters: day (str)
def day_error(day):
    if day == "":
        return day
    dict_day = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday":7}
    if day.lower() not in dict_day:
        return "Wrong spelling"
    return day.lower()
    
# TODO Description: Corrects day
# Parameters: day (str), days (str)
def day_correction(day, days):
    dict_day = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday":7}
    counter = dict_day[day] + int(days)
    while counter > 7:
        counter -= 7
    for i in dict_day.keys():
        if dict_day[i] == counter:
            return i[0].upper() + i[1:]

# TODO Description: Calculates correct answer?
# Parameters: start_hours (str), start_minutes (str), hours (str), minutes (str), day (str)
def calc(start_hours, start_minutes, hours, minutes, day = "", end_hours = "", end_minutes = ""):
    if end_minutes != "" and end_hours != "":
        hours_d = int(end_hours) - int(start_hours)
        minutes_d = 0
        while hours_d > 0:
            minutes_d += 60
            hours_d -= 1
        minutes_d = minutes_d - int(start_minutes)
        while minutes_d >= 60:
            hours_d += 1
            minutes_d -= 60
        return hours_d, minutes_d
    
    error_T = time_error(minutes, hours, start_hours, start_minutes)
    if error_T != None:
        return error_T
    
    error_D = day_error(day)
    if error_D == "Wrong spelling":
        return error_D
    
    minutes, hours, days = time_correction(start_minutes, start_hours, minutes, hours)

    if error_D == "":
        return int(hours), int(minutes)
    
    current_day = day_correction(error_D, days)
    return int(hours), int(minutes), current_day

# TODO Description: Generates random question
# Parameters: progress_tracker (Progression class)
def randomise(progress_tracker = None):
    current_hrs, interval_hr = random.sample([f"{i:02d}" for i in range(1, 13)], 2)
    current_mns, interval_mn = random.sample([f"{i:02d}" for i in range(0, 60, 5)], 2)
    current_day = random.choice(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])

    question = f"""
    The time and date now is {current_hrs}:{current_mns}, {current_day}. 
    What will be the time (and day if applicable) in {interval_hr} hours and {interval_mn} minutes?
    Enter your answer in 24 hour format (example: 13:30 Tuesday): """

    correct_hr, correct_mn, *_ = calc(current_hrs, current_mns, interval_hr, interval_mn, current_day)
    correct_day = "".join(_)

    user_input = input(question)
    while user_input == "":
        user_input = input(question)
    
    try:
        given_time, *_ = user_input.split()
        given_day = "".join(_)
        given_hr, given_mn = given_time.split(":")

        if int(given_hr) != correct_hr or int(given_mn) != correct_mn or given_day != correct_day:
            print("\nIncorrect answer")
        else:
            print("\nCorrect!")
            if progress_tracker:
                progress_tracker.add_pt(1)
    except:
        print("\nIncorrect format")

# TODO Description: Generates random question
# Parameters: progress_tracker (Progression class)
def qn_generator(progress_tracker = None, story_mode = False, qn = None, clock = ''):
    
    if story_mode == True:
        start_hours = clock.split(":")[0]
        start_minutes = clock.split(":")[1]

        half_hour = random.randrange(30,61,5)
        talk_time = random.randrange(5, 15, 5)
        qn_dict = {2: f"You have {half_hour} minutes to get ready before your school bus arrives. What time will your bus reach? (24-hour format e.g 14:04) ", 
                   5: f"The time now is {clock}. Lunch is at 12pm. How long more do you need to wait? (In hours:minutes) ", 
                   7: f"Well done! Now that you are done with the test, you must wait for the school bus. It’s {clock}. You have {talk_time} minutes to talk to your friend. What time does the bus come? (24-hour format e.g 14:04) "}
        user_input = input(qn_dict[qn])
        u_input = analyze_time_input(user_input)
        if qn == 2:
            try:
                calculated_time = calc(start_hours, start_minutes, minutes = half_hour, hours=0)
            except:
                print("\nIncorrect format")
            else:
                if calculated_time == ((int(u_input[0]), int(u_input[1]))):
                    print("\nGood job! That is the correct time.")
                    if progress_tracker:
                        progress_tracker.add_pt(1)
                else:
                    print("\nWrong answer")
                
        if qn == 5:
            try:
                duration = calc(start_hours, start_minutes, hours = 0, minutes = 0, day = "", end_hours = "12", end_minutes = "0")
            except:
                print("\nIncorrect format")
            else:
                if duration == ((int(u_input[0]), int(u_input[1]))):
                    print("\nGood job!")
                    if progress_tracker:
                        progress_tracker.add_pt(1)
                else:
                    print("\nWrong answer")

        if qn == 7:
            try:
                calculated_time = calc(start_hours, start_minutes, minutes = talk_time, hours=0)
            except:
                print("\nIncorrect format")
            else:
                if calculated_time == ((int(u_input[0]), int(u_input[1]))):
                    print("\nGood job! That is the correct time.")
                    if progress_tracker:
                        progress_tracker.add_pt(1)
                else:
                    print("\nWrong answer")
    
    else:
        randomise(progress_tracker)

# Unit Testing
# -------------------------------------------
# randomise()
# qn_generator(story_mode = True, qn = 5, clock = "11:40")