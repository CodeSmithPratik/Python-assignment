#  Implement a class and object with constructor and destructor
#  1) craate simple class
class Student:
    pass



# 2) create a class with constructor and destructor

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Destructor called")

student = Student("John", 20)
print(student.name)
print(student.age)



#  3) create a class with constructor and destructor and add a method to the class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)
        
student = Student("John", 20)
student.display()





#  4) create a class with constructor and destructor and add a method to the class and access the method outside the class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(self.name, self.age)

student = Student("John", 20)
student.display()






# 5) write simple mathematical operations using class

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

math = Math(10, 20)
print(math.add())




# 6) create a class with constructor and destructor and add a method to the class and access the method outside the class and add a method to the class and access the method outside the class

class MyClass:
    def __init__(self, name):
        # Constructor: 
        self.name = name
        print(f"Object {self.name} created.")

    def greet(self):
        # Method to greet the user
        return f"Hello, {self.name}!"

    def __del__(self):
        # Destructor: 
        print(f"Object {self.name} destroyed.")

obj = MyClass("Alice")

greeting = obj.greet()
print(greeting)

def say_goodbye(self):
    return f"Goodbye, {self.name}!"

MyClass.say_goodbye = say_goodbye


goodbye_message = obj.say_goodbye()
print(goodbye_message)

del obj
