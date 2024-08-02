### As an exercise, write a version of move_rectangle that creates and returns a new Rectangle instead of modifying the old one.

def move_rectangle (rect, dx, dy):
 
    rect2=copy.deepcopy (rect)
    rect2.corner.x +=dx
    rect2.corner.y +=dy

    return rect2
    



### Main
import math
import copy

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

box2 = move_rectangle(box, move_x, move_y)

print("box corner: (%g , %g)" %(box.corner.x, box.corner.y))
print("box2 corner: (%g , %g)" %(box2.corner.x, box2.corner.y))






