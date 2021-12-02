import random

# Description: Convert seconds to minutes
# Parameters: seconds (str)
def seconds_to_minutes(seconds):
    minutes = int(seconds) // 60
    remaining_seconds = seconds % 60
    print("""60 seconds is equal to 1 minute. Divide the number of seconds by 60 to get the number of minutes. 
             Any remainder value is the remaining seconds.""")
    return ("{} seconds is {} minutes and {} seconds.".format(seconds, minutes, remaining_seconds))

# Description: Convert minutes to seconds
# Parameters: minutes (str)
def minutes_to_seconds(minutes):
    seconds = int(minutes*60)
    print("1 minute is equal to  60 seconds. Multiply the number of minutes by 60 to get the number of seconds.")
    return ("{} minutes is {} seconds.".format(minutes,seconds))

# Description: Convert minutes to hours
# Parameters: minutes (str)
def minutes_to_hours(minutes):
    hours = int(minutes) // 60
    print("""60 minutes is equal to 1 hour. Divide the number of minutes by 60 to get the number of hours.""")
    return ("{} minutes is {} hours.".format(minutes,hours))

# Description: Convert hours to minutes
# Parameters: hours (str)
def hours_to_minutes(hours):
    minutes = int(hours*60)
    print("1 hour is equal to  60 minutess. Multiply the number of hours by 60 to get the number of minutes.")
    return ("{} hours is {} minutes.".format(hours,minutes))

# Description: Convert hours to days
# Parameters: hours (str)
def hours_to_days(hours):
    days = int(hours) // 24
    print("""24 hours is equal to 1 day. Divide the number of hours by 24 to get the number of days.""")
    return ("{} hours is {} days.".format(hours,days))

# Description: Convert months to years
# Parameters: months (str)
def months_to_years(months):
    years = int(months) // 12
    print("""There are 12 months in 1 year. Divide the number of months by 12 to get the number of years.""")
    return ("{} months is {} years.".format(months,years))

# TODO: Complete and integrate into main app with progress tracker
# Description: Generates random question
#  TODO Parameters: progress_tracker (Progression class)
def question(): #progress_tracker wll be added after unit testing
    conversions = {"seconds": "minutes", "minutes": ["seconds", "hours"], 
                 "hours": ["minutes", "days"], "months": "years"}
    
    start, end = random.choice(list(conversions.items()))
    if type(end) == list:
        end = random.choice(end)
    
    # Troubleshooting -> run this to check logic
    print(start, end)

    value = random.randint(1, 60)

    if start == "seconds":
        if end == "minutes":
            seconds_to_minutes(value)

    elif start == "minutes":
        if end == "seconds":
            minutes_to_seconds(value)
        elif end == "hours":
            minutes_to_hours(value)

    elif start == "hours":
        if end == "minutes":
            hours_to_minutes(value)
        elif end == "days":
            hours_to_days(value)

    elif start == "months":
        months_to_years(value)

# Troubleshooting -> run this to check logic
# question()