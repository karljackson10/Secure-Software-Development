# rite a function called print_time that takes a Time object and prints it in the form hour:minute:second. 

def print_time(t):
    print(' %.2d:%.2d:%.2d' %(t.hour, t.minute, t.second))
    return

def is_after(t1,t2):
    #compares the time in seconds, multiplying min by 60 and hour by 3600 (60^2)
    check = (t1.hour*60**2+t1.minute*60+t1.second) > (t2.hour*60**2+t2.minute*60+t2.second)

    return check

def increment (time,seconds):
    # new object t2 is the answer to the incriment
    t2 =Time()
    t2 =copy.copy(time)
    t2.second=t2.second+seconds
    
    #total_seconds is the total number of seconds
    total_seconds = t2.hour*60**2 + t2.minute*60 + t2.second
    
    #define hours taking the whole number answer to seconds/3600
    h=total_seconds//(60**2)
    h=h%24
    #s is the seconds remaining after allocatingn any hours
    s=total_seconds%(60**2)
    #define minutes by taking the remaining seconds and dividing by 60
    m=s//60
    #s is the seconds remaining after allocating the minutes
    s=s%60
    
    
    t2.hour =  h
    t2.minute =  m
    t2.second = s
    return t2

#main

import copy

class Time:
    """Represents the time of day.
    attributes: hour,  minute, second"""

time=Time()
time.hour = 23
time.minute = 59
time.second =3

time2=Time()
time2.hour = 11
time2.minute = 40
time2.second =3

print_time(time)

print_time(time2)

print(is_after(time,time2))

s=int(input('Increase time in seconds:'))
print_time(increment(time,s))