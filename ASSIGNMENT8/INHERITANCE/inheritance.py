class Animal:
    def m1(self):
        print("Animal")

class Dog(Animal):
    def m1(self):
        print("Dog")

dog = Dog()
dog.m1() 
