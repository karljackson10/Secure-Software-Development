class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    
  def __repr__(self):
    return f'Dog({self.name}, {self.breed})'
    
dogs = []
dogs.append(Dog('Rocky', 'Pomeranian'))
dogs.append(Dog('Bullwinkle', 'Labrador Retriever'))
print(dogs)
