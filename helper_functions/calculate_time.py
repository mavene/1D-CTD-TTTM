import random

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
def calc(start_hours, start_minutes, hours, minutes, day = ""):
    error_T = time_error(minutes, hours, start_hours, start_minutes)
    if error_T != None:
        return error_T
    
    error_D = day_error(day)
    if error_D == "Wrong spelling":
        return error_D
    
    minutes, hours, days = time_correction(start_minutes, start_hours, minutes, hours)

    if error_D == "":
        return hours, minutes
    
    current_day = day_correction(error_D, days)
    return hours, minutes, current_day

# TODO Description: Generates random question
# Parameters: progress_tracker (Progression class)
def question(progress_tracker = None):
    current_hrs, interval_hr = random.sample([f"{i:02d}" for i in range(1, 13)], 2)
    current_mns, interval_mn = random.sample([f"{i:02d}" for i in range(0, 60, 5)], 2)
    current_day = random.choice(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", ""])

    # Troubleshooting -> run this to check logic
    # print(current_hrs, current_mns, current_day)
    # print(interval_hr, interval_mn)

    question = f"""
    The time and date now is {current_hrs}:{current_mns}, {current_day}. 
    What will be the time (and day if applicable) in {interval_hr} hours and {interval_mn} minutes?
    Enter your answer in 24 hour format (example: 13:30 Tuesday): """

    correct_hr, correct_mn, *_ = calc(current_hrs, current_mns, interval_hr, interval_mn, current_day)
    correct_day = "".join(_)

    # Troubleshooting -> run this to check logic
    # print(correct_hr, correct_mn, correct_day)

    user_input = input(question)
    while user_input == "":
        user_input = input(question)
    
    given_time, *_ = user_input.split()
    given_day = "".join(_)
    given_hr, given_mn = given_time.split(":")

    # Troubleshooting -> run this to check logic
    # print(given_hr, given_mn, given_day)

    if given_hr != correct_hr or given_mn != correct_mn or given_day != correct_day:
        print("\nIncorrect answer")
    else:
        print("\nCorrect!")
        if progress_tracker:
            progress_tracker.add_pt(1)

# Troubleshooting -> run this to check logic
#question()