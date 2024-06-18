import json

data = ["apple", "banana", "cherry"]

with open("data.json", "w") as file:
    json.dump(data, file)
