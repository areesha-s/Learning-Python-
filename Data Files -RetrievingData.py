# Read data from the file and print each line
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())
