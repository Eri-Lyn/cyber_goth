"""
ASSIGNMENT 2 -- CLASSES
````````````````````````````````````````````````````````````````````````````````````````
1. Create a class called 'Animal'. It should have the following member variables:
   name  (ex. Cow)
   color (ex. Brown)
   sound (ex. Moo)
   type  (ex. Mammal)

2. Make a LIST of this Animal type. This list should be iterable and callable. In other words, if you return
   animalList[2], it should neatly output those member variables in some fashion. Likewise, you need a way
   to sort this class (which I will leave up to you). Attempting to call sort(animalList) should return a list
   of Animal objects organized by X member variable.

"""

from operator import attrgetter

class Animal:
   def __init__ (self,name,color,sound,type):
      self.name = name
      self.color = color
      self.sound = sound
      self.type = type
      
   def __str__(self):
      return f"{self.name} is a {self.color} color"
   
   def speak(self, sound):
      return f"{self.name} says {sound}"

cow = Animal("cow","brown","moo","mammal")
dog = Animal("dog","black","bark","mammal")
rooster = Animal("rooster","red","crow","reptile")
horse = Animal("horse","tan","neigh","mammal")
cat = Animal("cat","white","meow","mammal")
bird = Animal("bird","red","chirp","reptile")
cat1 = Animal("cat","black","meow","mammal")

#animalList = ['cow','dog','rooster','horse','cat']


animalList = []
# animalList.append(Animal("cow","brown","moo","mammal"))
# animalList.append(Animal("dog","black","bark","mammal"))
# animalList.append(Animal("rooster","red","crow","reptile"))
# animalList.append(Animal("horse","tan","neigh","mammal"))
# animalList.append(Animal("cat","white","meow","mammal"))
# animalList.append(Animal("cat","black","meow","mammal"))

animalList.append(bird)
animalList.append(cow)
animalList.append(dog)
animalList.append(rooster)
animalList.append(horse)
animalList.append(cat)
animalList.append(cat1)

print("Sort by...")
animalList.sort(key=attrgetter('name'))

print("...then show all animals and color:")
for animal in animalList:
   print("%s: \"%s\"" % (animal.name, animal.color))

look = input('What animal do you want? ')
for animal in animalList:
   if look in animal.name:
      #print("%s: \"%s\" \"%s\" \"%s\"" % (animal.name, animal.color, animal.sound, animal.type))
      print(animal.name + ' says ' + animal.sound)


