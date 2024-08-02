#Protected Variables and Methods
class Phone:
    def __init__(self, make, storage, megapixels, carrier):
        self._make = make
        self._storage = storage
        self._megapixels = megapixels
        self._carrier=carrier
    

class PrivateClass:
    def __init__(self):
        self.__private_attribute = 'I am a private attribute'
    
    def helper_method(self):
        return self.__private_method()

    def __private_method(self):
        return  'I am a private method'

#main
obj = PrivateClass()
print(obj.helper_method())
print(obj.__dict__)
print(obj._PrivateClass__private_method())

#The underscore indicated a private or protected variable or method
#The projected method can not be called from the main program, but can be used within the class 
#print(obj.__private_method)

my_phone = Phone("iPhone", 256, 12, 'Vodafone')


#protected variables in Python are not really protected
#the _ is a convention, not a rule
#variables with an _ can still be used.
print(my_phone._make)
print(my_phone._storage)
my_phone._storage=64
print(my_phone._storage)
print(my_phone._megapixels)


print(my_phone.__dict__)