#Codio 6 - Polymorphism - Exercises

#Exercise 1
#Use the Lottery class to the left as the parent class. 
#Create the PowerBall class as a child class of Lottery. 
#Override the shuffle method so that it returns a list of six random integers between 1 and 99.

import random

class Lottery:
  

  def shuffle(self):
    results = []
    for i in range(5):
      results.append(random.randint(1, 20))
    return results

class Poweball(Lottery):
  def shuffle(self):
    results = []
    for i in range(6):
      results.append(random.randint(1, 99))
    return results

#Exercise 2
#Complete the Airplane and Train classes so that 
#when an instance of each is passed to the passengers 
#function, they will return the total number of passengers on board.

class Airplane:
  def __init__(self, first_class, business_class, coach):
    self.first_class=first_class
    self.business_class = business_class
    self.coach=coach
  def total(self):
    return self.first_class + self.business_class + self.coach
  
class Train:
  def __init__(self, car1, car2, car3, car4, car5):
    self.car1 = car1
    self.car2 = car2
    self.car3 = car3
    self.car4 = car4
    self.car5 = car5
  def total(self):
    return self.car1 + self.car2 + self.car3 + self.car4 + self.car5
  
def passengers(obj):
  print(f'There are {obj.total()} passengers on board.')

#Exercise 3
#Create the class Characters which has the attribute phrases which is a list of strings passed as a parameter. 
#Overload the <, >, and == operators so that you can make comparisons based on the total number of characters in the string.
class Characters:
    def __init__(self, phrases=[]):
        self.phrases = phrases

    def character_count (self):
        chr=0
        for word in self.phrases:
            chr += len(word)
        return chr

    def __lt__(self, other):
        return self.character_count()<other.character_count()
    
    def __gt__(self,other):
      return self.character_count()>other.character_count()
    
    def __eq__(self,other):
      return self.character_count()==other.character_count()
    


#Exercise 4
#Create the Median that has the method calculate_median that calculates the median of the integers passed to the method. 
#Use method overloading so that this method can accept anywhere from two to five parameters.
class Median:
    
    def calculate_median(self, n1, n2, n3=None, n4=None, n5=None):
        self.list=[]
        self.list.append(n1)
        self.list.append(n2)
        if n3 !=None:
            self.list.append(n3)
        if n4 != None:
            self.list.append(n4)
        if n5 != None:
            self.list.append(n5)
        n=len(self.list)
        self.list.sort()
        print(self.list)
        print(n,' numbers in the list')
        
        if n%2==0:
            return (self.list[int(n/2)-1] + self.list[int(n/2)])/2
        else:
            return (self.list[int((n-1)/2)])
        """
        if n==3:
            return self.list[1]
        if n==4:
            return (self.list[1] + self.list[2])/2
        if n==5:
            return (self.list[2])"""

   
   



#Exercise 5

#On Codio

#Main
#Exercise 1  
l=Lottery()
p=Poweball()
print(l.shuffle())
print(p.shuffle())

#Exercise 2

plane=Airplane(4,10,50)
train=Train(12,10,20,40,20)
passengers(plane)
passengers(train)

#Exercise 3

sample_phrases1 = ['cat in the hat', 'green eggs and ham', 'the lorax']
sample_phrases2 = ['the taming of the shrew', 'hamlet', 'othello']

c1 = Characters(sample_phrases1)
c2 = Characters(sample_phrases2)
print(c1 > c2) # prints 'True'
print(c1 < c2) # prints 'False'
print(c1 == c1) # prints 'True'

#Exercise 4

m=Median()
print(m.calculate_median(3, 5, 1, 4, 2))
print(m.calculate_median(8, 6, 4, 2))
print(m.calculate_median(9, 3, 7))
print(m.calculate_median(5, 2))

#Exercise 5 Testing

a= 'Hello'
stars=len(a)
b='*'*stars
print(b)
