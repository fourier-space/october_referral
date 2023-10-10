"""
question4.py - classes and UML

The image uml.png contants a UML diagram for a set of related classes.

In this scheme, Dog and Cat are classes.
Dogs and Cats are both Animals -
  they implement the methods and properties of the Animal interface.
I.e. all Dogs and Cats have a fleas property and a describe method, etc.
(Animal is an interface and doesn't appear itself in the code)

Methods:
describe() - returns a string value describing the appearance of the animal,
             including whether the animal has fleas,
             whether they are holding a toy,
             And for a cat, the fur type - or for a dog, the breed.
             e.g.
             "A tabby cat with fleas holding a ball"
vocalise() - prints to the console the noise the animal makes,
             e.g.
             "Woof" or "Miaow"
clean()    - if the animal has fleas, fleas is set to false.

Cats are constructed, with __init__ with a fur type ("black", "tabby", etc.)
Dogs are constructed with a breed ("labrador", "poodle", etc.)

a) Implement both Cat and Dog classes.

b) the Sphynx_cat is a class that extends Cat - Implement Sphynx_cat.
    It's constructor doesn't take a fur_type,
    and this property on Cat is set to None,
    Sphynx_cat has its own method sphynx_purr(),
    which prints "prrrrrr" to the console.

c) implement a vet_surgery(animal) function.
    This will take an animal as an argument.
    If the animal has fleas,
        * call the clean() method
        * If the animal is not holding a toy, set toy to "Vet sticker"
    Otherwise,
        * call the vocalise() method

TOTAL POINTS AVAILABLE: 5 

Code Functionality (5)
a) 2 POINTS
b) 1 POINT
c) 2 POINTS
"""

class Cat():
    def __init__(self):
        pass

class Dog():
    def __init__(self):
        pass

def vet_surgery(animal):
    pass
