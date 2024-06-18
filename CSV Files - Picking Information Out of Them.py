import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        if int(row[1]) > 30:
            print(row[0])
