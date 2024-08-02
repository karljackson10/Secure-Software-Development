import math
import csv

class Movement:
    """Represent the dynamics for a moving object"""

    #The Movement class is a component class of the teh Vehicle has
    #This is used to decribe the movement of the vehicle
    def __init__(self,location = [0,0,0], direction=[0,0], gradient=0, speed=0, acceleration=0, time=0):
        self.location=location
        self.direction = direction
        self.gradient = gradient
        self.speed= speed
        self.acceleration = acceleration
        self.time=time


class Sensor:
    """Represents the vehicle sensors"""

    #This is limited to the energency stop settings in this example

    def __init__ (self, emergency_stop=False):
        self.emergency_stop=emergency_stop
        




class Vehicle:
    """Represents a vehicle"""
    
    def __init__(self,  reg, make, model, route,log):
        self.cat= type(self)
        self.reg = reg
        self.make = make
        self.model = model
        self.route = route
        self.log = log
        self.segment = route.get_road_segment()
        self.drive = Movement(self.segment.location_start, self.segment.direction, self.segment.gradient)
        self.sensor = Sensor()

    def __str__(self):
        """Displays the properties of a vehicle"""
        
        #defines the category of the vehicle by determining the component class
        if isinstance(self, Car):
            category = 'Car'
        elif isinstance(self, Van):
            category= 'Van'
        else:
            category='HGV'
        
        vehicle_details= category+': ' + self.make +' ' + self.model + ' :' + self.reg 
        vehicle_details+='\nLocated at: ' + str(self.drive.location)  
        vehicle_details+='\nMoving in direction: ' +str(self.drive.direction) 
        vehicle_details+=' Gradient: %.2f' %(self.drive.gradient)+'%'
        vehicle_details+= '\nSpeed: %.2fm/s' %(self.drive.speed) 
        vehicle_details+= ' Acceleration: %.2fm/s2'  %(self.drive.acceleration) 
        vehicle_details+= '\nTime: %.2fs' %(self.drive.time) 
        return vehicle_details
    
#################################################################################
#                                                                               #
#           Movement Paraments for aceleration and breaking defined             #
#                                                                               #
#################################################################################

    def accelerate (self):
        """Acerlation at 4 m/s2"""
        self.drive.acceleration =2
        
    
    def cruise(self):
        """cruise at speed limit"""
        self.drive.acceleration=0
        
    
    def brake (self):
        """Acceleration at - 4m/s2"""
        self.drive.acceleration =-2
        
       
    
    def emergency_brake (self):
        """Acceleration at -5m/s2"""
        self.drive.acceleration =-5
        self.sensor.emergency_stop=True
        self.drive_car()
       
    

#####################################################################################
#                                                                                   #
#          Methods to update the movement dynamics of the vehicle                   #
#          Basic Physics suvat equations have been applied                          #
#          s = displacement                                                         #
#          u = initial speed                                                        #
#          v = final speed                                                          #
#          a = acceleration                                                         #
#          t = time                                                                 #
#                                                                                   #
#####################################################################################
    
    def update_speed (self,s,t):
        """change in speed after t seconds"""
    
        #to model more acuratly t<1
        u= self.drive.speed
        a =self.drive.acceleration
        v= round(u+a*t,3)
        #if decelerating, ensure the stops and doesn't move backwards
        self.drive.speed = max ( 0, v)
            
               
    
    def update_location (self,s,t):
        """update the location"""
        #r is the magitude of the direction which is used to resolve the displacement 
        r=math.sqrt(self.drive.direction.long**2 + self.drive.direction.lat**2)
        
        #update location in the x plane
        self.drive.location.lat += self.drive.direction.lat/r * s 
        #update the location in the y plane
        self.drive.location.long += self.drive.direction.long/r *s
        
        #update the altitude
        self.drive.location.alt +=  self.drive.gradient * s*t
       
      
    
    def distance_traveled (self,t):
        """Returns the the distance traveled in t seconds"""
        u=self.drive.speed
        a=self.drive.acceleration
        s=u*t + 0.5 *a*t**2
        
        return s
    

#############################################################################
#                                                                           #
#           Drive Method                                                    #
#                                                                           #
#############################################################################


    def drive_car(self,time_interval=0.01):
        """adjusts aceralation and sterring according to location and slope """

        #speed limit determined by the road segment
        speed_limit= self.segment.speed_limit
        
        


        if self.sensor.emergency_stop==False:

            #accelerate if below the speed limit, or break if too fast

            if self.drive.speed<speed_limit:
                self.accelerate()
            elif self.drive.speed > speed_limit:
                self.brake()
            else:
                self.cruise()
        
        
        
        

        # update the location
        s=self.distance_traveled(time_interval)
        self.update_location(s,time_interval)
        

        #adjust the aceleraiton due to the gradient of the slope
        h = self.drive.gradient *s * time_interval
        g=9.8
        self.drive.acceleration=self.drive.acceleration - (g*h/s)

        # update the speed
        self.update_speed(s,time_interval)
        self.drive.time=round(self.drive.time+ time_interval,2)
        
        #log the movement
        self.log.add_to_log(self.drive)
        
        #steer in a new direction when the checkpoint is reached

        if self.at_checkpoint()==True:
            
            self.steer()
            
  ###############################################################################################
  #                                                                                             #
  #                 Check in arrived at the end of a road segment and adjust stearing           #
  #                                                                                             #
  ###############################################################################################     


    def at_checkpoint(self):
        """method to check the end of a road segment has been reached"""

        #check to see if the location of the vehicle is within 0.5m of the checkpoint
        lat_check= round(self.drive.location.lat,0)==round(self.segment.location_end.lat,0)
        long_check=round(self.drive.location.long,0)==round(self.segment.location_end.long,0)
        #check to see if the altitude is within 0.05m of the checkpoint
        alt_check=round(self.drive.location.alt,1)==round(self.segment.location_end.alt,1)
        
        #display message and vehile attributes when at the checkpoint
        if lat_check and long_check and alt_check:
            print('\nArrived at checkpoint')
            print(self)

        #returns True or False to indicate arrival    
            return True
        else:
            return False
    
    def steer(self):
        """steers to adjust the direction as a new road segment is rreached"""
        
        #gets the new road segment
        self.segment = self.route.get_road_segment()
        self.drive.gradient=self.segment.gradient
        
        #change direction
        self.drive.direction = self.drive.location.get_direction( self.segment.location_end)
        
#############################################################################################
#                                                                                           #
#               Emergency Stop method                                                       #
#                                                                                           #
#############################################################################################
        

    
    def emergency_stop (self):
        while self.drive.speed>0:
            self.emergency_brake()
        self.drive.acceleration=0     
        
    

#############################################################################################
#                                                                                           #
#                   Vehicles Classes                                                        #
#                                                                                           #
#               Car, Van and HGV inherit the vehicle class attributed and methods           #
#                                                                                           #
#############################################################################################



class Car(Vehicle):
    """represent a car"""
    
class Van(Vehicle):
    """represent a van"""
class HGV(Vehicle):
    """represent a HGV"""


#############################################################################################
#                                                                                           #
#           Log Class                                                                       #
#                                                                                           #
#           The Log class is a component class as each Vechile has a Log                    #
#                                                                                           #
#############################################################################################

class Log:
    """represents a journy log"""

    def __init__(self,file):
        self.file =file
        self.log= []
        #Adds heading to the log file
        self.log.append( ['long', 'lat', 'alt', 'gradient', 'speed', 'acceleration', 'time'])
    
    
    def __str__(self):
        """displays the journey log"""
        
        log = []
        
        #takes each row of data as a string
        for row in self.log:
            log.append(str(row))
        
        return '\n'.join(log)
    
    
    def add_to_log (self, data):
        """adds a snapshot of data to the log"""
        
        #add a row of Movemet class data to the log 
        log = [data.location.long,data.location.lat, data.location.alt, data.gradient, data.speed, data.acceleration, data.time]
        self.log.append(log)
         
    

    
    def save(self):
        """saves the log file"""
        
        #opens the log file in write mode
        with open(self.file, 'w', newline='') as f:

            #writes each row of the log list to the file
            writer = csv.writer(f) 
            writer.writerows(self.log)