person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "hobbies": ["reading", "traveling", "swimming"]
}
print(person)
people = [
    {"first_name": "John", "last_name": "Doe"},
    {"first_name": "Jane", "last_name": "Smith"},
    {"first_name": "Emily", "last_name": "Jones"}
]
print(people)

for person in people:
    print(person["first_name"])
