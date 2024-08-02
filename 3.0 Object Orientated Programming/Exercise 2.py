#Exercise 2
class Band:
  def __init__(self, name, genre, members):
    self.name = name
    self.genre = genre
    self.members = members

  def __str__(self):
    return('%s is a %s band.' %(self.name, self.genre))    
  
  def __repr__(self):
    return f'Band({self.name}, {self.genre}, {self.members})'



#Main
dead = Band('The Grateful Dead', 'rock\'n roll', ['Jerry', 'Bob', 'Mickey', 'Bill', 'Phil', 'Pigpen'])
print(dead)
print(repr(dead))