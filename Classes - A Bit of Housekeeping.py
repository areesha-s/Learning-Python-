class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello,", self.name)

# Creating an instance and calling the method
person1 = Person("John", 30)
person1.greet()
