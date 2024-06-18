new_data = "\nThis is additional data."

# Append data to the file
with open("sample.txt", "a") as file:
    file.write(new_data)

# Verify the appended data
with open("sample.txt", "r") as file:
    contents = file.read()
    print(contents)
