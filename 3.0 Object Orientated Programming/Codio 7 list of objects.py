# list of objects
from csv import reader
from app import App

apps = []

path='C:/Users/User/OneDrive/1. University of Essex/3.0 Object Orientated Programming/Codio 7 - Advanced Topics/'

with open(path+'app.csv') as csv_file:
  csv_reader = reader(csv_file, delimiter=',')
  next(csv_reader)
  for name, description, category in csv_reader:
    apps.append(App(name, description, category))
    
for app in apps:
  app.display()
print('\n The 3rd App in the list')
apps[2].display()

print('\n All social media apps')
for app in apps:
    if app.category =='social media':
        app.display()
    