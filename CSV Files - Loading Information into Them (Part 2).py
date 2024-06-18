import csv

additional_data = [
    {"name": "David", "age": 27, "city": "Boston"},
    {"name": "Eve", "age": 31, "city": "Denver"}
]

with open("output.csv", "a", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "city"])
    writer.writerows(additional_data)

# Read and print the contents of the CSV file
with open("output.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
