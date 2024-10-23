class Person:
    def __init__(self, name, age):
        print("Objrct instatiated")
        self.name = name
        self.age = age
    def hello(self):
        print("hello my name" "is",self.name,"age is ",self.age)
person = Person("Pratik", 20)
person.hello()