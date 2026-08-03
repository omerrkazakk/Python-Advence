# #SECTİON 5:ABSTRACT METHODS
#
print("-"*60)
print("Section 5: Abstract Methods")
print("-"*60)

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def run(self):
        pass
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def drink(self):
        pass
    @abstractmethod
    def watch(self):
        pass
class Dog(Animal):
    def run(self):
        print("Dog is running...")
    def eat(self):
        print("Dog is eating...")
    def drink(self):
        print("Dog is drinking...")
    def watch(self):
        print("Dog is watching...")
my_dog = Dog("Charlie")
my_dog.run()
my_dog.eat()
my_dog.drink()
my_dog.watch()