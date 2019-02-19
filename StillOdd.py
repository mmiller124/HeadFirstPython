from datetime import datetime
import time

odds = range(1,60,2)

right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute.")

print(time.strftime("%H %M"))
