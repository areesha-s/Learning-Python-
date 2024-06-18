# Create a sample text file
with open("sample.txt", "w") as file:
    file.write("Hello, world!\nThis is a sample text file.")

# Open and read the contents of the file
with open("sample.txt", "r") as file:
    contents = file.read()
    print(contents)
