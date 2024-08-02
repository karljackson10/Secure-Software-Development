class Point:
    """represents a coodinate"""
    #inialisation method with (0,0) as default
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
        return
    #string methood
    def __str__(self):
        return '(%g, %g)' %(self.x, self.y)
    #add method - operation overload +
    def __add__(self,other):
        if isinstance(other,Point):
            return Point(self.x+other.x  , self.y+other.y)
        else:
            return self.add_tuple(other)

    #special method radd for right addition
    def __radd__(self,other):
        return self.__add__(other)
    
    # asdd method add tuple to Point
    def add_tuple(self,other):
        return Point(self.x+other[0], self.y+other[1])

#main
print('Add two Points')
p=Point(5,2)
print('p: %s' %(p))
q=Point(7,3)
print('q: %s' %(q))
print( 'p+q: %s' %(p+q))

print('Add Point and Tuple')
t=[6,1]
print('p: %s' %(p))
print('t: ', t)
print( p+t)
print (t+p)

