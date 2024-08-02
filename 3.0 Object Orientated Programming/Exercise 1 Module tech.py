class Phone:
  def __init__(self, name, color, storage):
    self.name = name
    self.color = color
    self.storage = storage
    
  def __str__(self):
    return f'A {self.color} {self.name} with {self.storage}GB of storage.'
  
class Laptop:
  def __init__(self, name, size, storage):
    self.name = name
    self.size = size
    self.storage = storage
    
  def __str__(self):
    return f'{self.size}-inch {self.name} with {self.storage}GB of storage.'