import datetime

now = datetime.datetime.now()

now_year = now.year
now_month = now.month
now_day = now.day

# print(now_year)

var_weekday = datetime.date(now_year,now_month,now_day).weekday()

# print(var_weekday)

# 0 Mon; 1 Tue; 2 Wed; 3 Thur; 4 Fri; 5 Sat; 6 Sun

if var_weekday == 5:
    print('Party!')
elif var_weekday == 6:
    print('recover')
else:
    print('work, work, work...')

    
# elif is the python else if condition
