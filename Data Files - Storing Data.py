
data = "Hello, Areesha!\nThis is a sample text file."

# Write data to the file
with open("sample.txt", "w") as file:
    file.write(data)

# Open and read the contents of the file
with open("sample.txt", "r") as file:
    contents = file.read()
    print(contents)
