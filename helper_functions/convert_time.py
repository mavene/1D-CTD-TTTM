# TODO: Add in more input validation

# Description: Convert seconds to minutes
# Parameters: minutes (int)
def seconds_to_minutes(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return minutes, remaining_seconds

# Description: Convert minutes to seconds
# Parameters: minutes (int)
def minutes_to_seconds(minutes):
    seconds = minutes * 60
    return seconds

# Description: Convert minutes to hours
# Parameters: minutes (int)
def minutes_to_hours(minutes):
    hours = minutes // 60
    return hours

# Description: Convert hours to minutes
# Parameters: hours (int)
def hours_to_minutes(hours):
    minutes = hours * 60
    return minutes

# Description: Convert hours to days
# Parameters: hours (int)
def hours_to_days(hours):
    days = hours // 24
    return days

# Description: Convert months to years
# Parameters: months (str)
def months_to_years(months):
    years = str(int(months) // 12)
    return years

# Description: Convert months to years
# Parameters: months (str)
def check_input(user_input):
    while True:
        try:
            return int(user_input)
        except TypeError and ValueError:
            print("Please only enter numbers!")
            user_input = input()

import random
# Description: Convert months to years
# Parameters: months (str)
def question(progress_tracker = None, story_mode = False, qn = None):
    if not qn:
        qn_no = random.randint(0, 6)
    else:
        qn_no = qn

    msg = ''
    
    if qn_no == 0:
        if story_mode:
            random_seconds = (random.randint(100, 200)//5) * 5  #multiples of 5 only (to be approachable to children)
            msg = f'You play hide and seek with your friend. They start counting from {random_seconds}. How many minutes and seconds do you have?'
        else:
            random_seconds = (random.randint(0, 600)//5) * 5  #multiples of 5 only (to be approachable to children)
            msg = f'Convert {random_seconds} seconds to minutes and seconds.\nHint: 1 minute = 60 seconds.\nDivide the number of seconds by 60 to get the number of minutes.\nAny remainder value is the remaining seconds.'
        ans = input(msg)
        minutes, seconds = seconds_to_minutes(random_seconds)
        ans_min, ans_sec = ans.split()
        given_minutes = check_input(ans_min)
        given_seconds = check_input(ans_sec)

        if given_minutes == minutes and given_seconds == seconds:
            print("Correct!")
            if progress_tracker:
                progress_tracker.add_pt(1)
        else:
            print("Oops, not quite right.")

    elif qn_no == 1:
        random_minutes = random.randint(0, 61)
        ans = input(f'Convert {random_minutes} minutes to seconds.\nHint: 1 minute = 60 seconds.\nMultiply the number of minutes by 60 to get the number of seconds.')
        seconds = minutes_to_seconds(random_minutes)
        given_seconds = check_input(ans)

        if given_seconds == seconds:
            print("Correct!")
            if progress_tracker:
                progress_tracker.add_pt(1)
        else:
            print("Oops, not quite right.")
        
    elif qn_no == 2:
        random_minutes = (random.randint(45, 121)//5) * 5   #multiples of 5 only (to be approachable to children)
        if story_mode: 
            msg = f'Your first class today is science! Your teacher lets you watch a {random_minutes} minutes movie about plants. How many hours and minutes is that?'
        else:
            msg = f'Convert {random_minutes} minutes to hours.\n1 hour = 60 minutes.\nDivide the number of minutes by 60 to get the number of hours.'
        ans = input(msg)
        hours = minutes_to_hours(random_minutes)
        given_hours = check_input(ans)

        if given_hours == hours:
            print("Correct!")
            if progress_tracker:
                progress_tracker.add_pt(1)
        else:
            print("Oops, not quite right.")
        
    elif qn_no == 3:
        random_hours = random.randint(1, 13)
        ans = input(f'Convert {random_hours} hours to minutes.\n1 hour = 60 minutes.\nMultiply the number of hours by 60 to get the number of minutes.')
        minutes = hours_to_minutes(random_hours)
        given_minutes = check_input(ans)

        if given_minutes == minutes:
            print("Correct!")
            if progress_tracker:
                progress_tracker.add_pt(1)
        else:
            print("Oops, not quite right.")
        
    elif qn_no == 4:
        if story_mode:
            random_hours = 72
            msg = 'Your friend says you can survive without food for 72 hours. How many days is that?'
        else:
            random_hours = (random.randint(24, 481)// 24) * 24  
            msg = f'Convert {random_hours} hours to days.\n1 day = 24 hours.\nDivide the number of hours by 24 to get the number of days.'
        
        ans = input(msg)
        days = hours_to_days(random_hours)
        given_days = check_input(ans)

        if given_days == days:
            print("Correct!")
            if progress_tracker:
                progress_tracker.add_pt(1)
        else:
            print("Oops, not quite right.")
        
    else:
        random_months = (random.randint(12, 120)//12) * 12
        ans = input(f'Convert {random_months} months to years.\n1 year = 12 months.\nDivide the number of months by 12 to get the number of years.')
        years = months_to_years(random_months)
        given_years = check_input(ans)

        if given_years == years:
            print("Correct!")
            if progress_tracker:
                progress_tracker.add_pt(1)
        else:
            print("Oops, not quite right.")

# Unit Testing
# -------------------------------------------
# question()
# question(None, True, 0)