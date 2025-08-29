# POLYMORPHISM

class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

class Horse(Animal):
    def make_sound(self):
        print("Horse neighs")