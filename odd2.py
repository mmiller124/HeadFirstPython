from datetime import datetime
import time
import random

# list is like a very powerful array
# it can be on many lines
odds = [ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]



for i in range(5):
    print(time.strftime("%H:%M"))
        
# variable being created and assigned
# create an object that represents today's time, then extract the value of the minute attribute before assigning it to a variable
    right_this_minute = datetime.today().minute

# is the right_this_minute variable inside the odds list
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")

    if i < 4:
        RandTime = random.randint(1,60)
        print("waiting " + str(RandTime) + " seconds")
        time.sleep(RandTime)
