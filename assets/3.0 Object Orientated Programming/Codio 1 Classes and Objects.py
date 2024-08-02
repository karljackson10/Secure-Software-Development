### Returns distance, the distance between two co-ordinates a and b
### Note a and b are alias the objects and change in the function will change the object
def distance_between_points (a,b):

    distance=math.sqrt( (b.x - a.x)**2 + (b.y - a.y)**2 )
    return distance



### Main
import math
### Defines Point as a class
class Point:
    """Represents a co-ordinate"""
### Defines Point1 and Point2 as Point Objects
Point1 =Point()
Point2 =Point()

#Must use float to convert teh string input to a floating point decimal
Point1.x=float(input("Point1 (x):"))
Point1.y=float(input("Point1 (y):"))
Point2.x=float(input("Point2 (x):"))
Point2.y=float(input("Point2 (y):"))

#Print the distance 
print(distance_between_points(Point1, Point2))

