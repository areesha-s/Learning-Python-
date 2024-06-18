class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def change_length(self, new_length):
        self.length = new_length

# Creating an instance and changing the length
rectangle1 = Rectangle(5, 3)
print("Initial Length:", rectangle1.length)
rectangle1.change_length(10)
print("Updated Length:", rectangle1.length)
