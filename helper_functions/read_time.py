import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

# Read clock faces for progressive
dirname = os.path.dirname(__file__)
path = rf'{dirname}\\..\resources'

times = []
faces = []
for filename in os.listdir(path): # iterate over files in path folder
    
    if filename.endswith(".png"): # selecting only png image files (clock faces)
        a, b, _ = filename.split(".") 
        times.append(a+':'+b) # concatenate to create time format
        faces.append(filename)
        
dict_face = dict(zip(faces, times)) # zip to create dict with faces as keys and times as values

def question(progress_tracker = None):
    face, time = random.choice(list(dict_face.items()))
    
    question_bank = ['The clock face shows a time past noon. Enter the time on the clock face in the 12 hour format (example: 2:55 PM): ',
                     'The clock face shows a time before noon. Enter the time on the clock face in the 12 hour format (example: 2:55 AM): ',
                     'The clock face shows a time past noon. Enter the time on the clock face in the 24 hour format (example: 14:55): ',
                     'The clock face shows a time before noon. Enter the time on the clock face in the 24 hour format (example: 02:55): ']
    question = random.choice(question_bank)
    num = question_bank.index(question)
    
    hr, mn = time.split(':')
    tfr_hr_pm = str(int(hr)+12) + ':' + mn
    tfr_hr_am = hr.rjust(2, '0') + ':' + mn
    answer_key = [time+' PM', time+' AM', tfr_hr_pm, tfr_hr_am]
    
    img = mpimg.imread(path+"\\"+face)
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    
    #-----------------------------------
    #print(answer_key[num]) #for testing
    #-----------------------------------
    
    ans = input(question)
    try:
        #ans = ans.replace(' ', '') # <1> uncomment if spaces in between digits are to be accepted
        if ans == answer_key[num]:
            print('\nGood job! That is the correct time.')
            if progress_tracker:
                progress_tracker.add_pt(1)
            
        elif num == 2 or num == 3:
            hr, mn = ans.split(':')
            hr, mn = hr.strip(), mn.strip()
            
            if hr+':'+mn == answer_key[num]:
                print('\nThat is the correct time! Try to follow the format given next time.')
                if progress_tracker:
                    progress_tracker.add_pt(0.5)
            else:
                print('\nIncorrect. Ensure your digits are not spaced out and learn how to read the clock!')

        else:
            hr, tail = ans.split(':')
            
            tail = tail.replace(' ', '') # delete if <1>
            # tail contains minutes with AM/PM without whitespace
            
            mn, ap = tail[0: -2], tail[-2:].upper() # mn contains minutes, ap is the AM/PM string
                
            if hr.strip()+':'+mn+' '+ap == answer_key[num]: # delete .strip() if <1>
                print('\nThat is the correct time! Learn to present your answer better by following the given format.')
                if progress_tracker:
                    progress_tracker.add_pt(0.5)
            else:
                print('\nIncorrect. Ensure your digits are not spaced out and learn how to read the clock!')
    except:
        print('\nIncorrect. Ensure your digits are not spaced out and learn how to read the clock!')

#--------------------------------

# Read clock faces for story
morning_dict = {}
noon_dict = {}
evening_dict = {}
night_dict = {}

for face, time in dict_face.items():
    
    if time.startswith('6'):
        morning_dict[face] = time
        
    elif time.startswith('12') or time.startswith('1') or time.startswith('2'):
        noon_dict[face] = time
        
    elif time.startswith('5') or time.startswith('6'):
        evening_dict[face] = time
        
    elif time.startswith('9') or time.startswith('10'):
        night_dict[face] = time
        
    elif time.startswith('7'):
        morning_dict[face] = time
        evening_dict[face] = time
        
    elif time.startswith('8'):
        morning_dict[face] = time
        night_dict[face] = time
        
    else: pass

morn2nitetimes = [morning_dict, noon_dict, evening_dict, night_dict]

def story_question(time_of_day, twelve_hour_or_twenty_four_hour, progress_tracker = None, qn_num = 0, player = 'Timmy'):
    # set twelve_hour_or_twenty_four_hour = 'twenty-four hour'  for correct answer to be set in the twenty-four hour format
    
    ls = ['Morning', 'Noon', 'Evening', 'Night']
    # Morning := 6 - 8+ am, Noon := 12 - 2+ pm, Evening := 5 - 7+ pm, Night := 8 - 10+ pm
    idx = ls.index(time_of_day)
    face, time = random.choice(list(morn2nitetimes[idx].items()))
    
    hr, mn = time.split(':')
    tfr_hr_pm = str(int(hr)+12) + ':' + mn
    tfr_hr_am = hr.rjust(2, '0') + ':' + mn
    
    if time_of_day == 'Morning' and twelve_hour_or_twenty_four_hour == '12 hour':
        answer_key = time+' AM'
        
    elif time_of_day == 'Morning' and twelve_hour_or_twenty_four_hour == '24 hour':
        answer_key = tfr_hr_am
        
    elif (time_of_day == 'Noon' or time_of_day == 'Evening' or time_of_day == 'Night') and twelve_hour_or_twenty_four_hour == '12 hour':
        answer_key = time+' PM'
        
    elif (time_of_day == 'Noon' or time_of_day == 'Evening' or time_of_day == 'Night') and twelve_hour_or_twenty_four_hour == '24 hour':
        answer_key = tfr_hr_pm
    else:
        return "Invalid input"
    print(answer_key)
    
    img = mpimg.imread(path+"\\"+face)
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    
    #-----------------------------------
    #print(answer_key[num]) #for testing
    #-----------------------------------
    
    questions = [f'Good morning, {player}! You just woke up and look at the clock.\nWhat time is it now in the {twelve_hour_or_twenty_four_hour} format?',
                f'The movie starts to get boring and you are hungry.\nWhat time is it now in the {twelve_hour_or_twenty_four_hour} format?',
                f'After eating lunch, you have a Math quiz. In the middle of the test, you look at the clock.\nWhat time is it in the {twelve_hour_or_twenty_four_hour} format?']
    
    ans = input(questions[qn_num])
    try:
        #ans = ans.replace(' ', '') # <1> uncomment if spaces in between digits are to be accepted
        if ans == answer_key:
            print('\nGood job! That is the correct time.')
            
        elif twelve_hour_or_twenty_four_hour == '24 hour':
            hr, mn = ans.split(':')
            hr, mn = hr.strip(), mn.strip()
            
            if hr+':'+mn == answer_key:
                print('\nThat is the correct time! Try to follow the format given next time.')
                
            else:
                print('\nIncorrect. Ensure your digits are not spaced out and learn how to read the clock!')

        else:
            hr, tail = ans.split(':') 
            
            tail = tail.replace(' ', '') # delete if <1>
            # mn contains minutes with AM/PM without whitespace
            
            mn, ap = tail[0: -2], tail[-2:].upper() # mn contains minutes, ap is the AM/PM string
                
            if hr.strip()+':'+mn+' '+ap == answer_key: # delete .strip() if <1>
                print('\nThat is the correct time! Learn to present your answer better by following the given format.')
                    
            else:
                print('\nIncorrect. Ensure your digits are not spaced out and learn how to read the clock!')
    except:
        print('\nIncorrect. Ensure your digits are not spaced out and learn how to read the clock!')

# Unit Testing
# -------------------------------------------
# read_the_time()
# read_clock_story_mode("Morning", "12 hour")