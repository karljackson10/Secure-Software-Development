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

    
    #print time method
    def print_time(self):
        print(' %.2d:%.2d:%.2d' %(self.hour, self.minute, self.second))
        return
    #add_time method adds 2 time tpes
    def add_time(self,other):
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

#main
start=Time(9,45)
#start.hour = 9
#start.minute = 45
#start.second =00

#start.print_time()
print('start :',start)
#duration = Time(1,35)
duration=100
print('duration: ',duration)
print('end: ',start+duration)
print('end: ', duration+start)
#end = start.increment(1337)
#print(end)
#end.print_time()
#print(end.is_after(start))