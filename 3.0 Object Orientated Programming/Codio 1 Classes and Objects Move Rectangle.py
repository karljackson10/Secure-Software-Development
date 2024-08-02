### As an exercise, write a function named move_rectangle that takes a Rectangle and two numbers named dx and dy. 
### It should change the location of the rectangle by 
### adding dx to the x coordinate of corner and adding dy to the y coordinate of corner.

def move_rectangle (rect, dx, dy):
 
    rect.corner.x +=dx
    rect.corner.y +=dy

    return 
    



### Main
import math
### Defines Point as a class
class Point:
    """Represents a co-ordinate"""
### Defined Rectangle as a class
class Rectangle:
    """Represents a rectange
        attributes: width, height, corner"""



### Define bo1x as a Rectangle

box = Rectangle()
box.width = float(input('box width:'))
box.height = float(input('box height'))
box.corner = Point()
box.corner.x = float(input('corner(x):'))
box.corner.y= float(input('corner (y):'))



### Get movement vector
move_x=float(input('Move Rectangle (x):'))
move_y=float(input('move Rectangle (y):'))

move_rectangle(box, move_x, move_y)

print("new corner: (%g , %g)" %(box.corner.x, box.corner.y))






