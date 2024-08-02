#Encapsulation - Getters and Starters

class Phone:
  def __init__(self, model, storage, megapixels):
    self.__model = model
    self._storage = storage
    self._megapixels = megapixels
    
  def get_model(self):
    return self.__model
  
  def set_model(self, new_model):
    self.__model = new_model

class TestClass:
  def __init__(self, num1, num2):
    self._num1 = num1
    self._num2 = num2
    self._sum = 0
    
  def get_num1(self):
    return self._num1
  
  def set_num1(self, new_value):
    self._num1 = new_value
    
  def get_num2(self):
    return self._num2
  
  def set_num2(self, new_value):
    self._num2 = new_value
    
  def get_sum(self):
    return self._sum
  
  def set_sum(self, new_value):
    self._sum = new_value

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    #@property
    def get_age(self):
      return self._age
    
    #@age.setter
    def set_age(self, new_age):
        if type(new_age) != int or new_age<0:
           raise TypeError('Age must be a positive whole number')
        self._age = new_age


    #@property  
    def get_name(self):
        return self._name
    
    #@name.setter
    def set_name(self, new_name):
        if type(new_name) != str:
           raise TypeError('Names must be expressed as a string')
        self._name = new_name
  
    #Note the getter must come before the setter when using property
    name= property(get_name, set_name)
    age = property(get_age, set_age)
    
    


c = Person("Calvin", 6)
print(c.name)
print(c.age)
c.age =17
c.name = 'False'
print(c.name)
print(c.age)




"""#Main
obj = TestClass(5, 7)
print(obj.get_num1())
print(obj.get_num2())
#obj.set_sum(obj.get_num1() + obj.get_num2())
obj.sum(obj.num1 + obj.num2)
print(obj.get_sum())




  
my_phone = Phone("iPhone", 256, 12)
#print(my_phone.__model)
print(my_phone.get_model())
print(my_phone._storage)
my_phone.set_model("Galaxy S20")
print(my_phone.get_model())"""