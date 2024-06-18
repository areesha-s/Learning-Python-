import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        print("Name:", row[0], "| Age:", row[1])
