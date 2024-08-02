class Time:
    """Represents the time of day.
    attributes: hour,  minute, second"""
    #initialization
    def __init__(self, hour=0, minute =0, second =0):
        self.hour=hour
        self.minute = minute
        self.second =second
        return
    
    #special string method used form print function
    def __str__(self):
        return ' %.2d:%.2d:%.2d' %(self.hour, self.minute, self.second)
    
    #speciall add method used for + opperator
    def __add__(self,other):
        if isinstance(other,Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    #special radd method - right sided addiion, if the object is on the right of the +
    def __radd__(self,other):
        return self.__add__(other)

    #checks if a time is valid
    def valid_time (self):
        if self.hour<0 or self.minute<0 or self.second<0:
            return False
        if self.hour>23 or self.minute>=60 or self.second>=60:
            return False
        if type(self.hour) != int or type(self.minute) != int or type(self.second) != int:
            return False
        return True
 
   #print time method
    def print_time(self):
        
        print(' %.2d:%.2d:%.2d' %(self.hour, self.minute, self.second))
        return
    #add_time method adds 2 time tpes
    def add_time(self,other):
        print(self.valid_time())
        print(other.valid_time())
        assert self.valid_time() and other.valid_time(), print('error')
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
    #time_to_int method returns time in seconds
    def time_to_int(self):
        time_in_seconds = self.hour*60**2 + self.minute*60 + self.second
        return time_in_seconds
    #increment method increases time object by seconds
    def increment(self,seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    #is_after method tests if other time is after the object
    def is_after(self, other):
        return self.time_to_int()>other.time_to_int()

#function int_to_time
def int_to_time(total_seconds):
    # new object t2 is the answer to the incriment
    t2 =Time()
    #define hours taking the whole number answer to seconds/3600
    h=total_seconds//(60**2)
    #ensure that hours over 24 are rest to 0. Could change 24 to 12 for 12 hour clock
    h=h%24
    #s is the seconds remaining after allocatingn any hours
    s=total_seconds%(60**2)
    #define minutes by taking the remaining seconds and dividing by 60
    m=s//60
    #s is the seconds remaining after allocating the minutes
    s=s%60
    #assign h,m,s to attributes
    t2.hour =  h
    t2.minute =  m
    t2.second = s
    return t2

#checks if a time is valid
def time_check (self):
    if self.hour<0 or self.minute<0 or self.second<0:
        return False
    if self.hour>23 or self.minute>=60 or self.second>=60:
        return False
    print(type(self.hour))
    return True
#prints attributes 
def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr) )

#main
race_time = Time()
race_time.hour = 3
race_time.minute = 34
race_time.second = 5

race_distance = 26.2

total_min = race_time.time_to_int()/60
print('min per mile: %f' %(total_min/race_distance))
