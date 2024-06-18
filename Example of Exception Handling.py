def read_file(filename):
    try:
        with open(filename, "r") as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None

# Test the function
print(read_file("sample.txt"))  # Replace with an actual existing file
print(read_file("nonexistent_file.txt"))  # Should print the error message
