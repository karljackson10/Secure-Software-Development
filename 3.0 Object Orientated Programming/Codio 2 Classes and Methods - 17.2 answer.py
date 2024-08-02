class Kangaroo:
    """Represents a kangaroo amnd the contents of a pouch"""

    def __init__(self, name, pouch_contents=None):
        """Initializes a kangaroo object.

                pouch: list
        """
        self.name = name
        if pouch_contents == None:
            pouch_contents = []
        self.pouch_contents = pouch_contents
        return
    
    def __str__(self):
        """Returns a string representation of the kangaroo object and contents of pouch."""
        text=[self.name + ' has pouch contents: ']
        for item in self.pouch_contents:
            s =object.__str__(item) + ' '
            text.append(s)
        return '\n'.join(text)

    def put_in_pouch(self,item):
        """Adds a new item to the pouch contents"""
        self.pouch_contents.append(item)
        return
        

#main

kanga= Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)
print(roo)
