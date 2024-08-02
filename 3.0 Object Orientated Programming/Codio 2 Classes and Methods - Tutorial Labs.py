from typing import Any


class Person:
    count=0
    """Represents a generic Person."""
    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        Person.count = Person.count + 1

    def calc_bmi(self):
    
        return (self.weight_in_lbs * 703) / self.height_in_inches ** 2
    
    #Challenge 1
    #Add an instance method called print_self() that, when called, will output the instance object’s first name, last name, weight, height, and BMI. 
    #Call that method and validate the output is correct for each object instance you create.

    def print_self(self):
        print('First name: %s ' %self.first_name)
        print('Last name: %s' %self.last_name)
        print('Weight: %d lbs'%self.weight_in_lbs)
        print('Height: %d inches' %self.height_in_inches)
        print('BMI: %.2f' %self.calc_bmi())
        return
    
    #Challenge 1.2
    #Create another method in your Person class that returns a value 
    #indicating if the person is underweight, good weight, or overweight, according to the CDC ranges. 
    def bmi_indicator(self):
        bmi=self.calc_bmi()
        if bmi>=25:
            indicator = "Overweight"
        elif bmi<18.5:
            indicator = "Underweight"
        else:
            indicator = "Good Weight"


        print('A bmi score of %.2f indicates: %s' %(bmi, indicator))
        return

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    @classmethod
    def print_count(cls,):
        return cls.count
    
    @classmethod
    def print_class(cls,):
        
        attr = (vars(Person))
        for a in attr:
            print(a)
        return


#main
p = Person('Tom', 'Thumb', 150, 62)
p2 = Person('Fred', 'Flint', 225, 57)

print(p.calc_bmi())
print(p2.calc_bmi())
#print(Person.count) - do not call class variables using dot notation - use class methods
print(Person.print_count())
p.print_self()
p.bmi_indicator()
p2.print_self()
p2.bmi_indicator()
#Person.print_attributes
Person.print_class()
