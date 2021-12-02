import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Setup
dirname = os.path.dirname(__file__)
path = rf'{dirname}\\..\resources'
# path = r'C:\Users\dianm\Desktop\PG\1D\TTTM\resources' # replace with own directory path

times = []
faces = []
for filename in os.listdir(path): # iterate over files in path folder
    
    if filename.endswith(".png"): # selecting only png image files (clock faces)
        a, b, _ = filename.split(".") 
        times.append(a+':'+b) # concatenate to create time format
        faces.append(filename)
        
dict_face = dict(zip(faces, times)) # zip to create dict with faces as keys and times as values

# Troubleshooting -> run this to check output
# print(dict_face) # dictionary of clock png files and corresponding times on clock faces
# print('-----------------------')
# print('number of faces:', len(dict_face)) # 40 images in total

# for face, time in dict_face.items(): # loop to display clock faces with corresponding times below
#         img = mpimg.imread(face)
#         plt.imshow(img)
#         plt.show()
#         print(time)

# Reading clock faces (1st game)
import random

# TODO: Ask if we should prompt if user accidentally pressed enter
# TODO Description: Picks random preset question
# Parameters: progress_tracker (Progression class)
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
    
    ans = input(question)
    while ans == "":
        input(question)
        
    try:
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
                print('\nIncorrect. Check your input and learn how to read the clock!')
        else:
            hr, tail = ans.split(':')
            mn, ap = tail.split()
            hr, mn, ap = hr.strip(), mn.strip(), (ap.strip()).upper()
            if hr+':'+mn+' '+ap == answer_key[num]:
                
                print('\nThat is the correct time! Try to follow the format given next time.')
                if progress_tracker:
                    progress_tracker.add_pt(0.5)
            else:
                print('\nIncorrect. Check your input and learn how to read the clock!')
            
    except:
        print('\nIncorrect. Check your input and learn how to read the clock!')

# Troubleshooting -> run this to check logic
#question()