class MyClass:
    def __init__(self, message):
        print("object instatiated!!! Successfully...")
        self.message = message

    def __del__(self):
        print("Destructor called for object with message:", self.message)


obj = MyClass("Hello, world!")

