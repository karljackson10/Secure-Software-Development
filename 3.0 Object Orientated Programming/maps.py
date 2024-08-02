import math
class Point:
    """Represents a GPS Position"""
    def __init__(self, long=0, lat=0, alt=0):
        self.long = long
        self.lat = lat
        self.alt = alt
    
    def __str__(self):
        """Displays the GPS coordinates longitude, latitude, altitude"""

        #Coordinates are displayed to 2 decimal places
        return '(%.2f, %.2f, %.2f)' %(self.long, self.lat, self.alt)

    def get_direction(self, end):
        """Returns the 2D directional vector to a specified point - end"""
        
        direction=Direction()
        direction.long = end.long - self.long
        direction.lat = end.lat - self.lat

        return direction


class Direction(Point):
    """Represents a direction
    As a direction is a 3D vector, it has the same data structure as a 3D Point.  
    The new class Direction inherits the object properties of the Point object.  
    This makes the code easier to read"""



class Road_Segment:
    """Represents a road segment"""

    def __init__ (self, index, location_start, location_end, speed_limit):
        self.index = index
        self.location_start = Point(location_start[1], location_start[2], location_start[3])
        self.location_end = Point(location_end[1], location_end[2], location_end[3])
        self.speed_limit = speed_limit
        self.direction = self.location_start.get_direction( self.location_end)
        self.distance = self.get_distance()
        self.gradient = self.get_gradient()
        
    def __str__(self):
        """Dispays the data from the Road_Segment in a readable form"""
        index = str(self.index)
        start = ':From: ' + str(self.location_start) 
        end = ' To: ' + str(self.location_end)
        direction = ' Direction' + str(self.direction)
        #Display gradient and distance to 2 decimail places
        #The gradient is a percentage
        gradient = ' Gradient: %.2f' %self.gradient +'%'
        distance = ' Distance: %.2fm' %self.distance
        limit = ' Speed Limit: %.2fm/s' %self.speed_limit

        return index + start + end + direction + gradient + distance + limit

    def get_distance(self):
        """Calculates the distance travelled between 2 3D points"""

        long_dist = self.location_end.long - self.location_start.long
        lat_dist = self.location_end.lat - self.location_start.lat
        alt_dist = self.location_end.alt - self.location_start.alt
        #Uses Pythagoras’ Theorem to calculate the distance between 2 points  

        distance = math.sqrt(long_dist**2 + lat_dist**2 + alt_dist**2)

        return distance
    
    def get_gradient(self):
        """Calculates the gradient of the road section"""
        #calcultes the distance in teh x-y plane
        long_dist = self.location_end.long - self.location_start.long
        lat_dist = self.location_end.lat - self.location_start.lat
        distance_xy = math.sqrt(long_dist**2 + lat_dist**2 )
        #height is the change in altitute
        height = self.location_end.alt - self.location_start.alt
        #the gradient is the change in height over the distance travelled
        gradient = height/distance_xy
        #represent the gradient as a percentage
        gradient =gradient*100

        return gradient


class Road:
    """Represents a road"""

    def __init__ (self, name, category, data):
        self.name= name
        self.category = category
        self.data= data
        limit = 13.4
        #uses the start and end GPS coordinates to derive road segment data
        self.segments =[]
        for i in range (len(data)-1):
                segment = Road_Segment(i, data[i], data[i+1], limit)
                self.segments.append(segment)
    
    def __str__(self):
        """Displays the road data with a heading and series of road segment descriptions"""
        #creates an empty list to store the road segment data
        segs = []
        
        #creates a list of individual string representtions for each segment
        for segment in self.segments:
            segs.append(str(segment))
        #Header and each segment on a new line
        return 'Road: ' + str(self.name) + ' Type:' + str(self.category) +'\n' + '\n'.join(segs)
    
    def get_road_segment (self):
        """ returns a road segment from a que"""
        
        return self.segments.pop(0)
    
    def get_speed_limit(self):
        if self.category=="A":
            return 13.4
        else:
            return 31.3
    
