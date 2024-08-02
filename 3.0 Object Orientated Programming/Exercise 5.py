#Exercise 5

from item import Item
from shopping_cart import ShoppingCart

#print('Adding Items')
item1 = Item('milk', 1.5, 1)
item2 = Item('apple', 5, 0.75)
item3 = Item('bread', 2, 2.25)
#print()

cart = ShoppingCart()
cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)
#print('total value')
print(cart.get_total())
#print()

#print('number of items')
print(cart.get_num_items())
#print()
print(cart)
print(cart.get_items())