#16.1 Use the datetime module to write a program that gets the current date and prints the day of the week.
def print_day():
    today = datetime.today()
    print('Today is',today.strftime('%A'))

#16.2.2 Write a program that takes a birthday as input and prints the user’s age and the number of days, hours, minutes and seconds until their next birthday.
def time_to_bday():
    
    format= False
    while format==False:
        bday=input('input your birthday (dd/mm): ')
        try: 
            birthday=datetime.strptime(bday, '%d/%m')
            format=True
        except:
            print('incorrect date format')

    print('Your birthday is %s %s' %(birthday.strftime('%d'), birthday.strftime('%B')))
    #calander_bday is the string for this year's bhirthday
    calander_bday= bday +"/" +  datetime.strftime(datetime.today(), '%Y')
    #calcnder_birthday is the date of this year's birthday
    calander_birthday=datetime.strptime(calander_bday, '%d/%m/%Y')
    #checks to see if calander birthday is the next birthday, if not then add 365 days
    if calander_birthday>datetime.today():
        next_birthday=calander_birthday
    else:
        next_birthday=calander_birthday+timedelta(days=365)
        if next_birthday.day != birthday.day:
            #adds an additional day for leap years
            next_birthday = next_birthday + timedelta(days=1)

    #prints next birthday
    print('Your next_birthday is on %s %s %s'  %(next_birthday.strftime('%d'), next_birthday.strftime('%B'), next_birthday.strftime('%Y')) )
    
    #calculates countdown as a timedelta
    countdown = next_birthday - datetime.today()
    #converts timedelta to separtate variables for days, hours, min and sec
    countdown_days = countdown.days
    seconds_remaining = countdown.total_seconds() - countdown_days*24*60*60
    countdown_hours = seconds_remaining//60**2
    seconds_remaining= seconds_remaining%60**2
    countdown_min = seconds_remaining//60
    seconds_remaining = seconds_remaining%60
    countdown_sec = int(seconds_remaining)


    #prints out countdown
    print('The time until your next birthday is: %s days, %s hours, %s minutes and %s seconds' 
          %(countdown_days,countdown_hours,countdown_min,countdown_sec))
    return

def double_day():
    DOB1 = '15/9/1973'
    DOB2 = '15/9/2010'
    
    dob1= datetime.strptime(DOB1, '%d/%m/%Y')
    dob2= datetime.strptime(DOB2, '%d/%m/%Y')
    
    older = dob1-dob2
    day = dob2 - older
    print (older)
    print (day.strftime('%d'),day.strftime('%B'),day.strftime ('%Y'))

    age1 = day-dob1
    age2 = day - dob2
    print (age1)
    print (age2)
    print(age1/age2)

    
    return

def n_day():
    DOB1 = '15/9/2000'
    DOB2 = '08/08/2010'
    n=4
    dob1= datetime.strptime(DOB1, '%d/%m/%Y')
    dob2= datetime.strptime(DOB2, '%d/%m/%Y')
    
    older = dob1-dob2
    day = dob2 - older/(n-1)
    print (older)
    print (day.strftime('%d'),day.strftime('%B'),day.strftime ('%Y'))

    age1 = day-dob1
    age2 = day - dob2
    print (age1)
    print (age2)
    print(age1/age2)

    
    return

#main
from datetime import datetime
from datetime import timedelta
#Exercise 16.2 Question 1
#print_day()
#Exercise 16.2 Question 2
#time_to_bday()
#Exercise 16.2 Question 3
double_day()
n_day()