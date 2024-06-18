# Add a method to the Dog class that prints the dog's details.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def display_info(self):
        print("Name:", self.name)
        print("Breed:", self.breed)

# Creating an instance and calling the method
dog1 = Dog("Buddy", "Labrador")
dog1.display_info()
