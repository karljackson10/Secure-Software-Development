  
class Vehicle:
    """Represents a vehicle"""
    
    def __init__(self,  reg, make, model):
        self.cat= type(self)
        self.reg = reg
        self.make = make
        self.model = model
  

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

        return vehicle_details
    



class Car(Vehicle):
    """represent a car"""

    def dual_carriageway_speedlimit(self):
        """returns the speed limit on a dual carrige way"""
        return ('70mph')
    
class Van(Vehicle):
    """represent a van"""
    def dual_carriageway_speedlimit(self):
        """returns the speed limit on a dual carrige way"""
        return ('60mph')
    
class HGV(Vehicle):
    """represent a HGV"""

    def dual_carriageway_speedlimit(self):
        """returns the speed limit on a dual carrige way"""
        return ('50mph')



#Main
van=Van('V1', 'Citroen', 'Berlingo')
car=Car('C1', 'Volvo','XC90')
truck=HGV('H1', 'Mercedes', 'Actros' )

for vehicle in (car,van,truck):
    
    print (vehicle)
    print ('Dual Carriageway Speed Limit: ' + vehicle.dual_carriageway_speedlimit())
