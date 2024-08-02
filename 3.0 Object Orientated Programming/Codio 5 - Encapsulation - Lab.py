#Encapsulation Lab

import csv

# **********************************************
# code for the CoffeeJournal class
# **********************************************

class CoffeeJournal:
    def __init__(self, file):
        self._file = file
        self._roaster = ""
        self._country = ""
        self._region = ""
        self._stars = ""
        self._new_coffee = []
        self._old_coffee = self.load_coffee()
    def load_coffee(self):
        coffee = []
        with open(self._file) as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                coffee.append(row)
        return coffee
    
    def add_coffee(self):
        self._new_coffee.append([self._roaster, self._country, self._region, self._stars])
    
    #he save method opens the CSV file in append 'a' mode. 
    #The 2D list stored in _new_coffee is added to the end of the CSV file. 
    def save(self):
        with open(self._file, 'a') as f:
            writer = csv.writer(f)
            writer.writerows(self._new_coffee)


    def show_coffee(self):
        print()
        print('old Coffee len: ',len(self._old_coffee))
        print('new coffee lem: ', len(self._new_coffee))
        # if there is no information on any coffee, tell the user to add one
        if len(self._old_coffee) < 2 and len(self._new_coffee) == 0:
            print("Enter a coffee first")
        # if there is information in the CSV but not new coffee print the old coffee
        elif len(self._old_coffee) > 2 and len(self._new_coffee) == 0:
            print('True')
            print('self._old.coffee')
            for row in self._old_coffee:
                for i in row:
                    print(f'{str(i):13}', end=" ")
                print('\n')
                #print(f"{row[1]:13} {row[1]:13} {row[2]:13}  {row[3]:13}")
        # print both the old coffee and the new coffee
        else:
            for row in self._old_coffee:
                print(f"{row[1]:13} {row[1]:13} {row[2]:13}  {row[3]:13}")
            for row in self._new_coffee:
                print(f"{row[1]:13} {row[1]:13} {row[2]:13}  {row[3]:13}")
        print()

    @property
    def roaster(self):
        return self._roaster
  
    @roaster.setter
    def roaster(self, new_roaster):
        self._roaster = new_roaster

    @property
    def country(self):
        return self._country
  
    @country.setter
    def country(self, new_country):
        self._country = new_country
    
    @property
    def region(self):
        return self._region
  
    @region.setter
    def region(self, new_region):
        self._region = new_region
    
    @property
    def stars(self):
        return self._stars
  
    @stars.setter
    def stars(self, new_stars):
        self._stars = new_stars
    
# **********************************************
# code for testing your script
# **********************************************

#Note paths in Python use / rather than \
path='C:/Users/User\OneDrive/1. University of Essex/3.0 Object Orientated Programming/Encapulation/'
"""test_object = CoffeeJournal(path+'book1.csv')
test_object.load_coffee()
print(test_object._old_coffee)

# **********************************************
# code for testing your script 2
# **********************************************

try:
    test_object = CoffeeJournal(path+'book2.csv')
except:
    open('book2.csv','w')
    test_object =CoffeeJournal(path+'book2.csv')

test_object.roaster = "Peace River"
test_object.country = "Rawanda"
test_object.region = "Remera"
test_object.stars = "***"
print(test_object.roaster)
print(test_object.country)
print(test_object.region)
print(test_object.stars)

# **********************************************
# code for testing your script 3
# **********************************************

test_object = CoffeeJournal(path+'book2.csv')
#test_object.show_coffee()
"""
# **********************************************
# code for testing your script 4
# **********************************************

test_object = CoffeeJournal(path+'book2.csv')
test_object.roaster = "Peace River"
test_object.country = "Rawanda"
test_object.region = "Remera"
test_object.stars = "***"
test_object.add_coffee()
print(test_object._old_coffee)
print(test_object._new_coffee)
test_object.save()
print(test_object._old_coffee)
test_object._old_coffee = test_object.load_coffee()
print('old coffee')
print(test_object._old_coffee)
"""test_object._roaster = ""
test_object._country = ""
test_object._region = ""
test_object._stars = ""
test_object._new_coffee = []
test_object.show_coffee()"""