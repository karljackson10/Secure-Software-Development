class Dog:
    def __init__(self, name, breed):
        self.name=name
        self.breed=breed

    def __repr__(self):
        return '\nDog( %s, %s)' %(self.name, self.breed)

#Main
names=['Marceline', 'Cajun', 'Daisy', 'Rocky', 'Bella']
breeds=['German Shepherd','Belgian Malinois','Border Collie','Golden Retriever','Irish Setter']
dogs=[]

for i in range(5):
    dog=Dog(names[i], breeds[i])
    dogs.append(dog)

print(repr(dogs))
