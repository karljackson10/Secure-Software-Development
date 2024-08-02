#Item Class
class Item:
    def __init__(self, name, price=0, quantity=0):
        self.name=name
        self.price=price
        self.quantity=quantity
        self.subtotal=self.get_subtotal()
    
    def __repr__(self):
        return 'Item(%s, %g, %g, %g)' %(self.name, self.price, self.quantity, self.subtotal)
    
    def calculate_subtotal(self):
        return round(self.price*self.quantity,2)
    

    def get_subtotal(self):
        return self.calculate_subtotal()