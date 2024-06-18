class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Creating an instance and calling the method
rectangle1 = Rectangle(5, 3)
area = rectangle1.calculate_area()
print("Area:", area)
