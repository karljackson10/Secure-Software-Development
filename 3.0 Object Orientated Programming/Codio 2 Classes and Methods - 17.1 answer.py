"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


class Time:
    """Represents the time of day as seconds since midnight.
       
    attributes: second
    """
    def __init__(self,  second=0):
        """Initializes a time object.

                second: int
        """
        self.second = second

    def __str__(self):
        """Returns a string representation of the time."""
        hour = self.second//60**2
        seconds_remaining= self.second%60**2
        minute = seconds_remaining//60
        second = seconds_remaining%60
        return '%.2d:%.2d:%.2d' % (hour, minute, second)

    def print_time(self):
        """Prints a string representation of the time."""
        print(str(self))

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        
        return self.second

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.time_to_int() > other.time_to_int()

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        if  self.second < 0:
            return False
        if  self.second >= 60*60*24:
            return False
        return True


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    #minutes, second = divmod(seconds, 60)
    #hour, minute = divmod(minutes, 60)
    time = Time(seconds)
    return time


def main():
    start = Time(9*60**2 + 45*60 + 00)
    start.print_time()

    end = start.increment(1337)
    #end = start.increment(1337, 460)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9*60**2 +  45*60)
    duration = Time(1*60**2 + 35*60)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7*60**2 + 43*60)
    t2 = Time(7*60**2 + 41*60)
    t3 = Time(7*60**2 + 37*60)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()
