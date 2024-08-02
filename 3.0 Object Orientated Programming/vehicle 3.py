  
class Vehicle:
    """Represents a vehicle database"""
    
    def __init__(self,  data):
        self.cars=[]
        #creates a Car object for each car in the dictionary
        for car in data:
             self.cars.append(Car(data[car]['reg'], data[car]['make'], data[car]['model']))
      
  

    def __str__(self):
        """Displays the cars in of the vehicle database"""
        c=[]
        for car in self.cars:
             c.append(str(car))
        
        return '\n'.join(c)
    



class Car:
    """represent a car"""

    def __init__ (self,reg,make,model):

        self.reg=reg
        self.make =make
        self.model = model

    def __str__(self):
        """Displays the properties of a car"""

        return ('reg: '+str(self.reg) + ' make: '+str(self.make)+ ' model: '+str(self.model))
    
    

#Main


# Nested Dictionary of Cars
data = {
            'Car1' :{
                'reg' :'C1',
                'make': 'Volvo',
                'model':'XC90'
             },
            'Car2' : {
                'reg': 'C2',
                'make':'Citreon',
                'model':'Berlingo'
            }
         }

#Dictionary methods        
for car, obj in data.items():
            #prints the car dictionary name 
            print('\n',car)
            #prints the keys in the dictionary
            print(data[car].keys())
            #prints the values for each key in the dictionary
            print(data[car].items())


#creates a vehicle data base of Cars from the data
v =Vehicle(data)
#prints a single car from the list

print('\nThe first car is: ' +str(v.cars[0]))
#prints all the vehiceles
print('\nVehicle List')
print(v)


            