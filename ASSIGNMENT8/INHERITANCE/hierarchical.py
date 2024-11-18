class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):  
    def bark(self):
        return "Bark"

class Cat(Animal):
    def meow(self):
        return "Meow"

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())
print(dog.bark())
print(cat.meow())
