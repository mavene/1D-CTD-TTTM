def seconds_to_minutes(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    print("""60 seconds is equal to 1 minute. Divide the number of seconds by 60 to get the number of minutes. 
             Any remainder value is the remaining seconds.""")
    return ("{} seconds is {} minutes and {} seconds.".format(seconds, minutes, remaining_seconds))

def minutes_to_seconds(minutes):
    seconds = int(minutes*60)
    print("1 minute is equal to  60 seconds. Multiply the number of minutes by 60 to get the number of seconds.")
    return ("{} minutes is {} seconds.".format(minutes,seconds))

def minutes_to_hours(minutes):
    hours = minutes / 60
    print("""60 minutes is equal to 1 hour. Divide the number of minutes by 60 to get the number of hours.""")
    return ("{} minutes is {} hours.".format(minutes,hours))

def hours_to_minutes(hours):
    minutes = int(hours*60)
    print("1 hour is equal to  60 minutess. Multiply the number of hours by 60 to get the number of minutes.")
    return ("{} hours is {} minites.".format(hours,minutes))

def hours_to_days(hours):
    days = hours / 24
    print("""24 hours is equal to 1 day. Divide the number of hours by 24 to get the number of days.""")
    return ("{} hours is {} days.".format(hours,days))

def months_to_years(months):
    years = months / 12
    print("""There are 12 months in 1 year. Divide the number of months by 12 to get the number of years.""")
    return ("{} months is {} years.".format(months,years))

def question(progress_tracker):
    questions = []

    question = 