#parameterized constructor
#constructor
#destructor
class dog() :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print ('hey hello \n my name is',self.name,'\nand my age is ',self.age,'\nand I am a Good',self.__class__.__name__)
    def makeSound(self):
        print("Bouff..baouf.grr")
    def __del__(self):
        print ('This object is being Destructed...\n')

    
class cat() :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print ('hey hello \n my name is',self.name,'\nand my age is ',self.age,'\nand I am a Good',self.__class__.__name__)
    def makeSound(self):
        print("meaww..miww..")
    def __del__(self):
        print ('This object is being Destructed...\n')


a =dog('Moti',15)
a.intro()
a.makeSound()


a =cat('Maauu',15)
a.intro()
a.makeSound()