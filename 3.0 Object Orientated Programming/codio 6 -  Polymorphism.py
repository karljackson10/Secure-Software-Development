#Polymorphism
class Alpha:
    def show(self):
        print("I am from class Alpha")

    def hello(self):
       print('Hello from Alpha')

    
class Bravo(Alpha):
    def show(self):
        print("I am from class Bravo")

    def hello(self):
       print('Hello from Bravo')

class TestClass:
  def sum(self, a = None, b = None, c = None):
    if a is not None and b is not None and c is not None:
      return a + b + c
    elif a is not None and b is not None:
      return a + b
    elif a is not None:
      return a
    else:
      return 0
#A more elegant solutin to the addition problem
class TestClass2:
  def sum(self, a = 0, b = 0, c = 0):
    
      return a + b + c
    
class FinancialAccount:
  def __init__(self, amount):
    self.account = amount
    
  def __add__(self, other):
    return self.account + other.account
    
class BankAccount(FinancialAccount):
  pass

class InvestmentAccount(FinancialAccount):
  pass

my_banking = BankAccount(500)
my_investments = InvestmentAccount(750)
print(my_investments + my_banking)

#main
"""test_object = Alpha()
test_object.show()
test_object.hello()
test_object = Bravo()
test_object.show()
test_object.hello()

obj = TestClass2()
print(obj.sum(1, 2))
print(obj.sum(1, 2, 3))

my_string = "polymorphism"
num1 = 3
num2 = 5
print(num1 * num2)
print(my_string * num1)"""

num1 = 3
num2 = 5
print(int.__mul__(num1, num2))
print(int.__add__(num1, num2))
print(int.__sub__(num1, num2))
print(int.__truediv__(num1, num2))