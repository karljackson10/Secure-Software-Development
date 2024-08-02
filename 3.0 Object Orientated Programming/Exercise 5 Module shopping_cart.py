#shopping_cart
class ShoppingCart:
    def __init__(self):
        'The constructor should not take have any arguments'
        self.items=[]
        self.total=0
    
    def add_item(self,item):
        'Add an item to the shopping cart and then calls the calculate_total method'
        self.items.append(item)
        #print('adding to basket: ',item)
        
        

    def calculate_total	(self):
        'Assigns the total value of the shopping cart to the total attribute'
        self.total = self.get_total(self)
        

    def get_total(self):
        'Returns the total value of the shopping cart'
        #print('Calculating total value of basket')
        total=0
        for item in self.items:
            #print(item)
            total += item.price * item.quantity
            #print('running total =', total)
        self.total=total
        return total

    def get_num_items(self):
        'Returns the number of items in the shopping cart'
        return len(self.items)

    def get_items(self):
        'Returns a list of all of the items in the cart'
        return self.items

    def __str__(self):
        'Returns a human-readable string; see the Expected Output section for the format'
        items = self.get_num_items()
        return 'The cart has %i items for a total of $%.2f ' %(items, self.total)


