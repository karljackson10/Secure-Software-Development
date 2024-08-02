# codio 6 -polymorphism - Lab Challenge

class Chef:
  def __init__(self, name, cuisine, stars):
    self.name = name
    self.cuisine = cuisine
    self.michelin_stars = stars

  def __gt__(self, other):
    if self.michelin_stars> other.michelin_stars:
        return self.name + ' has more Michelin stars than ' + other.name
    else:
        return other.name + ' has more Michelin stars than ' + self.name

  def compare(self, other_chef):
    return self.__gt__(other_chef)
    
#Main
marco = Chef('Marco Pierre White', 'French, British', 3)
rene = Chef('Rene Redzepi', 'Nordic', 2)
print(marco.compare(rene))
print(rene.compare(marco))