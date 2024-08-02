#####################################################################################################
#                                                                                                   #
#           import modules                                                                          #
#                                                                                                   #
#####################################################################################################

# Import the Road class from the maps module
from maps import Road


# Import the Car class from the vehicles module
from vehicle import  Car

# Import the Log class from the vehicle module to store the log of a journey
from vehicle import Log




 ###################################################################################################
 #                                                                                                 #
 #                         Test 1 : Display Route                                                  #
 #                                                                                                 #
 ###################################################################################################
  
 #Define road coordinates

road_data = [  [0,0,0,0], [1,100,100,1], [2,200,100,1], [3,300,100,1.5], [4,400,200,1.7], [5,500,300,2.0], [6,500,400,1.5], [7,600,500,1.0], [8,700,400,1.2], [9,800,400,1.2], [10,900,300,1.4], [11,1000,300,1.4]        ]

#Create a route object
route=Road('Test', 'A',road_data)

# Display the route
print ('Test 1: Display Route')
print(route)



#####################################################################################################
#                                                                                                   #
#       Create instances for the Log and Car Objects                                                #
#                                                                                                   #
#####################################################################################################

# Define the name of the log file
file='log.csv'

# Create a log object
log=Log(file)

# Create a car object
car=Car('HK61','Volvo','XC90', route, log)


#####################################################################################################
#                                                                                                   #
#           Test2: Drive the car through each road segment in the route                             #
#                                                                                                   #
#####################################################################################################

print('\nTest 2: Drive Car On Route')

while len(route.segments)>0:
    car.drive_car()

#save the journey log
log.save()

#####################################################################################################
#                                                                                                   #
#           Test3: Emergency Stop                                                                   #
#                                                                                                   #
#####################################################################################################

# Define the speeds for emergency stop testing 
# Speeds are in m/s

speed = [8.9, 13.4, 17.9, 22.3, 26.8, 31.3]


# The road for emergency stop testing is a 1km straing road with zero gradient
road_data = [  [0,0,0,0], [1,1000,0,0]]

print('\nTest 3 Emergency Stop')

# Emergency Stop Testing for each speed
for n in range(len(speed)):

    # Initiate the road for rsting
    # Road type B with high speed limit of 31.4m/s
    route=Road('Stop', 'B',road_data)

    # Initiate an Emergency Stop journey log
    file = 'Emergency_Stop_ %.2f.csv'  %(speed[n])
    log= Log(file)

    # Initiate a car for testing
    car=Car('HK61','Volvo','XC90', route, log)

    # Set the car of on the straight road at a defined test speed
    car.drive.speed=speed[n]
   
    # Print test
    print ('\nEmergency Stop Speed %.2f' %(car.drive.speed) )
    
    # Perform the emergency-stop method
    car.emergency_stop()
    # Print final car data
    print(car)
    # Save journey log file
    log.save()
