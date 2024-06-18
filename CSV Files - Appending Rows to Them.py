import csv

new_row = {"name": "Frank", "age": 26, "city": "Miami"}

with open("output.csv", "a", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "city"])
    writer.writerow(new_row)

# Verify the appended row
with open("output.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
