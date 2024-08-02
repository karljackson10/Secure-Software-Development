#Encapsulation Exercises

#Excercise 1
#Define the Country class which has attributes for name, capital, population, and continent. 
#Please use the Python convention for making these attributes private.
class Country:
    def __init__(self, name, capital, population, continent):
        self._name=name
        self._capital=capital
        self._population=population
        self._continent=continent
    
    

#Excercise 2
#Define the Artist class which has attributes for name, medium, style, and famous_artwork. 
#Do not use the Python convention to make these attributes.
class Artist:
    def __init__(self,name, medium, style,famous_artwork):
        self.__name=name
        self.__medium=medium
        self.__style=style
        self.__famous_artwork=famous_artwork

#Excercise 3
#Define the BankAccount class which has attributes for checking and savings. 
#Use the Python convention to make these attributes private. 
#Create the getters get_checking and get_savings, and create the setters set_checking and set_savings.
class BankAccount:
    def __init__(self, checking=0, savings=0):
        self._checking=checking
        self._savings=savings
    
    def get_checking(self):
        return self._checking
    
    def set_checking(self,new_checking):
        self._checking=new_checking

    def get_savings(self):
        return self._savings
    
    def set_savings(self,new_savings):
        self._savings=new_savings


#Excercise 4
#Define the Dancer class which has attributes for name, nationality, and style. 
#Use the Python convention to make these attributes private. 
#Create the getters and setters using the property function.
class Dancer:
    def __init__(self, name, nationality, style):
        self._name=name
        self._nationality=nationality
        self._style=style
    
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        self._name=new_name
    
    def get_nationality(self):
        return self._nationality
    
    def set_nationality(self, new_nationality):
        self._nationality=new_nationality
    
    def get_style(self):
        return self._style
    
    def set_style(self, new_style):
        self._style=new_style

    name = property(get_name, set_name)
    nationality= property(get_nationality, set_nationality)
    style = property (get_style, set_style)


#Excercise 5
#Define the Cyclist class which has attributes name, nationality, and nickname. 
#Use the Python convention to make these attributes private. 
#Create the getters and setters using the property decorator.
class Cyclist:
    def __init__(self, name, nationality, nickname):
        self._name=name
        self._nationality=nationality
        self._nickname=nickname
    
    @property
    def name (self):
        return(self._name)
    
    @name.setter
    def name(self, new_name):
        self._name=new_name
    
    @property
    def nationality (self):
        return(self._nationality)
    
    @nationality.setter
    def nationality(self, new_nationality):
        self._nationality=new_nationality
            
    @property
    def nickname (self):
        return(self._nickname)
    
    @nickname.setter
    def nickname(self, new_nickname):
        self._nickname=new_nickname



#Main
        
#Excercise 1
        
my_country = Country('France', 'Paris', 67081000, 'Europe')

print(my_country._name)
print(my_country._capital)
print(my_country._population)
print(my_country._continent)

#Excercise 2

my_artist = Artist('Bill Watterson', 'ink and paper', 'cartoons', 'Calvin and Hobbes')
"""
# Taks to show error messages
print(my_artist.__name)
print(my_artist.__medium)
print(my_artist.__style)
print(my_artist.__famous_artwork)"""
#correct references
print(my_artist._Artist__name)
print(my_artist._Artist__medium)
print(my_artist._Artist__style)
print(my_artist._Artist__famous_artwork)


#Excercise 3

my_account = BankAccount()
my_account.set_checking(523.48)
print(my_account.get_checking())
my_account.set_savings(386.15)
print(my_account.get_savings())


#Excercise 4
my_dancer = Dancer("Savion Glover", "American", "tap")
print(my_dancer.name)
print(my_dancer.nationality)
print(my_dancer.style)
my_dancer.name = 'Anna Pavlova'
my_dancer.nationality = 'Russian'
my_dancer.style = 'ballet'
print(my_dancer.name)
print(my_dancer.nationality)
print(my_dancer.style)

#Excercise 5

my_cyclist = Cyclist("Greg LeMond", "American", "Le Montstre")

print(my_cyclist.name)
print(my_cyclist.nationality)
print(my_cyclist.nickname)
my_cyclist.name = "Eddy Merckx"
my_cyclist.nationality = "Belgian"
my_cyclist.nickname = "The Cannibal"
print(my_cyclist.name)
print(my_cyclist.nationality)
print(my_cyclist.nickname)