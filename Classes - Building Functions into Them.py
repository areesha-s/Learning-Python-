class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)

# Creating an instance and calling the method
book1 = Book("Python Programming", "John Doe")
book1.display_info()
