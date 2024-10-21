from datetime import datetime 

print(dir(datetime))



# Oct 21, 2024
# October 21, 2024
# 21 October 2024
now = datetime.now()
t = now.strftime("%H:%M:%S")

time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_one)

def generate_time(format = 'eu'):
    time_eu = now.strftime("%A %b %B %m/%d/%Y, %H:%M:%S")
    time_us = now.strftime("%d/%m/%Y, %H:%M:%S")
    # time_long = now.strftime('%d %B %Y %I:%M %p')
    time_long = now.strftime('%d/%m/%Y %I:%M %p')
    time_long = now.strftime('%d/%m/%Y %I:%M %p')
    print(time_long, type(time_long))
    if format.lower() == 'us':
        time_format = time_us
    elif format.lower() == 'eu':
        time_format = time_eu
    else:
        pass 
    
    return time_format

print(generate_time('us'))
print(generate_time('US'))
print(generate_time('Eu'))
print(generate_time())

date_string = "5 December, 2019"
print(date_string, type(date_string))
date_obj = datetime.strptime(date_string, '%d %B, %Y')
print(type(date_obj))
print(date_obj.year)
print(date_obj.month)
print(date_obj.day)
from datetime import time, date

print(time(18, 23, 55))
sometime_back = date(year=2019, month=11, day=22)
today = date(2024, 10, 21)
print(today - sometime_back)

from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)


from datetime import datetime, timedelta


# Using current time
ini_time_for_now = datetime.now()

# printing initial_date
print ('initial_date:', str(ini_time_for_now))

# Calculating past dates
# for two years
past_date_before_2yrs = ini_time_for_now - \
                       timedelta(days = 730)


# for two hours
past_date_before_2hours = ini_time_for_now - \
                        timedelta(hours = 2)


# printing calculated past_dates
print('past_date_before_2yrs:', str(past_date_before_2yrs))
print('past_date_before_2hours:', str(past_date_before_2hours))