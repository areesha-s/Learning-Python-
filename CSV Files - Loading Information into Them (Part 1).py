import csv

# Data to be written to the CSV file
data = [
    {"name": "Alice", "age": 28, "city": "Seattle"},
    {"name": "Bob", "age": 32, "city": "San Francisco"},
    {"name": "Charlie", "age": 29, "city": "Austin"}
]

# Write data to the CSV file
with open("output.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(data)

# Read and print the contents of the CSV file
with open("output.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
